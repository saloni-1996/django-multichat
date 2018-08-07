from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from feedback.models import Room
from event.models import Event

def feedback(request, event_id):
    """Feedback page to receive feedback using WebSockets."""
    # Get a list of rooms, ordered alphabetically
    rooms = Room.objects.order_by("title")
    event = Event.objects.get(id=event_id)
    # Render that in the index template
    ctx_dict = {"rooms": rooms, "event":event}
    return render(request, "feedback/feedback.html", ctx_dict)
