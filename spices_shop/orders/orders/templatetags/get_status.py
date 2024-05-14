from django import template

register = template.Library()


@register.simple_tag(name='get_status')
def get_status(status):
    status=status-1

    status_arr=['confirmed','processed','dispatched','delivered','cancelled']
    return status_arr[status]
