# BackgroundFillGradient

The background is a gradient fill.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the background fill, always “gradient” | [default to 'gradient']
**top_color** | **int** | Top color of the gradient in the RGB24 format | 
**bottom_color** | **int** | Bottom color of the gradient in the RGB24 format | 
**rotation_angle** | **int** | Clockwise rotation angle of the background fill in degrees; 0-359 | 

## Example

```python
from tele_rest.models.background_fill_gradient import BackgroundFillGradient

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundFillGradient from a JSON string
background_fill_gradient_instance = BackgroundFillGradient.from_json(json)
# print the JSON string representation of the object
print(BackgroundFillGradient.to_json())

# convert the object into a dict
background_fill_gradient_dict = background_fill_gradient_instance.to_dict()
# create an instance of BackgroundFillGradient from a dict
background_fill_gradient_from_dict = BackgroundFillGradient.from_dict(background_fill_gradient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


