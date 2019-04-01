# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models

class UtmTerm(models.Model):
    _name = 'utm.term'
    _description = 'UTM Term'

    name = fields.Char(string='Term Name', required=True, translate=True)
    
class UtmContent(models.Model):
    _name = 'utm.content'
    _description = 'UTM Content'

    name = fields.Char(string='Content Name', required=True, translate=True)