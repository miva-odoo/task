# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    
    override_credit_limit = fields.Boolean(string="Override Credit Limit")
    #-------------------------------
    # method declaration
    #-------------------------------
    
    def action_confirm(self):
        if self.override_credit_limit:
            return super(SaleOrder, self).action_confirm()
        elif self.amount_total > self.partner_id.credit_limit:
            return {'type': 'ir.actions.act_window',
                    'res_model': 'saleorder.wizard',
                    'view_mode': 'form',
                    'target' : 'new'}
        return super(SaleOrder, self).action_confirm()

    