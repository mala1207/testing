# -*- coding: utf-8 -*-
from odoo import http

# class ./pscloudTraining(http.Controller):
#     @http.route('/./pscloud_training/./pscloud_training/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./pscloud_training/./pscloud_training/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('./pscloud_training.listing', {
#             'root': '/./pscloud_training/./pscloud_training',
#             'objects': http.request.env['./pscloud_training../pscloud_training'].search([]),
#         })

#     @http.route('/./pscloud_training/./pscloud_training/objects/<model("./pscloud_training../pscloud_training"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./pscloud_training.object', {
#             'object': obj
#         })