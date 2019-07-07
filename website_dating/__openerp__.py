{
    'name': "Website Dating (Giga Mega Ultra Super Pre Alpha)",
    'version': "0.2",
    'author': "Sythil",
    'category': "Tools",
    'summary': "A directory of single people",
    'license':'LGPL-3',
    'data': [
        'views/res_dating_views.xml',
        'views/res_partner_views.xml',
        'views/res_country_state_city.xml',
        'views/res_country_state_city_import.xml',
        'views/res_country_state_views.xml',
        'views/website_dating_templates.xml',
        'views/res_dating_questionnaire_views.xml',
        'views/res_dating_questionnaire_answer_views.xml',
        'data/ir.cron.csv',
        'data/res.dating.fake.first.csv',
        'data/res.dating.fake.last.csv',
        'data/res.partner.gender.csv',
        'data/website.menu.csv',
        'data/res.partner.relationship.csv',
        'data/res.groups.csv',
        'data/ir.rule.csv',
        'data/res.sexualorientation.csv',
        'demo/res.dating.questionnaire.csv',
        'demo/res.dating.questionnaire.question.csv',
        'demo/res.dating.questionnaire.question.option.csv',
        'demo/res.dating.questionnaire.matchingrules.csv',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'depends': ['crm', 'website'],
    'images':[
        'static/description/1.jpg',
    ],
    'installable': True,
}