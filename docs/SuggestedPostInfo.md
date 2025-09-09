# SuggestedPostInfo

Contains information about a suggested post.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | State of the suggested post. Currently, it can be one of “pending”, “approved”, “declined”. | 
**price** | [**SuggestedPostPrice**](SuggestedPostPrice.md) |  | [optional] 
**send_date** | **int** | *Optional*. Proposed send date of the post. If the field is omitted, then the post can be published at any time within 30 days at the sole discretion of the user or administrator who approves it. | [optional] 

## Example

```python
from tele_rest.models.suggested_post_info import SuggestedPostInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestedPostInfo from a JSON string
suggested_post_info_instance = SuggestedPostInfo.from_json(json)
# print the JSON string representation of the object
print(SuggestedPostInfo.to_json())

# convert the object into a dict
suggested_post_info_dict = suggested_post_info_instance.to_dict()
# create an instance of SuggestedPostInfo from a dict
suggested_post_info_from_dict = SuggestedPostInfo.from_dict(suggested_post_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


