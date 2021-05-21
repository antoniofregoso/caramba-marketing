# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

{
    'name': "Marketing Strategy",

    'summary': "Marketing Strategy Framework",


    'author': "Antonio Fregoso",
    'website': "https://www.antoniofregoso.com",
    'category': 'Marketing/Strategy',
    'version': '2.1.0',
    'depends': ['mass_mailing','sale_crm', 'project', 'website_blog', 'event', 'survey'],
    'license': 'AGPL-3',
    'data': [
        'security/marketing_strategy_security.xml',
        'security/ir.model.access.csv',
        'views/marketing_strategy_views.xml',
        'views/marketing_strategy_settings_views.xml',
        'views/res_config_settings.xml',
        'views/utm_views.xml',
        'views/crm_lead_views.xml',
        'views/res_partner_views.xml',
        'views/marketing_strategy_story_brand_views.xml',
        'data/marketing_strategy_data.xml',
        'data/report_paperformat_data.xml',
        'report/marketing_plan.xml',
        'report/marketing_story_brand.xml',
        'report/marketing_value_proposition_canvas.xml',
        
    ],
    'demo': [
        'demo/demo.xml',
    ],    
    
    'installable': True,
    'application': True,
    'auto_install': False
}
