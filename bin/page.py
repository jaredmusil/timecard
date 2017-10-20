from locators import CurrentPayPeriodPageLocators
from locators import MainPageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def click_current_pay_period_button(self):
        self.driver.find_element(*MainPageLocators.CURRENT_PAY_PERIOD).click()


class CurrentPayPeriodPage(BasePage):

    def click_calculate_biweekly_totals_button(self):
        self.driver.find_element(*CurrentPayPeriodPageLocators.CALCULATE_BI_WEEKLY_TOTALS).click()

    def click_week_two_button(self):
        self.driver.find_element(*CurrentPayPeriodPageLocators.SHOW_WEEK_TWO).click()

    def click_save_button(self):
        self.driver.find_element(*CurrentPayPeriodPageLocators.SAVE).click()

    # WEEK 1

    def enter_time_wk1_saturday_in1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SATURDAY_IN1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SATURDAY_IN1).send_keys(entry)

    def enter_time_wk1_sunday_in1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SUNDAY_IN1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SUNDAY_IN1).send_keys(entry)

    def enter_time_wk1_monday_in1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_MONDAY_IN1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_MONDAY_IN1).send_keys(entry)

    def enter_time_wk1_tuesday_in1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_TUESDAY_IN1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_TUESDAY_IN1).send_keys(entry)

    def enter_time_wk1_wednesday_in1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_WEDNESDAY_IN1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_WEDNESDAY_IN1).send_keys(entry)

    def enter_time_wk1_thursday_in1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_THURSDAY_IN1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_THURSDAY_IN1).send_keys(entry)

    def enter_time_wk1_friday_in1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_FRIDAY_IN1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_FRIDAY_IN1).send_keys(entry)

    def enter_time_wk1_saturday_in2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SATURDAY_IN2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SATURDAY_IN2).send_keys(entry)

    def enter_time_wk1_sunday_in2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SUNDAY_IN2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SUNDAY_IN2).send_keys(entry)

    def enter_time_wk1_monday_in2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_MONDAY_IN2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_MONDAY_IN2).send_keys(entry)

    def enter_time_wk1_tuesday_in2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_TUESDAY_IN2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_TUESDAY_IN2).send_keys(entry)

    def enter_time_wk1_wednesday_in2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_WEDNESDAY_IN2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_WEDNESDAY_IN2).send_keys(entry)

    def enter_time_wk1_thursday_in2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_THURSDAY_IN2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_THURSDAY_IN2).send_keys(entry)

    def enter_time_wk1_friday_in2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_FRIDAY_IN2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_FRIDAY_IN2).send_keys(entry)

    def enter_time_wk1_saturday_in3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SATURDAY_IN3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SATURDAY_IN3).send_keys(entry)

    def enter_time_wk1_sunday_in3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SUNDAY_IN3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SUNDAY_IN3).send_keys(entry)

    def enter_time_wk1_monday_in3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_MONDAY_IN3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_MONDAY_IN3).send_keys(entry)

    def enter_time_wk1_tuesday_in3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_TUESDAY_IN3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_TUESDAY_IN3).send_keys(entry)

    def enter_time_wk1_wednesday_in3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_WEDNESDAY_IN3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_WEDNESDAY_IN3).send_keys(entry)

    def enter_time_wk1_thursday_in3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_THURSDAY_IN3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_THURSDAY_IN3).send_keys(entry)

    def enter_time_wk1_friday_in3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_FRIDAY_IN3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_FRIDAY_IN3).send_keys(entry)

    def enter_time_wk1_saturday_in4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SATURDAY_IN4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SATURDAY_IN4).send_keys(entry)

    def enter_time_wk1_sunday_in4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SUNDAY_IN4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SUNDAY_IN4).send_keys(entry)

    def enter_time_wk1_monday_in4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_MONDAY_IN4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_MONDAY_IN4).send_keys(entry)

    def enter_time_wk1_tuesday_in4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_TUESDAY_IN4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_TUESDAY_IN4).send_keys(entry)

    def enter_time_wk1_wednesday_in4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_WEDNESDAY_IN4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_WEDNESDAY_IN4).send_keys(entry)

    def enter_time_wk1_thursday_in4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_THURSDAY_IN4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_THURSDAY_IN4).send_keys(entry)

    def enter_time_wk1_friday_in4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_FRIDAY_IN4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_FRIDAY_IN4).send_keys(entry)

    def enter_time_wk1_saturday_out1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SATURDAY_OUT1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SATURDAY_OUT1).send_keys(entry)

    def enter_time_wk1_sunday_out1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SUNDAY_OUT1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SUNDAY_OUT1).send_keys(entry)

    def enter_time_wk1_monday_out1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_MONDAY_OUT1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_MONDAY_OUT1).send_keys(entry)

    def enter_time_wk1_tuesday_out1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_TUESDAY_OUT1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_TUESDAY_OUT1).send_keys(entry)

    def enter_time_wk1_wednesday_out1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_WEDNESDAY_OUT1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_WEDNESDAY_OUT1).send_keys(entry)

    def enter_time_wk1_thursday_out1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_THURSDAY_OUT1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_THURSDAY_OUT1).send_keys(entry)

    def enter_time_wk1_friday_out1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_FRIDAY_OUT1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_FRIDAY_OUT1).send_keys(entry)

    def enter_time_wk1_saturday_out2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SATURDAY_OUT2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SATURDAY_OUT2).send_keys(entry)

    def enter_time_wk1_sunday_out2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SUNDAY_OUT2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SUNDAY_OUT2).send_keys(entry)

    def enter_time_wk1_monday_out2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_MONDAY_OUT2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_MONDAY_OUT2).send_keys(entry)

    def enter_time_wk1_tuesday_out2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_TUESDAY_OUT2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_TUESDAY_OUT2).send_keys(entry)

    def enter_time_wk1_wednesday_out2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_WEDNESDAY_OUT2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_WEDNESDAY_OUT2).send_keys(entry)

    def enter_time_wk1_thursday_out2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_THURSDAY_OUT2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_THURSDAY_OUT2).send_keys(entry)

    def enter_time_wk1_friday_out2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_FRIDAY_OUT2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_FRIDAY_OUT2).send_keys(entry)

    def enter_time_wk1_saturday_out3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SATURDAY_OUT3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SATURDAY_OUT3).send_keys(entry)

    def enter_time_wk1_sunday_out3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SUNDAY_OUT3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SUNDAY_OUT3).send_keys(entry)

    def enter_time_wk1_monday_out3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_MONDAY_OUT3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_MONDAY_OUT3).send_keys(entry)

    def enter_time_wk1_tuesday_out3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_TUESDAY_OUT3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_TUESDAY_OUT3).send_keys(entry)

    def enter_time_wk1_wednesday_out3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_WEDNESDAY_OUT3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_WEDNESDAY_OUT3).send_keys(entry)

    def enter_time_wk1_thursday_out3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_THURSDAY_OUT3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_THURSDAY_OUT3).send_keys(entry)

    def enter_time_wk1_friday_out3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_FRIDAY_OUT3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_FRIDAY_OUT3).send_keys(entry)

    def enter_time_wk1_saturday_out4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SATURDAY_OUT4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SATURDAY_OUT4).send_keys(entry)

    def enter_time_wk1_sunday_out4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SUNDAY_OUT4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SUNDAY_OUT4).send_keys(entry)

    def enter_time_wk1_monday_out4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_MONDAY_OUT4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_MONDAY_OUT4).send_keys(entry)

    def enter_time_wk1_tuesday_out4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_TUESDAY_OUT4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_TUESDAY_OUT4).send_keys(entry)

    def enter_time_wk1_wednesday_out4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_WEDNESDAY_OUT4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_WEDNESDAY_OUT4).send_keys(entry)

    def enter_time_wk1_thursday_out4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_THURSDAY_OUT4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_THURSDAY_OUT4).send_keys(entry)

    def enter_time_wk1_friday_out4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_FRIDAY_OUT4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_FRIDAY_OUT4).send_keys(entry)

    def enter_time_wk1_saturday_total(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SATURDAY_TOTAL).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SATURDAY_TOTAL).send_keys(entry)

    def enter_time_wk1_sunday_total(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SUNDAY_TOTAL).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_SUNDAY_TOTAL).send_keys(entry)

    def enter_time_wk1_monday_total(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_MONDAY_TOTAL).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_MONDAY_TOTAL).send_keys(entry)

    def enter_time_wk1_tuesday_total(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_TUESDAY_TOTAL).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_TUESDAY_TOTAL).send_keys(entry)

    def enter_time_wk1_wednesday_total(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_WEDNESDAY_TOTAL).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_WEDNESDAY_TOTAL).send_keys(entry)

    def enter_time_wk1_thursday_total(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_THURSDAY_TOTAL).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_THURSDAY_TOTAL).send_keys(entry)

    def enter_time_wk1_friday_total(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_FRIDAY_TOTAL).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK1_FRIDAY_TOTAL).send_keys(entry)

    # WEEK 2

    def enter_time_wk2_saturday_in1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SATURDAY_IN1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SATURDAY_IN1).send_keys(entry)

    def enter_time_wk2_sunday_in1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SUNDAY_IN1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SUNDAY_IN1).send_keys(entry)

    def enter_time_wk2_monday_in1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_MONDAY_IN1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_MONDAY_IN1).send_keys(entry)

    def enter_time_wk2_tuesday_in1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_TUESDAY_IN1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_TUESDAY_IN1).send_keys(entry)

    def enter_time_wk2_wednesday_in1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_WEDNESDAY_IN1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_WEDNESDAY_IN1).send_keys(entry)

    def enter_time_wk2_thursday_in1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_THURSDAY_IN1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_THURSDAY_IN1).send_keys(entry)

    def enter_time_wk2_friday_in1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_FRIDAY_IN1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_FRIDAY_IN1).send_keys(entry)

    def enter_time_wk2_saturday_in2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SATURDAY_IN2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SATURDAY_IN2).send_keys(entry)

    def enter_time_wk2_sunday_in2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SUNDAY_IN2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SUNDAY_IN2).send_keys(entry)

    def enter_time_wk2_monday_in2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_MONDAY_IN2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_MONDAY_IN2).send_keys(entry)

    def enter_time_wk2_tuesday_in2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_TUESDAY_IN2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_TUESDAY_IN2).send_keys(entry)

    def enter_time_wk2_wednesday_in2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_WEDNESDAY_IN2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_WEDNESDAY_IN2).send_keys(entry)

    def enter_time_wk2_thursday_in2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_THURSDAY_IN2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_THURSDAY_IN2).send_keys(entry)

    def enter_time_wk2_friday_in2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_FRIDAY_IN2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_FRIDAY_IN2).send_keys(entry)

    def enter_time_wk2_saturday_in3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SATURDAY_IN3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SATURDAY_IN3).send_keys(entry)

    def enter_time_wk2_sunday_in3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SUNDAY_IN3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SUNDAY_IN3).send_keys(entry)

    def enter_time_wk2_monday_in3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_MONDAY_IN3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_MONDAY_IN3).send_keys(entry)

    def enter_time_wk2_tuesday_in3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_TUESDAY_IN3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_TUESDAY_IN3).send_keys(entry)

    def enter_time_wk2_wednesday_in3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_WEDNESDAY_IN3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_WEDNESDAY_IN3).send_keys(entry)

    def enter_time_wk2_thursday_in3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_THURSDAY_IN3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_THURSDAY_IN3).send_keys(entry)

    def enter_time_wk2_friday_in3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_FRIDAY_IN3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_FRIDAY_IN3).send_keys(entry)

    def enter_time_wk2_saturday_in4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SATURDAY_IN4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SATURDAY_IN4).send_keys(entry)

    def enter_time_wk2_sunday_in4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SUNDAY_IN4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SUNDAY_IN4).send_keys(entry)

    def enter_time_wk2_monday_in4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_MONDAY_IN4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_MONDAY_IN4).send_keys(entry)

    def enter_time_wk2_tuesday_in4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_TUESDAY_IN4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_TUESDAY_IN4).send_keys(entry)

    def enter_time_wk2_wednesday_in4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_WEDNESDAY_IN4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_WEDNESDAY_IN4).send_keys(entry)

    def enter_time_wk2_thursday_in4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_THURSDAY_IN4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_THURSDAY_IN4).send_keys(entry)

    def enter_time_wk2_friday_in4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_FRIDAY_IN4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_FRIDAY_IN4).send_keys(entry)

    def enter_time_wk2_saturday_out1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SATURDAY_OUT1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SATURDAY_OUT1).send_keys(entry)

    def enter_time_wk2_sunday_out1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SUNDAY_OUT1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SUNDAY_OUT1).send_keys(entry)

    def enter_time_wk2_monday_out1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_MONDAY_OUT1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_MONDAY_OUT1).send_keys(entry)

    def enter_time_wk2_tuesday_out1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_TUESDAY_OUT1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_TUESDAY_OUT1).send_keys(entry)

    def enter_time_wk2_wednesday_out1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_WEDNESDAY_OUT1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_WEDNESDAY_OUT1).send_keys(entry)

    def enter_time_wk2_thursday_out1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_THURSDAY_OUT1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_THURSDAY_OUT1).send_keys(entry)

    def enter_time_wk2_friday_out1(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_FRIDAY_OUT1).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_FRIDAY_OUT1).send_keys(entry)

    def enter_time_wk2_saturday_out2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SATURDAY_OUT2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SATURDAY_OUT2).send_keys(entry)

    def enter_time_wk2_sunday_out2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SUNDAY_OUT2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SUNDAY_OUT2).send_keys(entry)

    def enter_time_wk2_monday_out2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_MONDAY_OUT2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_MONDAY_OUT2).send_keys(entry)

    def enter_time_wk2_tuesday_out2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_TUESDAY_OUT2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_TUESDAY_OUT2).send_keys(entry)

    def enter_time_wk2_wednesday_out2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_WEDNESDAY_OUT2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_WEDNESDAY_OUT2).send_keys(entry)

    def enter_time_wk2_thursday_out2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_THURSDAY_OUT2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_THURSDAY_OUT2).send_keys(entry)

    def enter_time_wk2_friday_out2(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_FRIDAY_OUT2).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_FRIDAY_OUT2).send_keys(entry)

    def enter_time_wk2_saturday_out3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SATURDAY_OUT3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SATURDAY_OUT3).send_keys(entry)

    def enter_time_wk2_sunday_out3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SUNDAY_OUT3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SUNDAY_OUT3).send_keys(entry)

    def enter_time_wk2_monday_out3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_MONDAY_OUT3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_MONDAY_OUT3).send_keys(entry)

    def enter_time_wk2_tuesday_out3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_TUESDAY_OUT3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_TUESDAY_OUT3).send_keys(entry)

    def enter_time_wk2_wednesday_out3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_WEDNESDAY_OUT3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_WEDNESDAY_OUT3).send_keys(entry)

    def enter_time_wk2_thursday_out3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_THURSDAY_OUT3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_THURSDAY_OUT3).send_keys(entry)

    def enter_time_wk2_friday_out3(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_FRIDAY_OUT3).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_FRIDAY_OUT3).send_keys(entry)

    def enter_time_wk2_saturday_out4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SATURDAY_OUT4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SATURDAY_OUT4).send_keys(entry)

    def enter_time_wk2_sunday_out4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SUNDAY_OUT4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SUNDAY_OUT4).send_keys(entry)

    def enter_time_wk2_monday_out4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_MONDAY_OUT4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_MONDAY_OUT4).send_keys(entry)

    def enter_time_wk2_tuesday_out4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_TUESDAY_OUT4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_TUESDAY_OUT4).send_keys(entry)

    def enter_time_wk2_wednesday_out4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_WEDNESDAY_OUT4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_WEDNESDAY_OUT4).send_keys(entry)

    def enter_time_wk2_thursday_out4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_THURSDAY_OUT4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_THURSDAY_OUT4).send_keys(entry)

    def enter_time_wk2_friday_out4(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_FRIDAY_OUT4).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_FRIDAY_OUT4).send_keys(entry)

    def enter_time_wk2_saturday_total(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SATURDAY_TOTAL).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SATURDAY_TOTAL).send_keys(entry)

    def enter_time_wk2_sunday_total(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SUNDAY_TOTAL).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_SUNDAY_TOTAL).send_keys(entry)

    def enter_time_wk2_monday_total(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_MONDAY_TOTAL).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_MONDAY_TOTAL).send_keys(entry)

    def enter_time_wk2_tuesday_total(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_TUESDAY_TOTAL).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_TUESDAY_TOTAL).send_keys(entry)

    def enter_time_wk2_wednesday_total(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_WEDNESDAY_TOTAL).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_WEDNESDAY_TOTAL).send_keys(entry)

    def enter_time_wk2_thursday_total(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_THURSDAY_TOTAL).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_THURSDAY_TOTAL).send_keys(entry)

    def enter_time_wk2_friday_total(self, entry):
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_FRIDAY_TOTAL).clear()
        self.driver.find_element(*CurrentPayPeriodPageLocators.WK2_FRIDAY_TOTAL).send_keys(entry)
