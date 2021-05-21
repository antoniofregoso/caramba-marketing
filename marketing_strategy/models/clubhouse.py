# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models, tools, _




class ClubhouseClub(models.Model):
    _name = "marketing_strategy.clubhouse.club"
    _description = "Clubhouse Club"
    _order = "name"

    name = fields.Char('Name', required=True)


class ClubhouseRoom(models.Model):
    _name = "marketing_strategy.clubhouse.room"
    _description = "Clubhouse Room"
    _order = "name"

    name = fields.Char('Name', required=True)
    club_id = fields.Many2one('marketing_strategy.clubhouse.club', string='Club', required=True)