# SuggestedPostApproved

Describes a service message about the approval of a suggested post.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggested_post_message** | [**Message**](Message.md) |  | [optional] 
**price** | [**SuggestedPostPrice**](SuggestedPostPrice.md) |  | [optional] 
**send_date** | **int** | Date when the post will be published | 

## Example

```python
from tele_rest.models.suggested_post_approved import SuggestedPostApproved

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestedPostApproved from a JSON string
suggested_post_approved_instance = SuggestedPostApproved.from_json(json)
# print the JSON string representation of the object
print(SuggestedPostApproved.to_json())

# convert the object into a dict
suggested_post_approved_dict = suggested_post_approved_instance.to_dict()
# create an instance of SuggestedPostApproved from a dict
suggested_post_approved_from_dict = SuggestedPostApproved.from_dict(suggested_post_approved_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


