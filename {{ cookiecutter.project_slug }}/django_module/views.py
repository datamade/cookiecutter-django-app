import os

from django.shortcuts import render
from django.views.generic import TemplateView

{% if not cookiecutter.install_wagtail %}
class Home(TemplateView):
    template_name = "{{ cookiecutter.module_name }}/home_page.html"
{% endif %}

def robots_txt(request):
    return render(
        request,
        "{{ cookiecutter.module_name }}/robots.txt",
        {"ALLOW_CRAWL": True if os.getenv("ALLOW_CRAWL") == "True" else False},
        content_type="text/plain",
    )


def page_not_found(request, exception, template_name="noah_map/404.html"):
    return render(request, template_name, status=404)


def server_error(request, template_name="noah_map/500.html"):
    return render(request, template_name, status=500)
