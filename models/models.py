# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import os



class nl_whatsapp(models.Model):
    _name = 'whatsapp.model'
    _description = ''

    name = fields.Char()
    username = fields.Char(string='UserName')
    phone = fields.Char(string='Phone')

    def action_send_message(self):

        return self.env.ref("nl_whatsapp.action_send_message").sudo().read()[0]

        # if not self.phone:
        #     raise ValidationError("Phone number doesn't exist!")
        # whatsapp_api_url = 'https://api.whatsapp.com/send?phone=%s&text=%s' % (self.phone, self.name)

        # return {
        #     'type': 'ir.actions.act_url',
        #     'target': 'new',
        #     'url': whatsapp_api_url
        # }

