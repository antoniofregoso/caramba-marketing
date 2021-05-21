# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models, tools, _
from odoo.tools import ImageProcess

import logging
_logger = logging.getLogger(__name__)
 

PRODUCT_TYPE = [('good','Good'), ('service','Service'), ('event','Event'), ('experience','Experiences'), ('people','People'), ('pleace','Place'), ('property_right','Property right'), ('institution','Institution'), ('information','Information'), ('idea','Idea')]
PERSONALITY = [('average', 'Average'), ('reserved', 'Reserved'), ('self_centered', 'Self-centered'), ('role_model', 'Role model')]

OPENNESS = {'average':25, 'reserved':25, 'self_centered':25, 'role_model':60}
CONCIENTIOUSNESS = {'average':60, 'reserved':60, 'self_centered':35, 'role_model':80}
EXTRAVERSION = {'average':75, 'reserved':45, 'self_centered':75, 'role_model':75}
AGREEABLENESS = {'average':60, 'reserved':55, 'self_centered':30, 'role_model':75}
EMOTIONAL_RANGE = {'average':75, 'reserved':25, 'self_centered':45, 'role_model':85}



class BrandTag(models.Model):

    _name = "marketing_strategy.brand.tag"
    _description = "Brand Tag"

    name = fields.Char('Tag Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]

class BrandHashtag(models.Model):

    _name = "marketing_strategy.brand.hashtag"
    _description = "Brand Tag"

    name = fields.Char('Hashtag Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Hashtag name already exists !"),
    ]

class BrandTopic(models.Model):

    _name = "marketing_strategy.brand.topic"
    _description = "Topics of Conversation"

    name = fields.Char('Topics of Conversation', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]

class MarketingNeed(models.Model):

    _name = "marketing_strategy.need"
    _description = "Needs"

    name = fields.Char('Name', required=True, translate=True, readonly=True)
    color = fields.Integer('Color Index')


class MarketingValue(models.Model):

    _name = "marketing_strategy.value"
    _description = "Values"

    name = fields.Char('Name', required=True, translate=True, readonly=True)
    color = fields.Integer('Color Index')

class BrandInstagramHighlight(models.Model):

    _name = "marketing_strategy.brand.instagram_highlight"
    _description = "Instagram Highlight"

    name = fields.Char('Name', required=True, translate=True)
    cover = fields.Binary(string='Cover', help='Image size: 1080x1920 pixels')
    brand_id = fields.Many2one('marketing_strategy.brand', string='Brand', ondelete='cascade')

    @api.model
    def create(self, values):
        if 'cover' in values:
            resize_image = ImageProcess(values['cover']).crop_resize(1080,1920)
            values['cover'] = resize_image.image_base64(output_format='PNG')
        return super(BrandInstagramHighlight, self).create(values)

    def write(self, values):
        if 'cover' in values:
            resize_image = ImageProcess(values['cover']).crop_resize(1080,1920)
            values['cover'] = resize_image.image_base64(output_format='PNG')
        return super(BrandInstagramHighlight, self).write(values)
       
       
class MarketingBrand(models.Model):
    _name = 'marketing_strategy.brand'
    _description = 'Brand'    
    _inherit = ['mail.thread', 'mail.activity.mixin','image.mixin']
    _order = 'name asc'

    def _expand_relation(self, states, domain, order):
        return ['main', 'hunter', 'collaborator', 'competitor']

    name = fields.Char('Brand', required=True)
    product_type = fields.Selection(PRODUCT_TYPE)
    relation = fields.Selection([('main','Main'),('hunter','Hunter'),('collaborator','Collaborator'), ('competitor','Competitor')], 
            required=True, default='competitor', group_expand='_expand_relation')
    brand_owner_id = fields.Many2one('res.partner')
    related_brand_id = fields.Many2one('marketing_strategy.brand', string='Related Brand')
    tag_ids = fields.Many2many('marketing_strategy.brand.tag', 'marketing_strategy_brand_tags_rel', 'brand_id', 'tag_id', string='Tags') 
    hashtags_ids = fields.Many2many('marketing_strategy.brand.hashtag', string='Hashtags')
    color = fields.Integer('Kanban Color Index')
    twitter = fields.Char('Twitter Account')
    twitter_folowers = fields.Integer('Twiter Folowers')
    facebook = fields.Char('Facebook Page')
    facebook_likes = fields.Integer('Facebook Likes')
    facebook_folowers = fields.Integer('Facebook Folowers')
    instagram = fields.Char('Instagram Page')
    instagram_posts = fields.Integer('Instagram Posts')
    instagram_folowers = fields.Integer('Instagram Folowers')
    linkedin = fields.Char('Linkedin Page')
    linkedin_folowers = fields.Integer('Linkedin Folowers')
    youtube = fields.Char('Youtube Channel')
    youtube_subscribers = fields.Integer('Youtube Subscribers') 
    tiktok =  fields.Char('TikTok Account')
    tiktok_folowers = fields.Integer('TikTok Folowers')
    tiktok_likes = fields.Integer('TikTok Likes') 
    pinterest =  fields.Char('Pinterest Account')
    pinterest_folowers = fields.Integer('Pinterest Folowers')
    clubhouse = fields.Char('Clubhouse Account')
    clubhouse_folowers = fields.Integer('Clubhouse Folowers') 
    blog = fields.Char('Blog')
    blog_rank = fields.Integer('Rank')
    url = fields.Char('Website')
    website_rank = fields.Integer('Website Rank')
    podcast_channel = fields.Char('Podcast Channel')
    podcast_rank = fields.Integer('Podcast Rank')
    podcast_episodes = fields.Integer('Podcast Episodes')
    facebook_profile = fields.Binary(help='Image size: 170x170 pixels')
    facebook_cover = fields.Binary(help='Image size: 851x315 pixels')
    instagram_profile = fields.Binary(help='Image size: 170x170 pixels')
    instagram_highlights_ids = fields.One2many('marketing_strategy.brand.instagram_highlight', 'brand_id')
    twitter_profile = fields.Binary(help='Image size: 400x400 pixels')
    twitter_header = fields.Binary(help='Image size: 1,500x500 pixels')
    linkedin_profile = fields.Binary(help='Image size: 300x300 pixels')
    linkedin_cover = fields.Binary(help='Image size: 1,128x191 pixels')
    youtube_profile = fields.Binary(help='Image size: 800x800 pixels')
    youtube_cover = fields.Binary(help='Image size: 2,048x1,152 pixels')
    tiktok_profile = fields.Binary(help='Image size: 800x800 pixels', string="TikTok Profile")
    pinterest_profile = fields.Binary(help='Image size: 800x800 pixels', string="Pinterest Profile")
    clubhouse_profile = fields.Binary(help='Image size: 800x800 pixels')
    openness = fields.Float(compute='_compute_openness', readonly=True)
    conscientiousness = fields.Float(compute='_compute_conscientiousness', readonly=True)
    extraversion = fields.Float(compute='_compute_extraversion', readonly=True)
    agreeableness = fields.Float(compute='_compute_agreeableness', readonly=True)
    emotional_range = fields.Float(compute='_compute_emotional_range', readonly=True)
    needs_ids = fields.Many2many('marketing_strategy.need')
    values_ids = fields.Many2many('marketing_strategy.value', 'marketing_strategy_brand_needs_rel', 'brand_id', 'value_id')
    topics_ids = fields.Many2many('marketing_strategy.brand.topic')
    personality = fields.Selection(PERSONALITY, default='average')
    customer_relationship = fields.Selection([('unknown','Unknown'),('friends','Friends'),('colleagues','Colleagues'),('marriage','Marriage'),('partners','Partners'),('parents','Parents'),('lovers','Lovers'),('guru-disciple','Guru-Disciple'),('star-fan','Star-Fan'),('neighbors','Neighbors'),('teammates','Teammates')])
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company)

    
    @api.depends('personality')
    def _compute_openness(self):
        for record in self:
            record.openness = OPENNESS[record.personality]

    @api.depends('personality')
    def _compute_conscientiousness(self):
        for record in self:
            record.conscientiousness = CONCIENTIOUSNESS[record.personality]

    @api.depends('personality')
    def _compute_extraversion(self):
        for record in self:
            record.extraversion = EXTRAVERSION[record.personality]

    @api.depends('personality')
    def _compute_agreeableness(self):
        for record in self:
            record.agreeableness = AGREEABLENESS[record.personality]

    @api.depends('personality')
    def _compute_emotional_range(self):
        for record in self:
            record.emotional_range = EMOTIONAL_RANGE[record.personality]
    
    @api.model
    def create(self, values):
        if 'facebook_profile' in values:
            resize_image = ImageProcess(values['facebook_profile']).crop_resize(170,170)
            values['facebook_profile'] = resize_image.image_base64(output_format='PNG')
        if 'facebook_cover' in values:
            resize_image = ImageProcess(values['facebook_cover']).crop_resize(851,315)
            values['facebook_cover'] = resize_image.image_base64(output_format='PNG')
        if 'instagram_profile' in values:
            resize_image = ImageProcess(values['instagram_profile']).crop_resize(170,170)
            values['instagram_profile'] = resize_image.image_base64(output_format='PNG')
        if 'twitter_profile' in values:
            resize_image = ImageProcess(values['twitter_profile']).crop_resize(400,400)
            values['twitter_profile'] = resize_image.image_base64(output_format='PNG')
        if 'twitter_header' in values:
            resize_image = ImageProcess(values['twitter_header']).crop_resize(1500,500)
            values['twitter_header'] = resize_image.image_base64(output_format='PNG')
        if 'linkedin_profile' in values:
            resize_image = ImageProcess(values['linkedin_profile']).crop_resize(300,300)
            values['linkedin_profile'] = resize_image.image_base64(output_format='PNG')
        if 'linkedin_cover' in values:
            resize_image = ImageProcess(values['linkedin_cover']).crop_resize(1128,191)
            values['linkedin_cover'] = resize_image.image_base64(output_format='PNG')
        if 'youtube_profile' in values:
            resize_image = ImageProcess(values['youtube_profile']).crop_resize(800,800)
            values['youtube_profile'] = resize_image.image_base64(output_format='PNG')
        if 'youtube_cover' in values:
            resize_image = ImageProcess(values['youtube_cover']).crop_resize(2048 ,1152)
            values['youtube_cover'] = resize_image.image_base64(output_format='PNG')
        if 'tiktok_profile' in values:
            resize_image = ImageProcess(values['tiktok_profile']).crop_resize(800,800)
            values['tiktok_profile'] = resize_image.image_base64(output_format='PNG')
        if 'pinterest_profile' in values:
            resize_image = ImageProcess(values['pinterest_profile']).crop_resize(800,800)
            values['pinterest_profile'] = resize_image.image_base64(output_format='PNG')
        if 'clubhouse_profile' in values:
            resize_image = ImageProcess(values['clubhouse_profile']).crop_resize(800,800)
            values['clubhouse_profile'] = resize_image.image_base64(output_format='PNG')
        return super(MarketingBrand, self).create(values)

    def write(self, values):
        if 'facebook_profile' in values:
            resize_image = ImageProcess(values['facebook_profile']).crop_resize(170,170)
            values['facebook_profile'] = resize_image.image_base64(output_format='PNG')
        if 'facebook_cover' in values:
            resize_image = ImageProcess(values['facebook_cover']).crop_resize(851,315)
            values['facebook_cover'] = resize_image.image_base64(output_format='PNG')
        if 'instagram_profile' in values:
            resize_image = ImageProcess(values['instagram_profile']).crop_resize(170,170)
            values['instagram_profile'] = resize_image.image_base64(output_format='PNG')
        if 'twitter_profile' in values:
            resize_image = ImageProcess(values['twitter_profile']).crop_resize(400,400)
            values['twitter_profile'] = resize_image.image_base64(output_format='PNG')
        if 'twitter_header' in values:
            resize_image = ImageProcess(values['twitter_header']).crop_resize(1500,500)
            values['twitter_header'] = resize_image.image_base64(output_format='PNG')
        if 'linkedin_profile' in values:
            resize_image = ImageProcess(values['linkedin_profile']).crop_resize(300,300)
            values['linkedin_profile'] = resize_image.image_base64(output_format='PNG')
        if 'linkedin_cover' in values:
            resize_image = ImageProcess(values['linkedin_cover']).crop_resize(1128,191)
            values['linkedin_cover'] = resize_image.image_base64(output_format='PNG')
        if 'youtube_profile' in values:
            resize_image = ImageProcess(values['youtube_profile']).crop_resize(800,800)
            values['youtube_profile'] = resize_image.image_base64(output_format='PNG')
        if 'youtube_cover' in values:
            resize_image = ImageProcess(values['youtube_cover']).crop_resize(2048 ,1152)
            values['youtube_cover'] = resize_image.image_base64(output_format='PNG')
        if 'tiktok_profile' in values:
            resize_image = ImageProcess(values['tiktok_profile']).crop_resize(800,800)
            values['tiktok_profile'] = resize_image.image_base64(output_format='PNG')
        if 'pinterest_profile' in values:
            resize_image = ImageProcess(values['pinterest_profile']).crop_resize(800,800)
            values['pinterest_profile'] = resize_image.image_base64(output_format='PNG')
        if 'clubhouse_profile' in values:
            resize_image = ImageProcess(values['clubhouse_profile']).crop_resize(800,800)
            values['clubhouse_profile'] = resize_image.image_base64(output_format='PNG')
        return super(MarketingBrand, self).write(values)

    
    
