# -- coding: utf-8 --

from odoo.tools.misc import get_lang
from odoo import models,fields



class GeneralLedgerReportWizard(models.TransientModel):
    
    _name = 'general.ledger.report.wizard'
    _description = 'General Ledger Report Wizard'

    # ==========================
    # Field Declaration
    # ==========================

    account_id = fields.Many2many('account.account')
    from_date = fields.Date()
    to_date = fields.Date()


    # ==========================
    # Method Declaration
    # ==========================

    
    
    
    def general_ledger_report_wizard(self):
        # import pdb
        # pdb.set_trace()
        data = {
            "form_data":self.read()[0],
            }
        account_account = data['form_data']['account_id'][0]
        # print("+++++++++++",account_account)
        options = {
        "unfolded_lines": [],
        "allow_domestic": False,
        "fiscal_position": "all",
        "available_vat_fiscal_positions": [],
        "date": {'string': 'From {} to {}'.format(self.from_date, self.to_date),
            'period_type': 'custom',
            'mode': 'range',
            'strict_range': False,
            'date_from': self.from_date,
            'date_to': self.to_date,
            'filter': 'custom'},
        "all_entries": False,
        "analytic": True,
        "cash_basis": False,
        "journals": [],
        "name_journal_group": "All Journals",
        "unfold_all": False,
        "unposted_in_period": True,
        "account_id": self.account_id.ids,
        }
        
        # options_list = self._get_options_periods_list(options)
        xyz = self.env['account.general.ledger'].with_context(no_format=True, print_mode=True)._get_lines(options,line_id=None)
        abc = self.env['account.general.ledger'].with_context(no_format=True, print_mode=True)._get_lines(options,line_id=None)
        print('>>>>>>>>>>>>>>>>>>>>>>>abc >>>>>>>>>>>>>>>...', abc)
        return self.env.ref('general_ledger_report_customizationv.general_ledger_report').report_action([], data={'abc': abc})
