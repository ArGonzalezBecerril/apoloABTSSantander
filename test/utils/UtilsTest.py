import unittest
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, DataFrame, DataFrameStatFunctions
from pyspark.sql import HiveContext
import os


class CompanionUtils:

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
        context_.addPyFile(path_file_modules + "models/dims/pyme/Pyme.py")

    @staticmethod
    def get_path_here():
        dir_actual_ = os.path.dirname(os.path.abspath(__file__))
        path_file_modules = dir_actual_.replace("test/utils", "")
        return path_file_modules

    @staticmethod
    def get_spark_context(config):
        context_ = SparkContext(conf=config)
        return context_

    @staticmethod
    def get_hive_context(context_spark):
        sql_context = HiveContext(context_spark)
        return sql_context


class UtilsTest(unittest.TestCase):
    conf = CompanionUtils.get_spark_conf()
    path_here = CompanionUtils.get_path_here()
    context = CompanionUtils.get_spark_context(conf)
    CompanionUtils.load_modules_class(context, path_here)

    def test_names_ddl_files(self):
        from Utils import Utils
        from Log4j import Log4j

        log = Log4j.get_logger(self.context)
        names_ddl_files = Utils.read_path_ddl(self.path_here + 'conf/path_files_hql/path_files.properties')
        log.info("======================================================================")
        log.info("Validando que exitan la intancia de SparkConf")
        log.info("Assert Sparkconf = " + " !=  None")
        self.assertNotEquals(self.conf, None)
        log.info("======================================================================")
        log.info("Validando que existan nombres de ficheros ddl en el path /path_files_hql ")
        log.info("Assert 'abts_ddl_pyme.hql,abts_ddl_pyme2.hql' with " + names_ddl_files)
        self.assertEquals("abts_ddl_pyme.hql,abts_ddl_pyme2.hql", names_ddl_files)
        log.info("======================================================================")

    def test_params_dml_pyme(self):
        from Utils import Utils
        from Log4j import Log4j
        from Pyme import Pyme

        date_processed = "201806"
        log = Log4j.get_logger(self.context)
        path_file_prop_pyme = self.path_here + 'conf/pyme.properties'
        bean_pyme = Utils.read_params_dml_pyme(date_processed, path_file_prop_pyme)

        log.info("Validando parametros dml pyme")

        self.assertEquals("201806", bean_pyme.ciclo)
        self.assertEquals("af_macrobase_hist", bean_pyme.schema)
        self.assertEquals("v_ind_gestion_pyme_dl", bean_pyme.table_name)
        self.assertEquals("dml_abts_pyme.hql", bean_pyme.path_file_dml)

    def test_utils_path_exist(self):
        from Utils import Utils
        from Log4j import Log4j

        log = Log4j.get_logger(self.context)

        log.info("======================================================================")
        log.info("Validando si el fichero Utils.py existe")
        log.info("Assert :'" + self.path_here + "utils/Utils.py")
        self.assertEquals(Utils.is_path_exist(self.path_here + "utils/Utils.py"), True)
        log.info("======================================================================")


if __name__ == '__main__':
    unittest.main()


