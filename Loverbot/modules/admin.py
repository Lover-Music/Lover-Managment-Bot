import html

from telegram import ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
from telegram.utils.helpers import mention_html

from Razerbot import DRAGONS, dispatcher
from Razerbot.modules.disable import DisableAbleCommandHandler
from Razerbot.modules.helper_funcs.chat_status import (
    bot_admin,
    can_pin,
    can_promote,
    connection_status,
    user_admin,
    ADMIN_CACHE,
)
from Razerbot.modules.helper_funcs.admin_rights import user_can_changeinfo
from Razerbot.modules.helper_funcs.extraction import (
    extract_user,
    extract_user_and_text,
)
from Razerbot.modules.log_channel import loggable
from Razerbot.modules.helper_funcs.alternate import send_message
from Razerbot.modules.helper_funcs.alternate import typing_action


@run_async
@connection_status
@bot_admin
@can_promote
@user_admin
@loggable
def promote(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    args = context.args

    message = update.effective_message
    chat = update.effective_chat
    user = update.effective_user

    promoter = chat.get_member(user.id)

    if (
        not (promoter.can_promote_members or promoter.status == "creator")
        and user.id not in DRAGONS
    ):
        message.reply_text("ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ɴᴇᴄᴇssᴀʀʏ ʀɪɢʜᴛs ᴛᴏ ᴅᴏ ᴛʜᴀᴛ!")
        return

    user_id = extract_user(message, args)

    if not user_id:
        message.reply_text(
            "ʏᴏᴜ ᴅᴏɴ'ᴛ sᴇᴇᴍ ᴛᴏ ʙᴇ ʀᴇꜰᴇʀʀɪɴɢ ᴛᴏ ᴀ ᴜsᴇʀ ᴏʀ ᴛʜᴇ ɪᴅ sᴘᴇᴄɪꜰɪᴇᴅ ɪs ɪɴᴄᴏʀʀᴇᴄᴛ.."
        )
        return

    try:
        user_member = chat.get_member(user_id)
    except:
        return

    if user_member.status == "administrator" or user_member.status == "creator":
        message.reply_text("ʜᴏᴡ ᴀᴍ ɪ ᴍᴇᴀɴᴛ ᴛᴏ ᴘʀᴏᴍᴏᴛᴇ sᴏᴍᴇᴏɴᴇ ᴛʜᴀᴛ's ᴀʟʀᴇᴀᴅʏ ᴀɴ ᴀᴅᴍɪɴ?")
        return

    if user_id == bot.id:
        message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴘʀᴏᴍᴏᴛᴇ ᴍʏsᴇʟꜰ! ɢᴇᴛ ᴀɴ ᴀᴅᴍɪɴ ᴛᴏ ᴅᴏ ɪᴛ ꜰᴏʀ ᴍᴇ.")
        return

    # set same perms as bot - bot can't assign higher perms than itself!
    bot_member = chat.get_member(bot.id)

    try:
        bot.promoteChatMember(
            chat.id,
            user_id,
            can_change_info=bot_member.can_change_info,
            can_post_messages=bot_member.can_post_messages,
            can_edit_messages=bot_member.can_edit_messages,
            can_delete_messages=bot_member.can_delete_messages,
            can_invite_users=bot_member.can_invite_users,
            # can_promote_members=bot_member.can_promote_members,
            can_restrict_members=bot_member.can_restrict_members,
            can_pin_messages=bot_member.can_pin_messages,
        )
    except BadRequest as err:
        if err.message == "User_not_mutual_contact":
            message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴘʀᴏᴍᴏᴛᴇ sᴏᴍᴇᴏɴᴇ ᴡʜᴏ ɪsɴ'ᴛ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.")
        else:
            message.reply_text("ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀᴇᴅ ᴡʜɪʟᴇ ᴘʀᴏᴍᴏᴛɪɴɢ.")
        return

    bot.sendMessage(
        chat.id,
        f"sᴜᴄᴇssꜰᴜʟʟʏ ᴘʀᴏᴍᴏᴛᴇᴅ <b>{user_member.user.first_name or user_id}</b>!",
        parse_mode=ParseMode.HTML,
    )

    log_message = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#PROMOTED\n"
        f"<b>ᴀᴅᴍɪɴ:</b> {mention_html(user.id, user.first_name)}\n"
        f"<b>ᴜsᴇʀ:</b> {mention_html(user_member.user.id, user_member.user.first_name)}"
    )

    return log_message


