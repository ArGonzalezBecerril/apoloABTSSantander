class ExclusionesCanales:
    flg_nm_atm = ""
    flg_nm_buro = ""
    flg_nm_cd = ""
    flg_nm_ce = ""
    flg_nm_redes = ""
    flg_nm_sms = ""
    flg_nm_snet = ""
    flg_nm_suc = ""
    flg_nm_tmk = ""
    flg_no_molestar_email = ""
    flg_no_molestar_tels = ""
    num_anio_mes = ""

    def __init__(self, flg_nm_atm, flg_nm_buro, flg_nm_cd, flg_nm_ce, flg_nm_redes, flg_nm_sms, flg_nm_snet, flg_nm_suc, flg_nm_tmk, flg_no_molestar_email, flg_no_molestar_tels, num_anio_mes):
        self.flg_nm_atm = flg_nm_atm
        self.flg_nm_buro = flg_nm_buro
        self.flg_nm_cd = flg_nm_cd
        self.flg_nm_ce = flg_nm_ce
        self.flg_nm_redes = flg_nm_redes
        self.flg_nm_sms = flg_nm_sms
        self.flg_nm_snet = flg_nm_snet
        self.flg_nm_suc = flg_nm_suc
        self.flg_nm_tmk = flg_nm_tmk
        self.flg_no_molestar_email = flg_no_molestar_email
        self.flg_no_molestar_tels = flg_no_molestar_tels
        self.num_anio_mes = num_anio_mes

    def main(self):
        print("Object car_exclusiones_canales")
