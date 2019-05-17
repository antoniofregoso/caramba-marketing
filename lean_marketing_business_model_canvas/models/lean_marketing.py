# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)
    
class KeyResource(models.Model):

    _name = "lean_marketing.key_resources"
    _description = "Key Resource"

    name = fields.Char('Tag Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]
    
class KeyResourceFinancial(models.Model):

    _name = "lean_marketing.key_resources_financial"
    _description = "Key Financial Resource"

    name = fields.Char('Tag Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]
    
class KeyResourceIntellectual(models.Model):

    _name = "lean_marketing.key_resources_intellectual"
    _description = "Key Intellectual Resource"

    name = fields.Char('Tag Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]
    
class CustomerChannels(models.Model):

    _name = "lean_marketing.channels"
    _description = "Channels"

    name = fields.Char('Tag Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]
    

    
    

class Plan(models.Model):
    _name = 'lean_marketing.plan'
    _inherit = 'lean_marketing.plan'
       
    key_partners_ids = fields.Many2many('res.partner', 'lean_marketing_plan_res_partner_rel','plan_id', 'res_partner_id', string='Key Partners') 
    key_activities_ids = fields.Many2many('project.task', 'lean_marketing_plan_project_task_rel', 'plan_id', 'task_id', string='Key Activities')
    key_human_resources_ids = fields.Many2many('res.partner', 'lean_marketing_plan_hr_res_partner_rel','plan_id', 'res_partner_id', string='Human Resources') 
    key_physical_resource_ids = fields.Many2many('product.product', 'lean_marketing_plan_product_rel','plan_id', 'product_id', string='Physical Resources') 
    key_resources_ids = fields.Many2many('lean_marketing.key_resources', 'lean_marketing_key_resources_rel', 'plan_id', 'tag_id', string='Tags')
    key_resources_financial_ids = fields.Many2many('lean_marketing.key_resources_financial', 'lean_marketing_key_resources_financial_rel', 'plan_id', 'tag_id', string='Tags')
    key_resources_intellectual_ids = fields.Many2many('lean_marketing.key_resources_intellectual', 'lean_marketing_key_resources_intellectual_rel', 'plan_id', 'tag_id', string='Tags')
    value_propositions = fields.Many2many(related='solution_id.gain_creator_ids')
    channel_ids = fields.Many2many('lean_marketing.channels', 'lean_marketing_plan_channel_rel', 'plan_id', 'channel_id', string='Tags')
    cost_structure_ids = fields.Many2many('account.account', 'lean_marketing_plan_cost_structure_rel', 'plan_id', 'account_id', string="Cost Structure")
    revenue_streams_ids = fields.Many2many('account.account','lean_marketing_revenue_stream_rel', 'plan_id', 'account_id', string="Revenue Streams")
    

    
    
    