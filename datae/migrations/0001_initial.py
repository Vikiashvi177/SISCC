# Generated by Django 4.2.6 on 2023-10-20 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crudst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stname', models.CharField(max_length=100)),
                ('stemail', models.CharField(max_length=100)),
                ('staddress', models.CharField(max_length=100)),
                ('stmobile', models.BigIntegerField()),
                ('stgender', models.CharField(max_length=1)),
                ('ststart', models.CharField(max_length=100)),
                ('stend', models.CharField(max_length=100)),
                ('stbank', models.BigIntegerField()),
                ('staadhar', models.BigIntegerField()),
                ('strfid', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RFIDInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfid', models.CharField(max_length=100)),
                ('start_location', models.CharField(max_length=100)),
                ('end_location', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('route', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]