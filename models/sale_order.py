from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "task"

    def update_button(self):
        print(self.env.context)
        if self.env.context.get("code_match_sale"):
            pass
