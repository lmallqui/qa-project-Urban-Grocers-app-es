import sender_stand_request
import data

# esta función cambia los valores en el parámetro "name"
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Obtener token del nuevo usuario o usuaria
def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    return user_response.json()["authToken"]

# Función de prueba positiva
def positive_assert(kit_body,auth_token):
    user_body = get_kit_body(kit_body)
    user_response = sender_stand_request.post_new_client_kit(user_body,auth_token)
    assert user_response.status_code == 201
    assert user_response.json()["name"] == user_body["name"]

# Función de prueba negativa
def negative_assert_code_400(kit_body,auth_token):
    user_body = get_kit_body(kit_body)
    response = sender_stand_request.post_new_client_kit(user_body,auth_token)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "El nombre debe contener sólo letras latino, " \
                                         "un espacio y un guión.  "\
                                         "De 2 a 15 caracteres"

#Prueba 1
def test_create_user_1_letter_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert("a",auth_token)

#Prueba 2
def test_create_user_511_letter_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert(data.kit_body_511,auth_token)

#Prueba 3
def test_create_user_empty_name_get_error_response():
    auth_token = get_new_user_token()
    user_body = get_kit_body("")
    negative_assert_code_400(user_body,auth_token)

#Prueba 4
def test_create_user_512_letter_in_name_get_error_response():
    auth_token = get_new_user_token()
    negative_assert_code_400(data.kit_body_512,auth_token)

#Prueba 5
def test_create_user_special_symbol_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert("\"№%@\",",auth_token)

#Prueba 6
def test_create_user_space_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert(" A Aaa",auth_token)

#Prueba 7
def test_create_user_numer_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert("123",auth_token)

#Prueba 8
def test_create_user_no_name_get_error_response():
    auth_token = get_new_user_token()
    user_body = data.kit_body.copy()
    user_body.pop("name")
    negative_assert_code_400(user_body,auth_token)

#Prueba 9
def test_create_user_number_type_name_get_error_response():
    auth_token = get_new_user_token()
    user_body = get_kit_body(12)
    response = sender_stand_request.post_new_client_kit(user_body,auth_token)
    assert response.status_code == 400
