{
    #  Information

    'name': 'SO Pending Dues',
    'version': '15.0.0',
    'summary': 'SO Pending Dues',
    'description': "SO Pending Dues",
    'category': 'custom',

    # Author

    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    
    'depends': [
        'sale_management',
        'mrp',
        ],
        
    'data': [
        'views/sale_order_view.xml',
        'views/mrp_production_view.xml',
       
    ],

    # Other
    'installable': True,
    'auto_install': False,
   

} 