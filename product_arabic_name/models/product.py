from odoo import fields, api, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    arabic_name = fields.Char('Arabic Name')

