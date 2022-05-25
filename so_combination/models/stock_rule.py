# -- coding: utf-8 --

from odoo import models , fields

class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _prepare_mo_vals(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values, bom):
        res = super()._prepare_mo_vals(product_id, product_qty, product_uom, location_id, name, origin, company_id, values, bom)
        if values['group_id']:
            res['sale_order_id'] = values['group_id'].sale_id.id or False
        return res
