####################################################################################
#################   Flet. first App Edu   ##########################################
####################################################################################

# importaciones necesarias
import flet
from flet import *
import time

####################################################################################
#################    (main) Punto de Entrada App            ########################
####################################################################################

def main(myApp: Page): # parametro myApp: Objeto instancia de la Clase Page de Flet
    # propiedades del objeto (aplicación) 
    myApp.vertical_alignment="center"
    myApp.window_resizable = True
    myApp.scroll = 'always'
    myApp.window_width = 480
    myApp.window_height = 640
    myApp.padding = 30
    myApp.window_always_on_top = True
   
    
    # definicion de titulos (titulo de App y de cabeceras de vistas/rutas)
    myApp.title = "Flet Python Edu"
    myApp.bar_title_home="Primera toma de contacto con Flet"
    myApp.bar_title_settings="Configuraciones"
    myApp.bar_title_info = "Información"
    
    
    ####################################################################################
    #################   zonas rutas (vistas)   #########################################
    ####################################################################################
    # por cada vista se cargan los controles 
    # por referencia a sus variables asignadas.
    # Ver contenido en Zona de controles (buscar:Ctrl +F) Escribir: Controles para ruta
   
    def route_change(e):
        color_para_titulos="green"
        # cambia color de titulos
        def color_de_titulo(e):
          global color_para_titulos
          color_para_titulos = str(my_dropdown.value)
          titulo_cabecera.color = str(my_dropdown.value)
          texto_presentacion.color = str(my_dropdown.value)
          titulo_cabecera.update()
          texto_presentacion.update()
          my_dropdown.visible = False
          my_dropdown.update()
          Checkbox_opciones.label = "ver opciones de color de titulo"
          Checkbox_opciones.value = False
          Checkbox_opciones.update()

        # muestra / oculta un dropdown de opciones
        def Checkbox_opciones_change(e):
          # muestra / oculta un dropdown de opciones
          if Checkbox_opciones.value:
            Checkbox_opciones.label = "opciones para color de titulos"
            Checkbox_opciones.value = True
            Checkbox_opciones.update()
            my_dropdown.visible = True
            my_dropdown.update()

          else:
            Checkbox_opciones.label = "Ver opciones para color de titulo"
            my_dropdown.visible = False
            my_dropdown.update()
            Checkbox_opciones.value = False
            Checkbox_opciones.update()

        # actualiza el control de contador y realiza algunas animaciones de titulos
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
            contador.error_text = "(0) resultado inicial"
            texto_presentacion.value = "Contador Flet by E.Cabrera"
            titulo_cabecera.value = "Probando flet python 2024"
            myApp.update()    
        
        
        # controles o componentes declarados incluido logica programación
        barra_titulo_home = AppBar(title=Text(myApp.bar_title_home),
                                  bgcolor=colors.SURFACE_VARIANT),
        contador = TextField(label="contador", value=0, text_align='right', width=150)
        if contador.value == 0: contador.error_text = "(0) resultado inicial"
        contador.disabled = True
        texto_contador = Text(value="RESULTADO", text_align="center", italic=True)
        texto_presentacion = Text(value="Contador Flet by E.Cabrera",
                                  text_align="center", color=color_para_titulos, size=30)
        myApp.presentacion = Stack(
            [Row([texto_presentacion], alignment='center')], height=50)
        boton_menos = IconButton(icons.REMOVE, on_click=disminuir)
        boton_mas = IconButton(icons.ADD, on_click=aumentar)
        mis_botones = [boton_menos, boton_mas]
        myApp.contenedor = Stack(
            [Row([texto_contador, contador], alignment='center')])
        myApp.botones = Row(mis_botones, alignment='center')
        titulo_cabecera = Text(value="Probando Flet Python 2024",
                               size=30, color=color_para_titulos, italic=True, weight='bold')
        myApp.cabecera = Stack([titulo_cabecera], height=100)
        btn_menu = ElevatedButton('Reset contador', on_click=reload_contador)
        myApp.miboton = Stack([Row([btn_menu], alignment='center')], height=100)
      
        Checkbox_opciones = Checkbox(
            label="Ver opciones para color de titulos", value=False, on_change=Checkbox_opciones_change)
        my_dropdown = Dropdown(label="color de titulos", width=200, value="Green", visible=False, options=[
            dropdown.Option("Red"),
            dropdown.Option("Green"),
            dropdown.Option("Blue"),
        ], on_change=color_de_titulo)
        myApp.grupo_check_dropdown = Row([Checkbox_opciones, my_dropdown], height=100)
      
        myApp.views.clear()
        myApp.views.append(
            View(
                "/",
                [
                    barra_titulo_home,
                    Row([ ElevatedButton("Go to settings", on_click=open_settings),
                    ElevatedButton("Go to Info", on_click=open_info_settings),]),
                    myApp.cabecera,
                    myApp.presentacion,
                    myApp.contenedor,
                    myApp.botones,
                    myApp.miboton,
                   
                ],
               
            )
        )
        if myApp.route == "/settings":
            myApp.views.append(
                View(
                    "/settings",
                    [
                        AppBar(title=Text(myApp.bar_title_settings),
                               bgcolor=colors.SURFACE_VARIANT),
                        Row([ElevatedButton("Go Home", on_click=open_home),
                             ElevatedButton("Go to Info", on_click=open_info_settings)]),
                        myApp.grupo_check_dropdown,
                        
                    ],
                  
                )
            )
        if myApp.route == "/info":
            myApp.views.append(
                View(
                    "/info",
                    [
                        AppBar(
                            title=Text(myApp.bar_title_info), bgcolor=colors.SURFACE_VARIANT
                        ),
                        ElevatedButton("Go Home", on_click=open_home),
                    ],
                   
                )
            )
        myApp.update()
    
    
####################################################################################
################   zonas definiciones de enrutamiento###############################
####################################################################################

    # para boton back del navegador
    def view_pop(e):
        print("View pop:", e.view)
        myApp.views.pop()
        top_view = myApp.views[-1]
        myApp.go(top_view.route)
        myApp.update()
        
    # eventos cambio de ruta
    myApp.on_route_change = route_change
    myApp.on_view_pop = view_pop
    
    ####################################################################################
    #################   redirigir a rutas (vistas)  ####################################
    ####################################################################################

    def open_home(e):
        myApp.go("/")
        
    def open_info_settings(e):
        myApp.go("/info")

    def open_settings(e):
        myApp.go("/settings")
        
        

    # ruta incial cargada
    myApp.go(myApp.route)
    ############################# fin de la función principal o punto de entrada
    




####################################################################################
#################   Zona de ejecución llamando a punto de entrada  #################
####################################################################################

# llamada a función principal o renderizada
#flet.app(target=main)
# ejecutar con web-app
flet.app(target=main, view=flet.WEB_BROWSER)
