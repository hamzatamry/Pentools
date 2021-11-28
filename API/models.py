from django.db import models


class Scan(models.Model):
    pass


class ScanResult(models.Model):
    pass


class Target(models.Model):
    pass


class PentestTool(models.Model):
    pass


class Category(models.Model):
    pass


class EnumerationCategory(Category):
    pass


class ActiveReconCategory(Category):
    pass


class PassiveReconCategory(Category):
    pass
