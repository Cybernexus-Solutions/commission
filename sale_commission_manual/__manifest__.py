# Copyright 2024 Cybernexus Solutions
{
    "name": "Sales commissions - Manually Set Commissions",
    "version": "16.0.1.0.3",
    "author": "Cybernexus Solutions, Odoo Community Association (OCA)",
    "category": "Sales Management",
    "license": "AGPL-3",
    "depends": [
        "sale",
        "sale_commission",
    ],
    "website": "https://github.com/OCA/commission",
    "maintainers": ["cybernexus"],
    "data": [
        "security/ir.model.access.csv",
        "views/sale_order_view.xml",
        "wizards/sale_manually_set_commissions_wizard.xml",
    ],
    "installable": True,
}
