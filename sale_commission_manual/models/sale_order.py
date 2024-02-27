from odoo import _, api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def manually_set_commissions(self):
        action = {
            "name": _("Manually Set Commissions"),
            "view_mode": "form",
            "res_model": "sale.order.manual.commissions.wizard",
            "view_id": self.env.ref(
                "sale_commission_manual.sale_order_manually_set_commissions_wizard_view_form"
            ).id,
            "type": "ir.actions.act_window",
            "context": {
                "default_sale_order_id": self.id,
            },
            "target": "new",
        }
        return action