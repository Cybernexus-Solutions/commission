from . import models


def _pre_init_sale_commission(cr):
    """ Allow installing sale_commision in databases with large sale.order table (>1M records)
        - Creating the computed+stored field commission_total and
          partner_agent_ids is terribly slow with the ORM and leads to "Out of
          Memory" crashes
    """
    cr.execute("""ALTER TABLE "sale_order" ADD COLUMN "commission_total" double precision;""")
    cr.execute("""UPDATE sale_order
                     SET commission_total=0;""")