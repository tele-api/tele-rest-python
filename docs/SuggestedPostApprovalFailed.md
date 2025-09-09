# SuggestedPostApprovalFailed

Describes a service message about the failed approval of a suggested post. Currently, only caused by insufficient user funds at the time of approval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggested_post_message** | [**Message**](Message.md) |  | [optional] 
**price** | [**SuggestedPostPrice**](SuggestedPostPrice.md) |  | 

## Example

```python
from tele_rest.models.suggested_post_approval_failed import SuggestedPostApprovalFailed

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestedPostApprovalFailed from a JSON string
suggested_post_approval_failed_instance = SuggestedPostApprovalFailed.from_json(json)
# print the JSON string representation of the object
print(SuggestedPostApprovalFailed.to_json())

# convert the object into a dict
suggested_post_approval_failed_dict = suggested_post_approval_failed_instance.to_dict()
# create an instance of SuggestedPostApprovalFailed from a dict
suggested_post_approval_failed_from_dict = SuggestedPostApprovalFailed.from_dict(suggested_post_approval_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


