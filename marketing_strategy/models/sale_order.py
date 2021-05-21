# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#
from odoo import api, fields, models


class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit  = "sale.order"
    
    content_id = fields.Many2one('utm.content', 'Content',
                                  help="Identifies search terms.")
    term_id = fields.Many2one('utm.term', 'Term',
                                  help="Identifies what specifically was clicked to bring the user to the site, such as a banner ad or a text link. It is often used for A/B testing and content-targeted ads.")
    
