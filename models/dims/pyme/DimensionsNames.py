from abc import ABCMeta, abstractmethod
import operator


class DimensionsNames:
    __metaclass__ = ABCMeta
    tenencia_captacion_pyme = ''
    tenencia_colocacion_pyme = ''
    tenencia_seguros_pyme = ''
    txs_bca_elec_pyme = ''
    txs_cobros_pagos_pyme = ''
    txs_servicios_pyme = ''


class DimNameOracle(object):

    def __init__(self, tenen_captacion_pyme, tenen_colocacion_pyme, tenen_seguros_pyme, txs_bca_elec_pyme,
                 txs_cobros_pagos_pyme, txs_servicios_pyme):
        print 'Nombres de las dimensiones en Oracle'
        self.tenencia_captacion_pyme = tenen_captacion_pyme
        self.tenencia_colocacion_pyme = tenen_colocacion_pyme
        self.tenencia_seguros_pyme = tenen_seguros_pyme
        self.txs_bca_elec_pyme = txs_bca_elec_pyme
        self.txs_cobros_pagos_pyme = txs_cobros_pagos_pyme
        self.txs_servicios_pyme = txs_servicios_pyme

    tenencia_captacion_pyme = property(operator.attrgetter('_tenencia_captacion_pyme'))

    @tenencia_captacion_pyme.setter
    def tenencia_captacion_pyme(self, tcpym):
        if not tcpym:
            raise Exception('Error, el campo tenencia_captacion_pyme no puede ir vacio')
        self._tenencia_captacion_pyme = tcpym

    tenencia_colocacion_pyme = property(operator.attrgetter('_tenencia_colocacion_pyme'))

    @tenencia_colocacion_pyme.setter
    def tenencia_colocacion_pyme(self, tcolpy):
        if not tcolpy:
            raise Exception('Error, el campo tenencia_colocacion_pyme no puede ir vacio')
        self._tenencia_colocacion_pyme = tcolpy

    tenencia_seguros_pyme = property(operator.attrgetter('_tenencia_seguros_pyme'))

    @tenencia_seguros_pyme.setter
    def tenencia_seguros_pyme(self, tsegpy):
        if not tsegpy:
            raise Exception('Error, el campo tenencia_seguros_pyme no puede ir vacio')
        self._tenencia_seguros_pyme = tsegpy

    txs_bca_elec_pyme = property(operator.attrgetter('_txs_bca_elec_pyme'))

    @txs_bca_elec_pyme.setter
    def txs_bca_elec_pyme(self, txbca):
        if not txbca:
            raise Exception('Error, el campo txs_bca_elec_pyme no puede ir vacio')
        self._txs_bca_elec_pyme = txbca

    txs_cobros_pagos_pyme = property(operator.attrgetter('_txs_cobros_pagos_pyme'))

    @txs_cobros_pagos_pyme.setter
    def txs_cobros_pagos_pyme(self, tcobpy):
        if not tcobpy:
            raise Exception('Error el campo txs_cobros_pagos_pyme no puede ir vacio')
        self._txs_cobros_pagos_pyme = tcobpy

    txs_servicios_pyme = property(operator.attrgetter('_txs_servicios_pyme'))

    @txs_servicios_pyme.setter
    def txs_servicios_pyme(self, tserv):
        if not tserv:
            raise Exception('Error el campo txs_servicios_pyme no puede ir vacio')
        self._txs_servicios_pyme = tserv


class DimNameLago(object):

    def __init__(self, dim_tenen_captacion_pyme, dim_tenen_colocacion_pyme, dim_tenen_seguros_pyme,
                 dim_txs_bca_elec_pyme, dim_txs_cobros_pagos_pyme, dim_txs_servicios_pyme):
        print 'Nombres de las dimensiones en el Lago'
        self.tenencia_captacion_pyme = dim_tenen_captacion_pyme
        self.tenencia_colocacion_pyme = dim_tenen_colocacion_pyme
        self.tenencia_seguros_pyme = dim_tenen_seguros_pyme
        self.txs_bca_elec_pyme = dim_txs_bca_elec_pyme
        self.txs_cobros_pagos_pyme = dim_txs_cobros_pagos_pyme
        self.txs_servicios_pyme = dim_txs_servicios_pyme

    tenencia_captacion_pyme = property(operator.attrgetter('_tenencia_captacion_pyme'))

    @tenencia_captacion_pyme.setter
    def tenencia_captacion_pyme(self, tcpym):
        if not tcpym:
            raise Exception('Error, el campo tenencia_captacion_pyme no puede ir vacio')
        self._tenencia_captacion_pyme = tcpym

    tenencia_colocacion_pyme = property(operator.attrgetter('_tenencia_colocacion_pyme'))

    @tenencia_colocacion_pyme.setter
    def tenencia_colocacion_pyme(self, tcolpy):
        if not tcolpy:
            raise Exception('Error, el campo tenencia_colocacion_pyme no puede ir vacio')
        self._tenencia_colocacion_pyme = tcolpy

    tenencia_seguros_pyme = property(operator.attrgetter('_tenencia_seguros_pyme'))

    @tenencia_seguros_pyme.setter
    def tenencia_seguros_pyme(self, tsegpy):
        if not tsegpy:
            raise Exception('Error, el campo tenencia_seguros_pyme no puede ir vacio')
        self._tenencia_seguros_pyme = tsegpy

    txs_bca_elec_pyme = property(operator.attrgetter('_txs_bca_elec_pyme'))

    @txs_bca_elec_pyme.setter
    def txs_bca_elec_pyme(self, txbca):
        if not txbca:
            raise Exception('Error, el campo txs_bca_elec_pyme no puede ir vacio')
        self._txs_bca_elec_pyme = txbca

    txs_cobros_pagos_pyme = property(operator.attrgetter('_txs_cobros_pagos_pyme'))

    @txs_cobros_pagos_pyme.setter
    def txs_cobros_pagos_pyme(self, tcobpy):
        if not tcobpy:
            raise Exception('Error el campo txs_cobros_pagos_pyme no puede ir vacio')
        self._txs_cobros_pagos_pyme = tcobpy

    txs_servicios_pyme = property(operator.attrgetter('_txs_servicios_pyme'))

    @txs_servicios_pyme.setter
    def txs_servicios_pyme(self, tserv):
        if not tserv:
            raise Exception('Error el campo txs_servicios_pyme no puede ir vacio')
        self._txs_servicios_pyme = tserv
