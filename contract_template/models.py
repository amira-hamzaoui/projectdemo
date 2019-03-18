from polymorphic.models import PolymorphicModel
from django.db.models import (
    Model,
    ForeignKey,
    PositiveIntegerField,
    DateField,
    BooleanField,
    CASCADE
)


class ContractTemplate(PolymorphicModel):

    year = PositiveIntegerField()
    count_season = PositiveIntegerField(default=1)
    start = DateField()
    end = DateField()
    status = BooleanField(default=True)

    class Meta:
        unique_together = ("start", "end")

    def __unicode__(self):
        return "{}-{}".format(self.start, self.end)

class Period(PolymorphicModel):

    contract = ForeignKey(ContractTemplate, on_delete=CASCADE)
    start = DateField()
    end = DateField()
    season = PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("start", "end")
