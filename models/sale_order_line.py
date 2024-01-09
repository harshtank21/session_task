from odoo import models, fields, api


class SaleOrderLines(models.Model):
    _inherit = "sale.order.line"
    _description = "task"

    # sale_order = fields.Many2many("product.template", string="Sale Order")
    # quotation = fields.Many2many("product.template", string="Quotation")
    # sale_orders= fields.Many2many("product.template", string="Sale Order")
    # quotations = fields.Many2many("product.template", string="Quotation")
    orders = fields.Char(string="Sale Order")
    quot = fields.Char(string="Quotation")

    def create(self, vals):
        print("------------->",self.env.context)
        return super(SaleOrderLines, self).create(vals)
