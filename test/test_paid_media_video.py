# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.1.0
- **Modified**: 2025-07-05T02:41:43.458230827Z[Etc/UTC]
- **Generator Version**: 7.14.0

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


import unittest

from tele_rest.models.paid_media_video import PaidMediaVideo

class TestPaidMediaVideo(unittest.TestCase):
    """PaidMediaVideo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaidMediaVideo:
        """Test PaidMediaVideo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaidMediaVideo`
        """
        model = PaidMediaVideo()
        if include_optional:
            return PaidMediaVideo(
                type = 'video',
                video = tele_rest.models.video.Video(
                    file_id = '', 
                    file_unique_id = '', 
                    width = 56, 
                    height = 56, 
                    duration = 56, 
                    thumbnail = tele_rest.models.photo_size.PhotoSize(
                        file_id = '', 
                        file_unique_id = '', 
                        width = 56, 
                        height = 56, 
                        file_size = 56, ), 
                    cover = [
                        tele_rest.models.photo_size.PhotoSize(
                            file_id = '', 
                            file_unique_id = '', 
                            width = 56, 
                            height = 56, 
                            file_size = 56, )
                        ], 
                    start_timestamp = 56, 
                    file_name = '', 
                    mime_type = '', 
                    file_size = 56, )
            )
        else:
            return PaidMediaVideo(
                type = 'video',
                video = tele_rest.models.video.Video(
                    file_id = '', 
                    file_unique_id = '', 
                    width = 56, 
                    height = 56, 
                    duration = 56, 
                    thumbnail = tele_rest.models.photo_size.PhotoSize(
                        file_id = '', 
                        file_unique_id = '', 
                        width = 56, 
                        height = 56, 
                        file_size = 56, ), 
                    cover = [
                        tele_rest.models.photo_size.PhotoSize(
                            file_id = '', 
                            file_unique_id = '', 
                            width = 56, 
                            height = 56, 
                            file_size = 56, )
                        ], 
                    start_timestamp = 56, 
                    file_name = '', 
                    mime_type = '', 
                    file_size = 56, ),
        )
        """

    def testPaidMediaVideo(self):
        """Test PaidMediaVideo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
