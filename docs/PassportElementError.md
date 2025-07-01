# PassportElementError

This object represents an error in the Telegram Passport element which was submitted that should be resolved by the user. It should be one of:  * [PassportElementErrorDataField](https://core.telegram.org/bots/api/#passportelementerrordatafield) * [PassportElementErrorFrontSide](https://core.telegram.org/bots/api/#passportelementerrorfrontside) * [PassportElementErrorReverseSide](https://core.telegram.org/bots/api/#passportelementerrorreverseside) * [PassportElementErrorSelfie](https://core.telegram.org/bots/api/#passportelementerrorselfie) * [PassportElementErrorFile](https://core.telegram.org/bots/api/#passportelementerrorfile) * [PassportElementErrorFiles](https://core.telegram.org/bots/api/#passportelementerrorfiles) * [PassportElementErrorTranslationFile](https://core.telegram.org/bots/api/#passportelementerrortranslationfile) * [PassportElementErrorTranslationFiles](https://core.telegram.org/bots/api/#passportelementerrortranslationfiles) * [PassportElementErrorUnspecified](https://core.telegram.org/bots/api/#passportelementerrorunspecified)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Error source, must be *unspecified* | [default to 'unspecified']
**type** | **str** | Type of element of the user&#39;s Telegram Passport which has the issue | 
**field_name** | **str** | Name of the data field which has the error | 
**data_hash** | **str** | Base64-encoded data hash | 
**message** | **str** | Error message | 
**file_hash** | **str** | Base64-encoded file hash | 
**file_hashes** | **List[str]** | List of base64-encoded file hashes | 
**element_hash** | **str** | Base64-encoded element hash | 

## Example

```python
from tele_rest.models.passport_element_error import PassportElementError

# TODO update the JSON string below
json = "{}"
# create an instance of PassportElementError from a JSON string
passport_element_error_instance = PassportElementError.from_json(json)
# print the JSON string representation of the object
print(PassportElementError.to_json())

# convert the object into a dict
passport_element_error_dict = passport_element_error_instance.to_dict()
# create an instance of PassportElementError from a dict
passport_element_error_from_dict = PassportElementError.from_dict(passport_element_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


