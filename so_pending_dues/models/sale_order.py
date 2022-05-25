# -- coding: utf-8 --

from odoo import models , fields , api



class SaleOrder(models.Model):
    _inherit = 'sale.order'


    is_panding = fields.Boolean('Print pending dues for this customer')

    def get_pending_so_values(self):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>')

        # sale_order = self.env['sale.oder'].search(['partner_id' , '=',14 ])
        sale_order = self.env['sale.order'].search([('partner_id','=',self.partner_id.id)])
        print('sale order recode:;;;;;;;;', sale_order)
    
        pending_so_dict = []
        for i in sale_order:
            pending_so_dict.append({
                'name': i.name,
                'amount':i.invoice_ids.amount_residual,
            })
           
        print("::::::::::::::::::::::",pending_so_dict)
        return pending_so_dict
        
       
# amount_residual
