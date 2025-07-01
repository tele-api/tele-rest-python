# OwnedGifts

Contains the list of gifts received and owned by a user or a chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of gifts owned by the user or the chat | 
**gifts** | [**List[OwnedGift]**](OwnedGift.md) | The list of gifts | 
**next_offset** | **str** | *Optional*. Offset for the next request. If empty, then there are no more results | [optional] 

## Example

```python
from tele_rest.models.owned_gifts import OwnedGifts

# TODO update the JSON string below
json = "{}"
# create an instance of OwnedGifts from a JSON string
owned_gifts_instance = OwnedGifts.from_json(json)
# print the JSON string representation of the object
print(OwnedGifts.to_json())

# convert the object into a dict
owned_gifts_dict = owned_gifts_instance.to_dict()
# create an instance of OwnedGifts from a dict
owned_gifts_from_dict = OwnedGifts.from_dict(owned_gifts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


