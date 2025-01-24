from datetime import datetime

from django.shortcuts import render, HttpResponse, get_object_or_404

from events.constants import MAX_ITEMS_ON_MAIN_PAGE
from events.models import City, EventPlace, Event


def index(request):
    nearest_events = EventPlace.objects.filter(
        event_date__gte=datetime.now()
    ).select_related(
        'place__city',
        'event',
    )[:MAX_ITEMS_ON_MAIN_PAGE]

    last_events = EventPlace.objects.filter(
        event_date__lt=datetime.now()
    ).select_related(
        'place__city',
        'event',
    )[:MAX_ITEMS_ON_MAIN_PAGE]

    return render(
        request,
        'events/index.html',
        {
            'nearest_events': nearest_events,
            'last_events': last_events,
        },
    )


def cities(request):
    city_list = City.objects.all()

    return render(request, 'events/cities.html', context={'cities': city_list})


def places_by_city(request, city_id):
    city = get_object_or_404(City, id=city_id)
    places = city.places.all()

    return render(
        request,
        'events/places.html',
        {'places': places, 'city_name': city.name},
    )


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    return render(request, 'events/event_detail.html', {'event': event})
