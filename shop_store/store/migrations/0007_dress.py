# Generated by Django 4.2.1 on 2023-06-12 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_acc_item_id_remove_bottom_item_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=5, null=True)),
                ('itemname', models.CharField(max_length=255, null=True)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
    ]
