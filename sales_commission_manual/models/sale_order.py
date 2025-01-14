from odoo import _, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def manually_set_commissions(self):
        agents = {}
        for pia in self.order_line.mapped("agent_ids"):
            key = (pia.agent_id.id, pia.commission_id.id)
            if key not in agents:
                agents[key] = {
                    "agent_id": pia.agent_id.id,
                    "commission_id": pia.commission_id.id,
                }

        action = {
            "name": _("Manually Set Commissions"),
            "view_mode": "form",
            "res_model": "sale.order.manual.commissions.wizard",
            "view_id": self.env.ref(
                "sale_commission_manual.sale_order_manual_commissions_wizard_view_form"
            ).id,
            "type": "ir.actions.act_window",
            "context": {
                "default_sale_order_id": self.id,
                "default_partner_agent_ids": [
                    (0, 0, agents[key]) for key in agents.keys()
                ],
            },
            "target": "new",
        }
        return action
