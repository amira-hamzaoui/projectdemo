from django.contrib import admin
from django.forms import ModelForm, DateField
from django.forms.widgets import SelectDateWidget

from contract.models import Contract, Period


class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = "__all__"


class PeriodForm(ModelForm):
    start = DateField(widget=SelectDateWidget(), )
    end = DateField(widget=SelectDateWidget(), )


class PeriodInline(admin.TabularInline):
    model = Period
    extra = 0
    form = PeriodForm


@admin.register(Contract)
class ContractTemplateAdmin(admin.ModelAdmin):
    form = ContractForm
    list_display = ('pk', 'start', 'end', 'status')
    inlines = [PeriodInline, ]
