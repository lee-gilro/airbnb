from django.db import models
from common.models import CommonModel
# Create your models here.
class Room(CommonModel):
    """ Room Model definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("Shared_room", "Shared Room")

    name = models.CharField(max_length=180, default="")
    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    price = models.PositiveBigIntegerField()
    rooms = models.PositiveBigIntegerField()
    toilets = models.PositiveBigIntegerField()
    description = models.TextField(max_length= 250)
    pet_friendly = models.BooleanField(default=True,)
    kind = models.CharField(max_length=20, choices=RoomKindChoices.choices,)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="rooms",)
    amenities = models.ManyToManyField("rooms.Amenity", related_name= "rooms",)
    category = models.ForeignKey("categories.Category", on_delete= models.SET_NULL, blank=True, null=True, related_name= "rooms",)

    def __str__(self) -> str:
        return self.name
    
    def total_amenities(self):
        return self.amenity.count()

    def rating(self):
        count =  (self.reviews.count())

        if count == 0:
            return "No reviews"
        
        else:
            total_rating = 0
            for review in self.reviews.all().values("rating"):
                total_rating = total_rating + review["rating"]
            return round(total_rating/count,2)

            
class Amenity(CommonModel):
    """Amenity definition"""

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, null= True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"