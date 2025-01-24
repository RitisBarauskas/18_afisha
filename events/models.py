from django.db.models import (
    Model,
    CharField,
    IntegerField,
    TextField,
    ForeignKey,
    CASCADE,
    DateTimeField,
    SlugField,
    ManyToManyField,
)

from events.constants import MAX_LENGTH_CHAR_FIELD


class City(Model):
    name = CharField(verbose_name='Название города', max_length=MAX_LENGTH_CHAR_FIELD)
    population = IntegerField(verbose_name='Население')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ('-population',)

    def __str__(self):
        return self.name


class Place(Model):
    name = CharField(verbose_name='Название места', max_length=MAX_LENGTH_CHAR_FIELD)
    city = ForeignKey(City, verbose_name='Город', on_delete=CASCADE, related_name='places')
    capacity = IntegerField(verbose_name='Вместимость')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ('-capacity',)

    def __str__(self):
        return self.name


class Event(Model):
    title = CharField(verbose_name='Название события', max_length=MAX_LENGTH_CHAR_FIELD)
    description = TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ('-id',)

    def __str__(self):
        return self.title


class Tag(Model):
    name = CharField(verbose_name='Название тега', max_length=MAX_LENGTH_CHAR_FIELD)
    slug = SlugField(verbose_name='Слаг', unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('name',)

    def __str__(self):
        return self.name


class EventPlace(Model):
    event = ForeignKey(Event, verbose_name='Событие', on_delete=CASCADE, related_name='event_places')
    place = ForeignKey(Place, verbose_name='Место', on_delete=CASCADE, related_name='event_places')
    tags = ManyToManyField(Tag, verbose_name='Теги', related_name='event_places')
    event_date = DateTimeField(verbose_name='Дата события', null=False, blank=False)

    class Meta:
        verbose_name = 'Место события'
        verbose_name_plural = 'Места событий'
        ordering = ('event_date',)

    def __str__(self):
        return f'{self.event.title} - {self.place.name}'
