import uuid

from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.utils import timezone

from apps.mailer.mailer import send_mail


class BaseOTC(models.Model):
    """ Base class for OTC """
    code = models.UUIDField(
        verbose_name="code",
        default=uuid.uuid4
    )
    created_on = models.DateTimeField(
        verbose_name="created on",
        auto_now_add=True
    )
    applied_on = models.DateTimeField(
        verbose_name="applied on",
        null=True, blank=True
    )

    class Meta:
        abstract = True

    def apply(self):
        self.applied_on = timezone.now()
        self.save()

    @property
    def is_applied(self):
        return self.applied_on is not None

    @property
    def is_expired(self):
        expiration_date = timezone.now() - timezone.timedelta(days=settings.OTC_TTL_DAYS)
        return expiration_date > self.created_on

    def after_create(self):
        raise NotImplemented(
            "'after_create' method should be implemented in BaseOTC-derived classes"
        )

    def after_apply(self):
        raise NotImplemented(
            "'after_apply' method should be implemented in BaseOTC-derived classes"
        )

    def save(self, *args, **kwargs):
        created = self.pk is None
        prev = self.__class__.objects.get(pk=self.pk) if not created else None

        super().save(*args, **kwargs)

        if created:
            self.after_create()

        if self.is_applied and prev and not getattr(prev, 'applied_on'):
            self.after_apply()


class PasswordResetOTC(BaseOTC):
    """ Password reset OTC model """

    user = models.ForeignKey(
        verbose_name="user",
        to=User, related_name='password_reset_otcs',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "password reset OTC"
        verbose_name_plural = "password reset OTCs"
        ordering = ['user', '-id']

    def after_create(self):
        #TODO: add send email
        pass

    def after_apply(self):
        #TODO: add send email
        pass
