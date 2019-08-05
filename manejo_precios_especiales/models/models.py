# -*- coding: utf-8 -*-

from odoo import models, fields, api
from openerp.exceptions import UserError, RedirectWarning, ValidationError


# class add_sales(models.Model):
#     _name = 'add_sales.add_sales'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
#         

class add_campos(models.Model):
    _inherit = 'sale.order.line'  


    public_price = fields.Float(string="Precio Publico" , related='product_id.lst_price', default=0.0, readonly=True,)
    especial_price= fields.Float(string="Precio especial", compute="_compute_amount2")


    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
    def _compute_amount2(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            if line.discount !=0.00:
                if line.discount <=20:
                    price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
                    taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_shipping_id)
                    line.update({
                        'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                        'price_total': taxes['total_included'],
                        'especial_price': taxes['total_excluded'],
                    })
                else:
                    raise ValidationError('Porcentaje es mayor a lo permitido.') 