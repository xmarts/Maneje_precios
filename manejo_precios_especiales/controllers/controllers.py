# -*- coding: utf-8 -*-
from odoo import http

# class AddSales(http.Controller):
#     @http.route('/add_sales/add_sales/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_sales/add_sales/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_sales.listing', {
#             'root': '/add_sales/add_sales',
#             'objects': http.request.env['add_sales.add_sales'].search([]),
#         })

#     @http.route('/add_sales/add_sales/objects/<model("add_sales.add_sales"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_sales.object', {
#             'object': obj
#         })