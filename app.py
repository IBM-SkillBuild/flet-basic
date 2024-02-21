# importaciones
import flet as ft
from flet import Page,Row, icons,IconButton,TextField
import asyncio

#función renderizada
async def  main(myApp:ft.Page):
  # configuración de la app
  myApp.title="First Flet App"
  myApp.vertical_alignment="center"
  myApp.window_resizable=False
  myApp.window_width=360
  myApp.window_height=480
  myApp.padding=0
  myApp.window_always_on_top=True
  
  
  # controles o componentes declarados
  texto_presentacion = ft.Text(value="Hello World", text_align="center")
  contenedor_principal=ft.Container(texto_presentacion,width=360,height=480,alignment=ft.alignment.center,bgcolor=ft.colors.BLACK)
  
 
  
  
  # montaje de layaout (filas, columnas, componentes etc..)
  await myApp.add_async(contenedor_principal)
 
 
  
  
# llamada a función principal o renderizada  
ft.app(target=main)  
  
  
  
  