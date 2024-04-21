from django import template
from menu.models import MenuItem
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path
    root_menu_items = MenuItem.objects.filter(parent=None)

    def render_menu(menu_items):
        result = ''
        for item in menu_items:
            if current_path == item.url:
                active_class = 'active'
            else:
                active_class = ''
            result += (
                f'<li class="{active_class}">'
                f'<a href="{item.url}">{item.name}</a>'
            )
            children = item.children.all()

            if children.exists():
                result += '<ul>'
                result += render_menu(children)
                result += '</ul>'

            result += '</li>'

        return result

    if root_menu_items:
        menu_html = render_menu(root_menu_items)
        return mark_safe(menu_html)

    return mark_safe('No menu items')
