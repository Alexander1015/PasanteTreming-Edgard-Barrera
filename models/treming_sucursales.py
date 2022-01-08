# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class TremingSucursales(models.Model):
    _name='treming.sucursales'
    
    name = fields.Char(string='Nombre', required=True)
    name_corto = fields.Char(string='Nombre corto', required=True)
    compania = fields.Many2one('res.partner', string='Compañia', required=True, domain="[('is_company','=','is_company')]")