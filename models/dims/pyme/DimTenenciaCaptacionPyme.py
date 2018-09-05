class DimTenenciaCaptacionPyme(object):
    epymes = ""
    tradicional = ""
    spymes = ""
    resto_vista = ""
    inversion_vista = ""
    plazo = ""
    fondos = ""
    plazo_op = ""
    fondos_op = ""
    mdd = ""

    def __init__(self, epymes, tradicional, spymes, resto_vista, inversion_vista, plazo, fondos, plazo_op, fondos_op, mdd):

        self.epymes = epymes
        self.tradicional = tradicional
        self.spymes = spymes
        self.resto_vista = resto_vista
        self.inversion_vista = inversion_vista
        self.plazo = plazo
        self.fondos = fondos
        self.plazo_op = plazo_op
        self.fondos_op = fondos_op
        self.mdd = mdd

    def __str__(self):
        print self.epymes, self.tradicional, self.spymes, self.resto_vista, self.inversion_vista, self.plazo, self.fondos, self.plazo_op, self.fondos_op, self.mdd
