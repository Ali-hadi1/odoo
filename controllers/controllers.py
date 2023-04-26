# -*- coding: utf-8 -*-
# from odoo import http


# class NlWhatsapp(http.Controller):
#     @http.route('/nl_whatsapp/nl_whatsapp', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nl_whatsapp/nl_whatsapp/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nl_whatsapp.listing', {
#             'root': '/nl_whatsapp/nl_whatsapp',
#             'objects': http.request.env['nl_whatsapp.nl_whatsapp'].search([]),
#         })

#     @http.route('/nl_whatsapp/nl_whatsapp/objects/<model("nl_whatsapp.nl_whatsapp"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nl_whatsapp.object', {
#             'object': obj
#         })
