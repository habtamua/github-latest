import requests

response = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&tagged=django&site=stackoverflow')
question = response.json()['items'][0]

title = question['title']
user_id = question['owner']['user_id']
display_name = question['owner']['display_name']

response = requests.get('https://api.stackexchange.com/2.2/users/{}?order=desc&sort=reputation&site=stackoverflow'.format(user_id))

creation_date = response.json()['items'][0]['creation_date']

print("{} created on {} asked \"{}\"".format(display_name, creation_date, title))
# print(response.json())
# print(response.json().keys())
# print(response.json()['items'])
# print(response.json()['items'][0])
# print(response.json()['items'][0]['owner'])

# response = requests.get('https://stackoverflow.com/users/11082322/bhavana')
# print(response.content)

# response = requests.get('https://api.stackexchange.com/2.2/users/5215609?order=desc&sort=reputation&site=stackoverflow')

# print(response.json()['items'][0]['creation_date'])