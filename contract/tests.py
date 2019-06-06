from django.test import TestCase
from .factories import ContractFactory
from contract.models import Contract
from datetime import date, datetime, timedelta
from django.db.models import Q


class ContractModelTest(TestCase):

    def setUp(self):
        # Prepare a new, clean session
        self.contract_template = ContractFactory()
        self.contract2 = ContractFactory.create(year="2018", start=date(2018,2,12), end = date(2019,2,11))
        self.contract1 = ContractFactory.create(year="2019", start=date(2018,2,12), end = date(2019,2,15))
    def test_create_contract(self):

        entry = Contract(start=datetime.today(), end=datetime.today())
        self.assertEqual(entry.start, entry.start)
        self.assertEqual(entry.end, entry.end)

    def test_create_contract(self):

        end_contrat_must_be = self.contract_template.start + timedelta(days=365)
        self.assertIsNot(self.contract_template.end, end_contrat_must_be)
    def test_saison_count(self):
        self.assertIsNot(self.contract_template.count_season, 0)

    def test_unique_data_contract(self):

        # Creer le premier contrat
        dates = (self.contract2.start, self.contract2.end)
        contacts = Contract.objects.filter(
            Q(start__in=dates) or Q(end__in=dates)
        )
        self.assertNotEqual(contacts.count(), 0)

    def test_integrity_dates(self):
        self.assertIn(self.contract_template.year,
                      [self.contract_template.start.year, self.contract_template.end.year],
                            msg="les date ne sont pas conforme à l'annnee du contrat")
