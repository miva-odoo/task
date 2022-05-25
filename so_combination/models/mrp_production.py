
# -- coding: utf-8 --

from odoo import models , fields , api



class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    sale_order_id= fields.Many2one('sale.order',readonly = 0 )
   
    is_combination = fields.Boolean(related="sale_order_id.is_combination")