class TouchpointTag(models.Model):

    _name = "marketing_strategy.touchpoint.tag"
    _description = "Touchpoint Tag"

    name = fields.Char('Tag Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]
    
class Touchpoint(models.Model):
    _name = 'marketing_strategy.touchpoint'
    _description = 'Touchpoint'
    _order = 'name asc'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    
    name = fields.Char('Name', required=True)
    active = fields.Boolean(default=True)
    color = fields.Integer('Kanban Color Index')
    sequence = fields.Integer('Sequence')
    state = fields.Selection([
        ('draft', 'Draft'),('testing', 'Testing'),
        ('operating', 'Operating'), ('maintenance', 'Maintenance'), ('cancel', 'Cancelled')],
        string='Status', default='draft', required=True, copy=False, group_expand='_expand_states')
    ref = fields.Char(string='Internal Reference')
    type = fields.Selection([('online', 'Online'),('offline', 'Offline')], string='Type', required=True, default='online')
    url = fields.Char('URL')
    hub_id = fields.Many2one('res.partner', string='Touchpoints hub', required=True, domain=[('touchpoint_hub','=',True)])
    description = fields.Html('Description')
    tag_ids = fields.Many2many('marketing_strategy.touchpoint.tag', 'marketing_strategy_touchpoint_tags_rel', 'touchpoint_id', 'tag_id', string='Tags')
    brand_id = fields.Many2one('marketing_strategy.brand', related='story_brand_id.brand_id', string='Brand', readonly='True')
    story_brand_id = fields.Many2one('marketing_strategy.story_brand')
    plan_id = fields.Many2one('marketing_strategy.plan', string='Marketing Plan')
    buyer_journey_stage = fields.Selection([('awareness','Awareness'),('consideration','Consideration'),('purchase','Purchase'),('service','Service'),('loyalty','Loyalty')], string="Buyer's Journey Stage", default='awareness', required=True, copy=False, group_expand='_expand_buyer_journey')
    responsible_id = fields.Many2one('res.users', string='Responsible', required=False, default=lambda self: self.env.user)
    #image_1920 = fields.Image()
    logo = fields.Image()
    utm_source_id = fields.Many2one('utm.source')
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company)  

    def _expand_states(self, states, domain, order):
        return ['draft', 'testing', 'operating', 'maintenance', 'cancel']
        
    def _expand_buyer_journey(self, states, domain, order):
        return ['awareness','consideration','purchase','service', 'loyalty']     
    
