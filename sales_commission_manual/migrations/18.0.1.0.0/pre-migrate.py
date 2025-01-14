from odoo.upgrade import util

def migrate(cr, version):

    util.rename_module(cr, "sale_commission_manual", "sales_commission_manual")