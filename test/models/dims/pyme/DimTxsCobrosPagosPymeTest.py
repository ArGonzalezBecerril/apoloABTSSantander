import ConfigParser
import unittest
import os
from models.dims.pyme.DimTxsCobrosPagosPyme import DimTxsCobrosPagosPyme


class DimTxsCobrosPagosPymeTest(unittest.TestCase):
    def test_is_correct_values(self):
        config = get_config()
        bean = add_values_object(config)
        self.assertEquals(bean.id_tdd, "id_tdd")
        self.assertEquals(bean.id_pagprov_mb, "id_pagprov_mb")
        self.assertEquals(bean.id_pagprov_ob, "id_pagprov_ob")
        self.assertEquals(bean.id_pagprov, "id_pagprov")
        self.assertEquals(bean.id_impuestos, "id_impuestos")
        self.assertEquals(bean.id_provisionales, "id_provisionales")
        self.assertEquals(bean.id_pagocheques, "id_pagocheques")
        self.assertEquals(bean.id_cobrocheques, "id_cobrocheques")
        self.assertEquals(bean.id_recaud_fisica, "id_recaud_fisica")
        self.assertEquals(bean.id_recaud_elec, "id_recaud_elec")
        self.assertEquals(bean.id_retiros, "id_retiros")
        self.assertEquals(bean.id_giros, "id_giros")
        self.assertEquals(bean.id_depref, "id_depref")
        self.assertEquals(bean.id_online_cheque, "id_online_cheque")
        self.assertEquals(bean.id_pago_direc, "id_pago_direc")
        self.assertEquals(bean.id_pago_ocurre, "id_pago_ocurre")
        self.assertEquals(bean.id_confirming, "id_confirming")


if __name__ == '__main__':
    unittest.main()


def get_config():
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    init_file = os.path.join(dir_actual.replace("test\\models\\dims\\pyme", "conf\\"), 'pyme.properties')
    config = ConfigParser.RawConfigParser()
    config.read(init_file)
    return config


def add_values_object(config):
    bean = DimTxsCobrosPagosPyme
    bean.id_tdd = config.get('dim_txs_cobros_pagos_pyme', 'dim.id_tdd')
    bean.id_pagprov_mb = config.get('dim_txs_cobros_pagos_pyme', 'dim.id_pagprov_mb')
    bean.id_pagprov_ob = config.get('dim_txs_cobros_pagos_pyme', 'dim.id_pagprov_ob')
    bean.id_pagprov = config.get('dim_txs_cobros_pagos_pyme', 'dim.id_pagprov')
    bean.id_impuestos = config.get('dim_txs_cobros_pagos_pyme', 'dim.id_impuestos')
    bean.id_provisionales = config.get('dim_txs_cobros_pagos_pyme', 'dim.id_provisionales')
    bean.id_pagocheques = config.get('dim_txs_cobros_pagos_pyme', 'dim.id_pagocheques')
    bean.id_cobrocheques = config.get('dim_txs_cobros_pagos_pyme', 'dim.id_cobrocheques')
    bean.id_recaud_fisica = config.get('dim_txs_cobros_pagos_pyme', 'dim.id_recaud_fisica')
    bean.id_recaud_elec = config.get('dim_txs_cobros_pagos_pyme', 'dim.id_recaud_elec')
    bean.id_retiros = config.get('dim_txs_cobros_pagos_pyme', 'dim.id_retiros')
    bean.id_giros = config.get('dim_txs_cobros_pagos_pyme', 'dim.id_giros')
    bean.id_depref = config.get('dim_txs_cobros_pagos_pyme', 'dim.id_depref')
    bean.id_online_cheque = config.get('dim_txs_cobros_pagos_pyme', 'dim.id_online_cheque')
    bean.id_pago_direc = config.get('dim_txs_cobros_pagos_pyme', 'dim.id_pago_direc')
    bean.id_pago_ocurre = config.get('dim_txs_cobros_pagos_pyme', 'dim.id_pago_ocurre')
    bean.id_confirming = config.get('dim_txs_cobros_pagos_pyme', 'dim.id_confirming')
    return bean
