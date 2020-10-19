# -*- coding: utf-8 -*-
# Copyright 2020 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

{
    'name': "Product Edit Cost",
    'summary': """
        This tinyapp is used to edit product cost if using the FIFO system.""",
    'version': '11.0.1.0.0',
    'category': 'Sale',
    'website': "http://sodexis.com/",
    'author': "Sodexis",
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'depends': [
        'stock_account',
    ],
    'data': [
        'views/product_views.xml',
    ],
}