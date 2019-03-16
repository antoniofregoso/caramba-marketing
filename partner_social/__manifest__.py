# -*- coding: utf-8 -*-
{
    'name': "Partner Social",

    'summary': "Add social media accounts list to partner information",
    'description': """Add a tab to the partner form to add your accounts on social networks and blogs. """,
 

    'author': "Antonio Fregoso",
    'website': "https://www.antoniofregoso.blog/",


    'category': 'Marketing',
    'version': '12.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['contacts'],

    # always loaded
    'data': [
        'views/partner_social_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/partner_social_demo.xml',
    ],
}