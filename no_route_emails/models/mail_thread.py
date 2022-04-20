import logging
from odoo import api, models, tools, fields

_logger = logging.getLogger(__name__)


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    @api.model
    def message_route(self, message, message_dict, model=None, thread_id=None, custom_values=None):

        try:
            return super(MailThread, self).message_route(message, message_dict, model, thread_id, custom_values)
        except ValueError as e:

            record = self.env['no.route.email'].create({
                'name': message_dict.get('subject'),
                'email_from': message_dict.get('from'),
                'email_to': message_dict.get('to'),
                'email_cc': message_dict.get('cc'),
                'date': message_dict.get('date'),
                'body': message_dict.get('body')

            })
            user = self.env['ir.config_parameter'].sudo().get_param('no_route_emails.user', 0) or self.env.user.id
            record.activity_schedule('mail.mail_activity_data_todo', fields.Date.today(),  message_dict.get('subject'), user_id=user)
        return []
