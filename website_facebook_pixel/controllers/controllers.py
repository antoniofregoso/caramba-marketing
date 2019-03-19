# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteFacebookPixel(http.Controller):
#     @http.route('/website_facebook_pixel/website_facebook_pixel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_facebook_pixel/website_facebook_pixel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_facebook_pixel.listing', {
#             'root': '/website_facebook_pixel/website_facebook_pixel',
#             'objects': http.request.env['website_facebook_pixel.website_facebook_pixel'].search([]),
#         })

#     @http.route('/website_facebook_pixel/website_facebook_pixel/objects/<model("website_facebook_pixel.website_facebook_pixel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_facebook_pixel.object', {
#             'object': obj
#         })