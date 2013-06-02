__author__ = 'norad'

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

from common.decorators import accepts, render_to
from trails.models import Trail

from trails.forms import TrailSearchForm


@render_to('map/example.html')
def example(request):
    return {}


@accepts('GET')
@login_required
@render_to('trails/create_edit.html')
def create(request):
    return {
        'trail': Trail(creator=request.user),
    }


@accepts('GET', 'POST')
@login_required
@render_to('trails/create_edit.html')
def edit(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)

    if not trail.edit_permitted(request.user.profile):
        return HttpResponseForbidden()

    elif request.method == 'GET':
        return {
            'trail': trail
        }

    elif request.method == 'POST':
        # TODO add form and populate trail model
        return {
            'trail': trail
        }


@accepts('GET')
@render_to('map/view.html')
def view(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)

    return {
        'trail': trail
    }


@accepts('GET')
@render_to('map/search.html')
def search(request):
    if len(request.GET > 0):
        form = TrailSearchForm(request.GET)
    else:
        form = TrailSearchForm(initial={
            'tags': [],
            'created': -7,
            'location': request.user.preferences.location,
            'distance': 10
        })

    response = {
        'form': form,
    }

    if form.is_valid():
        response['results'] = filter_trails(form)


def filter_trails(form):
    pass