import six

if six.PY2:
    from vitoriagasteiz_budget_loader import VitoriaGasteizBudgetLoader
    from vitoriagasteiz_payments_loader import VitoriaGasteizPaymentsLoader
else:
    from .vitoriagasteiz_budget_loader import VitoriaGasteizBudgetLoader
    from .vitoriagasteiz_payments_loader import VitoriaGasteizPaymentsLoader
