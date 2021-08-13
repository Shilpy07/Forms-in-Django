from django.db import models


# class BaseModel(models.Model):
#     objects = models.Manager()
#
#     class Meta:
#         abstract = True


# Create your models here.
class CustomerRecord1(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    customer_id = models.IntegerField(null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Customer Records1'

    def __str__(self):
        return self.name


class CustomerRecord(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    customer_id = models.IntegerField(null=False, blank=False)
    items = models.ForeignKey(CustomerRecord1, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Customer Records'

    def __str__(self):
        return self.name


class StudentRecord(models.Model):
    CHOICES = (('None', 'None'),
               ('first', 'First'),
               ('second', 'Second'),
               ('third', 'Third'),
               ('forth', 'Forth')
               )
    name = models.CharField(max_length=255, blank=False, null=False, default='None')
    enrollment = models.IntegerField(blank=False, null=False, default=0)
    faculty = models.CharField(max_length=255, blank=False, null=False, default='None')
    year = models.CharField(max_length=255, blank=False, null=False, default='None', choices=CHOICES)
    register_date = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey(CustomerRecord, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Student Records'

# Create your models here.
