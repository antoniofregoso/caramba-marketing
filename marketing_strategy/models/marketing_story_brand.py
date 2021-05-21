# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models, tools, _

CHAPTERS = [
        ('chapter_1','1. Status Quo'),
        ('chapter_2','2. Call to Adventure'),
        ('chapter_3','3. Refusal of the call'),
        ('chapter_4','4. Meeting with the mentor'),
        ('chapter_5','5. Crossing the threshold'),
        ('chapter_6','6. Trials and Allies'),
        ('chapter_7','7. Approaching the cave'),
        ('chapter_8','8. The Ordeal'),
        ('chapter_9','9. The Reward'),
        ('chapter_A','10. The Road Back'),
        ('chapter_B','11. Resurrection'),
        ('chapter_C','12. Return with the Elixir')
        ]

class MarketingStrategyStoryBrandTheme(models.Model):
    _name = "marketing_strategy.story_brand.theme"
    _description = "Story Brand Theme"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'chapter'

    name = fields.Char('Name', required=True)
    description = fields.Char()
    value = fields.Selection([
        ('humor','Makes me laugh'),
        ('identity','This is me'),
        ('connection','Helps me connect with another person'),
        ('learning','It helps me do something'),
        ('feels','Makes me feel something')
        ], help="System BuzzFeed developed called cultural cartography", default="learning", required=True)
    concept = fields.Html()
    contents_ids = fields.One2many('marketing_strategy.story_brand.content', 'theme_id')
    story_brand_id = fields.Many2one('marketing_strategy.story_brand', ondelete='cascade', string='Brand Story') 
    chapter = fields.Selection(CHAPTERS, 'Chapter', help="Chapter within the brand's history.", required=True)
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company)



class MarketingStrategyStoryBrandContent(models.Model):
    _name = "marketing_strategy.story_brand.content"
    _description = "Story Brand Content"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'chapter'

    name = fields.Char('Name', required=True)
    content = fields.Html()
    format = fields.Selection([('blog','Blog'),('longform_content','Longform Content'),('case_study','Case Study'),('white_paper','White Paper'),('ebook','Ebook'),('infographic','Infographic'),('survey','Survey'),('video','Video'),('short_video','Short Video'),('webinar','Webinar'),('online_course','Online Course'),('email','email'), ('podcast','Podcast'), ('audio_chat', 'Audio Chat')], required=True, default='blog' )
    theme_id = fields.Many2one('marketing_strategy.story_brand.theme', ondelete='cascade')
    touch_point_ids = fields.Many2many('marketing_strategy.touchpoint', 'marketing_strategy_content_touchpoint_rel', 'touchpoint_id', 'content_id', string="Touchpoints")
    chapter = fields.Selection(CHAPTERS, related='theme_id.chapter', readonly=True, store=True)
    story_brand_id = fields.Many2one('marketing_strategy.story_brand', related='theme_id.story_brand_id', readonly=True, store=True)
    blog_post_id = fields.Many2one('blog.post', string='Blog Post')
    survey_id = fields.Many2one('survey.survey', string='Survey')
    event_id = fields.Many2one('event.event', string='Event')
    slide_chanel_id = fields.Many2one('slide.channel', string='Online Course')
    mailing_id = fields.Many2one('mailing.mailing', string='Mail')
    club_id = fields.Many2one('marketing_strategy.clubhouse.club', string='Club')
    room_id = fields.Many2one('marketing_strategy.clubhouse.room', string='Room')
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company)

class BrandHashtag(models.Model):

    _name = "marketing_strategy.story_brand.hashtag"
    _description = "Brand Tag"

    name = fields.Char('Hashtag Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Hashtag name already exists !"),
    ]



class MarketingStrategyStoryBrand(models.Model):
    _name = "marketing_strategy.story_brand"
    _description = "Brand Story"
    _inherit = ['mail.thread', 'mail.activity.mixin','image.mixin']

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
    summary = fields.Html()
    brand_owner_id = fields.Many2one('res.partner', required=True)
    value_proposition_id = fields.Many2one('marketing_strategy.value_proposition', required=True)
    hashtags_ids = fields.Many2many('marketing_strategy.story_brand.hashtag', 'marketing_strategy_story_brand_hashtag_id', 'story_brand_id', 'hashtag_id', string='Hashtags')
    user_id = fields.Many2one('res.users', string='Responsible', default=lambda self: self.env.user)
    brand_id = fields.Many2one('marketing_strategy.brand', domain = [('relation','=', 'main')], string='Mentor', required=True)
    tribe_id = fields.Many2one('marketing_strategy.tribe')
    chapters_ids = fields.One2many('marketing_strategy.story_brand.theme', 'story_brand_id')
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company)

    