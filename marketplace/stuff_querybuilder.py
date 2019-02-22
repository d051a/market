import datetime
from django.db.models import Q
from marketplace.models import Stuff


class StuffQueryBuilder:
    def __init__(self, params=None):
        self.params = self._clean_params(params or {})
        self.query = Stuff.objects.all()
        self._process()

    def _process(self):
        for key, value in self.params.items():
            if not value:
                continue
            method = f'_filter_{key}'
            getattr(self, method, lambda _: None)(value)

    def _clean_params(self, params):
        filters = filter(lambda _method: _method.startswith('_filter_'), dir(self))
        fields = list(map(lambda field: field.replace('_filter_', ''), filters))
        return {key: value for key, value in params.items() if value and key in fields}

    def _filter_text(self, text):
        q = Q(title__icontains=text) | Q(description__icontains=text)
        self.query = self.query.filter(q)

    def _filter_city(self, city_id):
        self.query = self.query.filter(city_id=city_id)

    def _filter_stuff_subcategory(self, category_id):
        self.query = self.query.filter(stuff_subcategory_id=category_id)

    def _filter_data_start(self, date_from):
        date_from = datetime.datetime.strptime(date_from, '%m/%d/%Y')
        self.query = self.query.filter(date__gte=date_from)

    def _filter_data_finish(self, date_to):
        date_to = datetime.datetime.strptime(date_to, '%m/%d/%Y')
        self.query = self.query.filter(date__lt=date_to)

    def _filter_price_start(self, price):
        if not price.isdigit:
            return
        self.query = self.query.filter(price__gte=price)

    def _filter_price_finish(self, price):
        if not price.isdigit():
            return
        self.query = self.query.filter(price__lt=price)

    def _filter_tags(self, tags):
        tags = map(str.strip, tags.split(','))
        tags = filter(bool, tags)
        self.query = self.query.filter(tags__name__in=tags)
