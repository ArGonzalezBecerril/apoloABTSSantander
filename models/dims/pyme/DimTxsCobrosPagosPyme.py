class DimTxsCobrosPagosPyme:
    id_tdd = ""
    id_pagprov_mb = ""
    id_pagprov_ob = ""
    id_pagprov = ""
    id_impuestos = ""
    id_provisionales = ""
    id_pagocheques = ""
    id_cobrocheques = ""
    id_recaud_fisica = ""
    id_recaud_elec = ""
    id_retiros = ""
    id_giros = ""
    id_depref = ""
    id_online_cheque = ""
    id_pago_direc = ""
    id_pago_ocurre = ""
    id_confirming = ""

    def __init__(self, id_tdd, id_pagprov_mb, id_pagprov_ob, id_pagprov, id_impuestos, id_provisionales, id_pagocheques,
                 id_cobrocheques, id_recaud_fisica, id_recaud_elec, id_retiros, id_giros, id_depref, id_online_cheque,
                 id_pago_direc, id_pago_ocurre, id_confirming):
        self.id_tdd = id_tdd
        self.id_pagprov_mb = id_pagprov_mb
        self.id_pagprov_ob = id_pagprov_ob
        self.id_pagprov = id_pagprov
        self.id_impuestos = id_impuestos
        self.id_provisionales = id_provisionales
        self.id_pagocheques = id_pagocheques
        self.id_cobrocheques = id_cobrocheques
        self.id_recaud_fisica = id_recaud_fisica
        self.id_recaud_elec = id_recaud_elec
        self.id_retiros = id_retiros
        self.id_giros = id_giros
        self.id_depref = id_depref
        self.id_online_cheque = id_online_cheque
        self.id_pago_direc = id_pago_direc
        self.id_pago_ocurre = id_pago_ocurre
        self.id_confirming = id_confirming
