# -*- coding: utf-8 -*-

__version__ = '0.1'

"""
Spend less time filling out your time card.
Less time = less dollars paid by policy holders.

Jared Musil - KBW5
"""

# self authored
import page

# packages
import os
import re
import math
import time
import json
import tkinter as tk
import tkinter.ttk as ttk
from selenium import webdriver


# from tkinter.filedialog import askopenfilename
# import shutil
# import pickle
# import subprocess
# from selenium.webdriver.common.keys import Keys


class Model:
    def __init__(self, root):
        self.root = root
        self.app_root = os.path.dirname(os.path.abspath(__file__))

    def get_schedule_names(self):
        """Populate schedule drop down with configuration name keys found in configuration.json"""

        try:
            with open('configuration.json') as config_file:
                schedule_names = []
                config = json.load(config_file)
                for schedule in config["schedules"]:
                    schedule_names.append(schedule["name"])
            return schedule_names
        except:
            print("Error: Something went wrong while processing the configuration.json file.")

    def get_schedule_selection(self):
        """Populate schedule drop down with configuration name keys found in configuration.json"""

        try:
            with open('configuration.json') as config_file:
                config = json.load(config_file)
            return config["selection"]
        except:
            print("Error in get_schedule_selection() - Something went wrong while processing the configuration.json file.")

    def load_schedule(self):
        """Populate GUI with predefined values from configuration.json"""

        try:
            with open('configuration.json') as config_file:
                config = json.load(config_file)
                selection = config["selection"]

                print("loading schedule as #" + str(selection))

                # set app time
                for period in range(1, self.root.pay_periods + 1):
                    # print("PERIOD:", period)
                    for instance in range(1, self.root.instances + 1):
                        # print(" INSTANCE:", instance)
                        for day in self.root.week:
                            # print("  DAY:", day)
                            _in = 'wk' + str(period) + '_' + day + '_' + 'in' + str(instance)
                            _out = 'wk' + str(period) + '_' + day + '_' + 'out' + str(instance)
                            _in_time = config["schedules"][selection]["week"][period-1]["instance"][instance-1]["in"][day]
                            _out_time = config["schedules"][selection]["week"][period-1]["instance"][instance-1]["out"][day]
                            # print("  ", _in, " | ", _in_time)
                            # print("  ", _out, " | ", _out_time)
                            self.root.user_time[_in].set(_in_time)
                            self.root.user_time[_out].set(_out_time)
            self.sum_rows()
            self.sum_totals()

        except:
            print("Error in set_schedule() - Something went wrong while processing the configuration.json file.")

    def sum_row(self, column, row):
        """
        Calculate the difference between in and out time values for a specific row.

        :param column: a column is equivalent to a period on the timecard
        :param row: a row is equivalent to a day on the timecard
        :return: a string in the format of "HH:MM" consisting of every in/out grouping of a given row.
        """

        total = 0

        # compute total time in minutes
        for instance in range(1, self.root.instances + 1):
            _in = 'wk' + str(column) + '_' + row + '_' + 'in' + str(instance)
            _out = 'wk' + str(column) + '_' + row + '_' + 'out' + str(instance)
            _in_val = self.root.user_time[_in].get()
            _out_val = self.root.user_time[_out].get()

            # print("IN:", _in, _in_val, "\t\tOUT:", _out, _out_val)

            # skip instance configurations with "" values
            if (_in_val is not "" or _out_val is not ""):
                in_split = re.split(':', _in_val)
                out_split = re.split(':', _out_val)

                # compute the difference between in and out
                instance_hours = int(out_split[0]) - int(in_split[0])
                instance_minutes = int(out_split[1]) - int(in_split[1])

                # convert to minutes
                minutes_from_hours = instance_hours * 60
                total_in_minutes = minutes_from_hours + instance_minutes

                # add to total
                total += total_in_minutes

        # convert minutes to timestamp
        hours = math.floor(total / 60)
        minutes = total % 60

        # use two decimal places for time
        if len(str(minutes)) == 1:
            timestamp = str(hours) + ":0" + str(minutes)
        else:
            timestamp = str(hours) + ":" + str(minutes)

        return timestamp

    def sum_rows(self):
        """Calculate the difference between in and out time values for each row, then sum the values."""

        for period in range(1, self.root.pay_periods + 1):
            for day in self.root.week:
                key = 'wk' + str(period) + '_' + day + '_' + 'total'
                value = self.sum_row(period, day)
                self.root.user_time[key].set(value)

    def sum_totals(self):
        """add up the hours and minutes for a pay period"""

        for period in range(1, self.root.pay_periods + 1):

            hours = 0
            minutes = 0

            for day in self.root.week:
                day_key = 'wk' + str(period) + '_' + day + '_' + 'total'
                day_total = self.root.user_time[day_key].get()

                # TODO - I don't think "" values are even possible after calling sun_rows() - double check if this is needed.
                # skip totals with "" values
                if (day_total is not ""):
                    day_total_split = re.split(':', day_total)

                hours = hours + int(day_total_split[0])
                minutes = minutes + int(day_total_split[1])

            # convert minutes into hours, for total time
            hours_from_minutes = math.floor(minutes / 60)

            if minutes > 60:
                total_minutes = str(minutes % 60)
            else:
                # use two decimal places for time
                if len(str(minutes)) == 1:
                    total_minutes = "0" + str(minutes)
                else:
                    total_minutes = str(minutes)

            # add up the hours and minutes, and convert it to a string
            week_total = str(hours + hours_from_minutes) + ":" + total_minutes

            # split this value into regular and overtime
            if ((hours + hours_from_minutes) > 40):
                week_regular = "40:00"
                week_overtime = str(hours + hours_from_minutes - 40) + ":" + str(minutes_remainder)
            else:
                week_regular = week_total
                week_overtime = "0"

            key_regular = 'wk' + str(period) + '_regular'
            key_overtime = 'wk' + str(period) + '_overtime'
            key_sick = 'wk' + str(period) + '_paid_sick_leave'
            self.root.user_time[key_regular].set(week_regular)
            self.root.user_time[key_overtime].set(week_overtime)
            self.root.user_time[key_sick].set("")
            # TODO Implement PSL code

            return [week_total, week_regular, week_overtime]

    def save_configuration(self):
        """Save any changes in configuration.json back to that file."""
        # TODO change this to save to "configuration.json" and not "configuration-save.json"

        try:
            with open('configuration.json') as config_file:
                config = json.load(config_file)
                selection = config["selection"]

                # save to config
                for period in range(1, self.root.pay_periods + 1):
                    # print("PERIOD:", period)
                    for instance in range(1, self.root.instances + 1):
                        # print(" INSTANCE:", instance)
                        for day in self.root.week:
                            # print("  DAY:", day)
                            _in = 'wk' + str(period) + '_' + day + '_' + 'in' + str(instance)
                            _out = 'wk' + str(period) + '_' + day + '_' + 'out' + str(instance)

                            _in_time = self.root.user_time[_in].get()
                            _out_time = self.root.user_time[_out].get()

                            # print("   IN:", _in, "IN_VAL:", _in_time)
                            # print("   OUT:", _out, "OUT_VAL:", _out_time)

                            config["schedules"][selection]["week"][period-1]["instance"][instance-1]["in"][day] = _in_time
                            config["schedules"][selection]["week"][period-1]["instance"][instance-1]["out"][day] = _out_time

            out_file = open("configuration.json", "w")
            json.dump(config, out_file, indent=4)
            out_file.close()

            print("\"configuration.json\" Saved!")

        except:
            print("Error saving schedule to configuration.json")

    def save_schedule_selection(self, selection):
        """Save the user selected schedule to user configuration.json file."""

        try:
            with open('configuration.json') as config_file:
                config = json.load(config_file)
                config["selection"] = selection

            out_file = open("configuration.json", "w")
            json.dump(config, out_file, indent=4)
            out_file.close()

            print("\"configuration.json\" Saved!")

        except:
            print("Error saving schedule to configuration.json")

    def submit_timecard(self):
        """Enter values in time card, using selenium webdriver."""

        self.driver = webdriver.Firefox()

        self.driver.get('http://sfnet.opr.statefarm.org/onlinetimecard/')

        main_page = page.MainPage(self.driver)
        main_page.click_current_pay_period_button()

        current_pay_period = page.CurrentPayPeriodPage(self.driver)

        # TODO refactor this into a loop
        current_pay_period.enter_time_wk1_saturday_in1(self.root.user_time['wk1_saturday_in1'].get())
        current_pay_period.enter_time_wk1_sunday_in1(self.root.user_time['wk1_sunday_in1'].get())
        current_pay_period.enter_time_wk1_monday_in1(self.root.user_time['wk1_monday_in1'].get())
        current_pay_period.enter_time_wk1_tuesday_in1(self.root.user_time['wk1_tuesday_in1'].get())
        current_pay_period.enter_time_wk1_wednesday_in1(self.root.user_time['wk1_wednesday_in1'].get())
        current_pay_period.enter_time_wk1_thursday_in1(self.root.user_time['wk1_thursday_in1'].get())
        current_pay_period.enter_time_wk1_friday_in1(self.root.user_time['wk1_friday_in1'].get())
        current_pay_period.enter_time_wk1_saturday_out1(self.root.user_time['wk1_saturday_out1'].get())
        current_pay_period.enter_time_wk1_sunday_out1(self.root.user_time['wk1_sunday_out1'].get())
        current_pay_period.enter_time_wk1_monday_out1(self.root.user_time['wk1_monday_out1'].get())
        current_pay_period.enter_time_wk1_tuesday_out1(self.root.user_time['wk1_tuesday_out1'].get())
        current_pay_period.enter_time_wk1_wednesday_out1(self.root.user_time['wk1_wednesday_out1'].get())
        current_pay_period.enter_time_wk1_thursday_out1(self.root.user_time['wk1_thursday_out1'].get())
        current_pay_period.enter_time_wk1_friday_out1(self.root.user_time['wk1_friday_out1'].get())

        current_pay_period.enter_time_wk1_saturday_in2(self.root.user_time['wk1_saturday_in2'].get())
        current_pay_period.enter_time_wk1_sunday_in2(self.root.user_time['wk1_sunday_in2'].get())
        current_pay_period.enter_time_wk1_monday_in2(self.root.user_time['wk1_monday_in2'].get())
        current_pay_period.enter_time_wk1_tuesday_in2(self.root.user_time['wk1_tuesday_in2'].get())
        current_pay_period.enter_time_wk1_wednesday_in2(self.root.user_time['wk1_wednesday_in2'].get())
        current_pay_period.enter_time_wk1_thursday_in2(self.root.user_time['wk1_thursday_in2'].get())
        current_pay_period.enter_time_wk1_friday_in2(self.root.user_time['wk1_friday_in2'].get())
        current_pay_period.enter_time_wk1_saturday_out2(self.root.user_time['wk1_saturday_out2'].get())
        current_pay_period.enter_time_wk1_sunday_out2(self.root.user_time['wk1_sunday_out2'].get())
        current_pay_period.enter_time_wk1_monday_out2(self.root.user_time['wk1_monday_out2'].get())
        current_pay_period.enter_time_wk1_tuesday_out2(self.root.user_time['wk1_tuesday_out2'].get())
        current_pay_period.enter_time_wk1_wednesday_out2(self.root.user_time['wk1_wednesday_out2'].get())
        current_pay_period.enter_time_wk1_thursday_out2(self.root.user_time['wk1_thursday_out2'].get())
        current_pay_period.enter_time_wk1_friday_out2(self.root.user_time['wk1_friday_out2'].get())

        current_pay_period.enter_time_wk1_saturday_in3(self.root.user_time['wk1_saturday_in3'].get())
        current_pay_period.enter_time_wk1_sunday_in3(self.root.user_time['wk1_sunday_in3'].get())
        current_pay_period.enter_time_wk1_monday_in3(self.root.user_time['wk1_monday_in3'].get())
        current_pay_period.enter_time_wk1_tuesday_in3(self.root.user_time['wk1_tuesday_in3'].get())
        current_pay_period.enter_time_wk1_wednesday_in3(self.root.user_time['wk1_wednesday_in3'].get())
        current_pay_period.enter_time_wk1_thursday_in3(self.root.user_time['wk1_thursday_in3'].get())
        current_pay_period.enter_time_wk1_friday_in3(self.root.user_time['wk1_friday_in3'].get())
        current_pay_period.enter_time_wk1_saturday_out3(self.root.user_time['wk1_saturday_out3'].get())
        current_pay_period.enter_time_wk1_sunday_out3(self.root.user_time['wk1_sunday_out3'].get())
        current_pay_period.enter_time_wk1_monday_out3(self.root.user_time['wk1_monday_out3'].get())
        current_pay_period.enter_time_wk1_tuesday_out3(self.root.user_time['wk1_tuesday_out3'].get())
        current_pay_period.enter_time_wk1_wednesday_out3(self.root.user_time['wk1_wednesday_out3'].get())
        current_pay_period.enter_time_wk1_thursday_out3(self.root.user_time['wk1_thursday_out3'].get())
        current_pay_period.enter_time_wk1_friday_out3(self.root.user_time['wk1_friday_out3'].get())

        current_pay_period.enter_time_wk1_saturday_in4(self.root.user_time['wk1_saturday_in4'].get())
        current_pay_period.enter_time_wk1_sunday_in4(self.root.user_time['wk1_sunday_in4'].get())
        current_pay_period.enter_time_wk1_monday_in4(self.root.user_time['wk1_monday_in4'].get())
        current_pay_period.enter_time_wk1_tuesday_in4(self.root.user_time['wk1_tuesday_in4'].get())
        current_pay_period.enter_time_wk1_wednesday_in4(self.root.user_time['wk1_wednesday_in4'].get())
        current_pay_period.enter_time_wk1_thursday_in4(self.root.user_time['wk1_thursday_in4'].get())
        current_pay_period.enter_time_wk1_friday_in4(self.root.user_time['wk1_friday_in4'].get())
        current_pay_period.enter_time_wk1_saturday_out4(self.root.user_time['wk1_saturday_out4'].get())
        current_pay_period.enter_time_wk1_sunday_out4(self.root.user_time['wk1_sunday_out4'].get())
        current_pay_period.enter_time_wk1_monday_out4(self.root.user_time['wk1_monday_out4'].get())
        current_pay_period.enter_time_wk1_tuesday_out4(self.root.user_time['wk1_tuesday_out4'].get())
        current_pay_period.enter_time_wk1_wednesday_out4(self.root.user_time['wk1_wednesday_out4'].get())
        current_pay_period.enter_time_wk1_thursday_out4(self.root.user_time['wk1_thursday_out4'].get())
        current_pay_period.enter_time_wk1_friday_out4(self.root.user_time['wk1_friday_out4'].get())

        current_pay_period.click_week_two_button()

        current_pay_period.enter_time_wk2_saturday_in1(self.root.user_time['wk2_saturday_in1'].get())
        current_pay_period.enter_time_wk2_sunday_in1(self.root.user_time['wk2_sunday_in1'].get())
        current_pay_period.enter_time_wk2_monday_in1(self.root.user_time['wk2_monday_in1'].get())
        current_pay_period.enter_time_wk2_tuesday_in1(self.root.user_time['wk2_tuesday_in1'].get())
        current_pay_period.enter_time_wk2_wednesday_in1(self.root.user_time['wk2_wednesday_in1'].get())
        current_pay_period.enter_time_wk2_thursday_in1(self.root.user_time['wk2_thursday_in1'].get())
        current_pay_period.enter_time_wk2_friday_in1(self.root.user_time['wk2_friday_in1'].get())
        current_pay_period.enter_time_wk2_saturday_out1(self.root.user_time['wk2_saturday_out1'].get())
        current_pay_period.enter_time_wk2_sunday_out1(self.root.user_time['wk2_sunday_out1'].get())
        current_pay_period.enter_time_wk2_monday_out1(self.root.user_time['wk2_monday_out1'].get())
        current_pay_period.enter_time_wk2_tuesday_out1(self.root.user_time['wk2_tuesday_out1'].get())
        current_pay_period.enter_time_wk2_wednesday_out1(self.root.user_time['wk2_wednesday_out1'].get())
        current_pay_period.enter_time_wk2_thursday_out1(self.root.user_time['wk2_thursday_out1'].get())
        current_pay_period.enter_time_wk2_friday_out1(self.root.user_time['wk2_friday_out1'].get())

        current_pay_period.enter_time_wk2_saturday_in2(self.root.user_time['wk2_saturday_in2'].get())
        current_pay_period.enter_time_wk2_sunday_in2(self.root.user_time['wk2_sunday_in2'].get())
        current_pay_period.enter_time_wk2_monday_in2(self.root.user_time['wk2_monday_in2'].get())
        current_pay_period.enter_time_wk2_tuesday_in2(self.root.user_time['wk2_tuesday_in2'].get())
        current_pay_period.enter_time_wk2_wednesday_in2(self.root.user_time['wk2_wednesday_in2'].get())
        current_pay_period.enter_time_wk2_thursday_in2(self.root.user_time['wk2_thursday_in2'].get())
        current_pay_period.enter_time_wk2_friday_in2(self.root.user_time['wk2_friday_in2'].get())
        current_pay_period.enter_time_wk2_saturday_out2(self.root.user_time['wk2_saturday_out2'].get())
        current_pay_period.enter_time_wk2_sunday_out2(self.root.user_time['wk2_sunday_out2'].get())
        current_pay_period.enter_time_wk2_monday_out2(self.root.user_time['wk2_monday_out2'].get())
        current_pay_period.enter_time_wk2_tuesday_out2(self.root.user_time['wk2_tuesday_out2'].get())
        current_pay_period.enter_time_wk2_wednesday_out2(self.root.user_time['wk2_wednesday_out2'].get())
        current_pay_period.enter_time_wk2_thursday_out2(self.root.user_time['wk2_thursday_out2'].get())
        current_pay_period.enter_time_wk2_friday_out2(self.root.user_time['wk2_friday_out2'].get())

        current_pay_period.enter_time_wk2_saturday_in3(self.root.user_time['wk2_saturday_in3'].get())
        current_pay_period.enter_time_wk2_sunday_in3(self.root.user_time['wk2_sunday_in3'].get())
        current_pay_period.enter_time_wk2_monday_in3(self.root.user_time['wk2_monday_in3'].get())
        current_pay_period.enter_time_wk2_tuesday_in3(self.root.user_time['wk2_tuesday_in3'].get())
        current_pay_period.enter_time_wk2_wednesday_in3(self.root.user_time['wk2_wednesday_in3'].get())
        current_pay_period.enter_time_wk2_thursday_in3(self.root.user_time['wk2_thursday_in3'].get())
        current_pay_period.enter_time_wk2_friday_in3(self.root.user_time['wk2_friday_in3'].get())
        current_pay_period.enter_time_wk2_saturday_out3(self.root.user_time['wk2_saturday_out3'].get())
        current_pay_period.enter_time_wk2_sunday_out3(self.root.user_time['wk2_sunday_out3'].get())
        current_pay_period.enter_time_wk2_monday_out3(self.root.user_time['wk2_monday_out3'].get())
        current_pay_period.enter_time_wk2_tuesday_out3(self.root.user_time['wk2_tuesday_out3'].get())
        current_pay_period.enter_time_wk2_wednesday_out3(self.root.user_time['wk2_wednesday_out3'].get())
        current_pay_period.enter_time_wk2_thursday_out3(self.root.user_time['wk2_thursday_out3'].get())
        current_pay_period.enter_time_wk2_friday_out3(self.root.user_time['wk2_friday_out3'].get())

        current_pay_period.enter_time_wk2_saturday_in4(self.root.user_time['wk2_saturday_in4'].get())
        current_pay_period.enter_time_wk2_sunday_in4(self.root.user_time['wk2_sunday_in4'].get())
        current_pay_period.enter_time_wk2_monday_in4(self.root.user_time['wk2_monday_in4'].get())
        current_pay_period.enter_time_wk2_tuesday_in4(self.root.user_time['wk2_tuesday_in4'].get())
        current_pay_period.enter_time_wk2_wednesday_in4(self.root.user_time['wk2_wednesday_in4'].get())
        current_pay_period.enter_time_wk2_thursday_in4(self.root.user_time['wk2_thursday_in4'].get())
        current_pay_period.enter_time_wk2_friday_in4(self.root.user_time['wk2_friday_in4'].get())
        current_pay_period.enter_time_wk2_saturday_out4(self.root.user_time['wk2_saturday_out4'].get())
        current_pay_period.enter_time_wk2_sunday_out4(self.root.user_time['wk2_sunday_out4'].get())
        current_pay_period.enter_time_wk2_monday_out4(self.root.user_time['wk2_monday_out4'].get())
        current_pay_period.enter_time_wk2_tuesday_out4(self.root.user_time['wk2_tuesday_out4'].get())
        current_pay_period.enter_time_wk2_wednesday_out4(self.root.user_time['wk2_wednesday_out4'].get())
        current_pay_period.enter_time_wk2_thursday_out4(self.root.user_time['wk2_thursday_out4'].get())
        current_pay_period.enter_time_wk2_friday_out4(self.root.user_time['wk2_friday_out4'].get())

        current_pay_period.click_calculate_biweekly_totals_button()

        # current_pay_period.click_save_button()

        self.driver.close()