class CustomerJob(models.Model):

    _name = "marketing_strategy.value_proposition.customer_job"
    _description = "Customer Job"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Custumer job name already exists !"),
    ]

class CustomerPain(models.Model):

    _name = "marketing_strategy.value_proposition.customer_pain"
    _description = "Customer Pain"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Customer pain name already exists !"),
    ]

class CustomerGain(models.Model):

    _name = "marketing_strategy.value_proposition.customer_gain"
    _description = "Customer Gain"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Custumer gain name already exists !"),
    ]

class PainReliever(models.Model):

    _name = "marketing_strategy.value_proposition.pain_reliever"
    _description = "Pain Reliever"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Pain reliever name already exists !"),
    ]

class GainCreator(models.Model):

    _name = "marketing_strategy.value_proposition.gain_creator"
    _description = "Gain Creator"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Gain creator name already exists !"),
    ]

class ProductsServices(models.Model):

    _name = "marketing_strategy.value_proposition.products_services"
    _description = "Products & Services"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Product or Service name already exists !"),
    ]

class ValueProposition(models.Model):
    _name = 'marketing_strategy.value_proposition'
    _description = 'Value Propositions'
    _order = 'name asc'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    
    def _expand_states(self, states, domain, order):
        return ['draft', 'active', 'done', 'cancel']
    
    name = fields.Char('Name', required=True)   
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('done', 'Completed'),
        ('cancel', 'Cancelled'),
        ],
        string='Status', default='draft', required=True, copy=False, group_expand='_expand_states')
    color = fields.Integer('Kanban Color Index')
    brand_owner_id = fields.Many2one('res.partner')
    assessment = fields.Selection([('in_progress','In Progress'),('fit','Fit'), ('mis_fit','Mis Fit')], string='Assessment', default='in_progress')
    description = fields.Html('Description')
    product_type = fields.Selection(PRODUCT_TYPE)
    brand_id = fields.Many2one('marketing_strategy.brand', string='Brand', required=True)
    ref = fields.Char(string='Internal Reference')
    customer_job_ids = fields.Many2many('marketing_strategy.value_proposition.customer_job', 'marketing_strategy_value_propositiont_customer_job_rel', 'value_proposition_id', 'customer_job_id', string='Custumer Jobs')
    customer_pain_ids = fields.Many2many('marketing_strategy.value_proposition.customer_pain', 'marketing_strategy_value_propositiont_customer_pain_rel', 'value_proposition_id', 'customer_pain_id', string='Custumer Pains')
    customer_gain_ids = fields.Many2many('marketing_strategy.value_proposition.customer_gain', 'marketing_strategy_value_propositiont_custumer_gain_rel', 'value_proposition_id', 'custumer_gain_id', string='Custumer Gain')
    pain_reliever_ids = fields.Many2many('marketing_strategy.value_proposition.pain_reliever', 'marketing_strategy_value_propositiont_pain_reliever_rel', 'value_proposition_id', 'pain_reliever_id', string='Pain Reliever')
    gain_creator_ids = fields.Many2many('marketing_strategy.value_proposition.gain_creator', 'marketing_strategy_value_propositiont_gain_creator_rel', 'value_proposition_id', 'gain_creator_id', string='Gain Creator')
    products_services_ids = fields.Many2many('marketing_strategy.value_proposition.products_services', 'marketing_strategy_value_propositiont_p_s_rel', 'value_proposition_id', 'p_s_id', string='Products & Services')
    buyer_persona_id = fields.Many2one('marketing_strategy.buyer_persona')
    tribe_id = fields.Many2one(related='buyer_persona_id.tribe_id', readonly=True)
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company)

 
class MeetingPlace(models.Model):

    _name = "marketing_strategy.meeting_place"
    _description = "Meeting place"

    name = fields.Char('Place Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Meeting place name already exists !"),
    ]
    
