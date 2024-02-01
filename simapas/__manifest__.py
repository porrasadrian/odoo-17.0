# -*- coding: utf-8 -*-
{
    'name': "Simapas Jamay",
    'summary': """
        Module for Simapas Jamay""",
    'description': """
        Module to record jobs, repairs, and drinking water works for Jamay simapas.
    """,
    'author': "Adrian Porras",
    'website': "",
    'category': 'Construction',
    'version': '1.0',
    'depends': ['base', 'mail','stock','purchase'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/repairs_view.xml',
      ]
}
