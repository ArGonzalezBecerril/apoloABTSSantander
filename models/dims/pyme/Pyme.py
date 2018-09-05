import operator


class Pyme(object):

    def __init__(self, ciclo_, schema, table_name, path_file_dml):
        self.ciclo = ciclo_
        self.schema = schema
        self.table_name = table_name
        self.path_file_dml = path_file_dml

    ciclo = property(operator.attrgetter('_ciclo'))

    @ciclo.setter
    def ciclo(self, ci):
        if not ci:
            raise Exception('El campo ciclo, no puede estar vacio')
        self._ciclo = ci

    schema = property(operator.attrgetter('_schema'))

    @schema.setter
    def schema(self, sh):
        if not sh:
            raise Exception('El campo schema, no puede estar vacio')
        self._schema = sh

    table_name = property(operator.attrgetter('_table_name'))

    @table_name.setter
    def table_name(self, tb):
        if not tb:
            raise Exception('El campo table_name, no puede estar vacio')
        self._table_name = tb

    @property
    def path_file_dml(self):
        return self.path_file_dml

    path_file_dml = property(operator.attrgetter('_path_file_dml'))

    @path_file_dml.setter
    def path_file_dml(self, pfd):
        if not pfd:
            raise Exception('El campo path_file_dml, no puede estar vacio')
        self._path_file_dml = pfd
