from django.db import models


class Code(models.Model):
    name = models.CharField(max_length=20, blank=False, unique=True)
    repo = models.CharField(max_length=50, blank=False, unique=True)


class Domain(models.Model):
    name = models.CharField(max_length=50, blank=True, unique=True)


class Application(models.Model):
    name = models.CharField(max_length=50, blank=False)
    code = models.ForeignKey(Code)
    domain = models.ForeignKey(Domain)
    context = models.CharField(max_length=20, help_text="Default is '/'")
