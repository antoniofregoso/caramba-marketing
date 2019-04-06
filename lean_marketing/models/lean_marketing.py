# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models, tools

class BrandTag(models.Model):

    _name = "lean_marketing.brand.tag"
    _description = "Brand Tag"

    name = fields.Char('Tag Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]
    


class MarketingBrand(models.Model):
    _name = 'lean_marketing.brand'
    _description = 'Brand'
    _order = 'name asc'

    name = fields.Char('Brand', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner')
    tag_ids = fields.Many2many('lean_marketing.brand.tag', 'lean_marketing_brand_tags_rel', 'brand_id', 'tag_id', string='Tags') 
    color = fields.Integer('Kanban Color Index')
    image = fields.Binary("Logo", attachment=True,
        help="This field holds the image used as logo for the brand, limited to 1024x1024px.")
    image_medium = fields.Binary("Medium-sized image", attachment=True,
        help="Medium-sized logo of the brand. It is automatically "
             "resized as a 128x128px image, with aspect ratio preserved. "
             "Use this field in form views or some kanban views.")
    image_small = fields.Binary("Small-sized image", attachment=True,
        help="Small-sized logo of the brand. It is automatically "
             "resized as a 64x64px image, with aspect ratio preserved. "
             "Use this field anywhere a small image is required.")
    partner_id = fields.Many2one('res.partner', string='Partner')
    twitter = fields.Char('Twitter Account')
    facebook = fields.Char('Facebook Page')
    linkedin = fields.Char('Linkedin Page')
    youtube = fields.Char('Youtube Channel')
    blog = fields.Char('Blog')
    url = fields.Char('Website')
   
    

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            tools.image_resize_images(vals)
        return super(MarketingBrand, self).create(vals_list)

    @api.multi
    def write(self, vals):
        tools.image_resize_images(vals)
        return super(MarketingBrand, self).write(vals)
    
class TouchpointTag(models.Model):

    _name = "lean_marketing.touchpoint.tag"
    _description = "Touchpoint Tag"

    name = fields.Char('Tag Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]
    
    
class Touchpoint(models.Model):
    _name = 'lean_marketing.touchpoint'
    _description = 'Touchpoint'
    _order = 'name asc'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char('Name', required=True)
    active = fields.Boolean(default=True)
    color = fields.Integer('Kanban Color Index')
    state = fields.Selection([
        ('draft', 'Draft'),('testing', 'Testing'),
        ('operating', 'Operating'), ('maintenance', 'Maintenance'), ('cancel', 'Cancelled')],
        string='Status', default='draft', required=True, copy=False, track_visibility='onchange', group_expand='_expand_states')
    ref = fields.Char(string='Internal Reference')
    type = fields.Selection([('online', 'Online'),('offline', 'Offline')], string='Type', required=True, default='online')
    url = fields.Char('URL')
    hub_id = fields.Many2one('res.partner', string='Touchpoints hub', required=True, domain=[('touchpoint_hub','=',True)])
    description = fields.Html('Description')
    tag_ids = fields.Many2many('lean_marketing.touchpoint.tag', 'lean_marketing_touchpoint_tags_rel', 'touchpoint_id', 'tag_id', string='Tags')
    image = fields.Binary("Photo", attachment=True,
        help="This field holds the image used as big, limited to 1024x1024px.")
    image_medium = fields.Binary("Medium-sized image", attachment=True,
        help="Medium-sized touchpoint. It is automatically "
             "resized as a 128x128px image, with aspect ratio preserved. "
             "Use this field in form views or some kanban views.")
    image_small = fields.Binary("Small-sized image", attachment=True,
        help="Small-sized touchpoint. It is automatically "
             "resized as a 64x64px image, with aspect ratio preserved. "
             "Use this field anywhere a small image is required.")
    plan_id = fields.Many2one('lean_marketing.plan', string='Lean Marketing Plan')
    buyer_journey_stage = fields.Selection([('awareness','Awareness'),('consideration','Consideration'),('purchase','Purchase'),('service','Service'),('loyalty','Loyalty')], string="Buyer's Journey Stage", default='awareness', required=True, copy=False, track_visibility='onchange', group_expand='_expand_buyer_journey')
    responsible_id = fields.Many2one('res.users', string='Responsible', required=False, default=lambda self: self.env.user)
    
    def _expand_states(self, states, domain, order):
        return ['draft', 'testing', 'operating', 'maintenance', 'cancel']
        
    def _expand_buyer_journey(self, states, domain, order):
        return ['awareness','consideration','purchase','service', 'loyalty']
        
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            tools.image_resize_images(vals)
        return super(Touchpoint, self).create(vals_list)
    
    
    @api.multi
    def write(self, vals):
        tools.image_resize_images(vals)
        return super(Touchpoint, self).write(vals)
    
class CustomerJob(models.Model):

    _name = "lean_marketing.solution.customer_job"
    _description = "Customer Job"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Custumer job name already exists !"),
    ]

class CustomerPain(models.Model):

    _name = "lean_marketing.solution.customer_pain"
    _description = "Customer Pain"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Custumer pain name already exists !"),
    ]

class CustomerGain(models.Model):

    _name = "lean_marketing.solution.customer_gain"
    _description = "Customer Gain"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Custumer gain name already exists !"),
    ]

