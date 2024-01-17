from odoo import models, fields, api


class SaleOrderLines(models.Model):
    _inherit = "sale.order.line"
    _description = "task"


