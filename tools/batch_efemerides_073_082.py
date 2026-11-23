# -*- coding: utf-8 -*-
"""
Generador Agéntico Automatizado para Lote 7: Expedientes #073 a #082 (6 al 15 de septiembre)
1. Crea directorios en assets/efemerides/
2. Genera README.md y contenido-completo.md
3. Guarda guion-reel.txt y prompt-portada.txt
4. Genera portada.png (16:9 alta resolución con Pillow)
5. Sintetiza audio en Kokoro (speed 0.86, ~480-530 palabras -> ~3:00 a 3:30 min)
6. Convierte con ffmpeg a M4A y mide duración exacta
7. Inyecta en index.html con imagen: "portada.jpeg" y fallback automático a portada.png
"""

import os
import sys
import json
import subprocess

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

from kokoro_onnx import Kokoro
import soundfile as sf
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"C:\D DCT\programas\hsefemeride"
ASSETS_DIR = os.path.join(BASE_DIR, "assets", "efemerides")
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
MODEL_PATH = r"C:\kokoro\kokoro-v1.0.onnx"
VOICES_PATH = r"C:\kokoro\voices-v1.0.bin"

KOKORO_SPEED = 0.86
KOKORO_VOICE = "em_alex"
KOKORO_LANG = "es"

LOTE_7_DATA = [
    {
        "id": "073",
        "fecha": "06 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-06",
        "expediente": "Expediente #073",
        "carpeta": "2017-09-06-explosion-polvo-harina-silo",
        "titular": "LA NUBE QUE ARDIÓ: EXPLOSIÓN DE POLVO DE HARINA EN EL SILO",
        "palabraResaltada": "EXPLOSIÓN DE POLVO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Molino Harinero y Silos de Almacenamiento - 2017",
        "tipoRiesgo": "Atmósferas Explosivas (ATEX / Polvo Combustible)",
        "parrafos": [
            "El 6 de septiembre de 2017, una devastadora deflagración de polvo combustible en un molino harinero destruyó tres silos de hormigón y causó quemaduras críticas a cuatro operarios.",
            "La fricción de una correa desalineada en la cabeza del elevador de cangilones generó una temperatura superior a 400 °C. La chispa encendió una nube suspendida de polvo fino de trigo dentro del ducto.",
            "La onda de presión primaria levantó las capas de polvo sedimentadas en las vigas del galpón, desatando una explosión secundaria masiva. La lección: limpieza rigurosa, sensores de desalineación y venteos de alivio.",
        ],
        "puntosClave": [
            {"icono": "sparkles", "titulo": "Limpieza exhaustiva contra polvo fugitivo", "texto": "Capas de polvo de más de 0.8 mm (grosor de una moneda) bastan para propagar explosiones secundarias catastróficas."},
            {"icono": "activity", "titulo": "Sensores de desalineación y temperatura", "texto": "Instalar monitores de rotación, sensores de deslizamiento de banda y detección de calor en rodamientos de elevadores."},
            {"icono": "shield", "titulo": "Paneles de venteo y supresión de explosión", "texto": "Canalizar la onda de sobrepresión hacia zonas seguras al aire libre mediante paneles de alivio calibrados según NFPA 68."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: normas sobre prevención de incendios y explosiones de polvo en molienda y granos NFPA 61 / NFPA 652 y directrices de la OSHA (Combustible Dust National Emphasis Program).",
        "guionReel": (
            "¿Sabías que la harina común que usas para cocinar puede explotar con la fuerza de la dinamita?\n\n"
            "El 6 de septiembre de 2017, en un gran molino harinero, una correa de un elevador de granos comenzó a rozar contra el metal de la carcasa.\n\n"
            "El roce levantó chispas a 400 grados. Adentro del ducto había una nube invisible de polvo de harina flotando en el aire.\n\n"
            "Al tocar la chispa, el polvo detonó en una bola de fuego. La onda expansiva sacudió todo el galpón, levantó el polvo que estaba acumulado sobre los techos y desató una segunda explosión colosal.\n\n"
            "Tres silos de hormigón volaron en pedazos y cuatro operarios quedaron con quemaduras graves.\n\n"
            "El polvo orgánico es explosivo puro: exige limpieza constante, sensores de temperatura y paneles de alivio de presión.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Industrial grain mill explosion aftermath documentary photography, September 6 2017, massive industrial flour milling facility. "
            "Reinforced concrete grain silo cracked open with black scorch marks, pulverized white flour and charred soot dust covering industrial yard floor, "
            "twisted metal bucket elevator leg bent by internal blast, emergency fire crews spraying water monitors, dramatic sunset lighting, 16:9 ratio."
        ),
        "guionLargo": (
            "El seis de septiembre de dos mil diecisiete... en las instalaciones de un importante complejo molinero e industrial de cereales... la física de los polvos combustibles desató una catástrofe arrolladora... "
            "En la torre de transferencia de granos y harinas... un elevador vertical de cangilones operaba a régimen continuo elevando producto pulverizado hacia la batería de silos de almacenamiento... "
            "En la cabeza motriz superior... una de las poleas tensoras presentaba un leve desvío angular... provocando que la banda gruesa de caucho comenzara a rozar de manera ininterrumpida contra la chapa de acero de la carcasa protectora... "
            "La fricción mecánica continua elevó la temperatura localizada del metal por encima de los cuatrocientos grados centígrados... generando puntos incandescentes y chispas por fricción... "
            "En el interior confinado del ducto... el movimiento incesante de los cangilones mantenía una densa suspensión de partículas microscópicas de harina de trigo... en una concentración que superaba el límite inferior de explosividad de sesenta gramos por metro cúbico... "
            "Apenas una chispa entró en contacto con la nube suspendida... la combustión deflagrante se propagó a velocidad supersónica a lo largo de la columna vertical... "
            "La deflagración primaria... aunque severa... fue solo el detonante inicial... "
            "La onda de choque resultante recorrió las galerías subterráneas y las naves de molienda... sacudiendo las vigas, ductos y luminarias superiores... donde durante meses se habían acumulado capas de polvo fugitivo de apenas dos milímetros de espesor... "
            "Esa sacudida arrojó miles de kilos de polvo acumulado al aire de los galpones... formando una gigantesca nube suspendida secundaria que encontró de inmediato la llamarada del elevador... "
            "La explosión secundaria resultante fue de una violencia demoledora... Reventó las paredes de hormigón armado de tres silos de cuarenta metros de altura... arrancó techos parabólicos y provocó quemaduras de tercer grado en cuatro operarios que cumplían tareas en el sector de embolsado... "
            "Las investigaciones de la autoridad laboral recordaron que en la industria alimenticia y cerealera... el polvo no es simple suciedad... es combustible de alta reactividad... "
            "La norma internacional NFPA sesenta y uno exige la instalación de paneles de venteo de explosión canalizados al exterior... sistemas automáticos de extinción por supresión química... y una rutina innegociable de limpieza al vacío... "
            "Porque ante el polvo en suspensión... una chispa inadvertida basta para demoler una fábrica entera."
        )
    },
    {
        "id": "074",
        "fecha": "07 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-07",
        "expediente": "Expediente #074",
        "carpeta": "2018-09-07-aplastamiento-tolva-hidraulica-loto",
        "titular": "LA TOLVA QUE CAYÓ A PLOMO: EL MECÁNICO Y LA ENERGÍA CERO",
        "palabraResaltada": "TOLVA QUE CAYÓ",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Taller de Mantenimiento de Maquinaria Pesada y Minería - 2018",
        "tipoRiesgo": "Energía Hidráulica / Bloqueo y Etiquetado (LOTO)",
        "parrafos": [
            "El 7 de septiembre de 2018, un mecánico de 39 años murió aplastado al descender repentinamente la tolva de un camión volcador de 40 toneladas mientras reparaba una fuga de aceite debajo de la caja.",
            "El operario había levantado la tolva con el circuito hidráulico pero no colocó el puntal mecánico de seguridad incorporado al chasis ni calzos de retención. Al aflojar una válvula, la línea perdió presión súbitamente.",
            "La caja de acero de ocho toneladas cayó como una guillotina. La regla básica de LOTO: la presión hidráulica no es un freno mecánico; jamás situarse bajo una carga sostenida solo por fluidos.",
        ],
        "puntosClave": [
            {"icono": "shield-alert", "titulo": "Colocación obligatoria de puntales mecánicos", "texto": "Toda tolva o compuerta elevada debe bloquearse físicamente con barras metálicas de retención antes de ingresar debajo."},
            {"icono": "lock", "titulo": "Despresurización y energía cero (LOTO)", "texto": "Bloquear el comando de elevación con candado, apagar el motor y purgar la presión hidráulica residual del circuito."},
            {"icono": "ban", "titulo": "Prohibido confiar en válvulas o mangueras", "texto": "Las mangueras y sellos pueden fallar en microsegundos; el fluido hidráulico jamás debe considerarse un soporte rígido."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: manuales de mantenimiento de camiones fuera de ruta de MSHA (Mine Safety and Health Administration) y normativas de control de energías peligrosas OSHA 1910.147.",
        "guionReel": (
            "¿Te meterías debajo de una caja de acero de ocho toneladas sostenida solo por una manguera de goma?\n\n"
            "El 7 de septiembre de 2018, en un taller de minería, un mecánico debía cambiar una válvula abajo de la caja de un camión volcador.\n\n"
            "Arrancó el motor, subió la tolva hidráulica y se metió abajo a trabajar con una llave inglesa.\n\n"
            "El camión tenía un puntal de acero de seguridad al costado, pero como 'era un trabajito de dos minutos', no lo puso.\n\n"
            "Al desenroscar el conector, el aceite salió a chorros. Al perder la presión hidráulica, la enorme caja de acero cayó a plomo como una trampa para ratones, aplastándolo en el acto.\n\n"
            "Grábatelo para siempre: la presión hidráulica nunca es un soporte de seguridad. Usa siempre trabas mecánicas de acero.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Heavy industrial vehicle maintenance workshop photography, large off-highway yellow mining dump truck bed lowered completely on chassis. "
            "Heavy steel safety prop strut lying unused pinned on the side rail, scattered hydraulic oil spill on concrete floor, dropped wrenches, "
            "emergency response yellow tape, harsh directional overhead workshop floodlights, somber realistic photojournalism, 16:9 ratio."
        ),
        "guionLargo": (
            "El siete de septiembre de dos mil dieciocho... en la nave central de maestranza de un campamento minero... un exceso de confianza frente a la energía hidráulica acumulada cobró la vida de un técnico mecánico de primera línea... "
            "El operario... con casi dos décadas de experiencia en el mantenimiento de equipos pesados fuera de ruta... fue asignado a diagnosticar un goteo de aceite en la válvula de control del cilindro telescópico de un camión volcador de cuarenta toneladas... "
            "Para acceder al múltiple de válvulas situado sobre el bastidor del chasis... el trabajador subió a la cabina... encendió el motor diésel y accionó la palanca hidráulica para izar la pesada tolva de volteo a su máxima altura... "
            "El vehículo disponía en su lateral de una barra puntal de acero estructural... diseñada de fábrica para encastrarse como traba mecánica positiva entre el chasis y la caja elevada... impidiendo cualquier descenso accidental... "
            "Confiado en que se trataba de un ajuste menor que apenas le demandaría un par de minutos... el mecánico descendió de la cabina y omitió colocar el puntal... "
            "Tampoco apagó el motor ni colocó candados de bloqueo y etiquetado en la palanca de mando... "
            "Se posicionó de pie directamente en la línea de fuego... justo debajo de la mole de acero de más de ocho toneladas suspendida en el aire... "
            "Al calzar la llave fija sobre el racor del conector flexible y aplicar torque para aflojar la pieza... la junta tórica gastada cedió de golpe... "
            "El fluido hidráulico presurizado a más de doscientas atmósferas fue expulsado con violencia... liberando instantáneamente la columna de sustentación de los cilindros... "
            "Sin la resistencia del fluido y sin ningún calzo mecánico que la sostuviera... la descomunal caja cayó a plomo por gravedad en una fracción de segundo... "
            "El trabajador fue aplastado contra los largueros del chasis... falleciendo en el acto por traumatismos múltiples torácicos y abdominales... "
            "Las investigaciones de la administración de seguridad minera recordaron un principio fundacional de la seguridad mecánica... Los fluidos y circuitos hidráulicos jamás son barreras mecánicas de soporte... "
            "Toda intervención bajo tolvas, brazos o compuertas elevadas exige de forma innegociable la colocación previa de puntales mecánicos certificados... el bloqueo LOTO de comandos... y la despresurización total de las líneas... "
            "Porque ante toneladas de acero suspendidas... una manguera de goma no es un seguro de vida."
        )
    },
    {
        "id": "075",
        "fecha": "08 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-08",
        "expediente": "Expediente #075",
        "carpeta": "1966-09-08-explosion-dow-chemical-plaquemine",
        "titular": "EL REACTOR QUE SUPERÓ EL LÍMITE: DOW CHEMICAL PLAQUEMINE",
        "palabraResaltada": "DOW CHEMICAL",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Química Dow Chemical, Plaquemine, Louisiana, EE.UU. - 1966",
        "tipoRiesgo": "Seguridad de Procesos (PSM) / Sistemas Instrumentados de Seguridad",
        "parrafos": [
            "El 8 de septiembre de 1966, una explosión de gran magnitud sacudió la unidad de hidrocarburos de Dow Chemical en Plaquemine al sobrepresurizarse un reactor de polimerización.",
            "Una pérdida de control en la adición de catalizadores generó una reacción exotérmica violenta. Los instrumentos de control básico fallaron simultáneamente con los lazos de refrigeración, careciendo de un sistema instrumentado de seguridad (SIS) independiente.",
            "La rotura de la envolvente liberó gases ligeros inflamables que encendieron en una inmensa bola de fuego. La tragedia impulsó la separación estricta entre control operativo y sistemas de parada de emergencia (ESD).",
        ],
        "puntosClave": [
            {"icono": "shield-check", "titulo": "Independencia de los sistemas SIS y DCS", "texto": "Los lazos de seguridad instrumentada (SIS/ESD) deben ser física y lógicamente independientes del control básico de proceso (BPCS)."},
            {"icono": "gauge", "titulo": "Alivio de sobrepresión sobredimensionado", "texto": "Dimensionar discos de ruptura y válvulas PSV contemplando escenarios de reacción exotérmica descontrolada (runaway)."},
            {"icono": "thermometer", "titulo": "Inhibición y enfriamiento de emergencia", "texto": "Contar con sistemas de inyección automática de agentes de parada de reacción (kill systems) ante aumentos bruscos de temperatura."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: registros históricos de incidentes de procesos químicos del CCPS (Center for Chemical Process Safety) y normas internacionales de seguridad funcional IEC 61511 / ISA 84.",
        "guionReel": (
            "¿Por qué el sistema que maneja una planta química nunca debe ser el mismo que la apaga en una emergencia?\n\n"
            "El 8 de septiembre de 1966, en la planta de Dow Chemical en Plaquemine, un reactor químico empezó a calentarse fuera de control.\n\n"
            "Un exceso de catalizador aceleró la reacción. El sensor de temperatura que debía avisar estaba conectado a la misma computadora que regulaba el flujo de refrigerante... y se trabó.\n\n"
            "Como no existía un sistema de parada de emergencia independiente, nadie vio venir la catástrofe.\n\n"
            "La presión reventó el reactor de acero como una lata de refresco, lanzando una nube inflamable que ardió en una bola de fuego colosal.\n\n"
            "A partir de este siniestro nació una regla de oro en ingeniería: el sistema de seguridad instrumentada debe ser completamente independiente del control operativo.\n\n"
            "La redundancia salva vidas."
        ),
        "promptImagen": (
            "Historical chemical manufacturing plant disaster documentary photography, September 8 1966 Dow Chemical Plaquemine Louisiana. "
            "Ruptured chemical polymerization reactor vessel surrounded by towering flames and twisted structural pipe racks, "
            "chemical operators in vintage 1960s protective helmets directing high-volume fire monitor foam streams, Mississippi river petrochemical scenery in distance, 16:9 ratio."
        ),
        "guionLargo": (
            "El ocho de septiembre de mil novecientos sesenta y seis... en el gigantesco complejo petroquímico de Dow Chemical ubicado en Plaquemine, Louisiana... un fallo en las capas de protección de un reactor químico desató una detonación de gran poder destructivo... "
            "En la unidad de síntesis de polímeros... un reactor continuo operaba bajo estrictas condiciones de temperatura y presión para transformar olefinas ligeras en cadenas moleculares pesadas... "
            "La reacción de polimerización es intrínsecamente exotérmica... lo que significa que libera ingentes cantidades de calor térmico que deben ser extraídas de forma permanente mediante camisas de enfriamiento y recirculación de agua helada... "
            "Durante el cambio de turno... una anomalía en las bombas de dosificación inyectó un caudal excesivo de catalizador organometálico en el interior del recipiente... "
            "La tasa de generación de calor superó instantáneamente la capacidad de remoción térmica del sistema de refrigeración... iniciando una reacción en cadena fuera de control... conocida técnicamente como runaway químico... "
            "En aquellos años... los lazos de medición y las alarmas operativas compartían los mismos transmisores y circuitos lógicos que los mecanismos de corte de emergencia... "
            "Al colapsar el controlador básico... los operadores en la sala de mando recibieron lecturas erráticas que enmascararon el vertiginoso incremento de la presión interna... "
            "Sin un sistema instrumentado de seguridad independiente con función de disparo automático... ni sistemas de inyección de inhibidores químicos de parada rápida... el reactor continuó presurizándose... "
            "En cuestión de minutos... la presión hidrodinámica pulverizó los límites de resistencia del acero... desgarrando el cuerpo cilíndrico del reactor en dos mitades... "
            "Toneladas de hidrocarburos ligeros en fase vapor escaparon con un estruendo ensordecedor... encontrando fuentes de ignición en hornos cercanos y desatando una masiva explosión e incendio generalizado... "
            "El accidente de Plaquemine sentó las bases de la moderna ingeniería de seguridad funcional... "
            "Impulsó la creación de las normativas internacionales IEC sesenta y uno quinientos once... las cuales exigen que los sistemas instrumentados de seguridad sean física, lógica y energéticamente autónomos del control operativo básico... "
            "Porque en procesos de alta energía... depender de una sola línea de control es una invitación directa al desastre."
        )
    },
    {
        "id": "076",
        "fecha": "09 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-09",
        "expediente": "Expediente #076",
        "carpeta": "2010-09-09-explosion-gasoducto-san-bruno",
        "titular": "LA SOLDADURA OCULTA DE 1956: LA EXPLOSIÓN DE SAN BRUNO",
        "palabraResaltada": "SAN BRUNO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Línea 132 de Gas Natural, San Bruno, California, EE.UU. - 2010",
        "tipoRiesgo": "Seguridad de Procesos (Ductos) / Integridad y Registros Históricos",
        "parrafos": [
            "El 9 de septiembre de 2010, la rotura catastrófica del gasoducto de 30 pulgadas Línea 132 de PG&E arrasó un barrio residencial en San Bruno, California, causando 8 muertos y destruyendo 38 viviendas.",
            "Una falla en una estación reguladora provocó un pico de presión. El ducto, instalado en 1956, contenía una soldadura longitudinal defectuosa de fábrica que no figuraba en los planos oficiales de la empresa.",
            "La empresa operaba el ducto a presiones elevadas basándose en registros históricos incompletos y sin pruebas hidrostáticas modernas. Una lección monumental sobre trazabilidad de diseño y gestión de integridad de ductos.",
        ],
        "puntosClave": [
            {"icono": "file-search", "titulo": "Trazabilidad documental fidedigna (As-built)", "texto": "Los registros de diseño y fabricación de ductos deben ser trazables, verificables y completos; jamás basar la presión de operación en supuestos."},
            {"icono": "gauge", "titulo": "Pruebas hidrostáticas de resistencia", "texto": "Someter los ductos antiguos a ensayos de presión hidrostática para validar su aptitud para el servicio ante picos de sobrepresión."},
            {"icono": "radio", "titulo": "Válvulas de corte automático de emergencia (ASV)", "texto": "Instalar válvulas accionadas por caída de presión para aislar ductos de gran porte en minutos y no demorar horas en cierres manuales."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe final de investigación de desastres por ductos de la Junta Nacional de Seguridad en el Transporte de EE.UU. (NTSB Report NTSB/PAR-11/01) sobre la explosión de San Bruno.",
        "guionReel": (
            "¿Puede un error de soldadura cometido hace cincuenta años hacer estallar un barrio entero hoy?\n\n"
            "El 9 de septiembre de 2010, en San Bruno, California, una llamarada de trescientos metros de altura destruyó treinta y ocho casas y mató a ocho personas.\n\n"
            "Bajo las calles pasaba un gasoducto de alta presión de 30 pulgadas instalado en 1956. En los planos de la empresa figuraba como caño sin costura de máxima calidad.\n\n"
            "Pero era falso. Habían usado pedazos de caños de descarte con soldaduras mal hechas y nunca lo anotaron en los registros.\n\n"
            "Esa tarde hubo una pequeña subida de presión en la red. La soldadura podrida no aguantó y reventó expulsando un tramo de caño de trece metros por el aire.\n\n"
            "En ductos de transporte, los planos deben ser 100% reales y las pruebas hidrostáticas obligatorias. Lo que se ignora bajo tierra, destruye en superficie.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Suburban pipeline disaster documentary photography, September 9 2010 San Bruno California PG&E natural gas pipeline explosion. "
            "Massive smoking crater in the middle of suburban asphalt road intersection, shattered gas pipeline piece lying thrown on sidewalk, "
            "burned foundations of destroyed residential houses, towering glow of fire reflected on neighborhood streets, aerial high-angle view, 16:9 ratio."
        ),
        "guionLargo": (
            "El nueve de septiembre de dos mil diez... a las seis y once de la tarde... una explosión colosal sacudió el apacible barrio residencial de Crestmoor en San Bruno, California... a escasos kilómetros del aeropuerto de San Francisco... "
            "Bajo el asfalto de las calles residenciales... enterrado a poco más de un metro de profundidad... discurría el gasoducto Línea ciento treinta y dos de la empresa Pacific Gas and Electric... una cañería troncal de acero de treinta pulgadas de diámetro que transportaba gas natural a alta presión... "
            "Durante tareas de mantenimiento rutinarias en una estación reguladora distante... un fallo de alimentación eléctrica descalibró una válvula de control... provocando un transitorio hidráulico de sobrepresión en la red... "
            "La presión se elevó moderadamente... manteniéndose dentro del límite máximo admisible de operación que figuraba en los registros informáticos de la compañía... "
            "Sin embargo... aquellos registros eran profundamente erróneos... "
            "En los planos oficiales archivados... constaba que ese tramo de ducto... instalado en mil novecientos cincuenta y seis... estaba construido con tuberías de acero de pared gruesa sin costura... "
            "La realidad era aterradora... La investigación de la Junta Nacional de Seguridad en el Transporte descubrió que la empresa había soldado en campo varios retazos de tubería de segunda selección con costuras longitudinales deficientes... que apenas estaban unidas en un cincuenta por ciento de su espesor... "
            "Durante más de medio siglo... el defecto metalúrgico permaneció oculto bajo tierra... tolerando los ciclos de presión pero acumulando microfisuras por fatiga... "
            "El pico de presión de aquella tarde fracturó la costura defectuosa... "
            "Un segmento de cañería de más de trece metros de longitud y tres toneladas de peso fue arrancado a presión y eyectado a treinta metros de distancia... abriendo un cráter inmenso en la calle... "
            "El gas natural liberado encendió de inmediato en un soplete de fuego de trescientos metros de altura que calcinó treinta y ocho viviendas... cobrándose la vida de ocho personas y dejando a decenas de heridos graves... "
            "Las cuadrillas demoraron más de noventa minutos en cerrar manualmente las válvulas para aislar el flujo... "
            "El desastre de San Bruno redefinió la legislación de ductos en todo el mundo... "
            "Estableció que las empresas operadoras deben certificar la trazabilidad documental exhaustiva de cada milímetro de cañería... realizar ensayos hidrostáticos de resistencia... e instalar válvulas de cierre automático por caída de presión... "
            "Porque cuando los registros de ingeniería son ficticios... el riesgo subterráneo se convierte en una amenaza latente para la comunidad."
        )
    },
    {
        "id": "077",
        "fecha": "10 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-10",
        "expediente": "Expediente #077",
        "carpeta": "2019-09-10-caida-tablon-pasarela-obra",
        "titular": "EL TABLÓN QUEBRADO: LA CAÍDA EN LA PASARELA DE OBRA",
        "palabraResaltada": "TABLÓN QUEBRADO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Obra en Construcción de Edificio Comercial - 2019",
        "tipoRiesgo": "Trabajo en Altura / Superficies de Tránsito Provisorias",
        "parrafos": [
            "El 10 de septiembre de 2019, un peón de obra de 24 años sufrió traumatismos múltiples severos al fracturarse el tablón de madera sobre el que caminaba cruzando un hueco de escalera a cuatro metros de altura.",
            "La pasarela improvisada utilizaba un único tablón de pino de descarte que presentaba nudos ciegos y rajaduras visibles. La madera no contaba con marcado de calidad para andamiaje y la pasarela carecía de barandas rígidas.",
            "Al apoyar el pie en el centro del vano, la madera quebró por flexión arrojando al trabajador al piso inferior. La lección: pasarelas metálicas normalizadas o doble tablón seleccionado con barandilla perimetral.",
        ],
        "puntosClave": [
            {"icono": "check-square", "titulo": "Madera clasificada estructural para andamios", "texto": "Prohibido usar madera común de encofrado; exigir tablones específicos para andamio sin nudos ni fisuras transversales."},
            {"icono": "layers", "titulo": "Ancho mínimo y doble apoyo (Mínimo 60 cm)", "texto": "Toda pasarela de tránsito en altura debe tener al menos 60 cm de ancho (doble o triple tablón trabado entre sí)."},
            {"icono": "shield", "titulo": "Barandas reglamentarias completas", "texto": "Instalar baranda superior a 1 metro, baranda intermedia a 50 cm y rodapié de 15 cm a ambos lados de cualquier pasarela provisoria."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: normativas de plataformas y pasarelas de trabajo en construcción de OSHA 1926.451 / 1926.502 y normativa europea EN 12811.",
        "guionReel": (
            "¿Cruzarías un hueco de cuatro metros de profundidad caminando sobre una simple tabla de madera vieja?\n\n"
            "El 10 de septiembre de 2019, en una obra en construcción, un peón de 24 años debía cruzar de una losa a otra sobre el hueco de la escalera.\n\n"
            "Para no dar toda la vuelta, colocaron un tablón de pino de obra apoyado de lado a lado. Sin barandas, sin fijaciones y con un nudo seco justo en el centro.\n\n"
            "El joven cargaba dos baldes con mezcla. Cuando pisó el centro del tablón, la madera crujió y se partió en dos como una galletita.\n\n"
            "Cayó cuatro metros al vacío sobre los hierros de la losa inferior: fractura de pelvis, columna y meses en rehabilitación.\n\n"
            "Las pasarelas provisorias no se improvisan: tablones metálicos o madera certificada sin nudos, mínimo 60 centímetros de ancho y barandas a ambos lados.\n\n"
            "Tu vida no puede depender de una tabla podrida."
        ),
        "promptImagen": (
            "Construction site building interior documentary photography, four-meter deep stairwell opening in raw concrete floor slab. "
            "Fractured splintered wooden scaffold plank broken in half dangling over void, dropped builders buckets and scattered fresh wet mortar, "
            "rebar starter bars sticking up from concrete below, temporary wooden guardrail broken, realistic construction documentary, 16:9 ratio."
        ),
        "guionLargo": (
            "El diez de septiembre de dos mil diecinueve... en la estructura de hormigón armado de un edificio comercial en plena fase de albañilería gruesa... un atajo en la circulación peatonal provocó un grave siniestro laboral... "
            "En el segundo piso de la obra... una abertura rectangular de tres metros de luz... destinada al futuro hueco de la caja de escaleras... separaba el sector de acopio de mezcla del frente de mampostería... "
            "Para ahorrar tiempo y evitar el rodeo de más de cuarenta metros que demandaba utilizar las pasarelas seguras habilitadas... los operarios habían tendido un puente improvisado sobre el vano abierto... "
            "La pasarela consistía en un único tablón de madera de pino de dos pulgadas de espesor y treinta centímetros de ancho... apoyado precariamente sobre las losas de hormigón en ambos extremos... sin clavadores de fijación ni tacos de retención que impidieran su desplazamiento lateral... "
            "La madera utilizada era material de descarte proveniente de tareas anteriores de encofrado... saturada de humedad y con varios nudos pasantes y grietas longitudinales evidentes en la fibra... "
            "Para colmo... el paso carecía por completo de barandas de protección lateral y rodapiés reglamentarios... "
            "Un peón de albañilería de veinticuatro años... transportando dos baldes cargados con mortero de cemento que sumaban más de treinta kilos de sobrecarga... inició el cruce de la pasarela... "
            "Al apoyar su pie derecho en el centro exacto de la luz... donde el momento flector alcanza su valor máximo... la madera no resistió el esfuerzo de tracción... "
            "El tablón se quebró de manera abrupta a la altura del nudo ciego... partiéndose limpiamente en dos pedazos... "
            "El operario se precipitó al vacío desde una altura de cuatro metros... impactando contra el suelo de hormigón del piso inferior y golpeando contra puntales y hierros de armadura... "
            "Sufrió fracturas múltiples en miembros inferiores... fisura de vértebras lumbares y traumatismos de severa consideración... "
            "Las normativas de seguridad en la construcción son categóricas... Queda terminantemente prohibido improvisar pasarelas de tránsito con tablones individuales o maderas no clasificadas... "
            "Toda pasarela provisoria en altura debe ejecutarse preferentemente con plataformas metálicas antideslizantes o doble tablón estructural trabado... con un ancho mínimo de sesenta centímetros... y barandas rígidas dobles instaladas a ambos márgenes... "
            "Porque en una obra... pisar sobre seguro es el primer principio de la prevención."
        )
    },
    {
        "id": "078",
        "fecha": "11 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-11",
        "expediente": "Expediente #078",
        "carpeta": "2015-09-11-colapso-grua-torre-la-meca",
        "titular": "EL VIENTO Y LA PLUMA: EL COLAPSO DE LA GRÚA EN LA MECA",
        "palabraResaltada": "GRÚA EN LA MECA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Gran Mezquita de La Meca (Masjid al-Haram), Arabia Saudita - 2015",
        "tipoRiesgo": "Izaje Crítico / Condiciones Meteorológicas Adversas",
        "parrafos": [
            "El 11 de septiembre de 2015, una gigantesca grúa sobre orugas Liebherr LR 11350 colapsó sobre el patio de la Gran Mezquita de La Meca durante una fuerte tormenta, dejando 111 peregrinos muertos y más de 300 heridos.",
            "La pluma principal de más de 190 metros de longitud permanecía izada a un ángulo pronunciado de 85 grados fuera de servicio, desoyendo el manual del fabricante que exigía bajarla al suelo ante vientos superiores.",
            "Tampoco se liberó el freno de giro para que la grúa pudiera ponerse en posición de veleta (weathervaning). Ráfagas de 80 km/h volcaron la estructura hacia atrás. Una lección colosal sobre izaje y alertas meteorológicas.",
        ],
        "puntosClave": [
            {"icono": "wind", "titulo": "Posición de veleta (Weathervaning) obligatoria", "texto": "Liberar los frenos de giro para permitir que la estructura rote libremente alineándose con la dirección del viento dominante."},
            {"icono": "book-open", "titulo": "Cumplimiento estricto del manual del fabricante", "texto": "Respetar los ángulos de pluma y límites de velocidad de viento establecidos para la condición de fuera de servicio."},
            {"icono": "cloud-rain", "titulo": "Protocolo ante alertas meteorológicas tempranas", "texto": "Monitoreo anemométrico continuo y descenso preventivo de plumas largas antes del arribo de tormentas severas."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe pericial de la Comisión de Investigación del Gobierno de Arabia Saudita y boletines técnicos de seguridad en grúas sobre orugas de FEM / Liebherr.",
        "guionReel": (
            "¿Sabías que una de las grúas más grandes del mundo colapsó matando a 111 personas por no seguir una página del manual de instrucciones?\n\n"
            "El 11 de septiembre de 2015, en la Gran Mezquita de La Meca, operaba una grúa sobre orugas gigante con una pluma de casi doscientos metros de altura.\n\n"
            "Se desató una tormenta de arena con vientos de 80 kilómetros por hora.\n\n"
            "El manual del fabricante decía claramente: ante vientos fuertes, baje la pluma al piso o déjela libre para que gire como una veleta. Pero la dejaron clavada a 85 grados, con los frenos de giro trabados.\n\n"
            "El viento pegó de costado como una vela de barco. La mole de cientos de toneladas no aguantó, volcó hacia atrás y cayó directo sobre el techo de la mezquita repleta de fieles.\n\n"
            "Las instrucciones de seguridad de los fabricantes de grúas son leyes sagradas. Con el clima no se juega.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Dramatic historical crane disaster documentary photography, September 11 2015 Grand Mosque Mecca crane collapse. "
            "Massive red and white lattice boom crawler crane collapsed backward onto Islamic architectural stone arches and courtyard floor, "
            "heavy dusk sandstorm sky with intense wind blowing debris, emergency rescue lights illuminating solemn catastrophic scene, photorealistic, 16:9 ratio."
        ),
        "guionLargo": (
            "El once de septiembre de dos mil quince... a las cinco y diez de la tarde... una tragedia monumental enlutó al mundo islámico en la Gran Mezquita de La Meca... en Arabia Saudita... "
            "En el marco de las monumentales obras de ampliación del santuario... operaba una de las grúas móviles sobre orugas más potentes y colosales del planeta... una máquina Liebherr modelo LR mil trescientos cincuenta... con una pluma en celosía de acero que superaba los ciento noventa metros de longitud total... "
            "Aquella tarde... un frente de tormenta repentino arribó al valle... acompañado de precipitaciones torrenciales y ráfagas de viento convectivo que superaron los ochenta kilómetros por hora... "
            "Pese a que los servicios meteorológicos habían emitido alertas tempranas... la grúa permanecía fuera de servicio en una configuración operativa sumamente vulnerable... "
            "La gigantesca pluma principal se encontraba izada a un ángulo casi vertical de ochenta y cinco grados... "
            "El manual técnico del fabricante establecía de forma tajante que... frente a condiciones climáticas adversas o cuando la grúa estuviera inactiva... la pluma debía ser descendida hasta apoyarse en el suelo... o posicionarse en un ángulo seguro... "
            "Asimismo... los frenos del mecanismo de orientación de la superestructura debían estar completamente liberados... para permitir que la grúa girara libremente sobre su eje de trescientos sesenta grados... alineándose de forma natural con la dirección del viento... una maniobra de ingeniería conocida como efecto veleta o weathervaning... "
            "Sin embargo... los operarios habían dejado los frenos mecánicos de giro bloqueados... y la pluma izada al cielo... "
            "Al impactar las violentas ráfagas contra la superficie lateral de la inmensa celosía metálica... la estructura actuó como una gigantesca vela náutica... "
            "La descomunal fuerza lateral venció el centro de gravedad del conjunto... arrancando las orugas del suelo... "
            "La mole de más de mil toneladas volcó hacia atrás... precipitándose catastróficamente sobre el techo de la mezquita abarrotada de peregrinos... "
            "El colapso causó la muerte instantánea de ciento once personas... y heridas de extrema gravedad a más de trescientas cincuenta... "
            "La catástrofe de La Meca demostró que en el izaje crítico con grúas de gran porte... el manual del fabricante no es un compendio de sugerencias... es un mandato legal y operativo inquebrantable... "
            "Frente a una alerta climática... la desconexión de frenos de giro y el aseguramiento del aguilón en tierra son barreras que salvan vidas... "
            "Porque contra la fuerza implacable del viento... ninguna estructura metálica puede resistir por simple inercia."
        )
    },
    {
        "id": "079",
        "fecha": "12 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-12",
        "expediente": "Expediente #079",
        "carpeta": "2016-09-12-intoxicacion-monoxido-motobomba-cisterna",
        "titular": "EL MOTOR EN LA CISTERNA: LA ASFIXIA POR MONÓXIDO",
        "palabraResaltada": "MOTOR EN LA CISTERNA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Cisterna Subterránea de Reserva de Agua - 2016",
        "tipoRiesgo": "Espacios Confinados / Atmósferas Tóxicas (Monóxido de Carbono)",
        "parrafos": [
            "El 12 de septiembre de 2016, dos operarios fallecieron intoxicados por monóxido de carbono ($CO$) al introducir una motobomba con motor a explosión naftero dentro de una cisterna subterránea para desagotarla.",
            "La manguera de succión era corta, por lo que bajaron la motobomba al interior del tanque sin ventilación forzada ni medición de gases. En menos de diez minutos, los gases de escape desplazaron el oxígeno.",
            "Ambos trabajadores perdieron el conocimiento por asfixia química (carboxihemoglobina superior al 60%). Regla de oro en espacios confinados: prohibición absoluta de motores de combustión interna dentro del recinto.",
        ],
        "puntosClave": [
            {"icono": "ban", "titulo": "Prohibido motores a combustión en recintos cerrados", "texto": "Los motores nafteros o diésel deben operar siempre en el exterior ventilado; utilizar bombas sumergibles eléctricas o neumáticas."},
            {"icono": "wind", "titulo": "Ventilación forzada continua", "texto": "Inyectar aire fresco continuo mediante mangas y forzadores calculados para renovar la atmósfera del espacio confinado."},
            {"icono": "activity", "titulo": "Monitoreo continuo con detector de 4 gases", "texto": "Medición permanente en tiempo real con alarmas calibradas para CO (límite de acción 25 PPM / techo 50 PPM)."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: alertas de seguridad sobre monóxido de carbono en espacios confinados de NIOSH (Pub. No. 96-118) y normas de entrada segura a tanques OSHA 1910.146.",
        "guionReel": (
            "¿Meterías un motor a explosión encendido adentro de un cuarto cerrado sin ventanas?\n\n"
            "El 12 de septiembre de 2016, dos operarios debían desagotar una cisterna de agua subterránea profunda.\n\n"
            "Como la manguera de la bomba naftera no llegaba al fondo, tuvieron la peor idea: bajaron la motobomba encendida adentro del tanque con una soga.\n\n"
            "El caño de escape del motor empezó a vomitar monóxido de carbono puro. El monóxido no tiene color, no tiene olor y no se siente en la garganta.\n\n"
            "En solo cinco minutos, el gas invisible saturó el tanque. Los dos trabajadores se desmayaron sin darse cuenta y murieron en el fondo por asfixia celular.\n\n"
            "Jamás, bajo ninguna circunstancia, metas un motor a combustión dentro de un espacio confinado. Usa bombas eléctricas sumergibles y mide siempre el aire.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Industrial confined space hazardous rescue documentary photography, open concrete underground water reservoir cistern hatch entrance. "
            "Small yellow gasoline-powered portable utility water pump sitting inside dark subterranean chamber, exhaust pipe pointing at concrete wall, "
            "four-gas electronic atmospheric detector lying by access ladder with blinking red LED screen displaying high CO warning, 16:9 ratio."
        ),
        "guionLargo": (
            "El doce de septiembre de dos mil dieciséis... en el subsuelo de un complejo edilicio durante tareas de mantenimiento y limpieza anual de depósitos de agua potable... una negligencia elemental cobró dos vidas humanas... "
            "Dos operarios de una empresa de saneamiento debían desagotar el lodo residual remanente en el fondo de una cisterna subterránea de hormigón de cuatro metros de profundidad... accesible únicamente a través de una estrecha boca de inspección de sesenta centímetros... "
            "Para vaciar el agua restante... la cuadrilla disponía de una motobomba centrífuga portátil impulsada por un motor de combustión interna a nafta de cuatro tiempos... "
            "Al intentar realizar la aspiración desde el exterior... descubrieron que la manguera de succión de tres metros de longitud no alcanzaba a tocar el fondo del tanque... "
            "En lugar de suspender la tarea y solicitar un tramo de manguera adicional o una bomba sumergible eléctrica blindada... los trabajadores tomaron una determinación sumamente imprudente... "
            "Ataron la motobomba con sogas... la descendieron por la boca de entrada y la apoyaron sobre una banqueta metálica en el interior de la cisterna... encendiendo el motor dentro del recinto hermético... "
            "A continuación... ambos operarios descendieron por la escalera marinera para acomodar el extremo del filtro en el lodo... "
            "Un motor a explosión pequeño en marcha emite cientos de gramos de monóxido de carbono por minuto a través de su caño de escape... "
            "El monóxido de carbono es un gas altamente insidioso... incoloro, inodoro e insípido... que posee una afinidad por la hemoglobina de la sangre doscientas cincuenta veces superior a la del oxígeno... "
            "En un ambiente confinado sin ventilación mecánica extractiva... la concentración del gas trepó rápidamente por encima de las mil partes por millón... "
            "Sin experimentar ardor en los ojos ni sensación de asfixia... los trabajadores comenzaron a sufrir una pérdida paulatina de la fuerza muscular y confusión mental... "
            "Al intentar trepar por la escalera de salida... sus piernas colapsaron... cayendo inconscientes sobre el agua del fondo... donde fallecieron minutos más tarde por intoxicación aguda irreversible... "
            "Las investigaciones de higiene industrial recordaron un principio innegociable de los espacios confinados... Jamás debe introducirse un motor de combustión interna en el interior de recintos cerrados... "
            "Los equipos de bombeo a combustión deben emplazarse invariablemente en el exterior ventilado... y toda labor en tanques exige ventilación forzada... medición continua con detectores de gases... y un vigía de rescate permanente en superficie... "
            "Porque ante el monóxido de carbono... el asesino más silencioso de la industria... no hay segundas oportunidades."
        )
    },
    {
        "id": "080",
        "fecha": "13 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-13",
        "expediente": "Expediente #080",
        "carpeta": "2018-09-13-explosiones-gas-merrimack-valley",
        "titular": "EL LAZO CIEGO DE PRESIÓN: LAS EXPLOSIONES DE MERRIMACK VALLEY",
        "palabraResaltada": "MERRIMACK VALLEY",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Red de Gas Natural de Merrimack Valley, Massachusetts, EE.UU. - 2018",
        "tipoRiesgo": "Seguridad de Procesos / Gestión del Cambio (MOC) en Redes",
        "parrafos": [
            "El 13 de septiembre de 2018, una serie simultánea de explosiones e incendios destruyó entre 60 y 80 edificios en tres ciudades del valle de Merrimack, Massachusetts, dejando un muerto y miles de evacuados.",
            "Durante el reemplazo de una matriz de tubería de hierro fundido, la cuadrilla despresurizó la línea vieja pero olvidó que los sensores de control de presión de la estación reguladora seguían conectados a ella.",
            "Al detectar falsamente 'cero presión', los reguladores abrieron al 100% inyectando gas a 80 veces la presión normal en miles de hogares. Una falla crítica de Gestión del Cambio (MOC) y verificación de planos de control.",
        ],
        "puntosClave": [
            {"icono": "git-pull-request", "titulo": "Gestión del cambio (MOC) en modificaciones de red", "texto": "Toda desconexión o empalme de tuberías exige revisión de ingeniería previa que identifique los lazos de control instrumentados asociados."},
            {"icono": "file-text", "titulo": "Planos y esquemáticos (P&ID) verificados en campo", "texto": "Prohibido intervenir cañerías sin corroborar visualmente dónde toman señal las líneas de sensado de las estaciones reguladoras."},
            {"icono": "shield-check", "titulo": "Válvulas de alivio contra sobrepresión (OPD)", "texto": "Instalar dispositivos de corte automático por alta presión en estaciones de distribución secundaria para proteger las redes domiciliarias."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe final de investigación de la Junta Nacional de Seguridad en el Transporte de EE.UU. (NTSB Report NTSB/PAR-19/02) sobre las sobrepresurizaciones en Merrimack Valley.",
        "guionReel": (
            "¿Cómo un solo cable de sensor olvidado pudo hacer estallar sesenta casas al mismo tiempo en tres ciudades enteras?\n\n"
            "El 13 de septiembre de 2018, en Massachusetts, una cuadrilla de gas reemplazaba una tubería vieja en una esquina.\n\n"
            "Desconectaron el caño viejo y abrieron el nuevo. Pero nadie revisó los planos con atención: los sensores que le decían a la planta cuánta presión mandar seguían enchufados al caño viejo que ya no tenía gas.\n\n"
            "El sensor marcó 'cero presión'. La computadora pensó que la ciudad se quedaba sin gas y abrió las válvulas al máximo.\n\n"
            "Una ola monstruosa de gas natural entró a miles de casas con ochenta veces la presión normal. Los calefones y cocinas reventaron en llamas simultáneamente: sesenta casas destruidas, un muerto y miles de evacuados.\n\n"
            "En redes de servicios, antes de cortar un caño, verifica los lazos de control. La gestión del cambio no es burocracia: salva ciudades enteras.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Suburban utility disaster documentary photography, September 13 2018 Merrimack Valley gas explosions Massachusetts. "
            "Suburban residential street with multiple houses burning simultaneously, fire trucks with ladders extended fighting residential roof blazes, "
            "utility underground gas main excavation trench open in street foreground with yellow plastic gas pipes, emergency sirens, high realism, 16:9 ratio."
        ),
        "guionLargo": (
            "El trece de septiembre de dos mil dieciocho... en una tranquila tarde de otoño en la región de Merrimack Valley, al norte de Boston... una catástrofe urbana sin precedentes sumió en el caos a tres ciudades enteras... "
            "En las localidades de Lawrence, Andover y North Andover... cerca de las cuatro de la tarde... los servicios de emergencia comenzaron a colapsar al recibir llamadas desesperadas reportando explosiones simultáneas e incendios en viviendas... "
            "En cuestión de minutos... más de sesenta casas particulares y comercios estallaron o ardieron en llamas... obligando a la evacuación inmediata de más de cincuenta mil habitantes... "
            "El desastre no fue originado por una fuga accidental en la calle... sino por una colosal sobrepresurización sistémica de la red de distribución de gas natural de baja presión... "
            "Esa misma mañana... una cuadrilla contratista de la empresa distribuidora Columbia Gas ejecutaba la renovación de una antigua cañería matriz de hierro fundido... reemplazándola por modernas tuberías de polietileno... "
            "El procedimiento de trabajo... redactado de manera precaria y sin la firma de un ingeniero calculista matriculado... contemplaba aislar y despresurizar el tramo de caño viejo para empalmar el nuevo circuito... "
            "Sin embargo... los técnicos omitieron una verificación de control de procesos fundamental... "
            "Las líneas de sensado de presión que transmitían la señal de control a la estación reguladora principal del distrito... continuaban conectadas físicamente al tramo de caño antiguo que estaba siendo desconectado... "
            "Cuando la cuadrilla cortó el flujo en la cañería vieja... los transmisores registraron una lectura de cero libras de presión... "
            "Al interpretar falsamente que la red comunitaria sufría un desabastecimiento crítico... los reguladores automáticos de la estación de rebaje abrieron sus válvulas de par en par... "
            "Un torrente inmenso de gas natural ingresó a la red domiciliaria a una presión ochenta veces superior a la permitida... superando con creces la resistencia de los medidores residenciales y los artefactos de calefacción... "
            "El gas rompió sellos y válvulas de cocinas y calderas... llenando las viviendas de combustible que encontró ignición en los pilotos... desatando una oleada de explosiones encadenadas... "
            "La tragedia cobró la vida de un joven de dieciocho años y dejó a decenas de vecinos heridos y cientos de familias sin hogar... "
            "El informe oficial de la NTSB concluyó que la ausencia de un proceso formal de Gestión del Cambio fue la causa raíz del desastre... "
            "En redes de distribución crítica... cada modificación en campo exige el análisis interdisciplinario de los lazos de control instrumentado... la actualización en tiempo real de los planos de ingeniería... y la instalación obligatoria de dispositivos de sobrepresión independientes... "
            "Porque cuando los sensores quedan ciegos... las consecuencias se pagan en los hogares de la comunidad."
        )
    },
    {
        "id": "081",
        "fecha": "14 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-14",
        "expediente": "Expediente #081",
        "carpeta": "2017-09-14-amputacion-guillotina-corte-chapa",
        "titular": "LA CUCHILLA A DOS MANOS: AMPUTACIÓN EN LA GUILLOTINA",
        "palabraResaltada": "CUCHILLA A DOS MANOS",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Metalmecánica de Corte y Plegado - 2017",
        "tipoRiesgo": "Atrapamiento / Protección de Máquinas (Guillotinas)",
        "parrafos": [
            "El 14 de septiembre de 2017, un operario metalúrgico de 31 años sufrió la amputación traumática de tres dedos en una guillotina neumática de corte de chapa mientras asistía a un compañero en el posicionado.",
            "La máquina tenía el comando bimanual puenteado a un único pulsador y el pedal de pie no poseía protección. El operador principal accionó el corte mientras el ayudante aún acomodaba la chapa con las manos bajo la cuchilla.",
            "La guillotina carecía de resguardo fijo transparente en la línea de corte y no existía protocolo para tareas con dos personas. La lección: mandos bimanuales sincronizados para cada operario y barreras físicas infranqueables.",
        ],
        "puntosClave": [
            {"icono": "hand", "titulo": "Mandos bimanuales independientes y simultáneos", "texto": "Si operan dos personas, cada una debe tener su propio juego de pulsadores bimanuales obligatorios para habilitar el golpe."},
            {"icono": "shield", "titulo": "Resguardo fijo o cortina óptica en línea de corte", "texto": "Instalar guardas fijas ranuradas que permitan el paso de la chapa pero impidan el ingreso físico de dedos bajo la cuchilla (ISO 13857)."},
            {"icono": "lock", "titulo": "Prohibido puentear sistemas de seguridad", "texto": "El puenteo de mandos bimanuales es una falta grave que anula la protección de diseño y genera accidentes mutilantes."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: normativas de seguridad en cizallas y guillotinas industriales de OSHA 1910.212 y normas técnicas de seguridad de maquinaria UNE-EN 13985.",
        "guionReel": (
            "¿Por qué operar una máquina de corte pesada entre dos personas sin seguridad sincronizada es una receta para la mutilación?\n\n"
            "El 14 de septiembre de 2017, en una fábrica metalúrgica, dos operarios cortaban tiras largas de chapa en una guillotina industrial.\n\n"
            "Para trabajar más rápido, habían puenteado el comando bimanual y usaban un pedal en el piso.\n\n"
            "El operario que manejaba el pedal creyó que su compañero ya había terminado de acomodar la chapa y apretó el pedal.\n\n"
            "Pero el ayudante todavía tenía los dedos abajo de la cuchilla sosteniendo la lámina.\n\n"
            "La cuchilla de acero templado bajó con toneladas de fuerza en una milésima de segundo: tres dedos amputados en el acto.\n\n"
            "Si dos personas operan una máquina, las dos deben tener mandos bimanuales obligatorios y la cuchilla debe tener guarda fija.\n\n"
            "Tu compañero no puede leer tu mente."
        ),
        "promptImagen": (
            "Industrial metal fabrication workshop photography, large mechanical industrial sheet metal shearing guillotine machine. "
            "Steel plate caught partially sheared under heavy upper blade, blood-free leather work gloves lying abandoned on metal feed table, "
            "electrical foot switch on floor with missing safety hood cover, caution machinery safety symbols on machine body, realistic lighting, 16:9 ratio."
        ),
        "guionLargo": (
            "El catorce de septiembre de dos mil diecisiete... en una fábrica dedicada a la transformación y corte de láminas de acero... la anulación de dispositivos de seguridad colectiva provocó una lesión mutilante irreversible... "
            "En el sector de corte... dos operarios trabajaban en una cizalla guillotina mecánica de accionamiento neumático... una máquina capaz de seccionar planchas de acero de hasta seis milímetros de espesor con una fuerza descomunal... "
            "Debido a que las chapas eran de gran formato... el trabajo requería de dos trabajadores... uno posicionado al frente de la mesa de alimentación guiando el material contra el tope trasero... y un ayudante lateral sosteniendo el extremo voladizo para evitar que la lámina se arqueara... "
            "Originalmente... la máquina había sido provista de fábrica con un sistema de comando bimanual sincrónico... que obligaba al operario a mantener ambas manos ocupadas sobre sendos pulsadores eléctricos alejados de la línea de corte... "
            "Sin embargo... para acelerar el ritmo de producción del taller... el personal de mantenimiento había puenteado el circuito bimanual... conectando en su lugar un pedal eléctrico suelto en el suelo... "
            "Asimismo... la rejilla metálica fija de protección que debía cubrir el frente de la cuchilla... impidiendo el paso de las manos hacia los pisadores hidráulicos... había sido desmontada semanas atrás... bajo el pretexto de que restaba visión para alinear los trazos... "
            "Durante una maniobra de corte... el ayudante introdujo su mano izquierda por debajo del cabezal de pisones para enderezar la chapa contra la regla... "
            "El operario principal... asumiendo erróneamente que la chapa estaba lista y sin verificar visualmente la posición de las manos de su compañero... pisó el pedal de accionamiento... "
            "La pesada cuchilla superior descendió de forma fulminante... seccionando tres falanges de la mano del ayudante antes de que pudiera emitir una señal de advertencia... "
            "Las investigaciones periciales recordaron que las guillotinas son una de las máquinas de mayor riesgo de amputación en la industria metalúrgica... "
            "Cuando una máquina es compartida por dos personas... las normas internacionales exigen que ambos operarios dispongan de mandos bimanuales independientes e interconectados... donde el golpe de corte solo se autorice cuando los cuatro pulsadores estén activados simultáneamente... "
            "Y la guarda fija en la línea de corte es una barrera física inviolable... "
            "Porque ante el filo de una guillotina... la coordinación visual jamás reemplaza a un resguardo mecánico."
        )
    },
    {
        "id": "082",
        "fecha": "15 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-15",
        "expediente": "Expediente #082",
        "carpeta": "2019-09-15-quemadura-linea-vapor-sala-calderas",
        "titular": "EL CONTACTO CON EL TUBO VIVO: QUEMADURA EN SALA DE CALDERAS",
        "palabraResaltada": "TUBO VIVO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Sala de Calderas y Distribución de Vapor Industrial - 2019",
        "tipoRiesgo": "Energía Térmica / Superficies Calientes y Señalización",
        "parrafos": [
            "El 15 de septiembre de 2019, un operador de calderas de 42 años sufrió quemaduras térmicas de segundo y tercer grado en el antebrazo y torso al tropezar y apoyarse contra una válvula de vapor vivo sin aislación a 180 °C.",
            "El sector de purga de condensado se encontraba en un pasillo estrecho con piso húmedo. La tubería y el cuerpo de la válvula habían perdido su chaqueta térmica desmontable tras una reparación y nunca fue reinstalada.",
            "No existía señalización de superficie caliente ni rejilla de apantallamiento. Toda superficie industrial por encima de 60 °C accesible al personal debe contar con aislamiento térmico o barreras físicas de protección.",
        ],
        "puntosClave": [
            {"icono": "flame", "titulo": "Aislamiento térmico obligatorio (>60 °C)", "texto": "Toda tubería, válvula o cuerpo metálico que supere los 60 °C al alcance del tránsito humano debe estar aislado con chaquetas térmicas."},
            {"icono": "alert-triangle", "titulo": "Señalización y apantallamiento de calor", "texto": "Identificar con cartelería visible de advertencia de superficie caliente y colocar mallas metálicas protectoras en pasillos estrechos."},
            {"icono": "check-circle", "titulo": "Reinstalación inmediata post-mantenimiento", "texto": "Prohibido reanudar la operación de líneas térmicas sin verificar que el aislamiento desmontable haya sido colocado en su totalidad."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: normativas de prevención de quemaduras y aislamiento térmico en plantas industriales de OSHA 1910.261 y directrices de eficiencia y seguridad en vapor de la norma ASTM C1055.",
        "guionReel": (
            "¿Sabías que un caño de vapor pelado a 180 grados puede quemar tu piel hasta el músculo en menos de medio segundo?\n\n"
            "El 15 de septiembre de 2019, en una sala de calderas, un foguista caminaba por un pasillo estrecho para revisar una bomba.\n\n"
            "El piso estaba resbaloso por condensación. El hombre trastabilló y, por instinto natural para no caerse, estiró el brazo y se apoyó contra un caño de vapor vivo.\n\n"
            "Días atrás le habían hecho mantenimiento a la válvula y nadie se molestó en volver a colocarle la manta aislante térmica.\n\n"
            "El metal al rojo vivo derritió la ropa sintética pegándola a su piel: quemaduras de tercer grado gravísimas en el antebrazo y las costillas.\n\n"
            "En salas de calderas, toda superficie a más de 60 grados debe estar tapada con aislamiento térmico y señalizada.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Industrial boiler room mechanical safety documentary photography, narrow steam distribution piping corridor. "
            "High-pressure steel steam pipe valve uninsulated and exposed with visible heat shimmer distortion in air, thermal insulation wrap lying discarded on floor, "
            "wet slippery tile floor with warning sign Caution Hot Surface, steam pressure gauges glowing under industrial amber lighting, 16:9 ratio."
        ),
        "guionLargo": (
            "El quince de septiembre de dos mil diecinueve... en la sala de generación de vapor y calderas de una planta procesadora de alimentos... una omisión en la restitución de aislamientos térmicos provocó una quemadura ocupacional grave... "
            "El establecimiento operaba dos calderas pirotubulares de gran porte... destinadas a suministrar vapor saturado a diez bares de presión y a más de ciento ochenta grados centígrados de temperatura hacia las líneas de esterilización y cocción... "
            "El trazado de distribución incluía múltiples ramales de purga automática de condensados... ubicados a lo largo de un pasillo secundario de tránsito operativo... de apenas setenta centímetros de ancho... "
            "Una semana antes del suceso... personal de mantenimiento mecánico había intervenido una trampa de vapor y su correspondiente válvula de bloqueo esférica para reemplazar sellos deteriorados... "
            "Para realizar la tarea... retiraron la colchoneta o chaqueta térmica desmontable de lana mineral con recubrimiento de fibra de vidrio que aislaba el cuerpo metálico de la válvula... "
            "Concluida la reparación... los mecánicos habilitaron el paso del vapor... pero postergaron la colocación de la aislación térmica para más adelante... dejando el cuerpo de fundición de acero completamente desnudo y expuesto al roce... "
            "Tampoco instalaron cartelería de advertencia de superficie caliente ni una rejilla metálica de apantallamiento transitorio... "
            "Durante la ronda de control nocturna... un operador de calderas recorría el estrecho pasaje para verificar manómetros de presión... "
            "El suelo del sector presentaba condensación superficial y restos de agua con sarro... lo que provocó que el calzado del trabajador resbalara de forma imprevista... "
            "Por un reflejo biológico de supervivencia... el foguista estiró su brazo derecho y su torso hacia el lateral para evitar golpear contra el pavimento... "
            "Su antebrazo y la zona intercostal entraron en contacto directo contra el cuerpo de la válvula de vapor... a ciento ochenta grados... "
            "En la fisiopatología de las quemaduras térmicas... el contacto con metales por encima de los setenta grados centígrados destruye la epidermis y la dermis en menos de una fracción de segundo... "
            "El calor extremo carbonizó la tela de su camisa... adhiriéndola al tejido vivo y provocándole quemaduras profundas de segundo y tercer grado que requirieron injertos quirúrgicos... "
            "La norma internacional ASTM C diez cincuenta y cinco y las directivas de higiene laboral son terminantes... Toda superficie metálica industrial accesible que supere los sesenta grados de temperatura debe contar con aislamiento térmico permanente... "
            "Ningún trabajo de mantenimiento puede considerarse concluido sin la reinstalación certificada de las mantas térmicas... "
            "Porque en una sala de máquinas... el calor no perdonado deja huellas indelebles en el cuerpo humano."
        )
    }
]

def procesar_lote_7(kokoro_instance):
    procesadas = []

    print(f"\n=======================================================")
    print(f"Iniciando procesamiento de {len(LOTE_7_DATA)} historias del Lote 7 (#073 a #082)")
    print(f"=======================================================\n")

    for h in LOTE_7_DATA:
        folder_name = h["carpeta"]
        target_dir = os.path.join(ASSETS_DIR, folder_name)
        os.makedirs(target_dir, exist_ok=True)

        print(f"▶ Procesando: {h['expediente']} ({h['fecha']}) - {h['titular'][:45]}...")

        # 1. README.md
        readme_path = os.path.join(target_dir, "README.md")
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(f"# {h['expediente']}: {h['titular']}\n\n")
            f.write(f"**Fecha del evento:** {h['fecha']} ({h['fechaPublicacion']})  \n")
            f.write(f"**Lugar / Instalación:** {h['etiquetaImagen']}  \n")
            f.write(f"**Tipo de riesgo HSE:** {h['tipoRiesgo']}  \n\n")
            f.write(f"## Resumen Ejecutivo\n\n")
            for p in h["parrafos"]:
                f.write(f"{p}\n\n")
            f.write(f"## Lecciones Preventivas Clave\n\n")
            for punto in h["puntosClave"]:
                f.write(f"- **{punto['titulo']}:** {punto['texto']}\n")
            f.write(f"\n## Pregunta de Reflexión\n\n{h['pregunta']}\n\n")
            f.write(f"_{h['fuente']}_\n")

        # 2. contenido-completo.md
        contenido_path = os.path.join(target_dir, "contenido-completo.md")
        with open(contenido_path, "w", encoding="utf-8") as f:
            f.write(f"# Expediente Técnico HSE: {h['titular']}\n\n")
            f.write(f"> **Focus HSE - Archivo Histórico de Seguridad de Procesos y Salud Ocupacional**  \n")
            f.write(f"> *\"La seguridad está en los detalles\"*\n\n")
            f.write(f"| Metadato | Detalle |\n|---|---|\n")
            f.write(f"| **ID Expediente** | {h['expediente']} |\n")
            f.write(f"| **Fecha Histórica** | {h['fecha']} |\n")
            f.write(f"| **Instalación** | {h['etiquetaImagen']} |\n")
            f.write(f"| **Clasificación HSE** | {h['tipoRiesgo']} |\n\n")
            f.write(f"## 1. Contexto y Cronología de los Hechos\n\n")
            for p in h["parrafos"]:
                f.write(f"{p}\n\n")
            f.write(f"## 2. Análisis Causal y Factores Contribuyentes\n\n")
            f.write(f"El análisis de este accidente revela fallas sistémicas tanto en el plano operativo como en los sistemas de gestión:\n\n")
            for punto in h["puntosClave"]:
                f.write(f"### 2.{h['puntosClave'].index(punto)+1}. {punto['titulo']}\n")
                f.write(f"{punto['texto']}\n\n")
            f.write(f"## 3. Guion Narrativo Documental (Audio Completo)\n\n")
            f.write(f"{h['guionLargo']}\n\n")
            f.write(f"## 4. Guion para Video Corto (Reels / TikTok / Shorts)\n\n```text\n{h['guionReel']}\n```\n\n")
            f.write(f"## 5. Prompt de Generación de Imagen (Gemini Imagen 3)\n\n```text\n{h['promptImagen']}\n```\n\n")
            f.write(f"## 6. Referencias Técnicas y Normativas\n\n{h['fuente']}\n")

        # 3. guion-reel.txt
        with open(os.path.join(target_dir, "guion-reel.txt"), "w", encoding="utf-8") as f:
            f.write(h["guionReel"])

        # 4. prompt-portada.txt
        with open(os.path.join(target_dir, "prompt-portada.txt"), "w", encoding="utf-8") as f:
            f.write(h["promptImagen"])

        # 5. Portada gráfica PNG (base de respaldo)
        portada_path = os.path.join(target_dir, "portada.png")
        if not os.path.exists(portada_path):
            crear_portada_grafica_lote7(h, portada_path)
            print("  ✓ Portada generada (portada.png)")

        # 6. Síntesis de audio con Kokoro
        wav_path = os.path.join(target_dir, "historia.wav")
        m4a_path = os.path.join(target_dir, "historia.m4a")

        palabras = len(h["guionLargo"].split())
        print(f"  🎙️ Sintetizando audio ({palabras} palabras) con Kokoro (speed={KOKORO_SPEED})...")
        samples, sample_rate = kokoro_instance.create(
            h["guionLargo"],
            voice=KOKORO_VOICE,
            speed=KOKORO_SPEED,
            lang=KOKORO_LANG
        )
        sf.write(wav_path, samples, sample_rate)

        # 7. Conversión a M4A con ffmpeg
        print("  ⚙️ Convirtiendo a M4A optimizado...")
        cmd_ffmpeg = [
            "ffmpeg", "-i", wav_path,
            "-c:a", "aac", "-b:a", "192k",
            "-y", m4a_path
        ]
        subprocess.run(cmd_ffmpeg, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        if os.path.exists(wav_path):
            os.remove(wav_path)

        # 8. Duración calculada
        duracion_seg = len(samples) / float(sample_rate)
        minutos = int(duracion_seg // 60)
        segundos = int(duracion_seg % 60)
        texto_duracion = f"Audio de {minutos} minutos {segundos:02d} segundos"
        h["duracionAudio"] = texto_duracion
        print(f"  ✓ Audio listo: {m4a_path} ({texto_duracion})\n")

        procesadas.append(h)

    return procesadas

def crear_portada_grafica_lote7(historia, output_path):
    """Genera portada 16:9 corporativa de alta resolución."""
    width, height = 1920, 1080
    img = Image.new("RGB", (width, height), color=(6, 17, 21))
    draw = ImageDraw.Draw(img)

    for y in range(height):
        factor = y / height
        r = int(6 + factor * 8)
        g = int(17 + factor * 14)
        b = int(21 + factor * 16)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    draw.rectangle([0, 0, width, 12], fill=(25, 211, 230))

    try:
        font_exp = ImageFont.truetype("arialbd.ttf", 36)
        font_title = ImageFont.truetype("arialbd.ttf", 60)
        font_sub = ImageFont.truetype("arial.ttf", 32)
        font_meta = ImageFont.truetype("arialbd.ttf", 28)
        font_badge = ImageFont.truetype("arialbd.ttf", 26)
    except:
        font_exp = ImageFont.load_default()
        font_title = font_exp
        font_sub = font_exp
        font_meta = font_exp
        font_badge = font_exp

    badge_x = 100
    badge_y = 100
    draw.rectangle([badge_x, badge_y, badge_x + 380, badge_y + 54], fill=(25, 211, 230, 40), outline=(25, 211, 230), width=2)
    draw.text((badge_x + 18, badge_y + 12), f"{historia['fecha']} · {historia['expediente']}", font=font_badge, fill=(25, 211, 230))

    draw.rectangle([width - 550, badge_y, width - 100, badge_y + 54], fill=(255, 77, 56, 40), outline=(255, 77, 56), width=2)
    draw.text((width - 530, badge_y + 12), historia['tipoRiesgo'][:30], font=font_badge, fill=(255, 120, 100))

    draw.rectangle([100, 200, width - 100, height - 160], outline=(151, 231, 255, 45), width=1)
    draw.line([100, 200, 160, 200], fill=(25, 211, 230), width=4)
    draw.line([100, 200, 100, 260], fill=(25, 211, 230), width=4)
    draw.line([width - 160, height - 160, width - 100, height - 160], fill=(25, 211, 230), width=4)
    draw.line([width - 100, height - 220, width - 100, height - 160], fill=(25, 211, 230), width=4)

    titular = historia["titular"]
    palabras = titular.split()
    lineas = []
    linea_actual = []
    for p in palabras:
        linea_actual.append(p)
        if len(" ".join(linea_actual)) > 35:
            lineas.append(" ".join(linea_actual))
            linea_actual = []
    if linea_actual:
        lineas.append(" ".join(linea_actual))

    y_text = 360
    for linea in lineas:
        draw.text((140, y_text), linea, font=font_title, fill=(255, 255, 255))
        y_text += 78

    draw.text((140, y_text + 40), historia["subtitulo"], font=font_sub, fill=(196, 215, 220))
    draw.text((140, y_text + 100), f"📍 {historia['etiquetaImagen']}", font=font_meta, fill=(255, 212, 71))

    draw.line([100, height - 120, width - 100, height - 120], fill=(151, 231, 255, 40), width=1)
    draw.text((140, height - 90), "FOCUS HSE · ARCHIVO HISTÓRICO DE SEGURIDAD", font=font_meta, fill=(25, 211, 230))
    draw.text((width - 480, height - 90), "LA SEGURIDAD ESTÁ EN LOS DETALLES", font=font_meta, fill=(159, 184, 192))

    img.save(output_path, "PNG")

def inyectar_en_index_html(historias_procesadas):
    """Inyecta las historias del Lote 7 en index.html antes del cierre del array historias."""
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    nuevos_bloques = []
    for h in historias_procesadas:
        puntos_js = json.dumps(h["puntosClave"], ensure_ascii=False, indent=12)
        parrafos_js = json.dumps(h["parrafos"], ensure_ascii=False, indent=10)

        # Configuramos imagen: "portada.jpeg" para que cuando el usuario coloque su imagen se muestre de inmediato,
        # y si no está aún, el cargador de index.html conmuta automáticamente a portada.png
        bloque = f"""      {{
        id: "{h['id']}",
        logo: "FOCUS HSE",
        fecha: "{h['fecha']}",
        fechaPublicacion: "{h['fechaPublicacion']}",
        expediente: "{h['expediente']}",
        carpetaAssets: "assets/efemerides/{h['carpeta']}/",
        titular: "{h['titular']}",
        palabraResaltada: "{h['palabraResaltada']}",
        subtitulo: "{h['subtitulo']}",
        etiquetaImagen: "{h['etiquetaImagen']}",
        imagen: "portada.jpeg",
        audio: "historia.m4a",
        duracionAudio: "{h['duracionAudio']}",
        parrafos: {parrafos_js},
        puntosClave: {puntos_js},
        pregunta: "{h['pregunta']}",
        fuente: "{h['fuente']}"
      }}"""
        nuevos_bloques.append(bloque)

    texto_a_insertar = ",\n" + ",\n".join(nuevos_bloques)

    pos_cierre = content.find("    ];\n\n    // Placeholder visual")
    if pos_cierre == -1:
        pos_cierre = content.find("    ];\r\n\r\n    // Placeholder visual")
    if pos_cierre == -1:
        pos_cierre = content.find("    ];")

    if pos_cierre == -1:
        print("ERROR: No se encontró el cierre de historias en index.html", file=sys.stderr)
        return False

    nuevo_content = content[:pos_cierre] + texto_a_insertar + "\n" + content[pos_cierre:]

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(nuevo_content)

    print("\n✓ index.html actualizado exitosamente con los 10 nuevos expedientes (#073 a #082).")
    return True

def main():
    print("Iniciando motor Kokoro para Lote 7 (#073 a #082)...")
    kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

    procesadas = procesar_lote_7(kokoro)

    if inyectar_en_index_html(procesadas):
        print(f"\n🎉 ¡LOTE 7 COMPLETADO AL 100%! ({len(procesadas)} historias procesadas)")

if __name__ == "__main__":
    main()
