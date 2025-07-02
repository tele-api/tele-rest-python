# EditUserStarSubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.edit_user_star_subscription_response import EditUserStarSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditUserStarSubscriptionResponse from a JSON string
edit_user_star_subscription_response_instance = EditUserStarSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(EditUserStarSubscriptionResponse.to_json())

# convert the object into a dict
edit_user_star_subscription_response_dict = edit_user_star_subscription_response_instance.to_dict()
# create an instance of EditUserStarSubscriptionResponse from a dict
edit_user_star_subscription_response_from_dict = EditUserStarSubscriptionResponse.from_dict(edit_user_star_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


