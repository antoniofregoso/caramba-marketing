# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

{
    'name': "Lean Marketing Buyer Persona",

    'summary': 'Tool to create person buyer templates and group them in tribes',

    'description': '',

    'author': "Antonio Fregoso",
    'website': 'http://www.antoniofregoso.blog',

    'category': 'Marketing',
    'version': '12.0.0.0.1',

    'depends': ['lean_marketing'],


    'data': [
        'security/ir.model.access.csv',
        'views/marketing_buyer_persona_views.xml',
        'views/marketing_buyer_persona_settings_views.xml',
        'data/buyer_persona_data.xml'
    ],

    'demo': [
        'demo/demo.xml',
    ],
    
    'license': 'AGPL-3',
}