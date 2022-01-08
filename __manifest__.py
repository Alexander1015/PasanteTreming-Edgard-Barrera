# -*- coding: utf-8 -*-
{
    'name': "Pasante Treming - Edgard Barrera",
    
    'summary': """
        Modulo que crea los requerimientos necesarios en la prueba para pasante en Treming.
    """,
    
    'description': """
        odulo que crea los requerimientos necesarios en la prueba para pasante en Treming.
    """,
    
    'author': "Alexander Barrera",
    'website': "http://www.treming.com",
    'category': 'Administration',
    'version': '0.1',
    'depends': ['contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/treming_contacts_views.xml',
        'views/treming_sucursales_views.xml',
    ],
}
