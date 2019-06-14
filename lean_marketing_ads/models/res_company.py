# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import models, fields, api, tools

class ResCompany(models.Model):

    _inherit = 'res.company'
    
    fb_business_id = fields.Char('Business ID', required=True, translate=True)
    fb_access_token = fields.Char('Access Token', required=True, translate=True)
    fb_app_id = fields.Char('App Id', required=True, translate=True)
    fb_app_secret = fields.Char('Name', required=True, translate=True)
    
    
    