class Customer:
    def __init__(self, cus_name, cus_email, cus_num):
        self.name = cus_name
        self.email = cus_email
        self.num = cus_num

    def cus_info(self):
      return f'{self.name} {self.email} {self.num}'

cus1 = Customer('paul', 'kasava@gmail.com','23434567')
cus1.name = 'brim'
cus1.email = 'gavana@gmail.com'
cus1.num = '24424335'
print(cus1.cus_info())
cus2 = Customer('james', 'havana@gmail.com', '123448889')
print(cus2.cus_info())
