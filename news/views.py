from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import TemplateView, DetailView


from news.models import Event, NewsCategory





class NewsPageView(TemplateView):
    template_name = 'news/events.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Events'
        context['news'] = Event.objects.all()
        context['news_category'] = NewsCategory.objects.all()
        return context



class NewsInfoView(DetailView):
    template_name = 'news/news_details.html'
    slug_url_kwarg = 'news_slug'
    context_object_name = 'events'

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        news = Event.objects.get(slug = self.kwargs.get(self.slug_url_kwarg))
        return news
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context
        

# def news_page(request):

#     news = Event.objects.all()
#     news_category = NewsCategory.objects.all()

#     context = {
#         'title': 'Events',
#         'news': news,
#         'news_category': news_category,
#     }

#     return render(request, 'news/events.html', context)

# def news_info(request, news_slug=False):

#     news = Event.objects.get(slug = news_slug)

#     context = {
#         'title': 'Event',
#         'events': news,
#     }

#     return render(request, 'news/news_details.html', context)