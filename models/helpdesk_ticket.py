from odoo import models, fields

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'

    name = fields.Char(string='Nombre del ticket', required=True)
    partner_id = fields.Many2one('res.partner', string='Cliente')
    state = fields.Selection([
        ('new', 'nuevo'),
        ('in_progress', 'en progreso'),
        ('resolved', 'resuelto')
    ], string='Estado', default='new', readonly=True)
    description = fields.Text(string='Descripción del problema')
    create_date = fields.Datetime(string='Fecha de creación', default=fields.Datetime.now, readonly=True)
    user_id = fields.Many2one('res.users', string='Usuario asignado')

    def action_mark_resolved(self):
        self.state = 'resolved'