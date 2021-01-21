import requests
import calendar
from datetime import datetime

class payment_input_validator:
    def __init__(self, data):
        # all the methods uses self.data for payment proessing
        self.data = data

    def __sum_digits(self, digit):
        if digit < 10:
            return digit
        else:
            sum = (digit % 10) + (digit // 10)
            return sum

    def __validate(self, cc_num):
        # reverse the credit card number
        cc_num = cc_num[::-1]
        # convert to integer list
        cc_num = [int(x) for x in cc_num]
        # double every second digit
        doubled_second_digit_list = list()
        digits = list(enumerate(cc_num, start=1))
        for index, digit in digits:
            if index % 2 == 0:
                doubled_second_digit_list.append(digit * 2)
            else:
                doubled_second_digit_list.append(digit)

        # add the digits if any number is more than 9
        doubled_second_digit_list = [self.__sum_digits(x) for x in doubled_second_digit_list]
        # sum all digits
        sum_of_digits = sum(doubled_second_digit_list)
        # return True or False
        return sum_of_digits % 10 == 0

    # Request data validation
    def validate_payment_info(self):
        print(self.data)
        data_check = {}
        
        #Input keys validation
        in_keys = list(self.data.keys())
        if 'card_cvv' in in_keys:
            #CVV number validation
            try:
                if len(str(self.data['card_cvv']))==3:
                    if int(self.data['card_cvv']) < 0:
                        data_check['card_cvv'] = "cvv number should be positive number"
                else:
                    data_check['card_cvv'] = "ccv number should be 3 digit"
            except ValueError:
                data_check['card_cvv'] = "Invalid CVV"
            in_keys.remove('card_cvv')
            
        if in_keys == ['card_number', 'card_holder', 'card_expiry', 'amount']:
            #card number validatio
            if str(self.data['card_number']).isnumeric():
                if not self.__validate(str(self.data['card_number'])):
                    data_check['card_number'] = "Invalid card Number"
            else:
                data_check['card_number'] = "Card number should be Numeric"
                
            # Card expiry date validation
            if "-" in self.data['card_expiry']:
                expiry_dt = self.data['card_expiry'].split("-")
                expiry_y = int(expiry_dt[1])
                expiry_m = int(expiry_dt[0])
                expiry_d = calendar.monthrange(expiry_y,expiry_m)[1]
                if datetime(expiry_y,expiry_m,expiry_d) < datetime.now():
                    data_check['card_expiry'] = "Expiry date cannot be past"           
            else:
                data_check['card_expiry'] = "Invalid Expiry date format"
                
            #Transaction amount validation
            try:
                if float(self.data['amount']) <= 0:
                    data_check['amount'] = "Amount should be positive number, greater than 0"
            except ValueError:
                data_check['amount'] = "Invalid amount"
            
            #Card holder name validation
            if not self.data['card_holder'].replace(" ", "").isalpha():
                data_check['card_holder'] = "Invalid card holder name"

        return data_check