class View:
    def __init__(self, root):
        self.root = root
        # self.absence_categories = {'Absent without Leave': 'AWOL', 'California Paid Leave': 'CAPL', 'Catastrophe Time Off': 'CTO', 'Community Svc/Education Support': 'CSES', 'Community Svc/Educ Supt-Cat': 'CSEC', 'Comm Srv/Edu Supt-Ag Interns': 'CSEA', 'Family Leave for Bonding': 'FLB', 'Florida Crime Victim': 'FLDV', 'Holiday': 'HOL', 'Late No Pay': 'LNP', 'Late with Pay': 'LP', 'Leave of Absence': 'LA', 'Medical Leave': 'ML', 'Military Leave 2 Paid': 'ML2P', 'Military Leave 2 Unpaid': 'ML2U', 'Military Qualifying Exigency': 'MQE', 'Office Closed': 'OC', 'Paid Adoption Leave': 'PAL', 'Paid Sick Leave': 'PSL', 'Paid Sick Leave - Agency Interns': 'PSLA', 'Paid Sick Leave - Cat Svcs & CA&P': 'PSLC', 'Paid Time Off': 'PTO', 'Paid Time Off - ESP employees': 'PTOE', 'Paid Vacation': 'PV', 'Paid Vacation - Agency Intern': 'PVA', 'Paid Vacation - Cat Svcs & CA&P': 'PVC', 'Paid Vacation - Massachusetts': 'PVMA', 'Permission Doctor/Dentist': 'PD', 'Permission Funeral': 'PF', 'Permission Gov. Obligation': 'PGO', 'Permission Morale': 'PM', 'Permission Sick Family': 'PSF', 'Personal Time': 'PT', 'Personal Time - Agency Interns': 'PTA', 'Personal Time - Cat Svcs & CA&P': 'PTC', 'Personal Time - Massachusetts': 'PTMA', 'Protected Sick Time Ordinance': 'PSTO', 'Provisional Weekend': 'PW', 'Re-acclimation Days – Cat Vol': 'REAC', 'Seattle Paid Sick/Safe Time': 'PSST', 'Substitute Holiday': 'SH', 'Veterans Day': 'VETD'}
        self.absence_categories = ['', 'AWOL', 'CAPL', 'CTO', 'CSES', 'CSEC', 'CSEA', 'FLB', 'FLDV', 'HOL', 'LNP', 'LP', 'LA', 'ML', 'ML2P', 'ML2U', 'MQE', 'OC', 'PAL', 'PSL', 'PSLA', 'PSLC', 'PTO', 'PTOE', 'PV', 'PVA', 'PVC', 'PVMA', 'PD', 'PF', 'PGO', 'PM', 'PSF', 'PT', 'PTA', 'PTC', 'PTMA', 'PSTO', 'PW', 'REAC', 'PSST', 'SH', 'VETD']
        self.icon = Icons()

        self._init_widgets()

    def _init_widgets(self):
        self.container = ttk.Frame(root)
        self.container.grid(row=0, column=0, sticky=tk.NSEW)

        self._timecard()
        self._footer()

    def _timecard(self):

        # widgets
        self.timecard = tk.Frame()
        self.timecard.week_1 = ttk.LabelFrame(self.timecard, text='Week 1')
        self.timecard.week_2 = ttk.LabelFrame(self.timecard, text='Week 2')
        self.timecard.absences_1 = ttk.LabelFrame(self.timecard, text='Absences')
        self.timecard.absences_2 = ttk.LabelFrame(self.timecard, text='Absences')
        self.timecard.total_1 = ttk.LabelFrame(self.timecard, text='Totals')
        self.timecard.total_2 = ttk.LabelFrame(self.timecard, text='Totals')

        # geometry
        self.timecard.grid(row=0, column=0, sticky=tk.NSEW)
        self.timecard.week_1.grid(row=0, column=0, sticky=tk.NSEW, padx=(5, 0), pady=5)
        self.timecard.week_2.grid(row=1, column=0, sticky=tk.NSEW, padx=(5, 0), pady=5)
        self.timecard.absences_1.grid(row=0, column=1, sticky=tk.NSEW, padx=(5, 0), pady=5)
        self.timecard.absences_2.grid(row=1, column=1, sticky=tk.NSEW, padx=(5, 0), pady=5)
        self.timecard.total_1.grid(row=0, column=2, sticky=tk.NSEW, padx=5, pady=5)
        self.timecard.total_2.grid(row=1, column=2, sticky=tk.NSEW, padx=5, pady=5)

        # weight
        self.timecard.grid_rowconfigure(0, weight=1)
        self.timecard.grid_rowconfigure(1, weight=1)
        self.timecard.grid_columnconfigure(0, weight=1)
        self.timecard.grid_columnconfigure(1, weight=1)

        self._pay_periods()
        self._absences()
        self._grand_totals()

    def _pay_periods(self):

        self._pay_period_row_labels()

        pay_periods = [self.timecard.week_1, self.timecard.week_2]
        instances = 4
        width = 5
        week = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']

        # widgets
        for period_index, period in enumerate(pay_periods):
            for instance in range(1, instances + 1):
                c_in = (instance * 2) - 1
                c_out = instance * 2

                ttk.Label(period, text='In', anchor=tk.CENTER).grid(row=0, column=c_in, sticky=tk.NSEW, padx=(0, 1), pady=(0, 1))
                ttk.Label(period, text='Out', anchor=tk.CENTER).grid(row=0, column=c_out, sticky=tk.NSEW, padx=(0, 5), pady=(0, 1))

                for day_index, day in enumerate(week):
                    day_index += 1  # offset for column labels

                    _in = 'wk' + str(period_index + 1) + '_' + day + '_' + 'in' + str(instance)
                    _out = 'wk' + str(period_index + 1) + '_' + day + '_' + 'out' + str(instance)

                    ## sv.trace(self.register(self.is_time_format), '%S')
                    ## validate_out.trace(self.register(self.is_time_format), '%S')

                    ttk.Entry(period, textvar=self.root.user_time[_in], validate='focusout', width=width).grid(row=day_index, column=c_in, sticky=tk.NSEW, padx=(0, 1), pady=(0, 1))
                    ttk.Entry(period, textvar=self.root.user_time[_out], validate='focusout', width=width).grid(row=day_index, column=c_out, sticky=tk.NSEW, padx=(0, 5), pady=(0, 1))

            # add a empty invisible frame solely to keep the UI pixel perfect
            ttk.Frame(period, height=4).grid(row=day_index + 1, columnspan=instances * 2 + 1, sticky=tk.NSEW)

        self._pay_period_row_totals(instances * 2 + 1)

    def _pay_period_row_labels(self):

        pay_period = [self.timecard.week_1, self.timecard.week_2]

        for period in pay_period:
            period.saturday = ttk.Label(period, text='Saturday').grid(row=1, column=0, sticky=tk.NSEW, padx=5, pady=(0, 1))
            period.sunday = ttk.Label(period, text='Sunday').grid(row=2, column=0, sticky=tk.NSEW, padx=5, pady=(0, 1))
            period.monday = ttk.Label(period, text='Monday').grid(row=3, column=0, sticky=tk.NSEW, padx=5, pady=(0, 1))
            period.tuesday = ttk.Label(period, text='Tuesday').grid(row=4, column=0, sticky=tk.NSEW, padx=5, pady=(0, 1))
            period.wednesday = ttk.Label(period, text='Wednesday').grid(row=5, column=0, sticky=tk.NSEW, padx=5, pady=(0, 1))
            period.thursday = ttk.Label(period, text='Thursday').grid(row=6, column=0, sticky=tk.NSEW, padx=5, pady=(0, 1))
            period.friday = ttk.Label(period, text='Friday').grid(row=7, column=0, sticky=tk.NSEW, padx=5, pady=(0, 1))

    def _pay_period_row_totals(self, column_offset):

        w = 5
        pay_periods = [self.timecard.week_1, self.timecard.week_2]
        week = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']

        # tkinter variables
        for period in range(1, len(pay_periods) + 1):
            for day in week:
                _total = 'wk' + str(period) + '_' + day + '_' + 'total'
                self.root.user_time[_total] = tk.StringVar()

        # widgets
        for period_index, period in enumerate(pay_periods):
            period.total = ttk.Label(period, text='Total').grid(row=0, column=column_offset, sticky=tk.NSEW, padx=5, pady=(0, 1))

            for day_index, day in enumerate(week):
                day_index += 1  # offset for column labels
                _total = 'wk' + str(period_index + 1) + '_' + day + '_' + 'total'
                ttk.Entry(period, textvar=self.root.user_time[_total], width=w, state='normal').grid(row=day_index, column=column_offset, sticky=tk.NSEW, padx=(0, 5), pady=(0, 1))

    def _absences(self):

        w = 6
        pay_period = [self.timecard.absences_1, self.timecard.absences_2]

        for period in pay_period:
            period.total = ttk.Label(period, text='Total').grid(row=0, column=0, sticky=tk.NSEW, padx=(5, 1), pady=(0, 1))

            period.total_saturday = ttk.Entry(period, width=w).grid(row=1, column=0, sticky=tk.NSEW, padx=(5, 1), pady=(0, 1))
            period.total_sunday = ttk.Entry(period, width=w).grid(row=2, column=0, sticky=tk.NSEW, padx=(5, 1), pady=(0, 1))
            period.total_monday = ttk.Entry(period, width=w).grid(row=3, column=0, sticky=tk.NSEW, padx=(5, 1), pady=(0, 1))
            period.total_tuesday = ttk.Entry(period, width=w).grid(row=4, column=0, sticky=tk.NSEW, padx=(5, 1), pady=(0, 1))
            period.total_wednesday = ttk.Entry(period, width=w).grid(row=5, column=0, sticky=tk.NSEW, padx=(5, 1), pady=(0, 1))
            period.total_thursday = ttk.Entry(period, width=w).grid(row=6, column=0, sticky=tk.NSEW, padx=(5, 1), pady=(0, 1))
            period.total_friday = ttk.Entry(period, width=w).grid(row=7, column=0, sticky=tk.NSEW, padx=(5, 1), pady=(0, 1))

            period.reason = ttk.Label(period, text='Code').grid(row=0, column=1, sticky=tk.NSEW, padx=(0, 5), pady=(0, 1))

            period.reason_saturday = ttk.Combobox(period, width=w, state='readonly')
            period.reason_sunday = ttk.Combobox(period, width=w, state='readonly')
            period.reason_monday = ttk.Combobox(period, width=w, state='readonly')
            period.reason_tuesday = ttk.Combobox(period, width=w, state='readonly')
            period.reason_wednesday = ttk.Combobox(period, width=w, state='readonly')
            period.reason_thursday = ttk.Combobox(period, width=w, state='readonly')
            period.reason_friday = ttk.Combobox(period, width=w, state='readonly')

            period.reason_saturday['values'] = self.absence_categories
            period.reason_sunday['values'] = self.absence_categories
            period.reason_monday['values'] = self.absence_categories
            period.reason_tuesday['values'] = self.absence_categories
            period.reason_wednesday['values'] = self.absence_categories
            period.reason_thursday['values'] = self.absence_categories
            period.reason_friday['values'] = self.absence_categories

            period.reason_saturday.current(0)
            period.reason_sunday.current(0)
            period.reason_monday.current(0)
            period.reason_tuesday.current(0)
            period.reason_wednesday.current(0)
            period.reason_thursday.current(0)
            period.reason_friday.current(0)

            period.reason_saturday.grid(row=1, column=1, sticky=tk.NSEW, padx=(0, 5), pady=(0, 1))
            period.reason_sunday.grid(row=2, column=1, sticky=tk.NSEW, padx=(0, 5), pady=(0, 1))
            period.reason_monday.grid(row=3, column=1, sticky=tk.NSEW, padx=(0, 5), pady=(0, 1))
            period.reason_tuesday.grid(row=4, column=1, sticky=tk.NSEW, padx=(0, 5), pady=(0, 1))
            period.reason_wednesday.grid(row=5, column=1, sticky=tk.NSEW, padx=(0, 5), pady=(0, 1))
            period.reason_thursday.grid(row=6, column=1, sticky=tk.NSEW, padx=(0, 5), pady=(0, 1))
            period.reason_friday.grid(row=7, column=1, sticky=tk.NSEW, padx=(0, 5), pady=(0, 1))

    def _grand_totals(self):
        # TODO refactor this to use loops / less lines of code

        # widgets
        self.timecard.total_1.regular = ttk.Label(self.timecard.total_1, text='Regular')
        self.timecard.total_1.overtime = ttk.Label(self.timecard.total_1, text='Overtime')
        self.timecard.total_1.paid_sick_leave = ttk.Label(self.timecard.total_1, text='PSL')
        self.timecard.total_1.regular_value = ttk.Entry(self.timecard.total_1, textvar=self.root.user_time['wk1_regular'], state='normal', width=6)
        self.timecard.total_1.overtime_value = ttk.Entry(self.timecard.total_1, textvar=self.root.user_time['wk1_overtime'], state='normal', width=6)
        self.timecard.total_1.paid_sick_leave_value = ttk.Entry(self.timecard.total_1, textvar=self.root.user_time['wk1_paid_sick_leave'], state='normal', width=6)
        self.timecard.total_2.regular = ttk.Label(self.timecard.total_2, text='Regular')
        self.timecard.total_2.overtime = ttk.Label(self.timecard.total_2, text='Overtime')
        self.timecard.total_2.paid_sick_leave = ttk.Label(self.timecard.total_2, text='PSL')
        self.timecard.total_2.regular_value = ttk.Entry(self.timecard.total_2, textvar=self.root.user_time['wk1_regular'], state='normal', width=6)
        self.timecard.total_2.overtime_value = ttk.Entry(self.timecard.total_2, textvar=self.root.user_time['wk1_overtime'], state='normal', width=6)
        self.timecard.total_2.paid_sick_leave_value = ttk.Entry(self.timecard.total_2, textvar=self.root.user_time['wk1_paid_sick_leave'], state='normal', width=6)

        # geometry
        self.timecard.total_1.regular.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=(0, 1))
        self.timecard.total_1.regular_value.grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=(0, 1))
        self.timecard.total_1.overtime.grid(row=1, column=0, sticky=tk.NSEW, padx=5, pady=(0, 1))
        self.timecard.total_1.overtime_value.grid(row=1, column=1, sticky=tk.NSEW, padx=5, pady=(0, 1))
        self.timecard.total_1.paid_sick_leave.grid(row=2, column=0, sticky=tk.NSEW, padx=5, pady=(0, 1))
        self.timecard.total_1.paid_sick_leave_value.grid(row=2, column=1, sticky=tk.NSEW, padx=5, pady=(0, 1))
        self.timecard.total_2.regular.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=(0, 1))
        self.timecard.total_2.regular_value.grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=(0, 1))
        self.timecard.total_2.overtime.grid(row=1, column=0, sticky=tk.NSEW, padx=5, pady=(0, 1))
        self.timecard.total_2.overtime_value.grid(row=1, column=1, sticky=tk.NSEW, padx=5, pady=(0, 1))
        self.timecard.total_2.paid_sick_leave.grid(row=2, column=0, sticky=tk.NSEW, padx=5, pady=(0, 1))
        self.timecard.total_2.paid_sick_leave_value.grid(row=2, column=1, sticky=tk.NSEW, padx=5, pady=(0, 1))

    def _footer(self):

        # variabless
        self.schedules = []
        # configDirectory = os.path.dirname(os.path.abspath(__file__)) + 'config/'

        # widgets
        self.status = ttk.Frame(root)
        self.status.label = ttk.Label(self.status, text='Choose a Configuration:')
        self.status.schedule = ttk.Combobox(self.status, state='readonly')
        self.status.schedule['values'] = self.schedules
        self.status.load = ttk.Button(self.status, text='Load')
        self.status.save = ttk.Button(self.status, image=self.icon.run, compound="right", text='Save')
        self.status.submit = ttk.Button(self.status, image=self.icon.reset, compound="right", text='Submit')

        # geometry
        self.status.grid(row=1, column=0, sticky=tk.NSEW, padx=5, pady=(0, 5))
        self.status.label.grid(row=0, column=0, sticky=tk.NSEW)
        self.status.schedule.grid(row=0, column=1, sticky=tk.NSEW, padx=5)
        self.status.load.grid(row=0, column=2, sticky=tk.NSEW, padx=(0, 5))
        self.status.save.grid(row=0, column=3, sticky=tk.NSEW, padx=(0, 5))
        self.status.submit.grid(row=0, column=4, sticky=tk.NSEW)

        # weight
        self.status.grid_columnconfigure(1, weight=1)

    def is_time_format(self, S):
        """
        Only allow military time to be input (00:00 to 24:00)

        # valid percent substitutions (from the Tk entry man page)
        # %d = Type of action (1=insert, 0=delete, -1 for others)
        # %i = index of char string to be inserted/deleted, or -1
        # %P = value of the entry if the edit is allowed
        # %s = value of entry prior to editing
        # %S = the text string being inserted or deleted, if any
        # %v = the type of validation that is currently set
        # %V = the type of validation that triggered the callback
        #      (key, focusin, focusout, forced)
        # %W = the tk name of the widget
        """

        try:
            time.strptime(S, '%H:%M')
            return True
        except ValueError:
            return False

    def set_schedules(self, schedules):
        self.status.schedule['values'] = schedules
        #self.status.schedule.current(0)

    def get_schedule_selected(self):
        return self.status.schedule.current()


