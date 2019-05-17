# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

{
    'name': "Lean Marketing Business Model Canvas",

    'summary': "Implementation of business model canvas for lean marketing campaigns",

    'description': """
        Long description of module's purpose
    """,

    'author': "Antonio Fregoso",
    'website': "http://www.antonio.fregoso.blog",

    
    'category': 'Marketing',
    'version': '12.0.0.0.0',

   
    'depends': ['marketing_buyer_persona'],

   
    'data': [
        'security/ir.model.access.csv',
        'views/lean_marketing_business_model_canvas_views.xml',
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
}