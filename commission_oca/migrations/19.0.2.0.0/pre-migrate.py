from openupgradelib import openupgrade

from odoo.upgrade import util


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.rename_fields(
        env,
        [
            (
                "res.partner",
                env["res.partner"]._table,
                "agent_ids",
                "commission_agent_ids",
            ),
        ],
    )

    util.add_to_migration_reports(
        "- Renamed `res.partner.agent_ids` → `commission_agent_ids`",
        category="commission_oca",
        format="md",
    )
