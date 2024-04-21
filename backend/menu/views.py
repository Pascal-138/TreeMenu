from django.shortcuts import render

from .models import MenuItem


def draw_menu(request, menu_name):
    menu_items = (
        MenuItem.objects
        .filter(name=menu_name)
        .select_related('parent')
    )
    context = {
        'menu_items': menu_items
    }

    return render(request, 'menu/base.html', context=context)
