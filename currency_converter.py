import requests

class CurrencyConverter:
    API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

    def __init__(self):
        self.rates = self.get_rates()

    def get_rates(self):
        try:
            response = requests.get(self.API_URL)
            response.raise_for_status()
            return response.json()["rates"]
        except Exception as e:
            print("Ошибка загрузки курсов валют:", e)
            return {}

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.rates or to_currency not in self.rates:
            return "Ошибка: Неверный код валюты"
        
        from_rate = self.rates[from_currency]
        to_rate = self.rates[to_currency]

        # Проверка деления на 0
        if from_rate == 0 or to_rate == 0:
            return "Ошибка: Неверный код валюты"
        
        rate = to_rate / from_rate
        return amount * rate


if __name__ == "__main__":
    converter = CurrencyConverter()
    print("Простой конвертер валют")
    amount = float(input("Введите сумму: "))
    from_currency = input("Из какой валюты (например, USD): ").upper()
    to_currency = input("В какую валюту (например, EUR): ").upper()
    result = converter.convert(amount, from_currency, to_currency)
    print(f"Результат: {result}")

