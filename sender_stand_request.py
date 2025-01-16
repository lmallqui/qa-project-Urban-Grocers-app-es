import configuration
import requests
import data

#Solicitar nuevo usuario o usuaria
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body)

#Solicitar un nuevo kit
def post_new_client_kit(kit_body,auth_token):
    headers = data.headers
    headers["Authorization"] = f"Bearer {auth_token}"
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)