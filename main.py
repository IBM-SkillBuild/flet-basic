import os
import time
from typing import Dict
import flet
import flet as ft
from flet import *
from flet_navigator import VirtualFletNavigator, PageData, ROUTE_404, route, Page
from rembg import remove
from PIL import Image
import numpy as np
import random
import requests





def main(page: Page):
  page.horizontal_alignment = "center"
  page.vertical_alignment="center"
  page.window_resizable = True
  page.scroll = 'always'
  #page.window_width = 480
  #page.window_height = 640
  page.padding = 30
  #page.window_always_on_top = True
  page.theme_mode= ThemeMode.DARK
 
  
  
  VirtualFletNavigator(
    {
      "/":home,
      "info":info,
      "resultado":resultado,
      ROUTE_404: route_404
    },
      VirtualFletNavigator().render(page)
  )



@route('/')
def home(MyApp:PageData):
   MyApp.page.controls.clear()
   myAppBar=AppBar(
     title=Text("Home page. Remove background images"),
     bgcolor="blue")  
   MyApp.set_appbar(myAppBar) 
   try:
    for filename in os.listdir('./assets'):
        if not filename.startswith("entrada") and not filename.startswith("salida") and not filename.startswith("procesando"):
            os.remove("./assets/"+filename)
   except:
     pass
   
   
   
   btn_info = ElevatedButton('Información', on_click=lambda _:MyApp.navigator.navigate(f'info',MyApp.page,('hola',"hola")))
   btn_resultado = ElevatedButton('Resultado', on_click=lambda _: MyApp.navigator.navigate(
       f'resultado', MyApp.page, ('hola', 'hola')))
   MyApp.page.add(Row([btn_info,btn_resultado]))
   
   prog_bars: Dict[str, ProgressRing] = {}
   files = Ref[Column]()
   upload_button = Ref[ElevatedButton]()
   antes = flet.Image(
                src=f"salida.png",
                col={"md": 2},
             
                fit=ImageFit.CONTAIN,

            )
   intermedio = Text("", col={"md": 1}, text_align=ft.TextAlign.CENTER)
   despues = flet.Image(src=f"entrada.jpeg",
                                
                                col={"md": 2},
                                 fit=ft.ImageFit.CONTAIN
                                 )
   imagen_salida = ft.ResponsiveRow([
               antes,intermedio,despues
                
               
            ],alignment="center")
            
   MyApp.page.add(imagen_salida)
   
  
     

   def file_picker_result(e: FilePickerResultEvent):
       
        upload_button.current.disabled = True if e.files is None else False
        prog_bars.clear()
        files.current.controls.clear()
        if e.files is not None:
            for f in e.files:
                prog = ProgressRing(value=0, bgcolor="#eeeeee", width=20, height=20)
                prog_bars[f.name] = prog
                files.current.controls.append(Row([prog, Text(f.name, )], alignment='center'))
                
               
        MyApp.page.update()

   def on_upload_progress(e: FilePickerUploadEvent):
        prog_bars[e.file_name].value = e.progress
        prog_bars[e.file_name].update()

   file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)

   def  upload_files(e):
        
           
        uf = []
        if file_picker.result is not None and file_picker.result.files is not None:
            for f in file_picker.result.files:
                uf.append(
                    FilePickerUploadFile(
                        f.name,
                        upload_url=MyApp.page.get_upload_url(f.name, 600),
                    )
                )
          
            file_picker.upload(uf)
                      
            procesando = "./assets/"+"procesando.gif"
            load = ft.Image(src=procesando,
                            width=50,
                            height=50,
                            fit=ft.ImageFit.CONTAIN,
                            )
            loading = ft.ResponsiveRow([load])
            MyApp.page.add(loading)
            
            source ="./assets/"+str(f.name)
            salida ="./assets/output" + str(random.randint(3, 99999))+".png"
            # while not os.path.exists(source):
            #     time.sleep(0.2)
            #     time_counter += 1
            #     if time_counter > time_to_wait:
            #       break
            
            #btn_upload.visible=False
            #btn_upload.update()
            #btn_select_files.visible=False
            #btn_select_files.update()
            
           
          
            while True:
              if os.path.exists(source) :
                input = Image.open(source)
                input_array = np.array(input)
                output_array = remove(input_array)
                output_image = Image.fromarray(output_array)
                output_image.save(salida)
                break
            while True:
              if os.path.exists(salida) :
                loading.visible=False
                loading.update()
                MyApp.navigator.navigate(f'resultado',MyApp.page,(source,salida))
                break
           

   # hide dialog in a overlay
   MyApp.page.overlay.append(file_picker)
   btn_upload = ElevatedButton(
       "Upload",
       ref=upload_button,
       icon=icons.UPLOAD,
       on_click=upload_files,
       disabled=True,
   )
   btn_select_files = ElevatedButton(
       "Select file...",
       icon=icons.FOLDER_OPEN,
       on_click=lambda _: file_picker.pick_files(allow_multiple=False),
   )
   MyApp.page.add(
        btn_select_files,
        Column(ref=files),
        btn_upload,
    )
   


