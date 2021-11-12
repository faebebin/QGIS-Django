# Generated by Django 2.2.24 on 2021-11-11 20:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LayerDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True, help_text='The upload date. Automatically added on file upload.', verbose_name='Uploaded on')),
                ('modified_date', models.DateTimeField(editable=False, help_text='The upload date. Automatically added on file upload.', verbose_name='Modified on')),
                ('name', models.CharField(help_text='A unique name for this resource', max_length=256, unique=True, verbose_name='Name')),
                ('description', models.TextField(help_text='A description of this resource.', max_length=5000, verbose_name='Description')),
                ('download_count', models.IntegerField(default=0, editable=False, help_text='The number of times this resource has been downloaded. This is updated automatically.', verbose_name='Downloads')),
                ('approved', models.BooleanField(db_index=True, default=False, help_text='Set to True if you wish to approve this resource.', verbose_name='Approved')),
                ('require_action', models.BooleanField(db_index=True, default=False, help_text='Set to True if you require creator to update the resource.', verbose_name='Requires Action')),
                ('file', models.FileField(help_text='A Layer Definition file. The filesize must less than 1MB', upload_to='layerdefinitions', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['qlr'])], verbose_name='Layer Definition file')),
                ('thumbnail_image', models.ImageField(help_text='Please upload an image that demonstrate this resource.', upload_to='layerdefinitions', verbose_name='Thumbnail')),
                ('url_datasource', models.URLField(blank=True, null=True, verbose_name='URL Data Source')),
                ('provider', models.TextField(max_length=5000, verbose_name='Provider')),
                ('creator', models.ForeignKey(help_text='The user who uploaded this resource.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateTimeField(auto_now_add=True, help_text='The review date. Automatically added on review resource.', verbose_name='Reviewed on')),
                ('comment', models.TextField(blank=True, help_text='A review comment. Please write your review.', max_length=1000, null=True, verbose_name='Comment')),
                ('resource', models.ForeignKey(help_text='The reviewed Layer Definition', on_delete=django.db.models.deletion.CASCADE, to='layerdefinitions.LayerDefinition', verbose_name='Layer Definition')),
                ('reviewer', models.ForeignKey(help_text='The user who reviewed this %(app_label)s.', on_delete=django.db.models.deletion.CASCADE, related_name='layerdefinitions_review_related', to=settings.AUTH_USER_MODEL, verbose_name='Reviewed by')),
            ],
            options={
                'ordering': ['review_date'],
                'abstract': False,
            },
        ),
    ]
