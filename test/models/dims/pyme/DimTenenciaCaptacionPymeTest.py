import ConfigParser
import unittest
import os
from models.dims.pyme.DimTenenciaCaptacionPyme import DimTenenciaCaptacionPyme


class DimTenenciaCaptacionPymeTest(unittest.TestCase):

    def test_is_correct_config(self):
        config = get_config()
        self.assertNotEqual(config, None)

    def test_is_correct_values(self):
        config = get_config()
        bean = add_values_object(config)
        self.assertEquals(bean.epymes,"epymes")
        self.assertEquals(bean.tradicional, "tradicional")
        self.assertEquals(bean.spymes, "spymes")
        self.assertEquals(bean.resto_vista, "resto_vista")
        self.assertEquals(bean.inversion_vista, "inversion_vista")
        self.assertEquals(bean.plazo, "plazo")
        self.assertEquals(bean.fondos, "fondos")
        self.assertEquals(bean.plazo_op, "plazo_op")
        self.assertEquals(bean.fondos_op, "fondos_op")
        self.assertEquals(bean.mdd, "mdd")

    if __name__ == "__main__":
        test_is_correct_values()


def get_config():
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    init_file = os.path.join(dir_actual.replace("test\\models\\dims\\pyme", "conf\\"), 'pyme.properties')
    config = ConfigParser.RawConfigParser()
    config.read(init_file)
    return config


def add_values_object(config):
    bean = DimTenenciaCaptacionPyme
    bean.epymes = config.get('dim_tenencia_captacion_pyme', 'dim.epymes')
    bean.tradicional = config.get('dim_tenencia_captacion_pyme', 'dim.tradicional')
    bean.spymes = config.get('dim_tenencia_captacion_pyme', 'dim.spymes')
    bean.resto_vista = config.get('dim_tenencia_captacion_pyme', 'dim.resto_vista')
    bean.inversion_vista = config.get('dim_tenencia_captacion_pyme', 'dim.inversion_vista')
    bean.plazo = config.get('dim_tenencia_captacion_pyme', 'dim.plazo')
    bean.fondos = config.get('dim_tenencia_captacion_pyme', 'dim.fondos')
    bean.plazo_op = config.get('dim_tenencia_captacion_pyme', 'dim.plazo_op')
    bean.fondos_op = config.get('dim_tenencia_captacion_pyme', 'dim.fondos_op')
    bean.mdd = config.get('dim_tenencia_captacion_pyme', 'dim.mdd')
    return bean






