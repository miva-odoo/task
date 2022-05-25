{
    #  Information

    'name': 'Sale Order Combination',
    'version': '15.0.0',
    'summary': 'Sale Order Combinationr',
    'description': "Sale Order Combination",
    'category': 'custom',

    # Author

    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    
    'depends': [
        'sale_management',
        'stock',
        ],
    'data': [
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
        'reports/sale_order_report.xml',
        'reports/account_report_invoice.xml',
       
    ],

    # Other
    'installable': True,
    'auto_install': False,
   

} 