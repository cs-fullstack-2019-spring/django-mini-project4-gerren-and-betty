# Generated by Django 2.0.6 on 2019-03-05 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password1', models.CharField(max_length=16)),
                ('password2', models.CharField(max_length=16)),
                ('dateAccountCreated', models.DateField(verbose_name=django.utils.timezone.now)),
                ('userTableForeignKey', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GameModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('developer', models.CharField(max_length=50)),
                ('dateMade', models.DateField(default='')),
                ('ageLimit', models.IntegerField(default=0)),
                ('collector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gameapp.CollectorModel')),
            ],
        ),
    ]
