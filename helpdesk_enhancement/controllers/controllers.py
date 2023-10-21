# -*- coding: utf-8 -*-
# from odoo import http


# class HelpdeskEnhancement(http.Controller):
#     @http.route('/helpdesk_enhancement/helpdesk_enhancement', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/helpdesk_enhancement/helpdesk_enhancement/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('helpdesk_enhancement.listing', {
#             'root': '/helpdesk_enhancement/helpdesk_enhancement',
#             'objects': http.request.env['helpdesk_enhancement.helpdesk_enhancement'].search([]),
#         })

#     @http.route('/helpdesk_enhancement/helpdesk_enhancement/objects/<model("helpdesk_enhancement.helpdesk_enhancement"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('helpdesk_enhancement.object', {
#             'object': obj
#         })
