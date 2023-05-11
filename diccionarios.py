#Detalle de aplicación de la medida de seguridad
medida_seguridad = {
    "código": "",
    "descripcion": "",
    "dimensiones": [],
    "aplicabilidad": "",
    "grado": "",
    "nivel": "",
    "documento": "",
    "evidencias": [],
    "comentarios": ""
}

dimensiones = {
    "D": "Disponibilidad",
    "I": "Integridad",
    "C": "Confidencialidad",
    "A": "Autenticidad",
    "T": "Trazabilidad",
    "V": "Verificación"
}

# Diccionario de categorías de seguridad de sistemas de información
categorias_sistema = {
    "A": "Alta",
    "M": "Media",
    "B": "Baja"
}

# Diccionario de niveles de seguridad
niveles_dimension = {
    "B": "Bajo",
    "M": "Medio",
    "A": "Alto",
    "NA": "No aplica"
}

impacto_dimension = {
    "Disposición legal": "",
    "Perjuicio directo": "",
    "Incumplimiento de norma": "",
    "Pérdidas económicas": "",
    "Reputación": "",
    "Protestas": "",
    "Delitos": "",
}

sistemas = {
    "información": {
        "confidencialidad": "",
        "integridad": "",
        "autenticidad": "",
        "trazabilidad": ""},
    "servicio": {
        "disponibilidad": "",
        "autenticidad": "",
        "trazabilidad": ""
    },
}

# Diccionario de grados de implantación
dict_grados = {
    "NI": "No implantado",
    "P": "en Proceso",
    "I": "Implantado"
}

# Diccionario de niveles de madurez
dict_madurez = {
    "L0": "Inexistente",
    "L1": "Inicial",
    "L2": "Repetible, pero intuitivo",
    "L3": "Proceso Definido",
    "L4": "Gestionado y Medible",
    "L5": "Optimizado"
}

lista_medidas = [
    {"código": "org.1",
        "descripción": "Política de seguridad",
        "marco": "organizativo"
    },
    {"código": "org.2",
        "descripción": "Normativa de seguridad",
        "marco": "organizativo"
    },
    {"código": "org.3",
        "descripción": "Procedimientos de seguridad",
        "marco": "organizativo"
    },
    {"código": "org.4",
        "descripción": "Proceso de autorización",
        "marco": "organizativo"
    },
    {"código": "op.pl.1",
        "descripción": "Análisis de riesgos",
        "marco": "operacional",
        "area": "planificación"
    },
    {"código": "op.pl.2",
        "descripción": "Arquitecura de seguridad",
        "marco": "operacional",
        "area": "planificación"
    },
    {"código": "op.pl.3",
        "descripción": "Adquisición de nuevos componentes",
        "marco": "operacional",
        "area": "planificación"
    },
    {"código": "op.pl.4",
        "descripción": "Dimensionamiento y gestión de capacidad",
        "marco": "operacional",
        "area": "planificación"
    },
    {"código": "op.pl.5",
        "descripción": "Componentes certificados",
        "marco": "operacional",
        "area": "planificación"
    },
]

dict_medidas = {
    "marco organizativo": {
        "código": "org",
        "medidas": [
            {"código": "org.1", 
                "descripción": "Política de seguridad"},
            {"código": "org.2",
                "descripción": "Normativa de seguridad"},
            {"código": "org.3",
                "descripción": "Procedimientos de seguridad"},
            {"código": "org.4",
                "descripción": "Proceso de autorización"}
        ]
    },
    "marco operacional": {
        "código": "op",
        "medidas": [
            {"código": "op.pl",
                "descripción": "Planificación"},
            {"código": "op.acc",
                "descripción": "Control de acceso"},
            {"código": "op.exp",
                "descripción": "Explotación"},
            {"código": "op.ext",
                "descripción": "Recursos Externos"},
            {"código": "op.nub",
                "descripción": "Servicios en la nube"},
            {"código": "op.cont",
                "descripción": "Continuidad del servicio"},
            {"código": "op.mon",
                "descripción": "Monitorización"}
        ]
    },
    "marco de protección": {
        "código": "mp",
        "categorías": [
            {"código": "mp.if",
                "descripción": "Protección de las instalaciones e infraestructuras",
                "medidas": []
                },
            {"código": "mp.per",
                "descripción": "Gestión de personal",
                "medidas": []
                },
            {"código": "mp.eq",
                "descripción": "Protección de los equipos",
                "medidas": []
                },
            {"código": "mp.com",
                "descripción": "Protección de las comunicaciones",
                "medidas": [
                    {"código": "mp.com.1",
                        "descripción": "Perímetro seguro",
                    },
                    {"código": "mp.com.2",
                        "descripción": "Protección de la confidencialidad"},
                    {"código": "mp.com.3",
                        "descripción": "Protección de la integridad y de la autenticidad"},
                    {"código": "mp.com.4",
                        "descripción": "Separación de flujos de información en la red"},
                ]
            },  
            {"código": "mp.si",
                "descripción": "Protección de los soportes de información",
                "medidas": []
            },
            {"código": "mp.sw",
                "descripción": "Protección de las aplicaciones informáticas",
                "medidas": []
            },
            {"código": "mp.info",
                "descripción": "Protección de la información",
                "medidas": []
            },
            {"código": "mp.s",
                "descripción": "Protección de los servicios",
                "medidas": []
            }
        ]
    }
}

