from django.shortcuts import render, HttpResponse, Http404

from events.constants import DATABASE


def index(request):
    return HttpResponse('Hello, world!')


def cities(request):
    city_list = DATABASE.get('cities')

    return render(request, 'events/cities.html', context={'cities': city_list})


def places_by_city(request, city_id):
    city_name = next((city.get('name') for city in DATABASE.get('cities') if city.get('id') == city_id), None)
    if city_name is None:
        raise Http404()

    places = DATABASE.get('places')
    filtered_places = [place for place in places if place.get('city_id') == city_id]

    return render(
        request,
        'events/places.html',
        {'places': filtered_places, 'city_name': city_name},
    )
