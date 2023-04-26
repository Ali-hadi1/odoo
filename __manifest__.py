# -*- coding: utf-8 -*-
{
    'name': "nl_whatsapp",

    'summary': """""",
    'author': 'NETLINKS LTD',
    'website': 'www.netlinks.af',
    'support': 'info@netlinks.af',
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'wizard/send_message_to_whatsapp.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
