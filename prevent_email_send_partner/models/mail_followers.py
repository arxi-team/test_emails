# -*- coding: utf-8 -*-

from odoo import models
import logging

_logger = logging.getLogger(__name__)


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    def _notify_compute_recipients(self, message, msg_vals):
        recipients_data = super(MailThread, self)._notify_compute_recipients(message, msg_vals)
        return_list = []
        if msg_vals.get('author_id'):
            author_user_id = self.env['res.users'].search([('partner_id', '=', msg_vals['author_id'])])
            if author_user_id and author_user_id.has_group('base.group_user'):
                return recipients_data
            for data in recipients_data:
                user_id = self.env['res.users'].search([('partner_id', '=', data['id'])])
                if user_id and user_id.has_group('base.group_user'):
                    return_list.append(data)
            return return_list
        return recipients_data






