# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict
import math

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import AccessError, UserError
from odoo.tools import float_compare

class MrpProduction(models.Model):
    """ Manufacturing Orders """
    _inherit = 'mrp.workorder'

    def open_tablet_all_view(self):
        qty_production = self.qty_production
        qty_produced = self.qty_produced
        for qty in range(int(qty_produced),int(qty_production)):
            correlativo= self.env['ir.sequence'].next_by_code('mrp.series')
            barcode = self.production_id.product_id.as_sku
            self.final_lot_id = self.env['stock.production.lot'].create({
                'name': str(barcode)+str(correlativo),
                'product_id': self.production_id.product_id.id,
                'ref': correlativo,
            })
            self.record_production()
            if qty_produced == qty_production:
                self.do_finish()



       