# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class server\odoo\addons\pasante_treming-edgard-barrera(models.Model):
#     _name = 'server\odoo\addons\pasante_treming-edgard-barrera.server\odoo\addons\pasante_treming-edgard-barrera'
#     _description = 'server\odoo\addons\pasante_treming-edgard-barrera.server\odoo\addons\pasante_treming-edgard-barrera'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
