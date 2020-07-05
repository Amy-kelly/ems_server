from django.db import models

# Create your models here.
class User(models.Model):
    gender_choices = (
        (0,'female'),
        (1,'male'),
    )
    username = models.CharField(max_length=32)
    real_name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    gender = models.SmallIntegerField(choices=gender_choices,default=1)
    status = models.SmallIntegerField(default=False)
    register_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "ems_user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class Employee(models.Model):
    emp_name = models.CharField(max_length=32)
    img = models.ImageField(upload_to="pic",default="pic/1.jpg")
    salary = models.DecimalField(max_digits=8,decimal_places=2)
    age = models.IntegerField()
    is_delete = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "ems_employee"
        verbose_name = "员工"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.emp_name

    @property
    def age_change(self):
        if self.age < 18:
            return str(self.age) + "(未成年)"
        elif 18 <= self.age <40:
            return str(self.age) + "(青年)"
        else:
            return str(self.age) + "(中年)"

