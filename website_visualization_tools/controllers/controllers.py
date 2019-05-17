# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteVisualizationTools(http.Controller):
#     @http.route('/website_visualization_tools/website_visualization_tools/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_visualization_tools/website_visualization_tools/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_visualization_tools.listing', {
#             'root': '/website_visualization_tools/website_visualization_tools',
#             'objects': http.request.env['website_visualization_tools.website_visualization_tools'].search([]),
#         })

#     @http.route('/website_visualization_tools/website_visualization_tools/objects/<model("website_visualization_tools.website_visualization_tools"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_visualization_tools.object', {
#             'object': obj
#         })