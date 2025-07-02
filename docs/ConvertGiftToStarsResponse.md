# ConvertGiftToStarsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.convert_gift_to_stars_response import ConvertGiftToStarsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertGiftToStarsResponse from a JSON string
convert_gift_to_stars_response_instance = ConvertGiftToStarsResponse.from_json(json)
# print the JSON string representation of the object
print(ConvertGiftToStarsResponse.to_json())

# convert the object into a dict
convert_gift_to_stars_response_dict = convert_gift_to_stars_response_instance.to_dict()
# create an instance of ConvertGiftToStarsResponse from a dict
convert_gift_to_stars_response_from_dict = ConvertGiftToStarsResponse.from_dict(convert_gift_to_stars_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


