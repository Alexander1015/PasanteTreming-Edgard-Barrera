# -*- coding: utf-8 -*-
# from odoo import http


# class Server\odoo\addons\pasanteTreming-edgard-barrera(http.Controller):
#     @http.route('/server\odoo\addons\pasante_treming-edgard-barrera/server\odoo\addons\pasante_treming-edgard-barrera/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/server\odoo\addons\pasante_treming-edgard-barrera/server\odoo\addons\pasante_treming-edgard-barrera/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('server\odoo\addons\pasante_treming-edgard-barrera.listing', {
#             'root': '/server\odoo\addons\pasante_treming-edgard-barrera/server\odoo\addons\pasante_treming-edgard-barrera',
#             'objects': http.request.env['server\odoo\addons\pasante_treming-edgard-barrera.server\odoo\addons\pasante_treming-edgard-barrera'].search([]),
#         })

#     @http.route('/server\odoo\addons\pasante_treming-edgard-barrera/server\odoo\addons\pasante_treming-edgard-barrera/objects/<model("server\odoo\addons\pasante_treming-edgard-barrera.server\odoo\addons\pasante_treming-edgard-barrera"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('server\odoo\addons\pasante_treming-edgard-barrera.object', {
#             'object': obj
#         })
