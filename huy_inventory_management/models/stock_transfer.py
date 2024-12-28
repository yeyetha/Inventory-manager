from odoo import models, fields

class StockTransfer(models.Model):
    _inherit = 'stock.picking'

    transfer_status = fields.Selection([
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='pending', string='Transfer Status')
    
    def approve_transfer(self):
        self.write({'transfer_status': 'approved'})

    def generate_purchase_order(self):
        # Generate a purchase order if needed
        pass
