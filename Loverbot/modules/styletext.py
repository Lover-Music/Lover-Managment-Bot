from Razerbot import dispatcher
from Razerbot.modules.disable import DisableAbleCommandHandler
from Razerbot.modules.helper_funcs.alternate import typing_action
from telegram import ParseMode
from telegram.ext import run_async

normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
weebyfont = [
    "卂",
    "乃",
    "匚",
    "刀",
    "乇",
    "下",
    "厶",
    "卄",
    "工",
    "丁",
    "长",
    "乚",
    "从",
    "𠘨",
    "口",
    "尸",
    "㔿",
    "尺",
    "丂",
    "丅",
    "凵",
    "リ",
    "山",
    "乂",
    "丫",
    "乙",
]
bubblefont = [
    "𝐀",
    "𝐁",
    "𝐂",
    "𝐃",
    "𝐄",
    "𝐅",
    "𝐆",
    "𝐇",
    "𝐈",
    "𝐉",
    "𝐊",
    "𝐋",
    "𝐌",
    "𝐍",
    "𝐎",
    "𝐏",
    "𝐐",
    "𝐑",
    "𝐒",
    "𝐓",
    "𝐔",
    "𝐕",
    "𝐖",
    "𝐗",
    "𝐘",
    "𝐙",
]
bifont = [
    "𝘼",
    "𝘽",
    "𝘾",
    "𝘿",
    "𝙀",
    "𝙁",
    "𝙂",
    "𝙃",
    "𝙄",
    "𝙅",
    "𝙆",
    "𝙇",
    "𝙈",
    "𝙉",
    "𝙊",
    "𝙋",
    "𝙌",
    "𝙍",
    "𝙎",
    "𝙏",
    "𝙐",
    "𝙑",
    "𝙒",
    "𝙓",
    "𝙔",
    "𝙕",
]
fbubblefont = [
    "𝙖",
    "𝙗",
    "𝙘",
    "𝙙",
    "𝙚",
    "𝙛",
    "𝙜",
    "𝙝",
    "𝙞",
    "𝙟",
    "𝙠",
    "𝙡",
    "𝙢",
    "𝙣",
    "𝙤",
    "𝙥",
    "𝙦",
    "𝙧",
    "𝙨",
    "𝙩",
    "𝙪",
    "𝙫",
    "𝙬",
    "𝙭",
    "𝙮",
    "𝙯",
]
squarefont = [
    "ᴀ",
    "ʙ",
    "ᴄ",
    "ᴅ",
    "ᴇ",
    "ғ",
    "ɢ",
    "ʜ",
    "ɪ",
    "ᴊ",
    "ᴋ",
    "ʟ",
    "ᴍ",
    "ɴ",
    "ᴏ",
    "ᴘ",
    "ǫ",
    "ʀ",
    "s",
    "ᴛ",
    "ᴜ",
    "ᴠ",
    "ᴡ",
    "x",
    "ʏ",
    "ᴢ",
]
fsquarefont = [
    "🅰",
    "🅱",
    "🅲",
    "🅳",
    "🅴",
    "🅵",
    "🅶",
    "🅷",
    "🅸",
    "🅹",
    "🅺",
    "🅻",
    "🅼",
    "🅽",
    "🅾",
    "🅿",
    "🆀",
    "🆁",
    "🆂",
    "🆃",
    "🆄",
    "🆅",
    "🆆",
    "🆇",
    "🆈",
    "🆉",
]
bluefont = [
    "🇦 ",
    "🇧 ",
    "🇨 ",
    "🇩 ",
    "🇪 ",
    "🇫 ",
    "🇬 ",
    "🇭 ",
    "🇮 ",
    "🇯 ",
    "🇰 ",
    "🇱 ",
    "🇲 ",
    "🇳 ",
    "🇴 ",
    "🇵 ",
    "🇶 ",
    "🇷 ",
    "🇸 ",
    "🇹 ",
    "🇺 ",
    "🇻 ",
    "🇼 ",
    "🇽 ",
    "🇾 ",
    "🇿 ",
]
latinfont = [
    "𝒶",
    "𝒷",
    "𝒸",
    "𝒹",
    "ℯ",
    "𝒻",
    "ℊ",
    "𝒽",
    "𝒾",
    "𝒿",
    "𝓀",
    "𝓁",
    "𝓂",
    "𝓃",
    "ℴ",
    "𝓅",
    "𝓆",
    "𝓇",
    "𝓈",
    "𝓉",
    "𝓊",
    "𝓋",
    "𝓌",
    "𝓍",
    "𝓎",
    "𝓏",
]
linedfont = [
    "𝕒",
    "𝕓",
    "𝕔",
    "𝕕",
    "𝕖",
    "𝕗",
    "𝕘",
    "𝕙",
    "𝕚",
    "𝕛",
    "𝕜",
    "𝕝",
    "𝕞",
    "𝕟",
    "𝕠",
    "𝕡",
    "𝕢",
    "𝕣",
    "𝕤",
    "𝕥",
    "𝕦",
    "𝕧",
    "𝕨",
    "𝕩",
    "𝕪",
    "𝕫",
]


