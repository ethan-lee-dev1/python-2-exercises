class TaxMan:
    def __init__(self, list, percent):
        self.list = list
        self.percent = float(percent.strip('%')) / 100
        self.total = 0
        
    def calc_total(self):
        total_price = 0
        for item in self.list:
            total_price += item["price"]
        tax_amount = total_price * self.percent
        self.total = total_price + tax_amount
        
    def get_total(self):
        return self.total
