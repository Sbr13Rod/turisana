# -*- coding: utf-8 -*-

from odoo import _, models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools import image_resize_images

import logging

_logger = logging.getLogger(__name__)

class Productos(models.Model):
    _name='productos.turisana'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripcion')
    temporada = fields.Selection(
        [
            ('Verano','Verano'),
            ('Invierno','Invierno'),
        ],
		string='Temporada',
		track_visibility='onchange',
		required = True,
	)
    imagen_producto = fields.Binary(string='Imagen')
    fecha_inicio = fields.Date(string='Inicio Temporada', readonly=true)
    fecha_fin = fields.Date(string='Final Temporada', readonly=true)

    @api.multi
    def write(self, vals):
        # Esto seria en cualquier otro lado, en elwrite seria distinto porque los datos que quieres vienen en la variable vals
         if self.temporada == 'Verano':
             self.fecha_inicio = '21/6/2021'
             self.fecha_fin = '21/6/2021'
         elif self.temporada == 'Invierno':
        _logger.info(vals)
        # Vals es un dictionario, si hacemos un get nos devuelve el campo si se ha modificado, si no devuelve false y no entra en el if
        if vals.get('temporada'):
            if vals['temporada'] == 'Verano':
                # Esto da error, pero buscalo y arreglalo que es sencillo
                vals['fecha_inicio'] = '21/6/2021'
                vals['fecha_fin'] = '21/9/2021'
            elif vals['temporada'] == 'Invierno':
                vals['fecha_inicio'] = '21/11/2021'
                vals['fecha_fin'] = '21/2/2021'
        # Esto de super(Productos, self).write(vals) ejecua la accion de guardar, sin esto no hace nada
        return super(Productos, self).write(vals)