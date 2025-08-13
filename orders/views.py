from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView

from orders.forms import ReservationCreateForm
from orders.models import Reservation



class CreateOrderView(LoginRequiredMixin, FormView):
    form_class = ReservationCreateForm
    login_url = "/user/login/"

    def form_valid(self, form):
        user = self.request.user

        reservation = Reservation.objects.create(
            user = user,
            phone = form.cleaned_data["phone"],
            quantity = form.cleaned_data["quantity"],
            time = form.cleaned_data["time"],
            date = form.cleaned_data["date"],
            comment = form.cleaned_data["comment"],
        )
                
        return HttpResponseRedirect(reverse('main:index'))

    def form_invalid(self, form):
        return HttpResponse('Ошибка')
    
# @login_required
# def create_order(request):

#     if request.method == 'POST':
#         form = ReservationCreateForm(data=request.POST)

        
#         if form.is_valid():
                
#             user = request.user

#             reservation = Reservation.objects.create(
#                 user = user,
#                 phone = form.cleaned_data["phone"],
#                 quantity = form.cleaned_data["quantity"],
#                 time = form.cleaned_data["time"],
#                 date = form.cleaned_data["date"],
#                 comment = form.cleaned_data["comment"],
#                 )
                
            

#     return HttpResponseRedirect(reverse('main:index'))