class Controller:
    def __init__(self, root):
        self.root = root
        self.root.title('SF Timecard')
        self.root.iconbitmap(os.path.dirname(os.path.abspath(__file__)) + '\\clock.ico')

        # variables
        self.widthProcessBtn = 130
        self.widthProcessIcon = 27

        # root window resizing
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.init_variables()

        self.model = Model(root)
        self.view = View(root)
        self.view.status.schedule.bind("<<ComboboxSelected>>", self.on_schedule_change)

        self.view.status.load.config(command=lambda: self.model.load_schedule())
        self.view.status.save.config(command=lambda: self.model.save_configuration())
        self.view.status.submit.config(command=lambda: self.model.submit_timecard())

        # Initialize
        self.load_schedule_choices()
        self.model.load_schedule()


    def load_schedule_choices(self):
        schedule_names = self.model.get_schedule_names()
        self.view.set_schedules(schedule_names)

        schedule_selection = self.model.get_schedule_selection()
        self.view.status.schedule.current(schedule_selection)

    def on_schedule_change(self, event):
        selection = self.view.get_schedule_selected()
        self.model.save_schedule_selection(selection)
        self.model.load_schedule()

    def init_variables(self):
        self.root.pay_periods = 2
        self.root.instances = 4
        self.root.week = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        self.root.user_time = {}

        # tkinter StringVar's
        for period in range(1, self.root.pay_periods + 1):
            for instance in range(1, self.root.instances + 1):
                for day in self.root.week:
                    _in = 'wk' + str(period) + '_' + day + '_' + 'in' + str(instance)
                    _out = 'wk' + str(period) + '_' + day + '_' + 'out' + str(instance)
                    self.root.user_time[_in] = tk.StringVar()
                    self.root.user_time[_out] = tk.StringVar()

        #TODO clean this up / add to above loop
        self.root.user_time['wk1_regular'] = tk.StringVar()
        self.root.user_time['wk1_overtime'] = tk.StringVar()
        self.root.user_time['wk1_paid_sick_leave'] = tk.StringVar()
        self.root.user_time['wk2_regular'] = tk.StringVar()
        self.root.user_time['wk2_overtime'] = tk.StringVar()
        self.root.user_time['wk2_paid_sick_leave'] = tk.StringVar()


