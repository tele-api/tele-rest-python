# UniqueGiftColors

This object contains information about the color scheme for a user's name, message replies and link previews based on a unique gift.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_custom_emoji_id** | **str** | Custom emoji identifier of the unique gift&#39;s model | 
**symbol_custom_emoji_id** | **str** | Custom emoji identifier of the unique gift&#39;s symbol | 
**light_theme_main_color** | **int** | Main color used in light themes; RGB format | 
**light_theme_other_colors** | **List[int]** | List of 1-3 additional colors used in light themes; RGB format | 
**dark_theme_main_color** | **int** | Main color used in dark themes; RGB format | 
**dark_theme_other_colors** | **List[int]** | List of 1-3 additional colors used in dark themes; RGB format | 

## Example

```python
from tele_rest.models.unique_gift_colors import UniqueGiftColors

# TODO update the JSON string below
json = "{}"
# create an instance of UniqueGiftColors from a JSON string
unique_gift_colors_instance = UniqueGiftColors.from_json(json)
# print the JSON string representation of the object
print(UniqueGiftColors.to_json())

# convert the object into a dict
unique_gift_colors_dict = unique_gift_colors_instance.to_dict()
# create an instance of UniqueGiftColors from a dict
unique_gift_colors_from_dict = UniqueGiftColors.from_dict(unique_gift_colors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