@run_async
@typing_action
def weebify(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/weebify <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@run_async
@typing_action
def bubble(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/bubble <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            bubblecharacter = bubblefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, bubblecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@run_async
@typing_action
def fbubble(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/fbubble <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            fbubblecharacter = fbubblefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, fbubblecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@run_async
@typing_action
def square(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/square <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            squarecharacter = squarefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, squarecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@run_async
@typing_action
def fsquare(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/fsquare <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            fsquarecharacter = fsquarefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, fsquarecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@run_async
@typing_action
def blue(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/blue <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            bluecharacter = bluefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, bluecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)
        
@run_async
@typing_action
def bi(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/bi <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            bicharacter = bifont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, bicharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)
        


@run_async
@typing_action
def latin(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/latin <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            latincharacter = latinfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, latincharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@run_async
@typing_action
def lined(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/lined <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            linedcharacter = linedfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, linedcharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)
       

WEEBIFY_HANDLER = DisableAbleCommandHandler("weebify", weebify)
BUBBLE_HANDLER = DisableAbleCommandHandler("bold", bubble)
FBUBBLE_HANDLER = DisableAbleCommandHandler("bis", fbubble)
SQUARE_HANDLER = DisableAbleCommandHandler("tiny", square)
FSQUARE_HANDLER = DisableAbleCommandHandler("fsquare", fsquare)
BLUE_HANDLER = DisableAbleCommandHandler("blue", blue)
LATIN_HANDLER = DisableAbleCommandHandler("latin", latin)
LINED_HANDLER = DisableAbleCommandHandler("lined", lined)
BI_HANDLER = DisableAbleCommandHandler("bi", bi)

dispatcher.add_handler(WEEBIFY_HANDLER)
dispatcher.add_handler(BUBBLE_HANDLER)
dispatcher.add_handler(FBUBBLE_HANDLER)
dispatcher.add_handler(SQUARE_HANDLER)
dispatcher.add_handler(FSQUARE_HANDLER)
dispatcher.add_handler(BLUE_HANDLER)
dispatcher.add_handler(LATIN_HANDLER)
dispatcher.add_handler(LINED_HANDLER)
dispatcher.add_handler(BI_HANDLER)

__command_list__ = ["weebify"]
__command_list__ = ["bold"]
__command_list__ = ["bis"]
__command_list__ = ["tiny"]
__command_list__ = ["fsquare"]
__command_list__ = ["blue"]
__command_list__ = ["latin"]
__command_list__ = ["lined"]
__command_list__ = ["bi"]
__handlers__ = [WEEBIFY_HANDLER]
__handlers__ = [BUBBLE_HANDLER]
__handlers__ = [FBUBBLE_HANDLER]
__handlers__ = [SQUARE_HANDLER]
__handlers__ = [FSQUARE_HANDLER]
__handlers__ = [BLUE_HANDLER]
__handlers__ = [LATIN_HANDLER]
__handlers__ = [LINED_HANDLER]
__handlers__ = [BI_HANDLER]
