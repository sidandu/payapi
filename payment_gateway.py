class PaymentMethods:
    def __init__(self, data):
        '''
        all the methods uses self.data for payment processing
        '''
        self.data = data
        
    def select_payment_gateway(self):
        '''
        Selects the payment gateway based on business condition and make the payment and returns payment status
        :return:Payment status (Currently there is no return value as it is dummy method)
        '''
        amount = float(self.data['amount'])
        print(amount)
        # as per the requirements, there is no case to handle 20, so i included 20 as well here
        if amount <= 20:
            self.__cheap_payment_gateway()
        elif amount > 20 and amount < 500:
            self.__expensive_payment_gateway()
        else:
            for i in range(3):
                self.__premium_payment_gateway()
                #if payment is successful -> break
                #else wait for some time sleep(20) and retry
            
    def __cheap_payment_gateway(self):
        '''
        Process the payment by using cheap payment gateway
        :return: payment status
        '''
        print("CHEAP payment gateway integration goes here...")
        
    def __expensive_payment_gateway(self):
        '''
        Process the payment using expensive payment gateway
        :return: payment status
        '''
        try:
            raise
            print("EXPENSIVE payment gateway integration goes here..")
            #Raise exception if expensive payment gateway is unavailable
        except:
            print("EXPENSIVE payment gateway unavailable..")
            self.__cheap_payment_gateway()
            
    def __premium_payment_gateway(self):
        '''
        Process the payment using premium payment gateway
        :return: payment status
        '''
        print("PREMIUM payment gateway integration goes here..")