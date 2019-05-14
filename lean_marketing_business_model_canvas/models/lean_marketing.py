# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models


    
class KeyResource(models.Model):

    _name = "lean_marketing.key_resources"
    _description = "Key Resource"

    name = fields.Char('Tag Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]
    
class CustomerRelationship(models.Model):

    _name = "lean_marketing.customer_relationship"
    _description = "Customer Relationship"

    name = fields.Char('Tag Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]
    
    

class Plan(models.Model):
    _name = 'lean_marketing.plan'
    _inherit = 'lean_marketing.plan'
    
    def _get_value_proposition(self):
        return False
       
    key_partners_ids = fields.Many2many('res.partner', 'lean_marketing_plan_res_partner_rel','plan_id', 'res_partner_id', string='Key Partners') 
    key_activities_ids = fields.Many2many('project.task', 'lean_marketing_plan_project_task_rel', 'plan_id', 'task_id', string='Key Activities')
    key_resources_ids = fields.Many2many('lean_marketing.key_resources', 'lean_marketing_key_resources_rel', 'plan_id', 'tag_id', string='Tags')
    value_propositions = fields.Many2many('lean_marketing.solution.gain_creator', 'lean_marketing_plan_solution_gain_greator_rel', 'plan_id','gain_creator_id', string='Gain Creator', default=_get_value_proposition)
    customer_relationships_ids = fields.Many2many('lean_marketing.customer_relationship', 'lean_marketing_plan_customer_relationship_rel', 'plan_id', 'customer_relationship_id', string='Tags')
    cost_structure_ids = fields.Many2many('product.category', 'lean_marketing_plan_cost_structure_rel', 'plan_id', 'product_category_id', string="Cost Structure")
    revenue_streams_ids = fields.Many2many('product.category','lean_marketing_revenue_stream_rel', 'plan_id', 'product_category_id', string="Revenue Streams")
    
    