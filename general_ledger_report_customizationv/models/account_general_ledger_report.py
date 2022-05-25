# -- coding: utf-8 --

from odoo import models,api
  
class AccountGeneralLedgerReport(models.AbstractModel):
  
    _inherit = "account.general.ledger"


     # ==========================
    # Method Declaration
    # ==========================

    @api.model
    def create(self, vals_list):
        templates = super(AccountGeneralLedgerReport, self).create(vals_list)
        for template, vals in zip(templates, vals_list):
            related_vals = {}
            if vals.get('internal_refence_miva'):
                related_vals['internal_refence_miva'] = vals['internal_refence_miva']
            if related_vals:
                template.write(related_vals)
        return templates