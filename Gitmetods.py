from .Apiconnector import Connector


class GitMetods(Connector):

    def __init__(self, git, repo_token, owner):
        self.owner = owner
        super().__init__(git, repo_token)

    def create_repository(self, *args, **kwargs):
        respone = GitMetods.post(self, '/user/repos', *args, **kwargs)
        return respone

    def delete_repository(self, owner, name, *args, **kwargs):
        respone = GitMetods.delete(self, f'/repos/{owner}/{name}', *args, **kwargs)
        return respone

    def list_repositories(self, private=False, *args, **kwargs):
        respone = GitMetods.get(self, '/user/repos', *args, **kwargs)
        assert respone.status_code == 200, f'status_code -> {respone.status_code}'
        repo_list_name = [i['name'] for i in respone.json() if len(respone.json()) != 0 and i['private'] is private]
        return repo_list_name
