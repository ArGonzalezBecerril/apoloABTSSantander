from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, DataFrame, DataFrameStatFunctions
from pyspark.sql import HiveContext
import os


class SparkConnector:

    def __init__(self):
        print "*******Clase el cual es el encargado de obtener un contexto de spark*****"

    @staticmethod
    def get_spark_conf():
        config = SparkConf().set("spark.yarn.queue", "crm_resource_pool").set("spark.executor.memory", "11G").set(
            "spark.executor.instances", "26").setAppName("ABTSSantanderTestUnit")
        return config

    @staticmethod
    def load_init_modules(context_, path_file_modules):
        context_.addPyFile(path_file_modules + "utils/Modules.py")
        context_.addPyFile(path_file_modules + "engine/connector/Spark.py")

    @staticmethod
    def get_path_here():
        dir_actual_ = os.path.dirname(os.path.abspath(__file__))
        path_file_modules = dir_actual_.replace("main", "")
        return path_file_modules

    @staticmethod
    def get_spark_context(config):
        context_ = SparkContext(conf=config)
        return context_

    @staticmethod
    def get_hive_context(context_spark):
        sql_context = HiveContext(context_spark)
        return sql_context


# *********************** Header ************************************************ #
conf = SparkConnector.get_spark_conf()
context = SparkConnector.get_spark_context(conf)
path_principal = SparkConnector.get_path_here()
SparkConnector.load_init_modules(context, path_principal)

from Modules import Modules

hive_context = SparkConnector.get_hive_context(context)
Modules.load_core_modules(context, path_principal)

from Log4j import Log4j
from Utils import Utils
from Pyme import Pyme
from EtlPyme import EtlPyme

# **************************** Main ********************************************* #
log = Log4j.get_logger(context)
date_processed = "201806"

path_ddl_file_pyme = Utils.read_path_ddl(path_principal + 'conf/path_files_hql/path_files.properties')
Utils.execute_ddl_file(path_ddl_file_pyme, log)

path_file_prop_pyme = path_principal + 'conf/pyme.properties'
path_dml_file_pyme = path_principal + 'conf/dml_files/dml_abts_pyme.hql'
bean_pyme = Utils.read_params_dml_pyme(date_processed, path_file_prop_pyme)
Utils.execute_dml_file(bean_pyme, path_dml_file_pyme, log)

bean_ora_name_dims = EtlPyme.read_names_dims_oracle(path_file_prop_pyme)
bean_lago_name_dims = EtlPyme.read_names_dims_lago(path_file_prop_pyme)

bean_jdbc_conn = EtlPyme.get_conn_oracle(path_principal + 'conf/connector/oracle_stage.properties')
prop_jdbc_conn = EtlPyme.build_properties(bean_jdbc_conn)

EtlPyme.write_jdbc(bean_ora_name_dims, bean_lago_name_dims, prop_jdbc_conn, hive_context,
                   bean_jdbc_conn.url)


log.info("\n**************Realizando un test de sqlContext******************\n")
tabla = hive_context.sql("select * from sb_crm.abts_dim_tenencia_captacion_pyme")
tabla.printSchema()

