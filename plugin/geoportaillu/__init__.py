def classFactory(iface):
    from .geoportail import GeoportailLU
    return GeoportailLU(iface)