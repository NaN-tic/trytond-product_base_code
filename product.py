# This file is part product_base_code module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta

__all__ = ['Template']
__metaclass__ = PoolMeta


class Template:
    __name__ = "product.template"
    base_code = fields.Char('Base Code', help='Base Code Product Template')
