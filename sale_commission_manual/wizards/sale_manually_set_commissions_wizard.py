from odoo import api, fields, models


class SaleOrderManuallySetCommissionsWizard(models.TransientModel):
    _name = "sale.order.manual.commissions.wizard"
    _description = "Sales Order Manually Set Commissions Wizard"

    sale_order_id = fields.Many2one("sale.order", string="Sale Order")

    partner_agent_ids = fields.Char(
        compute='_compute_partner_agent_ids', 
        inverse='_inverse_partner_agent_ids', 
        string='Agent Commissions')
    
    @api.depends('sale_order_id.order_line.agent_ids')
    def _compute_partner_agent_ids(self):
        for record in self.order_line:
            for sol in record.sale_order_id.order_line:
                record.partner_agent_ids |= sol.agent_ids

    def _inverse_partner_agent_ids(self):
        for record in self:
            for sol in record.sale_order_id.order_line:
                sol.agent_ids = False  # for resetting previous agents
                if record.sale_order_id.partner_id and not sol.commission_free:
                    sol.agent_ids = [(0, 0, {"agent_id": pia.agent_id.id, "commission_id": pia.commission_id.id}) for pia in record.partner_agent_ids]

class SaleOrderManuallySetCommissionsWizardAgents(models.TransientModel):
    _name = "sale.order.manual.commissions.wizard.agent"
    _description = "Sales Order Manually Set Commissions Wizard Agent"

    agent_id = fields.Many2one(
        comodel_name="res.partner",
        domain="[('agent', '=', True)]",
        required=True
    )
    commission_id = fields.Many2one(
        comodel_name="commission",
        required=True
    )