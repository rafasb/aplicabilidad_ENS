# Formulario web con streamlit para definir la declaración de aplicabilidad del ENS
#

# Importación de librerías
import streamlit as st
import pandas as pd
from diccionarios import dict_grados
from diccionarios import dict_madurez
import json

st.session_state["columnas"] = []
st.session_state["dimensiones"] = ""

CODIGO,MARCO,AREA,DESC,DIM,APL,GRAD,MAD,DOC,CONT = [
    {"nombre":"código","título":"Código","ayuda":"Acrónimo de la medida de seguridad"},
    {"nombre":"marco","título":"Marco","ayuda":"Marco de referencia de la medida de seguridad"},
    {"nombre":"área","título":"Área","ayuda":"Área de aplicación de la medida de seguridad"},
    {"nombre":"descripción","título":"Descripción","ayuda":"Descripción de la medida de seguridad"},
    {"nombre":"dimensión","título":"Dimensión","ayuda":"Dimensión de la medida de seguridad"},
    {"nombre":"aplica","título":"Aplica","ayuda":"Indica si la medida de seguridad aplica o no"},
    {"nombre":"grado implementación","título":"Grado de implementación","ayuda":"Grado de implementación de la medida de seguridad"},
    {"nombre":"nivel madurez","título":"Nivel de madurez","ayuda":"Nivel de madurez de la medida de seguridad"},
    {"nombre":"aplicación","título":"Documento de aplicación","ayuda":"URL al documento de aplicación de la medida de seguridad"},
    {"nombre":"controles","título":"Documento de controles y evidencias","ayuda":"URL al documento de controles y evidencias de la medida de seguridad"}
]
COL = ["código", "marco", "area", "descripción", "dimensión", "aplica", "grado implementación", "nivel madurez", "aplicación", "controles"]

def cargar_medidas():
    # Se muestra el dataframe con el listado de medidas de seguridad
    with open('datos/medidas.json', 'r', encoding='utf-8') as f:
        medidas = json.load(f)
    return medidas

#Función para identificar si el parámetro no está definido y devolver un valor por defecto ""
def get_value(lista, param):
    # Verificar si la clave param existe en el diccionario lista
    if param not in lista:
        return ""
    else:
        return lista[param]

def get_index(lista, param, diccionario):
    if get_value(lista,param) == "":
        return 0
    else:
        return int (list(diccionario.values()).index(get_value(lista,param)))
    
def set_url(url):
    return f'<a href="{url}">{url}</a>'

def set_url_medidas(lista):
    for medida in lista:
        if get_value(medida,"aplicación") != "":
            medida["aplicación"] = set_url(medida["aplicación"])
        if get_value(medida,"controles") != "":
            medida["controles"] = set_url(medida["controles"])
    return lista

def columnas_activas(columna,nombre_columna):
    if columna.checkbox(nombre_columna, value=True):
        st.session_state["columnas"].append(nombre_columna)
    # else:
    #     st.session_state["columnas"].remove(nombre_columna)
    return st.session_state["columnas"]

def set_dimension(dimension):
    st.session_state["dimensiones"] = st.session_state["dimensiones"] + dimension
Marcos = ['organizativo', 'operacional', 'medidas de protección']

opcionesMenu = ['Listado de medidas de seguridad', 'Crear nueva medida de seguridad', 'Editar medida de seguridad']

# Configuración de la aplicación
st.set_page_config(page_title='Declaración de aplicabilidad del ENS', page_icon='🔒', layout='wide', initial_sidebar_state='expanded')

# Título de la aplicación
st.title('Declaración de aplicabilidad del ENS')

# Subtítulo de la aplicación
st.markdown('Aplicación web basada en Stremlit para definir la declaración de aplicabilidad del Esquema Nacional de Seguridad (ENS) en las entidades del sector público.')

# En el menu lateral se muestran las opciones de navegación
# La primera es mostrar la lista de medidas de seguridad
# La segunda es crear una nueva medida de seguridad
st.sidebar.header('Navegación')
menu = st.sidebar.radio('Ir a', opcionesMenu) 

if menu == 'Listado de medidas de seguridad':
    # Mostramos la lista de medidas
    st.header('Listado de medidas de seguridad')
    medidas = cargar_medidas()
    medidas = set_url_medidas(medidas)
    # mostramos un elemento expandible con las columnas de la lista de medidas de seguridad
    with st.expander('Columnas'):
        # Mediante un checkbox seleccionamos las columnas a mostrar
        col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
        columnas_activas(col1,CODIGO["nombre"])
        columnas_activas(col2,MARCO["nombre"])
        columnas_activas(col3,AREA["nombre"])
        columnas_activas(col4,DESC["nombre"])
        columnas_activas(col5,DIM["nombre"])
        columnas_activas(col6,APL["nombre"])
        columnas_activas(col7,GRAD["nombre"])
        columnas_activas(col8,MAD["nombre"])
        columnas_activas(col9,DOC["nombre"])
        columnas_activas(col10,CONT["nombre"])
        # st.write(st.session_state["columnas"])
    # Mostramos el dataframe con el listado de medidas de seguridad como una tabla con las URLs como enlaces
    # Eliminamos del dataframe las columnas que no se han seleccionado
    # medidas_df = pd.DataFrame(medidas)
    # medidas_df[st.session_state["columnas"]]
    st.write(pd.DataFrame(medidas)[st.session_state["columnas"]].to_html(escape=False, na_rep="", index=False), unsafe_allow_html=True)
