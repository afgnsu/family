# -*- coding: utf-8 -*-
from odoo import http

# class Family(http.Controller):
#     @http.route('/family/family/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/family/family/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('family.listing', {
#             'root': '/family/family',
#             'objects': http.request.env['family.family'].search([]),
#         })

#     @http.route('/family/family/objects/<model("family.family"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('family.object', {
#             'object': obj
#         })