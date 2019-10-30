from telegram.ext import Updater, CommandHandler
import click

@click.command()
@click.argument('token', nargs=1)
def run_bot(token):
    def hello(update, context):
        update.message.reply_text(
            'Hello {}'.format(update.message.from_user.first_name))


    updater = Updater(token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('hello', hello))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    run_bot()