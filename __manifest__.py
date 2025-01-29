# -*- coding: utf-8 -*-
{
    'name': 'Tax Invoice Custom',
    'version': '17.0.3.0.5',
    'category': 'Accounting',
    'summary': """
        Tax Invoice Customizations
    """,
    'description': """
        Module for customizing the Tax Invoice report.
    """,
    'author': 'Amr Gebil',
    'depends': [
        'base',
        'account',
    ],
    'data': [
        'reports/tax_invoice_report.xml',  # Ensure the XML file exists and is valid
    ],

    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
