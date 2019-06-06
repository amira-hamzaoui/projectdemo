from factory import DjangoModelFactory, SubFactory
from .models import Contract
from datetime import date


class ContractFactory (DjangoModelFactory):
    class Meta:
        model = Contract
        django_get_or_create = ('start', 'end')

    count_season = 2
    start = date(2017, 2, 12)
    end = date(2018, 2, 11)
    status = "True"
    year = 2018
