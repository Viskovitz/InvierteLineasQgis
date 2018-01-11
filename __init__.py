# -*- coding: utf-8 -*-
"""
/***************************************************************************
 InvierteLineas
                                 A QGIS plugin
 Invierte el sentido de digitalización las líneas seleccionadas de una capa en edición
                             -------------------
        begin                : 2018-01-11
        copyright            : (C) 2018 by Raúl Casado Barbero
        email                : rcbarbero@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load InvierteLineas class from file InvierteLineas.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .invierte_lineas import InvierteLineas
    return InvierteLineas(iface)
