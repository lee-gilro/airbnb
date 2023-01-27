from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from reviews.serializers import ReviewSerializer
from medias.serializers import PhotoSerializer
class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )
        

class RoomListSerializer(ModelSerializer):
    rating = SerializerMethodField()
    is_owner = SerializerMethodField()
    photos = PhotoSerializer(many = True, read_only = True)

    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_owner",
            "photos",
        )
        depth = 1

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return request.user == room.owner


class RoomDetailSerializer(ModelSerializer):
    
    owner = TinyUserSerializer(read_only = True)
    #amenities = AmenitySerializer(read_only = True, many = True)
    category = CategorySerializer(read_only = True)
    is_owner = SerializerMethodField()
    rating = SerializerMethodField()
    photos = PhotoSerializer(many = True, read_only = True)

    class Meta:
        model = Room
        exclude = ("amenities",)
    def get_rating(self, room):
        return room.rating()
        
    def get_is_owner(self, room):
        request = self.context["request"]
        return request.user == room.owner
