from django import template
from accounts.choices import BOARD_CHOICES

register = template.Library()

@register.filter
def get_board_name(value):
    return dict(BOARD_CHOICES)[value]