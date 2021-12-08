# -*- coding: utf-8 -*-

{
    'name': "La Turisana",
    
    'summary': """
        Implementa desarrollo personalizado para marcar actualizacion necesaria en movimientos de stock'   
        """,

    'description': """
        Módulo que añade marcar actualizacion necesaria en movimientos de stock
    """,

    'author': "Jonathan",
    'website': "https://www.laturi.es",

    'category': 'Stock Move',
    'version': '12.0.1.1',

    'depends': ['base', 'sale', 'stock'],          

    'data': [
        'security/ir.model.access.csv',
        'views/productos_view.xml',
    ],

}
