from datetime import datetime
from notify_run import Notify

notify = Notify(endpoint='https://notify.run/JWn7WTa1SBOXqJGI22RF')

notify.send(f'Tim...?  Are you there, Tim...?')
