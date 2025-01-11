from pathlib import Path

import click
from pandera.typing.pandas import DataFrame

from e_invoice_acq.df_read import read_csv_invoices
from e_invoice_acq.df_schemas.invoice_df import InvoiceDF

from .config import (
    CONFIG_FILE,
    DEFAULT_OUTPUT_DIR,
    load_config,
)
from .group import sector


@click.group()
@click.version_option()
@click.pass_context
@click.option(
    "--config_file",
    "-c",
    "config_file_str",
    default=CONFIG_FILE,
    type=click.Path(
        exists=False,
    ),
)
@click.option(
    "--output_dir",
    "-o",
    "output_dir_str",
    default=None,
    type=click.Path(
        exists=False,
    ),
)
@click.option(
    "--filepath_in",
    "-fi",
    "filepath_in_str",
    type=click.Path(
        exists=True,
    ),
)
def cli(
    context: click.Context,
    config_file_str: str,
    output_dir_str: str | None,
    filepath_in_str: str,
):
    """
    e-factura analyzer
    """
    # cast expected types vars
    config_file: Path = Path(config_file_str)
    filepath_in: Path = Path(filepath_in_str)

    # Set config
    config = load_config(
        config_path=config_file,
    )

    output_path_dir: Path
    # get output dir from command, if not get from config file, then default
    if output_dir_str is None:
        output_path_dir = Path(
            config.get(
                "output_dir",
                DEFAULT_OUTPUT_DIR,
            )
        )

    else:
        output_path_dir = Path(output_dir_str)

    # Read files
    df: DataFrame[InvoiceDF] = read_csv_invoices(
        filepath_or_buffer=filepath_in,
    )

    context.ensure_object(dict)
    context.obj["config"] = config
    context.obj["output_dir"] = output_path_dir


@cli.group()
def group():
    """Configuration options."""
    pass


group.add_command(sector)
