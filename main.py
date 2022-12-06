from github import Github as gt
from random import randint
from os import environ as env

# Creating Github instance and connecting access token

g = gt(env['GITHUB_ACCESS_TOKEN'])

#Creating instance to name new repo

num = randint(1, 700)

#  Accessing API to create repo ( Using random number so there is no test with the same name

repo = g.get_user().create_repo(f'Test{num}')