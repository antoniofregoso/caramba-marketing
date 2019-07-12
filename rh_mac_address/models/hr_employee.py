# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = "hr.employee"
    _description = "Employee"
    
    mac_address = fields.Char(string="Mac Address", help="mac address of the wifi device.", copy=False)
    
    
    
    