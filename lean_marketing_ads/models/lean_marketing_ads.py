 # -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#
from odoo import models, fields, api

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.business import Business

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
    type = fields.Selection([('owned', 'Owned'),('shared', 'Shared')], string='Type', default='owned', readonly=True)
    fb_id = fields.Char(string='ID', readonly=True) 
    account_status = fields.Selection(ACCOUNT_STATUS, string='Status', readonly=True)
    disable_reason = fields.Selection(DISABLE_REASON, string='Disable Reason', readonly=True)
    age = fields.Float('Age', readonly=True)
    currency = fields.Char('Currency', size=3, readonly=True)
    balance = fields.Float('Spend', readonly=True)
    active_campaigns = fields.Integer('Active Campaigns', readonly=True)
    company_id = fields.Many2one('res.company', string='Company', index=True, default=lambda self: self.env.user.company_id.id)
    color = fields.Integer('Kanban Color Index')
    
    def update_ad_account(self):
        api_access = self.env['res.company'].sudo().search_read([],['id', 'fb_business_id', 'fb_access_token', 'fb_app_id', 'fb_app_secret'])
        obj_ad_accounts = self.env['lean_marketing.ad_account'].search_read([],['id', 'account_id'])
        ad_accounts = []
        for bsn in api_access:
            if bsn['fb_business_id'] != None and bsn['fb_business_id'] != None and bsn['fb_access_token'] != None and bsn['fb_app_id'] != None and bsn['fb_app_secret'] != None:
                FacebookAdsApi.init(bsn['fb_app_id'], bsn['fb_app_secret'], bsn['fb_access_token'] )
                my_business = Business(bsn['fb_business_id'])
                fields = ['id', 'account_id', 'name','currency', 'age','balance','disable_reason', 'account_status']
                accounts = my_business.get_owned_ad_accounts(fields=fields)
                for account in accounts:
                    data = {}
                    data['name'] = account['name']
                    data['account_id'] = account['account_id']
                    data['fb_id'] = account['id']
                    data['account_status'] = account['account_status']
                    data['disable_reason'] = account['disable_reason']
                    data['age'] = account['age']
                    data['currency'] = account['currency']
                    data['balance'] = account['balance']
                    data['company_id'] = bsn['id']
                    ad_accounts.append(account)
        for account in ad_accounts:
            
            
        _logger.warn('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh{}'.format(ad_accounts))
        return True
    

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
    
    
    
    

    
    