import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView
from django.views.decorators.csrf import csrf_exempt

from ads.models import Ad, Category


def index(request):
    return JsonResponse({"status": "ok"})


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
        ads = Ad.objects.all()

        result = []
        for ad in ads:
            result.append({
              "id": ad.Id,
              "name": ad.name,
              "author": ad.author,
              "price": ad.price,
              "description": ad.description,
              "address": ad.address,
              "is_published": ad.is_published
            })
        return JsonResponse(result, safe=False)

    def post(self, request):
        ad_data = json.loads(request.body)

        ad = Ad.objects.create(
            name=ad_data["name"],
            author=ad_data["author"],
            price=ad_data["price"],
            description=ad_data["description"],
            address=ad_data["address"],
            is_published=ad_data["is_published"],
        )

        return JsonResponse({
              "id": ad.Id,
              "name": ad.name,
              "author": ad.author,
              "price": ad.price,
              "description": ad.description,
              "address": ad.address,
              "is_published": ad.is_published
            })


class AdsDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()
        except Ad.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
              "id": ad.Id,
              "name": ad.name,
              "author": ad.author,
              "price": ad.price,
              "description": ad.description,
              "address": ad.address,
              "is_published": ad.is_published
            })


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()

        result = []
        for category in categories:
            result.append(
                {"id": category.id,
                "name": category.name})

        return JsonResponse(result, safe=False)

    def post(self, request):
        cat_data = json.loads(request.body)
        cat = Category.objects.create(name=cat_data["name"])
        return JsonResponse({"id": cat.id,
                             "name": cat.name})


class CategoriesDetaileView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            category = self.get_object()
        except Ad.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)
        return JsonResponse({
              "id": category.id,
              "name": category.name})