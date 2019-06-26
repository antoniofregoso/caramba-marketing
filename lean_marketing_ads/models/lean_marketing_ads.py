 # -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#
from odoo import models, fields, api


import logging
_logger = logging.getLogger(__name__)

ADS_PLATFORMS = [
    ('facebook', 'Facebook'),
    ('google', 'Google'), 
    ('twitter','Twitter'),
    ('bing','Bing'),
    ('linkedin','LinkedIn'),
    ('wase','Wase'),
    ('whatsapp','WhatsApp')
    ]

ACCOUNT_STATUS = [
    (1,'Active'), 
    (2,'Disabled'), 
    (3,'Unsettled'), 
    (7,'Pending Risk Review'), 
    (8,'Pending Settlement'), 
    (9,'In Grace Period'), 
    (100,'Pending Closure'), 
    (101,'Closed'), 
    (201,'Any Active'), 
    (202,'Any Closed')]

DISABLE_REASON = [
    (0, 'NONE'),
    (1, 'ADS_INTEGRITY_POLICY'),
    (2, 'ADS_IP_REVIEW'),
    (3, 'RISK_PAYMENT'),
    (4, 'GRAY_ACCOUNT_SHUT_DOWN'),
    (5, 'ADS_AFC_REVIEW'),
    (6, 'BUSINESS_INTEGRITY_RAR'),
    (7, 'PERMANENT_CLOSE'),
    (8, 'UNUSED_RESELLER_ACCOUNT'),
    (9, 'UNUSED_ACCOUNT')
    ]


#Default Value last_30d
DATE_PRESET = [
    ('today,','Today'),
    ('yesterday','Yesterday'),
    ('this_month','This month'),
    ('last_month','Last month'),
    ('this_quarter','This quarter'),
    ('lifetime,','Life time'),
    ('last_7d,','Last 7 days'),
    ('last_14d,','Last 14 days'),
    ('last_28d,','Last 28 days'),
    ('last_30d','Last 30 days'),
    ('last_90d','Last 90 Days'),
    ('last_week_mon_sun','Last week monday to sunday'),
    ('last_week_sun_sat,','Last week sunday to saturday'),
    ('last_quarter','Last quarter'),
    ('last_year','Last year'),
    ('this_week_mon_today','This week monday to tuday'),
    ('this_week_sun_today','This week sunday to today'),
    ('this_year','This year')
    ]



class AdAccount(models.Model):
    _name = 'lean_marketing.ad_account'
    _description = 'Ad Account'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string='Name', required=True)
    account_id = fields.Char(string='Account ID', readonly=True) 
    type = fields.Selection([('owned', 'Owned'),('shared', 'Shared')], string='Type')
    fb_id = fields.Char(string='ID', readonly=True) 
    account_status = fields.Selection(ACCOUNT_STATUS, string='Status', readonly=True)
    disable_reason = fields.Selection(DISABLE_REASON, string='Disable Reason', readonly=True)
    age = fields.Float('Age', digits=10, readonly=True)
    currency = fields.Char('Currency', size=3, readonly=True)
    balance = fields.Float('Spend', readonly=True)
    active_campaigns = fields.Integer('Active Campaigns', readonly=True)
    company_id = fields.Many2one('res.company', string='Company', index=True, default=lambda self: self.env.user.company_id.id)
    color = fields.Integer('Kanban Color Index')
    
    
    
    @api.multi
    def read(self, fields=None, load='_classic_read'):
        #Update ad account

        """ read([fields])

        Reads the requested fields for the records in ``self``, low-level/RPC
        method. In Python code, prefer :meth:`~.browse`.

        :param fields: list of field names to return (default is all fields)
        :return: a list of dictionaries mapping field names to their values,
                 with one dictionary per record
        :raise AccessError: if user has no read rights on some of the given
                records
        """
        # check access rights
        self.check_access_rights('read')
        fields = self.check_field_access_rights('read', fields)

        # split fields into stored and computed fields
        stored, inherited, computed = [], [], []
        for name in fields:
            field = self._fields.get(name)
            if field:
                if field.store:
                    stored.append(name)
                elif field.base_field.store:
                    inherited.append(name)
                else:
                    computed.append(name)
            else:
                _logger.warning("%s.read() with unknown field '%s'", self._name, name)

        # fetch stored fields from the database to the cache; this should feed
        # the prefetching of secondary records
        self._read_from_database(stored, inherited)

        # retrieve results from records; this takes values from the cache and
        # computes remaining fields
        self = self.with_prefetch(self._prefetch.copy())
        data = [(record, {'id': record._ids[0]}) for record in self]
        use_name_get = (load == '_classic_read')
        for name in (stored + inherited + computed):
            convert = self._fields[name].convert_to_read
            # restrict the prefetching of self's model to self; this avoids
            # computing fields on a larger recordset than self
            self._prefetch[self._name] = set(self._ids)
            for record, vals in data:
                # missing records have their vals empty
                if not vals:
                    continue
                try:
                    vals[name] = convert(record[name], record, use_name_get)
                except:
                    vals.clear()
        result = [vals for record, vals in data if vals]
        _logger.warn('********************************************************{}'.format(self.env.user.company_id.name))
        return result
 

class AdsCampaign(models.Model):
    _name = 'lean_marketing.ads_campaign'
    _description = 'Ads Campaign'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char('Name', required=True)
    active = fields.Boolean('Active', default=False)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('done', 'Completed'),
        ('cancel', 'Cancelled'),
        ],
        string='Status', default='draft', required=True, copy=False, track_visibility='onchange', group_expand='_expand_states')
    platform = fields.Selection(ADS_PLATFORMS, 'Platform', required=True, default='facebook')
    campaign_id = fields.Many2one('utm.campaign', 'Campaign',
        required=True, ondelete='cascade',   help=" Campaign")
    color = fields.Integer('Kanban Color Index')
    
    def _expand_states(self, states, domain, order):
        return ['draft', 'active', 'done', 'cancel']
    
   
    

class Audience(models.Model):
    _name = 'lean_marketing.ads_campaign.audience'
    _description = 'Audience'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string='Name', required=True)
    color = fields.Integer('Kanban Color Index')
    buyer_persona_id = fields.Many2one('lean_marketing.buyer_persona', 'Buyer Persona')
    res_company_id = fields.Many2one('res_company', 'Business')
    platform = fields.Selection(ADS_PLATFORMS, 'Platform', required=True, default='facebook')
    


    
class AdsGroup(models.Model):
    _name = 'lean_marketing.ads_campaign.ads_group'
    _description = 'Ads Group'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char('Name', required=True)
    active = fields.Boolean('Active', default=False)
    ads_campaign_id = fields.Many2one('lean_marketing.ads_campaign', 'Campaign', domain=['|',('active','=',True),('active','=', False)])
    audience_id = fields.Many2one('lean_marketing.ads_campaign.audience', 'Audience')
    color = fields.Integer('Kanban Color Index')
    
class Ad(models.Model):
    _name = 'lean_marketing.ads_campaign.ad'
    _description = 'Ad'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char('Name', required=True)
    active = fields.Boolean('Active', default=False)
    ads_group_id = fields.Many2one('lean_marketing.ads_campaign.ads_group', required=True, domain=['|',('active','=',True),('active','=', False)])
    color = fields.Integer('Kanban Color Index')
    
class BuyerPersona(models.Model):
    _inherit = "lean_marketing.buyer_persona"
    
    audience_id = fields.Many2one('lean_marketing.ads_campaign.audience', 'Audience')
    
    
    
    

    
    