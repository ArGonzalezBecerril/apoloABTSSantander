
class Log4j:

    def __init__(self, context,logger4j, path_file):
        logger4j.info("**************Iniciando el Log del programa ******************")

    @staticmethod
    def get_logger(context):
        get_logger = context._jvm.org.apache.log4j
        log4j = get_logger.LogManager.getLogger(__name__)
        return log4j
