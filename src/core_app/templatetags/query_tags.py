from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def query_tags(context, remove=None, **kwargs):
    request = context['request']
    params = request.GET.copy()

    if remove:
        for key in remove.split(','):
            params.pop(key, None)

    for k, v in kwargs.items():
        params[k] = v

    return params.urlencode()