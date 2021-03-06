# Generated by Django 3.1.7 on 2021-03-29 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracd_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, null=True)),
                ('No_of_tickets', models.FloatField(null=True)),
                ('To', models.CharField(choices=[('Anna Nagar', 'Anna Nagar'), ('Alanthur', 'Alanthur'), ('Parrys Corner', 'Parrys Corner'), ('Porur', 'Porur'), ('Vadapalani', 'Vadapalani'), ('Koyembedu', 'Koyembedu')], max_length=100, null=True)),
                ('From', models.CharField(choices=[('Anna Nagar', 'Anna Nagar'), ('Alanthur', 'Alanthur'), ('Parrys Corner', 'Parrys Corner'), ('Porur', 'Porur'), ('Vadapalani', 'Vadapalani'), ('Koyembedu', 'Koyembedu')], max_length=100, null=True)),
                ('Time_of_arrival', models.TimeField()),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
