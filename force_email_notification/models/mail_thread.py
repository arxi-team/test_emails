# -*- coding: utf-8 -*-
import logging
from odoo import models

_logger = logging.getLogger(__name__)


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    # Push Notification
    def _notify_thread(self, message, msg_vals=False, notify_by_email=True, **kwargs):
        return super(MailThread, self)._notify_thread(message, msg_vals, True, **kwargs)
