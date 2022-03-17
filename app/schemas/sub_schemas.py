from flask_restx import Namespace, fields


api = Namespace("invoices", description="Invoices related operations")


BillingPeriod = api.model("BillingPeriod", {
    'From': fields.String(required=True, description="Billing period from"),
    'To': fields.String(required=True, description="Billing period to"),
    'InvoiceAuthorization': fields.String(required=True, description="Invoice authorization"),
    'StartDate': fields.String(required=True, description="Start date"),
    'EndDate': fields.String(required=True, description="End date"),
})


Additional = api.model("Additional", {
      'CreateBy': fields.String(description="Create by"),
      'UpdateBy': fields.String(description="Update by"),
      'CUFE': fields.String(required=True, description="CUFE"),
      'Contingency': fields.String(required=True, description="Contingency"),
      'SendEmail': fields.Boolean(required=True, description="Send email"),
      'DianSoftwareId': fields.String(required=True, description="Dian software id"),
      'DianPin': fields.String(required=True, description="Dian pin"),
      'DianTechnicalKey': fields.String(required=True, description="Dian technical key"),
      'DianTestSetId': fields.String(required=True, description="Dian test set id"),
      'ProfileExecutionId': fields.String(required=True, description="Profile execution id"),
})


PaymentMeans = api.model("PaymentMean", {
    'Code': fields.String(required=True, description="Code"),
    'Mean': fields.String(required=True, description="Mean"),
    'DueDate': fields.String(required=True, description="Due date"),
})


IdentificationIssuer = api.model("Identification", {
    'DocumentNumber': fields.String(required=True, description="Document number"),
    'DocumentType': fields.String(required=True, description="Document type"),
    'CountryCode': fields.String(required=True, description="Country code"),
    'CheckDigit': fields.String(required=True, description="Check digit"),
})
AddressIssuer = api.model("Address", {
    'DepartmentCode': fields.String(required=True, description="Department code"),
    'DepartmentName': fields.String(required=True, description="Department name"),
    'CityCode': fields.String(required=True, description="City code"),
    'CityName': fields.String(required=True, description="City name"),
    'AddressLine': fields.String(required=True, description="Address line"),
    'PostalCode': fields.String(required=True, description="Postal code"),
    'Country': fields.String(required=True, description="Country"),
})
IssuerParty = api.model("IssuerParty", {
    'LegalType': fields.String(required=True, description="Legal type"),
    'Identification': fields.Nested(IdentificationIssuer),
    'Name': fields.String(required=True, description="Name"),
    'Email': fields.String(required=True, description="Email"),
    'Address': fields.Nested(AddressIssuer),
    'TaxScheme': fields.String(required=True, description="Tax scheme"),
    'ResponsabilityTypes': fields.String(required=True, description="Responsability types")
})


AddressCustomer = api.model("AddressCustomer", {
    'DepartmentCode': fields.String(required=True, description="Department code"),
    'DepartmentName': fields.String(required=True, description="Department name"),
    'CityCode': fields.String(required=True, description="City code"),
    'CityName': fields.String(required=True, description="City name"),
    'AddressLine': fields.String(required=True, description="Address line"),
    'PostalCode': fields.String(required=True, description="Postal code"),
    'Country': fields.String(required=True, description="Country"),
})
IdentificationCustomer = api.model("IdentificationCustomer", {
    'DocumentNumber': fields.String(required=True, description="Document number"),
    'DocumentType': fields.String(required=True, description="Document type"),
    'CountryCode': fields.String(required=True, description="Country code"),
    'CheckDigit': fields.String(required=True, description="Check digit"),
})
CustommerDocumentContacts = api.model("DocumentContacts", {
    'Name': fields.String(required=True, description="Name"),
    'Type': fields.String(required=True, description="Type"),
    'Telephone': fields.String(required=True, description="Telephone"),
})
CustomerParty = api.model("CustomerParty", {
    'TeleFax': fields.String(required=True, description="Telefax"),
    'DocumentContacts': fields.List(fields.Nested(CustommerDocumentContacts)),
    'LegalType': fields.String(required=True, description="Legal type"),
    'Identification': fields.Nested(IdentificationCustomer),
    'Name': fields.String(required=True, description="Name"),
    'Email': fields.String(required=True, description="Email"),
    'Address': fields.Nested(AddressCustomer),
    'TaxScheme': fields.String(required=True, description="Tax scheme"),
    'ResponsabilityTypes': fields.List(fields.String(required=True, description="Responsability types")),
})


