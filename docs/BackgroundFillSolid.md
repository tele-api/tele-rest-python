# BackgroundFillSolid

The background is filled using the selected color.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the background fill, always “solid” | [default to 'solid']
**color** | **int** | The color of the background fill in the RGB24 format | 

## Example

```python
from tele_rest.models.background_fill_solid import BackgroundFillSolid

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundFillSolid from a JSON string
background_fill_solid_instance = BackgroundFillSolid.from_json(json)
# print the JSON string representation of the object
print(BackgroundFillSolid.to_json())

# convert the object into a dict
background_fill_solid_dict = background_fill_solid_instance.to_dict()
# create an instance of BackgroundFillSolid from a dict
background_fill_solid_from_dict = BackgroundFillSolid.from_dict(background_fill_solid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


