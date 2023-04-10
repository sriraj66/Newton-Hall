from django.db import models
from django.contrib.auth.models import User

STATUS = (
    ("WAITING","WAITING"),
    ("APPROVED","APPROVED")
)

class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    f_date = models.DateTimeField()
    e_date = models.DateTimeField()

    is_booked = models.PositiveIntegerField(choices=STATUS,default=0)

    timestramp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.user} for {self.reason}"
    
    class Meta:
        ordering = ["-timestramp"]