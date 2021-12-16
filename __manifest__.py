# -*- coding: utf-8 -*-
{
    'name': "convalidation_app",

    'summary': """
        This app is an app to convalidate student modules""",

    'description': """
        This app is an app to convalidate student modules and manage information of modules and students
    """,

    'author': "Jasban S.A",
    'website': "http://www.jasban.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/ir.model.access.csv',
        'views/module_view.xml',
        'views/student_view.xml',
        'views/cicle_view.xml',
        'views/convalidation_view.xml',
        'views/menu.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
