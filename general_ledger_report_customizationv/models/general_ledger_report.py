# -- coding: utf-8 --

from doctest import DocFileSuite
from odoo import models,api, fields


class RepoerGeneralLedger(models.AbstractModel):

    _name = 'report.general_ledger_report_customizationv.general_ledger'
    _description = 'General Ledger Report'

    from_date = fields.Date('From Date')

    @api.model
    def _get_report_values(self, docids, data=None):
        
        print('\n\n\n>>>>>>>>', data['form']['account_id'])
        
        return {'data': data}
  