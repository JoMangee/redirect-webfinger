from aiohttp_wsgi import WSGIHandler
from .__main__ import create_app
import os

# loadoadload these from environment variables or config
accts = os.environ.get('ACCT', '').split(',')
mastodon_server = os.environ.get('MASTODON_SERVER', '')
mastodon_user = os.environ.get('MASTODON_USER', '')

app = create_app(accts, mastodon_server, mastodon_user)
application = WSGIHandler(app)