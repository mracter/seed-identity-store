# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-26 10:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('identities', '0004_detailkey'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptIn',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='UUID of this opt-in request.', primary_key=True, serialize=False)),
                ('address_type', models.CharField(default='', help_text='Address type used to identify the identity.', max_length=50)),
                ('address', models.CharField(default='', help_text='Address used to identify the identity.', max_length=255)),
                ('request_source', models.CharField(help_text='Service that the optin was requested from.', max_length=100)),
                ('requestor_source_id', models.CharField(help_text='ID for the user requesting the optin on the service that it was requested from. Ideally a UUID.', max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Time request was received.')),
                ('created_by', models.ForeignKey(help_text='User creating the OptIn', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='optin_created', to=settings.AUTH_USER_MODEL)),
                ('identity', models.ForeignKey(help_text='UUID for the identity opting in.', null=True, on_delete=django.db.models.deletion.CASCADE, to='identities.Identity')),
            ],
        ),
    ]
