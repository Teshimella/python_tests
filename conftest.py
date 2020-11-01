import pytest
from .Gitmetods import GitMetods
import time
import base64
import os

token = os.environ["TOKEN"].encode('utf-8')
owner = 'Teshimella'
git = 'https://api.github.com'
encode_token = base64.b64encode(owner.encode("UTF-8") + b':' + token).decode("UTF-8")


@pytest.fixture
def api(name):
    apiagent = GitMetods(git, encode_token, owner)

    yield apiagent

    apiagent.delete_repository(apiagent.owner, name)
    time.sleep(10)
    spisok_repo = apiagent.list_repositories()
    assert name not in spisok_repo, f'repo {name} not in {spisok_repo}'


@pytest.fixture
def api_s():
    apiagent = GitMetods(git, encode_token, owner)

    yield apiagent

    name = '--test11--'
    apiagent.delete_repository(apiagent.owner, name)
    time.sleep(10)
    spisok_repo = apiagent.list_repositories()
    assert name not in spisok_repo, f'repo {name} not in {spisok_repo}'
