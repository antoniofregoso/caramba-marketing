# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'
    
    influencer = fields.Boolean(string='Is a Influencer', default=False,
                               help="Check this box if this contact is a influencer.")
    evangelist = fields.Boolean(string='Is a Evangelist', default=False,
                               help="Check this box if this contact is a brand evangelist.")
    touchpoint_hub = fields.Boolean(string='Is a Touchpoints Hub', default=False,
                               help="Check this box if this locationt is a touchpoint.")


