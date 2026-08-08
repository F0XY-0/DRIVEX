from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=20 ,decimal_places=2)
    mileage = models.PositiveIntegerField()
    fuel = models.CharField(max_length=100)
    transmission = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    horsepower = models.PositiveIntegerField()
    description = models.TextField()
    cover_image = models.ImageField(upload_to="cars/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model}"