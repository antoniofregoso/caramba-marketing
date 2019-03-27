# -*- coding: utf-8 -*-
from odoo import http

# class ImFacebookCampaign(http.Controller):
#     @http.route('/marketing_facebook_campaign/marketing_facebook_campaign/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/marketing_facebook_campaign/marketing_facebook_campaign/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('marketing_facebook_campaign.listing', {
#             'root': '/marketing_facebook_campaign/marketing_facebook_campaign',
#             'objects': http.request.env['marketing_facebook_campaign.marketing_facebook_campaign'].search([]),
#         })

#     @http.route('/marketing_facebook_campaign/marketing_facebook_campaign/objects/<model("marketing_facebook_campaign.marketing_facebook_campaign"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('marketing_facebook_campaign.object', {
#             'object': obj
#         })