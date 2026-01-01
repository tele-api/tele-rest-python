# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2026 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.3.0
- **Modified**: 2026-01-01T02:06:09.762570119Z[Etc/UTC]
- **Generator Version**: 7.18.0

<details>
<summary><strong>⚠️ Important Disclaimer & Limitation of Liability</strong></summary>
<br>
> **IMPORTANT**: This software is provided "as is" without any warranties, express or implied, including but not limited
> to warranties of merchantability, fitness for a particular purpose, or non-infringement. The developers, contributors,
> and licensors (collectively, "Developers") make no representations regarding the accuracy, completeness, or reliability
> of this software or its outputs.
>
> This client is not intended to provide financial, investment, tax, or legal advice. It facilitates interaction with the
> Telegram Bot API service but does not endorse or recommend any financial actions, including the purchase, sale, or holding of
> financial instruments (e.g., stocks, bonds, derivatives, cryptocurrencies). Users must consult qualified financial or
> legal professionals before making decisions based on this software's outputs.
>
> Financial markets are inherently speculative and carry significant risks. Using this software in trading, analysis, or
> other financial activities may result in substantial losses, including total loss of capital. The Developers are not
> liable for any losses or damages arising from such use. Users assume full responsibility for validating the software's
> outputs and ensuring their suitability for intended purposes.
>
> This client may rely on third-party data or services (e.g., market feeds, APIs). The Developers do not control or verify
> the accuracy of these services and are not liable for any errors, delays, or losses resulting from their use. Users must
> comply with third-party terms and conditions.
>
> Users are solely responsible for ensuring compliance with all applicable financial, tax, and regulatory requirements in
> their jurisdiction. This includes obtaining necessary licenses or approvals for trading or investment activities. The
> Developers disclaim liability for any legal consequences arising from non-compliance.
>
> To the fullest extent permitted by law, the Developers shall not be liable for any direct, indirect, incidental,
> consequential, or punitive damages arising from the use or inability to use this software, including but not limited to
> loss of profits, data, or business opportunities.

