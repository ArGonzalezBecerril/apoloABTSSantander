import ConfigParser
import unittest
import os
from models.dims.pyme.DimTxsBcaElecPyme import DimTxsBcaElecPyme


class DimTxsBcaElecPymeTest(unittest.TestCase):
    def test_is_correct_values(self):
        config = get_config()
        bean = add_values_object(config)
        self.assertEquals(bean.be_consultas, "be_consultas")
        self.assertEquals(bean.be_consultas_int, "be_consultas_int")
        self.assertEquals(bean.be_chequera_seg, "be_chequera_seg")
        self.assertEquals(bean.be_pag_directo, "be_pag_directo")
        self.assertEquals(bean.be_ctos_implantadas, "be_ctos_implantadas")
        self.assertEquals(bean.be_ctos_consultivas, "be_ctos_consultivas")
        self.assertEquals(bean.be_ctos_transaccional, "be_ctos_transaccional")
        self.assertEquals(bean.be_comisionables, "be_comisionables")


if __name__ == '__main__':
    unittest.main()


def get_config():
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    init_file = os.path.join(dir_actual.replace("test\\models\\dims\\pyme", "conf\\"), 'pyme.properties')
    config = ConfigParser.RawConfigParser()
    config.read(init_file)
    return config


def add_values_object(config):
    bean = DimTxsBcaElecPyme
    bean.be_consultas = config.get('dim_txs_bca_elec_pyme', 'dim.be_consultas')
    bean.be_consultas_int = config.get('dim_txs_bca_elec_pyme', 'dim.be_consultas_int')
    bean.be_chequera_seg = config.get('dim_txs_bca_elec_pyme', 'dim.be_chequera_seg')
    bean.be_pag_directo = config.get('dim_txs_bca_elec_pyme', 'dim.be_pag_directo')
    bean.be_ctos_implantadas = config.get('dim_txs_bca_elec_pyme', 'dim.be_ctos_implantadas')
    bean.be_ctos_consultivas = config.get('dim_txs_bca_elec_pyme', 'dim.be_ctos_consultivas')
    bean.be_ctos_transaccional = config.get('dim_txs_bca_elec_pyme', 'dim.be_ctos_transaccional')
    bean.be_comisionables = config.get('dim_txs_bca_elec_pyme', 'dim.be_comisionables')
    return bean

