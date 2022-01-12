# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Pet(models.Model):
    _name = "family.pet"
    _description = "寵物"

    name = fields.Char(string="名字", required=True)
    sex = fields.Selection([("M", "男"), ("F", "女")], string="性別", default="M")
    age = fields.Integer(string="歲")
    master = fields.Many2one("family.child", string="主人")