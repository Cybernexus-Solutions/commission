import logging

from odoo.upgrade import util

_logger = logging.getLogger(__name__)



def migrate(cr, version):
    _logger.info("=== Account commissions OCA PRE-MIGRATION: Starting ===")

    util.rename_module(cr, 'account_commission', 'account_commission_oca')

    _logger.info("=== Account commissions OCA PRE-MIGRATION: Complete ===")
