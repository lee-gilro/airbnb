from django.db import models
from common.models import CommonModel
# Create your models here.


class Review(CommonModel):

    """Review from a User to a Room or Exp"""


    user = models.ForeignKey("users.User", on_delete = models.CASCADE)
    room = models.ForeignKey("rooms.Room", null= True, blank=True, on_delete= models.CASCADE)
    experiences = models.ForeignKey("experiences.Experience", on_delete= models.CASCADE , null= True, blank= True)
    payload = models.TextField()
    rating = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"{self.user} / {self.rating}"