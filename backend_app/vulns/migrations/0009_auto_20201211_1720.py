# Generated by Django 3.0.10 on 2020-12-11 17:20

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulns', '0008_auto_20201022_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalvuln',
            name='cvss3',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='historicalvuln',
            name='cvss3_metrics',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='historicalvuln',
            name='cvss3_vector',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='historicalvuln',
            name='cvss3_version',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='historicalvuln',
            name='cvss_metrics',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='historicalvuln',
            name='cvss_version',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='vuln',
            name='cvss3',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='vuln',
            name='cvss3_metrics',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='vuln',
            name='cvss3_vector',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='vuln',
            name='cvss3_version',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='vuln',
            name='cvss_metrics',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='vuln',
            name='cvss_version',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
