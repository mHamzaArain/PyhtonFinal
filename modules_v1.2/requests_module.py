# import requests
# URL -> Uniform Resource Locator
# https: //en.wikipedia.org/wiki/URL?key=value&life=42#History

# Protocol/Scheme:            http, https, ftp, ....
# Host:                                en.wikipedia.org
# Port:                                 http=80, https= 443
# Path:                                 wiki/URL
# Querystring:                     key=value&life=42
# Fragment:                         #History

# var=requests.get()            # get text of website



# var.status.code                   # tell the status of file
    #   200                                 # successfully get site
    #   403                                 # Forbidden
    #   404                                 #  not found
    #   400                                 # Bad Request

# ######Implementation
# res = requests.get('https://api.github.com')
# ####Know methods
# print(dir(res))                         # shows methods i.e, ok, content, json, ...
# print(type(res))                       # <class 'requests.models.Response'>
# print(res)                                 #  <Response [200]>

# ###Response
# print(res.content)                      # Return in byte for (best for images)
                                                    #  b'{"current_user_url":"https://api.github.com/user",  ....
# print(res.text)                             # return data in utf-8 for str  
                                                    # {"current_user_url":"https://api.github.com/user",...

# print(res.json())                             # return in list/dictionary
                                                    # {'current_user_url': 'https://api.github.com/user', ....

# #####Headers
# print(res.headers)                             # useful information, such as the content type, date, server. etc
#                                                           # {'Server': 'GitHub.com', 'Date': 'Thu, 03 Oct 2019 11:37:16 GMT',
# print(res.headers['Content-Type'])    # abstract specific header which is not case sensitive
                                                              #  application/json; charset=utf-8

# # #####Query String Parameters
# import requests

# # Search GitHub's repositories for requests
# response = requests.get(
#     'https://api.github.com/search/repositories',
#     params={'q': 'requests+language:python'},
# )

# # #Inspect some attributes of the `requests` repository
# json_response = response.json()           # 'git_commits_url': 'https://api.github.com/repos
# repository = json_response['items'][0]                  # {'id': 4290214, 'node_id': 'MDEwOlJlcG9zaXRvcnk0MjkwMjE0',
# print(f'Repository name: {repository["name"]}')  # Repository name: grequests
# print(f'Repository description: {repository["description"]}')  # Repository description: Requests + Gevent = <3

# #######################Downloading txt data from url 
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(res.status_code)      # 200 success

# res.raise_for_status()  # Return error if exists
# playFile = open('rj.txt', 'wb')
# for chunk in res.iter_content(100000):
#     playFile.write(chunk)
# playFile.close()

#  ##################### Check response from HTTPError to see exact error
# import requests
# from requests.exceptions import HTTPError

# for url in ['https://api.github.com', 'https://api.github.com/invalid']:
#     try:
#         response = requests.get(url)

#         # If the response was successful, no Exception will be raised
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')  # Python 3.6
#     except Exception as err:
#         print(f'Other error occurred: {err}')  # Python 3.6
#     else:
#         print('Success!')
