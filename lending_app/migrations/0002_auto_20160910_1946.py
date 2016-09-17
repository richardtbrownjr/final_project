# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-10 19:46
from __future__ import unicode_literals

from django.db import migrations, models

import csv
import os


def import_data(apps, schema_editor):
    filename = os.path.abspath('final_bank_data.csv')
    Bank = apps.get_model("lending_app", "Bank")
    State = apps.get_model("lending_app", "State")

    states = {
        "AK": "Alaska",
        "AL": "Alabama",
        "AR": "Arkansas",
        "AS": "American Samoa",
        "AZ": "Arizona",
        "CA": "California",
        "CO": "Colorado",
        "CT": "Connecticut",
        "DC": "District of Columbia",
        "DE": "Delaware",
        "FL": "Florida",
        "GA": "Georgia",
        "GU": "Guam",
        "HI": "Hawaii",
        "IA": "Iowa",
        "ID": "Idaho",
        "IL": "Illinois",
        "IN": "Indiana",
        "KS": "Kansas",
        "KY": "Kentucky",
        "LA": "Louisiana",
        "MA": "Massachusetts",
        "MD": "Maryland",
        "ME": "Maine",
        "MI": "Michigan",
        "MN": "Minnesota",
        "MO": "Missouri",
        "MS": "Mississippi",
        "MT": "Montana",
        "NC": "North Carolina",
        "ND": "North Dakota",
        "NE": "Nebraska",
        "NH": "New Hampshire",
        "NJ": "New Jersey",
        "NM": "New Mexico",
        "NV": "Nevada",
        "NY": "New York",
        "OH": "Ohio",
        "OK": "Oklahoma",
        "OR": "Oregon",
        "PA": "Pennsylvania",
        "PR": "Puerto Rico",
        "RI": "Rhode Island",
        "SC": "South Carolina",
        "SD": "South Dakota",
        "TN": "Tennessee",
        "TX": "Texas",
        "UT": "Utah",
        "VA": "Virginia",
        "VI": "Virgin Islands",
        "VT": "Vermont",
        "WA": "Washington",
        "WI": "Wisconsin",
        "WV": "West Virginia",
        "WY": "Wyoming"
    }

    with open(filename) as f:
        f.seek(0)
        reader = csv.reader(f, delimiter=",")
        # next(reader)
        for row in reader:
            for index, item in enumerate(row):
                if item == '':
                    row[index] = 0
            name = row[0]
            location = row[1] + ", " + row[2] + ", " + row[3]  # city, state, zipcode
            number_of_employees = row[5]
            total_assets = row[6]
            total_liability = row[7]
            total_deposits = row[8]
            common_stock = row[9]
            derivatives = row[10]
            total_securities = row[11]
            asset_backed_securities = row[12]
            mortgage_backed_securities = row[13]
            family_residential_loans = row[14]
            home_equity_loans = row[15]
            adjustable_rate_loans_secured_by_family_residential = row[16]
            total_loans = row[17]
            total_amount_individual = row[18]
            total_amount_micro = row[19]
            total_amount_small = row[21]

            total_num_loans_micro = row[20]
            total_num_loans_small = row[22]
            total_amount_farm = row[23]
            total_num_loans_farm = row[24]

            if int(total_loans) == 0:
                individual_loan_percentage = 0
                small_loan_percentage = 0
                micro_loan_percentage = 0
                farm_loan_percentage = 0
            else:
                individual_loan_percentage = int(total_amount_individual) / int(total_loans)
                small_loan_percentage = int(total_amount_small) / int(total_loans)
                micro_loan_percentage = int(total_amount_micro) / int(total_loans)
                farm_loan_percentage = int(total_amount_farm) / int(total_loans)

            other_real_estate_owned = row[25]
            real_estate_acquired = row[26]
            other_real_estate_owned_family = row[27]
            other_real_estate_owned_multi_family_residential = row[28]
            other_real_estate_owned_commercial_real_estate = row[29]
            other_real_estate_owned_construction_development = row[30]
            other_real_estate_owned_farmland = row[31]
            foreclosed_properties_from_GNMA_loans = row[32]
            net_interest_margin = row[34] # + ?
            noninterest_income_to_average_assets = row[35]
            noninterest_expense_to_average_assets = row[36]
            loan_and_lease_loss_provision_to_assets = row[37]
            net_operating_income_to_assets = row[38]
            return_on_assets = row[39]
            return_on_equity = row[40]
            retained_earnings_to_average_equity = row[41]
            net_charge_offs_to_loans = row[42]
            net_loans_and_leases_to_total_assets = row[43]
            net_loans_and_leases_to_deposits = row[44]
            net_loans_and_leases_to_core_deposits = row[45]
            total_domestic_deposits_to_total_assets = row[46]
            average_total_assets = row[47]
            average_earning_assets = row[48]
            average_equity = row[49]
            average_total_loans = row[50]
            number_domestic_offices = row[51]
            total_complaints = row[53]
            score = (individual_loan_percentage + small_loan_percentage +
                     micro_loan_percentage + farm_loan_percentage)


            # Need to customize s for more states
            s = State.objects.get_or_create(name=states[row[2]])
            b = Bank(state=s[0], name=name, location=location,
                     number_of_employees=number_of_employees,
                     total_assets=total_assets,
                     total_liability=total_liability,
                     total_deposits=total_deposits,
                     common_stock=common_stock,
                     derivatives=derivatives,
                     total_securities=total_securities,
                     asset_backed_securities=asset_backed_securities,
                     mortgage_backed_securities=mortgage_backed_securities,
                     family_residential_loans=family_residential_loans,
                     home_equity_loans=home_equity_loans,
                     adjustable_rate_loans_secured_by_family_residential=adjustable_rate_loans_secured_by_family_residential,
                     total_num_loans_small=total_num_loans_small,
                     total_num_loans_micro=total_num_loans_micro,
                     total_num_loans_farm=total_num_loans_farm,
                     total_amount_small=total_amount_small,
                     total_amount_micro=total_amount_micro,
                     total_amount_farm=total_amount_farm,
                     individual_loan_percentage=individual_loan_percentage,
                     small_loan_percentage=small_loan_percentage,
                     micro_loan_percentage=micro_loan_percentage,
                     farm_loan_percentage=farm_loan_percentage,
                     other_real_estate_owned=other_real_estate_owned,
                     real_estate_acquired=real_estate_acquired,
                     other_real_estate_owned_family=other_real_estate_owned_family,
                     other_real_estate_owned_multi_family_residential=other_real_estate_owned_multi_family_residential,
                     other_real_estate_owned_commercial_real_estate=other_real_estate_owned_commercial_real_estate,
                     other_real_estate_owned_construction_development=other_real_estate_owned_construction_development,
                     other_real_estate_owned_farmland=other_real_estate_owned_farmland,
                     foreclosed_properties_from_GNMA_loans=foreclosed_properties_from_GNMA_loans,
                     net_interest_margin=net_interest_margin,
                     noninterest_income_to_average_assets=noninterest_income_to_average_assets,
                     noninterest_expense_to_average_assets=noninterest_expense_to_average_assets,
                     loan_and_lease_loss_provision_to_assets=loan_and_lease_loss_provision_to_assets,
                     net_operating_income_to_assets=net_operating_income_to_assets,
                     return_on_assets=return_on_assets,
                     return_on_equity=return_on_equity,
                     retained_earnings_to_average_equity=retained_earnings_to_average_equity,
                     net_charge_offs_to_loans=net_charge_offs_to_loans,
                     net_loans_and_leases_to_total_assets=net_loans_and_leases_to_total_assets,
                     net_loans_and_leases_to_deposits=net_loans_and_leases_to_deposits,
                     net_loans_and_leases_to_core_deposits=net_loans_and_leases_to_core_deposits,
                     total_domestic_deposits_to_total_assets=total_domestic_deposits_to_total_assets,
                     average_total_assets=average_total_assets,
                     average_earning_assets=average_earning_assets,
                     average_equity=average_equity,
                     average_total_loans=average_total_loans,
                     number_domestic_offices=number_domestic_offices,
                     total_complaints=total_complaints,
                     score=score)
            b.save()
        print("Banks imported")


def update_states(apps, schema_editor):
    State = apps.get_model("lending_app", "State")
    states = State.objects.all()
    for state in states:
        b = state.bank_set.count()
        avg_of_score = state.bank_set.aggregate(models.Avg('score'))['score__avg']
        state.number_of_banks = b
        state.average_score = avg_of_score
        state.save()



class Migration(migrations.Migration):

    dependencies = [
        ('lending_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_data),
        migrations.RunPython(update_states)
    ]
