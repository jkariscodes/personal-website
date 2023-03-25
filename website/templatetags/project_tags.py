from django import template
from ..models import PortfolioProjects

register = template.Library()


@register.inclusion_tag("website/all_projects.html")
def all_projects():
    projects = PortfolioProjects.objects.all().order_by("title")
    return {"all_projects": projects}
