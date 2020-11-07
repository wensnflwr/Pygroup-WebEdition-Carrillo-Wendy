# Mensajes HTTP
c0dc9d8

Los mensajes HTTP, son los medios por los cuales se intercambian datos entre servidores y clientes. Hay dos tipos de mensajes: peticiones, enviadas por el cliente al servidor, para pedir el inicio de una acción; y respuestas, que son la respuesta del servidor. 

## ¿Que es un metodo de petición HTTP?

Como se mencionó anteriormente, una petición HTTP es un mensaje enviado desde el **cliente** hacia el **servidor** para dar lugar al inicio de una acción.

# Tipos de petición HTTP y sus funciones:

## ***GET***
El método GET  solicita una representación de un recurso específico. Las peticiones que usan el método GET sólo deben recuperar datos.

## ***HEAD***
El método HEAD pide una respuesta idéntica a la de una petición GET, pero sin el cuerpo de la respuesta.

## ***POST***
El método POST se utiliza para enviar una entidad a un recurso en específico, causando a menudo un cambio en el estado o efectos secundarios en el servidor.

## ***PUT***
El modo PUT reemplaza todas las representaciones actuales del recurso de destino con la carga útil de la petición.

## ***DELETE***
El método DELETE borra un recurso en específico.

## ***CONNECT***
El método CONNECT establece un túnel hacia el servidor identificado por el recurso.

## ***OPTIONS***
El método OPTIONS es utilizado para describir las opciones de comunicación para el recurso de destino.

## ***TRACE***
El método TRACE  realiza una prueba de bucle de retorno de mensaje a lo largo de la ruta al recurso de destino.

## ***PATCH***
El método PATCH  es utilizado para aplicar modificaciones parciales a un recurso.


## ¿Que es un código de respuesta HTTP?
Es la respuesta que da el servidor al cliente respecto a la petición hecha.

***200***	Aceptar.

***400***	Argumento no válido o solicitud incorrecta

***401***	Acceso no autorizado.

***403***	Acceso prohibido Verifica Cloud Console y el archivo de credenciales para asegurarte de que el servicio se habilitó correctamente.

***404***	No se encontró el recurso.

***409***	Se intentó crear un recurso que ya existe o se anuló.

***429***	Demasiadas solicitudes. El cliente superó las restricciones de la cuota asignada. Consulta Cuotas y límites para obtener más información sobre tu cuota.

***499***	La operación se canceló.

***500***	Error del servidor interno

***501***	La operación no se implementó, no está habilitada o no se admite.

***503***	Servicio no disponible. Vuelve a intentarlo más tarde.

***504***	Tiempo de espera de la solicitud de la puerta de enlace



## Enlaces de busqueda: 

- https://cloud.google.com/talent-solution/job-search/docs/http-response-codes?hl=es-419

- https://yosoy.dev/peticiones-http-get-post-put-delete-etc/

- https://developer.mozilla.org/es/docs/Web/HTTP/Methods