elif menu == 'Crear nueva medida de seguridad':
    # Mediante un formulario solicitamos los campos de la medida de seguridad: código, descripción y marco  
    st.header('Crear nueva medida de seguridad')
    col1, col2 = st.columns(2)
    medida_seguridad = {}
    medida_seguridad[MARCO["nombre"]] = col1.selectbox(MARCO["título"], Marcos, help=MARCO["ayuda"])
    medida_seguridad[AREA["nombre"]] = col1.text_input(AREA["título"],placeholder='Monitorización del sistema', help=AREA["ayuda"]) 
    medida_seguridad[CODIGO["nombre"]] = col1.text_input(CODIGO["título"], '', placeholder='mp.mon.1', help=CODIGO["ayuda"])
    medida_seguridad[DESC["nombre"]] = col1.text_input(DESC["título"], placeholder='Detección de intrusión', help=DESC["ayuda"])
    medida_seguridad[APL["nombre"]] = col1.checkbox(APL["título"], help=APL["ayuda"])
    col1.write(DIM["título"])
    d1,d2,d3,d4,d5 = col1.columns(5)
    d1.checkbox('Confidencialidad', value=False, on_change=set_dimension("C"))
    d2.checkbox('Integridad', value=False, on_change=set_dimension("I"))
    d3.checkbox('Autenticidad', value=False, on_change=set_dimension("A"))
    d4.checkbox('Disponibilidad', value=False, on_change=set_dimension("D"))
    d5.checkbox('Trazabilidad', value=False, on_change=set_dimension("T"))
    medida_seguridad[DIM["nombre"]] = st.session_state["dimensiones"]
    medida_seguridad[GRAD["nombre"]] = col1.selectbox(GRAD["título"], list(dict_grados.values()), help=GRAD["ayuda"])  
    medida_seguridad[MAD["nombre"]] = col1.selectbox(MAD["título"], list(dict_madurez.values()), help=MAD["ayuda"])
    medida_seguridad[DOC["nombre"]] = col1.text_input(DOC["título"], placeholder='https://colabora.cacsa.eu', help=DOC["ayuda"])
    medida_seguridad[CONT["nombre"]] = col1.text_input(DOC["título"], placeholder='https://colabora.cacsa.eu', help=CONT["ayuda"])
    col2.write(medida_seguridad)

    # Mediante un botón añadimos el nuevo elemento a la lista de medidas de seguridad
    if col2.button('Añadir medida de seguridad'):
        # Cargamos la lista de medidas de seguridad
        lista_medidas = cargar_medidas()
        lista_medidas.append(medida_seguridad)
        col1.success('Medida de seguridad añadida correctamente')
        #Actualizamos el dataframe con el listado de medidas de seguridad
        df_medidas = pd.DataFrame(lista_medidas)
        df_medidas.to_csv('datos/medidas.csv', index=False)
        json_string = json.dumps(lista_medidas).encode('utf-8')
        with open('datos/medidas.json', 'w', encoding='utf-8') as f:
            json.dump(lista_medidas, f, ensure_ascii=False, indent=4)
        col1.success('Fichero guardado correctamente')
        menu = opcionesMenu[0]
elif menu == 'Editar medida de seguridad':
    st.header('Editar medida de seguridad')
    col1, col2 = st.columns(2)
    # Mediante un formulario solicitamos el campo de código de la medida de seguridad
    medida_editada = {}
    lista_medidas = cargar_medidas()
    codigos = [medida[CODIGO["nombre"]] for medida in lista_medidas]
    codigo = col1.selectbox(CODIGO["título"], codigos, help=CODIGO["ayuda"])
    indice = codigos.index(codigo)
    medida = lista_medidas[indice]
    medida_editada[CODIGO["nombre"]] = col1.text_input(f'Nuevo {CODIGO["título"]}', value=medida[CODIGO["nombre"]], help=CODIGO["ayuda"])
    medida_editada[MARCO["nombre"]] = col1.selectbox(MARCO["título"], Marcos, index=int (Marcos.index(medida[MARCO["nombre"]])), help=MARCO["ayuda"])
    medida_editada[AREA["nombre"]] = col1.text_input(AREA["título"], value=medida[AREA["nombre"]], help=AREA["ayuda"])
    medida_editada[DESC["nombre"]] = col1.text_input(DESC["título"], value=medida[DESC["nombre"]], help=DESC["ayuda"])
    medida_editada[DIM["nombre"]] = col1.text_input(DIM["título"], value=get_value(medida,DIM["nombre"]), help=DIM["ayuda"])
    medida_editada[APL["nombre"]] = col1.checkbox(APL["título"], value=get_value(medida,DIM["nombre"]), help=APL["ayuda"])
    medida_editada[GRAD["nombre"]] = col1.selectbox(GRAD["título"], list(dict_grados.values()), index=get_index(medida,GRAD["nombre"],dict_grados))  
    medida_editada[MAD["nombre"]] = col1.selectbox(MAD["título"], list(dict_madurez.values()), index=get_index(medida,MAD["nombre"],dict_madurez))
    medida_editada[DOC["nombre"]] = col1.text_input(DOC["título"], value=get_value(medida,DOC["nombre"]), help=DOC["ayuda"])
    medida_editada[CONT["nombre"]] = col1.text_area(CONT["título"], value=get_value(medida,CONT["nombre"]), help=CONT["ayuda"])
    lista_medidas[indice] = medida_editada
    col2.write(medida_editada)
    if col2.button('Modificar medida de seguridad'):
        df_medidas = pd.DataFrame(lista_medidas)
        df_medidas.to_csv('datos/medidas.csv', index=False)
        json_string = json.dumps(lista_medidas).encode('utf-8')
        with open('datos/medidas.json', 'w', encoding='utf-8') as f:
            json.dump(lista_medidas, f, ensure_ascii=False, indent=4)
        col1.success('Fichero guardado correctamente')
        menu = opcionesMenu[0]