class Icons:
    def __init__(self):
        # images
        self.add = tk.PhotoImage(
            data='R0lGODlhEAAQALMKAABy/5bG4ZDG5pLI247E9JXH2ZbF4ZDH5o7B/5LI3P///wAAAAAAAAAAAAAAAAAAACH5BAEAAAoALAAAAAAQABAAAAQ0UMlJq71Ygg3yBEHQeQookmWAjBa3EYTLpkJtH+FsDjyf5BRZoSDDAAwnkmlmBCo5qGg0AgA7')
        self.run = tk.PhotoImage(
            data='R0lGODlhEAAQAMZSADNIYzNIZDRJYzVKZTdMZjhNZzlNaDlOaDxQazxRaz5SbD5SbUJWb0RYcipbvUdadEpdd0teeExeeE5helBifFFkfVRmf1RngFlrhFtuhlxuh2BxiWFzi2R1jWV3jmZ4kGd5kEN+9Gt9k21/lm+Al1GD5XOEmneHnn+PpF6T/NTe9dXf9tbh9tji99rj9tzk99zl993m997n99/n+OHn+OLp+OPp+ePr+eXr+eXr+ubs+ebs+ubt+uju+eju+urv+uvv+uvw+uzx++3y++7y++7z++/z+/Dz/PD0/PH1/PL2/PP2/fT3/fX3/fX4/ff5/fn7/vv8/v///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////yH5BAEKAH8ALAAAAAAQABAAAAeXgH+Cg4SFhCWHiYaLi4iDjoKQkYqTkSkpIQ4ll5mbmA6RmaGgfyWig6SCqX+pJyYkIiAdGxoYFxUTEA8NfyNSv8DBv0wKfx5RKFAfTxRNCUoARwBDBX8ZTkxLSUhGREJAPz48OQF/FkUcQRE9BjoANgAzADAAfxI7ODc1NDIxLy4tWKxQUa8BgwUIDhAYIACAw4f1GC0KBAA7')
        self.open = tk.PhotoImage(
            data='R0lGODlhEAAQAOMJAICAAJ+fP///n19fP5+ff9+/P7+fP//fn19fX////////////////////////////yH5BAEKAA8ALAAAAAAQABAAAARE8MlJq70WaIAnOsJxIB0AnsemBRMQvudLSiZspy087Hw/1IdBYUgcGkiuYLF4pCmXxtkDMDBYr1fpg4Doer+dsHgsjgAAOw==')
        self.okay = tk.PhotoImage(
            data='R0lGODlhEAAQAIABAB4eHQAAACH5BAEAAAEALAAAAAAQABAAAAIjjI+pG8AK3DtRzmotwlk3TkUhtlUfWXJmoq6QeqGx99DTVAAAOw==')
        self.reset = tk.PhotoImage(
            data='R0lGODlhEAAQAOMJAAAAALAwF39ZBo1jBpVyHdGUDNusN+K7Uu7WgP///////////////////////////yH5BAEKAA8ALAAAAAAQABAAAARF8ElAq6XyAYK6/wIwIUZhnmYpakgRXEDQrsCcZXVB2zerj79ebhe8DSszDM5WaxWBxJWRp5FaZM+p55DFoQoDqRDWK5cjADs=')
        self.delete_document = tk.PhotoImage(
            data='R0lGODlhEAAQAOcAAP///8opAJMAAPb4+v/M/4SQnfr7/Pj5+/z9/f7+/vT2+Ss2QvH1+P9MDP8zAP8pAOnu9O3y9uXs8u/z9+vw9f+DIJSfq/9sFHJ+ivr7/ff5+4+PyGBpc/n7/GNsd1dfaIGOmkpUX3aBjX6KlvP2+e7y9/n6+3B7h2Zveuzx9oSRnfH09v3+/2hyfVBZYW14hJKRy/7///j6/I6Ox//+/mBoc52evoSRnrjBx2t1gHuHk3mEkOXr8dPY3oiUn4mVoerv9Ss3QlRcZoCKlvD1+Kissejt84iUof///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////yH5BAEKAH8ALAAAAAAQABAAAAjRAH/cKECwoAofFv4oVAgCgMOHDmEASLhwBIAEGDMCmOGQ4h8dABCIHAlgw0OKOwAYWMkyhg0XQj4MUSgCwIGbOE2wWNEDxxGFGAAMGEp0qAYZADAoPAGAhIKnTzM4lApA4QsARBhoZdCBRoAADr/+yQGgxISzEwAEIEDgK9sALQCkiEA3AgABFSqwzSsABQAgFAJT0HD3guELAv54AGAEgmMIA9Q2mNwgwB8OAHhI2CxBLYEHDhw8aFsD4kMBoAUIEC0gRJAFsGEXuSvAoeo/AQEAOw==')
        self.output = tk.PhotoImage(
            data='R0lGODlhEAAQAKUqAABCZQFGagBHbgBLcwBMcwFMdAFQeT9DRgBSewJSeAJXgQBZhANagklNTwJdiQBfiwNijwNmlAVsmwdwoV5hZAl0pmlsb25xc06LrVOOsGCdvKnV+KfY+rPa+Krf+b3f98Lh+crl+dHo+tfq+9zs++Hw/OXy/Ofz/e32/fD4/f///////////////////////////////////////////////////////////////////////////////////////yH5BAEKAD8ALAAAAAAQABAAAAaNwJ/wV6kMf5ekcjhJTY7QoQQlklivP4vW8oucQKCTWByBPkqdtDr9+FHelN9iQ6/TF9EfgsNB+P8/DYINQwQeBHl5AgJHB46PQhGSDJKVlJM/EBomJhoQJhCfn5wQPw4kDqcOI6msqw4JPwohCrO2t7RCARghIRgBGb0ZAQYfBkMAAwMAPwAFy83QiYlBADs=')
        self.recover = tk.PhotoImage(
            data='R0lGODlhEAAQALMAAP9jAP8AAM4AAL0AAP///87OznNzcwAAAP///wAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAgALAAAAAAQABAAAARaEEl5qp0YVQI6IFV2EGRgBmRxTGMqDC9JGKuW0pas2kRBYy1fBRAQ1IBE44E4OLKYw6KTkow2Mxpoi+QM/ragXKp2KMg8n96PYigUTgH3mnUwwGA4LMUSwkQAADs=')
        self.information_blue = tk.PhotoImage(
            data='R0lGODlhEAAQAMZAABqQ1iSS3CuS1SCX2SGX2yaZ3i6Y5C6c4zSf5i2k3zCj5C2k4yul4Tuf7zmi6z6i8DKn5DOn5Tmn3jym7D6o3jmq6EGp3z2q6kap4UOp8EWp8T6t6UCt6z2x5UGw6FOt5Eaw70yv806w9UK25liw5T645lqw5Vqw5k2z8k+z81Oz+VK28lO29ES851i1+1C661m591679168+mG99WO9/GO++mjE8WjH8HDF/G7H9HTI+3vM+XvN9oTQ/YzT/pLW/v///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////yH5BAEKAH8ALAAAAAAQABAAAAe8gH+CggKFhoOIf4UnPz4+PyeFiQImPTg0Li40OD0mAoMCJDo1MipAQCoyNTokn4o7MTAwIqcisjE7nwIfMywsKRoNDyG+LDMfhTwrKCgZp0AZzCgrPIU5INgTzw7Y2DmFNhziFwanCOLiNoU3GxXuB6cH7hUbN4UYHhERCgGnAQr6PGDQ9QLCggLPgBRYAOGFKwEWOjAgkJAAgw4WXCmiMCLBAAAABiQYQUEjIQESWpQo0UKCpEQnDZn8EwgAOw==')
        self.delete = tk.PhotoImage(
            data='R0lGODlhEAAQAKU5ANshId0iItwkJN4lJd4mJuAnJ9UrK98qKuErK+QuLuEvL+kzM+c2Nt45OeQ6Ot4+PuY+Puo9Pe48POk+Pt9BQfA+PutAQOhBQeZCQudEROFGRu5DQ+9GRvRHR/JISPFKSutQUORTU/JSUvVTU+VYWPlTU/ZVVeVaWuZaWvlYWPpaWvpeXvVhYfxjY/BoaPFoaPxnZ/RubvtwcPxwcPZ7e/l7e/2EhP6MjP6Skv///////////////////////////yH5BAEKAD8ALAAAAAAQABAAAAarwJ9QaCgah8hfEYW73XCoYtJwss1grRZsZjsZhgaSLFVSrVaqUkpG+ipro1yuYzJ15KPa1xBieeQ5FRWAHiwhRTQiHxKAgBIfIjRFMRwcGwuNCxuVMUUvFhYRCY0JEaAvRS4TDAiNcggMEy5FGhetcgICgAgXGnsgB3IACAgAcgcgbgYUDgIAAwUFAwACDhRuSg8YCgQBAQQKGA/YRAYNGRAQGQ1SSeVG5D9BADs=')
        # colors
        self.ncsRed = '#C40233'
        self.ncsBlue = '#0087BD'
        self.ncsGreen = '#009F6B'
        self.ncsYellow = '#FFD300'
        # styles
        style = ttk.Style()
        style.configure('bgRed.TLabel', background=self.ncsRed)
        style.configure('bgGreen.TLabel', background=self.ncsGreen)
        style.configure('bgYellow.TLabel', background=self.ncsYellow)


