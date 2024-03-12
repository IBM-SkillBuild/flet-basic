# importaciones
import time
import flet
from flet import *



# función renderizada
def main(myApp: Page):
    # configuración de la app. Asignar atributos o propiedades al objeto de tipo Page
    myApp.title = "First Flet App"
    # myApp.vertical_alignment="center"
    myApp.window_resizable = True
    myApp.scroll='always'
    myApp.window_width = 480
    myApp.window_height = 640
    myApp.padding = 30
    myApp.window_always_on_top = True

    # funciones
    def color_de_titulo(e):
      titulo_cabecera.color=my_dropdown.value
      texto_presentacion.color = my_dropdown.value
      titulo_cabecera.update()
      texto_presentacion.update()
      my_dropdown.visible=False
      my_dropdown.update()
      Checkbox_opciones.label="ver opciones"
      Checkbox_opciones.value=False
      Checkbox_opciones.update()
    def Checkbox_opciones_change(e):
      if Checkbox_opciones.value:
        Checkbox_opciones.label="opciones actuales"
        Checkbox_opciones.value=True
        Checkbox_opciones.update()
        my_dropdown.visible=True
        my_dropdown.update()
       
      else:
        Checkbox_opciones.label="Ver opciones"  
        my_dropdown.visible=False
        my_dropdown.update()
        Checkbox_opciones.value=False
        Checkbox_opciones.update()  
    def actualizar_contador(data):

        contador.update()
        if contador.value == 0:
          contador.error_text = "(0) resultado inicial"
        else:
           contador.error_text = ""
        contador.update()
        texto_titulo = "Programado por Eduardo Cabrera"
        if data == "aumentar":
            texto_cambiar = "Aumentando contador a "
        else:
            texto_cambiar = "Disminuyendo contador a "
        for i in range(0, len(texto_cambiar)+1):
            texto_presentacion.value = texto_cambiar[:i]
            texto_presentacion.update()
            time.sleep(0.02)
        texto_presentacion.value += str(contador.value)
        texto_presentacion.update()
        for i in range(0, len(texto_titulo)+1):
            titulo_cabecera.value = texto_titulo[:i]
            titulo_cabecera.update()
            time.sleep(0.02)
           

    def disminuir(e):
        contador.value = int(contador.value)-1
        actualizar_contador("disminuir")
       
    def aumentar(e):
        contador.value = int(contador.value)+1
        actualizar_contador("aumentar")
       

    def reload_contador(e):
        contador.value = 0
        contador.error_text="(0) resultado inicial"
        texto_presentacion.value = "Contador Flet by E.Cabrera"
        titulo_cabecera.value = "Probando flet python 2024"
        myApp.update()

    # controles o componentes declarados incluido contenedor principal
    contador = TextField(label="contador",value=0, text_align='right', width=150)
    if contador.value==0:contador.error_text="(0) resultado inicial"
    contador.disabled = True
    texto_contador = Text(value="RESULTADO", text_align="center",italic=True)
    texto_presentacion = Text(
        value="Contador Flet by E.Cabrera", text_align="center", size=30)
    presentacion = Stack(
        [Row([texto_presentacion], alignment='center')], height=50)
    boton_menos = IconButton(icons.REMOVE, on_click=disminuir)
    boton_mas = IconButton(icons.ADD, on_click=aumentar)
    mis_botones = [boton_menos, boton_mas]
    contenedor = Stack([Row([texto_contador, contador], alignment='center')])
    botones = Row(mis_botones, alignment='center')
    titulo_cabecera = Text(value="Probando Flet Python 2024",size=30,color="green", italic=True,weight='bold')
    cabecera = Stack([titulo_cabecera], height=100)
    btn_menu = ElevatedButton('Reset contador', on_click=reload_contador)
    miboton = Stack([Row([btn_menu], alignment='center')], height=100)
    Checkbox_opciones=Checkbox(label="opciones previstas",value=False,on_change=Checkbox_opciones_change)
    my_dropdown = Dropdown(label="color de titulos", width=200,value="Green",visible=False,options=[
            dropdown.Option("Red"),
            dropdown.Option("Green"),
            dropdown.Option("Blue"),
        ],on_change=color_de_titulo
    )
       
    
    grupo_check_dropdown=Row([Checkbox_opciones,my_dropdown],height=100)
    # montaje de layaout por referencias tanto a rows(filas), a columnas,
    # o directamente a componentes (controles) etc.. usando variables asignadas anteriormente)
    imagen_entrada = Image(src=f"https://www.zooplus.es/magazine/wp-content/uploads/2022/05/Cuanto-pesa-un-gato-2.jpeg",
                    width=300,
                    height=300,
                    fit=ImageFit.CONTAIN,
                )
    myApp.add(imagen_entrada)
    myApp.add(grupo_check_dropdown,
              cabecera,
              presentacion,
              contenedor,
              botones,
              miboton)


# llamada a función principal o renderizada
#flet.app(target=main)
# ejecutar con web-app
flet.app(target=main, view=flet.WEB_BROWSER)
