class Phone:
    def __init__(phone , ph_name, ph_ram, ph_gig):
        phone.name = ph_name
        phone.ram = ph_ram
        phone.gig = ph_gig

    def ph_info(phone):
      return f'{phone.name} {phone.ram} {phone.gig}'

ph1 = Phone('samsung','4GB', '128GB')
print(ph1.ph_info())
















