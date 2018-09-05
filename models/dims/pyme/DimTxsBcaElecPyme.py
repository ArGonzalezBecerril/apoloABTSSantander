class DimTxsBcaElecPyme:
    be_consultas = ""
    be_consultas_int = ""
    be_chequera_seg = ""
    be_pag_directo = ""
    be_ctos_implantadas = ""
    be_ctos_consultivas = ""
    be_ctos_transaccional = ""
    be_comisionables = ""

    def __init__(self, be_consultas, be_consultas_int, be_chequera_seg, be_pag_directo, be_ctos_implantadas,
                 be_ctos_consultivas, be_ctos_transaccional, be_comisionables):
        self.be_consultas = be_consultas
        self.be_consultas_int = be_consultas_int
        self.be_chequera_seg = be_chequera_seg
        self.be_pag_directo = be_pag_directo
        self.be_ctos_implantadas = be_ctos_implantadas
        self.be_ctos_consultivas = be_ctos_consultivas
        self.be_ctos_transaccional = be_ctos_transaccional
        self.be_comisionables = be_comisionables
