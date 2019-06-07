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
    platform = fields.Selection(ADS_PLATFORMS, 'Platform', required=True)
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
    buyer_persona_id = fields.Many2one('lean_marketing.buyer_persona', 'Buyer Persona')
    color = fields.Integer('Kanban Color Index')
    

    @api.one
    def  write(self, values): 
        buyer_persona_obj = self.env['lean_marketing.buyer_persona']
        buyer_persona_ids = buyer_persona_obj.search([('audience_id', '=', self.id)])     
        if len(buyer_persona_ids)>=1:
            for i in  buyer_persona_obj.browse(buyer_persona_ids):   
                i.id.audience_id = None                     
        res = super(Audience, self).write(values)   
        audience_ids = self.search([('buyer_persona_id', '=', self.buyer_persona_id.id)]) 
        if  len(audience_ids) >= 1:
            for i in self.browse(audience_ids): 
                i.id.buyer_persona_id  = None
        buyer_persona = buyer_persona_obj.browse([self.buyer_persona_id])
        if len(buyer_persona) == 1:
            buyer_persona.id.audience_id = self.id   
            return res
        else:
            res = False
    
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
    
    
    
    

    
    