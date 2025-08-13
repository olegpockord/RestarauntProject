from django.shortcuts import render
from django.views.generic import TemplateView


<<<<<<< HEAD
# классовое представление

=======
# Class View
# @method_decorator(cache_page(60*3), name='dispatch') dont work in Docker Container
>>>>>>> main
class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context

# View function
# def index(request):
#     context = {
#         'title': 'Home',
#     }

    

#     return render(request, 'main/index.html', context)