from django.shortcuts import render
from django.urls import resolve
from .models import MenuItem


def draw_menu(request, menu_name):
    current_url = request.path_info
    current_url_name = resolve(request.path_info).url_name
    menu_items = MenuItem.objects.filter(menu_name=menu_name)
    context = {'menu_items': menu_items, 'current_url': current_url, 'current_url_name': current_url_name}
    return render(request, 'menu/menu.html', context)


def my_page(request, menu_name):
    return render(request, 'page.html', {'menu_name': menu_name})
