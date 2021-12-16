from odoo import models, fields, api


class ConvalidationModel(models.Model):
    _name = 'convalidation_app.convalidation_model'
    _description = 'Convalidation Model'

    date = fields.Date('Convalidation Date', required=True)
    module = fields.Many2one("convalidation_app.module_model","Module")
    student = fields.Many2one("convalidation_app.student_model","Student")
    