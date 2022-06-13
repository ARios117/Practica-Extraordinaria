from django import forms
from .models import Order


class CartAddBookForm(forms.Form):

    quantity = forms.IntegerField(
        initial=1, min_value=1, label="Unidades", required=True
    )


class OrderCreateForm(forms.Form):

    first_name = forms.CharField(
        max_length=100, label="Nombre", required=True
    )
    last_name = forms.CharField(
        max_length=100, label="Apellidos", required=True
    )
    email = forms.EmailField(
        max_length=200, label="Email", required=True
    )
    address = forms.CharField(
        max_length=200, label="Dirección", required=True
    )
    city = forms.CharField(
        max_length=50, label="Ciudad", required=True
    )
    postal_code = forms.CharField(
        max_length=20, label="Código Postal", required=True
    )

    def save(self):
        if self.is_valid():
            return Order.objects.create(
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                email=self.cleaned_data['email'],
                address=self.cleaned_data['address'],
                postal_code=self.cleaned_data['postal_code'],
                city=self.cleaned_data['city']
            )

    class Meta:
        model = Order
        fields = (
            'first_name',
            'last_name',
            'email',
            'address',
            'city',
            'postal_code'
        )
