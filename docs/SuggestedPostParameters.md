# SuggestedPostParameters

Contains parameters of a post that is being suggested by the bot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | [**SuggestedPostPrice**](SuggestedPostPrice.md) |  | [optional] 
**send_date** | **int** | *Optional*. Proposed send date of the post. If specified, then the date must be between 300 second and 2678400 seconds (30 days) in the future. If the field is omitted, then the post can be published at any time within 30 days at the sole discretion of the user who approves it. | [optional] 

## Example

```python
from tele_rest.models.suggested_post_parameters import SuggestedPostParameters

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestedPostParameters from a JSON string
suggested_post_parameters_instance = SuggestedPostParameters.from_json(json)
# print the JSON string representation of the object
print(SuggestedPostParameters.to_json())

# convert the object into a dict
suggested_post_parameters_dict = suggested_post_parameters_instance.to_dict()
# create an instance of SuggestedPostParameters from a dict
suggested_post_parameters_from_dict = SuggestedPostParameters.from_dict(suggested_post_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


