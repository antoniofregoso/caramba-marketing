# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import models, fields, api

class Plan(models.Model):
    _name = 'lean_marketing.plan'
    _inherit ='lean_marketing.plan'
    
    buyers_persona_ids = fields.Many2many('lean_marketing.buyer_persona', 'lean_marketing_plan_buyer_persona_rel', 'plan_id', 'buyer_persona_id', string='Buyers Persona')