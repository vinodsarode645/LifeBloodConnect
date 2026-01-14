# Generated migration for BloodDonationCenter model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodapp', '0002_bloodrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodDonationCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('services', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Blood Donation Center',
                'verbose_name_plural': 'Blood Donation Centers',
                'ordering': ['city', 'name'],
            },
        ),
    ]
