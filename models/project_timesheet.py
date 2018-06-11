# -*- coding: utf-8 -*-

from odoo import models, fields, api

class spw_project_task(models.Model):
    _inherit = "project.task"

    hourly_rate_task = fields.Integer(string="Hourly rate")
    task_type = fields.Many2one('spw.tasks.type', ondelete='set null', string="Type")

class spw_account_analytic_line(models.Model):
    _inherit = "account.analytic.line"

    #hourly_rate_timesheet = fields.Integer(string="Hourly rate", compute='_hourly_rate_timesheet')
    hourly_rate_timesheet = fields.Integer(string="Hourly rate", default=lambda self: self._get_default_hourly_rate())
    #hourly_rate_timesheet = fields.Integer(string="Hourly rate")
    hourly_rate_timesheet_total = fields.Integer(string="Hourly rate Total", compute='_hourly_rate_timesheet_total')
    report_date = fields.Date(string="Report Submit Date")
    task_type = fields.Many2one('spw.tasks.type', ondelete='set null', string="Type" ,default=lambda self: self._get_default_type())





    #@api.depends('unit_amount', 'hourly_rate_timesheet')
    #def _hourly_rate_timesheet(self):
    #    for r in self:
    #        r.hourly_rate_timesheet = r.task_id.hourly_rate_task

    @api.depends('unit_amount','hourly_rate_timesheet')
    def _hourly_rate_timesheet_total(self):
        for r in self:
            r.hourly_rate_timesheet_total = r.hourly_rate_timesheet * r.unit_amount

    @api.model
    def _get_default_hourly_rate(self):
        return self.env['project.task'].search([('id','=',self._context.get('default_my_taks_id'))]).hourly_rate_task

    def _get_default_type(self):
        return self.env['project.task'].search([('id', '=', self._context.get('default_my_taks_id'))]).task_type


class spw_task_type(models.Model):
    _name = "spw.tasks.type"
    name = fields.Char(string="Task Type")