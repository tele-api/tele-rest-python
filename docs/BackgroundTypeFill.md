# BackgroundTypeFill

The background is automatically filled based on the selected colors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the background, always “fill” | [default to 'fill']
**fill** | [**BackgroundFill**](BackgroundFill.md) |  | 
**dark_theme_dimming** | **int** | Dimming of the background in dark themes, as a percentage; 0-100 | 

## Example

```python
from tele_rest.models.background_type_fill import BackgroundTypeFill

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundTypeFill from a JSON string
background_type_fill_instance = BackgroundTypeFill.from_json(json)
# print the JSON string representation of the object
print(BackgroundTypeFill.to_json())

# convert the object into a dict
background_type_fill_dict = background_type_fill_instance.to_dict()
# create an instance of BackgroundTypeFill from a dict
background_type_fill_from_dict = BackgroundTypeFill.from_dict(background_type_fill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


