from django.db import models
from django.contrib.auth.models import User


class RegistrationTry(models.Model):
    user = models.ForeignKey(
        verbose_name="user",
        to=User, related_name='registration_try',
        on_delete=models.CASCADE
    )
    extra_data = models.Text(
        verbose_name="extra_data"
    )

