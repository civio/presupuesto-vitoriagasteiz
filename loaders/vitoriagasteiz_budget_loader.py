# -*- coding: UTF-8 -*-
from budget_app.models import *
from budget_app.loaders import SimpleBudgetLoader


class BudgetCsvMapper:
    expenses_mapping = {
        '2018': {'ic_code': 0, 'fc_code': 1, 'full_ec_code': 2, 'description': 3, 'forecast_amount': 4, 'actual_amount': 6},
    }

    income_mapping = {
        '2018': {'full_ec_code': 0, 'description': 1, 'forecast_amount': 2, 'actual_amount': 4},
    }

    default = '2018'

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
    }

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
            # We got 4 or 6 digit institutional codes as input, so we normalize
            # them at 6 and add trailing zeroes when required
            ic_code = '000' #line[mapper.ic_code].ljust(6, '0')

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
            ic_code = '000'

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
