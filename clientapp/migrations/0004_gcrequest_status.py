# Generated by Django 2.0.4 on 2018-04-13 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0003_gcrequest_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='gcrequest',
            name='status',
            field=models.CharField(choices=[('0', 'Not responded yet'), ('1', 'Accepted'), ('2', 'Rejected')], default='0', max_length=1),
        ),
    ]