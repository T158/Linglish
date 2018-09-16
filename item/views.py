from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse, HttpResponse
from django.views.decorators.http import require_POST

from .models import Item, WishList


def index(request):
    # item一覧を取得し、辞書に格納
    context = {'items': Item.objects.all()}
    return TemplateResponse(request, 'item/list.html', context=context)