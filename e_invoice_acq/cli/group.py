from pathlib import Path

from pandera.typing.pandas import DataFrame
import click
from e_invoice_acq.df_read import read_csv_invoices
from e_invoice_acq.df_schemas.invoice_df import InvoiceDF


@click.pass_context
@click.command()
def sector(
    context: click.Context,
):
    df: DataFrame[InvoiceDF] = read_csv_invoices(
        filepath_or_buffer=filepath_in,
    )
    df_sector = df.groupby(
        by=[
            "Sector",
        ]
    ).agg(
        total=("Total", "sum"),
        vat=("VAT", "sum"),
        taxable_base=("taxable_base", "sum"),
    )
    df_sector.to_csv(
        path_or_buf=filepath_out,
    )
