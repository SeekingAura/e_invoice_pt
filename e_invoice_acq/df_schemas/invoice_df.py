import pandera as pa
from pandera.typing import Series
from typing import Optional
import pandera.dtypes as pa_dtypes


class InvoiceDF(pa.DataFrameModel):
    sector: Series[str]
    issuer: Series[str]
    invoice_num: Optional[Series[str]]
    _type: Optional[Series[str]]
    issue_date: Series[str]
    total: Series[pa_dtypes.Decimal]
    vat: Series[pa_dtypes.Decimal]
    taxable_base: Series[pa_dtypes.Decimal]
    status: Series[str]
    issuer_communication: Optional[Series[str]]
    acquirer_communication: Optional[Series[str]]
