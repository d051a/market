from urllib import parse
from django.shortcuts import redirect
from django.views.generic import ListView
from marketplace.forms import SearchForm
from marketplace.models import Stuff
from marketplace.stuff_querybuilder import StuffQueryBuilder


def main_redirect(request):
    # tag='bar' - называется костыль
    return redirect('/market', tag='bar')


class StuffList(ListView):
    context_object_name = 'stuff_list'
    template_name = 'marketplace/stuff_list.html'
    paginate_by = 2

    def __init__(self, **kwargs):
        self.filter_params = {}
        super().__init__(**kwargs)

    def get_queryset(self):
        # try except придуман не для этого
        # stuff_list = Stuff.objects.all()
        # try:
        #     stuff_list = stuff_list.filter(tags__name=self.request.GET["tag"])
        # except KeyError:
        #     pass
        # return stuff_list
        params = dict(self.request.GET.items())
        if not params:
            return Stuff.objects.all()
        builder = StuffQueryBuilder(params)
        self.filter_params = builder.params
        return builder.query

    def get_context_data(self, **kwargs):
        # в python 3+ super можно вызывать без аргументов
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(initial=self.request.GET)
        context['filter_params'] = parse.urlencode(self.filter_params)
        return context