@route('info')
def info(MyApp:PageData):
    myAppBar=AppBar(
    title=Text("Info page. "),
    bgcolor="blue")  
    MyApp.set_appbar(myAppBar) 
    MyApp.page.add(Text(f'funciona info '))  
    btn_prueba = FilledButton('Resultado', on_click=lambda _:MyApp.navigator.navigate(f'resultado',MyApp.page,('hola','hola')))
    MyApp.page.add(btn_prueba)
    btn_home = ElevatedButton('home', on_click=lambda _: MyApp.navigator.navigate_homepage(MyApp.page, ('hola', 'hola')))
    MyApp.page.add(btn_home)
    
    
def descarga(item):
  image_url = "http://127.0.0.1/"+item
  r = requests.get(image_url) 
  
  with open("python_logo.png",'wb') as f: 
    f.write(r.content)    
    

@route('resultado')
def resultado(MyApp: PageData):
    
    MyApp.page.controls.clear()
    MyApp.page.update()
    myAppBar=AppBar(
    title=Text("Resultado"),
    bgcolor="blue")  
    MyApp.set_appbar(myAppBar) 
    if MyApp.arguments[0]=='hola':
      MyApp.page.add(
        Text("Debe cargar una imagen para ser procesada"))
    else:
      procesando = "./assets/"+"procesando.gif"
      load=ft.Image( src=procesando,
                    width=50,
                    height=50,
                    fit=ft.ImageFit.CONTAIN,
                )
      loading = ft.ResponsiveRow([load])
      MyApp.page.add(loading)
    btn_home = ElevatedButton('home', on_click=lambda _: MyApp.navigator.navigate_homepage(MyApp.page, ('hola', 'hola')))
    MyApp.page.add(btn_home)
    btn_prueba = FilledButton('Descargar', on_click=lambda _:descarga(MyApp.arguments[1]))  
    MyApp.page.add(btn_prueba)
    entrada=MyApp.arguments[0]
    salida=MyApp.arguments[1]
   
    
    
    while True:
      if os.path.exists(salida) :
            
                  
        antes = ft.Image(
            src=entrada,
            col={"md": 3},

            fit=ImageFit.CONTAIN,

        )
      
        intermedio = Text(MyApp.arguments[0], col={
                          "md": 2}, text_align=ft.TextAlign.CENTER)
        despues = ft.Image(src=salida,

                            col={"md": 3},
                            fit=ft.ImageFit.CONTAIN
                            )
      
        imagen_salida = ft.ResponsiveRow([
            antes, intermedio, despues


        ], alignment="center")
        
      
        MyApp.page.add(imagen_salida)
        antes.update()
        despues.update()
        imagen_salida.update()
        MyApp.page.update()
        loading.visible=False
        loading.update()
        break
    
   
   
    
   
    
    

@route(ROUTE_404)
def route_404(MyApp: PageData):
   MyApp.page.add(Text('funciona 404'))

# llamada a función principal o renderizada
#flet.app(target=main)
# ejecutar con web-app
flet.app(target=main,assets_dir="assets",upload_dir="assets", view=ft.AppView.WEB_BROWSER)
