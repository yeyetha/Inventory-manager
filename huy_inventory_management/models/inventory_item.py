from odoo import models, fields, api

class InventoryItem(models.Model):
    _inherit = 'stock.quant'

    reorder_level = fields.Integer('Reorder Level')
    reorder_alert = fields.Boolean('Reorder Alert', compute='_compute_reorder_alert')
    project_id = fields.Many2one('project.project', 'Linked Project')
    supplier_ids = fields.Many2many('res.partner', string='Suppliers', domain="[('supplier_rank', '>', 0)]")
    
    @api.depends('quantity', 'reorder_level')
    def _compute_reorder_alert(self):
        for item in self:
            item.reorder_alert = item.quantity < item.reorder_level
