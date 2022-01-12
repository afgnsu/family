# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Child(models.Model):
    _name = "family.child"
    _description = "子女"

    name = fields.Char(string="姓名", required=True)
    sex = fields.Selection([("M", "男"), ("F", "女")], string="性別", default="M")
    age = fields.Integer(string="歲")
    parent_ids = fields.Many2many("family.parent", "family_child_parent_rel", "child_id", "parent_id", string="父母")
    pet_ids = fields.One2many("family.pet", "master", "寵物")