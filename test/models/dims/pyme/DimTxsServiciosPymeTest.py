import ConfigParser
import unittest
import os
from models.dims.pyme.DimTxsServiciosPyme import DimTxsServiciosPyme


class DimTxsServiciosPymeTest(unittest.TestCase):
    def test_is_correct_values(self):
        config = get_config()
        bean = add_values_object(config)
        self.assertEquals(bean.id_cambios, "id_cambios")
        self.assertEquals(bean.id_cambios_fxonline, "id_cambios_fxonline")
        self.assertEquals(bean.id_derivados_tasa, "id_derivados_tasa")
        self.assertEquals(bean.id_nomina, "id_nomina")
        self.assertEquals(bean.id_tpv, "id_tpv")
        self.assertEquals(bean.id_domic_pag, "id_domic_pag")
        self.assertEquals(bean.id_domic_cob, "id_domic_cob")
        self.assertEquals(bean.id_emi_mb, "id_emi_mb")
        self.assertEquals(bean.id_emi_ob, "id_emi_ob")
        self.assertEquals(bean.id_rec_mb, "id_rec_mb")
        self.assertEquals(bean.id_rec_ob, "id_rec_ob")
        self.assertEquals(bean.id_custodia, "id_custodia")
        self.assertEquals(bean.id_trans_be, "id_trans_be")
        self.assertEquals(bean.id_trans_digitales, "id_trans_digitales")
        self.assertEquals(bean.id_internacionales, "id_internacionales")
        self.assertEquals(bean.id_internacionales_rec, "id_internacionales_rec")
        self.assertEquals(bean.id_remesas, "id_remesas")


if __name__ == '__main__':
    unittest.main()

def get_config():
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    init_file = os.path.join(dir_actual.replace("test\\models\\dims\\pyme", "conf\\"), 'pyme.properties')
    config = ConfigParser.RawConfigParser()
    config.read(init_file)
    return config


def add_values_object(config):
    bean = DimTxsServiciosPyme
    bean.id_cambios = config.get('dim_txs_servicios_pyme', 'dim.id_cambios')
    bean.id_cambios_fxonline = config.get('dim_txs_servicios_pyme', 'dim.id_cambios_fxonline')
    bean.id_derivados_tasa = config.get('dim_txs_servicios_pyme', 'dim.id_derivados_tasa')
    bean.id_nomina = config.get('dim_txs_servicios_pyme', 'dim.id_nomina')
    bean.id_tpv = config.get('dim_txs_servicios_pyme', 'dim.id_tpv')
    bean.id_domic_pag = config.get('dim_txs_servicios_pyme', 'dim.id_domic_pag')
    bean.id_domic_cob = config.get('dim_txs_servicios_pyme', 'dim.id_domic_cob')
    bean.id_emi_mb = config.get('dim_txs_servicios_pyme', 'dim.id_emi_mb')
    bean.id_emi_ob = config.get('dim_txs_servicios_pyme', 'dim.id_emi_ob')
    bean.id_rec_mb = config.get('dim_txs_servicios_pyme', 'dim.id_rec_mb')
    bean.id_rec_ob = config.get('dim_txs_servicios_pyme', 'dim.id_rec_ob')
    bean.id_custodia = config.get('dim_txs_servicios_pyme', 'dim.id_custodia')
    bean.id_trans_be = config.get('dim_txs_servicios_pyme', 'dim.id_trans_be')
    bean.id_trans_digitales = config.get('dim_txs_servicios_pyme', 'dim.id_trans_digitales')
    bean.id_internacionales = config.get('dim_txs_servicios_pyme', 'dim.id_internacionales')
    bean.id_internacionales_rec = config.get('dim_txs_servicios_pyme', 'dim.id_internacionales_rec')
    bean.id_remesas = config.get('dim_txs_servicios_pyme', 'dim.id_remesas')
    return bean