class PainReliever(models.Model):

    _name = "lean_marketing.solution.pain_reliever"
    _description = "Pain Reliever"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Pain reliever name already exists !"),
    ]

class GainCreator(models.Model):

    _name = "lean_marketing.solution.gain_creator"
    _description = "Gain Creator"

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Gain creator name already exists !"),
    ]


    
class Solution(models.Model):
    _name = 'lean_marketing.solution'
    _description = 'Lean Marketing Solutions'
    _order = 'name asc'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char('Name', required=True)
    color = fields.Integer('Kanban Color Index')
    description = fields.Html('Description')
    type = fields.Selection([('product','Product'),('service','Service')], string='Type')
    ref = fields.Char(string='Internal Reference')
    customer_job_ids = fields.Many2many('lean_marketing.solution.customer_job', 'lean_marketing_solutiont_customer_job_rel', 'solution_id', 'customer_job_id', string='Custumer Jobs')
    customer_pain_ids = fields.Many2many('lean_marketing.solution.customer_pain', 'lean_marketing_solutiont_customer_pain_rel', 'solution_id', 'customer_pain_id', string='Custumer Pains')
    custumer_gain_ids = fields.Many2many('lean_marketing.solution.customer_gain', 'lean_marketing_solutiont_custumer_gain_rel', 'solution_id', 'custumer_gain_id', string='Custumer Gain')
    pain_reliever_ids = fields.Many2many('lean_marketing.solution.pain_reliever', 'lean_marketing_solutiont_pain_reliever_rel', 'solution_id', 'pain_reliever_id', string='Pain Reliever')
    gain_creator_ids = fields.Many2many('lean_marketing.solution.gain_creator', 'lean_marketing_solutiont_gain_creator_rel', 'solution_id', 'gain_creator_id', string='Gain Creator')
    products_ids = fields.Many2many('product.product',  'lean_marketing_solutiont_product_rel', 'solution_id', 'product_id', string='Products or Services')
    
    image = fields.Binary("Photo", attachment=True,
        help="This field holds the image used as big, limited to 1024x1024px.")
    image_medium = fields.Binary("Medium-sized image", attachment=True,
        help="Medium-sized touchpoint. It is automatically "
             "resized as a 128x128px image, with aspect ratio preserved. "
             "Use this field in form views or some kanban views.")
    image_small = fields.Binary("Small-sized image", attachment=True,
        help="Small-sized touchpoint. It is automatically "
             "resized as a 64x64px image, with aspect ratio preserved. "
             "Use this field anywhere a small image is required.")
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            tools.image_resize_images(vals)
        return super(Solution, self).create(vals_list)
    
    
    @api.multi
    def write(self, vals):
        tools.image_resize_images(vals)
        return super(Solution, self).write(vals)
    
class Plan(models.Model):
    _name = 'lean_marketing.plan'
    _description = 'Lean Marketing Plan'
    _order = 'name asc'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char('Name', required=True) 
    active = fields.Boolean(default=True,
        help="If the active field is set to False, it will allow you to hide the project without removing it.")
    mission = fields.Html('Description')
    solution_id = fields.Many2one('lean_marketing.solution', string='Solution', required=True)
    target = fields.Monetary('Target', currency_field='company_currency', track_visibility='always')
    date_start = fields.Date(string='Start Date')
    date_end = fields.Date(string='End Date')
    user_id = fields.Many2one('res.users', string='Product owner', default=lambda self: self.env.user, track_visibility="onchange")
    project_id = fields.Many2one('project.project', string='Project', ondelete='cascade')
    campaigns_ids = fields.One2many('utm.campaign', 'plan_id', string="Campaigns", ondelete='cascade')
    touchpoints_ids = fields.One2many('lean_marketing.touchpoint', 'plan_id', string="Touchpoints", ondelete='set null')
    color = fields.Integer(string='Color Index')
    company_id = fields.Many2one('res.company', string='Company', index=True, default=lambda self: self.env.user.company_id.id)
    company_currency = fields.Many2one(string='Currency', related='company_id.currency_id', readonly=True, relation="res.currency")
    
    