# Declaración de aplicabilidad
declaracion_aplicabilidad = {
    "marco organizativo": {
        "código": "org",
        "medidas": [
            {"código": "org.1", 
                "descripción": "Política de seguridad"},
            {"código": "org.2",
                "descripción": "Normativa de seguridad"},
            {"código": "org.3",
                "descripción": "Procedimientos de seguridad"},
            {"código": "org.4",
                "descripción": "Proceso de autorización"}
        ]
    },
    "marco operacional": {
        "código": "op",
        "medidas": [
            {"código": "op.pl",
                "descripción": "Planificación"},
            {"código": "op.acc",
                "descripción": "Control de acceso"},
            {"código": "op.exp",
                "descripción": "Explotación"},
            {"código": "op.ext",
                "descripción": "Recursos Externos"},
            {"código": "op.nub",
                "descripción": "Servicios en la nube"},
            {"código": "op.cont",
                "descripción": "Continuidad del servicio"},
            {"código": "op.mon",
                "descripción": "Monitorización"}
        ]
    },
    "marco de protección": {
        "código": "mp",
        "categorías": [
            {"código": "mp.if",
                "descripción": "Protección de las instalaciones e infraestructuras",
                "medidas": []
                },
            {"código": "mp.per",
                "descripción": "Gestión de personal",
                "medidas": []
                },
            {"código": "mp.eq",
                "descripción": "Protección de los equipos",
                "medidas": []
                },
            {"código": "mp.com",
                "descripción": "Protección de las comunicaciones",
                "medidas": [
                    {"código": "mp.com.1",
                        "descripción": "Perímetro seguro",
                        "dimensiones": ["C", "I", "A"],
                        "aplicabilidad": "Sí",
                        "grado": "Implantado",
                        "nivel": "L3",
                        "documento": "https://www.ccn-cert.cni.es/seguridad-al-dia/guias-practicas/guias-ccn-stic/3009-guia-ccn-stic-3009.html",
                        "evidencias": ["https://www.ccn-cert.cni.es/seguridad-al-dia/guias-practicas/guias-ccn-stic/3009-guia-ccn-stic-3009.html"],
                        "comentarios": ""
                        },
                    {"código": "mp.com.2",
                        "descripción": "Protección de la confidencialidad"},
                    {"código": "mp.com.3",
                        "descripción": "Protección de la integridad y de la autenticidad"},
                    {"código": "mp.com.4",
                        "descripción": "Separación de flujos de información en la red"},
                ]
            },  
            {"código": "mp.si",
                "descripción": "Protección de los soportes de información",
                "medidas": []
            },
            {"código": "mp.sw",
                "descripción": "Protección de las aplicaciones informáticas",
                "medidas": []
            },
            {"código": "mp.info",
                "descripción": "Protección de la información",
                "medidas": []
            },
            {"código": "mp.s",
                "descripción": "Protección de los servicios",
                "medidas": []
            }
        ]
    }
}   


# Listado de columnas de la declaración de aplicabilidad
columnas = ["Dimensiones", "Medida", "Descripción", "Aplica", "Grado de Implementación", "Nivel de Madurez", "Enlace Documento Aplicabilidad", "Enlaces Directorio Evidencias"]






