
#  ApoloABTSSantander
Este proyecto tiene como finalidad obtener información de HDFS y transportarla a Oracle.

[![N|Solid](https://trello-attachments.s3.amazonaws.com/5a1baed8137a75335503cc3a/5b33d15509d605077c55ce57/9bb824613c209da4d6582e11b7b14dcc/ABTS1ETL.PNG)](https://nodesource.com/products/nsolid)

#### Herramientas utilizadas:
- Spark 1.6
- Python 2.6
- Hive 1.1.0
- Hadoop 2.6

#### Estructura del proyecto

[![N|Solid](https://trello-attachments.s3.amazonaws.com/5a1baed8137a75335503cc3a/5b33d15509d605077c55ce57/066e645e4f1b64594549764dfad56b76/2apoloEstructura.PNG)](https://nodesource.com/products/nsolid)


#### Directorios
- **conf:** Contiene archivos de propiedades y ficheros con extensión ‘hql’, cada fichero comparte la misma lógica ya que solo encontraremos parámetros de configuración y scripts (ddl, dml) en hive estáticos.
- **engine:** Se encuentra el core del desarrollo, clases y funciones para limpieza y transformación de datos.
- **libs:** Librerías necesarias para el desarrollo
- **main:** Fichero principal donde inicia la ejecución del programa
- **models:** Directorio donde encontramos las clases modelo necesarias para el proyecto
- **test:** Cada objeto, modulo o función de utilería tiene su respectiva prueba unitaria en este apartado se encuentran.
- **utils:** En este directorio encontraremos clases y funciones que son utilizados en más de una clase core o de  modelo de datos, se le denomina utilerías porque no son creados para un solo fin sino más bien son utilizados por más de un actor.

#### Especificaciones de ejecución del programa
>El fichero se encuentra en “main” y se llama “principal.py” este script es el encargado de mapear todos los ficheros del proyecto y cargarlos en un apartado temporal de spark
>Importante : Establecer una conexión al clúster ya sea mediante ssh o una conexión en putty

##### Abrir una consola
.
```sh
# Acceder al directorio main del proyecto
user@host$ ls -rlht
/home/user/.tmp/apoloABTSSantander-master-dev
user@host$ cd main/
-rw-r--r-- 1 n557453 domain users    0 Sep  4 19:18 __init__.py
-rw-r--r-- 1 n557453 domain users 3.0K Sep  4 19:18 principal.py
# Ejecutar el proyecto
user@host$ spark-submit principal.py --jars ../libs/spark-csv_2.10-1.5.0.jar,../libs/univocity-parsers-2.1.2.jar, ../libs/commons-csv-1.4.jar, ../libs/ojdbc7-12.1.0.2.jar, ../libs/spark-avro_2.11-3.2.0.jar
```
** **
#### Estándares de codificación
A continuación se describe las especificaciones de codificación y estándares que se aplican al desarrollo de ABTS por parte del Lago.

#### **Clases**
Todos los nombres de clases tienen prefijo del apartado para el cual fueron creados por ejemplo:
- **ABTS**********:** Específica que es un objeto que se creó para trabajar con los datos del lago, es decir encapsular alguna tabla temporal, limpieza de datos, es similar a un DAO en java.
- **Dim***********:** Este tipo de objetos son contenedores de la información de las dimensiones solo se usan para armar el módulo de exportación a Oracle.

- **Utils**: Son clases de utilerías que contienen funciones de uso general, funciones que usa el Fichero principal o que usa cualquier objeto de tipo ABTS**** para realizar algún tipo de acción (transposición, pivot, filter) sobre los datos.
- **'*****Companion**: Es un objeto acompañante son implementados en las pruebas unitarias, sirven para obtener los datos necesarios para llevar a cabo las pruebas unitarias, es un tipo de objeto DTO equivalente en java
- **'**********Test**: Este tipo de Clases son parte de las pruebas unitarias y contienen una o varias funciones de validación. Todas las clases anteriores tienen su respectiva prueba unitaria

#### **Funciones o Métodos**
> Se han implementado 3 clasificaciones de métodos, los cuales son:

-	Funciones o métodos de acceso (retorna Any o None)
-	Funciones o métodos de predicado(retorna un tipo booleano)
-	Funciones  de uso generales(funciones de tipo void, que no retornan nada)

**Funciones de predicado que devuelven booleano:** Estas funciones se caracterizan por realizar una pregunta concreta. Todas las funciones de este tipo comienzan con el prefijo 'is' P.E para preguntar si la cadena esta vacía 'is_empty (...)'

**Funciones de acceso:** Todas las funciones de acceso tiene el prefijo get, P.E para obtener un contexto de Spark 'get_spark_context (...)'

**Funciones de uso General:** Este tipo de funciones se nombraron de esta manera ya que implican algún tipo de trabajo diferente, ya sea para cargar variables de un fichero de propiedades 'load**** (...)', eliminar una tabla ‘delete (...)' este tipo de funciones no regresan ningún tipo de valor si los comparamos con java serian funciones de tipo void

> **Nota:** Para las funciones de tipo set****(...) es muy nula la aparición de >este tipo de bloques de código en el proyecto, y solo implican agregar un >valor al atributo del objeto referido P.E

#### Estándar de ficheros (No involucran código en python):

**Ficheros de propiedades:** Todos los ficheros de propiedades tienen el sufijo '.properties' la esencia de estos ficheros es para que todas las clases y/o funciones compartan una misma configuración de tal forma que sea más flexible el desarrollo cuando existan cambios en los parámetros.
**Ficheros con prefijo DDL...hql:** Este tipo de ficheros indican que solo contienen comandos de tipo create, alter o drop(Estos ficheros son ejecutados en Hive)
**Ficheros con prefijo DML...hql:** Ficheros que contienen código que ejecutan solo comandos del tipo 'select, insert, update o delete'.(Estos ficheros son ejecutados en Hive)


Licencia **Santander**
Septiembre 05 2018