class SplashScreen:
    def __init__(self, root, file, wait):
        self.__root = root
        self.__file = file
        self.__wait = wait + time.clock()

    def __enter__(self):
        # Hide the root while it is built.
        self.__root.withdraw()
        # Create components of splash screen.
        window = tk.Toplevel(self.__root)
        canvas = tk.Canvas(window)
        splash = tk.PhotoImage(master=window, file=self.__file)
        # Get the screen's width and height.
        scrW = window.winfo_screenwidth()
        scrH = window.winfo_screenheight()
        # Get the images's width and height.
        imgW = splash.width()
        imgH = splash.height()
        # Compute positioning for splash screen.
        Xpos = (scrW - imgW) // 2
        Ypos = (scrH - imgH) // 2
        # Configure the window showing the logo.
        window.overrideredirect(True)
        window.geometry('+{}+{}'.format(Xpos, Ypos))
        # Setup canvas on which image is drawn.
        canvas.configure(width=imgW, height=imgH, highlightthickness=0)
        canvas.grid()
        # Show the splash screen on the monitor.
        canvas.create_image(imgW // 2, imgH // 2, image=splash)
        window.update()
        # Save the variables for later cleanup.
        self.__window = window
        self.__canvas = canvas
        self.__splash = splash

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Ensure that required time has passed.
        now = time.clock()
        if now < self.__wait:
            time.sleep(self.__wait - now)
        # Free used resources in reverse order.
        del self.__splash
        self.__canvas.destroy()
        self.__window.destroy()
        # Give control back to the root program.
        self.__root.update_idletasks()
        self.__root.deiconify()

# -----------------------------------------------------------------------------

if __name__ == '__main__':
    root = tk.Tk()
    Controller(root)
    root.mainloop()