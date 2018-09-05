from Modules import Modules
from DimensionsNames import DimNameOracle
from DimensionsNames import DimNameLago
from Utils import Utils
from OracleJDBC import OracleJDBC


class EtlPyme:

    def __init__(self):
        print "*******Class EtlPyme *****"

    @staticmethod
    def read_names_dims_oracle(path_properties):
        config = Utils.get_config_parser(path_properties)
        bean = DimNameOracle(config.get('tablename_dest_oracle', 'car.tenencia_captacion_pyme'),
                             config.get('tablename_dest_oracle', 'car.tenencia_colocacion_pyme'),
                             config.get('tablename_dest_oracle', 'car.tenencia_seguros_pyme'),
                             config.get('tablename_dest_oracle', 'car.txs_bca_elec_pyme'),
                             config.get('tablename_dest_oracle', 'car.txs_cobros_pagos_pyme'),
                             config.get('tablename_dest_oracle', 'car.txs_servicios_pyme'))
        return bean

    @staticmethod
    def read_names_dims_lago(path_properties):
        config = Utils.get_config_parser(path_properties)
        bean = DimNameLago(config.get('tablename_orig_lago', 'abts.dim_tenencia_captacion_pyme'),
                           config.get('tablename_orig_lago', 'abts.dim_tenencia_colocacion_pyme'),
                           config.get('tablename_orig_lago', 'abts.dim_tenencia_seguros_pyme'),
                           config.get('tablename_orig_lago', 'abts.dim_txs_bca_elec_pyme'),
                           config.get('tablename_orig_lago', 'abts.dim_txs_cobros_pagos_pyme'),
                           config.get('tablename_orig_lago', 'abts.dim_txs_servicios_pyme'))
        return bean

    @staticmethod
    def get_conn_oracle(path_properties):
        config = Utils.get_config_parser(path_properties)
        bean_jdbc_conn = OracleJDBC(config.get('jdbc_conn_info', 'conn.user'),
                                    config.get('jdbc_conn_info', 'conn.driver'),
                                    config.get('jdbc_conn_info', 'conn.password'),
                                    config.get('jdbc_conn_info', 'conn.url'))
        return bean_jdbc_conn

    @staticmethod
    def build_properties(bean_jdbc_attr):
        properties = {
            "user": bean_jdbc_attr.user,
            "driver": bean_jdbc_attr.driver,
            "password": bean_jdbc_attr.password
        }
        return properties

    @staticmethod
    def write_jdbc(bean_ora, bean_lago, prop_jdbc, hive_context, url_jdbc):
        ten_capt_pyme = hive_context.sql("select * from sb_crm." + bean_lago.tenencia_captacion_pyme)
        ten_capt_pyme.count()
        ten_col_pyme = hive_context.sql("select * from sb_crm." + bean_lago.tenencia_colocacion_pyme)
        ten_seg_pyme = hive_context.sql("select * from sb_crm." + bean_lago.tenencia_seguros_pyme)
        txt_bca_elec_pyme = hive_context.sql("select * from sb_crm." + bean_lago.txs_bca_elec_pyme)
        txs_cob_pag_pyme = hive_context.sql("select * from sb_crm." + bean_lago.txs_cobros_pagos_pyme)
        txs_serv_pyme = hive_context.sql("select * from sb_crm." + bean_lago.txs_servicios_pyme)

        # ten_capt_pyme.write.mode("append").jdbc(url_jdbc, bean_ora.tenencia_captacion_pyme, prop_jdbc)
        # ten_col_pyme.write.mode("append").jdbc(url_jdbc, bean_ora.tenencia_colocacion_pyme, prop_jdbc)
        # ten_seg_pyme.write.mode("append").jdbc(url_jdbc, bean_ora.tenencia_seguros_pyme, prop_jdbc)
        # txt_bca_elec_pyme.write.mode("append").jdbc(url_jdbc, bean_ora.txs_bca_elec_pyme, prop_jdbc)
        # txs_cob_pag_pyme.write.mode("append").jdbc(url_jdbc, bean_ora.txs_cobros_pagos_pyme, prop_jdbc)
        # txs_serv_pyme.write.mode("append").jdbc(url_jdbc, bean_ora.txs_servicios_pyme, prop_jdbc)

