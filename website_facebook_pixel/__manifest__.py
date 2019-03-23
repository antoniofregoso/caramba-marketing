# -*- coding: utf-8 -*-
{
    'name': "Website Facebook Pixel",

    'summary': "Add the Facebook pixel to the Odoo pages",

    'description': """
       Allows you to add the list of standard events and their properties in the web pages.
    """,

    'author': "Antonio Fregoso",
    'website': "https://www.antoniofregoso.blog",


    'category': 'Marketing',
    'version': '12..0.0.0.0',

 
    'depends': ['website'],


    'data': [
        # 'security/ir.model.access.csv',
        'views/website_facebook_pixel_views.xml',
        'views/templates.xml',
    ],
   
    'demo': [
        'demo/demo.xml',
    ],
}