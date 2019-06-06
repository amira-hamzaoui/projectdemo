from django.core.exceptions import ValidationError
from django.db.models import Model, ForeignKey, Q, Manager, CASCADE
from django.db.models import PositiveIntegerField, DateField, BooleanField
from polymorphic.models import PolymorphicModel, PolymorphicManager
from datetime import timedelta


class Contract(Model):
    year = PositiveIntegerField()
    count_season = PositiveIntegerField(default=1)
    start = DateField()
    end = DateField()
    status = BooleanField(default=True)
    objects = Manager()

    class Meta:
        unique_together = ("start", "end")

    def __unicode__(self):
        return "{}-{}".format(self.start, self.end)

    # def clean(self):
    #     # Don't allow contract with similar or intgrated dates.
    #     q = Contract.objects.filter(
    #         Q(start__in=(self.start, self.end)) or Q(end__in=(self.start, self.end))
    #     ).count()
    #     print(q)
    #     if q > 0:
    #         raise ValidationError({
    #             'start': ValidationError('invalid start date.', code='required'),
    #             'end': ValidationError('Invalid end date.', code='invalid'),
    #         })
    #     print(self.end,  self.start + timedelta(days=365))
    #     #if self.end != self.start + timedelta(days=365):
    #      #   raise ValidationError({
    #       #      'end': ValidationError('end date must be one year after start date.', code='invalid'),
    #        # })


class BasePeriod(PolymorphicModel):
    start = DateField()
    end = DateField()
    objects = PolymorphicManager()


class Period(BasePeriod):
    contract = ForeignKey(Contract, on_delete=CASCADE)
    season = PositiveIntegerField(default=1)  # TODO: add contraint : between 1 and Contract.count_saison
