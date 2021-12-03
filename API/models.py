from django.db import models
from django.contrib.auth.models import User


class Target(models.Model):
    target_id = models.AutoField(primary_key=True)
    target_url = models.URLField(max_length=200, blank=False)


class ScanResult(models.Model):
    scan_result_id = models.AutoField(primary_key=True)
    scan_result_file = models.FileField(upload_to='uploads/', blank=False, unique=True)


class Category(models.Model):
    CATEGORY_TYPES = [
        ('ENUM', 'Enumeration'),
        ('AR', 'ActiveRecon'),
        ('PR', 'PassiveRecon')
    ]

    category_id = models.AutoField(primary_key=True)
    category_description = models.CharField(max_length=500, blank=False)
    category_type = models.CharField(max_length=4, choices=CATEGORY_TYPES, blank=False)


class PentestTool(models.Model):
    PENTEST_TOOLS = [
        ('sherlock', 'sherlock'),
         ('nmap', 'nmap'),
        ('gobuster', 'gobuster')
    ]
    pentest_tool_id = models.AutoField(primary_key=True)
    pentest_tool_name = models.CharField(max_length=30, blank=False, choices=PENTEST_TOOLS)
    pentest_tool_version = models.CharField(max_length=10, blank=False)
    pentest_tool_description = models.CharField(max_length=500, blank=False)
    categories = models.ManyToManyField(Category, blank=False)


class Scan(models.Model):
    scan_id = models.AutoField(primary_key=True)
    scan_start_date = models.DateTimeField(auto_now_add=True, blank=False)
    scan_end_date = models.DateTimeField(auto_now_add=True, blank=False)

    scan_result = models.OneToOneField(ScanResult,  on_delete=models.CASCADE, blank=False)
    pentest_tool = models.OneToOneField(PentestTool, on_delete=models.CASCADE, blank=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    target = models.ForeignKey(Target, on_delete=models.CASCADE, blank=False)


