# Proyecto Urban Grocers 

Luis Mallqui - 17vo - Sprint 7 

## Crear un kit
endpoint para crear una kit de una tarjeta específica O de usuario.

- Es obligatorio pasar el encabezado Authorisation O el parámetro cardId, para crear la kit

- Si se recibe una solicitud con un encabezado Authorisation que contenga el authToken de un/a usuario/a en particular - se creará la kit de este/a usuario/a.

- Si se recibe el parámetro cardId, se creará una kit dentro de la tarjeta correspondiente

- Si no se pasa ninguno de los parámetros, se devolverá un error.

- Cuando se pasan ambos parámetros, Authorization es la prioridad

**POST**

```sh
/api/v1/kits
```

## EJECUTAR LAS PRUEBAS

1. Clonar el repositorio: git clone https://github.com/lmallqui/qa-project-Urban-Grocers-app-es
2. Instalar libreria: pytest y request
3. Ejecutar las pruebas: por medio del IDE
4. Analizar resultados: visualizar consola

## LISTA DE COMPROBACIÓN DE PRUEBAS

| № | Description | ER:|
|---|------ | ------ |
| 1 |El número permitido de caracteres (1): kit_body = { "name": "a"} | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 2 |El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"} | Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud |
| 3 |El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" } | Código de respuesta: 400 |
| 4 |El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” } | Código de respuesta: 400 |
| 5 |Se permiten caracteres especiales: kit_body = { "name": ""№%@"," } | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 6 |Se permiten espacios: kit_body = { "name": " A Aaa " } | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 7 |Se permiten números: kit_body = { "name": "123" }|Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud|
| 8 |El parámetro no se pasa en la solicitud: kit_body = { }|Código de respuesta: 400|
| 9 |Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }|Código de respuesta: 400|