# Generated by Django 3.2.9 on 2021-12-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0011_alter_detinationdetails_destination'),
    ]

    operations = [
        migrations.CreateModel(
            name='RenderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Img', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
