from flask_restx import Namespace, fields
from .sub_schemas import api
from .sub_schemas import (
   BillingPeriod,
   Additional,
   PaymentMeans,
   IssuerParty,
   CustomerParty,
   LinesDes,
   TaxSubTotals,
   WithholdingTaxSubTotals,
   AllowanceCharges,
   TaxTotals,
   WithholdingTaxTotals,
   Total,
   DocumentReferences,
   AdditionalCustomer,
   PdfData,
)


InvoiceModel = api.model(
    "Invoice",
{
   'BillingPeriod': fields.Nested(BillingPeriod),
   'Additional': fields.Nested(Additional),
   'SeriePrefix': fields.String(required=True, description="Serie prefix"),
   'SerieNumber': fields.String(required=True, description="Serie number"),
   'IssueDate': fields.String(required=True, description="Issue date"),
   'DueDate': fields.String(required=True, description="Due date"),
   'IssueTime': fields.String(required=True, description="Issue time"),
   'CorrelationDocumentId': fields.String(required=True, description="Correlation document id"),
   'SerieExternalKey': fields.String(required=True, description="Serie external key"),
   'DeliveryDate': fields.String(required=True, description="DeliveryDate"),
   'DeliveryTime': fields.String(required=True, description="Delivery time"),
   'PaymentMeans': fields.List(fields.Nested(PaymentMeans)),
   'IssuerParty': fields.Nested(IssuerParty),
   'CustomerParty': fields.Nested(CustomerParty),
   'Currency': fields.String(required=True, description="Currency"),
   'OperationType': fields.String(required=True, description="Operation type"),
   'Lines': fields.List(fields.Nested(LinesDes)),
   'TaxSubTotals': fields.List(fields.Nested(TaxSubTotals)),
   'WithholdingTaxSubTotals': fields.List(fields.Nested(WithholdingTaxSubTotals)),
   'AllowanceCharges': fields.List(fields.Nested(AllowanceCharges)),
   'TaxTotals': fields.List(fields.Nested(TaxTotals)),
   'WithholdingTaxTotals': fields.List(fields.Nested(WithholdingTaxTotals)),
   'Total': fields.Nested(Total),
   'DocumentReferences': fields.List(fields.Nested(DocumentReferences)),
   'AdditionalCustomers': fields.List(fields.Nested(AdditionalCustomer)),
   'PdfData': fields.Nested(PdfData),
})
