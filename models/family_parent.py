# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Parent(models.Model):
    _name = "family.parent"
    _description = "父母"

    name = fields.Char(string="姓名", required=True, help="必填")
    sex = fields.Selection([("M", "男"), ("F", "女")], string="性別", default="M")
    age = fields.Integer(string="歲")
    is_retaird = fields.Boolean(string="退休", default=True)
    child_ids = fields.Many2many("family.child", "family_child_parent_rel", "parent_id", "child_id", string="兒女")