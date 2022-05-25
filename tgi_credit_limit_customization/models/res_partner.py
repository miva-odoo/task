# -*- coding: utf-8 -*-

from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    #--------------------------------
    # Fields declaration
    #--------------------------------
    
    credit_limit = fields.Integer(string='Credit Limit')
    total_receivable = fields.Integer(string='Total Receivable')
    #credit_limit_approver = fields.many2many('res.partner', string='Credit Limit Approver')
    #override_credit_limit = fields.Boolean(string="Override Credit Limit")