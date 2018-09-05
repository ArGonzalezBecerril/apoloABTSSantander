from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, DataFrame, DataFrameStatFunctions
from pyspark.sql import HiveContext
import ConfigParser
import os


class Spark(object):
    master = ""
    queue = ""
    executor_memory = ""
    executor_instance = ""
    app_name = ""

    def __init__(self, master, queue, executor_memory, executor_instance, app_name):
        self.master = master
        self.queue = queue
        self.executor_memory = executor_memory
        self.executor_instance = executor_instance
        self.app_name = app_name

    @staticmethod
    def get_config():
        dir_actual = os.path.dirname(os.path.abspath(__file__))
        init_file = os.path.join(dir_actual.replace("engine\\connector", "conf\\connector"), 'spark.properties')
        config = ConfigParser.RawConfigParser()
        config.read(init_file)
        return config

    @staticmethod
    def get_hive_context(context):
        sql_context = HiveContext(context)
        return sql_context

    @staticmethod
    def get_spark_context(config):
        context = SparkContext(conf=config)
        return context


