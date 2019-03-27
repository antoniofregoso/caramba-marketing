# -*- coding: utf-8 -*-
{
    'name': 'Facebook Campaigns',

    'summary': 'Facebook Campaign Management',

    'description': '''
    
    ''',

    'author': "Antonio Fregoso",
    'website': "http://www.antoniofregoso.blog",
    'category': 'Marketing',
    'version': '12.0.0.0.0',

    
    'depends': ['mass_mailing'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}