LinesWithholdingTaxTotal = api.model("WithholdingTaxTotal", {
    'WithholdingTaxCategory': fields.String(required=True, description="Withholding tax category"),
    'TaxAmount': fields.String(required=True, description="Tax amount"),
    'TaxableAmount': fields.String(required=True, description="Taxable amount"),
})
LinesWithholdingTaxSubTotal = api.model("WithholdingTaxSubTotal", {
    'WithholdingTaxCategory': fields.String(required=True, description="Withholding tax category"),
    'TaxPercentage': fields.String(required=True, description="Tax percentage"),
    'TaxableAmount': fields.String(required=True, description="Taxable amount"),
    'TaxAmount': fields.String(required=True, description="Tax amount"),
})
LinesItem = api.model("Item", {
    'SellerItemIdentification': fields.String(required=True, description="Seller item identification"),
    'Description': fields.String(required=True, description="Description"),
    'IncomePurposeCode': fields.String(required=True, description="Income purpose code"),
    'UnitsPerPackage': fields.String(required=True, description="Units per package"),
    'BrandName': fields.String(required=True, description="Brand name"),
    'ModelName': fields.String(required=True, description="Model name"),
})
LinesAllowanceCharge = api.model("AllowanceCharge", {
    'ChargeIndicator': fields.String(required=True, description="Charge indicator"),
    'BaseAmount': fields.String(required=True, description="Base amount"),
    'ReasonCode': fields.String(required=True, description="Reason code"),
    'Reason': fields.String(required=True, description="Reason"),
    'Amount': fields.String(required=True, description="Amount"),
    'Percentage': fields.String(required=True, description="Percentage"),
    'SequenceIndicator': fields.String(required=True, description="Sequence indicator"),
})
LinesTaxTotal = api.model("TaxTotal", {
    'TaxCategory': fields.String(required=True, description="Tax category"),
    'TaxAmount': fields.String(required=True, description="Tax amount"),
    'RoundingAmount': fields.String(required=True, description="Rounding amount"),
})
LinesTaxSubTotal = api.model("TaxSubTotal", {
    'TaxableAmount': fields.String(required=True, description="Taxable amount"),
    'TaxCategory': fields.String(required=True, description="Tax category"),
    'TaxPercentage': fields.String(required=True, description="Tax percentage"),
    'PerUnitAmount': fields.String(required=True, description="Per unit amount"),
    'TaxAmount': fields.String(required=True, description="Tax amount"),
})
LinesDes = api.model("LineDes", {
    'Number': fields.String(required=True, description="Number"),
    'Quantity': fields.String(required=True, description="Quantity"),
    'QuantityUnitOfMeasure': fields.String(required=True, description="Quantity unit of measure"),
    'TaxSubTotals': fields.List(fields.Nested(LinesTaxSubTotal)),
    'TaxTotals': fields.List(fields.Nested(LinesTaxTotal)),
    'UnitPrice': fields.String(required=True, description="Unit price"),
    'GrossAmount': fields.String(required=True, description="Gross amount"),
    'NetAmount': fields.String(required=True, description="Net amount"),
    'AllowanceCharges': fields.List(fields.Nested(LinesAllowanceCharge)),
    'Item': fields.Nested(LinesItem),
    'WithholdingTaxSubTotals': fields.List(fields.Nested(LinesWithholdingTaxSubTotal)),
    'WithholdingTaxTotals': fields.List(fields.Nested(LinesWithholdingTaxTotal)),
})


