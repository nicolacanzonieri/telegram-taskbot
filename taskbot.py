# pip install python-telegram-bot

from typing import Final
from telegram import Update, Bot, Message
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = 'YOUR_BOT_TOKEN'
BOT_USERNAME: Final = 'YOUR_BOT_USERNAME'
USER_USERNAME: Final = 'YOUR_USERNAME'
CUSTOM_USERNAME: Final = 'YOUR_CUSTOM_NAME'

tasks = []

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user.username == USER_USERNAME:
        await update.message.reply_text('Hi ' + CUSTOM_USERNAME + '! I am your task manager')
        await update.message.reply_text('I am here to assist you during your everyday tasks!')
    else:
        await update.message.reply_text('I am sorry but I cannot help you!')
        await update.message.reply_text('My services are limited to a few persons')
        await update.message.reply_text('If you are still interested my code is available on GitHub in the profile of nicolacanzonieri!')

async def debug_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text[7:])

async def add_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user.username == USER_USERNAME:
        task = update.message.text[5:]
        if len(task) > 0:
            tasks.append(task)
            await update.message.reply_text('I have added ' + task + ' to your tasks!')
        else:
            await update.message.reply_text('Your message is empty!')
    else:
        await update.message.reply_text('Authorization denied')

async def list_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user.username == USER_USERNAME:
        if len(tasks) == 0:
            await update.message.reply_text('You have no tasks to do today!')
        else:
            tasks_list = 'Tasks:\n'
            for task in tasks:
                tasks_list += f'• {task}\n'

            await update.message.reply_text(tasks_list)
    else:
        await update.message.reply_text('Authorization denied')

async def remove_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user.username == USER_USERNAME:
        taskName = update.message.text[8:]

        if len(taskName) > 0:
            if taskName not in tasks:
                await update.message.reply_text('I did not find ' + taskName + ' in your task list!')
            else:
                tasks.remove(taskName)
                await update.message.reply_text('I have removed ' + taskName + ' from your tasks!')
        else:
            await update.message.reply_text('Your message is empty!')
    else:
        await update.message.reply_text('Authorization denied')

# Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

        print('Bot: ', response)
        await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    #app.add_handler(CommandHandler('debug', debug_command))
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('add', add_command))
    app.add_handler(CommandHandler('list', list_command))
    app.add_handler(CommandHandler('remove', remove_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Check every 3 seconds if a message arrived
    print('Polling...')
    app.run_polling(poll_interval = 3)
