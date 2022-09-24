
# forignToIQD = float( Amount)* float(currency.sell_price)

# IQDtoForign = float(amount)/float(currency.buy_price)



from cgitb import reset


def foreing_to_local(price, buy_price):
    """
        from the company's propective, a customer is selling a foreing currency
        when he brought a foreing currency, and the company are buying the foreing currency
        therefor it's a buying transaction for them
    """
    # tx type -> buy
    result = float(price)* float(buy_price)
    return result


def local_to_foreing(price, sell_price):
    """
        from the company's propective, a customer is buying a foreing currency
        when he brought a local currency, and the company are selling the foreing currency
        there for it's a selling transaction for them
    """
    # tx type -> sell
    result = float(price)/float(sell_price)
    return result


