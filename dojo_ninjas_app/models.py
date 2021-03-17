from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    desc = models.CharField(max_length=45, null=True)
    # related name of students is how the dojo sees the people inside
    def __repr__(self):
        return f"Dojo | {self.name} | {self.city} | {self.state} | {self.desc}"
class Ninja(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dojo = models.ForeignKey('Dojo', related_name = 'students', on_delete = models.CASCADE)
    def __repr__(self):
        return f"\n Ninja | {self.first_name} | {self.last_name} | {self.dojo.name}"
