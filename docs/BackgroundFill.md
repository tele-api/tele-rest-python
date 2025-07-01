# BackgroundFill

This object describes the way a background is filled based on the selected colors. Currently, it can be one of  * [BackgroundFillSolid](https://core.telegram.org/bots/api/#backgroundfillsolid) * [BackgroundFillGradient](https://core.telegram.org/bots/api/#backgroundfillgradient) * [BackgroundFillFreeformGradient](https://core.telegram.org/bots/api/#backgroundfillfreeformgradient)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the background fill, always “freeform\\_gradient” | [default to 'freeform_gradient']
**color** | **int** | The color of the background fill in the RGB24 format | 
**top_color** | **int** | Top color of the gradient in the RGB24 format | 
**bottom_color** | **int** | Bottom color of the gradient in the RGB24 format | 
**rotation_angle** | **int** | Clockwise rotation angle of the background fill in degrees; 0-359 | 
**colors** | **List[int]** | A list of the 3 or 4 base colors that are used to generate the freeform gradient in the RGB24 format | 

## Example

```python
from tele_rest.models.background_fill import BackgroundFill

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundFill from a JSON string
background_fill_instance = BackgroundFill.from_json(json)
# print the JSON string representation of the object
print(BackgroundFill.to_json())

# convert the object into a dict
background_fill_dict = background_fill_instance.to_dict()
# create an instance of BackgroundFill from a dict
background_fill_from_dict = BackgroundFill.from_dict(background_fill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


