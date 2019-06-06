from factory import DjangoModelFactory, SubFactory
from .models import ContractTemplate
from datetime import date
from roadmap.factories import YearFactory

class ContractFactory(DjangoModelFactory):
    class Meta:
        model = ContractTemplate
        django_get_or_create = ('start','end')

    count_saison = 2
    start = date(2017,2,12)
    end = date(2018,2,11)
    status = "True"
    year = SubFactory(YearFactory)

