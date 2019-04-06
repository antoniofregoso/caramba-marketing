# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models

class UtmTerm(models.Model):
    _name = 'utm.term'
    _description = 'UTM Term'

    name = fields.Char(string='Term Name', required=True, translate=True)
    
class UtmContent(models.Model):
    _name = 'utm.content'
    _description = 'UTM Content'

    name = fields.Char(string='Content Name', required=True, translate=True)
    
class UtmCampaign(models.Model):
    # OLD crm.case.resource.type
    _name = 'utm.campaign'
    _inherint = 'utm.campaign'
    
    plan_id = fields.Many2one('lean_marketing.plan')
    
    
class UtmSource(models.Model):
    _name = 'utm.source'
    _inherint  = 'utm.source'
    
    hub_id = fields.Many2one('res.partner', string='Touchpoints hub', domain=[('touchpoint_hub','=',True)])
    
class UtmMedium(models.Model):
    _name = 'utm.medium'
    _inherint  = 'utm.medium'
    
    touchpoint_id = fields.Many2one('lean_marketing.touchpoint', string='Touchpoints hub')