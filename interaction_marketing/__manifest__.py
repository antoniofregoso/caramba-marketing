# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

{
    'name': "Marketing Buyer Persona",

    'summary': 'Tool to create person buyer templates and group them in tribes',

    'description': '',

    'author': "Antonio Fregoso",
    'website': 'http://www.antoniofregoso.blog',

    'category': 'Marketing',
    'version': '12.0.0.0.1',

    'depends': ['project', 'project_timeline', 'mass_mailing'],


    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
    
    'license': 'AGPL-3',
}