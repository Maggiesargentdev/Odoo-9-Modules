{
    'name': "Website Help Desk / Support Ticket",
    'version': "1.3.1",
    'author': "Sythil",
    'category': "Tools",
    'summary': "A helpdesk / support ticket system for your website",
    'license':'LGPL-3',
    'data': [
        'views/website_support_ticket_templates.xml',
        'views/website_support_ticket_views.xml',
        'views/website_support_ticket_categories_views.xml',
        'views/website_support_ticket_states_views.xml',
        'views/res_partner_views.xml',
        'views/res_users_views.xml',
        'views/website_support_help_groups_views.xml',
        'views/website_support_help_page_views.xml',
        'data/website.support.ticket.states.csv',
        'data/website.support.ticket.categories.csv',
        'data/website.menu.csv',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'depends': ['mail','web', 'crm', 'website'],
    'images':[
        'static/description/3.jpg',
        'static/description/1.jpg',
        'static/description/2.jpg',
        'static/description/4.jpg',
        'static/description/5.jpg',
    ],
    'installable': True,
}