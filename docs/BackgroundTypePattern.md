# BackgroundTypePattern

The background is a .PNG or .TGV (gzipped subset of SVG with MIME type “application/x-tgwallpattern”) pattern to be combined with the background fill chosen by the user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the background, always “pattern” | [default to 'pattern']
**document** | [**Document**](Document.md) |  | 
**fill** | [**BackgroundFill**](BackgroundFill.md) |  | 
**intensity** | **int** | Intensity of the pattern when it is shown above the filled background; 0-100 | 
**is_inverted** | **bool** | *Optional*. *True*, if the background fill must be applied only to the pattern itself. All other pixels are black in this case. For dark themes only | [optional] [default to True]
**is_moving** | **bool** | *Optional*. *True*, if the background moves slightly when the device is tilted | [optional] [default to True]

## Example

```python
from tele_rest.models.background_type_pattern import BackgroundTypePattern

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundTypePattern from a JSON string
background_type_pattern_instance = BackgroundTypePattern.from_json(json)
# print the JSON string representation of the object
print(BackgroundTypePattern.to_json())

# convert the object into a dict
background_type_pattern_dict = background_type_pattern_instance.to_dict()
# create an instance of BackgroundTypePattern from a dict
background_type_pattern_from_dict = BackgroundTypePattern.from_dict(background_type_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


