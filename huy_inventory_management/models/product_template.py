from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    
    additional_field = fields.Char(string="Additional Info")
