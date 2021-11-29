from django.db import models


class Scan(models.Model):
    scan_id = models.AutoField(primary_key=True)
    scan_start_date = models.DateTimeField(auto_now_add=True)
    scan_end_date = models.DateTimeField(auto_now_add=True)


class ScanResult(models.Model):
    scan_result_id = models.AutoField(primary_key=True)
    scan_result_file = models.FileField(upload_to='uploads/', default='')


class Target(models.Model):
    target_id = models.AutoField(primary_key=True)
    target_url = models.URLField(max_length=200, default='')


class PentestTool(models.Model):
    pentest_tool_id = models.AutoField(primary_key=True)
    pentest_tool_name = models.CharField(max_length=30, blank=False)
    pentest_tool_version = models.CharField(max_length=10, blank=True)
    pentest_tool_description = models.CharField(max_length=500)


class EnumerationCategory(models.Model):
    enumeration_category_id = models.AutoField(primary_key=True)
    enumeration_category_description = models.CharField(max_length=200)


class ActiveReconCategory(models.Model):
    active_recon_category_id = models.AutoField(primary_key=True)
    active_recon_category_description = models.CharField(max_length=200)


class PassiveReconCategory(models.Model):
    passive_recon_category_id = models.AutoField(primary_key=True)
    passive_recon_category_description = models.CharField(max_length=200)