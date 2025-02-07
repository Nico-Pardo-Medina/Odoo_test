{
    'name': 'Helpdesk Ticket',
    'version': '1.0',
    'summary': 'Modulo de gestión de tickets de soporte',
    'author': 'Tu Nombre',
    'category': 'Services',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/helpdesk_ticket_view.xml',
    ],
    'installable': True,
    'application': True,
}