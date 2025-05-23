from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0015_attendancerange'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendanceclass',
            options={'verbose_name': 'Attendance', 'verbose_name_plural': 'Attendance'},
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
