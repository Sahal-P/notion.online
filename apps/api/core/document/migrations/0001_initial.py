# Generated by Django 5.0 on 2023-12-26 05:17

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=355)),
                ('content', models.TextField(blank=True, null=True)),
                ('coverImage', models.CharField(blank=True, max_length=500, null=True)),
                ('coverImageBlurHash', models.CharField(blank=True, max_length=150, null=True)),
                ('icon', models.CharField(blank=True, max_length=500, null=True)),
                ('isArchived', models.BooleanField(default=False)),
                ('isPublished', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('parentDocument', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='document.document')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]