from django import forms



from orders.models import Reservation

class ReservationCreateForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    quantity = forms.IntegerField()
    time = forms.CharField()
    date = forms.CharField()
    comment = forms.CharField(required=False)

    class Meta:
        model = Reservation
        fields = (
            "first_name",
            "last_name",
            "phone",
            "quantity",
            "time",
            "date",
            "comment"
        )

