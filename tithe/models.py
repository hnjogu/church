# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.signals import setting_changed
from django.dispatch import receiver
from django.db import models

# Create your models here.
class offering(models.Model):
 	member_code = models.ForeignKey(settings.AUTH_USER_MODEL)
	member = models.CharField(max_length=45)
	receipt_code = models.CharField(max_length=45, unique=True)
	tithes = models.IntegerField()
	combinedoffering = models.IntegerField()
	campmeetingoffering = models.IntegerField()
	churchbuilding = models.IntegerField()
	conference = models.IntegerField()
	localchurch = models.IntegerField()
	funds = models.IntegerField()
	total = models.IntegerField()
	created_date = models.DateTimeField(
		    default=timezone.now)
	published_date = models.DateTimeField(
		    blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.receitcode

	class Meta:
		abstract = True
		unique_together = ["receipt_code"]
