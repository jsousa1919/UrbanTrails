__author__ = 'norad'

from functools import wraps

from django.http import HttpResponseNotAllowed
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.decorators import available_attrs


def render_to(template):
    """
Decorator for Django views that sends returned dict to render_to_response function
with given template and RequestContext as context instance.

If view doesn't return dict then decorator simply returns output.
Additionally view can return two-tuple, which must contain dict as first
element and string with template name as second. This string will
override template name, given as parameter

Parameters:

- template: template name to use
"""
    def renderer(view_func):
        def wrapper(request, *args, **kwargs):
            output = view_func(request, *args, **kwargs)

            if isinstance(output, (list, tuple)):
                output = render_to_response(output[1], output[0], RequestContext(request))
            elif isinstance(output, dict):
                output = render_to_response(template, output, RequestContext(request))

            return output
        return wraps(view_func, assigned=available_attrs(view_func))(wrapper)
    return renderer


def accepts(*methods):
    """
    Decorator for view that only accepts certain html methods
    """
    def renderer(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.method in methods:
                return HttpResponseNotAllowed(methods)

            return view_func(request, *args, **kwargs)
        return wraps(view_func, assigned=available_attrs(view_func))(wrapper)
    return renderer