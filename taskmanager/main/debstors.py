# models.py
from django.db import models
from django.conf import settings


class Debt(models.Model):
    full_name = models.CharField(max_length=100)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_debt = models.DecimalField(max_digits=10, decimal_places=2)
    accrued_interest = models.DecimalField(max_digits=10, decimal_places=2)
    opening_date = models.DateField()


# views.py
from django.http import JsonResponse
from .models import Debt


def get_debtors(request, date):
    debtors = Debt.objects.filter(opening_date__lte=date, remaining_debt__gt=0)
    debtor_list = []
    for debtor in debtors:
        debtor_data = {
            'full_name': debtor.full_name,
            'loan_amount': debtor.loan_amount,
            'remaining_debt': debtor.remaining_debt,
            'accrued_interest': debtor.accrued_interest
        }
        debtor_list.append(debtor_data)

    return JsonResponse(debtor_list, safe=False)

