from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import json

# Your bot token from BotFather
TOKEN = '7681089825:AAGr-SFyODXro57n-YvEpfDw4h9-LeQJ86w'


# Define a function for the /start command with buttons for all commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Main menu buttons (inline keyboard for options)
    keyboard = [
        [InlineKeyboardButton("Վիրտուալ ադմինիստրատիվ օգնական", callback_data='1')],
        [InlineKeyboardButton("Հնարավորությունների պահոց", callback_data='2')],
        [InlineKeyboardButton("Ինքնակրթություն", callback_data='3')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Create a custom keyboard for all available commands in the typing section
    command_buttons = ReplyKeyboardMarkup([
        ['/start', '/help', '/about', '/contact'],  # Add other commands as needed
    ], resize_keyboard=True, one_time_keyboard=True)

    # Send the start message with the inline keyboard and custom command buttons
    await update.message.reply_text('Ի՞Նչ կարիք ունեք:', reply_markup=reply_markup)
    await update.message.reply_text(
        "",
        reply_markup=command_buttons
    )


# Define a function to show the second-level options for Option 1
async def show_option_1_options(update: Update) -> None:
    keyboard = [
        [InlineKeyboardButton("Պետական Բուհեր(Երևան)", callback_data='1_1')],
        [InlineKeyboardButton("Պետական Բուհեր(Մարզեր)", callback_data='1_2')],
        [InlineKeyboardButton("Միջպետական Բուհեր", callback_data='1_3')],
        [InlineKeyboardButton("Մասնավոր Բուհեր", callback_data='1_4')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text('', reply_markup=reply_markup)

async def show_option_1_1_options(update: Update) -> None:
    keyboard = [
        [InlineKeyboardButton("Երևանի պետական համալսարան (ԵՊՀ)", callback_data='1_1_1')],
        [InlineKeyboardButton("Հայաստանի ազգային պոլիտեխնիկական համալսարան", callback_data='1_1_2')],
        [InlineKeyboardButton("Հայաստանի պետական տնտեսագիտական համալսարան (ՀՊՏՀ)", callback_data='1_1_3')],
        [InlineKeyboardButton("Երևանի պետական բժշկական համալսարան (ԵՊԲՀ)", callback_data='1_1_4')],
        [InlineKeyboardButton("Հայկական պետական մանկավարժական համալսարան(ՀՊՄՀ)", callback_data='1_1_5')],
        [InlineKeyboardButton("Երևանի Պետական Լեզվաբանական Համալսարան, Վալերի Բրյուսովի անվան (ԵՊԼՀ)", callback_data='1_1_6')],
        [InlineKeyboardButton("Երևանի պետական կոնսերվատորիա, Կոմիտասի անվան (ԵՊԿ)", callback_data='1_1_7')],
        [InlineKeyboardButton("Երևանի թատրոնի և կինոյի պետական ինստիտուտ", callback_data='1_1_8')],
        [InlineKeyboardButton("Ճարտարապետության և շինարարարության Հայաստանի ազգային համալսարան", callback_data='1_1_9')],
        [InlineKeyboardButton("Հայաստանի ազգային ագրարային համալսարան", callback_data='1_1_10')],
        [InlineKeyboardButton("Հայաստանի գեղարվեստի պետական ակադեմիա", callback_data='1_1_11')],
        [InlineKeyboardButton("Հայաստանի Հանրապետության պետական կառավարման ակադեմիա (ՀՀ ՊԿԱ)", callback_data='1_1_12')],
        [InlineKeyboardButton("Ֆիզիկական կուլտուրայի հայկական պետական ինստիտուտ", callback_data='1_1_13')],
        [InlineKeyboardButton("ՀՀ ԳԱԱ Գիտակրթական միջազգային կենտրոն", callback_data='1_1_14')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text('', reply_markup=reply_markup)

# Define a function to show the second-level options for Option 2
async def show_option_2_options(update: Update) -> None:
    keyboard = [
        [InlineKeyboardButton("Կրթական ծրագրեր", callback_data='2_1')],
        [InlineKeyboardButton("Կամավորական ծրագրեր", callback_data='2_2')],
        [InlineKeyboardButton("Աշխատանք", callback_data='2_3')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text('')

async def show_option_1_3_options(update: Update) -> None:
    keyboard = [
        [InlineKeyboardButton("Հայաստանի ամերիկյան համալսարան", callback_data='1_3_1')],
        [InlineKeyboardButton("Հայաստանում ֆրանսիական համալսարան", callback_data='1_3_2')],
        [InlineKeyboardButton("Հայ-ռուսական համալսարան", callback_data='1_3_3')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text('',reply_markup=reply_markup)


async def show_option_3_options(update: Update) -> None:
    keyboard = [
        [InlineKeyboardButton("Գրքեր", callback_data='3_1')],
        [InlineKeyboardButton("Պոդկաստներ", callback_data='3_2')],
        [InlineKeyboardButton("Օգտակար հղումներ", callback_data='3_3')],
        [InlineKeyboardButton("Տելեգրամ ալիքներ", callback_data='3_4')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text('Choose an option from the second level for Option 3:',
                                                   reply_markup=reply_markup)


async def send_links(update: Update,strJson,str) -> None:
    try:
        with open(strJson, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        await update.callback_query.message.reply_text("The data file is missing.")
        return
    except json.JSONDecodeError:
        await update.callback_query.message.reply_text("Error reading the data file.")
        return

    links = data.get(str, [])
    message = ""
    for link in links:
        message = link + "\n\n"
        await update.callback_query.message.reply_text(message)


# Define a callback query handler to handle button clicks
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  # Acknowledge the callback query

    # Main menu options
    if query.data == '1':
        await show_option_1_options(update)
    elif query.data == '2':
        await show_option_2_options(update)
    elif query.data == '3':
        await show_option_3_options(update)

    # Second-level options for Option 1
    elif query.data == '1_1':
        await show_option_1_1_options(update)
    elif query.data == '1_2':
        await send_links(update, 'AdminUni.json', 'universities')
    elif query.data == '1_3':
        await show_option_1_3_options(update)
    elif query.data == '1_4':
        await send_links(update, 'AdminUni.json', 'Mas')

    elif query.data == '1_1_1':
        await send_links(update, 'AdminUni.json', '1_1')
    elif query.data == '1_1_2':
        await send_links(update, 'AdminUni.json', '1_2')
    elif query.data == '1_1_3':
        await send_links(update, 'AdminUni.json', '1_3')
    elif query.data == '1_1_4':
        await send_links(update, 'AdminUni.json', '1_4')
    elif query.data == '1_1_5':
        await send_links(update, 'AdminUni.json', '1_5')
    elif query.data == '1_1_6':
        await send_links(update, 'AdminUni.json', '1_6')
    elif query.data == '1_1_7':
        await send_links(update, 'AdminUni.json', '1_7')
    elif query.data == '1_1_8':
        await send_links(update, 'AdminUni.json', '1_8')
    elif query.data == '1_1_9':
        await send_links(update, 'AdminUni.json', '1_9')
    elif query.data == '1_1_10':
        await send_links(update, 'AdminUni.json', '1_10')
    elif query.data == '1_1_11':
        await send_links(update, 'AdminUni.json', '1_11')
    elif query.data == '1_1_12':
        await send_links(update, 'AdminUni.json', '1_12')
    elif query.data == '1_1_13':
        await send_links(update, 'AdminUni.json', '1_13')
    elif query.data == '1_1_14':
        await send_links(update, 'AdminUni.json', '1_14')

    elif query.data == '1_3_1':
        await send_links(update, 'AdminUni.json', '3_1')
    elif query.data == '1_3_2':
        await send_links(update, 'AdminUni.json', '3_2')
    elif query.data == '1_3_3':
        await send_links(update, 'AdminUni.json', '3_3')

    # Second-level options for Option 2
    elif query.data == '2_1':
        await send_links(update, 'Opportunities.json', 'education')
    elif query.data == '2_2':
        await send_links(update, 'Opportunities.json', 'volunteering')
    elif query.data == '2_3':
        await send_links(update, 'Opportunities.json', 'jobs')


    # Second-level options for Option 2
    elif query.data == '3_1':
        await send_links(update, 'selfStudy.json', 'books')
    elif query.data == '3_2':
        await send_links(update, 'selfStudy.json', 'podcasts')
    elif query.data == '3_3':
        await send_links(update,'selfStudy.json','links')
    elif query.data == '3_4':
        await send_links(update,'selfStudy.json','TgChannels')

    # After any action, return to the main menu
    await start(update, context)  # This ensures after any query, it will return to the start menu


# Define the main function to start the bot
def main():
    # Initialize the application with your bot token
    application = Application.builder().token(TOKEN).build()

    # Add command handler for /start
    application.add_handler(CommandHandler("start", start))

    # Add a callback handler for button clicks
    application.add_handler(CallbackQueryHandler(button_click))

    # Start the bot
    application.run_polling()


if __name__ == '__main__':
    main()
