from odoo import models, fields

class ProjectBudget(models.Model):
    _inherit = 'project.project'

    budget_amount = fields.Monetary('Project Budget')
    spent_amount = fields.Monetary('Spent Amount', compute='_compute_spent_amount')

    def _compute_spent_amount(self):
        for project in self:
            project.spent_amount = sum(project.task_ids.mapped('material_request_ids.amount'))
