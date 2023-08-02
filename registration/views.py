#from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, EventSerializer

from .models import User, Event


# Create your views here.

# class RegistrationViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

@api_view(['GET'])
def get_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register_user(request):
    # Implement the user registration logic here, including captcha verification
    # For brevity, let's assume you receive user data from the request payload

    # Deserialize the user data
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        user = user_serializer.save()

        # Get the selected events from the request data (assuming it's in the format {"events": [1, 2, 3]})
        selected_event_ids = request.data.get('events', None)
        if selected_event_ids:
            try:
                # Fetch the selected events from the database
                selected_events = Event.objects.filter(pk__in=selected_event_ids)
                # Associate the selected events with the user
                user.events.set(selected_events)
            except Event.DoesNotExist:
                # Handle the case when the selected event IDs are not valid
                # You can raise an error or return an appropriate response
                pass

        # Return a successful response with the user data
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)

    # Return error response for invalid user data
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)