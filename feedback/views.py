from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room

def feedback(request, event_id):
    """Feedback page to receive feedback using WebSockets."""
    # Get a list of rooms, ordered alphabetically
    rooms = Room.objects.order_by("title")

    # Render that in the index template
    return render(request, "index.html", {
        "rooms": rooms,
    })
