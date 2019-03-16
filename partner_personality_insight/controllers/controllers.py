# -*- coding: utf-8 -*-
from odoo import http

# class PartnerPersonalityInsight(http.Controller):
#     @http.route('/partner_personality_insight/partner_personality_insight/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_personality_insight/partner_personality_insight/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_personality_insight.listing', {
#             'root': '/partner_personality_insight/partner_personality_insight',
#             'objects': http.request.env['partner_personality_insight.partner_personality_insight'].search([]),
#         })

#     @http.route('/partner_personality_insight/partner_personality_insight/objects/<model("partner_personality_insight.partner_personality_insight"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_personality_insight.object', {
#             'object': obj
#         })