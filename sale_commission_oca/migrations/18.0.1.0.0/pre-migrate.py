import logging

from odoo.upgrade import util

_logger = logging.getLogger(__name__)



def migrate(cr, version):
    _logger.info("=== Sale commissions OCA PRE-MIGRATION: Starting ===")

    util.rename_module(cr, 'sale_commission', 'sale_commission_oca')

    _logger.info("=== Sale commissions OCA PRE-MIGRATION: Complete ===")
