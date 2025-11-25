import json


file = open("github_repos.json", "r")
file_content = file.read()
repos = json.loads(file_content)
file.close()

for repo in repos["scanner"]:
    name =repo['name']
    url = repo['url']
    description = repo['description']
    line_text = f"| [{name}](https://github.com/{url}) | [![Last Commit](https://img.shields.io/github/last-commit/{url})](https://github.com/{url}/commits) | [![Contributors](https://img.shields.io/github/contributors/{url})](https://github.com/{url}/graphs/contributors) | [![Stars](https://img.shields.io/github/stars/{url})](https://github.com/{url}/stargazers) | [![Forks](https://img.shields.io/github/forks/{url})](https://github.com/{url}/forks) | {description} |"
    print(line_text)

# print(repos["scanner"])