# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import models, fields, api, tools
import logging
_logger = logging.getLogger(__name__)

class MeetingPlace(models.Model):

    _name = "lean_marketing.meeting_place"
    _description = "Meeting place"

    name = fields.Char('Place Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Meeting place name already exists !"),
    ]
    
class MeetingContentType(models.Model):

    _name = "lean_marketing.content_type"
    _description = "Content Type"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Content type name already exists !"),
    ]
    
class SocialMediaPreference(models.Model):

    _name = "lean_marketing.social_media_preference"
    _description = "Social Media Preference"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Social Media name already exists !"),
    ]
    
class BuyerObjection(models.Model):

    _name = "lean_marketing.buyer_objection"
    _description = "Buyer Objection"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Objection name already exists !"),
    ]
    
class BuyerGoal(models.Model):

    _name = "lean_marketing.buyer_goal"
    _description = "Buyer Goal"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Goal name already exists !"),
    ]
    
class Preference(models.Model):

    _name = "lean_marketing.buyer_preferences"
    _description = "Buyer Preference"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Buyer preference name already exists !"),
    ]
    
class Competence(models.Model):

    _name = "lean_marketing.buyer_competence"
    _description = "Buyer Competence"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Buyer competence name already exists !"),
    ]
    
class Segment(models.Model):
    _name = "lean_marketing.segment"
    
    name = fields.Char('Name', required=True, translate=True)
    distribution = fields.Char('Distribution', translate=True)
    primary_motivation = fields.Selection([('ideals', 'Ideals'), ('achievement', 'Achievement'), ('self-expression', 'Self-Expresion')], 'Primary Motivation', translate=True)
    resources = fields.Selection([('high-resources','High Resources'),('low-resources', 'Low Resources')], 'Resources', translate=True)
    lifestyle = fields.Html('Lifestyle Characteristics', translate=True)
    psychological  = fields.Html('Psychological Characteristics', translate=True)
    consumer = fields.Html('Consumer Characteristics', translate=True)
    members_ids = fields.One2many('lean_marketing.buyer_persona', 'segment_id', string='Members') 
    color = fields.Integer('Color Index')
    
    
class BuyerPersona(models.Model):
    _name = "lean_marketing.buyer_persona"
    _description = "Buyer Persona"
    
    @api.model
    def _lang_get(self):
        return self.env['res.lang'].get_installed()
    
    name = fields.Char('Place Name', required=True, translate=True)
    segment_id = fields.Many2one('lean_marketing.segment', string='Segment')
    tribe_id = fields.Many2one('lean_marketing.tribe', string='Tribe',  required=True)
    color = fields.Integer(string='Color Index', default=0)
    bio = fields.Html('Bio', translate=True)
    age_min = fields.Integer('Age Min')
    age_max = fields.Integer('Age Max')
    gender = fields.Selection([('female','Female'),('male','Male'), ('gay','Gay'),('lesbian','Lesbian')], string='Gender')
    status = fields.Selection([('married','Married'),('single','Single'), ('divorced','Divorced'),('widower','Widower')])
    children = fields.Integer('# Children')
    income = fields.Monetary('Annual Income', currency_field='company_currency')
    title = fields.Many2one('res.partner.title')
    function = fields.Char(string='Job Position')
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict', domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    zip = fields.Char('Zip')
    city = fields.Char('City')
    lang = fields.Selection(_lang_get, string='Language', default=lambda self: self.env.lang,
                            help="All the emails and documents sent to this contact will be translated in this language.")
    
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
    content_type_ids = fields.Many2many('lean_marketing.content_type', 'buyer_content_rel', 'buyer_id', 'content_type_id', string='Content Type Preferences')
    social_media_ids = fields.Many2many('lean_marketing.social_media_preference', 'buyer_social_media_preferences_rel', 'buyer_id', 'social_media_id', string='Social Media Preferences')
    objection_ids = fields.Many2many('lean_marketing.buyer_objection', 'buyer_objection_rel', 'buyer_id', 'objection_id', string='Objections')
    goal_ids = fields.Many2many('lean_marketing.buyer_goal', 'buyer_goal_rel', 'buyer_id', 'goal_id', string='Goals')    
    company_id = fields.Many2one('res.company', string='Company', index=True, default=lambda self: self.env.user.company_id.id)
    company_currency = fields.Many2one(string='Currency', related='company_id.currency_id', readonly=True, relation="res.currency")
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            tools.image_resize_images(vals)
        return super(BuyerPersona, self).create(vals_list)

    @api.multi
    def write(self, vals):
        tools.image_resize_images(vals)
        return super(BuyerPersona, self).write(vals)
    
class TribeCategory(models.Model):

    _name = "lean_marketing.tribe.category"
    _description = "Tribe Category"

    name = fields.Char('Name', required=True, translate=True)
   
    
class Tribe(models.Model):
    _name = "lean_marketing.tribe"
    _description = "Tribe"
    
    name = fields.Char('Tribe Name', required=True, translate=True) 
    category_id = fields.Many2one('lean_marketing.tribe.category',  string='Category')   
    color = fields.Integer(string='Color Index', default=0)
    meeting_place_ids = fields.Many2many('lean_marketing.meeting_place', 'tribe_buyer_rel', 'tribe_id', 'meeting_place_id', string='Meeting Places')
    description = fields.Html('Description')
    members_ids = fields.One2many('lean_marketing.buyer_persona', 'tribe_id', string='Members') 
    
    