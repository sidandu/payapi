class payment_methods:
    def __init__(self, data):
        # all the methods uses self.data for payment proessing
        self.data = data
        
    def select_payment_gateway(self):
        amount = float(self.data['amount'])
        print(amount)
        if amount <= 20:    #as per the assignment, there is no case to handle 20, so i included so as well here
            self.__cheap_payment_gateway()
        elif amount > 20 and amount < 500:
            self.__expensive_payment_gateway()
        else:
            for i in range(3):
                self.__premium_payment_gateway()
                #if payment is successful -> break
                #else wait for some time sleep(20) and retry
            
    def __cheap_payment_gateway(self):
        print("CHEAP payment gateway integration goes here...")
        
    def __expensive_payment_gateway(self):
        try:
            raise
            print("EXPENSIVE payment gateway integration goes here..")
            #Raise exception if expensive payment gateway is unavailable
        except:
            print("EXPENSIVE payment gateway unavailable..")
            self.__cheap_payment_gateway()
            
    def __premium_payment_gateway(self):
        print("PREMIUM payment gateway integration goes here..")