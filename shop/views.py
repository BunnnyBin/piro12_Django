from django.http import HttpResponse
from django.shortcuts import render

from shop.models import Item


def archives_year(request, year):
    return HttpResponse(f'{year}년도에 대한 내용')

def item_list(request):
    qs = Item.objects.all()

    q = request.GET.get('q','')  # 검색 단어
    if q:
        qs = qs.filter(name__icontains=q)

    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'q': q  # 검색단어 남게하기
    })
