import unittest
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, DataFrame, DataFrameStatFunctions
from pyspark.sql import HiveContext
import os


class CompanionOracleJDBC:

    def __init__(self):
        print "*******Class companion of Utils*****"

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
        context_.addPyFile(path_file_modules + "models/dims/pyme/Pyme.py")

    @staticmethod
    def get_path_here():
        dir_actual_ = os.path.dirname(os.path.abspath(__file__))
        path_file_modules = dir_actual_.replace("test/engine/connector", "")
        return path_file_modules

    @staticmethod
    def get_spark_context(config):
        context_ = SparkContext(conf=config)
        return context_

    @staticmethod
    def get_hive_context(context_spark):
        sql_context = HiveContext(context_spark)
        return sql_context


class OracleJDBCTest(unittest.TestCase):
    conf = CompanionOracleJDBC.get_spark_conf()
    path_here = CompanionOracleJDBC.get_path_here()
    context = CompanionOracleJDBC.get_spark_context(conf)
    CompanionOracleJDBC.load_modules_class(context, path_here)

    def test_is_object_empty(self):
        from Utils import Utils
        from Log4j import Log4j
        from OracleJDBC import OracleJDBC

        log = Log4j.get_logger(self.context)

        log.info("Validando que la instancia de OracleJDBC este vacio")
        try:
            bean_ora_jdbc = OracleJDBC("", "", "", "")
        except Exception:
            pass

    def test_is_object_not_empty(self):
        from Utils import Utils
        from Log4j import Log4j
        from OracleJDBC import OracleJDBC

        log = Log4j.get_logger(self.context)
        log.info("Validando que la instancia de OracleJDBC no este vacio")
        bean_ora_jdbc = OracleJDBC("user", "drive", "password", "url_jdbc")

        self.assertNotEqual(bean_ora_jdbc, None)


if __name__ == '__main__':
    unittest.main()
