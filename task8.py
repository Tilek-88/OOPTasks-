class MoneyFmt:
    def init(self, value=0.0): 
        self.value = float(value)
    def str(self):
        if self.value >= 0:
            return '${:,.2f}'.format(self.value)
        else:
            return '-${:,.2f}'.format(-self.value)
    def update(self, value=None):
        self.value=value
    def repr(self):
        print(self.value)
        return f'{self.value}'
cash = MoneyFmt(12345678.021)
cash.update(100000.4567)
cash.update(-0.3)
print(cash)
repr(cash)