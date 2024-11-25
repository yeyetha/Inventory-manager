from odoo import models, fields, api

class MaterialRequest(models.Model):
    _inherit = 'stock.picking'

    project_id = fields.Many2one('project.project', 'Related Project')
    approver_id = fields.Many2one('res.users', 'Approver', readonly=True)
    request_status = fields.Selection([
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='pending', string='Request Status')

    def submit_request(self):
        self.write({'request_status': 'pending'})

    def approve_request(self):
        self.write({'request_status': 'approved', 'approver_id': self.env.user.id})

    def reject_request(self):
        self.write({'request_status': 'rejected', 'approver_id': self.env.user.id})
