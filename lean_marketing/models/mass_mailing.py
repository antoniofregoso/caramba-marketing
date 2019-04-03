# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models, tools

class MassMailingCampaign(models.Model):
    _inherit = 'mail.mass_mailing.campaign'
    
    plan_id = fields.Many2one('lean_marketing.plan', string='Plan', ondelete='cascade')


    
    