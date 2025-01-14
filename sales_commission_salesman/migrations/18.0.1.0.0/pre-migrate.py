from odoo.upgrade import util

def migrate(cr, version):

    util.rename_module(cr, "sale_commission_salesman", "sales_commission_salesman")