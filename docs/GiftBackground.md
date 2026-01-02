# GiftBackground

This object describes the background of a gift.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**center_color** | **int** | Center color of the background in RGB format | 
**edge_color** | **int** | Edge color of the background in RGB format | 
**text_color** | **int** | Text color of the background in RGB format | 

## Example

```python
from tele_rest.models.gift_background import GiftBackground

# TODO update the JSON string below
json = "{}"
# create an instance of GiftBackground from a JSON string
gift_background_instance = GiftBackground.from_json(json)
# print the JSON string representation of the object
print(GiftBackground.to_json())

# convert the object into a dict
gift_background_dict = gift_background_instance.to_dict()
# create an instance of GiftBackground from a dict
gift_background_from_dict = GiftBackground.from_dict(gift_background_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


