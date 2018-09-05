import ConfigParser
import unittest
import os
from models.dims.pyme.DimTenenciaColocacionPyme import DimTenenciaColocacionPyme


class DimTenenciaColocacionPymeTest(unittest.TestCase):
    def test_starting_out(self):
        config = get_config()
        bean = add_values_object(config)
        self.assertEquals(bean.hipotecario, "hipotecario")
        self.assertEquals(bean.auto, "auto")
        self.assertEquals(bean.cred_simple, "cred_simple")
        self.assertEquals(bean.cred_comercial, "cred_comercial")
        self.assertEquals(bean.agil, "agil")
        self.assertEquals(bean.comex, "comex")
        self.assertEquals(bean.agro, "agro")
        self.assertEquals(bean.linea, "linea")
        self.assertEquals(bean.resto_col, "resto_col")
        self.assertEquals(bean.tdc, "tdc")
        self.assertEquals(bean.tde, "tde")
        self.assertEquals(bean.id_cc_exp_vig, "id_cc_exp_vig")
        self.assertEquals(bean.id_cc_exp_vig, "id_cc_exp_vig")

    if __name__ == '__main__':
        test_starting_out


def get_config():
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    init_file = os.path.join(dir_actual.replace("test\\models\\dims\\pyme", "conf\\"), 'pyme.properties')
    config = ConfigParser.RawConfigParser()
    config.read(init_file)
    return config


def add_values_object(config):
    bean = DimTenenciaColocacionPyme
    bean.hipotecario = bean.hipotecario = config.get('dim_tenencia_colocacion_pyme', 'dim.hipotecario')
    bean.auto = bean.auto = config.get('dim_tenencia_colocacion_pyme', 'dim.auto')
    bean.cred_simple = bean.cred_simple = config.get('dim_tenencia_colocacion_pyme', 'dim.cred_simple')
    bean.cred_comercial = bean.cred_comercial = config.get('dim_tenencia_colocacion_pyme', 'dim.cred_comercial')
    bean.agil = bean.agil = config.get('dim_tenencia_colocacion_pyme', 'dim.agil')
    bean.comex = bean.comex = config.get('dim_tenencia_colocacion_pyme', 'dim.comex')
    bean.agro = bean.agro = config.get('dim_tenencia_colocacion_pyme', 'dim.agro')
    bean.linea = bean.linea = config.get('dim_tenencia_colocacion_pyme', 'dim.linea')
    bean.resto_col = bean.resto_col = config.get('dim_tenencia_colocacion_pyme', 'dim.resto_col')
    bean.tdc = bean.tdc = config.get('dim_tenencia_colocacion_pyme', 'dim.tdc')
    bean.tde = bean.tde = config.get('dim_tenencia_colocacion_pyme', 'dim.tde')
    bean.id_cc_imp_vig = bean.id_cc_imp_vig = config.get('dim_tenencia_colocacion_pyme', 'dim.id_cc_imp_vig')
    bean.id_cc_exp_vig = bean.id_cc_exp_vig = config.get('dim_tenencia_colocacion_pyme', 'dim.id_cc_exp_vig')
    return bean