class MeetingContentType(models.Model):

    _name = "marketing_strategy.content_type"
    _description = "Content Type"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Content type name already exists !"),
    ]
    
class SocialMediaPreference(models.Model):

    _name = "marketing_strategy.social_media_preference"
    _description = "Social Media Preference"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Social Media name already exists !"),
    ]
    
class BuyerObjection(models.Model):

    _name = "marketing_strategy.buyer_objection"
    _description = "Buyer Objection"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Objection name already exists !"),
    ]
    
class BuyerGoal(models.Model):

    _name = "marketing_strategy.buyer_goal"
    _description = "Buyer Goal"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Goal name already exists !"),
    ]
    
class Lifestyle(models.Model):

    _name = "marketing_strategy.buyer_lifestyle"
    _description = "Buyer Lifestyle"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Buyer lifestyle name already exists !"),
    ]
    
class Competence(models.Model):

    _name = "marketing_strategy.buyer_competence"
    _description = "Buyer Competence"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Buyer competence name already exists !"),
    ]
    
    
    
   
    
class BuyerPersona(models.Model):
    _name = "marketing_strategy.buyer_persona"
    _description = "Buyer Persona"
    _inherit = ['image.mixin']
    
    @api.model
    def _lang_get(self):
        return self.env['res.lang'].get_installed()
    
    name = fields.Char('Name', required=True, translate=True)
    tribe_id = fields.Many2one('marketing_strategy.tribe', string='Tribe',  required=True)
    color = fields.Integer(string='Color Index', default=0)
    bio = fields.Html('Bio', translate=True)
    age = fields.Integer('Age')
    gender = fields.Selection([('female','Female'),('male','Male'), ('gay','Gay'),('lesbian','Lesbian')], string='Gender')
    status = fields.Selection([('married','Married'),('single','Single'), ('divorced','Divorced'),('widower','Widower')], string='Civil Status')
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
    
    competence_ids = fields.Many2many('marketing_strategy.buyer_competence', 'buyer_competence_rel', 'buyer_id', 'competence_id', string='Competences')
    lifestyle_ids = fields.Many2many('marketing_strategy.buyer_lifestyle', 'buyer_buyer_lifestyle_rel', 'buyer_id', 'buyer_lifestyle_id', string='Lifestyle')
    content_type_ids = fields.Many2many('marketing_strategy.content_type', 'buyer_content_rel', 'buyer_id', 'content_type_id', string='Content Type')
    social_media_ids = fields.Many2many('marketing_strategy.social_media_preference', 'buyer_social_media_preferences_rel', 'buyer_id', 'social_media_id', string='Social Media')
    objection_ids = fields.Many2many('marketing_strategy.buyer_objection', 'buyer_objection_rel', 'buyer_id', 'objection_id', string='Objections')
    goal_ids = fields.Many2many('marketing_strategy.buyer_goal', 'buyer_goal_rel', 'buyer_id', 'goal_id', string='Goals')  
    personality = fields.Selection(PERSONALITY, default='average')
    openness = fields.Float(compute='_compute_openness', readonly=True)
    conscientiousness = fields.Float(compute='_compute_conscientiousness', readonly=True)
    extraversion = fields.Float(compute='_compute_extraversion', readonly=True)
    agreeableness = fields.Float(compute='_compute_agreeableness', readonly=True)
    emotional_range = fields.Float(compute='_compute_emotional_range', readonly=True)
    needs_ids = fields.Many2many('marketing_strategy.need', 'marketing_strategy_buyer_persona_needs_rel', 'brand_id', 'need_id')
    values_ids = fields.Many2many('marketing_strategy.value', 'marketing_strategy_buyer_persona_rel', 'brand_id', 'value_id')
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.company)
    company_currency = fields.Many2one('res.currency', related='company_id.currency_id')
    

    @api.depends('personality')
    def _compute_openness(self):
        for record in self:
            record.openness = OPENNESS[record.personality]

    @api.depends('personality')
    def _compute_conscientiousness(self):
        for record in self:
            record.conscientiousness = CONCIENTIOUSNESS[record.personality]

    @api.depends('personality')
    def _compute_extraversion(self):
        for record in self:
            record.extraversion = EXTRAVERSION[record.personality]

    @api.depends('personality')
    def _compute_agreeableness(self):
        for record in self:
            record.agreeableness = AGREEABLENESS[record.personality]

    @api.depends('personality')
    def _compute_emotional_range(self):
        for record in self:
            record.emotional_range = EMOTIONAL_RANGE[record.personality]

    
