
class CurrencyConverter:
    def __init__(self, exchange_rate=0.7757):

        self.exchange_rate = exchange_rate

    def convert_to_usd(self, amount_in_gbp):

        return amount_in_gbp / self.exchange_rate

    def convert_to_gbp(self, amount_in_usd):

        return amount_in_usd * self.exchange_rate



converter = CurrencyConverter()



sumof = int(input("How many pounds would you like to convert to dollars: "))

amount_in_usd = converter.convert_to_usd(sumof)
print(f"£{sumof} is approximately ${amount_in_usd:} USD")