{
    #  Information
    'name': 'Journal Entry Print',
    'description': 'Journal Entry Print',
    'version' :'14.0.1',
    'category': 'custom',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'license': '',

    # Dependency
    'depends': ['account'],
    'data': [
        'reports/report.xml',
        'reports/template.xml',
    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,
}
