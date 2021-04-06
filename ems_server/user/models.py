from django.db import models


# Create your models here.


class Admin(models.Model):
    gender_choices = (
        (0, "male"),
        (1, "female"),
    )

    name = models.CharField(max_length=30)
    real_name = models.CharField(max_length=30, verbose_name="真实姓名")
    password = models.CharField(max_length=64)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)
    register = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "bz_admin"
        verbose_name = "管理员"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
