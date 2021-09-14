# -*-coding: utf-8 -*-

import os
import sqlite3
import qrcode
from PIL import Image
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
Config.set("graphics","width","340")
Config.set("graphics","heigth","640")
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.uix.camera import Camera
from kivy.uix.relativelayout import RelativeLayout
from kivy.garden.mapview import MapView
from kivy.garden.mapview import MapMarkerPopup

def conecct_to_database(path):
    try:
        con = sqlite3.connect(path)
        cursor = con.cursor()
        create_table_descuentos(cursor)
        con.commit()
        con.close()
    except Exception as e:
        print(e)

class InicioScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class DescuentosScreen(Screen):
    def __init__(self,**kwargs):
        super(DescuentosScreen, self).__init__()
        self.APP_PATH = os.getcwd()
        self.DB_PATH = self.APP_PATH + "/TURIT_Database.db"
        self.ListaDescuentosScreen = ListaDescuentosScreen
# Crea la BD y pasa el PATH como parametro para armarla en la carpeta del programa
    def create_database(self):
        conecct_to_database(self.DB_PATH)
    pass

class ListaDescuentosScreen(Screen):
    def __init__(self,**kwargs):
        super(ListaDescuentosScreen, self).__init__()

    def qr_canje(self):
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            version=1,
            box_size=10,
            border=4,
        )
        qr.add_data('ID, Nombre, Proveedor, Valor_Descuento, Costo_Puntos')
        qr.make(fit=True)
        imagen = qr.make_image()
        imagen.save('Canje N1.png', 'png')
        imagen.show()
    pass
#Crea la tabla descuentos dentro de la BD TURIT_Database con sus atributos
def create_table_descuentos(cursor):
    cursor.execute(
            """
            CREATE TABLE Descuentos(
            ID              INT PRIMARY KEY NOT NULL,
            Nombre          TEXT            NOT NULL,
            Proveedor       TEXT            NOT NULL,
            Valor_Descuento INT             NOT NULL,
            Costo_Puntos    INT             NOT NULL
            )
            """
        )

class NotificacionesScreen(Screen):
    pass

class UsuarioScreen(Screen):
    pass

class UbicacionScreen(Screen):
    pass

class StoreScreen(Screen):
    pass

class CameraScreen(Camera, Screen):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strfrtime('%Y%m%d_%H%M%S')
        camera.export_to_png('IMG_{}.PNG'.format(timestr))
        print("Captured")
    pass

class TestCamera(App):
    def build(self):
        return CameraClick()
    pass

class AgregarScreen(Screen):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

class DatosUsuarioScreen(Screen):
    pass

GUI = Builder.load_file('main.kv')

class MainApp(App):
    title = 'TUR_IT'
    def build(self):
        self.icon = 'icons/WEST.jpg'
        return GUI
    def change_screen(self, screen_name):
        screen_manager = (self.root.ids['screen_manager'])
        screen_manager.current = screen_name

if __name__ == '__main__':
    MainApp().run()


