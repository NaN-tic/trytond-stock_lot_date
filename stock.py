# This file is part stock_lot_date module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta

__all__ = ['Lot']


class Lot(metaclass=PoolMeta):
    __name__ = 'stock.lot'
    lot_date = fields.Date('Date Lot', required=True)

    @classmethod
    def __setup__(cls):
        super(Lot, cls).__setup__()
        cls._order.insert(0, ('lot_date', 'DESC'))
        cls._order.insert(1, ('id', 'DESC'))

    @staticmethod
    def default_lot_date():
        Date = Pool().get('ir.date')
        return Date.today()
