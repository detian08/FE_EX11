# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime
from odoo.exceptions import UserError
from odoo.tools import float_compare, float_round, float_is_zero
class MrpProductProduce(models.TransientModel):
    _inherit = 'mrp.product.produce'

    final_product_lot = fields.Many2one('stock.production.lot', string='Lot')

    @api.onchange('serial')
    def get_lot_sale(self):
        self.lot_id = self.final_product_lot