class TribeCategory(models.Model):

    _name = "marketing_strategy.tribe.category"
    _description = "Tribe Category"

    name = fields.Char('Name', required=True, translate=True)

class TribeOnlinePlace(models.Model):

    _name = "marketing_strategy.online_place"
    _description = "Online Meeting Place"

    name = fields.Char('Name', required=True, translate=True)
    url = fields.Char('URL', required=True)
    place_type = fields.Selection([('website','Website'),('youtube','Youtube Channel'),('fbk_fanpagr','Facebook Fanpage'),
                    ('fbk_group','Facebook Group'),('twitter','Twitter Account'), ('','LinkedIn Group')], default='website')
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Online place name already exists !"),
        ('url_uniq', 'unique (url)', "URL already exists !"),
    ] 
   
    
class Tribe(models.Model):
    _name = "marketing_strategy.tribe"
    _description = "Tribe"
    _inherit = ['image.mixin']
    
    name = fields.Char('Tribe Name', required=True, translate=True) 
    category_id = fields.Many2one('marketing_strategy.tribe.category',  string='Category')   
    color = fields.Integer(string='Color Index', default=0)
    meeting_place_ids = fields.Many2many('marketing_strategy.meeting_place', 'tribe_buyer_rel', 'tribe_id', 'meeting_place_id', string='Meeting Places')
    online_place_ids = fields.Many2many('marketing_strategy.online_place', 'tribe_online_rel', 'tribe_id', 'online_place_id', string='Online Places') 
    description = fields.Html('Description')
    age_min = fields.Integer('Age Min')
    age_max = fields.Integer('Age Max')
    members_ids = fields.One2many('marketing_strategy.buyer_persona', 'tribe_id', string='Members') 
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company)
    
