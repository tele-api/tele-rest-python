# CreateInvoiceLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **str** |  | 

## Example

```python
from tele_rest.models.create_invoice_link_response import CreateInvoiceLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceLinkResponse from a JSON string
create_invoice_link_response_instance = CreateInvoiceLinkResponse.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceLinkResponse.to_json())

# convert the object into a dict
create_invoice_link_response_dict = create_invoice_link_response_instance.to_dict()
# create an instance of CreateInvoiceLinkResponse from a dict
create_invoice_link_response_from_dict = CreateInvoiceLinkResponse.from_dict(create_invoice_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


