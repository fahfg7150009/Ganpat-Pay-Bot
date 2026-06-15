from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8851811283:AAEabjGwCiaa-u5hd2SrjEVXXNP5Z2s0y9o"

CHANNEL_USERNAME = "@GanpatE_09"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 Join Channel", url="https://t.me/GanpatE_09")],
        [InlineKeyboardButton("✅ Claim", callback_data="claim")]
    ]

    await update.message.reply_text(
        "🎉 Welcome To Ganpat Tasks Payment Bot",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def claim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    try:
        member = await context.bot.get_chat_member(
            chat_id=CHANNEL_USERNAME,
            user_id=user_id
        )

        if member.status in ["member", "administrator", "creator"]:

            keyboard = [
                [InlineKeyboardButton("🔐 Verify", callback_data="verify")]
            ]

            await query.message.reply_text(
                "🔐 Verify Yourself To Start Bot",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

        else:
            keyboard = [
                [InlineKeyboardButton("📢 Join Channel", url="https://t.me/GanpatE_09")],
                [InlineKeyboardButton("✅ Claim", callback_data="claim")]
            ]

            await query.message.reply_text(
                "❌ Please Join Channel First",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

    except Exception:
        keyboard = [
            [InlineKeyboardButton("📢 Join Channel", url="https://t.me/GanpatE_09")],
            [InlineKeyboardButton("✅ Claim", callback_data="claim")]
        ]

        await query.message.reply_text(
            "❌ Please Join Channel First",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("🚀 Continue To Bot", callback_data="continue")]
    ]

    await query.message.reply_text(
        "✅ Verification Complete\n\nYour device has been verified.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def continue_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [
            InlineKeyboardButton("👤 My Account", callback_data="account"),
            InlineKeyboardButton("👥 Refer & Earn", callback_data="refer")
        ],
        [
            InlineKeyboardButton("🎁 Gift Code", callback_data="gift"),
            InlineKeyboardButton("🎉 Pay To User", callback_data="pay")
        ],
        [
            InlineKeyboardButton("🎧 Support", callback_data="support"),
            InlineKeyboardButton("🚀 Withdraw", callback_data="withdraw")
        ]
    ]

    await query.message.reply_text(
        "🏠 Main Menu",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def account(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.reply_text(
        "👤 My Account\n\n💰 Balance: ₹0"
    )


async def refer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.reply_text(
        f"👥 Refer & Earn\n\nhttps://t.me/Ganpat_Pay_Bot?start={update.callback_query.from_user.id}"
    )


async def gift(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.reply_text(
        "🎁 Gift Code Coming Soon"
    )


async def pay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.reply_text(
        "🎉 Pay To User Coming Soon"
    )


async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.reply_text(
        "🎧 Support\n\nAdmin: @Ganpat_09"
    )


async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.reply_text(
        "🚀 Withdraw\n\nMinimum Withdraw: ₹5"
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(CallbackQueryHandler(claim, pattern="^claim$"))
app.add_handler(CallbackQueryHandler(verify, pattern="^verify$"))
app.add_handler(CallbackQueryHandler(continue_bot, pattern="^continue$"))

app.add_handler(CallbackQueryHandler(account, pattern="^account$"))
app.add_handler(CallbackQueryHandler(refer, pattern="^refer$"))
app.add_handler(CallbackQueryHandler(gift, pattern="^gift$"))
app.add_handler(CallbackQueryHandler(pay, pattern="^pay$"))
app.add_handler(CallbackQueryHandler(support, pattern="^support$"))
app.add_handler(CallbackQueryHandler(withdraw, pattern="^withdraw$"))

print("Ganpat Tasks Payment Bot Started")

app.run_polling()
