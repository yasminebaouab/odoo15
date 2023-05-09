# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectEmployee(http.Controller):
#     @http.route('/project_employee/project_employee', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_employee/project_employee/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_employee.listing', {
#             'root': '/project_employee/project_employee',
#             'objects': http.request.env['project_employee.project_employee'].search([]),
#         })

#     @http.route('/project_employee/project_employee/objects/<model("project_employee.project_employee"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_employee.object', {
#             'object': obj
#         })
