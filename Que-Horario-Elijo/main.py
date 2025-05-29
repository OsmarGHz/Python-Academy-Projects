import os.path
import datetime as dt

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def introPrograma():
    print("""
    ¡Bienvenido a ¿Qué horario elijo?!
    En este programa, tú agregas tus opciones de clases por separado para este semestre, y nosotros haremos la magia!
    Con nuestros calendarios que puedes agregar a Google Calendar, te ahorrarás tiempo!
    """)

def mostrarAyuda(): #Mostrar aiuda
    print("""
    Permítenos darte nuestro menú de opciones:
        conectar \t Conecta esta app con tu cuenta de Google
        desconectar \t Desconecta tu cuenta de Google, de esta app
        help \t\t Muestra esta "aiuda"
        clases \t\t Guarda o elimina tus clases
        calendarios \t Administra tus calendarios, y genera nuevos en base a tus clases (dentro, podrás pushear tu calendario a Calendar)
    """)

def mostrarDespedida():
    print("""
    Nos vemos pronto!
    """)

def esSalir(palabra):
    if palabra.lower() == "salir":
        return True
    else: return False

def esIgualString(palabra1, palabra2):
    if(palabra1==palabra2):
        return True
    else: return False

def menuCiclado():
    entrada = ""
    while not esSalir(entrada):
        entrada = input(" -> ")

def main():
    introPrograma()
    mostrarAyuda()
    menuCiclado()
    mostrarDespedida()

if __name__  == "__main__":
    main()