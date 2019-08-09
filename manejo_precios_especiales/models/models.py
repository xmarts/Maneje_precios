# -*- coding: utf-8 -*-

from odoo import models, fields, api
from openerp.exceptions import UserError, RedirectWarning, ValidationError


class add_campos(models.Model):
    _inherit = 'sale.order.line'  


    public_price = fields.Float(string="Precio Publico" , related='product_id.lst_price', default=0.0, readonly=True,)
    especial_price= fields.Float(string="Precio especial", compute="_compute_amount2")

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id','order_id')
    def _compute_amount2(self):

        for line in self:
            if line.discount !=0.00:
                if line.discount <=20:
                    line.order_id.dis =True
                    price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
                    taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_shipping_id)
                    line.update({
                        'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                        'price_total': taxes['total_included'],
                        'especial_price': taxes['total_excluded'],
                    })
                else:
                    raise ValidationError('Porcentaje es mayor a lo permitido.')
            else:
                line.order_id.dis=False       

class campo_tru(models.Model):
        _inherit = 'sale.order'  
        
        dis = fields.Boolean(string="true")