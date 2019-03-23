# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import models, fields, api

class Website(models.Model):
    _inherit = "website" 
    
    fb_pixel = fields.Char('Facebook Pixel ID')

class Page(models.Model):

    _inherit = "website.page"
    
    fbq_ids = fields.One2many('website.facebook_pixel', 'page_id', string="Pixel Events")
    fb_pixel = fields.Char('Facebook Pixel ID')