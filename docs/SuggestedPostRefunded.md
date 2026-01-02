# SuggestedPostRefunded

Describes a service message about a payment refund for a suggested post.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggested_post_message** | [**Message**](Message.md) |  | [optional] 
**reason** | **str** | Reason for the refund. Currently, one of “post\\_deleted” if the post was deleted within 24 hours of being posted or removed from scheduled messages without being posted, or “payment\\_refunded” if the payer refunded their payment. | 

## Example

```python
from tele_rest.models.suggested_post_refunded import SuggestedPostRefunded

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestedPostRefunded from a JSON string
suggested_post_refunded_instance = SuggestedPostRefunded.from_json(json)
# print the JSON string representation of the object
print(SuggestedPostRefunded.to_json())

# convert the object into a dict
suggested_post_refunded_dict = suggested_post_refunded_instance.to_dict()
# create an instance of SuggestedPostRefunded from a dict
suggested_post_refunded_from_dict = SuggestedPostRefunded.from_dict(suggested_post_refunded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


