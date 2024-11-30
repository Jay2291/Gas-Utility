# Generated by Django 5.1.3 on 2024-11-30 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicerequest',
            old_name='description',
            new_name='details',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='request_type',
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='attachments',
            field=models.FileField(blank=True, null=True, upload_to='attachments/'),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='service_type',
            field=models.CharField(choices=[('install', 'Install'), ('repair', 'Repair'), ('maintenance', 'Maintenance')], max_length=50),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]