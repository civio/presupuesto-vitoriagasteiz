# -*- coding: UTF-8 -*-
from budget_app.loaders import PaymentsLoader
from budget_app.models import Budget
from vitoriagasteiz_budget_loader import VitoriaGasteizBudgetLoader

import dateutil.parser


class PaymentsCsvMapper:
    column_mapping = {
        'default': {'fc_code': 6, 'date': 1, 'payee': 15, 'description': 17, 'amount': 19},
    }

    default = 'default'

    def __init__(self, year):
        column_mapping = PaymentsCsvMapper.column_mapping
        mapping = column_mapping.get(year)

        if not mapping:
            mapping = column_mapping.get(PaymentsCsvMapper.default)

        self.fc_code = mapping.get('fc_code')
        self.date = mapping.get('date')
        self.payee = mapping.get('payee')
        self.description = mapping.get('description')
        self.amount = mapping.get('amount')


class VitoriaGasteizPaymentsLoader(PaymentsLoader):
    # Parse an input line into fields
    def parse_item(self, budget, line):
        # Mapper
        mapper = PaymentsCsvMapper(budget.year)

        # We got the functional code
        fc_code = line[mapper.fc_code]

        # For pre 2015 budgets we may need to amend the programme code
        # Some payments with 2014 classification are still present in 2015
        if int(budget.year) <= 2015:
            fc_code = VitoriaGasteizBudgetLoader.programme_mapping.get(fc_code, fc_code)

        # first two digits of the functional code make the policy id
        policy_id = fc_code[:2]

        # but what we want as area is the policy description
        policy = Budget.objects.get_all_descriptions(budget.entity)['functional'][policy_id]

        # We got a localized date
        date = line[mapper.date]
        date = dateutil.parser.parse(date, dayfirst=True).strftime("%Y-%m-%d")

        # Payee data
        payee = line[mapper.payee].strip()

        # Some rows doesn't include payee data, so we asign an arbitrary value
        if not payee:
            payee = "OTROS" if budget.entity.language == 'es' else 'BESTE BATZUK'

        # we haven't got any anonymized entries
        anonymized = False

        # Description
        description = line[mapper.description].strip()

        # We got a localized amount
        amount = line[mapper.amount]
        amount = self._read_spanish_number(amount)

        return {
            'area': policy,
            'programme': None,
            'fc_code': None,  # We don't try (yet) to have foreign keys to existing records
            'ec_code': None,
            'ic_code': None,
            'date': date,
            'payee': payee,
            'anonymized': anonymized,
            'description': description,
            'amount': amount
        }
