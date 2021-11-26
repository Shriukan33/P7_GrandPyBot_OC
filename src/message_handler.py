from .stop_words import STOP_WORDS
import re


class MessageHandler:
    """
    Class that handles the messages sent by the user.
    """
    # def __init__(self, message: str, is_bot: bool):
    #     self.message = message
    #     self.is_bot = is_bot

    def parse_message(message: str) -> str:
        parsed_message = message
        parsed_message = parsed_message.lower()
        # Make a list with the words, excluding special characters
        # and numbers.
        splitted_message = re.split(r'[^a-zA-Z0-9À-ÿ]+', parsed_message)
        parsed_message = list(splitted_message)

        # Cleanse the list from stop words
        for word in splitted_message:
            for stop_word in STOP_WORDS:
                if word == stop_word:
                    parsed_message.remove(word)
                    break

        # Remove empty extra spaces if any
        parsed_message = " ".join(parsed_message).strip()

        return parsed_message

    def wrap_message(message: str, is_bot: bool) -> str:
        """
        Wrap a message and format it depending on if this is
        the bot talking or the user.
        """
        formated_message = ""

        if is_bot:
            formated_message = \
                "<span class='bot_message'>GrandPy:</span> " + message
        else:
            formated_message = \
                "<span class='user_message'>Vous:</span> " + message

        return formated_message

    def add_wiki_answer(message: str, wiki_answer: dict) -> str:
        """
        Add the wiki answer to the message and its link.
        """
        if wiki_answer:
            message += wiki_answer['extract']
            message += f" [<a href={wiki_answer['url']}>En savoir" + \
                " plus sur Wikipedia</a>]"
        else:
            message += "Peux tu répéter ? Mon audition n'est plus " + \
                "ce qu'elle était ..."
        return message

    def add_address(message: str, formated_address) -> str:
        """
        Add the address to the message.
        """
        if formated_address:
            message += formated_address + ". "
        return message
