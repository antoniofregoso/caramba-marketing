# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_marketing_strategy_consumer_trend = fields.Boolean("Consumer Trend Canvas")
    module_marketing_business_model = fields.Boolean("Business Model Canvas")
    module_marketing_funnels = fields.Boolean("Funnels")
    module_marketing_strategy_gap_assessment = fields.Boolean("Gap Assessment")
    module_content_marketing = fields.Boolean("Content Marketing")
    module_marketing_facebook_ads = fields.Boolean("Facebook Ads")
    module_marketing_google_ads = fields.Boolean("Google Ads")
    module_base_social_networks = fields.Boolean("Social Networks")
    module_website_facebook_pixel = fields.Boolean("Facebook Pixel")