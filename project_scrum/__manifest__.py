# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

{
    'name': "Project Scrum",

    'summary': 'Use Scrum Method to manage your project',


    'author': "My Company",
    'website': "http://www.yourcompany.com",

   
    'category': 'Project',
    'version': '12.0.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['project'],

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