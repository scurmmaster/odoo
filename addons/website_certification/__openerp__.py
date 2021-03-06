# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-TODAY OpenERP S.A. <http://www.openerp.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Certified People',
    'category': 'Website',
    'summary': 'Display your network of certified people on your website',
    'version': '1.0',
    'author': 'OpenERP S.A.',
    'depends': ['marketing', 'website'],
    'description': """
    Display your network of certified people on your website
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/website_certification_views.xml',
        'views/website_certification_templates.xml',
    ],
    'installable': True,
}
