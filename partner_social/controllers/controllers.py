# -*- coding: utf-8 -*-
from odoo import http

# class PartnerSocial(http.Controller):
#     @http.route('/partner_social/partner_social/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_social/partner_social/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_social.listing', {
#             'root': '/partner_social/partner_social',
#             'objects': http.request.env['partner_social.partner_social'].search([]),
#         })

#     @http.route('/partner_social/partner_social/objects/<model("partner_social.partner_social"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_social.object', {
#             'object': obj
#         })