from django import forms

class VesAvtoForm(forms.Form):
    numberAuto = forms.IntegerField(label='номер')
    seriaAuto = forms.CharField(label='серия', max_length=100)
    regionAuto = forms.IntegerField(label='регион')
    numberPricep = forms.IntegerField(label='номер')
    seriaPricep = forms.CharField(label='серия', max_length=100)
    regionPricep = forms.IntegerField(label='регион')
    nakladnaya = forms.CharField(label="накладная", max_length=100)
    auto_in = forms.BooleanField(label='автомобиль на въезд')
    ves = forms.FloatField(label='ИТОГ')
