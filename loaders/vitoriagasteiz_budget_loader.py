# -*- coding: UTF-8 -*-
from budget_app.models import *
from budget_app.loaders import SimpleBudgetLoader
import os


class BudgetCsvMapper:
    expenses_mapping = {
        'default': {'ic_code': 0, 'fc_code': 1, 'full_ec_code': 2, 'description': 3, 'forecast_amount': 5, 'actual_amount': 6},
        '2018': {'ic_code': 0, 'fc_code': 1, 'full_ec_code': 2, 'description': 4, 'forecast_amount': 6, 'actual_amount': 7},
        '2019': {'ic_code': 0, 'fc_code': 1, 'full_ec_code': 2, 'description': 4, 'forecast_amount': 6, 'actual_amount': 7},
        '2020': {'ic_code': 0, 'fc_code': 1, 'full_ec_code': 2, 'description': 4, 'forecast_amount': 6, 'actual_amount': 7},
    }

    income_mapping = {
        'default': {'full_ec_code': 0, 'description': 1, 'forecast_amount': 3, 'actual_amount': 4},
        '2019': {'full_ec_code': 0, 'description': 1, 'forecast_amount': 2, 'actual_amount': 3},
        '2020': {'full_ec_code': 0, 'description': 1, 'forecast_amount': 2, 'actual_amount': 3},
    }

    default = 'default'

    def __init__(self, year, is_expense):
        column_mapping = BudgetCsvMapper.income_mapping

        if is_expense:
            column_mapping = BudgetCsvMapper.expenses_mapping

        mapping = column_mapping.get(year)

        if not mapping:
            mapping = column_mapping.get(BudgetCsvMapper.default)

        self.ic_code = mapping.get('ic_code')
        self.fc_code = mapping.get('fc_code')
        self.full_ec_code = mapping.get('full_ec_code')
        self.description = mapping.get('description')
        self.forecast_amount = mapping.get('forecast_amount')
        self.actual_amount = mapping.get('actual_amount')


