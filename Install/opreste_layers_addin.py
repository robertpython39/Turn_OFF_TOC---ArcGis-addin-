# -------------------------------------------------------------------------------
# Name:        Layers_OFF_TOC_addin
# Purpose:     intern
#
# Author:      rnicolescu
#
# Created:     05/07/2022
# Copyright:   (c) rnicolescu 2022
# Licence:     <your license here>
# -------------------------------------------------------------------------------


import arcpy
import pythonaddins

class LayersOffTOC(object):
    """Implementation for opreste_layers_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        mxd = arcpy.mapping.MapDocument("current")
        data_frame = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
        layers = arcpy.mapping.ListLayers(mxd)

        for layer in layers:
            if layer.isGroupLayer:
                layer.visible = False
            if layer.longName == "Group Name\SubLayer Name":
                layer.visible = False

        arcpy.RefreshTOC()
        arcpy.RefreshActiveView()