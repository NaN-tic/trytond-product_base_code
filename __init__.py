# This file is part product_base_code module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import product

def register():
    Pool.register(
        product.Template,
        module='product_base_code', type_='model')
