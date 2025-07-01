# BackgroundFillFreeformGradient

The background is a freeform gradient that rotates after every message in the chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the background fill, always “freeform\\_gradient” | [default to 'freeform_gradient']
**colors** | **List[int]** | A list of the 3 or 4 base colors that are used to generate the freeform gradient in the RGB24 format | 

## Example

```python
from tele_rest.models.background_fill_freeform_gradient import BackgroundFillFreeformGradient

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundFillFreeformGradient from a JSON string
background_fill_freeform_gradient_instance = BackgroundFillFreeformGradient.from_json(json)
# print the JSON string representation of the object
print(BackgroundFillFreeformGradient.to_json())

# convert the object into a dict
background_fill_freeform_gradient_dict = background_fill_freeform_gradient_instance.to_dict()
# create an instance of BackgroundFillFreeformGradient from a dict
background_fill_freeform_gradient_from_dict = BackgroundFillFreeformGradient.from_dict(background_fill_freeform_gradient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


