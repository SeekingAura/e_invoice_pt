from decimal import Decimal

from pandera.typing import Series


def clean_money_eur(column: Series[str]) -> Series[Decimal]:  # type: ignore
    """
    Set money values how numeric values, ready for numeric operations, remove
    symbols (on this case €), replace comma "," with dots (decimal point) and
    set data type Decimal (best for financial case)

    :param column: Income raw money value
    :type column: Series[str]
    :return: cleaned money series
    :rtype: Series[Decimal]
    """
    return column.str.replace("€", "").str.replace(",", ".").str.strip().apply(Decimal)  # type: ignore