</details>
"""  # noqa: E501

from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from tele_rest.models.passport_element_error_data_field import PassportElementErrorDataField
from tele_rest.models.passport_element_error_file import PassportElementErrorFile
from tele_rest.models.passport_element_error_files import PassportElementErrorFiles
from tele_rest.models.passport_element_error_front_side import PassportElementErrorFrontSide
from tele_rest.models.passport_element_error_reverse_side import PassportElementErrorReverseSide
from tele_rest.models.passport_element_error_selfie import PassportElementErrorSelfie
from tele_rest.models.passport_element_error_translation_file import PassportElementErrorTranslationFile
from tele_rest.models.passport_element_error_translation_files import PassportElementErrorTranslationFiles
from tele_rest.models.passport_element_error_unspecified import PassportElementErrorUnspecified
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

PASSPORTELEMENTERROR_ONE_OF_SCHEMAS = ["PassportElementErrorDataField", "PassportElementErrorFile", "PassportElementErrorFiles", "PassportElementErrorFrontSide", "PassportElementErrorReverseSide", "PassportElementErrorSelfie", "PassportElementErrorTranslationFile", "PassportElementErrorTranslationFiles", "PassportElementErrorUnspecified"]

class PassportElementError(BaseModel):
    """
    This object represents an error in the Telegram Passport element which was submitted that should be resolved by the user. It should be one of:  * [PassportElementErrorDataField](https://core.telegram.org/bots/api/#passportelementerrordatafield) * [PassportElementErrorFrontSide](https://core.telegram.org/bots/api/#passportelementerrorfrontside) * [PassportElementErrorReverseSide](https://core.telegram.org/bots/api/#passportelementerrorreverseside) * [PassportElementErrorSelfie](https://core.telegram.org/bots/api/#passportelementerrorselfie) * [PassportElementErrorFile](https://core.telegram.org/bots/api/#passportelementerrorfile) * [PassportElementErrorFiles](https://core.telegram.org/bots/api/#passportelementerrorfiles) * [PassportElementErrorTranslationFile](https://core.telegram.org/bots/api/#passportelementerrortranslationfile) * [PassportElementErrorTranslationFiles](https://core.telegram.org/bots/api/#passportelementerrortranslationfiles) * [PassportElementErrorUnspecified](https://core.telegram.org/bots/api/#passportelementerrorunspecified)
    """
    # data type: PassportElementErrorDataField
    oneof_schema_1_validator: Optional[PassportElementErrorDataField] = None
    # data type: PassportElementErrorFrontSide
    oneof_schema_2_validator: Optional[PassportElementErrorFrontSide] = None
    # data type: PassportElementErrorReverseSide
    oneof_schema_3_validator: Optional[PassportElementErrorReverseSide] = None
    # data type: PassportElementErrorSelfie
    oneof_schema_4_validator: Optional[PassportElementErrorSelfie] = None
    # data type: PassportElementErrorFile
    oneof_schema_5_validator: Optional[PassportElementErrorFile] = None
    # data type: PassportElementErrorFiles
    oneof_schema_6_validator: Optional[PassportElementErrorFiles] = None
    # data type: PassportElementErrorTranslationFile
    oneof_schema_7_validator: Optional[PassportElementErrorTranslationFile] = None
    # data type: PassportElementErrorTranslationFiles
    oneof_schema_8_validator: Optional[PassportElementErrorTranslationFiles] = None
    # data type: PassportElementErrorUnspecified
    oneof_schema_9_validator: Optional[PassportElementErrorUnspecified] = None
    actual_instance: Optional[Union[PassportElementErrorDataField, PassportElementErrorFile, PassportElementErrorFiles, PassportElementErrorFrontSide, PassportElementErrorReverseSide, PassportElementErrorSelfie, PassportElementErrorTranslationFile, PassportElementErrorTranslationFiles, PassportElementErrorUnspecified]] = None
    one_of_schemas: Set[str] = { "PassportElementErrorDataField", "PassportElementErrorFile", "PassportElementErrorFiles", "PassportElementErrorFrontSide", "PassportElementErrorReverseSide", "PassportElementErrorSelfie", "PassportElementErrorTranslationFile", "PassportElementErrorTranslationFiles", "PassportElementErrorUnspecified" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = PassportElementError.model_construct()
        error_messages = []
        match = 0
        # validate data type: PassportElementErrorDataField
        if not isinstance(v, PassportElementErrorDataField):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PassportElementErrorDataField`")
        else:
            match += 1
        # validate data type: PassportElementErrorFrontSide
        if not isinstance(v, PassportElementErrorFrontSide):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PassportElementErrorFrontSide`")
        else:
            match += 1
        # validate data type: PassportElementErrorReverseSide
        if not isinstance(v, PassportElementErrorReverseSide):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PassportElementErrorReverseSide`")
        else:
            match += 1
        # validate data type: PassportElementErrorSelfie
        if not isinstance(v, PassportElementErrorSelfie):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PassportElementErrorSelfie`")
        else:
            match += 1
        # validate data type: PassportElementErrorFile
        if not isinstance(v, PassportElementErrorFile):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PassportElementErrorFile`")
        else:
            match += 1
        # validate data type: PassportElementErrorFiles
        if not isinstance(v, PassportElementErrorFiles):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PassportElementErrorFiles`")
        else:
            match += 1
        # validate data type: PassportElementErrorTranslationFile
        if not isinstance(v, PassportElementErrorTranslationFile):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PassportElementErrorTranslationFile`")
        else:
            match += 1
        # validate data type: PassportElementErrorTranslationFiles
        if not isinstance(v, PassportElementErrorTranslationFiles):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PassportElementErrorTranslationFiles`")
        else:
            match += 1
        # validate data type: PassportElementErrorUnspecified
        if not isinstance(v, PassportElementErrorUnspecified):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PassportElementErrorUnspecified`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in PassportElementError with oneOf schemas: PassportElementErrorDataField, PassportElementErrorFile, PassportElementErrorFiles, PassportElementErrorFrontSide, PassportElementErrorReverseSide, PassportElementErrorSelfie, PassportElementErrorTranslationFile, PassportElementErrorTranslationFiles, PassportElementErrorUnspecified. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in PassportElementError with oneOf schemas: PassportElementErrorDataField, PassportElementErrorFile, PassportElementErrorFiles, PassportElementErrorFrontSide, PassportElementErrorReverseSide, PassportElementErrorSelfie, PassportElementErrorTranslationFile, PassportElementErrorTranslationFiles, PassportElementErrorUnspecified. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into PassportElementErrorDataField
        try:
            instance.actual_instance = PassportElementErrorDataField.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PassportElementErrorFrontSide
        try:
            instance.actual_instance = PassportElementErrorFrontSide.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PassportElementErrorReverseSide
        try:
            instance.actual_instance = PassportElementErrorReverseSide.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PassportElementErrorSelfie
        try:
            instance.actual_instance = PassportElementErrorSelfie.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PassportElementErrorFile
        try:
            instance.actual_instance = PassportElementErrorFile.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PassportElementErrorFiles
        try:
            instance.actual_instance = PassportElementErrorFiles.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PassportElementErrorTranslationFile
        try:
            instance.actual_instance = PassportElementErrorTranslationFile.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PassportElementErrorTranslationFiles
        try:
            instance.actual_instance = PassportElementErrorTranslationFiles.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PassportElementErrorUnspecified
        try:
            instance.actual_instance = PassportElementErrorUnspecified.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into PassportElementError with oneOf schemas: PassportElementErrorDataField, PassportElementErrorFile, PassportElementErrorFiles, PassportElementErrorFrontSide, PassportElementErrorReverseSide, PassportElementErrorSelfie, PassportElementErrorTranslationFile, PassportElementErrorTranslationFiles, PassportElementErrorUnspecified. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into PassportElementError with oneOf schemas: PassportElementErrorDataField, PassportElementErrorFile, PassportElementErrorFiles, PassportElementErrorFrontSide, PassportElementErrorReverseSide, PassportElementErrorSelfie, PassportElementErrorTranslationFile, PassportElementErrorTranslationFiles, PassportElementErrorUnspecified. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], PassportElementErrorDataField, PassportElementErrorFile, PassportElementErrorFiles, PassportElementErrorFrontSide, PassportElementErrorReverseSide, PassportElementErrorSelfie, PassportElementErrorTranslationFile, PassportElementErrorTranslationFiles, PassportElementErrorUnspecified]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


