--RECIBE UN PARAMETRO PARA EL CICLO A INGESTAR
--EL PARAMETRO CICLO DEBE CUMPLIR LA FORMA yyyymm ej. 201412

--Especificar la pila
set mapred.job.queue.name=crm_resource_pool;
set mapred.reduce.tasks = 2;

--DIM_TENENCIA_CAPTACION_PYME
INSERT OVERWRITE TABLE SB_CRM.abts_dim_tenencia_captacion_pyme
SELECT DISTINCT
EPYMES
,TRADICIONAL
,SPYMES
,RESTO_VISTA
,INVERSION_VISTA
,PLAZO
,FONDOS
,PLAZO_OP
,FONDOS_OP
,MDD
,${hiveconf:varCiclo}
FROM ${hiveconf:varSchema}.${hiveconf:varTablaFuente} WHERE data_date_part=${hiveconf:varCiclo};

--DIM_TENENCIA_COLOCACION_PYME
INSERT OVERWRITE TABLE SB_CRM.abts_dim_tenencia_colocacion_pyme
SELECT DISTINCT
HIPOTECARIO
,AUTO
,CRED_SIMPLE
,CRED_COMERCIAL
,AGIL
,COMEX
,AGRO
,LINEA
,RESTO_COL
,TDC
,TDE
,ID_CC_IMP_VIG
,ID_CC_EXP_VIG
,${hiveconf:varCiclo}
FROM ${hiveconf:varSchema}.${hiveconf:varTablaFuente} WHERE data_date_part=${hiveconf:varCiclo};

--DIM_TENENCIA_SEGUROS_PYME
INSERT OVERWRITE TABLE SB_CRM.abts_dim_tenencia_seguros_pyme
SELECT DISTINCT
SEG_PROTEGIDA
,SEG_MEDADVANCE
,SEG_CRED_RELATED
,SEG_RESTO
,${hiveconf:varCiclo}
FROM ${hiveconf:varSchema}.${hiveconf:varTablaFuente} WHERE data_date_part=${hiveconf:varCiclo};

--DIM_TXS_BCA_ELEC_PYME
INSERT OVERWRITE TABLE SB_CRM.abts_dim_txs_bca_elec_pyme
SELECT DISTINCT
BE_CONSULTAS
,BE_CONSULTAS_INT
,BE_CHEQUERA_SEG
,BE_PAG_DIRECTO
,BE_CTOS_IMPLANTADAS
,BE_CTOS_CONSULTIVAS
,BE_CTOS_TRANSACCIONAL
,BE_COMISIONABLES
,${hiveconf:varCiclo}
FROM ${hiveconf:varSchema}.${hiveconf:varTablaFuente} WHERE data_date_part=${hiveconf:varCiclo};

--DIM_TXS_COBROS_PAGOS_PYME
INSERT OVERWRITE TABLE SB_CRM.abts_dim_txs_cobros_pagos_pyme
SELECT DISTINCT
ID_TDD
,ID_PAGPROV_MB
,ID_PAGPROV_OB
,ID_PAGPROV
,ID_IMPUESTOS
,ID_PROVISIONALES
,ID_PAGOCHEQUES
,ID_COBROCHEQUES
,ID_RECAUD_FISICA
,ID_RECAUD_ELEC
,ID_RETIROS
,ID_GIROS
,ID_DEPREF
,ID_ONLINE_CHEQUE
,ID_PAGO_DIREC
,ID_PAGO_OCURRE
,ID_CONFIRMING
,${hiveconf:varCiclo}
FROM ${hiveconf:varSchema}.${hiveconf:varTablaFuente} WHERE data_date_part=${hiveconf:varCiclo};

--DIM_TXS_SERVICIOS_PYME
INSERT OVERWRITE TABLE SB_CRM.abts_dim_txs_servicios_pyme
SELECT DISTINCT
ID_CAMBIOS
,ID_CAMBIOS_FXONLINE
,ID_DERIVADOS_TASA
,ID_NOMINA
,ID_TPV
,ID_DOMIC_PAG
,ID_DOMIC_COB
,ID_EMI_MB
,ID_EMI_OB
,ID_REC_MB
,ID_REC_OB
,ID_CUSTODIA
,ID_TRANS_BE
,ID_TRANS_DIGITALES
,ID_INTERNACIONALES
,ID_INTERNACIONALES_REC
,ID_REMESAS
,${hiveconf:varCiclo}
FROM ${hiveconf:varSchema}.${hiveconf:varTablaFuente} WHERE data_date_part=${hiveconf:varCiclo};