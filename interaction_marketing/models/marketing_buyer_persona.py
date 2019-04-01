# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import models, fields, api

class MeetingPlace(models.Model):

    _name = "marketing.meeting_place"
    _description = "Meeting place"

    name = fields.Char('Place Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Meeting place name already exists !"),
    ]
    
class MeetingContentType(models.Model):

    _name = "marketing.content_type"
    _description = "Content Type"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')
    
class SocialMediaPreference(models.Model):

    _name = "marketing.social_media_preference"
    _description = "Social Media Preferences"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')
    
class BuyerObjections(models.Model):

    _name = "marketing.buyer_objections"
    _description = "Buyer Objections"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')
    
class BuyerPersona(models.Model):
    _name = "marketing.buyer_persona"
    _description = "Buyer Persona"
    
    name = fields.Char('Place Name', required=True, translate=True)
    tribe_id = fields.Many2one('marketing.tribe', string='Tribe', index=True)
    color = fields.Integer(string='Color Index', default=0)
    description = fields.Html('Description')
    image = fields.Binary("Image", attachment=True,
        help="This field holds the image used as avatar for this contact, limited to 1024x1024px",)
    image_medium = fields.Binary("Medium-sized image", attachment=True,
        help="Medium-sized image of this contact. It is automatically "\
             "resized as a 128x128px image, with aspect ratio preserved. "\
             "Use this field in form views or some kanban views.")
    image_small = fields.Binary("Small-sized image", attachment=True,
        help="Small-sized image of this contact. It is automatically "\
             "resized as a 64x64px image, with aspect ratio preserved. "\
             "Use this field anywhere a small image is required.")
    influencer_ids = fields.One2many('res.partner', 'parent_id', string='Influencers', domain=[('influencer', '=', True)])
    content_type_ids = fields.Many2many('marketing.content_type', 'buyer_content_rel', 'buyer_id', 'content_type_id', string='Content Type Preferences')
    social_media_ids = fields.Many2many('marketing.social_media_preference', 'buyer_social_media_preferences_rel', 'buyer_id', 'social_media_id', string='Social Media Preferences')
    objection_ids = fields.Many2many('marketing.buyer_objections', 'buyer_objections_rel', 'buyer_id', 'objection_id', string='Objection Preferences')
    
    
    

    
class Tribe(models.Model):
    _name = "marketing.tribe"
    _description = "Tribe"
    
    name = fields.Char('Place Name', required=True, translate=True)
    meeting_place_ids = fields.Many2many('marketing.meeting_place', 'tribe_buyer_rel', 'tribe_id', 'meeting_place_id', string='Meeting Places')
    description = fields.Html('Description')
    members_ids = fields.One2many('marketing.buyer_persona', 'tribe_id', string='Members') 