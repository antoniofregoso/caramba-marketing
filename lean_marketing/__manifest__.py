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


    'depends': ['crm', 'sale', 'project', 'project_timeline', 'mass_mailing', 'website_crm', 'website_blog_category_and_author'],


    'data': [
        'security/lean_marketing_security.xml',
        'security/ir.model.access.csv',
        'views/lean_marketing_views.xml',
        'views/lean_marketing_settings_views.xml',
        'views/res_partner_views.xml',
        'views/crm_lead_views.xml',
        'views/utm_views.xml',
        'views/website_crm_templates.xml'
        
    ],

    'demo': [
        'demo/demo.xml',
    ],
    
    'post_init_hook': '_set_blacklisted_out',
}