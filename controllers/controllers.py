# -*- coding: utf-8 -*-
# from odoo import http


# class ConvalidationApp(http.Controller):
#     @http.route('/convalidation_app/convalidation_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/convalidation_app/convalidation_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('convalidation_app.listing', {
#             'root': '/convalidation_app/convalidation_app',
#             'objects': http.request.env['convalidation_app.convalidation_app'].search([]),
#         })

#     @http.route('/convalidation_app/convalidation_app/objects/<model("convalidation_app.convalidation_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('convalidation_app.object', {
#             'object': obj
#         })
