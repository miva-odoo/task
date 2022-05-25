# -- coding: utf-8 --

from odoo import models , fields , api



class AccountMove(models.Model):
    _inherit = 'account.move'


    is_panding = fields.Boolean('Print pending dues for this customer')

    def get_pending_so_values(self):
        # sale_order = self.env['sale.oder'].search(['partner_id' , '=',14 ])
        sale_order = self.env['sale.order'].search([('partner_id','=',self.partner_id.id)])
        
        pending_so_dict = []
        for i in sale_order:
            pending_so_dict.append({
                'name': i.name,
                'amount':i.invoice_ids.amount_residual,
            })
           
        return pending_so_dict
        