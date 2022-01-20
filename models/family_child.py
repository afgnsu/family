# -*- coding: utf-8 -*-
from odoo import models, fields, api

class FamilyChild(models.Model):
    _name = "family.child"
    _description = "子女"
    _order = "age desc"

    name = fields.Char(string="姓名", required=True)
    sex = fields.Selection([("M", "男"), ("F", "女")], string="性別", default="M")
    age = fields.Integer(string="歲")
    parent_ids = fields.Many2many(comodel_name="family.parent", relation="family_child_parent_rel", column1="child_id", column2="parent_id", string="父母")
    pet_ids = fields.One2many(comodel_name="family.pet", inverse_name="master", string="寵物")