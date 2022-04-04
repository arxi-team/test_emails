# -*- coding: utf-8 -*-

from odoo import api, fields, models, Command
import logging

_logger = logging.getLogger(__name__)


class Followers(models.Model):
    _inherit = 'mail.followers'

    def _get_recipient_data(self, records, message_type, subtype_id, pids=None):
        res = super(Followers, self)._get_recipient_data(records, message_type, subtype_id, pids=pids)
        _logger.info(f"IM RUNINT WITH {records} and my pids are {pids}")
        _logger.info(f"THE DATA THAT I GOT FROM SUPER IS {res}")
        # for pid, active, pshare, notif, groups in res:
        return res



