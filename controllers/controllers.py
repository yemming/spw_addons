# -*- coding: utf-8 -*-
from odoo import http

# class SpwAddons(http.Controller):
#     @http.route('/spw_addons/spw_addons/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/spw_addons/spw_addons/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('spw_addons.listing', {
#             'root': '/spw_addons/spw_addons',
#             'objects': http.request.env['spw_addons.spw_addons'].search([]),
#         })

#     @http.route('/spw_addons/spw_addons/objects/<model("spw_addons.spw_addons"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('spw_addons.object', {
#             'object': obj
#         })