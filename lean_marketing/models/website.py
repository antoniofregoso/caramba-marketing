# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#
from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)

class Website(models.Model):
    _inherit = ['website']
    
    def get_utmContent(self, utmContent):
        content_id=  self.env['utm.content'].sudo().search_read([('name','=',utmContent)], ['name'])
        if content_id:
            return content_id[0]['id']
        else:
            return 0
    
    def get_utmTerm(self, utmTerm):
        term_id=  self.env['utm.term'].sudo().search_read([('name','=',utmTerm)], ['name'])
        if term_id:
            return term_id[0]['id']
        else:
            return 0