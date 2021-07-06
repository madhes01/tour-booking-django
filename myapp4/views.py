from django.shortcuts import render
from .models import Destination


def index (request):

    dest1 = Destination()
    dest1.name = 'France'
    dest1.img = 'im-1.jpg'

    dest2 = Destination()
    dest2.name = 'London'
    dest2.img = 'im-2.jpg'

    dest3 = Destination()
    dest3.name = 'Paris'
    dest3.img = 'im-3.jpg'

    dest4 = Destination()
    dest4.name = 'Washington'
    dest4.img = 'im-4.jpg'

    dests = [dest1, dest2, dest3, dest4]

    return render(request, "index.html", {'dests':dests})
