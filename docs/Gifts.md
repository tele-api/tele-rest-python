# Gifts

This object represent a list of gifts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gifts** | [**List[Gift]**](Gift.md) | The list of gifts | 

## Example

```python
from tele_rest.models.gifts import Gifts

# TODO update the JSON string below
json = "{}"
# create an instance of Gifts from a JSON string
gifts_instance = Gifts.from_json(json)
# print the JSON string representation of the object
print(Gifts.to_json())

# convert the object into a dict
gifts_dict = gifts_instance.to_dict()
# create an instance of Gifts from a dict
gifts_from_dict = Gifts.from_dict(gifts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


