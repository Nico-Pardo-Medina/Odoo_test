{
    'name': 'Helpdesk Ticket',
    'version': '1.0',
    'description': 'Modulo de gestión de tickets de soporte',
    'author': 'Nico Pardo Medina',
    'category': 'Custom',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/helpdesk_ticket_view.xml',
    ],
    'installable': True,
    'application': True,
    'demo': [
        'demo/demo_data.xml',
    ],
}