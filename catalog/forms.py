from django import forms


class Filter_form(forms.Form):
    mans = [
        ('bosch', 'BOSCH'),
        ('interskol', 'ИНТЕРСКОЛ'),
        ('makita', 'Makita'),
        ('vihr', 'ВИХРЬ'),
        ('zubr', 'Зубр'),
    ]
    manufacturer = forms.MultipleChoiceField(choices=mans, required=False)
    minprice = forms.IntegerField(required=False)
    maxprice = forms.IntegerField(required=False)