from pathlib import Path
from typing import cast

import pandas as pd
from e_invoice_acq.df_apply.clean_money import clean_money_eur
from e_invoice_acq.df_schemas.invoice_df import InvoiceDF
from pandera.typing import DataFrame


def read_csv_invoices(
    filepath_or_buffer: Path,
    money_columns: list[str] = [
        "total",
        "vat",
        "taxable_base",
    ],
    cols: dict[str, str] = {
        "Setor": "sector",
        "Emitente": "issuer",
        "Nº Fatura / ATCUD": "invoice_num",
        "Tipo": "_type",
        "Data Emissão": "issue_date",
        "Total": "total",
        "IVA": "vat",
        "Base Tributável": "taxable_base",
        "Situação": "status",
        "Comunicação  Emitente": "issuer_communication",
        "Comunicação  Adquirente": "acquirer_communication",
    },
) -> DataFrame[InvoiceDF]:
    """
    read CSV invoices data and normalize money values ready for operations,
    the expected column names are
    - "sector": Expected portuguese name "Setor"
    - "issuer": Expected portuguese name "Emitente"
    - "invoice_num": Expected portuguese name "Nº Fatura / ATCUD"
    - "_type": Expected portuguese name "Tipo"
    - "issue_date": Expected portuguese name "Data Emissão"
    - "total": Expected portuguese name "Total"
    - "vat": Expected portuguese name "IVA"
    - "taxable_base": Expected portuguese name "Base Tributável"
    - "status": Expected portuguese name "Situação"
    - "issuer_communication": Expected portuguese name "Comunicação  Emitente"
    - "acquirer_communication": Expected portuguese name "Comunicação  Adquirente"

    money values are "Total", "IVA" and "Base Tributável"

    :param filepath_or_buffer: file path
    :type filepath_or_buffer: Path
    :param money_columns: Columns with money value that requires to be cleaned\
    , defaults to [ "Total", "IVA", "Base Tributável", ]
    :type money_columns: list[str], optional
    :param cols: Col names to be read from the file with the end expected\
    english name
    :type cols: dict[str, str]
    :return: DF normalized
    :rtype: DataFrame[InvoiceDF]
    """
    df: DataFrame[InvoiceDF] = cast(
        DataFrame[InvoiceDF],
        pd.read_csv(
            filepath_or_buffer=filepath_or_buffer,
            sep=";",
            usecols=tuple(cols.keys()),
        ),
    )

    df.rename(
        mapper=cols,
        inplace=True,
    )

    # clean money values, set to numeric values
    df[money_columns] = df[money_columns].apply(clean_money_eur)

    return df
