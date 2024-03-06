from odoo import _, api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def manually_set_commissions(self):
        agents = {}
        for pia in self.line_ids.mapped("agent_ids"):
            key = (pia.agent_id.id, pia.commission_id.id)
            if key not in agents:
                agents[key] = {'agent_id': pia.agent_id.id, 'commission_id': pia.commission_id.id}

        action = {
            "name": _("Manually Set Commissions"),
            "view_mode": "form",
            "res_model": "account.move.manual.commissions.wizard",
            "view_id": self.env.ref(
                "account_commission_manual.account_move_manual_commissions_wizard_view_form"
            ).id,
            "type": "ir.actions.act_window",
            "context": {
                "default_acount_move_id": self.id,
                "default_partner_agent_ids": [(0,0, agents[key] ) for key in agents.keys()]
            },
            "target": "new",
        }
        return action