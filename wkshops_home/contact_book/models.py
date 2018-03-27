from django.db import models

# Create your models here.

CONTACT_TYPES = (
    (1, "Personal"),
    (2, "Work")
)


class Address(models.Model):
    city = models.CharField(max_length=40)
    street = models.IntegerField(max_length=10)
    house_number = models.IntegerField(max_length=10)
    app_number = models.IntegerField(max_length=10)


class Person(models.Model):
    first_name = models.CharField(max_length = 64)
    last_name = models.CharField(max_length=62)
    description = models.TextField(max_length=200)
    address = models.ForeignKey(Address, on_delete=None, null=True)

    @property
    def name(self):
        return "{} {}" .format(self.first_name, self.last_name)

    def __str__(self):
        return self.name



class Mail(models.Model):
    mail_address = models.EmailField(max_length=100)
    type = models.IntegerField(choices=CONTACT_TYPES)
    contact_person = models.ForeignKey(Person, on_delete=None)


class Phone(models.Model):
    number = models.IntegerField(max_length=20)
    type = models.IntegerField(choices= CONTACT_TYPES)
    contact_person = models.ForeignKey(Person, on_delete=None)



class ContactGroup(models.Model):
    name = models.CharField(max_length=64)
    persons = models.ManyToManyField(Person)



