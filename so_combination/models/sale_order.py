# -- coding: utf-8 --

from odoo import models , fields , api



class SaleOrder(models.Model):
    _inherit = 'sale.order'
 
    is_combination = fields.Boolean('Combination')
   

#    search method 

    # def action_confirm(self):
    #     for res in self:

            # result = self.env['sale.order'].search([])
            # print('sale order recode:    ', result)

            # p_result = self.env['sale.order'].search([('partner_id','=',14)])
            # print('sale order recode:;;;;;;;;', p_result)
            

            # b_result = self.env['sale.order'].browse([7, 18, 12])
            # print('sale order recode:   ', b_result)


            # vals = {
            #     'name' : '',
            #     'partner_id':''
            # }
            # abc = self.env['sale.order'].create(vals)

            # print('__________________', abc)

            # record_update = self.env['sale.order'].browse()
            # if record_update.exits():
            #     vals = {
            #         'partner_id' : 'miva'
            #     }
            #     record_update.write(vals)










            


