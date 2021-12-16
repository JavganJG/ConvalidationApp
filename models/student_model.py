# -*- coding: utf-8 -*-
import random
import string
from odoo import models, fields, api


class StudentModel(models.Model):
    _name = 'convalidation_app.student_model'
    _description = 'Student Model'

    name = fields.Char('Student Name', required=True)
    password = fields.Char('Password', required=True)    
    image = fields.Image('Image')
    age = fields.Integer('Age')
    city = fields.Char('City')
    province = fields.Char('Province')
    email = fields.Char('Email')
    convalidations = fields.One2many("convalidation_app.convalidation_model","student","Convalidations")

    def resetPassword(self):
        self.ensure_one()
        self.password = ''.join(random.choice(string.printable) for i in range(8))
