from django.contrib import admin
from django.forms import ModelForm, DateField
from django.forms.widgets import DateInput, SelectDateWidget

from contract_template.models import ContractTemplate, Period

class ContractTemplateForm(ModelForm):

    class Meta:
        model = ContractTemplate
        fields = "__all__"

class PeriodForm(ModelForm):

    start = DateField(widget=SelectDateWidget(), )
    end = DateField(widget=SelectDateWidget(), )





class PeriodInline(admin.TabularInline):
    model = Period
    extra = 0
    form = PeriodForm



@admin.register(ContractTemplate)
class ContractTemplateAdmin(admin.ModelAdmin):

    form = ContractTemplateForm
    list_display = ('pk','start', 'end', 'status')
    inlines = [PeriodInline,]