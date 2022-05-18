from django import template
from covidapp.models import Availability

register = template.Library()

@register.simple_tag
def get_table_class(value):
    if value:
        return 'bg-success text-light'
    return 'bg-danger text-light'

@register.simple_tag
def get_availibilities(hospital):
    return Availability.objects.filter(hospital=hospital).order_by('facility_id')


@register.simple_tag
def is_option_selected(selected_option, pk):
    if selected_option == str(pk):
        return 'selected'
    else:
        return ''

# @register.simple_tag
# def isCitySelected(selected_city, pk):
#     if selected_city == str(pk):
#         return 'selected'
#     else:
#         return ''