TaxSubTotals = api.model("TaxSubTotals", {
    'TaxCategory': fields.String(required=True, description="Tax category"),
    'TaxPercentage': fields.String(required=True, description="Tax percentage"),
    'TaxableAmount': fields.String(required=True, description="Taxable amount"),
    'TaxAmount': fields.String(required=True, description="Tax amount"),
})


WithholdingTaxSubTotals = api.model("WithholdingTaxSubTotals", {
    'WithholdingTaxCategory': fields.String(required=True, description="Withholding tax category"),
    'TaxPercentage': fields.String(required=True, description="Tax percentage"),
    'TaxableAmount': fields.String(required=True, description="Taxable amount"),
    'TaxAmount': fields.String(required=True, description="Tax amount"),
})


AllowanceCharges = api.model("AllowanceCharges", {
    'ChargeIndicator': fields.String(required=True, description="Charge indicator"),
    'BaseAmount': fields.String(required=True, description="Base amount"),
    'ReasonCode': fields.String(required=True, description="Reason code"),
    'Reason': fields.String(required=True, description="Reason"),
    'Amount': fields.String(required=True, description="Amount"),
    'Percentage': fields.String(required=True, description="Percentage"),
    'SequenceIndicator': fields.String(required=True, description="Sequence indicator"),
})


TaxTotals = api.model("TaxTotals", {
    'TaxCategory': fields.String(required=True, description="Tax category"),
    'TaxAmount': fields.String(required=True, description="Tax amount"),
    'RoundingAmount': fields.String(required=True, description="Rounding amount"),
})


WithholdingTaxTotals = api.model("WithholdingTaxTotals", {
    'WithholdingTaxCategory': fields.String(required=True, description="Withholding tax category"),
    'TaxAmount': fields.String(required=True, description="Tax amount"),
})


Total = api.model("Total", {
    'GrossAmount': fields.String(required=True, description="Gross amount"),
    'TotalBillableAmount': fields.String(required=True, description="Total billable amount"),
    'PayableAmount': fields.String(required=True, description="Payable amount"),
    'TaxableAmount': fields.String(required=True, description="Taxable amount"),
    'AllowancesTotalAmount': fields.String(required=True, description="Allowances total amount"),
    'ChargesTotalAmount': fields.String(required=True, description="Charges total amount"),
    'PrePaidTotalAmount': fields.String(required=True, description="Pre paid total amount"),
    'TotalIva': fields.String(required=True, description="Total iva"),
    'TotalIca': fields.String(required=True, description="Total ica"),
    'TotalTaxConsume': fields.String(required=True, description="Total tax consume"),
})


DocumentReferences = api.model("DocumentReferences", {
    'DocumentReferred': fields.String(required=True, description="Document referred"),
    'IssueDate': fields.String(required=True, description="Issue date"),
    'Type': fields.String(required=True, description="Type"),
    'OtherReferenceTypeId': fields.String(required=True, description="Other reference type id"),
    'OtherReferenceTypeDescription': fields.String(required=True, description="Other reference type description"),
    'DocumentReferredCUFE': fields.String(required=True, description="Document referred CUFE"),
})

IdentificationAdditionalCustomers = api.model("IdentificationAdditionalCustomers", {
    'DocumentNumber': fields.String(required=True, description="Document number"),
    'DocumentType': fields.String(required=True, description="Document type"),
    'CountryCode': fields.String(required=True, description="Country code"),
    'CheckDigit': fields.String(required=True, description="Check digit"),
})
AdditionalCustomer = api.model("AdditionalCustomers", {
    'Name': fields.String(required=True, description="Name"),
    'CommercialRegistrationNumber': fields.String(required=True, description="Commercial registration number"),
    'Identification': fields.Nested(IdentificationAdditionalCustomers),
    'ParticipationPercentage': fields.String(required=True, description="Participation percentage"),
})


PdfData = api.model("PdfData", {
    'Pdf': fields.String(required=True, description="Pdf"),
})
