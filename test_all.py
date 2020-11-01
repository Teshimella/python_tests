import pytest


@pytest.mark.parametrize("name", ['test11', 'test22', 'test33'])
def test_create_repository(api, name):
    sozdanie = api.create_repository({'name': name})
    assert sozdanie.ok
    spisok_repo = api.list_repositories()
    assert name in spisok_repo, f'repo {name} not in {spisok_repo}'


@pytest.mark.parametrize("name", ['test11', 'test22', 'test33'])
def test_create_repository_private(api, name):
    sozdanie = api.create_repository({'name': name, "private": True})
    assert sozdanie.ok
    spisok_repo = api.list_repositories(private=True)
    assert name in spisok_repo, f'repo {name} not in {spisok_repo}'


@pytest.mark.parametrize("name", ['-!@#$%^&*()test11-!@#$%^&*()'])
def test_create_repository_name_with_symbols(api_s, name):
    sozdanie = api_s.create_repository({'name': name, "private": True})
    assert sozdanie.ok
    name = '--test11--'
    spisok_repo = api_s.list_repositories(private=True)
    assert name in spisok_repo, f'repo {name} not in {spisok_repo}'
