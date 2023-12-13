from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saumya_prasad', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='created_time',
        ),
    ]
