import logging
import re
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, render
from shop.models import Item
from .forms import ItemForm


def archives_year(request, year):
    return HttpResponse(f'{year}년도에 대한 내용')


def item_list(request):
    qs = Item.objects.all()

    q = request.GET.get('q', '')  # 검색 단어
    if q:
        qs = qs.filter(name__icontains=q)

    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'q': q  # 검색단어 남게하기
    })


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item': item,
    })


# django form
def item_new(request, item=None):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect(item)
    else:
        form = ItemForm(instance=item)
    return render(request, 'shop/item_form.html', {
        'form': form,
    })


def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return item_new(request, item)
