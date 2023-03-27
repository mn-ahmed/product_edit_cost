# Copyright 2020-2023 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

{
    "name": "Product Edit Cost",
    "summary": """This module protects the 'Cost' field using a group""",
    "version": "16.0.1.0.0",
    "category": "Sale",
    "website": "https://sodexis.com/",
    "author": "Sodexis",
    "license": "OPL-1",
    "installable": True,
    "application": False,
    "depends": [
        "product",
    ],
    "data": [
        "views/product_views.xml",
        "security/ir_security.xml",
    ],
}
