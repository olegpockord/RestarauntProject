from django.http import Http404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse as HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.mail import BadHeaderError
from django.urls import reverse


from feedback.tasks import send_email_to_staff_task
from user.models import User



class UserContactView(LoginRequiredMixin, TemplateView):
    template_name = 'feedback/contact_form.html'
    login_url = "/user/login/"

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        message = request.POST['message']
        name = f"{first_name} {last_name}"
        try:
            send_email_to_staff_task.delay(name=name, message=message, email=["Youremail"])
        except BadHeaderError:
            
            raise Http404("Error")

        return HttpResponseRedirect(reverse("main:index"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact'
        return context




class ContactStaffView(TemplateView):
    template_name = 'feedback/contact_form_staff.html'

    def post(self, request):
        title = request.POST['first']
        email = [request.POST['Email']]
        flag = request.POST.getlist('toall')
        message = request.POST['message']

        if len(flag) > 0:
            email = list(User.objects.values_list("email", flat=True)
                         .distinct().exclude(email=""))

        send_email_to_staff_task.delay(name=title, message=message, email=email)

        return HttpResponseRedirect(reverse("main:index"))
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'ContactStaff'
        return context

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)




# @staff_member_required
# def contact_staff(request):

#     if request.method == 'POST':
#         title = request.POST['first']
#         email = [request.POST['Email']]
#         flag = request.POST.getlist('toall')
#         message = request.POST['message']

#         if len(flag) > 0:
#             email = list(User.objects.values_list("email", flat=True)
#                          .distinct().exclude(email=""))

#         send_mail(
#             title,
#             message,
#             'settings.EMAIL_HOST_USER',
#             recipient_list = email,
#             fail_silently=False,
#         )
#         return HttpResponseRedirect(reverse("main:index"))

#     context = {
#         'title': 'ContactStaff',
#     }
#     return render(request, 'feedback/contact_form_staff.html', context)


# @login_required(login_url="/user/login/")
# def contact_user(request):
    
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         message = request.POST['message']
#         name = f"{first_name} {last_name}"
#         try:
#             send_mail(
#                 name,
#                 message,
#                 'settings.EMAIL_HOST_USER',
#                 ["oleg222200005555@gmail.com"],
#                 fail_silently=False
#             )
#         except BadHeaderError:
#             return HttpResponseRedirect(reverse("main:index"))
        
#         return HttpResponseRedirect(reverse("main:index"))


#     context = {
#         'title': 'Contact',
#     }
#     return render(request, 'feedback/contact_form.html', context)
