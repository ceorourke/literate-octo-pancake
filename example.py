import sentry_sdk
from sentry_sdk import capture_exception
import os

sentry_sdk.init(
    dsn='https://c0b1efa652d144108fb523f9e0ce3210@meowlificent.ngrok.io/11',
    debug=True,
    release=os.environ.get('COMMIT')
)

try:
    im_gonna_break()
except Exception as e:
    capture_exception(e)