# -*- coding: utf-8 -*-

from odoo import models,fields,api

class ResPartner(models.Model): 
    _inherit ='res.partner'

    #------------------------
    #  fields Declaration
    #------------------------

    party_type = fields.Selection([
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
        
    ])


   
    