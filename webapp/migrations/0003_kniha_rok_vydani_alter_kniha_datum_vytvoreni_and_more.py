# Generated by Django 5.0.2 on 2024-03-03 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_rename_zaznam_kniha'),
    ]

    operations = [
        migrations.AddField(
            model_name='kniha',
            name='rok_vydani',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kniha',
            name='datum_vytvoreni',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='kniha',
            name='pocet_stran',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='kniha',
            name='zanr',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
