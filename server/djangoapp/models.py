from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='Toyota')
    description = models.CharField(null=False, max_length=30, default='SUV')
    dob = models.DateField(null=False)

    def __str__(self):
        return self.name + " " + self.description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:

class CarModel(models.Model):
    new = models.BooleanField(default=True)
    # number_of_doors = models.ForeignKey()
    dealer_id = models.IntegerField()
    car_make = models.ManyToManyField(CarMake)

    def __str__(self):
        return "Name of car brand:" + self.name + ", vehicle type " + \
               + self.description + " is brand" + str(self.new) + \
               " bought by " + self.dealer_id

# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
