# -*- coding: utf-8 -*-
from odoo import api, fields, models



class Repairs(models.Model):
    _name = 'repairs'
    _description = 'Model dedicated to repair information'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'id'

    start_date = fields.Date(string="Fecha de inicio", track_visibility='onchange', help="Indique la fecha de incicio")
    end_date = fields.Date(string="Fecha de finalizacion", track_visibility='onchange',
                           help="Indique la fecha de finalizacion")
    location = fields.Char(string="Localizacion", track_visibility="onchange", help="Indique la localizacion")
    municipaly = fields.Selection([('jamay', 'Jamay')], string="Municipio",
                                  track_visibility='onchange', help="¿Cual es el municipio?")
    name_work = fields.Char(string="Nombre del trabajo", track_visibility='onchange',
                            help="Escribe el nombre del trabajo")
    end_date_work = fields.Date(string="Fecha de finalizacion", track_visibility="onchange",
                                help="Indique la fecha de finalizacion")
    coords_x = fields.Char(string="Coordenadas X", track_visibility="onchange", help="Escribe las coordenadas X")
    coords_y = fields.Char(string="Coordenadas Y", track_visibility="onchange", help="Coordenadas Y")
    google_maps_url = fields.Char(string="Google Maps URL", compute='_compute_google_maps_url', store=True)

    @api.depends('coords_x', 'coords_y')
    def _compute_google_maps_url(self):
        for record in self:
            if record.coords_x and record.coords_y:
                record.google_maps_url = f'https://www.google.com/maps?q={record.coords_x},{record.coords_y}'
            else:
                record.google_maps_url = False

    def button_open_google_maps(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'url': self.google_maps_url,
            'target': 'new',
        }

    street_from = fields.Char(string="Entre calle", track_visibility="onchange",
                              help="¿Entre que calles esta el trabajo?")
    street_to = fields.Char(string="Y calle", track_visibility="onchange", help="¿Entre que calles esta el trabajo?")
    details = fields.Text(string="Detalles", track_visibility="onchange", help="Escribe los detalles del trabajo")
    stage_id = fields.Selection(
        [('draft', 'Borrador'), ('initial', 'Inicial'), ('in_progress', 'En proceso'), ('completed', 'Completado'),
         ('cancel', 'Cancelado')],
        default='draft', string="Estados", copy=False)
    active = fields.Boolean(string="Archivado", default=True)
