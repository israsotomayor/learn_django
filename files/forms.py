from django import forms

from .models import Car


class CarForm(forms.Form):
    name = forms.CharField()
    price = forms.DecimalField()


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'price']

    def clean_name(self, *args, **kwargs):
        instance = self.instance
        name = self.cleaned_data.get('name')
        qs = Car.objects.filter(name__iexact=name)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk) # id=instance.id
        if qs.exists():
            raise forms.ValidationError("Este nombre ya ha sido usado. Por favor selecciona otro")
        return name
