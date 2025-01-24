from django.contrib import admin

from events.models import Event, Place, City, Tag, EventPlace


class EventPlaceInline(admin.TabularInline):
    model = EventPlace
    extra = 1


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [EventPlaceInline]
    list_display = ('title', 'description')
    search_fields = ('title', 'description')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'capacity')
    search_fields = ('name', 'city__name')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'population')
    search_fields = ('name', 'population')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(EventPlace)
class EventPlaceAdmin(admin.ModelAdmin):
    list_display = ('event', 'place', 'event_date')
    search_fields = ('event__title', 'place__name')