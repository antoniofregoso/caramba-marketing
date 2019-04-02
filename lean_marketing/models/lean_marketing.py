# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models, tools

class MarketingBrand(models.Model):
    _name = 'lean_marketing.brand'
    _description = 'Brand of the vehicle'
    _order = 'name asc'

    name = fields.Char('Brand', required=True)
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
   
    

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            tools.image_resize_images(vals)
        return super(MarketingBrand, self).create(vals_list)

    @api.multi
    def write(self, vals):
        tools.image_resize_images(vals)
        return super(MarketingBrand, self).write(vals)
    
    
class Touchpoint(models.Model):
    _name = 'lean_marketing.touchpoint'
    _description = 'Touchpoint'
    _order = 'name asc'
    _inherit = ['mail.thread']
    
    name = fields.Char('Name', required=True)
    active = fields.Boolean(default=True)
    color = fields.Integer('Kanban Color Index')
    state = fields.Selection([
        ('draft', 'Draft'), ('cancel', 'Cancelled'),
        ('operating', 'Operating'), ('maintenance', 'Maintenance')],
        string='Status', default='draft', readonly=True, required=True, copy=False)
    ref = fields.Char(string='Internal Reference')
    type = fields.Selection([('online', 'Online'),('offline', 'Offline')], string='Type')
    url = fields.Char('URL')
    partner_id = fields.Many2one('res.partner', string='Touchpoints hub')
    description = fields.Html('Description')
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
        return super(Touchpoint, self).create(vals_list)
    
    
    @api.multi
    def write(self, vals):
        tools.image_resize_images(vals)
        return super(Touchpoint, self).write(vals)

    

    