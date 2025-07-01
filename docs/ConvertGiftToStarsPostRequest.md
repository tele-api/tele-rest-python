# ConvertGiftToStarsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**owned_gift_id** | **str** | Unique identifier of the regular gift that should be converted to Telegram Stars | 

## Example

```python
from tele_rest.models.convert_gift_to_stars_post_request import ConvertGiftToStarsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertGiftToStarsPostRequest from a JSON string
convert_gift_to_stars_post_request_instance = ConvertGiftToStarsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ConvertGiftToStarsPostRequest.to_json())

# convert the object into a dict
convert_gift_to_stars_post_request_dict = convert_gift_to_stars_post_request_instance.to_dict()
# create an instance of ConvertGiftToStarsPostRequest from a dict
convert_gift_to_stars_post_request_from_dict = ConvertGiftToStarsPostRequest.from_dict(convert_gift_to_stars_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


