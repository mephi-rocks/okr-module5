import unittest
from currency_converter import CurrencyConverter

class TestCurrencyConverter(unittest.TestCase):
    def setUp(self):
        # Создаем экземпляр CurrencyConverter и подменяем курсы валют
        self.converter = CurrencyConverter()
        self.converter.rates = {
            "USD": 1.0,
            "EUR": 0.85,
            "JPY": 110.0,
            "RUB": 75.0,
        }

    def test_conversion_usd_to_eur(self):
        result = self.converter.convert(100, "USD", "EUR")
        self.assertAlmostEqual(result, 85.0)

    def test_conversion_eur_to_usd(self):
        result = self.converter.convert(85, "EUR", "USD")
        self.assertAlmostEqual(result, 100.0)

    def test_conversion_usd_to_jpy(self):
        result = self.converter.convert(10, "USD", "JPY")
        self.assertAlmostEqual(result, 1100.0)

    def test_conversion_invalid_currency(self):
        result = self.converter.convert(100, "USD", "XXX")
        self.assertEqual(result, "Ошибка: Неверный код валюты")

    def test_conversion_zero_amount(self):
        result = self.converter.convert(0, "USD", "EUR")
        self.assertEqual(result, 0.0)

    def test_division_by_zero_rate(self):
        # Устанавливаем курс EUR равным 0
        self.converter.rates["EUR"] = 0
        result = self.converter.convert(100, "USD", "EUR")
        self.assertEqual(result, "Ошибка: Неверный код валюты")

if __name__ == "__main__":
    unittest.main()

