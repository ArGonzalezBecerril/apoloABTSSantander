class DimTxsServiciosPyme:
    id_cambios = ""
    id_cambios_fxonline = ""
    id_derivados_tasa = ""
    id_nomina = ""
    id_tpv = ""
    id_domic_pag = ""
    id_domic_cob = ""
    id_emi_mb = ""
    id_emi_ob = ""
    id_rec_mb = ""
    id_rec_ob = ""
    id_custodia = ""
    id_trans_be = ""
    id_trans_digitales = ""
    id_internacionales = ""
    id_internacionales_rec = ""
    id_remesas = ""

    def __init__(self, id_cambios, id_cambios_fxonline, id_derivados_tasa, id_nomina, id_tpv, id_domic_pag,
                 id_domic_cob, id_emi_mb, id_emi_ob, id_rec_mb, id_rec_ob, id_custodia, id_trans_be, id_trans_digitales,
                 id_internacionales, id_internacionales_rec, id_remesas):
        self.id_cambios = id_cambios
        self.id_cambios_fxonline = id_cambios_fxonline
        self.id_derivados_tasa = id_derivados_tasa
        self.id_nomina = id_nomina
        self.id_tpv = id_tpv
        self.id_domic_pag = id_domic_pag
        self.id_domic_cob = id_domic_cob
        self.id_emi_mb = id_emi_mb
        self.id_emi_ob = id_emi_ob
        self.id_rec_mb = id_rec_mb
        self.id_rec_ob = id_rec_ob
        self.id_custodia = id_custodia
        self.id_trans_be = id_trans_be
        self.id_trans_digitales = id_trans_digitales
        self.id_internacionales = id_internacionales
        self.id_internacionales_rec = id_internacionales_rec
        self.id_remesas = id_remesas