@run_async
@connection_status
@bot_admin
@can_promote
@user_admin
@loggable
def demote(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    args = context.args

    chat = update.effective_chat
    message = update.effective_message
    user = update.effective_user

    user_id = extract_user(message, args)
    if not user_id:
        message.reply_text(
            "ʏᴏᴜ ᴅᴏɴ'ᴛ sᴇᴇᴍ ᴛᴏ ʙᴇ ʀᴇꜰᴇʀʀɪɴɢ ᴛᴏ ᴀ ᴜsᴇʀ ᴏʀ ᴛʜᴇ ɪᴅ sᴘᴇᴄɪꜰɪᴇᴅ ɪs ɪɴᴄᴏʀʀᴇᴄᴛ.."
        )
        return

    try:
        user_member = chat.get_member(user_id)
    except:
        return

    if user_member.status == "creator":
        message.reply_text("ʟᴍᴀᴏ ᴛʀʏɴɴᴀ ᴅᴇᴍᴏᴛᴇ ᴛʜᴇ ᴏᴡɴᴇʀ? ɴɪᴄᴇ ᴏɴᴇ xᴅ")
        return

    if not user_member.status == "administrator":
        message.reply_text("ᴛʜᴇʏ'ʀᴇ ᴀʟʀᴇᴀᴅʏ ᴀ ɴᴏʀᴍᴀʟ ᴍᴇᴍʙᴇʀ, ʜᴏᴡ ᴡᴏᴜʟᴅ ɪ ᴅᴇᴍᴏᴛᴇ ᴛʜᴇᴍ?")
        return

    if user_id == bot.id:
        message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴅᴇᴍᴏᴛᴇ ᴍʏsᴇʟꜰ! ɢᴇᴛ ᴀɴ ᴀᴅᴍɪɴ ᴛᴏ ᴅᴏ ɪᴛ ꜰᴏʀ ᴍᴇ.")
        return

    try:
        bot.promoteChatMember(
            chat.id,
            user_id,
            can_change_info=False,
            can_post_messages=False,
            can_edit_messages=False,
            can_delete_messages=False,
            can_invite_users=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
        )

        bot.sendMessage(
            chat.id,
            f"sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴅᴇᴍᴏᴛᴇᴅ <b>{user_member.user.first_name or user_id}</b>!",
            parse_mode=ParseMode.HTML,
        )

        log_message = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"#DEMOTED\n"
            f"<b>ᴀᴅᴍɪɴ:</b> {mention_html(user.id, user.first_name)}\n"
            f"<b>ᴜsᴇʀ:</b> {mention_html(user_member.user.id, user_member.user.first_name)}"
        )

        return log_message
    except BadRequest:
        message.reply_text(
            "ᴄᴏᴜʟᴅ ɴᴏᴛ ᴅᴇᴍᴏᴛᴇ. ɪ ᴍɪɢʜᴛ ɴᴏᴛ ʙᴇ ᴀᴅᴍɪɴ, ᴏʀ ᴛʜᴇ ᴀᴅᴍɪɴ sᴛᴀᴛᴜs ᴡᴀs ᴀᴘᴘᴏɪɴᴛᴇᴅ ʙʏ ᴀɴᴏᴛʜᴇʀ"
            " ᴜsᴇʀ, sᴏ ɪ ᴄᴀɴ'ᴛ ᴀᴄᴛ ᴜᴘᴏɴ ᴛʜᴇᴍ!"
        )
        return


@run_async
@user_admin
def refresh_admin(update, _):
    try:
        ADMIN_CACHE.pop(update.effective_chat.id)
    except KeyError:
        pass

    update.effective_message.reply_text("ᴀᴅᴍɪɴ ᴄᴀᴄʜᴇ ʀᴇʟᴏᴀᴅᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ.")


