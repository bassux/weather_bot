import os
import datetime

this_path = os.path.dirname(os.path.abspath(__file__))

def add_users_to_log(user: str, text: str) -> None:
    """
    Logging user's requests to file.
    """
    dt = datetime.datetime.now()

    with open(os.path.join(this_path, 'log_users.txt'), 'a+') as file:
        file.write(f"{dt.strftime('%X %d-%B-%Y')} @{user} запросил: {text}\n")
