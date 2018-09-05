import ConfigParser
import os
import subprocess
# from Pyme import Pyme
from Pyme import Pyme


class Utils:

    def __init__(self, context,logger4j, path_file):
        logger4j.info("**************Iniciando el Log del programa ******************")

    @staticmethod
    def is_path_exist(path_file):
        if os.path.exists(path_file):
            return True
        else:
            return False

    @staticmethod
    def get_path_properties(name_file):
        dir_actual = os.path.dirname(os.path.abspath(__file__))
        path_file = os.path.join(dir_actual.replace("\\utils", "\\conf\\"), name_file)
        Utils.is_path_exist(path_file)
        return path_file

    @staticmethod
    def execute_ddl_file(names_ddl_files, logger):
        logger.info("******** Hive ejecutara los siguientes ficheros hql:" + names_ddl_files)
        [logger.info('hive -f  "' + ddl + '"') for ddl in names_ddl_files.split(',')]
        # os.system('hive -f  "' + path_file + '"')

    @staticmethod
    def delete_hive_table(name_table):
        print "Eliminando la tabla :" + name_table
        os.system('hive -e " drop table sb_crm.' + name_table + '"')

    @staticmethod
    def get_logger(context):
        log4j_logger = context._jvm.org.apache.log4j
        log_4j = log4j_logger.LogManager.getLogger(__name__)
        return log_4j

    @staticmethod
    def get_path_here():
        dir_actual_ = os.path.dirname(os.path.abspath(__file__))
        path_file_modules = dir_actual_.replace("utils", "")
        return path_file_modules

    @staticmethod
    def read_path_ddl(name_file_ddl):
        config = ConfigParser.RawConfigParser()
        config.read(name_file_ddl)
        return config.get('names_ddl_files', 'names')

    @staticmethod
    def get_config_parser(path_file):
        config = ConfigParser.RawConfigParser()
        config.read(path_file)
        return config

    @staticmethod
    def read_params_dml_pyme(date_processing, path_params):
        config = Utils.get_config_parser(path_params)
        bean = Pyme(date_processing, config.get('dml_parameters', 'pyme.schema'),
                    config.get('dml_parameters', 'pyme.table_name'),
                    config.get('dml_parameters', 'pyme.path_file_dml'))
        return bean

    @staticmethod
    def is_not_empty_string(string):
        if not string:
            print "Correcto, la cadena no esta vacia"
        else:
            print "Error, la cadena esta vacia"
            exit(1)

    @staticmethod
    def execute_dml_file(bean_pyme, path_dml_file_pyme, logger):
        logger.info("******** Lanzando el siguiente comando en hive:*************")
        query_hive = "hive -v --hiveconf varCiclo=" + bean_pyme.ciclo + ' --hiveconf varSchema=' + bean_pyme.schema + ' --hiveconf varTablaFuente= ' + bean_pyme.table_name + ' -f ' + path_dml_file_pyme
        print query_hive
        # os.system(query_hive)
