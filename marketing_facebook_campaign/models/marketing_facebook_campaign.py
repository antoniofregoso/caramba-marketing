 # -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#
from odoo import models, fields, api

FB_OBJETIVES = [
    ('BRAND_AWARENESS', 'App install'),
    ('CANVAS_APP_ENGAGEMENT', 'Brand awarness'),
    ('CANVAS_APP_INSTALLS', 'Conversions'),
    ('EVENT_RESPONSES', 'Event responses'),
    ('LEAD_GENERATION', 'Lead generation'),
    ('LOCAL_AWARENESS', 'Link clicks'),
    ('MOBILE_APP_ENGAGEMENT', 'Local awarness'),
    ('MOBILE_APP_INSTALLS', 'Messages'),
    ('NONE', 'Offer claims'),
    ('OFFER_CLAIMS', 'Pages likes'),
    ('PAGE_LIKES', 'Post engagement'),
    ('POST_ENGAGEMENT', 'Product catalog sales'),
    ('LINK_CLICKS', 'Reach'),
    ('CONVERSIONS', 'Video Views'),
    ('VIDEO_VIEWS', 'Video Views'),
    ('PRODUCT_CATALOG_SALES', 'Video Views')
    ]


FB_BID_STRATEGY = [
    ('LOWEST_COST_WITHOUT_CAP','Lowest cost without cap'),
    ('LOWEST_COST_WITH_BID_CAP','Lowest cost with bid cap'),
    ('TARGET_COST','Target Cost')
    ]


FB_STATUS = [
    ('ACTIVE','Active'),
    ('PAUSED','Paused'),
    ('DELETED','Deleted'),
    ('ARCHIVED','Archived')
    ]

FB_EFFECTIVE_STATUS = [
        ('ACTIVE','Active'),
        ('PAUSED','Paused'),
        ('DELETED','Deleted'),
        ('PENDING_REVIEW','Pending review'),
        ('DISAPPROVED','Disapproved'),
        ('PREAPPROVED','Preaproved'),
        ('PENDING_BILLING_INFO','Pending billing info'),
        ('CAMPAIGN_PAUSED','Campaign paused'),
        ('ARCHIVED','Archived'),
        ('ADSET_PAUSED','Adset paused'),
        ('WITH_ISSUES','With issued')
    ]

FB_LEBELS = [
    ('HIGH','Hight'),
    ('MEDIUM','Medium'),
    ('LOW','Low')
    
    ]

class MarketingFacebookAdtag(models.Model):
    _name = 'lean_marketing.facebook.adtag'
    _description = 'Facebook Adtag'

    name = fields.Char('Tag Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]
    
class MarketingFacebookAdrecommendation(models.Model):
    _name = 'lean_marketing.facebook.adrecommendation'
    _description = 'Facebook Adrecomendation'
    
    blame_field = 'blame_field'
    code = 'code'
    confidence = 'confidence'
    importance = 'importance'
    message = 'message'
    recommendation_data = 'recommendation_data'
    title = 'title'
    


class MassMailingCampaign(models.Model):
    """Model of mass mailing campaigns. """
    _inherit = 'mail.mass_mailing.campaign'
    
    fb_account_id = fields.Char('Account', required=True)
    fb_campaign_id = fields.Char('Account', required=True)
    fb_addtag_ids = fields.Many2many('lean_marketing.Facebook.Addtag', 'facebook_addtags_rel', 'campaign_id', 'addtag_id', string='Tags')
    fb_bid_strategy = fields.Selection(FB_BID_STRATEGY, string='Bind Strategy')
    fb_budget_rebalance_flag = fields.Boolean('Budget rebalance Flag')
    fb_budget_remaining = fields.Char('Budget remaining')
    fb_buying_type = fields.Selection([('AUCTION', 'Auction'), ('RESERVED', 'Reserved')], string="Buying type", default='AUCTION', help='RESERVED: for reach and frequency ads')
    fb_can_create_brand_lift_study = fields.Boolean('Brand lift study', help="If we can create a new automated brand lift study for the ad set.")
    fb_can_use_spend_cap = fields.Boolean('Spend Cap', help="Whether the campaign can set the spend cap")
    fb_configured_status = fields.Selection(FB_STATUS, string='Status')
    fb_created_time = fields.datetime('Created Date')
    fb_daily_budget = fields.Monetary('Daily budget')
    fb_effective_status = fields.Selection(FB_EFFECTIVE_STATUS, 'Effective status')
    fb_id = fields.Integer('Id')
    fb_last_budget_toggling_time = 'last_budget_toggling_time'
    fb_lifetime_budget = fields.Char('Lifetime budget', help='The lifetime budget of the campaign')
    fb_objective = fields.Selection(FB_OBJETIVES, string='Objetive', help="Campaign's objective")
    fb_recommendations = 'recommendations'
    fb_source_campaign = 'source_campaign'
    fb_source_campaign_id = 'source_campaign_id'
    fb_spend_cap = 'spend_cap'
    fb_start_time = 'start_time'
    fb_status = 'status'
    fb_stop_time = 'stop_time'
    fb_topline_id = 'topline_id'
    fb_updated_time = 'updated_time'
    fb_adbatch = 'adbatch'
    fb_execution_options = 'execution_options'
    fb_upstream_events = 'upstream_events'
    fb_iterative_split_test_configs = 'iterative_split_test_configs'    
    