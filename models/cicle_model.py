from odoo import models, fields, api


class CicleModel(models.Model):
    _name = 'convalidation_app.cicle_model'
    _description = 'Cicle Model'

    name = fields.Char('Cicle Name', required=True)
    description = fields.Html('Description')  
    modules = fields.One2many("convalidation_app.module_model","cicle","Modules")