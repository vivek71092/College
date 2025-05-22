from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0013_auto_20181112_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
