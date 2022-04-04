# -*- coding: utf-8 -*-

from odoo import api, fields, models, Command
import logging

_logger = logging.getLogger(__name__)


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    def _notify_compute_recipients(self, message, msg_vals):
        recipients_data = super(MailThread, self)._notify_compute_recipients(message, msg_vals)
        _logger.info(f"At _notify_compute_recipients i got the message [{message}] and the vals are [{msg_vals}]")
        _logger.info(f"--------From super i got {recipients_data}")

        return recipients_data



