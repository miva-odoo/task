# -*- coding: utf-8 -*-
{
    #  Information
    'name':'TGI Credit Limit Customization',
    'version': '15.0',
    'summary': 'TGI Credit Limit Customization',
    'description':'TGI Credit Limit Customization',
    'category':'',

    # Author
    'author': 'Odoo Ps',
    'website': 'https://www.odoo.com/',
    'license': '',
    
    # Dependency
    'data':[
        'wizards/sale_order_wizard.xml',
        'views/res_partner_views.xml',
        #'views/sale_wizard_views.xml',
        'views/sale_order_views.xml',
        'security/ir.model.access.csv',
        'security/security_group.xml',
        'data/email_template_data.xml',
        ],
    'depends':['sale_management','mail'],
    'demo':[''],
    # Other
    'application':True,
    'installble':True,
}
