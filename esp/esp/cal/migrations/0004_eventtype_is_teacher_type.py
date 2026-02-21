# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import migrations, models

def backfill_teacher_types(apps, schema_editor):
    EventType = apps.get_model('cal', 'EventType')
    EventType.objects.filter(description__in=['Teacher Interview', 'Teacher Training']).update(is_teacher_type=True)


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0003_event_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtype',
            name='is_teacher_type',
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(backfill_teacher_types, reverse_code=migrations.RunPython.noop),
    ]
