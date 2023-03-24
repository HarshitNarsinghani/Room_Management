
from .models import Building,Room,RoomType,BlockedDay
from Test.models import Room
from Test.serializers import RoomSerializer

from django.db.models import  Min
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Test.models import Room, Building
from Test.serializers import RoomSerializer

from rest_framework import status
from .models import Room
from .serializers import RoomSerializer

# Create your views here.
@api_view(['GET'])
def available_rooms(request):
    building_name = request.GET.get('building')
    checkin_date = request.GET.get('check_in')
    checkout_date = request.GET.get('check_out')
    
    # Add debug statement to print the values of the query parameters
   # print("Building name: ", building_name)
    #print("Checkin date: ", checkin_date)
  #  print("Checkout date: ", checkout_date)

    try:
        # Query the database to retrieve all available rooms of the specified building that are available in the given date range.
        building = Building.objects.get(name = building_name)
        room_type = RoomType.objects.get(building=building)
        rooms = Room.objects.filter(
            room_type=room_type,
        ).annotate(
            min_price=Min('price')
        ).order_by('price')

        # Serialize the resulting data into a format that can be returned as an HTTP response.
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Building.DoesNotExist:
        # Add debug statement to print the error message
       # print("Building matching query does not exist")
        return Response(status=status.HTTP_404_NOT_FOUND)


