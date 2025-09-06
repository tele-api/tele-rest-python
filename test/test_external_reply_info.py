# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.2.0
- **Modified**: 2025-09-06T05:32:06.285336202Z[Etc/UTC]
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

from tele_rest.models.external_reply_info import ExternalReplyInfo

class TestExternalReplyInfo(unittest.TestCase):
    """ExternalReplyInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExternalReplyInfo:
        """Test ExternalReplyInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExternalReplyInfo`
        """
        model = ExternalReplyInfo()
        if include_optional:
            return ExternalReplyInfo(
                origin = None,
                chat = tele_rest.models.chat.Chat(
                    id = 56, 
                    type = 'private', 
                    title = '', 
                    username = '', 
                    first_name = '', 
                    last_name = '', 
                    is_forum = True, 
                    is_direct_messages = True, ),
                message_id = 56,
                link_preview_options = tele_rest.models.link_preview_options.LinkPreviewOptions(
                    is_disabled = True, 
                    url = '', 
                    prefer_small_media = True, 
                    prefer_large_media = True, 
                    show_above_text = True, ),
                animation = tele_rest.models.animation.Animation(
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
                    file_name = '', 
                    mime_type = '', 
                    file_size = 56, ),
                audio = tele_rest.models.audio.Audio(
                    file_id = '', 
                    file_unique_id = '', 
                    duration = 56, 
                    performer = '', 
                    title = '', 
                    file_name = '', 
                    mime_type = '', 
                    file_size = 56, 
                    thumbnail = tele_rest.models.photo_size.PhotoSize(
                        file_id = '', 
                        file_unique_id = '', 
                        width = 56, 
                        height = 56, 
                        file_size = 56, ), ),
                document = tele_rest.models.document.Document(
                    file_id = '', 
                    file_unique_id = '', 
                    thumbnail = tele_rest.models.photo_size.PhotoSize(
                        file_id = '', 
                        file_unique_id = '', 
                        width = 56, 
                        height = 56, 
                        file_size = 56, ), 
                    file_name = '', 
                    mime_type = '', 
                    file_size = 56, ),
                paid_media = tele_rest.models.paid_media_info.PaidMediaInfo(
                    star_count = 56, 
                    paid_media = [
                        null
                        ], ),
                photo = [
                    tele_rest.models.photo_size.PhotoSize(
                        file_id = '', 
                        file_unique_id = '', 
                        width = 56, 
                        height = 56, 
                        file_size = 56, )
                    ],
                sticker = tele_rest.models.sticker.Sticker(
                    file_id = '', 
                    file_unique_id = '', 
                    type = 'regular', 
                    width = 56, 
                    height = 56, 
                    is_animated = True, 
                    is_video = True, 
                    thumbnail = tele_rest.models.photo_size.PhotoSize(
                        file_id = '', 
                        file_unique_id = '', 
                        width = 56, 
                        height = 56, 
                        file_size = 56, ), 
                    emoji = '', 
                    set_name = '', 
                    premium_animation = tele_rest.models.file.File(
                        file_id = '', 
                        file_unique_id = '', 
                        file_size = 56, 
                        file_path = '', ), 
                    mask_position = tele_rest.models.mask_position.MaskPosition(
                        point = 'forehead', 
                        x_shift = 1.337, 
                        y_shift = 1.337, 
                        scale = 1.337, ), 
                    custom_emoji_id = '', 
                    needs_repainting = True, 
                    file_size = 56, ),
                story = tele_rest.models.story.Story(
                    chat = tele_rest.models.chat.Chat(
                        id = 56, 
                        type = 'private', 
                        title = '', 
                        username = '', 
                        first_name = '', 
                        last_name = '', 
                        is_forum = True, 
                        is_direct_messages = True, ), 
                    id = 56, ),
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
                video_note = tele_rest.models.video_note.VideoNote(
                    file_id = '', 
                    file_unique_id = '', 
                    length = 56, 
                    duration = 56, 
                    thumbnail = tele_rest.models.photo_size.PhotoSize(
                        file_id = '', 
                        file_unique_id = '', 
                        width = 56, 
                        height = 56, 
                        file_size = 56, ), 
                    file_size = 56, ),
                voice = tele_rest.models.voice.Voice(
                    file_id = '', 
                    file_unique_id = '', 
                    duration = 56, 
                    mime_type = '', 
                    file_size = 56, ),
                has_media_spoiler = True,
                checklist = tele_rest.models.checklist.Checklist(
                    title = '', 
                    title_entities = [
                        tele_rest.models.message_entity.MessageEntity(
                            type = 'mention', 
                            offset = 56, 
                            length = 56, 
                            url = '', 
                            user = tele_rest.models.user.User(
                                id = 56, 
                                is_bot = True, 
                                first_name = '', 
                                last_name = '', 
                                username = '', 
                                language_code = '', 
                                is_premium = True, 
                                added_to_attachment_menu = True, 
                                can_join_groups = True, 
                                can_read_all_group_messages = True, 
                                supports_inline_queries = True, 
                                can_connect_to_business = True, 
                                has_main_web_app = True, ), 
                            language = '', 
                            custom_emoji_id = '', )
                        ], 
                    tasks = [
                        tele_rest.models.checklist_task.ChecklistTask(
                            id = 56, 
                            text = '', 
                            text_entities = [
                                tele_rest.models.message_entity.MessageEntity(
                                    type = 'mention', 
                                    offset = 56, 
                                    length = 56, 
                                    url = '', 
                                    language = '', 
                                    custom_emoji_id = '', )
                                ], 
                            completed_by_user = tele_rest.models.user.User(
                                id = 56, 
                                is_bot = True, 
                                first_name = '', 
                                last_name = '', 
                                username = '', 
                                language_code = '', 
                                is_premium = True, 
                                added_to_attachment_menu = True, 
                                can_join_groups = True, 
                                can_read_all_group_messages = True, 
                                supports_inline_queries = True, 
                                can_connect_to_business = True, 
                                has_main_web_app = True, ), 
                            completion_date = 56, )
                        ], 
                    others_can_add_tasks = True, 
                    others_can_mark_tasks_as_done = True, ),
                contact = tele_rest.models.contact.Contact(
                    phone_number = '', 
                    first_name = '', 
                    last_name = '', 
                    user_id = 56, 
                    vcard = '', ),
                dice = tele_rest.models.dice.Dice(
                    emoji = '', 
                    value = 56, ),
                game = tele_rest.models.game.Game(
                    title = '', 
                    description = '', 
                    photo = [
                        tele_rest.models.photo_size.PhotoSize(
                            file_id = '', 
                            file_unique_id = '', 
                            width = 56, 
                            height = 56, 
                            file_size = 56, )
                        ], 
                    text = '', 
                    text_entities = [
                        tele_rest.models.message_entity.MessageEntity(
                            type = 'mention', 
                            offset = 56, 
                            length = 56, 
                            url = '', 
                            user = tele_rest.models.user.User(
                                id = 56, 
                                is_bot = True, 
                                first_name = '', 
                                last_name = '', 
                                username = '', 
                                language_code = '', 
                                is_premium = True, 
                                added_to_attachment_menu = True, 
                                can_join_groups = True, 
                                can_read_all_group_messages = True, 
                                supports_inline_queries = True, 
                                can_connect_to_business = True, 
                                has_main_web_app = True, ), 
                            language = '', 
                            custom_emoji_id = '', )
                        ], 
                    animation = tele_rest.models.animation.Animation(
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
                        file_name = '', 
                        mime_type = '', 
                        file_size = 56, ), ),
                giveaway = tele_rest.models.giveaway.Giveaway(
                    chats = [
                        tele_rest.models.chat.Chat(
                            id = 56, 
                            type = 'private', 
                            title = '', 
                            username = '', 
                            first_name = '', 
                            last_name = '', 
                            is_forum = True, 
                            is_direct_messages = True, )
                        ], 
                    winners_selection_date = 56, 
                    winner_count = 56, 
                    only_new_members = True, 
                    has_public_winners = True, 
                    prize_description = '', 
                    country_codes = [
                        ''
                        ], 
                    prize_star_count = 56, 
                    premium_subscription_month_count = 56, ),
                giveaway_winners = tele_rest.models.giveaway_winners.GiveawayWinners(
                    chat = tele_rest.models.chat.Chat(
                        id = 56, 
                        type = 'private', 
                        title = '', 
                        username = '', 
                        first_name = '', 
                        last_name = '', 
                        is_forum = True, 
                        is_direct_messages = True, ), 
                    giveaway_message_id = 56, 
                    winners_selection_date = 56, 
                    winner_count = 56, 
                    winners = [
                        tele_rest.models.user.User(
                            id = 56, 
                            is_bot = True, 
                            first_name = '', 
                            last_name = '', 
                            username = '', 
                            language_code = '', 
                            is_premium = True, 
                            added_to_attachment_menu = True, 
                            can_join_groups = True, 
                            can_read_all_group_messages = True, 
                            supports_inline_queries = True, 
                            can_connect_to_business = True, 
                            has_main_web_app = True, )
                        ], 
                    additional_chat_count = 56, 
                    prize_star_count = 56, 
                    premium_subscription_month_count = 56, 
                    unclaimed_prize_count = 56, 
                    only_new_members = True, 
                    was_refunded = True, 
                    prize_description = '', ),
                invoice = tele_rest.models.invoice.Invoice(
                    title = '', 
                    description = '', 
                    start_parameter = '', 
                    currency = '', 
                    total_amount = 56, ),
                location = tele_rest.models.location.Location(
                    latitude = 1.337, 
                    longitude = 1.337, 
                    horizontal_accuracy = 1.337, 
                    live_period = 56, 
                    heading = 56, 
                    proximity_alert_radius = 56, ),
                poll = tele_rest.models.poll.Poll(
                    id = '', 
                    question = '0', 
                    question_entities = [
                        tele_rest.models.message_entity.MessageEntity(
                            type = 'mention', 
                            offset = 56, 
                            length = 56, 
                            url = '', 
                            user = tele_rest.models.user.User(
                                id = 56, 
                                is_bot = True, 
                                first_name = '', 
                                last_name = '', 
                                username = '', 
                                language_code = '', 
                                is_premium = True, 
                                added_to_attachment_menu = True, 
                                can_join_groups = True, 
                                can_read_all_group_messages = True, 
                                supports_inline_queries = True, 
                                can_connect_to_business = True, 
                                has_main_web_app = True, ), 
                            language = '', 
                            custom_emoji_id = '', )
                        ], 
                    options = [
                        tele_rest.models.poll_option.PollOption(
                            text = '0', 
                            text_entities = [
                                tele_rest.models.message_entity.MessageEntity(
                                    type = 'mention', 
                                    offset = 56, 
                                    length = 56, 
                                    url = '', 
                                    language = '', 
                                    custom_emoji_id = '', )
                                ], 
                            voter_count = 56, )
                        ], 
                    total_voter_count = 56, 
                    is_closed = True, 
                    is_anonymous = True, 
                    type = 'regular', 
                    allows_multiple_answers = True, 
                    correct_option_id = 56, 
                    explanation = '', 
                    explanation_entities = [
                        
                        ], 
                    open_period = 56, 
                    close_date = 56, ),
                venue = tele_rest.models.venue.Venue(
                    location = tele_rest.models.location.Location(
                        latitude = 1.337, 
                        longitude = 1.337, 
                        horizontal_accuracy = 1.337, 
                        live_period = 56, 
                        heading = 56, 
                        proximity_alert_radius = 56, ), 
                    title = '', 
                    address = '', 
                    foursquare_id = '', 
                    foursquare_type = '', 
                    google_place_id = '', 
                    google_place_type = '', )
            )
        else:
            return ExternalReplyInfo(
                origin = None,
        )
        """

    def testExternalReplyInfo(self):
        """Test ExternalReplyInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
