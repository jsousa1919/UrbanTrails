__author__ = 'norad'

from common.decorators import render_to


@render_to('map/example.html')
def example(request):
    return {}