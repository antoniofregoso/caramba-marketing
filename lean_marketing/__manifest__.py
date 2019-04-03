# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

{
    'name': "Lean Marketing",

    'summary': "Implements lean marketing management-",

    'description': """
        Lean marketing focus on results of small, trial campaigns, learn from the results, and evolve the elements of the campaign.
    """,

    'author': "Antonio Fregoso",
    'website': "http://www.antoniofregoso.blog",


    'category': 'Marketing',
    'version': '12.0.0.0.0',


    'depends': ['crm', 'sale', 'project', 'project_timeline', 'mass_mailing'],


    'data': [
        'security/lean_marketing_security.xml',
        'security/ir.model.access.csv',
        'views/lean_marketing_views.xml',
        'views/lean_marketing_settings_views.xml',
        'views/res_partner_views.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
}