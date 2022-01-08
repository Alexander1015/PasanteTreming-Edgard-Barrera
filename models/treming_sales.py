# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class TremingSales(models.Model):
    _inherit = 'sale.order'

    # all_cliente = fields.Many2one('res.partner', string='Clientes')
    sucursal = fields.Many2one('treming.sucursales', string='Sucursal', domain="[('name','=','partner_id.sucursal')]")
    
    @api.onchange('partner_id')
    def _onchange_parent_id(self):
        self.sucursal = ""
        for s in self:
            _logger.info(s)
            s.sucursal = s.partner_id.sucursal