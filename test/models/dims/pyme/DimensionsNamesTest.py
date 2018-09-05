import unittest
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, DataFrame, DataFrameStatFunctions
from pyspark.sql import HiveContext
import os
# from models.dims.pyme.DimensionsNames import DimNameOracle


class CompanionDimensionsNames:
    def __init__(self):
        print 'Companion Object DimensionsName'

    @staticmethod
    def get_spark_conf():
        config = SparkConf().set("spark.yarn.queue", "crm_resource_pool").set("spark.executor.memory", "11G").set(
            "spark.executor.instances", "26").setAppName("ABTSSantanderTestUnit")
        return config

    @staticmethod
    def load_modules_class(context_, path_file_modules):
        context_.addPyFile(path_file_modules + "utils/Modules.py")
        context_.addPyFile(path_file_modules + "engine/connector/Spark.py")
        context_.addPyFile(path_file_modules + "utils/Utils.py")
        context_.addPyFile(path_file_modules + "utils/Log4j.py")
        context_.addPyFile(path_file_modules + "models/connections/OracleJDBC.py")
        context_.addPyFile(path_file_modules + "models/dims/pyme/DimensionsNames.py")
        context_.addPyFile(path_file_modules + "models/dims/pyme/Pyme.py")

    @staticmethod
    def get_path_here():
        dir_actual_ = os.path.dirname(os.path.abspath(__file__))
        path_file_modules = dir_actual_.replace("test/models/dims/pyme", "")
        return path_file_modules

    @staticmethod
    def get_spark_context(config):
        context_ = SparkContext(conf=config)
        return context_

    @staticmethod
    def get_hive_context(context_spark):
        sql_context = HiveContext(context_spark)
        return sql_context


class DimensionsNames(unittest.TestCase):
    conf = CompanionDimensionsNames.get_spark_conf()
    path_here = CompanionDimensionsNames.get_path_here()
    context = CompanionDimensionsNames.get_spark_context(conf)
    CompanionDimensionsNames.load_modules_class(context, path_here)

    def test_object_null(self):
        from Utils import Utils
        from Log4j import Log4j
        from DimensionsNames import DimNameOracle
        log = Log4j.get_logger(self.context)

        log.info("Validando que la instancia de DimNameOracle este vacio")
        try:
            bean_dim_ora_null = DimNameOracle("", "", "", "", "", "")
        except Exception:
            pass

    def test_object_not_null(self):
        from Utils import Utils
        from Log4j import Log4j
        from DimensionsNames import DimNameOracle
        log = Log4j.get_logger(self.context)

        bean_dim_ora_notnull = DimNameOracle("dim1", "dim2", "dim3", "dim4", "dim5", "dim6")

        self.assertEquals("dim1", bean_dim_ora_notnull.tenencia_captacion_pyme)
        self.assertEquals("dim2", bean_dim_ora_notnull.tenencia_colocacion_pyme)
        self.assertEquals("dim3", bean_dim_ora_notnull.tenencia_seguros_pyme)
        self.assertEquals("dim4", bean_dim_ora_notnull.txs_bca_elec_pyme)
        self.assertEquals("dim5", bean_dim_ora_notnull.txs_cobros_pagos_pyme)
        self.assertEquals("dim6", bean_dim_ora_notnull.txs_servicios_pyme)
        log.info("El bean dim_name_oracle se construyo correctamente")


if __name__ == '__main__':
    unittest.main()
