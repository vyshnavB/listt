# Generated by Django 4.1.3 on 2023-08-08 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_categories_company_delete_billingaddress_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts/'),
        ),
    ]
