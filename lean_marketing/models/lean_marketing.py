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

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            tools.image_resize_images(vals)
        return super(MarketingBrand, self).create(vals_list)

    @api.multi
    def write(self, vals):
        tools.image_resize_images(vals)
        return super(MarketingBrand, self).write(vals)
    
    
class OnlineTouchpoint(models.Model):
    _name = 'lean_marketing.online_touchpoint'
    _description = 'Online Touchpoint'
    _order = 'name asc'
    
    name = fields.Char('Name', required=True)
    ref = fields.Char(string='Internal Reference')
    url = fields.Char('URL', required=True)
    description = fields.Char('Description')
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

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            tools.image_resize_images(vals)
        return super(MarketingBrand, self).create(vals_list)
    
class OfflineTouchpoint(models.Model):
    _name = 'lean_marketing.offline_touchpoint'
    _description = 'Offline Touchpoint'
    _order = 'name asc'
    
    name = fields.Char('Name', required=True)
    ref = fields.Char(string='Internal Reference')
    fields.Many2one('res.partner', string='Hub')
    description = fields.Char('Description')
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

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            tools.image_resize_images(vals)
        return super(MarketingBrand, self).create(vals_list)

    

    