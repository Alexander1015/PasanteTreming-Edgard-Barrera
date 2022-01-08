# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class TremingContactos(models.Model):
    _inherit = 'res.partner'
    
    dui = fields.Char(string='DUI', size=9, required=True)
    nit = fields.Char(string='NIT', size=17, required=False)
    nrc = fields.Char(string='NRC', required=False)
    sucursal = fields.Many2one('treming.sucursales', string='Sucursal', required=True, domain="[('compania','=',parent_id)]")
    
    @api.onchange('parent_id')
    def _onchange_parent_id(self):
        self.sucursal = ""