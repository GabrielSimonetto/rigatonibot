from telegram import Bot, Update, Message, File
from telegram.ext import Updater, CommandHandler
import click
import responses
import send    

@click.command()
@click.argument('token', nargs=1)
def run_bot(token):
    def hello(update, context):
        update.message.reply_text(
            'Hello {}'.format(update.message.from_user.first_name))

    def make_pasta(update, context):
        msg = update.message

        if msg.reply_to_message is None:
            msg.reply_text(responses.NOT_A_REPLY)
            return
        if msg.reply_to_message.document is None:
            msg.reply_text(responses.NOT_A_DOC)
            return
        pasta = File(msg.reply_to_message.document.file_id)
        print('----------------')
        print(pasta)
        print(type(pasta))
        print(pasta.file_id)
        print(pasta['file_id'])
        print('----------------')
        print(dir(pasta))
        print('----------------')
        pasta.download()
        print('Passou')

        # link = send.filepath_to_paste(
        #             msg.reply_to_message.document.file_id)
        # msg.reply_to_message(f"Hey, it worked! You can find you file on {link}")

        # msg.reply_text(msg.document)

    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('hello', hello))
    dp.add_handler(CommandHandler('make_pasta', make_pasta))

    print('Log: Seu bot iniciou! (:')
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    run_bot()