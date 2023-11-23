from decimal import Decimal, getcontext

# Set the maximum number of decimal places
getcontext().prec = 20


def amountToContract(inputAmount: str, asaDecimals: int) -> str:
    return int(Decimal(inputAmount) * (10**asaDecimals))
