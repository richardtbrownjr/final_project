# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-10 19:46
from __future__ import unicode_literals

from django.db import migrations, models

import csv
import os


def import_data(apps, schema_editor):
    filename = os.path.abspath('north_carolina_banks.csv')
    Bank = apps.get_model("lending_app", "Bank")
    State = apps.get_model("lending_app", "State")
    with open(filename) as f:
        f.seek(0)
        reader = csv.reader(f, delimiter=",")
        next(reader)
        for row in reader:
            name = row[0]
            location = row[1] + ", " + row[2] + ", " + row[3]
            total_assets = row[6]
            total_liability = row[7]
            net_income = row[8]
            total_amount_small = row[9]
            total_num_loans_small = row[10]
            total_amount_micro = row[11]
            total_num_loans_micro = row[12]
            # Need to customize s for more states
            s = State.objects.get_or_create(name="North Carolina")
            b = Bank(state=s[0], name=name, location=location,
                     net_income=net_income, total_assets=total_assets,
                     total_liability=total_liability,
                     total_num_loans_small=total_num_loans_small,
                     total_num_loans_micro=total_num_loans_micro,
                     total_amount_small=total_amount_small,
                     total_amount_micro=total_amount_micro)
            b.save()
        print("Banks imported")


class Migration(migrations.Migration):

    dependencies = [
        ('lending_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_data)
    ]