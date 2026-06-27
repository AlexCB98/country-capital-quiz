class CountryQuestion:

    def __init__(self, country, capital, answer):
        self.country = country
        self.capital = capital
        self.answer = answer

    def __str__(self):
        return (f'Country : {self.country}\n'
                f'Capital: {self.capital}\n'
                f'Answer: {self.answer}')