{
#information
    
 'name':'General Ledger Report Customization',
 'version': '15.0',
 'summary': 'General Ledger Report Customization',
 'description': 'General Ledger Report Customization',
 'category': 'custom',

# Author

 'author': 'odoo Ps',
 'website': 'https://www.odoo.com/',
 'license': '',

# Dependency
 'depends': [
     'account',
     'account_accountant',
     'account_reports',
     'base','web',
 ],
 
 'data': [
     'reports/report.xml' ,
     'reports/report_template.xml' ,
     'security/ir.model.access.csv',
     'wizards/general_ledger_report_wizard.xml',
     'views/account_move_views.xml' ,
     
    
 ],

 # Other
 'installable': True,
 'auto_install': False,
}
