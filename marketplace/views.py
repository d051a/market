from django.views.generic import ListView
from .models import Stuff
from django.shortcuts import redirect
from .forms import SearchForm
from .filters import StuffFilter


def main_redirect(request):
	return redirect('/market', tag='bar')

class StuffList(ListView):
	context_object_name = 'stuff_list'
	queryset = Stuff.tags.all()
	template_name = 'marketplace/stuff_list.html'
	paginate_by = 25

	def get_queryset(self):
		stuff_list = Stuff.objects.all()
		try:
			stuff_list = stuff_list.filter(tags__name = self.request.GET["tag"])
		except KeyError:
			pass
		return stuff_list

	def get_context_data(self, **kwargs):
		context =  super(StuffList,self).get_context_data(**kwargs)
		context['filter'] = StuffFilter(self.request.GET, queryset=self.get_queryset())
		context['form'] = SearchForm()
		return context