from typing import Any
from django.views.generic import TemplateView


from products.models import Categories, Meals


class MenuView(TemplateView):
    template_name = 'products/menu.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Menu'
        context['products'] = Meals.objects.all()
        context['categories'] = Categories.objects.all()
        return context


# def menu(request):
#     products = Meals.objects.all()
#     categories = Categories.objects.all()

#     context = {
#         'title': 'Menu',
#         'products': products,
#         'categories': categories,

#     }
#     return render(request, 'products/menu.html', context)