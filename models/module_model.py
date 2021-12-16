from odoo import models, fields, api


class ModuleModel(models.Model):
    _name = 'convalidation_app.module_model'
    _description = 'Module Model'

    name = fields.Char('Module Name', required=True)
    description = fields.Html('Description')    
    hours = fields.Integer('Hours')
    convalidations = fields.One2many("convalidation_app.convalidation_model","module","Convalidations")
    cicle = fields.Many2one("convalidation_app.cicle_model","Cicle")


