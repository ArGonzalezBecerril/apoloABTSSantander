import os


class Modules:

    def __init__(self, context,logger4j, path_file):
        logger4j.info("****************Cargando los modulos de proyecto ApoloAbtsSantander")

    @staticmethod
    def load_core_modules(context, path_file):
        get_logger = context._jvm.org.apache.log4j
        log4j = get_logger.LogManager.getLogger(__name__)
        log4j.info("\n*********************************************************************\n")
        log4j.info("\n*****************Agregando los modulos a spark***********************\n")
        log4j.info("\n*********************************************************************\n")
        context.addPyFile(path_file + "conf/connector/spark.properties")
        context.addPyFile(path_file + "conf/ddl_files/ddl_abts_pyme.hql")
        context.addPyFile(path_file + "conf/path_files_hql/path_files.properties")
        context.addPyFile(path_file + "conf/pyme.properties")
        context.addPyFile(path_file + "engine/core/EtlPyme.py")
        context.addPyFile(path_file + "main/principal.py")
        context.addPyFile(path_file + "models/dims/pyme/DimensionsNames.py")
        context.addPyFile(path_file + "models/dims/pyme/DimTenenciaCaptacionPyme.py")
        context.addPyFile(path_file + "models/dims/pyme/DimTenenciaColocacionPyme.py")
        context.addPyFile(path_file + "models/dims/pyme/DimTenenciaSegurosPyme.py")
        context.addPyFile(path_file + "models/dims/pyme/DimTxsBcaElecPyme.py")
        context.addPyFile(path_file + "models/dims/pyme/DimTxsCobrosPagosPyme.py")
        context.addPyFile(path_file + "models/dims/pyme/DimTxsServiciosPyme.py")
        context.addPyFile(path_file + "models/dims/pyme/Pyme.py")
        context.addPyFile(path_file + "models/connections/OracleJDBC.py")
        context.addPyFile(path_file + "utils/Utils.py")
        context.addPyFile(path_file + "utils/Log4j.py")


