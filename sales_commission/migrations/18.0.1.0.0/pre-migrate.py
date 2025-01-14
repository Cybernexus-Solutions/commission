from odoo.upgrade import util

def migrate(cr, version):

    util.rename_module(cr, "sale_commission", "sales_commission")