class ProspectsSource(models.Model):

    _name = "marketing_strategy.prospect_source"
    _description = "Prospects Source"
    _order = 'name'

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]

class Plan(models.Model):
    _name = 'marketing_strategy.plan'
    _description = 'Marketing Plan'
    _order = 'name asc'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    
    def _expand_states(self, states, domain, order):
        return ['draft', 'active', 'done', 'cancel']
    
    name = fields.Char('Name', required=True) 
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('done', 'Completed'),
        ('cancel', 'Cancelled'),
        ],
        string='Status', default='draft', required=True, copy=False, group_expand='_expand_states')
    active = fields.Boolean(default=True,
        help="If the active field is set to False, it will allow you to hide the project without removing it.")
    mission = fields.Html('Description')
    value_proposition_id = fields.Many2one('marketing_strategy.value_proposition', string='Value Proposition', required=True)
    story_brand_id = fields.Many2one('marketing_strategy.story_brand')
    prospects_sources_ids = fields.Many2many('marketing_strategy.prospect_source', string='Prospects Sources')
    cac = fields.Monetary('CAC', help='Customer Acquisition Cost', currency_field='company_currency', default=0.0)
    ltv = fields.Monetary('LTV', help='Lifetime Value', currency_field='company_currency', default=0.0)
    ue = fields.Monetary('UE', help='Unit Economics', currency_field='company_currency', compute='_get_ue')
    sales = fields.Monetary('Sales', currency_field='company_currency')
    date_start = fields.Date(string='Start Date')
    date_end = fields.Date(string='End Date')
    user_id = fields.Many2one('res.users', string='Responsible', default=lambda self: self.env.user)
    project_id = fields.Many2one('project.project', string='Project', ondelete='cascade')
    campaigns_ids = fields.One2many('utm.campaign', 'plan_id', string="Campaigns")
    color = fields.Integer(string='Color Index')
    sequence = fields.Integer('Sequence')
    buyers_persona_ids = fields.Many2many('marketing_strategy.buyer_persona', 'marketing_strategy_plan_buyer_persona_rel', 'plan_id', 'buyer_persona_id', string='Buyers Persona')     
    touchpoints_ids = fields.One2many('marketing_strategy.touchpoint', 'plan_id', string="Touchpoints")    
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.company)
    company_currency = fields.Many2one('res.currency', related='company_id.currency_id')

    @api.depends('ltv','cac')
    def _get_ue(self):
        for record in self:
            if record.cac == 0.0:
                record.ue = 0.0
            else:
                record.ue = record.ltv / record.cac
    

    
    