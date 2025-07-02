# PostAnswerWebAppQuery200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**SentWebAppMessage**](SentWebAppMessage.md) |  | 

## Example

```python
from tele_rest.models.post_answer_web_app_query200_response import PostAnswerWebAppQuery200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostAnswerWebAppQuery200Response from a JSON string
post_answer_web_app_query200_response_instance = PostAnswerWebAppQuery200Response.from_json(json)
# print the JSON string representation of the object
print(PostAnswerWebAppQuery200Response.to_json())

# convert the object into a dict
post_answer_web_app_query200_response_dict = post_answer_web_app_query200_response_instance.to_dict()
# create an instance of PostAnswerWebAppQuery200Response from a dict
post_answer_web_app_query200_response_from_dict = PostAnswerWebAppQuery200Response.from_dict(post_answer_web_app_query200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


