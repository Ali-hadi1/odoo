from odoo import fields, models, api
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import json
import aiohttp
import asyncio 


class SendMessageToWhatsapp(models.TransientModel):
    _name = 'send.message'

    partner_id = fields.Many2one('res.partner')
    message_body = fields.Text(string="Body")
    document = fields.Binary()


    def action_send(self):
        doc = 'https://www.africau.edu/images/default/sample.pdf'
        data = get_text_message_input('93%s' % self.partner_id.phone, self.message_body)
        # data = get_templated_message_input('93%s' % self.partner_id.phone, doc, self.message_body)
        asyncio.run(send_message(data))


whatsapp_config = {
    "APP_ID": "1434475217376598",
    "APP_SECRET": "8a10177edc9e3dc9544d091bb67ce973",
    "VERSION": "v16.0",
    "PHONE_NUMBER_ID": "121192324283029",
    "ACCESS_TOKEN": "EAAUYpcnFVVYBADpxar4hUH5gBnsb7ZBRfBTWKg2agoy0TdaCCr4RyMI1Cggxhu99aPDVvG6VF5FS0i2OqPCZBAIZC2F62bz6PwZAX0Ic3Bdp40ExvVjAZBqgIRa8i6EkLQCmORGdaavmgdzxo6s9QiCb8BkofUohyFGZAy2AnZBWRVpGgAvjPiARha1N0kqUc9bzwvfauzzswZDZD"
}   

async def send_message(data):
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {whatsapp_config['ACCESS_TOKEN']}",
        }
    
    async with aiohttp.ClientSession() as session:
        url = 'https://graph.facebook.com' + f"/{whatsapp_config['VERSION']}/{whatsapp_config['PHONE_NUMBER_ID']}/messages"
        try:
            async with session.post(url, data=data, headers=headers) as response:
                if response.status == 200:
                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>', "Status:", response.status)
                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', "Content-type:", response.headers['content-type'])

                    html = await response.text()
                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', "Body:", html)
                else:
                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', response.status)        
                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', response)        
        except aiohttp.ClientConnectorError as e:
            print('Connection Error', str(e))

def get_text_message_input(recipient, text):
    return json.dumps({
        "messaging_product": "whatsapp",
        "preview_url": False,
        "recipient_type": "individual",
        "to": recipient,
        "type": "text",
        "text": {
            "body": text
        }
    })

def get_templated_message_input(recipient, document, message_body):
  return json.dumps({
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": recipient,
    "type": "template",
    "template": {
        "name": "payment_resat_template",
        "language": {
            "code": "en_US"
        },
        "components": [
            {
                "type": "header",
                "parameters": [
                {
                    "type": "document",
                    "document": {
                        "filename": "payment_raset.pdf",
                        "link": document
                    }
                }
                ]
            },
            {
                "type": "body",
                "parameters": [
                    {
                        "type": "text",
                        "text": message_body
                    }
                ]
            },
        ]}
    })

    #sending message to whatsapp with twilio
    # def action_send(self):
    #     account_sid = 'AC987480cc56c709ec7326ba5a26251097'
    #     auth_token = '27b152dbc5d7ff3807718f80825260eb'

    #     client = Client(account_sid, auth_token)
       
    #     try:
    #         message = client.messages.create(
    #                 media_url='https://www.africau.edu/images/default/sample.pdf',
    #                 from_='whatsapp:+14155238886',
    #                 body=self.message_body,
    #                 to='whatsapp:+93773714746'
    #             )
                                            
    #     except TwilioRestException as e:
    #         print(e)