class VitoriaGasteizBudgetLoader(SimpleBudgetLoader):
    # Programme codes have changed in 2015, due to new laws. Since the
    # application expects a code-programme mapping to be constant over time, we
    # are forced to amend budget data prior to 2015.
    # See https://github.com/dcabo/presupuestos-aragon/wiki/La-clasificaci%C3%B3n-funcional-en-las-Entidades-Locales
    programme_mapping = {
        # old programme: new programme
        '1111': '9123',     # OFICINA DEFENSOR DEL VECINO -> Oficina defensor del vecino
        '1201': '9205',     # PARQUE MÓVIL -> Parque móvil
        '1203': '9206',     # SUMINISTROS CENTRALIZADOS -> Suministros centralizados
        '1204': '9331',     # GESTIÓN DEL PATRIMONIO -> Gestión del patrimonio municipal
        '1211': '9201',     # SERVICIO JURÍDICO -> Asistencia y asesoría jurídica
        '1231': '9221',     # PROCESOS ELECTORALES -> Gastos de procesos electorales
        '1240': '9202',     # FUNCIÓN PÚBLICA -> Gestión de los recursos humanos
        '1242': '3351',     # EUSKERA/PERSONAL -> Euskara
        '1246': '9203',     # SERVICIO MEDICO -> Prevención y salud laboral
        '1250': '9204',     # SISTEMAS Y TECNOLOGÍA DE LA INFORMACIÓN HARDWARE-SOFTWARE -> Sistemas y tecnología de la información Hardware-Software
        '1251': '9221',     # GASTOS ELECTORALES -> Gastos de procesos electorales
        '1261': '9208',     # SUB-ALTERNOS -> Subalternos y personal de control
        '1270': '9271',     # COMUNICACIONES EXTERNAS: TELEFONÍA, INFORMACIÓN, NOTIFICACIÓN -> Comunicaciones externas, publicaciones y relaciones institucionales
        '1901': '9215',     # CONTRATO DE EFICIENCIA ENERGETICA -> Contrato de eficiencia energética
        '1902': '3422',     # CONTRATOS PISCINAS -> Contratos piscinas
        '2221': '1321',     # MANTENIMIENTO SERVICIOS OPERATIVOS -> Seguridad ciudadana
        '2223': '1321',     # EDUCACION VIAL -> Seguridad ciudadana
        '2224': '1331',     # CONTROL DE APARCAMIENTOS -> Ordenación del tráfico y del estacionamiento
        '2231': '1361',     # MANTENIMIENTO SERVICIOS OPERATIVOS DEL S.E.I.S. -> Servicio de prevención y extinción de incendios, y salvamento
        '2232': '1361',     # EMERGENCIAS SANITARIAS -> Servicio de prevención y extinción de incendios, y salvamento
        '2233': '1361',     # U.C.E.I.S -> Servicio de prevención y extinción de incendios, y salvamento
        '2234': '1361',     # EDIFICIOS E INFRAESTRUCTURAS -> Servicio de prevención y extinción de incendios, y salvamento
        '3100': '2301',     # SERVICIOS GENERALES -> Servicios generales de acción social
        '3101': '2316',     # AYUDA A LA MUJER -> Ayuda a la mujer
        '3110': '2311',     # SERVICIO DE INFANCIA -> Infancia y familia
        '3120': '2312',     # RESIDENCIAS -> Residencias
        '3121': '2313',     # CENTROS SOCIO-CULTURALES MAYORES -> Centros socio-culturales mayores
        '3122': '2314',     # APARTAMENTOS TUTELADOS -> Apartamentos tutelados
        '3131': '2321',     # ATENCIÓN Y APOYO A PERSONAS Y FAMILIAS CON NECESI. SOCIALES -> Atención y apoyo a personas y familias con necesidades sociales
        '3133': '2328',     # CENTROS CÍVICOS -> Servicios generales de acción comunitaria
        '3134': '2322',     # PRESTACIONES SOCIALES -> Servicios sociales de base
        '3135': '2315',     # ATENCIONES A COLECTIVOS DISCAPACITADOS -> Atenciones a colectivos discapacitados y especiales
        '3140': '2317',     # PENSIONISTAS -> Servicios generales de personas mayores
        '3150': '2323',     # SERVICIO DE URGENCIAS -> Servicio de urgencias
        '3151': '2324',     # CENTRO MUNICIPAL DE ACOGIDA SOCIAL -> Centro municipal de acogida social
        '3152': '2325',     # RECURSOS ATENCIÓN EXCLUIDOS SOCIALES -> Recursos atención excluidos sociales
        '3153': '2326',     # ATENCIÓN EMIGRANTES -> Atención inmigrantes
        '3210': '3201',     # MANCOMUNIDADES Y CONSORCIOS EDUCACIÓN -> Servicios generales de educación
        '3211': '3231',     # ACCIÓN  EDUCATIVA EN ESCUELAS INFANTILES Y LUDOTECAS -> Funcionamiento de centros docentes de educación infantil
        '3212': '3232',     # COLABORACIÓN EDUCATIVA CON CENTROS ESCOLARES -> Colaboración educativa con centros escolares
        '3213': '3261',     # PROMOCIÓN EDUCATIVA -> Servicios complementarios de educación
        '3214': '3201',     # SERVICIOS GENERALES -> Servicios generales de educación
        '3220': '2411',     # FORMACIÓN Y EMPLEO -> Formación y apoyo al empleo
        '3221': '2411',     # CETIC -> Formación y apoyo al empleo
        '3223': '2411',     # IGNACIO ELLACURIA -> Formación y apoyo al empleo
        '3224': '2411',     # PROGRAMA DE INTEGRACION SOCIOLABORAL -> Formación y apoyo al empleo
        '3226': '2411',     # OTROS PROGRAMAS DE FORMACIÓN DE EMPLEO -> Formación y apoyo al empleo
        '4110': '3111',     # DIRECCIÓN -> Promoción de la salud comunitaria
        '4111': '3111',     # SALUD PÚBLICA -> Promoción de la salud comunitaria
        '4112': '3112',     # SANITARIO Y DE CONSUMO -> Control sanitario y de consumo
        '4113': '3113',     # LABORATORIO MUNICIPAL -> Laboratorio municipal
        '4300': '1502',     # PATRIMONIO MUNICIPAL DEL SUELO -> Servicios generales de urbanismo
        '4322': '1511',     # GESTIÓN URBANÍSTICA -> Planeamiento urbanístico
        '4324': '1535',     # PLAN MEJORA HIDROLÓGICA -> Infraestructuras de mejora hidrológica
        '4329': '9214',     # MANTENIMIENTO DE LIMPIEZA DE CENTROS -> Limpieza de edificios e instalaciones municipales
        '4340': '1511',     # MANTENIMIENTO DE LA LEGALIDAD URBANÍSTICA -> Planeamiento urbanístico
        '4350': '1711',     # PROMOCIÓN,DIVULGACION Y MANT. ZONAS  VERDES Y VIVERO -> Parques, jardines e infraestructuras verdes
        '4360': '1651',     # MANTENIMIENTO DE INSTALACIONES ELÉCTRICAS -> Alumbrado público
        '4361': '1651',     # INVERSIONES EN INSTALACIONES ELÉCTRICAS -> Alumbrado público
        '4420': '1631',     # LIMPIEZA PÚBLICA, RSU, Y VERTEDERO -> Limpieza viaria
        '4431': '1641',     # CEMENTERIOS Y SERVICIOS FUNERARIOS -> Cementerios y servicios funerarios
        '4442': '1623',     # TRATAMIENTO DE LOS RESIDUOS URBANOS -> Tratamiento de residuos
        '4443': '1621',     # RECOGIDAS SELECTIVAS -> Recogida de residuos
        '4445': '1341',     # PLAN MOVILIDAD SOSTENIBLE -> Movilidad urbana
        '4447': '1722',     # CONTROL Y MEJORA DEL MEDIO AMBIENTE -> Protección y mejora del medio ambiente
        '4510': '3301',     # INFRAESTRUCTURAS Y ADMINISTRACION GENERAL -> Servicios generales de cultura
        '4511': '3341',     # PROGRAMAS CULTURALES -> Programas culturales
        '4512': '3391',     # ACADEMIA DE FOLKLORE -> Academia de folklore
        '4513': '3392',     # BANDA DE MÚSICA -> Banda municipal de música
        '4514': '3332',     # CENTRO CULTURAL MONTEHERMOSO Y ACTIVIDADES PLASTICAS -> Centro cultural Montehermoso
        '4515': '3371',     # CENTROS CÍVICOS -> Instalaciones de esparcimiento, ocio y tiempo libre
        '4517': '4321',     # CONGRESOS Y TURISMO -> Promoción de ciudad y apoyo al turismo
        '4518': '3342',     # ESPECTACULOS Y FESTIVALES -> Espectáculos y festivales
        '4519': '3381',     # FESTEJOS -> Fiestas populares y festejos
        '4521': '3411',     # PROMOCIÓN DEPORTIVA POPULAR. DEPORTE PARA TODOS -> Promoción y fomento del deporte
        '4522': '3421',     # MANTENIMIENTO Y CONSERVACIÓN DE INSTAL. DEPORTIVAS MUNICIPALES -> Instalaciones deportivas
        '4523': '3401',     # PROMOCIÓN DEPORTIVA POPULAR. DEPORTE PARA TODOS -> Servicios generales de deportes
        '4524': '3421',     # INVERSIONES DE MEJORA EN INSTALACIONES DEPORTIVAS -> Instalaciones deportivas
        '4530': '2371',     # SERVICIOS GENERALES -> Promoción y servicios a la juventud
        '4531': '2371',     # PROGRAMA DE VOLUNTARIADO -> Promoción y servicios a la juventud
        '4532': '2371',     # PROGRAMA CLUB JOVEN -> Promoción y servicios a la juventud
        '4533': '2371',     # PROMOCION SOCIOCULTURAL -> Promoción y servicios a la juventud
        '4534': '2371',     # O.M.I.J. -> Promoción y servicios a la juventud
        '4536': '2371',     # LUDOTECAS -> Promoción y servicios a la juventud
        '4541': '3321',     # ARCHIVOS Y BIBLIOTECAS -> Bibliotecas públicas
        '4621': '9271',     # GABINETE DE PRENSA -> Comunicaciones externas, publicaciones y relaciones institucionales
        '4622': '9242',     # APOYO A ASOCIACIONES -> Movimientos asociativos
        '4630': '2391',     # COOPERACIÓN AL DESARROLLO -> Cooperación al desarrollo
        '5112': '1331',     # ORDENACIÓN DEL TRAFICO -> Ordenación del tráfico y del estacionamiento
        '5142': '4333',     # REVITALIZACIÓN CASCO HISTÓRICO -> Revitalización casco histórico
        '5330': '1742',     # MEJORA DE LA INFRAESTRUCTURA URBANA -> Limpieza y recogida de residuos medio rural
        '5331': '1743',     # MEJORA DEL MEDIO NATURAL -> Reparación, conservación y mantenimiento de espacios medio rural
        '5332': '1749',     # PROMOCIÓN DE ACTIVIDADES SOCIALES EN LAS ENTIDADES LOCALES -> Servicios generales medio rural
        '7110': '4314',     # CAMPAÑAS PROMOCION ECONOMICA -> Promoción y dinamización comercial
        '7211': '4331',     # PROMOCIÓN DE EMPRESAS Y ACTIVIDADES ECONÓMICAS -> Promoción y dinamización económica y empresarial
        '7213': '4334',     # PARTICIPACIÓN EN EMPRESAS Y PROYECTOS INSTITUCIONALES -> Participaciones en capital social
        '9210': '4411',     # TRANSFERENCIAS A SOCIEDADES MUNICIPALES -> Transporte colectivo urbano de viajeros
        # old programmes without direct mapping but with changing politic codes
        '1110': '912X',     # CORPORACIÓN MUNICIPAL
        '1200': '921X',     # EDIFICIOS MUNICIPALES Y ASIMILADOS
        '1220': '921Y',     # DEPENDENCIAS GENERALES
        '1900': '920X',     # SERVICIOS DE ADMINISTRACIÓN GENERAL
        '3225': '431X',     # COMERCIO
        '4114': '493X',     # O.M.I.C.
        '4444': '172X',     # VITORIA-GASTEIZ GREEN CAPITAL
        '4449': '172Y',     # MEDIDAS DE CONTROL MEDIOAMBIENTAL
        '5110': '453X',     # INVERSIONES EN REPOSICIÓN DE INFRAESTRUCTURA
        '5111': '453X',     # MANTENIMIENTO DE INFRAESTRUCTURAS
        '5113': '453X',     # SEÑALIZACIÓN VIARIA
        '5131': '441X',     # TRANSPORTE URBANO MUNICIPAL
        '5141': '45XX',     # PROYECTOS FIL
        '6111': '932X',     # ADMINISTRACIÓN TRIBUTARIA Y RECAUDACIÓN
        '6112': '931X',     # ADMINISTRACIÓN FINANCIERA-INTERVENCIÓN
        '6113': '931Y',     # ADMINISTRACIÓN FINANCIERA
    }

    # We override this to allow a different classification per year
    def get_institutional_classification_path(self, path):
        return os.path.join(path, 'clasificacion_organica.csv')

    # make year data available in the class and call super
    def load(self, entity, year, path, status):
        self.year = year
        SimpleBudgetLoader.load(self, entity, year, path, status)

    # Parse an input line into fields
    def parse_item(self, filename, line):
        # Type of data
        is_expense = (filename.find('gastos.csv') != -1)
        is_actual = (filename.find('/ejecucion_') != -1)

        # Mapper
        mapper = BudgetCsvMapper(self.year, is_expense)

        # Expenses
        if is_expense:
            # Institutional code
            # We got 4 or 6 digit institutional codes as input, but we only need
            # the first 2
            ic_code = line[mapper.ic_code][:2]
            # We check if we need to amend the code
            if int(self.year) > 2015 and ic_code == '16':
                ic_code = '10'
            # We build the actual code
            ic_code = '00' + ic_code

            # Functional code
            fc_code = line[mapper.fc_code]

            # For pre 2015 budgets we may need to amend the programme code
            if int(self.year) < 2015:
                fc_code = VitoriaGasteizBudgetLoader.programme_mapping.get(fc_code, fc_code)

            # Economic code
            full_ec_code = line[mapper.full_ec_code]

            # Concepts are the first 3 digits from the economic codes
            ec_code = full_ec_code[:3]

            # Item numbers are the last 2 digits from the economic codes
            # (digits 4 and 5)
            item_number = full_ec_code[-2:]

            # Description
            description = line[mapper.description]

            # Parse amount
            amount = line[mapper.actual_amount if is_actual else mapper.forecast_amount]
            amount = self._parse_amount(amount)

        # Income
        else:
            # Institutional code (all income goes to the root node)
            ic_code = '0000'

            # Functional code
            # We don't have functional codes in income
            fc_code = None

            # Economic code
            full_ec_code = line[mapper.full_ec_code]

            # Concepts are the firts 3 digits from the economic codes
            ec_code = full_ec_code[:3]

            # Item numbers are the last 2 digits from the economic codes
            # (digits 4 and 5)
            item_number = full_ec_code[-2:]

            # Description
            description = line[mapper.description]

            # Parse amount
            amount = line[mapper.actual_amount if is_actual else mapper.forecast_amount]
            amount = self._parse_amount(amount)

        return {
            'is_expense': is_expense,
            'is_actual': is_actual,
            'fc_code': fc_code,
            'ec_code': ec_code,
            'ic_code': ic_code,
            'item_number': item_number,
            'description': description,
            'amount': amount
        }
