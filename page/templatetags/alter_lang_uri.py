from django import template

register = template.Library()

@register.simple_tag
def alter_lang_uri(request, lang):
    url = request.get_full_path()
    new_url = "/" + lang + url[3:]
    new_uri = request.build_absolute_uri(new_url)
    return new_uri
