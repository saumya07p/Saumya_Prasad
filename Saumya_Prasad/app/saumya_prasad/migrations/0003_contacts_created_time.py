
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saumya_prasad', '0002_remove_contacts_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='created_time',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
    ]
