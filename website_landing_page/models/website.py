# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import models, fields

class Page(models.Model):

    _inherit ='website.page'
    
    landing_page = fields.Boolean('Is landing page', default=False, help='Hidden menu, footer and home link.')

