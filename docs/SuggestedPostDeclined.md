# SuggestedPostDeclined

Describes a service message about the rejection of a suggested post.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggested_post_message** | [**Message**](Message.md) |  | [optional] 
**comment** | **str** | *Optional*. Comment with which the post was declined | [optional] 

## Example

```python
from tele_rest.models.suggested_post_declined import SuggestedPostDeclined

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestedPostDeclined from a JSON string
suggested_post_declined_instance = SuggestedPostDeclined.from_json(json)
# print the JSON string representation of the object
print(SuggestedPostDeclined.to_json())

# convert the object into a dict
suggested_post_declined_dict = suggested_post_declined_instance.to_dict()
# create an instance of SuggestedPostDeclined from a dict
suggested_post_declined_from_dict = SuggestedPostDeclined.from_dict(suggested_post_declined_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


