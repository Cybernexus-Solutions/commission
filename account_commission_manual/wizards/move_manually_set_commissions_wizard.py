from odoo import api, fields, models, Command


class AccountMoveManuallySetCommissionsWizard(models.TransientModel):
    _name = "account.move.manual.commissions.wizard"
    _description = "Sales Order Manually Set Commissions Wizard"

    account_move_id = fields.Many2one("account.move", string="Sale Order")

    account_move_partner_id = fields.Many2one(related='account_move_id.partner_id', string='Sales Order Customer')

    partner_agent_ids = fields.One2many(
        comodel_name='account.move.manual.commissions.wizard.agent',
        inverse_name='manual_commission_wizard_id',
        string='Agent Commissions')
   
    def action_save_commissions(self):
        for sol in self.account_move_id.order_line.filtered(lambda x: not x.commission_free):
            sol.agent_ids = False  # for resetting previous agents
            for pia in self.partner_agent_ids:
                if pia.agent_id and pia.commission_id:
                    sol.agent_ids = [(0,0, {"agent_id": pia.agent_id.id, "commission_id": pia.commission_id.id})] 

    def action_reset_default_commissions(self):
        self.account_move_id.recompute_lines_agents()

class SaleOrderManuallySetCommissionsWizardAgents(models.TransientModel):
    _name = "account.move.manual.commissions.wizard.agent"
    _description = "Sales Order Manually Set Commissions Wizard Agent"

    manual_commission_wizard_id = fields.Many2one('account.move.manual.commissions.wizard', string='Manual Commission Wizard')
    
    agent_id = fields.Many2one(
        comodel_name="res.partner",
        domain="[('agent', '=', True)]",
        required=True
    )
    commission_id = fields.Many2one(
        comodel_name="commission",
        required=True
    )