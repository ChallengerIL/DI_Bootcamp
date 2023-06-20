import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotel_torquay.settings")
import django
django.setup()
from visitors.models import Room
import random

ROOMS_TOTAL = 200

for i in range(1, ROOMS_TOTAL+1):
    # Room.objects.all().delete()
    # quit()
    room_type_name = random.choice(Room.RoomType.names)
    room_type = Room.RoomType[room_type_name]

    room = Room(
        room_type=room_type,
        price=int(room_type * 100),
        room_number=i,
    )
    room.save()
