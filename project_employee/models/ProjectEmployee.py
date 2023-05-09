# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectEmployeeWeight(models.Model):
    _name = 'project.employee'


    project_id = fields.Many2one('project.project', string='Project', required=True, ondelete='cascade', index=True)
    weight = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10')], default='1', string="weight")

    employee_ids = fields.Many2many('hr.employee', required=True)