@run_async
@connection_status
@bot_admin
@can_promote
@user_admin
def set_title(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args

    chat = update.effective_chat
    message = update.effective_message

    user_id, title = extract_user_and_text(message, args)
    try:
        user_member = chat.get_member(user_id)
    except:
        return

    if not user_id:
        message.reply_text(
            "ʏᴏᴜ ᴅᴏɴ'ᴛ sᴇᴇᴍ ᴛᴏ ʙᴇ ʀᴇꜰᴇʀʀɪɴɢ ᴛᴏ ᴀ ᴜsᴇʀ ᴏʀ ᴛʜᴇ ɪᴅ sᴘᴇᴄɪꜰɪᴇᴅ ɪs ɪɴᴄᴏʀʀᴇᴄᴛ.."
        )
        return

    if user_member.status == "creator":
        message.reply_text(
            "ʟᴏʟ ᴛʀʏɴɴᴀ sᴇᴛ ᴛɪᴛʟᴇ ꜰᴏʀ ᴛʜᴇ ᴏᴡɴᴇʀ? ɴɪᴄᴇ ᴏɴᴇ xᴅ"
        )
        return

    if user_member.status != "administrator":
        message.reply_text(
            "ᴛʜᴀᴛ's ᴀ ɴᴏʀᴍᴀʟ ᴜsᴇʀ ʀɪɢʜᴛ ᴛʜᴇʀᴇ, ᴛʜᴇʏ ᴀɪɴ'ᴛ ɢᴇᴛᴛɪɴɢ ᴀɴʏ ᴛᴀɢ"
        )
        return

    if user_id == bot.id:
        message.reply_text(
            "ɪ ᴄᴀɴ'ᴛ sᴇᴛ ᴍʏ ᴏᴡɴ ᴛɪᴛʟᴇ ᴍʏsᴇʟꜰ! ɢᴇᴛ ᴛʜᴇ ᴏɴᴇ ᴡʜᴏ ᴍᴀᴅᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴛᴏ ᴅᴏ ɪᴛ ꜰᴏʀ ᴍᴇ."
        )
        return

    if not title:
        message.reply_text("sᴇᴛᴛɪɴɢ ʙʟᴀɴᴋ ᴛɪᴛʟᴇ ᴅᴏᴇsɴ'ᴛ ᴅᴏ ᴀɴʏᴛʜɪɴɢ!")
        return

    if len(title) > 16:
        message.reply_text(
            "ᴛɪᴛʟᴇ ᴄᴀɴ'ᴛ ʙᴇ ᴍᴏʀᴇ ᴛʜᴀɴ 16 ᴄʜᴀʀᴀᴄᴛᴇʀs. ᴛʀᴜɴᴄᴀᴛɪɴɢ ɪᴛ ᴛᴏ 16 ᴄʜᴀʀᴀᴄᴛᴇʀs"
        )

    try:
        bot.setChatAdministratorCustomTitle(chat.id, user_id, title)
    except BadRequest:
        message.reply_text("ɪ ᴄᴀɴ'ᴛ sᴇᴛ ᴄᴜsᴛᴏᴍ ᴛɪᴛʟᴇ ꜰᴏʀ ᴀᴅᴍɪɴs ᴛʜᴀᴛ ɪ ᴅɪᴅɴ'ᴛ ᴘʀᴏᴍᴏᴛᴇ!")
        return

    bot.sendMessage(
        chat.id,
        f"sᴜᴄᴇssꜰᴜʟʟʏ sᴇᴛ ᴛɪᴛʟᴇ ꜰᴏʀ <code>{user_member.user.first_name or user_id}</code> "
        f"ᴀs <code>{html.escape(title[:16])}</code>!",
        parse_mode=ParseMode.HTML,
    )


@run_async
@bot_admin
@user_admin
@typing_action
def setchatpic(update, context):
    chat = update.effective_chat
    msg = update.effective_message
    user = update.effective_user

    if user_can_changeinfo(chat, user, context.bot.id) is False:
        msg.reply_text("You are missing right to change group info!")
        return

    if msg.reply_to_message:
        if msg.reply_to_message.photo:
            pic_id = msg.reply_to_message.photo[-1].file_id
        elif msg.reply_to_message.document:
            pic_id = msg.reply_to_message.document.file_id
        else:
            msg.reply_text("You can only set some photo as chat pic!")
            return
        dlmsg = msg.reply_text("Just a sec...")
        tpic = context.bot.get_file(pic_id)
        tpic.download("gpic.png")
        try:
            with open("gpic.png", "rb") as chatp:
                context.bot.set_chat_photo(int(chat.id), photo=chatp)
                msg.reply_text("Successfully set new chatpic!")
        except BadRequest as excp:
            msg.reply_text(f"Error! {excp.message}")
        finally:
            dlmsg.delete()
            if os.path.isfile("gpic.png"):
                os.remove("gpic.png")
    else:
        msg.reply_text("Reply to some photo or file to set new chat pic!")


@run_async
@bot_admin
@user_admin
@typing_action
def rmchatpic(update, context):
    chat = update.effective_chat
    msg = update.effective_message
    user = update.effective_user

    if user_can_changeinfo(chat, user, context.bot.id) is False:
        msg.reply_text("You don't have enough rights to delete group photo")
        return
    try:
        context.bot.delete_chat_photo(int(chat.id))
        msg.reply_text("Successfully deleted chat's profile photo!")
    except BadRequest as excp:
        msg.reply_text(f"Error! {excp.message}.")
        return


@run_async
@bot_admin
@user_admin
@typing_action
def setchat_title(update, context):
    chat = update.effective_chat
    msg = update.effective_message
    user = update.effective_user
    args = context.args

    if user_can_changeinfo(chat, user, context.bot.id) is False:
        msg.reply_text("You don't have enough rights to change chat info!")
        return

    title = " ".join(args)
    if not title:
        msg.reply_text("Enter some text to set new title in your chat!")
        return

    try:
        context.bot.set_chat_title(int(chat.id), str(title))
        msg.reply_text(
            f"Successfully set <b>{title}</b> as new chat title!",
            parse_mode=ParseMode.HTML,
        )
    except BadRequest as excp:
        msg.reply_text(f"Error! {excp.message}.")
        return


@run_async
@bot_admin
@user_admin
@typing_action
def set_sticker(update, context):
    msg = update.effective_message
    chat = update.effective_chat
    user = update.effective_user

    if user_can_changeinfo(chat, user, context.bot.id) is False:
        return msg.reply_text("You're missing rights to change chat info!")

    if msg.reply_to_message:
        if not msg.reply_to_message.sticker:
            return msg.reply_text(
                "You need to reply to some sticker to set chat sticker set!"
            )
        stkr = msg.reply_to_message.sticker.set_name
        try:
            context.bot.set_chat_sticker_set(chat.id, stkr)
            msg.reply_text(
                f"Successfully set new group stickers in {chat.title}!")
        except BadRequest as excp:
            if excp.message == "Participants_too_few":
                return msg.reply_text(
                    "Sorry, due to telegram restrictions chat needs to have minimum 100 members before they can have group stickers!"
                )
            msg.reply_text(f"Error! {excp.message}.")
    else:
        msg.reply_text(
            "You need to reply to some sticker to set chat sticker set!")


@run_async
@bot_admin
@user_admin
@typing_action
def set_desc(update, context):
    msg = update.effective_message
    chat = update.effective_chat
    user = update.effective_user

    if user_can_changeinfo(chat, user, context.bot.id) is False:
        return msg.reply_text("You're missing rights to change chat info!")

    tesc = msg.text.split(None, 1)
    if len(tesc) >= 2:
        desc = tesc[1]
    else:
        return msg.reply_text("Setting empty description won't do anything!")
    try:
        if len(desc) > 255:
            return msg.reply_text(
                "Description must needs to be under 255 characters!")
        context.bot.set_chat_description(chat.id, desc)
        msg.reply_text(
            f"Successfully updated chat description in {chat.title}!")
    except BadRequest as excp:
        msg.reply_text(f"Error! {excp.message}.")


def __chat_settings__(chat_id, user_id):
    return "You are *admin*: `{}`".format(
        dispatcher.bot.get_chat_member(chat_id, user_id).status
        in ("administrator", "creator")
    )


@run_async
@bot_admin
@can_pin
@user_admin
@loggable
def pin(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    args = context.args

    user = update.effective_user
    chat = update.effective_chat

    is_group = chat.type != "private" and chat.type != "channel"
    prev_message = update.effective_message.reply_to_message

    is_silent = True
    if len(args) >= 1:
        is_silent = not (
            args[0].lower() == "notify"
            or args[0].lower() == "loud"
            or args[0].lower() == "violent"
        )

    if prev_message and is_group:
        try:
            bot.pinChatMessage(
                chat.id, prev_message.message_id, disable_notification=is_silent
            )
        except BadRequest as excp:
            if excp.message == "Chat_not_modified":
                pass
            else:
                raise
        log_message = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"#PINNED\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}"
        )

        return log_message


@run_async
@bot_admin
@can_pin
@user_admin
@loggable
def unpin(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    chat = update.effective_chat
    user = update.effective_user

    try:
        bot.unpinChatMessage(chat.id)
    except BadRequest as excp:
        if excp.message == "Chat_not_modified":
            pass
        else:
            raise

    log_message = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#UNPINNED\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}"
    )

    return log_message


@run_async
@bot_admin
@user_admin
@connection_status
def invite(update: Update, context: CallbackContext):
    bot = context.bot
    chat = update.effective_chat

    if chat.username:
        update.effective_message.reply_text(f"https://t.me/{chat.username}")
    elif chat.type in [chat.SUPERGROUP, chat.CHANNEL]:
        bot_member = chat.get_member(bot.id)
        if bot_member.can_invite_users:
            invitelink = bot.exportChatInviteLink(chat.id)
            update.effective_message.reply_text(invitelink)
        else:
            update.effective_message.reply_text(
                "I don't have access to the invite link, try changing my permissions!"
            )
    else:
        update.effective_message.reply_text(
            "I can only give you invite links for supergroups and channels, sorry!"
        )


@run_async
@connection_status
def adminlist(update, context):
    chat = update.effective_chat  # type: Optional[Chat]
    user = update.effective_user  # type: Optional[User]
    args = context.args
    bot = context.bot

    if update.effective_message.chat.type == "private":
        send_message(update.effective_message, "This command only works in Groups.")
        return

    chat = update.effective_chat
    chat_id = update.effective_chat.id
    chat_name = update.effective_message.chat.title

    try:
        msg = update.effective_message.reply_text(
            "Fetching group admins...", parse_mode=ParseMode.HTML
        )
    except BadRequest:
        msg = update.effective_message.reply_text(
            "Fetching group admins...", quote=False, parse_mode=ParseMode.HTML
        )

    administrators = bot.getChatAdministrators(chat_id)
    text = "Admins in <b>{}</b>:".format(html.escape(update.effective_chat.title))

    bot_admin_list = []

    for admin in administrators:
        user = admin.user
        status = admin.status
        custom_title = admin.custom_title

        if user.first_name == "":
            name = "☠ Deleted Account"
        else:
            name = "{}".format(
                mention_html(
                    user.id, html.escape(user.first_name + " " + (user.last_name or ""))
                )
            )

        if user.is_bot:
            bot_admin_list.append(name)
            administrators.remove(admin)
            continue

        # if user.username:
        #    name = escape_markdown("@" + user.username)
        if status == "creator":
            text += "\n 👑 Creator:"
            text += "\n<code> • </code>{}\n".format(name)

            if custom_title:
                text += f"<code> ┗━ {html.escape(custom_title)}</code>\n"

    text += "\n🔱 Admins:"

    custom_admin_list = {}
    normal_admin_list = []

    for admin in administrators:
        user = admin.user
        status = admin.status
        custom_title = admin.custom_title

        if user.first_name == "":
            name = "☠ Deleted Account"
        else:
            name = "{}".format(
                mention_html(
                    user.id, html.escape(user.first_name + " " + (user.last_name or ""))
                )
            )
        # if user.username:
        #    name = escape_markdown("@" + user.username)
        if status == "administrator":
            if custom_title:
                try:
                    custom_admin_list[custom_title].append(name)
                except KeyError:
                    custom_admin_list.update({custom_title: [name]})
            else:
                normal_admin_list.append(name)

    for admin in normal_admin_list:
        text += "\n<code> • </code>{}".format(admin)

    for admin_group in custom_admin_list.copy():
        if len(custom_admin_list[admin_group]) == 1:
            text += "\n<code> • </code>{} | <code>{}</code>".format(
                custom_admin_list[admin_group][0], html.escape(admin_group)
            )
            custom_admin_list.pop(admin_group)

    text += "\n"
    for admin_group, value in custom_admin_list.items():
        text += "\n🚨 <code>{}</code>".format(admin_group)
        for admin in value:
            text += "\n<code> • </code>{}".format(admin)
        text += "\n"

    text += "\n🤖 Bots:"
    for each_bot in bot_admin_list:
        text += "\n<code> • </code>{}".format(each_bot)

    try:
        msg.edit_text(text, parse_mode=ParseMode.HTML)
    except BadRequest:  # if original message is deleted
        return


__help__ = """
 ⋗ /admins*:* list of admins in the chat

*Admins only:*
 ⋗ /pin*:* silently pins the message replied to - add `'loud'` or `'notify'` to give notifs to users
 ⋗ /unpin*:* unpins the currently pinned message
 ⋗ /invitelink*:* gets invitelink
 ⋗ /promote*:* promotes the user
 ⋗ /demote*:* demotes the user
 ⋗ /title <title here>*:* sets a custom title for an admin that the bot promoted
 ⋗ /admincache*:* force refresh the admins list
 ⋗ /antispam <on/off/yes/no>*:* Will toggle our antispam tech or return your current settings.
 ⋗ /setgtitle <newtitle>*:* Sets new chat title in your group.
 ⋗ /setgpic*:* As a reply to file or photo to set group profile pic!
 ⋗ /delgpic*:* Same as above but to remove group profile pic.
 ⋗ /setsticker*:* As a reply to some sticker to set it as group sticker set!
 ⋗ /setdescription <description>*:* Sets new chat description in group.
 ⋗ /import: Reply to the backup file for the butler group to import as much as possible, making transfers very easy! 
 ⋗ /export: Export group data, which will be exported are: rules, notes (documents, images, music, video, audio, voice, text, text buttons) 
 ⋗ /logchannel: get log channel info
 ⋗ /setlog: set the log channel.
 ⋗ /unsetlog: unset the log channel.
 ⋗ /del: deletes the message you replied to
 ⋗ /purge: deletes all messages between this and the replied to message.
 ⋗ /purge <integer X>: deletes the replied message, and X messages following it if replied to a message.
 ⋗ /rules: get the rules for this chat.
 ⋗ /setrules <your rules here>: set the rules for this chat.
 ⋗ /clearrules: clear the rules for this chat.

Setting the log channel is done by:
⋗ adding the bot to the desired channel (as an admin!)
⋗ sending /setlog in the channel
⋗ forwarding the /setlog to the group

*Note:* Night Mode chats get Automatically closed at 12 am(IST)
and Automatically openned at 6 am(IST) To Prevent Night Spams.

"""

ADMINLIST_HANDLER = DisableAbleCommandHandler("admins", adminlist)

PIN_HANDLER = CommandHandler("pin", pin, filters=Filters.group)
UNPIN_HANDLER = CommandHandler("unpin", unpin, filters=Filters.group)

INVITE_HANDLER = DisableAbleCommandHandler("invitelink", invite)

PROMOTE_HANDLER = DisableAbleCommandHandler("promote", promote)
DEMOTE_HANDLER = DisableAbleCommandHandler("demote", demote)

SET_TITLE_HANDLER = CommandHandler("title", set_title)
ADMIN_REFRESH_HANDLER = CommandHandler(
    "admincache", refresh_admin, filters=Filters.group
)

CHAT_PIC_HANDLER = CommandHandler("setgpic", setchatpic, filters=Filters.group)
DEL_CHAT_PIC_HANDLER = CommandHandler(
    "delgpic", rmchatpic, filters=Filters.group)
SETCHAT_TITLE_HANDLER = CommandHandler(
    "setgtitle", setchat_title, filters=Filters.group
)
SETSTICKET_HANDLER = CommandHandler(
    "setsticker", set_sticker, filters=Filters.group)
SETDESC_HANDLER = CommandHandler(
    "setdescription",
    set_desc,
    filters=Filters.group)

dispatcher.add_handler(ADMINLIST_HANDLER)
dispatcher.add_handler(PIN_HANDLER)
dispatcher.add_handler(UNPIN_HANDLER)
dispatcher.add_handler(INVITE_HANDLER)
dispatcher.add_handler(PROMOTE_HANDLER)
dispatcher.add_handler(DEMOTE_HANDLER)
dispatcher.add_handler(SET_TITLE_HANDLER)
dispatcher.add_handler(ADMIN_REFRESH_HANDLER)
dispatcher.add_handler(CHAT_PIC_HANDLER)
dispatcher.add_handler(DEL_CHAT_PIC_HANDLER)
dispatcher.add_handler(SETCHAT_TITLE_HANDLER)
dispatcher.add_handler(SETSTICKET_HANDLER)
dispatcher.add_handler(SETDESC_HANDLER)

__mod_name__ = "Aᴅᴍɪɴ"
__command_list__ = [
    "adminlist",
    "admins",
    "invitelink",
    "promote",
    "demote",
    "admincache",
]
__handlers__ = [
    ADMINLIST_HANDLER,
    PIN_HANDLER,
    UNPIN_HANDLER,
    INVITE_HANDLER,
    PROMOTE_HANDLER,
    DEMOTE_HANDLER,
    SET_TITLE_HANDLER,
    ADMIN_REFRESH_HANDLER,
]
