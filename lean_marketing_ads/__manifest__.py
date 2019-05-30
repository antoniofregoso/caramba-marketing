# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

{
    'name': "Ads",

    'summary': "Online Ads",

    'description': """
        Base module for advertising management in social networks and search engines.
    """,

    'author': "Antonio Fregoso",
    'website': "http://www.antoniofregoso.blog",

   
    'category': 'Marketing',
    'version': '12.0.0.0.0',

    
    'depends': ['marketing_buyer_persona'],

   
    'data': [
        'security/lean_marketing_ads.xml',
        'security/ir.model.access.csv',
        'views/lean_marketing_ads_views.xml'
    ],
   
}