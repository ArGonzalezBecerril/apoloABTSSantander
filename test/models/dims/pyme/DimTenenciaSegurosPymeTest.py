import ConfigParser
import unittest
import os
from models.dims.pyme.DimTenenciaSegurosPyme import DimTenenciaSegurosPyme


class DimTenenciaSegurosPymeTest(unittest.TestCase):
    def test_is_correct_values(self):
        config = get_config()
        bean = add_values_object(config)
        self.assertEquals(bean.seg_protegida, "seg_protegida")
        self.assertEquals(bean.seg_medadvance, "seg_medadvance")
        self.assertEquals(bean.seg_cred_related, "seg_cred_related")
        self.assertEquals(bean.seg_resto, "seg_resto")


if __name__ == '__main__':
    unittest.main()


def get_config():
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    init_file = os.path.join(dir_actual.replace("test\\models\\dims\\pyme", "conf\\"), 'pyme.properties')
    config = ConfigParser.RawConfigParser()
    config.read(init_file)
    return config

def add_values_object(config):
    bean = DimTenenciaSegurosPyme
    bean.seg_protegida = config.get('dim_tenencia_seguros_pyme', 'dim.seg_protegida')
    bean.seg_medadvance = config.get('dim_tenencia_seguros_pyme', 'dim.seg_medadvance')
    bean.seg_cred_related = config.get('dim_tenencia_seguros_pyme', 'dim.seg_cred_related')
    bean.seg_resto = config.get('dim_tenencia_seguros_pyme', 'dim.seg_resto')
    return bean
