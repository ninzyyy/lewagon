# pylint: disable=missing-docstring

# TODO: add some currency rates
RATES = {"USDEUR":0.85, "GBPEUR":1.13, "CHFEUR":0.86, "EURGBP":0.885}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    conversion_string = amount[1] + currency.upper()
    if conversion_string in RATES:
        converted_amount = round(RATES[conversion_string] * amount[0])
        return converted_amount
    return None
