# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'
    
    touchpoint_hub = fields.Boolean(string='Touchpoints Hub', default=False,
                               help="Check this box if this locationt is a touchpoint.")
    evangelist = fields.Boolean(string='Is a Evangelist', default=False,
                               help="Check this box if this partner is a brand evangelist.")
    heater = fields.Boolean(string='Is a Heater', default=False,
                               help="Check this box if this partner is a brand heater.")
    brand_advocacy = fields.Selection([('does_not_apply','Does not apply'), ('employee_advocate','Employee Advocate'), ('customer_advocate','Customer Advocate'), ('ambassador','Ambassador'), ('influencer','Influencer')], default='does_not_apply', group_expand='_expand_brand_advocacy')

    def _expand_brand_advocacy(self, brand_advocacy, domain, order):
        return ['employee_advocate', 'customer_advocate', 'ambassador', 'influencer']
    