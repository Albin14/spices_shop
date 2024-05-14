from django import template

register = template.Library()


@register.simple_tag(name='get_total')
def get_total(cart):

    total = 0

    for item in cart.cart_items.all():
        total += item.count * item.product.price
    return total
