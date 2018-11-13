import sentry_sdk
from sentry_sdk import capture_exception
import os

sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN'),
    release=os.environ.get('COMMIT')
)

try:
    im_gonna_break_more_3()
except Exception as e:
    capture_exception(e)

# blah 