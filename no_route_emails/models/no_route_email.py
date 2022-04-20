import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class NoRouteEmail(models.Model):
    _name = 'no.route.email'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Emails without route"

    name = fields.Char(string='Subject')
    email_from = fields.Char()
    email_to = fields.Char()
    email_cc = fields.Char()
    date = fields.Datetime()
    body = fields.Html()
