from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.postgres.fields import JSONField, ArrayField
from simple_history.models import HistoricalRecords


def access_default_dict():
    return {
        'authentication': None,
        'complexity': None,
        'vector': None
    }


def impact_default_dict():
    return {
        'availability': None,
        'confidentiality': None,
        'integrity': None
    }

#
# class Product(models.Model):
#     name = models.CharField(max_length=250, null=True)
#
#
# class Vendor(models.Model):
#     name = models.CharField(max_length=250, null=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)


class CPE(models.Model):
    title = models.TextField(default="")
    vendor = models.CharField(max_length=250, default="", null=True)
    product = models.CharField(max_length=250, default="", null=True)
    vector = models.CharField(max_length=250, default="", null=True)
    vulnerable_products = ArrayField(
        models.CharField(max_length=250, blank=True), null=True)

    class Meta:
        db_table = "cpe"

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class CWE(models.Model):
    cwe_id = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=250, null=True)
    description = models.TextField(default="")

    class Meta:
        db_table = "cwe"

    def __unicode__(self):
        return self.cwe_id

    def __str__(self):
        return self.cwe_id


class CVE(models.Model):
    cve_id = models.CharField(max_length=20, null=True)
    summary = models.TextField(default="")
    published = models.DateTimeField(null=True)
    modified = models.DateTimeField(null=True)
    assigner = models.CharField(max_length=50, null=True)
    cvss = models.FloatField(default=0.0, null=True)
    cvss_time = models.DateTimeField(null=True)
    cvss_vector = models.CharField(max_length=250, null=True)
    cwe = models.ForeignKey(CWE, on_delete=models.CASCADE, null=True)
    access = JSONField(default=access_default_dict)
    impact = JSONField(default=impact_default_dict)
    vulnerable_products = ArrayField(
        models.CharField(max_length=10, blank=True), null=True)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True)
    history = HistoricalRecords()

    class Meta:
        db_table = "cve"

    def __unicode__(self):
        return self.cve_id

    def __str__(self):
        return self.cve_id

    def save(self, *args, **kwargs):
        # Todo
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(CVE, self).save(*args, **kwargs)
