import os.path                # Importa funciones para trabajar con rutas de archivos.
import datetime as dt         # Importa el módulo datetime y lo renombra como 'dt'.

from google.auth.transport.requests import Request         # Para refrescar credenciales.
from google.oauth2.credentials import Credentials          # Para manejar credenciales OAuth2.
from google_auth_oauthlib.flow import InstalledAppFlow     # Para el flujo de autenticación OAuth2.
from googleapiclient.discovery import build                # Para construir el servicio de Google Calendar.
from googleapiclient.errors import HttpError               # Para manejar errores de la API.

SCOPES = ["https://www.googleapis.com/auth/calendar"]      # Define el alcance de permisos (acceso total al calendario).

def main():                                                # Función principal del programa.
    creds = None                                           # Inicializa las credenciales como None.
    if os.path.exists("token.json"):                       # Si existe el archivo de token guardado...
        creds = Credentials.from_authorized_user_file("token.json")  # ...carga las credenciales desde ese archivo.

    if not creds or not creds.valid:                       # Si no hay credenciales o son inválidas...
        if creds and creds.expired and creds.refresh_token:    # ...pero hay token expirado y refresh_token...
            creds.refresh(Request())                           # ...refresca las credenciales.
        else:                                                 # Si no hay credenciales válidas...
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json",SCOPES)  # Crea el flujo de autenticación.
            creds = flow.run_local_server(port = 0)            # Inicia el servidor local para autenticación.

        with open("token.json", "w") as token:                 # Guarda las credenciales nuevas en token.json.
            token.write(creds.to_json())

    try:
        service = build("calendar","v3",credentials=creds)     # Construye el servicio de Google Calendar.

        event = {                                              # Define un evento de ejemplo.
            "summary": "My Python Event",                      # Título del evento.
            "location": "Somewhere Online",                    # Ubicación.
            "description": "Some more details on this awesome event",  # Descripción.
            "colorId": 6,                                      # Color del evento.
            "start": {                                         # Fecha y hora de inicio.
                "dateTime": "2024-12-15T00:00:00+"
            }
        }

        # now = dt.datetime.now().isoformat() + "Z"            # (Comentado) Obtiene la fecha y hora actual en formato ISO.

        # event_result = service.events().list(calendarId="primary", timeMin=now, maxResults=10, singleEvents=True, orderBy="startTime").execute()
        # events = event_result.get("items", [])                # (Comentado) Obtiene los próximos 10 eventos.
        # if not events:                                       # (Comentado) Si no hay eventos...
        #     print("No upcoming events found")                 # ...muestra mensaje y termina.
        #     return
        # for event in events:                                 # (Comentado) Para cada evento...
        #     start = event["start"].get("dateTime",event["start"].get("date"))  # ...obtiene la fecha de inicio.
        #     print(start, event["summary"])                   # ...imprime la fecha y el título.

    except HttpError as error:                                 # Si ocurre un error con la API...
        print("An error ocurred", error)                       # ...lo imprime.

if __name__  == "__main__":                                   # Si el archivo se ejecuta directamente...
    main()                                                    # ...llama a la función principal.