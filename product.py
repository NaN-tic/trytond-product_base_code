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

    @classmethod
    def create(cls, vlist):
        for vals in vlist:
            if 'base_code' in vals:
                if 'products' in vals:
                    product = vals['products'][0]
                    if product[0] == 'create':
                        for prod_vals in product[1]:
                            if 'code' in prod_vals and not prod_vals['code']:
                                prod_vals['code'] = vals['base_code']
                                break
        return super(Template, cls).create(vlist)

    @classmethod
    def write(cls, *args):
        actions = iter(args)
        args = []
        for templates, values in zip(actions, actions):
            if 'base_code' in values:
                for template in templates:
                    for product in template.products:
                        if not product.code:
                            product.code = values['base_code']
                            product.save()
                            break
            args.extend((templates, values))
        super(Template, cls).write(*args)
