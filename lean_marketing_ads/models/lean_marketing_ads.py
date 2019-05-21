 # -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#
from odoo import models, fields, api

ADS_PLATFORMS = [
    ('facebook', 'Facebook'),
    ('google', 'Google'), 
    ('twitter','Twitter'),
    ('bing','Bing'),
    ('linkedin','LinkedIn'),
    ('wase','Wase')
    ]

class AddsCampaign(models.Model):
    _name = 'lean_marketing.adds_campaign'
    _description = 'Ads Campaign'
    
    name = fields.Char('Name', required=True)
    active = fields.Boolean('Active', default=True, track_visibility=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('done', 'Completed'),
        ('cancel', 'Cancelled'),
        ],
        string='Status', default='draft', required=True, copy=False, track_visibility='onchange', group_expand='_expand_states')
    platform = fields.Selection(ADS_PLATFORMS, 'Platform')
    campaign_id = fields.Many2one('utm.campaign', 'campaign_id',
        required=True, ondelete='cascade',  help="This name helps you tracking your different campaign efforts, e.g. Fall_Drive, Christmas_Special")
    
    def _expand_states(self, states, domain, order):
        return ['draft', 'active', 'done', 'cancel']

class Audience(models.Model):
    _name = 'lean_marketing.adds_campaign.audience'
    _description = 'Audience'
    
    name = fields.Char('Name', required=True)
    
    