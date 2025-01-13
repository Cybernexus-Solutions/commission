# Copyright 2024 Cybernexus Solutions
{
    "name": "Account commissions - Manually Set Commissions",
    "version": "17.0.1.0.3",
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
        "views/account_move_view.xml",
        "wizards/move_manually_set_commissions_wizard.xml",
    ],
    "installable": True,
}
