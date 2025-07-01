# UniqueGiftBackdropColors

This object describes the colors of the backdrop of a unique gift.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**center_color** | **int** | The color in the center of the backdrop in RGB format | 
**edge_color** | **int** | The color on the edges of the backdrop in RGB format | 
**symbol_color** | **int** | The color to be applied to the symbol in RGB format | 
**text_color** | **int** | The color for the text on the backdrop in RGB format | 

## Example

```python
from tele_rest.models.unique_gift_backdrop_colors import UniqueGiftBackdropColors

# TODO update the JSON string below
json = "{}"
# create an instance of UniqueGiftBackdropColors from a JSON string
unique_gift_backdrop_colors_instance = UniqueGiftBackdropColors.from_json(json)
# print the JSON string representation of the object
print(UniqueGiftBackdropColors.to_json())

# convert the object into a dict
unique_gift_backdrop_colors_dict = unique_gift_backdrop_colors_instance.to_dict()
# create an instance of UniqueGiftBackdropColors from a dict
unique_gift_backdrop_colors_from_dict = UniqueGiftBackdropColors.from_dict(unique_gift_backdrop_colors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


