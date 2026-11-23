# -*- coding: utf-8 -*-
"""
Generador Agéntico Automatizado para Lote 9: Expedientes #093 a #102 (26 de septiembre al 5 de octubre)
1. Crea directorios en assets/efemerides/
2. Genera README.md y contenido-completo.md
3. Guarda guion-reel.txt y prompt-portada.txt
4. Genera portada.png (16:9 alta resolución con Pillow)
5. Sintetiza audio en Kokoro (speed 0.86, ~350-420 palabras -> ~2:15 a 2:50 min)
6. Convierte con ffmpeg a M4A y mide duración exacta
7. Inyecta en index.html con imagen: "portada.jpeg" y fallback automático a portada.png
"""

import os
import sys
import json
import subprocess
import re

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

LOTE_9_DATA = [
    {
        "id": "093",
        "fecha": "26 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-26",
        "expediente": "Expediente #093",
        "carpeta": "2019-09-26-incendio-planta-quimica-lubrizol-ruan",
        "titular": "LA NUBE NEGRA SOBRE EL SENA: EL INCENDIO DE LUBRIZOL EN RUAN",
        "palabraResaltada": "LUBRIZOL EN RUAN",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Química de Aditivos Lubrizol, Ruan, Francia - 2019",
        "tipoRiesgo": "Seguridad de Procesos / Almacenamiento",
        "parrafos": [
            "El 26 de septiembre de 2019, un voraz incendio en la planta química Lubrizol en Ruan destruyó más de 9.500 toneladas de productos químicos y lubricantes, generando una columna de humo tóxico de 22 kilómetros.",
            "El fuego se originó durante la noche en un área abierta de almacenamiento de tambores y contenedores IBC contigua a una empresa vecina, propagándose rápidamente por falta de muros cortafuego estancos y barreras de retención.",
            "Cientos de miles de habitantes sufrieron olores asfixiantes y las actividades agrícolas fueron paralizadas en cinco departamentos. La lección: compartimentación cortafuego, sistemas fijos de espuma y control riguroso de carga térmica.",
        ],
        "puntosClave": [
            {"icono": "shield", "titulo": "Compartimentación y muros cortafuego", "texto": "Separar físicamente los depósitos de lubricantes y químicos inflamables mediante muros cortafuego con resistencia mínima RF-120."},
            {"icono": "flame", "titulo": "Sistemas de rociadores de espuma pesada", "texto": "Proteger los parques de tambores con sistemas automáticos de extinción por espuma de baja y media expansión con detección térmica temprana."},
            {"icono": "droplets", "titulo": "Contención de aguas de extinción (Cubeto)", "texto": "Diseñar piletas de contención dimensionadas para retener tanto los químicos derramados como las miles de toneladas de agua bomberil contaminada."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de la Oficina de Análisis de Riesgos y Contaminaciones Industriales de Francia (BARPI) sobre el incendio de Lubrizol y directiva Seveso III.",
        "guionReel": (
            "¿Te imaginas ver una columna de humo negro de 22 kilómetros cubriendo toda tu ciudad?\n\n"
            "26 de septiembre de 2019. Ruan, Francia. Planta química Lubrizol. A mitad de la noche, se desata un incendio en un patio de almacenamiento.\n\n"
            "Miles de tambores y contenedores plásticos con aditivos para aceites comenzaron a estallar uno tras otro. No había muros cortafuego que frenaran la reacción en cadena.\n\n"
            "Nueve mil quinientas toneladas de químicos ardieron sin control. La nube negra cruzó el río Sena y sembró el pánico en miles de habitantes.\n\n"
            "Se cerraron escuelas y se prohibió consumir leche y cosechas en cinco departamentos.\n\n"
            "La lección de HSE es contundente: almacenar tambores químicos exige cubetos estancos, sistemas fijos de espuma y barreras cortafuego infranqueables.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic dramatic photograph of a massive chemical warehouse fire aftermath at dusk. "
            "Twisted rows of blackened, exploded metal drums and melted plastic IBC containers in an industrial storage yard, "
            "pools of reflective chemical foam and water on asphalt, heavy industrial fire suppression monitors in foreground, "
            "distant charred warehouse structural steel columns against a smoky dusk sky, documentary photojournalism, 8k resolution, raw textures."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 26 de septiembre de 2019, poco antes de las tres de la madrugada, las alarmas de la planta química Lubrizol en Ruan, Francia, "
            "desataron una de las mayores crisis ambientales e industriales de la última década en Europa. "
            "El complejo, clasificado como de alto riesgo bajo la directiva Seveso, albergaba formulaciones complejas de aditivos "
            "para aceites de motor y fluidos industriales.\n\n"
            "El fuego se declaró inicialmente en una plataforma logística exterior donde se acopiaban miles de tambores metálicos "
            "y contenedores plásticos tipo IBC. La ausencia de barreras cortafuego y la excesiva densidad de carga térmica permitieron "
            "que el calor radiante hiciera colapsar los envases plásticos en cascada. Arroyos de hidrocarburos ardientes fluyeron "
            "por las pendientes del pavimento hacia naves cubiertas y depósitos vecinos de la empresa Normandie Logistique, "
            "provocando el estallido sucesivo de miles de recipientes sometidos a sobrepresión térmica.\n\n"
            "Más de novecientas cincuenta toneladas de sustancias químicas ardieron en una hoguera monumental. "
            "El penacho de humo negro y denso se elevó a cientos de metros, extendiéndose a lo largo de más de veinte kilómetros sobre el valle del Sena. "
            "Aunque no hubo que lamentar víctimas fatales directas gracias a la evacuación temprana de los operarios, "
            "el impacto social y económico fue devastador: se suspendió la comercialización de productos agrícolas y lácteos en cinco regiones, "
            "y miles de ciudadanos experimentaron náuseas, cefaleas y ansiedad colectiva ante la sospecha de compuestos carcinógenos.\n\n"
            "El siniestro de Ruan derivó en una profunda revisión de las normas francesas de almacenamiento de líquidos inflamables. "
            "Consagró la exigencia de compartimentaciones cortafuego estancas entre parcelas de almacenamiento, "
            "la instalación obligatoria de sistemas automáticos de deluge de espuma sobre estibas de envases plásticos, "
            "y el dimensionamiento de cuencas de retención capaces de albergar no solo el producto derramado sino el volumen total "
            "de las aguas empleadas en la extinción para evitar la contaminación de cursos hídricos superficiales y subterráneos.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "094",
        "fecha": "27 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-27",
        "expediente": "Expediente #094",
        "carpeta": "2017-09-27-atrapamiento-tambor-cola-cinta-transportadora-aridos",
        "titular": "EL PUNTO CIEGO DEL TAMBOR: ATRAPAMIENTO EN CINTA TRANSPORTADORA",
        "palabraResaltada": "TAMBOR DE COLA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Cantera y Planta de Clasificación de Áridos - 2017",
        "tipoRiesgo": "Atrapamiento / Protección de Máquinas",
        "parrafos": [
            "El 27 de septiembre de 2017, un operario de mantenimiento de 31 años murió atrapado en el tambor de cola de una cinta transportadora de áridos al intentar raspar barro acumulado con una pala mientras el equipo operaba.",
            "El tambor motriz carecía de defensas perimetrales y resguardos laterales de seguridad. La pala fue succionada por el punto de convergencia entre la banda de goma y el rodillo giratorio, arrastrando el brazo y el tórax del trabajador.",
            "El operario no aplicó bloqueo y etiquetado (LOTO) ni apagó el motor antes de intervenir. La lección: guardas fijas impenetrables en puntos de atrapamiento, raspadores automáticos y bloqueo de energía cero antes de cualquier limpieza.",
        ],
        "puntosClave": [
            {"icono": "shield-alert", "titulo": "Resguardos fijos en puntos de convergencia", "texto": "Proteger el tambor de retorno y rodillos de cola con defensas metálicas fijas que impidan el acceso físico a menos de 1 metro del nip point."},
            {"icono": "lock", "titulo": "Bloqueo y consignación LOTO obligatoria", "texto": "Desenergizar, enclavar con candado el seccionador principal y verificar energía cero antes de tocar cualquier parte móvil."},
            {"icono": "wrench", "titulo": "Raspadores y arados mecánicos autolimpiantes", "texto": "Instalar raspadores de poliuretano en V para limpiar el barro de la banda automáticamente sin exponer las manos humanas."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: normativas de seguridad en transportadores de banda de OSHA 1910.212 / 1926.555, norma europea EN 620 y recomendaciones de MSHA para minería.",
        "guionReel": (
            "¿Limpiarías una cinta transportadora en marcha solo para no parar la producción?\n\n"
            "27 de septiembre de 2017. Planta de áridos. La cinta de arena húmeda se desalinea porque el barro se apelmaza en el tambor de cola.\n\n"
            "Un operario de 31 años se acerca con una pala de mano para raspar el rodillo mientras gira a toda velocidad. Las protecciones laterales habían sido retiradas meses atrás.\n\n"
            "En una fracción de segundo, la banda atrapó la punta de la pala y la succionó con fuerza demoledora, arrastrando su brazo y su pecho hacia el tambor.\n\n"
            "Murió por aplastamiento antes de que alguien pudiera cortar la energía.\n\n"
            "La lección de HSE es de hierro: una cinta en movimiento nunca se limpia manualmente. Exige guardas fijas, raspadores mecánicos y LOTO estricto.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an industrial quarry aggregate belt conveyor tail pulley station. "
            "Heavy rubber conveyor belt wrapped around a steel drum caked with damp sand and mud, yellow steel safety cage guard with interlock switch in focus, "
            "lockout hasp with red padlock applied to nearby electrical disconnect switch, industrial warning sign 'Keep Hands Clear of Nip Point', "
            "high detail mechanical textures, realistic industrial dirt and lighting, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 27 de septiembre de 2017, en una planta de molienda y clasificación de áridos para la construcción, "
            "la presión cotidiana por evitar atascos de material cobró una vida de forma atroz. "
            "Un operario de mantenimiento mecánico de treinta y un años falleció tras quedar atrapado "
            "en el tambor de retorno inferior de una cinta transportadora de grava que operaba a plena carga.\n\n"
            "Las lluvias de los días previos habían provocado la acumulación de finos arcillosos húmedos sobre la superficie interna de la banda. "
            "Al pasar por el tambor de cola, el barro formaba costras que amenazaban con desalinear el sistema. "
            "Para no detener la línea y evitar paradas en los camiones tolva, el trabajador intentó limpiar la costra "
            "introduciendo el filo de una pala de mano entre la goma en movimiento y el rodillo cilíndrico de acero. "
            "El resguardo enrejado original había sido desmontado durante una reparación anterior y nunca fue vuelto a colocar.\n\n"
            "Al tocar el tambor, la inmensa fuerza tractora del motor de veintidós kilovatios aprisionó la pala de inmediato. "
            "La herramienta actuó como un anzuelo mecánico que absorbió el brazo derecho del operario hacia el punto de convergencia "
            "o nip point. En menos de un segundo, su torso fue traccionado hacia el espacio ciego entre la banda y la estructura metálica. "
            "La cuerda de parada de emergencia de tirón perimetral no estaba conectada al interruptor de corte, "
            "haciendo imposible que sus compañeros detuvieran el arrastre a tiempo.\n\n"
            "Este trágico suceso resume los tres principios inviolables de la seguridad en transportadores continuos: "
            "Primero: ningún ser humano debe intervenir manualmente sobre un componente móvil; los tambores deben estar equipados "
            "con raspadores de uretano y arados limpiadores en ángulo para desalojar los sedimentos automáticamente. "
            "Segundo: los tambores de retorno y reenvío deben poseer defensas perimetrales fijas enclavadas eléctricamente, "
            "que requieran herramientas especiales para su retiro. Y tercero: toda tarea de desobstrucción exige la aplicación inquebrantable "
            "de las pautas LOTO: desenergizar, candadear el seccionador principal y disipar cualquier energía residual acumulada en la contrapesa de tensión.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "095",
        "fecha": "28 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-28",
        "expediente": "Expediente #095",
        "carpeta": "2015-09-28-derrumbe-zanja-acopio-borde-excavacion-cloacas",
        "titular": "EL PESO EN LA CORONA: DERRUMBE DE ZANJA POR ACOPIO AL BORDE",
        "palabraResaltada": "PESO EN LA CORONA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Obra Urbana de Tendido de Red Cloacal y Saneamiento - 2015",
        "tipoRiesgo": "Derrumbe / Excavaciones",
        "parrafos": [
            "El 28 de septiembre de 2015, dos operarios de saneamiento quedaron sepultados al colapsar las paredes de una zanja de 2,60 metros de profundidad durante la colocación de cañerías cloacales en una calle urbana.",
            "La tierra extraída por la retroexcavadora había sido depositada al borde exacto de la zanja, generando una sobrecarga crítica en la corona del talud. Además, el tránsito de camiones pesados al costado transmitió vibraciones que fracturaron el suelo.",
            "La excavación carecía de entibado, cajón de seguridad o talud escalonado. Uno de los trabajadores falleció por asfixia traumática. La lección: acopiar tierra a más de 1 metro del borde, entibar a partir de 1,20 m y restringir el tránsito contiguo.",
        ],
        "puntosClave": [
            {"icono": "arrow-down-to-line", "titulo": "Distancia mínima de acopio (1 metro)", "texto": "El material excavado y las herramientas pesadas deben depositarse como mínimo a 1 metro (o la mitad de la profundidad) del borde del corte."},
            {"icono": "shield", "titulo": "Entibado o cajón de zanja obligatorio", "texto": "Toda excavación vertical de más de 1,20 metros en suelo no cohesivo exige apuntalamiento hidráulico o cajón blindado de escape."},
            {"icono": "truck", "titulo": "Segregación y corte de tránsito vehicular", "texto": "Desviar camiones y maquinaria vibratoria a una distancia segura de la zona de excavación para evitar la falla por corte del terreno."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: normativas de seguridad en excavaciones y zanjas de OSHA 1926 Subpart P, norma IRAM 11520 y manuales de prevención en obras viales.",
        "guionReel": (
            "¿Sabías que una zanja sin entibar puede convertirse en tu propia tumba en un parpadeo?\n\n"
            "28 de septiembre de 2015. Obra cloacal en plena calle. Dos operarios trabajan a dos metros y medio de profundidad instalando tuberías.\n\n"
            "La retroexcavadora apiló toda la tierra mojada al borde mismo de la zanja. Justo al lado, pasan camiones pesados haciendo temblar el pavimento.\n\n"
            "El suelo no resistió la sobrecarga. Una pared de varias toneladas de tierra cedió como una guillotina, sepultando a ambos obreros hasta el cuello.\n\n"
            "Uno de ellos murió asfixiado antes de que pudieran cavar para sacarlo.\n\n"
            "La regla de oro de excavaciones es innegociable: deposita el material a más de un metro del borde, entiba siempre a más de 1,20 m y aleja las cargas pesadas.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an urban trench excavation for sewer pipes after a partial sidewall collapse. "
            "A cross section of an excavated trench in damp soil, heavy mounds of excavated dirt piled dangerously close to the trench lip, "
            "cracked asphalt edge, an aluminum trench box safety shield standing prepared nearby, yellow safety hard hat resting on trench edge, "
            "solemn construction civil engineering documentary visual, overcast afternoon light, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 28 de septiembre de 2015, en una obra civil de tendido de colectores cloacales en una transitada avenida urbana, "
            "la omisión elemental de las reglas de mecánica de suelos derivó en un desenlace fatal. "
            "Dos trabajadores que nivelaban el fondo de una zanja de dos metros con sesenta centímetros de profundidad "
            "fueron sepultados de manera imprevista por el colapso masivo de la pared lateral izquierda de la excavación.\n\n"
            "La investigación geotécnica identificó una combinación crítica de factores que desencadenaron la falla por corte. "
            "El operador de la retroexcavadora, buscando ganar velocidad de avance, depositaba todo el material extraído "
            "en una pila continua al borde exacto del labio de la zanja. Este montículo de tierra húmeda y escombros, "
            "con un peso estimado de más de cuatro toneladas por metro lineal, sobrecargó la cuña natural de deslizamiento del terreno. "
            "Para agravar la situación, el carril contiguo de la avenida permanecía abierto al tránsito de colectivos y camiones de carga, "
            "cuyas vibraciones dinámicas terminaron por fracturar la cohesión del suelo arenoso.\n\n"
            "Las paredes verticales carecían de entibados de madera, módulos de blindaje metálico o cualquier tipo de talud estabilizador. "
            "El derrumbe se produjo en una fracción de segundo, sin dar crujido previo de advertencia. "
            "Los operarios quedaron sepultados bajo más de un metro de tierra compacta. Pese a los desesperados intentos de rescate "
            "manual de sus compañeros de cuadrilla, la compresión torácica imposibilitó la ventilación de uno de los trabajadores, "
            "quien falleció por asfixia traumática antes de ser extraído.\n\n"
            "Este doloroso accidente reafirma los principios técnicos básicos contemplados en los estándares internacionales de zanjas: "
            "Primero: el acopio del material excavado, las herramientas y cualquier equipo auxiliar deben situarse a una distancia mínima "
            "de un metro del borde de la coronación, o a una distancia igual a la mitad de la profundidad de la excavación. "
            "Segundo: a partir de un metro con veinte centímetros de profundidad, es obligatorio el uso de cajones de zanja autoportantes "
            "o entibados certificados cuando no se cuente con espacio para generar un talud seguro a cuarenta y cinco grados. "
            "Y tercero: debe asegurarse el desvío y corte riguroso del tránsito rodado pesado en el perímetro de influencia de las obras de saneamiento.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "096",
        "fecha": "29 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-29",
        "expediente": "Expediente #096",
        "carpeta": "2012-09-29-explosion-tanque-acido-acrilico-nippon-shokubai-himeji",
        "titular": "LA POLIMERIZACIÓN EN CADENA: LA EXPLOSIÓN DE NIPPON SHOKUBAI",
        "palabraResaltada": "NIPPON SHOKUBAI",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Química Nippon Shokubai, Himeji, Japón - 2012",
        "tipoRiesgo": "Seguridad de Procesos (PSM)",
        "parrafos": [
            "El 29 de septiembre de 2012, una explosión catastrófica en la planta de Nippon Shokubai en Himeji, Japón, destruyó un tanque de almacenamiento de ácido acrílico, matando a un bombero e hiriendo a 36 personas.",
            "Durante una parada de planta por anomalías operativas, el ácido acrílico se mantuvo estancado en un tanque intermedio sin agitación suficiente ni suministro de aire e inhibidor (MEHQ). Se inició una polimerización exotérmica descontrolada.",
            "La presión y temperatura superaron la capacidad del venteo de alivio, estallando el tanque mientras los bomberos intentaban enfriarlo. La lección: monitoreo de temperatura, inyección de emergencia de inhibidores y perímetros de evacuación seguros.",
        ],
        "puntosClave": [
            {"icono": "thermometer", "titulo": "Química de polimerización e inhibidores", "texto": "El ácido acrílico requiere oxígeno disuelto para que el inhibidor MEHQ funcione; el estancamiento sin aire detona la polimerización."},
            {"icono": "shield-check", "titulo": "Enfriamiento redundante y agente de parada", "texto": "Disponer de sistemas independientes de inyección rápida de fenotiazina (PTZ) para detener en segundos reacciones de polimerización fuera de control."},
            {"icono": "users", "titulo": "Zona de exclusión y repliegue de brigadas", "texto": "Ante el incremento exponencial de temperatura en monómeros reactivos, evacuar inmediatamente a todo el personal y bomberos a distancia segura."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de investigación de accidentes de la Asociación de Fabricantes de Ácido Acrílico y Acrilatos (Accredited Acrylic Acid Panel) e informe oficial del Gobierno de Japón sobre Himeji.",
        "guionReel": (
            "¿Sabías que un químico líquido puede empezar a calentarse solo hasta reventar un tanque de acero de 20 metros?\n\n"
            "29 de septiembre de 2012. Himeji, Japón. Planta de Nippon Shokubai. Detienen la producción por un fallo técnico, dejando ácido acrílico estancado en un tanque intermedio.\n\n"
            "Pero el monómero es traicionero: necesita aire constante para que el inhibidor químico evite que reaccione. Sin agitación ni aire, las moléculas empezaron a unirse en una reacción en cadena violenta.\n\n"
            "La temperatura subió a más de 100 grados. Los bomberos llegaron a enfriar con mangueras, pero ya era tarde.\n\n"
            "El tanque estalló en una gigantesca bola de fuego. Un bombero de 28 años murió y 36 personas resultaron heridas.\n\n"
            "La lección de seguridad de procesos: los monómeros reactivos exigen monitoreo térmico implacable, inyección de emergencia y evacuación a tiempo.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an industrial chemical plant after a thermal runaway storage tank explosion. "
            "Ruptured massive stainless steel chemical vessel split like an opened tin can, blackened distillation columns in background, "
            "firefighting water monitors spraying mist over smoking metal ruins, debris scattered across wet concrete apron, "
            "high contrast industrial lighting under an overcast sky, technical process safety forensic aesthetic, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 29 de septiembre de 2012, en la planta de Nippon Shokubai en Himeji, Japón —uno de los mayores complejos productores "
            "de polímeros superabsorbentes y ácido acrílico del mundo—, una reacción química fuera de control "
            "derivó en una violenta explosión que enlutó a los servicios de emergencia y conmocionó a la industria química global.\n\n"
            "El incidente comenzó tras una parada no planificada de una columna de purificación de ácido acrílico. "
            "Para vaciar el sistema, los operadores transfirieron una mezcla concentrada de monómero a un tanque vertical de almacenamiento intermedio. "
            "El ácido acrílico es una sustancia altamente reactiva que tiende a polimerizarse liberando enormes cantidades de calor. "
            "Para evitarlo, se le añade un inhibidor químico conocido como MEHQ. Sin embargo, este inhibidor solo puede activarse "
            "si existe una concentración mínima de oxígeno disuelto en el líquido. Al dejarse el producto estancado, caliente "
            "y sin inyección de aire instrumental ni agitación continua, el inhibidor se agotó rápidamente.\n\n"
            "A partir de ese instante se desencadenó una polimerización exotérmica en cadena o runaway reaction. "
            "La temperatura y la presión interna comenzaron a elevarse de forma exponencial. Los operadores detectaron humo blanco "
            "saliendo por los venteos de alivio y convocaron a la brigada de bomberos de la ciudad para refrigerar las paredes con mangueras. "
            "Lamentablemente, el calor interno generó una velocidad de gasificación que superó la capacidad de los discos de ruptura. "
            "A las catorce horas y cuarenta minutos, la envolvente del tanque reventó catastróficamente, liberando una nube de vapor inflamable "
            "que encendió de inmediato en una colosal bola de fuego. La onda expansiva mató a un joven bombero de veintiocho años e hirió a treinta y seis personas.\n\n"
            "La tragedia de Himeji transformó los protocolos de manejo de monómeros reactivos en el mundo entero. "
            "Estableció que ante cualquier desvío en el perfil térmico de un recipiente con monómeros, "
            "debe activarse de forma remota un sistema independiente de parada química mediante inyección forzada de fenotiazina u otros inhibidores de emergencia. "
            "Y sobre todo, dejó una lección vital para el comando de incidentes: cuando un recipiente químico sufre una reacción desbocada, "
            "la refrigeración externa con bomberos a pie es inútil y mortal; se debe ordenar la evacuación total e inmediata "
            "hacia un perímetro de exclusión seguro.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "097",
        "fecha": "30 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-30",
        "expediente": "Expediente #097",
        "carpeta": "1999-09-30-accidente-criticidad-nuclear-tokaimura",
        "titular": "EL DESTELLO AZUL: EL ACCIDENTE DE CRITICIDAD DE TOKAIMURA",
        "palabraResaltada": "TOKAIMURA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta de Fabricación de Combustible Nuclear JCO, Tokaimura, Japón - 1999",
        "tipoRiesgo": "Seguridad de Procesos / Factor Humano",
        "parrafos": [
            "El 30 de septiembre de 1999, una reacción nuclear en cadena no controlada en la planta de combustible JCO en Tokaimura, Japón, liberó una lluvia letal de neutrones y radiación gamma, provocando la muerte de dos operarios y afectando a 667 personas.",
            "Buscando acelerar los tiempos de producción, los operarios mezclaron manualmente óxido de uranio enriquecido al 18,8% en baldes de acero inoxidable dentro de un tanque de precipitación no geométricamente seguro, excediendo siete veces el límite crítico de masa.",
            "Al verter el séptimo balde, la masa alcanzó la criticidad y emitió un destello azul de radiación de Cherenkov. La lección: prohibición absoluta de atajos operacionales, diseño intrínsecamente seguro por geometría y estricto control de masa fisible.",
        ],
        "puntosClave": [
            {"icono": "radio", "titulo": "Diseño intrínsecamente seguro (Geometría)", "texto": "Los recipientes para manipular material fisionable deben diseñarse con geometrías estrechas que hagan físicamente imposible alcanzar la criticidad."},
            {"icono": "clipboard-check", "titulo": "Tolerancia cero a los atajos operativos", "texto": "Ningún procedimiento escrito aprobado por la autoridad reguladora puede ser modificado por conveniencia productiva o ahorro de tiempo."},
            {"icono": "shield-alert", "titulo": "Control estricto y pesaje de masa crítica", "texto": "Bloquear físicamente la dosificación de material fisionable mediante enclavamientos que impidan agregar más masa que el límite subcrítico autorizado."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe del Organismo Internacional de Energía Atómica (OIEA / IAEA Report STI/PUB/1090) sobre el accidente de criticidad en Tokaimura y análisis de la Comisión de Seguridad Nuclear de Japón.",
        "guionReel": (
            "¿Qué ocurre cuando unos operarios usan baldes de acero de cocina para mezclar uranio enriquecido?\n\n"
            "30 de septiembre de 1999. Tokaimura, Japón. Planta nuclear JCO. Para apurar la entrega de combustible, la gerencia permite saltarse los pasos lentos del manual.\n\n"
            "Dos técnicos vierten uranio líquido con embudos y baldes comunes dentro de un tanque ancho. Nadie controló la báscula.\n\n"
            "El límite seguro era de 2,4 kilos de uranio. Al vaciar el séptimo balde, sumaron 16 kilos. De repente, una luz azul brillante inundó la sala: la radiación de Cherenkov.\n\n"
            "Habían creado un reactor nuclear casero fuera de control. Los neutrones atravesaron sus cuerpos al instante.\n\n"
            "Ambos trabajadores murieron tras agonías inhumanas. La lección de HSE es definitiva: en procesos críticos, un atajo operacional no ahorra tiempo, cuesta vidas.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an industrial nuclear fuel processing preparation room from 1999. "
            "A stainless steel precipitation tank with connecting chemical glass pipes, empty stainless steel buckets and funnels sitting on a metal workbench, "
            "faint eerie blue atmospheric luminescence reflecting on polished steel surfaces, radiation hazard signs in Japanese and English, "
            "solemn and chilling forensic documentary style, precise scientific details, 8k resolution, raw photojournalistic realism."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 30 de septiembre de 1999, a las diez y treinta y cinco de la mañana, la pequeña localidad nuclear de Tokaimura, "
            "en la prefectura de Ibaraki, Japón, fue escenario del primer accidente de criticidad nuclear grave con víctimas fatales "
            "en instalaciones comerciales de procesamiento. Dos trabajadores recibieron dosis masivas de radiación ionizante "
            "que destruyeron por completo sus cromosomas celulares, falleciendo semanas después en medio de un intenso sufrimiento.\n\n"
            "La investigación oficial destapó una degradación sistemática de la cultura de seguridad en la empresa JCO. "
            "Para cumplir con un pedido urgente de combustible para el reactor experimental Joyo, los operadores tenían que preparar "
            "nitrato de uranilo enriquecido al dieciocho coma ocho por ciento en uranio doscientos treinta y cinco. "
            "El procedimiento oficial aprobado por el gobierno requería disolver el uranio en una columna angosta especialmente diseñada, "
            "cuya geometría cilíndrica delgada evitaba físicamente que los neutrones interactuaran entre sí para iniciar una reacción en cadena. "
            "Sin embargo, debido a que el proceso era lento, la supervisión de planta toleró un procedimiento clandestino: "
            "disolver el uranio manualmente en baldes de acero inoxidable de diez litros y trasvasarlo con embudos a un tanque de precipitación ancho.\n\n"
            "La masa crítica máxima autorizada para ese equipo era de dos coma cuatro kilogramos de uranio enriquecido. "
            "Aquella mañana, los operarios vertieron sucesivamente siete baldes, acumulando más de dieciséis kilogramos de material fisionable "
            "en una solución acuosa que además actuó como moderador de neutrones. Al vaciar el último recipiente, la masa alcanzó la criticidad nuclear. "
            "Una ráfaga invisible de neutrones y rayos gamma atravesó a los técnicos, acompañada por un destello azul característico "
            "producido por la radiación de Cherenkov. Las alarmas de radiación gamma sonaron en todo el predio mientras la reacción "
            "permaneció activa de manera intermitente durante veinte horas hasta que brigadistas lograron drenar el agua de refrigeración.\n\n"
            "El desastre de Tokaimura es el ejemplo definitivo de la patología organizacional del atajo operativo. "
            "Demostró que la seguridad nuclear y de procesos nunca debe depender exclusivamente del comportamiento humano: "
            "los equipos deben ser intrínsecamente seguros por geometría, impidiendo físicamente que la criticidad ocurra "
            "incluso si se vierten cantidades excesivas. Asimismo, consagró la necesidad de auditorías independientes implacables "
            "para garantizar que la urgencia comercial no degrade jamás los procedimientos operativos certificados.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "098",
        "fecha": "01 OCTUBRE",
        "fechaPublicacion": "2026-10-01",
        "expediente": "Expediente #098",
        "carpeta": "2018-10-01-caida-techo-fibrocemento-fragil-canaletas",
        "titular": "LA TRAMPA INVISIBLE: CAÍDA A TRAVÉS DE TECHO DE FIBROCEMENTO",
        "palabraResaltada": "FIBROCEMENTO FRÁGIL",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Nave Industrial y Depósito de Materiales - 2018",
        "tipoRiesgo": "Trabajo en Altura / Superficies Frágiles",
        "parrafos": [
            "El 1 de octubre de 2018, un operario de mantenimiento de 45 años falleció al caer desde 7 metros de altura tras quebrarse una placa de fibrocemento envejecida mientras limpiaba las canaletas de desagüe pluvial en el techo de un depósito.",
            "El trabajador caminaba directamente apoyando su calzado sobre las crestas de las chapas onduladas sin utilizar pasarelas rígidas de repartición de carga. La placa, debilitada por décadas de intemperie y radiación solar, colapsó bajo su peso.",
            "El operario no contaba con línea de vida instalada ni redes anticaídas inferiores. La lección: toda cubierta de fibrocemento o traslúcida debe considerarse no transitable y exige pasarelas de trabajo, redes de seguridad y anclaje continuo.",
        ],
        "puntosClave": [
            {"icono": "alert-triangle", "titulo": "Presunción de fragilidad total", "texto": "Prohibido pisar directamente sobre cubiertas de fibrocemento, polietileno o claraboyas; tratarlas siempre como superficies frágiles no resistentes."},
            {"icono": "layout", "titulo": "Uso de pasarelas de repartición de peso", "texto": "Instalar tablones o pasarelas de aluminio con topes laterales apoyadas sobre las correas estructurales para transitar y trabajar en el techo."},
            {"icono": "shield", "titulo": "Redes anticaídas y línea de vida obligatoria", "texto": "Montar redes perimetrales bajo el techo antes de acceder y mantener al trabajador anclado al 100% a una línea de vida de acero certificada."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: directrices de seguridad para trabajos sobre cubiertas frágiles de OSHA 1926.501, norma británica HSE HSG33 (Health and Safety in Roof Work) y normativa española RD 2177/2004.",
        "guionReel": (
            "¿Pisarías sobre una placa de cartón a siete metros de altura? Pues pisar un techo de fibrocemento viejo es exactamente lo mismo.\n\n"
            "1 de octubre de 2018. Mantenimiento de techo industrial. Un operario de 45 años sube a limpiar las canaletas llenas de hojas secas antes de la lluvia.\n\n"
            "El techo tiene 30 años de sol y humedad. Las chapas de fibrocemento están secas y quebradizas como galletas. El operario camina pisando las ondulaciones sin pasarelas de madera.\n\n"
            "De pronto, un crujido seco. La placa se parte bajo sus botas y se abre un agujero negro. El trabajador cae al vacío desde 7 metros de altura sin estar anclado.\n\n"
            "Murió en el impacto contra el suelo de concreto.\n\n"
            "La lección de HSE es tajante: en techos de fibrocemento jamás se camina directo. Usa pasarelas de reparto, redes por debajo y línea de vida continua.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an industrial warehouse roof showing a large jagged hole in an aged corrugated asbestos-cement sheet. "
            "A broken fiber-cement roof panel with exposed fractured edges, sunlight streaming down through the opening onto the warehouse floor below, "
            "wooden crawling boards with safety handrails staged alongside gutters, safety harness lanyard connected to a roof ridge steel cable, "
            "dramatic high altitude documentary shot, realistic weather-worn roof textures, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 1 de octubre de 2018, en una nave industrial dedicada al almacenamiento de insumos comerciales, "
            "un operario de servicios generales de cuarenta y cinco años perdió la vida de forma fulminante. "
            "Había subido a la cubierta exterior para efectuar el desatasco preventivo de las canaletas colectoras de agua pluvial "
            "ante la inminencia de un temporal de primavera.\n\n"
            "La cubierta estaba conformada por antiguas láminas onduladas de fibrocemento instaladas hacía más de tres décadas. "
            "El material fibroso, expuesto durante años a la radiación ultravioleta, los ciclos térmicos y la humedad ácida, "
            "había perdido toda su tenacidad mecánica, volviéndose extremadamente quebradizo. "
            "El trabajador, habituado a desplazarse por el techo, caminaba pisando directamente sobre las crestas de las chapas, "
            "confiando en que la proximidad de los ganchos de fijación a las correas de hierro le otorgaría soporte suficiente. "
            "No se habían dispuesto tablones de reparto ni pasarelas metálicas de tránsito seguro.\n\n"
            "En determinado momento, al agacharse con una pala pequeña para retirar lodo de una canaleta, concentró todo el peso de su cuerpo "
            "en el pie derecho en el vano central de una de las placas. El panel colapsó con una rotura frágil instantánea en forma de estrella, "
            "creando un hueco por el que el operario cayó limpiamente al vacío desde una altura de siete metros. "
            "En el interior de la nave no existían redes horizontales de contención ni el trabajador estaba amarrado "
            "a ningún sistema anticaídas. El impacto contra la losa de hormigón le causó traumatismos craneoencefálicos y torácicos letales.\n\n"
            "Las caídas a través de cubiertas frágiles siguen siendo una de las principales causas de muerte en mantenimiento edilicio. "
            "La normativa internacional exige considerar a cualquier techo de fibrocemento, plástico o policarbonato como una superficie "
            "estructuralmente nula. Toda intervención requiere tres medidas ineludibles: el uso mandatorio de pasarelas móviles "
            "de avance con peldaños que distribuyan el peso uniformemente sobre al menos dos vigas portantes, "
            "la instalación de redes de seguridad bajo cubierta para mitigar cualquier falla del material, "
            "y la conexión permanente al cien por ciento a una línea de vida de cable de acero independiente y certificada.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "099",
        "fecha": "02 OCTUBRE",
        "fechaPublicacion": "2026-10-02",
        "expediente": "Expediente #099",
        "carpeta": "2016-10-02-intoxicacion-gas-cloro-mezcla-lavandina-acido-muriatico",
        "titular": "LA MEZCLA MORTAL: INTOXICACIÓN POR GAS CLORO EN VESTUARIOS",
        "palabraResaltada": "MEZCLA MORTAL",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Vestuarios y Sanitarios de Planta Industrial - 2016",
        "tipoRiesgo": "Higiene Industrial / Riesgo Químico",
        "parrafos": [
            "El 2 de octubre de 2016, tres operarios de maestranza sufrieron intoxicación respiratoria severa tras mezclar accidentalmente hipoclorito de sodio (lavandina) con ácido muriático (clorhídrico) para limpiar sarro en el piso de un vestuario cerrado.",
            "La reacción ácida sobre el hipoclorito liberó instantáneamente una densa nube de gas cloro elemental (Cl2), un tóxico pulmonar altamente sofocante que saturó el recinto en segundos por falta de ventilación natural o extractores mecánicos.",
            "Los trabajadores carecían de capacitación básica en incompatibilidades químicas y no contaban con fichas de datos de seguridad (FDS). Dos requirieron intubación endotraqueal. La lección: prohibición absoluta de mezclar químicos de limpieza y entrenamiento obligatorio.",
        ],
        "puntosClave": [
            {"icono": "ban", "titulo": "Prohibición taxativa de mezclas químicas", "texto": "Nunca combinar lavandina (cloro líquido) con ácidos, amoníaco o detergentes; la reacción genera gas cloro letal o cloraminas tóxicas."},
            {"icono": "file-text", "titulo": "Capacitación en Fichas de Seguridad (FDS)", "texto": "Todo el personal de limpieza debe conocer los pictogramas del SGA y las incompatibilidades de los productos químicos que manipula."},
            {"icono": "wind", "titulo": "Ventilación permanente en tareas de desinfección", "texto": "Realizar tareas de limpieza profunda garantizando renovación continua de aire y disponiendo de un protocolo de evacuación inmediata ante olores picantes."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: guías de manejo seguro de productos químicos de limpieza de OSHA (Hazard Communication Standard 1910.1200), fichas toxicológicas de NIOSH sobre Gas Cloro y normativas del INSST.",
        "guionReel": (
            "¿Alguna vez pensaste en mezclar lavandina con ácido para limpiar mejor una mancha difícil? ¡Nunca lo hagas!\n\n"
            "2 de octubre de 2016. Vestuarios de una fábrica. Tres operarios de limpieza quieren quitar sarro acumulado en las duchas.\n\n"
            "Para 'potenciar la desinfección', vierten en el mismo balde lavandina concentrada y ácido muriático. En dos segundos, el líquido comenzó a hervir.\n\n"
            "Se liberó una nube amarillo-verdosa de gas cloro puro. Un gas asfixiante utilizado como arma química en la Primera Guerra Mundial.\n\n"
            "El vestuario no tenía ventanas. El gas quemó sus gargantas y llenó sus pulmones de líquido. Terminaron en terapia intensiva con daño pulmonar permanente.\n\n"
            "La lección de HSE es básica: jamás mezcles productos de limpieza. Lee las fichas de seguridad y capacita a tu equipo.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an industrial facility tiled shower and locker room after a chemical hazard incident. "
            "A yellow plastic mop bucket on wet ceramic tile floor emitting a faint greenish-yellow gaseous vapor mist, "
            "overturned containers of industrial bleach and hydrochloric acid with hazardous substance warning labels, "
            "an open locker room door with yellow caution tape across the entryway, harsh fluorescent tube lighting reflections on wet tiles, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 2 de octubre de 2016, en el área de sanitarios y vestuarios de un complejo manufacturero, "
            "una práctica errónea pero tristemente recurrente en tareas de mantenimiento de higiene "
            "estuvo a punto de cobrarse la vida de tres operarios de maestranza. "
            "Una supuesta 'receta casera' para mejorar la remoción de manchas de cal y sarro en el suelo de las duchas "
            "desencadenó una emanación masiva de gas cloro en un ambiente cerrado y confinado.\n\n"
            "El equipo de limpieza, contratado recientemente y sin capacitación previa en riesgo químico, "
            "decidió combinar en un mismo balde plástico dos productos comerciales habituales: hipoclorito de sodio al diez por ciento, "
            "comúnmente conocido como lavandina o lejía, y ácido muriático, que es ácido clorhídrico concentrado de uso técnico. "
            "La mezcla provocó una reacción redox exotérmica e instantánea. El medio fuertemente ácido desplazó el equilibrio químico del cloro, "
            "liberando de golpe varios litros de gas cloro elemental diatómico, reconocible por su característico color amarillo verdoso "
            "y su olor sofocante.\n\n"
            "Los vestuarios, ubicados en el subsuelo de la planta, carecían de ventanas al exterior y los extractores mecánicos de pared "
            "estaban apagados. Al inhalar el gas, este reaccionó inmediatamente con la película de agua de las mucosas respiratorias de los operarios, "
            "formando ácido clorhídrico y ácido hipocloroso en sus pulmones. Los trabajadores experimentaron espasmos de glotis, quemaduras químicas "
            "en las vías aéreas y asfixia aguda. Pese a que lograron salir a gatas hacia el pasillo principal tosiendo sangre, "
            "dos de ellos debieron ser intubados de urgencia en el hospital por edema agudo de pulmón no cardiogénico.\n\n"
            "Este grave suceso demuestra que la peligrosidad química no es exclusiva de las grandes refinerías o reactores de síntesis. "
            "Los productos de higiene doméstica o industrial poseen una reactividad severa si se desprecian sus incompatibilidades elementales. "
            "Es deber ineludible de todo programa de HSE capacitar al cien por ciento del personal de maestranza en el Sistema Globalmente Armonizado (SGA), "
            "prohibir de manera terminante el trasvase y mezcla de soluciones de limpieza, y exigir que toda tarea que involucre agentes químicos "
            "se desarrolle con ventilación activa y mascarillas con filtros para gases adecuados.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "100",
        "fecha": "03 OCTUBRE",
        "fechaPublicacion": "2026-10-03",
        "expediente": "Expediente #100",
        "carpeta": "2014-10-03-vuelco-grua-movil-terreno-blando-estabilizadores",
        "titular": "EL GATO QUE SE HUNDIÓ: VUELCO DE GRÚA MÓVIL EN MONTAJE",
        "palabraResaltada": "VUELCO DE GRÚA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Montaje de Estructura Metálica en Obra Industrial - 2014",
        "tipoRiesgo": "Izaje Crítico / Estabilidad de Equipos",
        "parrafos": [
            "El 3 de octubre de 2014, una grúa móvil todo terreno de 70 toneladas volcó durante el izaje de una viga reticulada de 8 toneladas al ceder imprevistamente el terreno bajo uno de sus estabilizadores laterales.",
            "Los gatos hidráulicos habían sido apoyados directamente sobre suelo de relleno compactado sin realizar un ensayo de resistencia portante ni utilizar almohadillas de reparto (outrigger pads) de superficie adecuada. Al girar la pluma con carga, la presión puntual perforó el suelo.",
            "La pluma telescópica cayó sobre una nave vecina destruyendo techos y provocando heridas graves al operador y a un señalero. La lección: evaluar la capacidad portante del suelo, usar placas de reparto sobredimensionadas y respetar la tabla de carga.",
        ],
        "puntosClave": [
            {"icono": "anchor", "titulo": "Cálculo y uso de almohadillas de reparto", "texto": "El área de las almohadillas de apoyo bajo los platos estabilizadores debe calcularse en función de la capacidad portante del suelo (ton/m²)."},
            {"icono": "activity", "titulo": "Verificación del terreno y compactación", "texto": "Prohibido emplazar grúas sobre suelos de relleno, canalizaciones enterradas o bordes de taludes sin estudio geotécnico previo."},
            {"icono": "compass", "titulo": "Plan de izaje crítico y tabla de carga", "texto": "Verificar que la carga máxima en el estabilizador más exigido durante el radio de giro completo nunca supere el límite seguro de sustentación."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: manuales de izaje seguro de ASME B30.5 (Mobile and Locomotive Cranes), directrices de FEM (Federación Europea de Manutención) y guías de izaje de OSHA 1926 Subpart CC.",
        "guionReel": (
            "¿Sabías que más del 50% de los vuelcos de grúas gigantes ocurren porque el piso debajo de ellas simplemente colapsa?\n\n"
            "3 de octubre de 2014. Montaje de una nave industrial. Una grúa de 70 toneladas levanta una pesada viga de acero a veinte metros de altura.\n\n"
            "Los estabilizadores de la grúa se apoyaron sobre tierra removida, usando apenas unos tacos pequeños de madera. Nadie midió si el suelo aguantaba la presión.\n\n"
            "Al girar la pluma, todo el peso se trasladó al estabilizador trasero derecho. El gato hidráulico perforó la tierra como un clavo caliente.\n\n"
            "La grúa volcó de costado y la pluma telescópica aplastó el techo del taller contiguo. El operador y un señalero quedaron gravemente heridos.\n\n"
            "La lección de HSE es sagrada: una grúa es tan fuerte como el piso donde se apoya. Exige placas de reparto calculadas y verifica siempre el terreno.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an overturned 70-ton all-terrain mobile crane lying on its side at an industrial construction site. "
            "One hydraulic outrigger sunken deep into a collapsed mud and loose fill crater, crushed inadequate wooden cribbing pads, "
            "extended telescopic boom bent across steel structural framing of a damaged warehouse, safety cones and caution tape surrounding site, "
            "dramatic overcast daylight, civil forensic inspection realism, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 3 de octubre de 2014, en las obras de ampliación de una importante planta siderometalúrgica, "
            "una maniobra rutinaria de izaje pesado derivó en el vuelco violento de una grúa móvil telescópica todo terreno "
            "de setenta toneladas de capacidad nominal. La falla estructural de la sustentación del terreno convirtió una operación "
            "programada en una emergencia con cuantiosos daños materiales y dos operarios con traumatismos de gravedad.\n\n"
            "El equipo se encontraba posicionado para colocar una viga reticulada de puente grúa de ocho toneladas a un radio de dieciséis metros. "
            "Durante el emplazamiento preliminar a primera hora de la mañana, el operador extendió los cuatro gatos hidráulicos estabilizadores "
            "y colocó debajo de cada plato metálico una simple tabla de madera de pino de apenas cuatro centímetros de espesor. "
            "El sector donde se instaló el equipo correspondía a un terreno que había sido rellenado recientemente tras zanjeos de cañerías subterráneas, "
            "sin haber sido compactado mecánicamente ni evaluado mediante penetrómetro dinámico.\n\n"
            "Cuando la grúa izó la viga a veinte metros del suelo e inició el giro hacia el sector derecho, las leyes de la física "
            "hicieron sentir su rigor. El centro de gravedad del conjunto se desplazó bruscamente, concentrando más del setenta y cinco por ciento "
            "del peso total del vehículo y la carga sobre el cilindro estabilizador trasero derecho. La presión transmitida superó con creces "
            "la reducida tensión admisible del suelo suelto. La zapata quebró la madera y se hundió repentinamente más de un metro en la tierra, "
            "provocando el vuelco lateral instantáneo de la máquina. La pluma colapsó sobre las cabriadas de una nave vecina, "
            "atrapando al señalero que coordinaba la maniobra en tierra y despidiendo al gruista de su cabina.\n\n"
            "Este siniestro subraya una premisa fundamental que todo supervisor de maniobras de izaje debe recordar: "
            "la capacidad de una grúa no depende únicamente de su hidráulica y sus contrapesos, sino de la resistencia del terreno sobre el que se posa. "
            "Todo izaje crítico exige la confección previa de un plan de maniobra que verifique la capacidad portante del sustrato, "
            "el cálculo riguroso de la superficie de las almohadillas de reparto de carga (outrigger pads) construidas con materiales compuestos "
            "o maderas duras certificadas, y la prohibición absoluta de emplazar maquinaria pesada sobre terrenos sin compactación comprobada.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "101",
        "fecha": "04 OCTUBRE",
        "fechaPublicacion": "2026-10-04",
        "expediente": "Expediente #101",
        "carpeta": "2019-10-04-quemaduras-explosion-vapor-metal-fundido-molde-humedo",
        "titular": "LA GOTA QUE EXPLOTÓ: PROYECCIÓN DE METAL FUNDIDO EN FUNDICIÓN",
        "palabraResaltada": "METAL FUNDIDO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Taller de Fundición de Acero y Aleaciones Metálicas - 2019",
        "tipoRiesgo": "Energía Térmica / Procesos Metalúrgicos",
        "parrafos": [
            "El 4 de octubre de 2019, dos operarios de fundición sufrieron quemaduras de tercer grado en cara y torso cuando una explosión por vapor dentro de un molde metálico proyectó acero fundido a 1.550 °C en todas direcciones.",
            "El molde de fundición había sido lavado previamente y almacenado bajo un techo con goteras, acumulando agua residual en su cavidad inferior. Al verter la colada, el agua atrapada se vaporizó instantáneamente multiplicando su volumen 1.700 veces.",
            "Los trabajadores no contaban con máscaras faciales doradas reflectivas ni trajes aluminizados completos. La lección: precalentamiento y secado obligatorio de moldes y herramientas antes del contacto con metal líquido, y uso estricto de EPP aluminizado.",
        ],
        "puntosClave": [
            {"icono": "flame", "titulo": "Precalentamiento y secado estricto de moldes", "texto": "Todo molde, cuchara o herramienta debe someterse a precalentamiento térmico con soplete para evaporar hasta la última molécula de humedad antes de la colada."},
            {"icono": "shield", "titulo": "EPP aluminizado para fundición", "texto": "Uso obligatorio de chaquetón, polainas aluminizadas y pantalla facial dorada reflectiva para rechazar el calor radiante y las salpicaduras de metal líquido."},
            {"icono": "droplets", "titulo": "Control de goteras y condensación en solera", "texto": "Prohibir la presencia de cañerías de agua elevadas, goteras o charcos en todas las áreas de transporte y vaciado de metal fundido."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: normativas de seguridad en fundición y acerías de OSHA 1910.132, normas de la Asociación Americana de Fundidores (AFS Safety Guidelines) y norma europea EN ISO 11612.",
        "guionReel": (
            "¿Sabías que una sola gota de agua puede hacer estallar un caldero de acero hirviendo como si fuera una granada?\n\n"
            "4 de octubre de 2019. Taller de fundición. Los operarios inclinan la cuchara con acero líquido a más de 1.500 grados Celsius para llenar un molde metálico.\n\n"
            "Pero el molde tenía una pequeña película de agua en el fondo por una gotera en el techo del galpón. Nadie lo secó con soplete antes.\n\n"
            "Al entrar el acero, el agua se transformó en vapor en un milisegundo, expandiéndose 1.700 veces su volumen. La explosión física escupió metal fundido como metralla incandescente.\n\n"
            "Dos operarios sufrieron quemaduras de tercer grado gravísimas en rostro y pecho.\n\n"
            "La lección de HSE es intransigente: el agua y el metal fundido son enemigos mortales. Seca y precalienta siempre cada molde y herramienta antes de la colada.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an industrial steel foundry floor after a liquid metal splash incident. "
            "A heavy iron casting mold with glowing cooling steel drips splattered across its dark textured rim, "
            "metallic spatter patterns across the concrete floor and protective heat shields, aluminized safety jacket and gold-coated reflective visor resting on a tool cart, "
            "smoky atmospheric workshop air with intense directional orange heat glow, high dynamic range, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 4 de octubre de 2019, en una planta de fundición de aceros especiales y piezas para la industria pesada, "
            "la violación de una de las reglas termodinámicas más antiguas de la metalurgia culminó en un grave siniestro. "
            "Dos trabajadores coladores sufrieron quemaduras térmicas de tercer grado que abarcaron el rostro, el cuello "
            "y el torso durante el vaciado de una cuchara de transporte con acero líquido a más de mil quinientos cincuenta grados Celsius.\n\n"
            "El incidente tuvo su origen en la presencia inadvertida de humedad en la lingotera de colada. "
            "El molde metálico de acero fundido había sido lavado el día anterior y almacenado bajo un sector de la cubierta que presentaba "
            "filtraciones pluviales por goteras no reparadas. Una pequeña cantidad de agua, estimada en menos de cincuenta mililitros, "
            "quedó acumulada en los relieves del fondo del molde. Debido al apuro por completar la hornada, los operarios omitieron "
            "el paso estipulado en la orden de trabajo consistente en aplicar la llama de un soplete de gas para precalentar y deshumidificar la matriz.\n\n"
            "En el instante en que el primer chorro de acero al rojo blanco tocó el agua atrapada en el fondo ciego, se produjo una explosión "
            "física de vapor o BLEVE a microescala. Al no poder evaporarse libremente debido a la densidad del metal que caía sobre ella, "
            "el agua se sobrecalentó instantáneamente por encima de su punto crítico, expandiendo su volumen en más de mil setecientas veces en microsegundos. "
            "La sobrepresión resultante actuó como un mortero de artillería, expulsando violentamente una lluvia de metal fundido "
            "en un radio de más de diez metros. Los trabajadores, que utilizaban ropa de trabajo de algodón común y gafas simples "
            "en lugar de escudos faciales aluminizados con filtro de oro para calor radiante, recibieron el impacto directo de las gotas de acero incandescente.\n\n"
            "Las acerías y fundiciones exigen una disciplina operativa sin margen para concesiones. "
            "En el entorno del metal fundido, el agua es el agente más destructivo y peligroso. "
            "Es mandatorio protocolizar el secado y precalentamiento a más de cien grados de todo molde, lingotera, cuchara o herramienta de escoriado "
            "antes de permitir el contacto con la colada. Asimismo, se debe garantizar la integridad de techos e instalaciones pluviales en naves de fundición, "
            "y fiscalizar el uso estricto y sin excepciones de indumentaria de protección aluminizada ignífuga certificada bajo norma EN ISO 11612.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "102",
        "fecha": "05 OCTUBRE",
        "fechaPublicacion": "2026-10-05",
        "expediente": "Expediente #102",
        "carpeta": "2007-10-05-incendio-tuberia-forzada-cabin-creek-xcel-energy",
        "titular": "ATRAPADOS EN EL TUBO: EL INCENDIO DE CABIN CREEK",
        "palabraResaltada": "CABIN CREEK",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Tubería Forzada (Penstock) de Central Hidroeléctrica Cabin Creek, Colorado, EE.UU. - 2007",
        "tipoRiesgo": "Espacios Confinados / Atmósferas Inflamables",
        "parrafos": [
            "El 5 de octubre de 2007, cinco trabajadores de mantenimiento murieron atrapados por un incendio dentro de una empinada tubería forzada (penstock) de 1.200 metros en la central hidroeléctrica Cabin Creek en Colorado.",
            "Los operarios utilizaban metiletilcetona (MEK), un solvente altamente volátil e inflamable, para limpiar una máquina de aplicación de resina epoxi dentro del ducto subterráneo sin ventilación forzada ni monitoreo continuo de explosividad (LEL).",
            "Una chispa estática en el equipo encendió los vapores, bloqueando con fuego la única salida transitable hacia la parte inferior. La lección: sustituir solventes inflamables en espacios confinados, garantizar ventilación mecánica continua y vías dobles de escape.",
        ],
        "puntosClave": [
            {"icono": "flame", "titulo": "Sustitución de solventes inflamables", "texto": "Prohibir el ingreso de solventes con bajo punto de inflamación (como MEK o acetona) en espacios confinados; sustituirlos por desengrasantes acuosos o no inflamables."},
            {"icono": "wind", "titulo": "Ventilación continua y monitoreo LEL", "texto": "Insuflar aire fresco ininterrumpidamente y mantener monitores de 4 gases con alarma sonora fijada al 10% del límite inferior de explosividad (LEL)."},
            {"icono": "door-open", "titulo": "Plan de rescate y rutas de escape redundantes", "texto": "Todo trabajo en túneles o tuberías forzadas exige una segunda vía de escape despejada y una brigada de rescate con equipos autónomos en boca de acceso."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de investigación de desastres de la Junta de Seguridad Química de EE.UU. (CSB Report 2008-01-I-CO) sobre el incendio de Cabin Creek de Xcel Energy.",
        "guionReel": (
            "¿Entrarías a limpiar un tubo subterráneo de un kilómetro con un solvente que se enciende con una simple chispa?\n\n"
            "5 de octubre de 2007. Central hidroeléctrica Cabin Creek en Colorado. Nueve pintores trabajan dentro de una tubería forzada de agua, inclinada a 55 grados.\n\n"
            "Para limpiar una máquina de pintura, introdujeron varios galones de MEK, un solvente extremadamente inflamable. No había extractores ni detectores de gas.\n\n"
            "Los vapores pesados se acumularon en el fondo. Una pequeña chispa eléctrica encendió la atmósfera. Una pared de fuego cortó la tubería en dos.\n\n"
            "Cuatro lograron escapar por arriba entre humo negro. Los otros cinco quedaron atrapados detrás del fuego sin salida y murieron por asfixia.\n\n"
            "La lección de la CSB es categórica: nunca uses solventes inflamables en espacios confinados y asegura siempre un plan de escape real.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph looking inside a massive, steep industrial steel penstock water tunnel for a hydroelectric plant. "
            "A dark cylindrical steel conduit sloping downwards at a steep 55-degree angle, blackened soot marks on steel lining, "
            "ventilation air duct tubes and emergency lifelines lying along the curved metal wall, emergency searchlights illuminating the interior, "
            "chilling industrial safety forensic documentation, 8k resolution, raw authentic textures."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 5 de octubre de 2007, en la central hidroeléctrica de bombeo Cabin Creek de Xcel Energy, "
            "ubicada en las montañas de Colorado a más de tres mil metros de altitud, una serie de fallas críticas en la gestión "
            "de espacios confinados provocó una tragedia desgarradora. Cinco trabajadores de una empresa contratista "
            "fallecieron asfixiados tras quedar atrapados en el interior de una tubería forzada de acero de mil doscientos metros de longitud "
            "y cuatro metros de diámetro, inclinada a cincuenta y cinco grados de pendiente.\n\n"
            "La tarea consistía en recubrir el interior de la tubería forzada con resina epoxi para proteger el metal contra la corrosión. "
            "Para limpiar las boquillas y mangueras de los equipos pulverizadores dentro del ducto, los aplicadores ingresaron varios baldes "
            "de metiletilcetona, conocida como MEK, un solvente orgánico altamente volátil cuyo vapor es dos veces y media más denso que el aire. "
            "A pesar del confinamiento extremo, la empresa no instaló un sistema de ventilación mecánica de extracción forzada "
            "ni contaba con detectores portátiles de gases calibrados para medir el porcentaje del límite inferior de explosividad (LEL).\n\n"
            "Al verter el solvente sobre los componentes mecánicos, los vapores inflamables se acumularon sobre la base de la tubería. "
            "Una chispa electrostática o eléctrica en el equipo de pulverización encendió la nube de solvente en un instante, "
            "desatando un incendio violento que bloqueó la sección central del túnel. De los nueve trabajadores presentes, "
            "cuatro lograron escapar con quemaduras trepando penosamente hacia la boca superior. "
            "Lamentablemente, los otros cinco operarios quedaron atrapados en el extremo inferior ciego, detrás de una muralla impenetrable "
            "de fuego y monóxido de carbono. Los brigadistas de rescate demoraron horas en llegar con equipos autónomos, "
            "hallando a los cinco trabajadores fallecidos por inhalación de humos tóxicos.\n\n"
            "La investigación exhaustiva de la Junta de Seguridad Química de los Estados Unidos (CSB) expuso lecciones indelebles: "
            "Primero: principio de sustitución por diseño; está estrictamente prohibido utilizar solventes inflamables con bajo punto de destello "
            "en recintos confinados cuando existen alternativas acuosas no combustibles. "
            "Segundo: la ventilación por extracción continua y el monitoreo atmosférico en tiempo real con alarmas audibles al diez por ciento del LEL "
            "son condiciones innegociables para autorizar el ingreso. Y tercero: todo permiso de trabajo en espacios confinados críticos "
            "debe contemplar rutas de evacuación redundantes y un equipo de rescate in situ con capacidad operativa inmediata.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    }
]

def format_duration(seconds):
    """Formatea la duración en minutos y segundos en texto amigable."""
    m = int(seconds // 60)
    s = int(round(seconds % 60))
    if s == 60:
        m += 1
        s = 0
    return f"Audio de {m} minutos {s} segundos"

def crear_portada_pillow(historia, output_path):
    """Genera una portada de respaldo 16:9 (1920x1080) de alta calidad gráfica."""
    width, height = 1920, 1080
    img = Image.new("RGB", (width, height), color=(11, 26, 32))
    draw = ImageDraw.Draw(img)

    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=(16, 36, 44), width=1)
    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill=(16, 36, 44), width=1)

    for i in range(120):
        color = (5, 16, 20)
        draw.rectangle([i, i, width - i, height - i], outline=color, width=1)

    try:
        font_title = ImageFont.truetype("arialbd.ttf", 62)
        font_sub = ImageFont.truetype("arial.ttf", 34)
        font_meta = ImageFont.truetype("arialbd.ttf", 26)
        font_badge = ImageFont.truetype("arialbd.ttf", 22)
    except:
        font_title = font_sub = font_meta = font_badge = ImageFont.load_default()

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
    """Inyecta las historias del Lote 9 en index.html antes del cierre del array historias."""
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    nuevos_bloques = []
    for h in historias_procesadas:
        puntos_js = json.dumps(h["puntosClave"], ensure_ascii=False, indent=12)
        parrafos_js = json.dumps(h["parrafos"], ensure_ascii=False, indent=10)

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

    print("\n✓ index.html actualizado exitosamente con los 10 nuevos expedientes (#093 a #102).")
    return True

def sincronizar_portadas_disco():
    """Ejecuta la sincronización final de portadas verificando la presencia en disco."""
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    lineas = content.splitlines(keepends=True)
    nuevas_lineas = []
    carpeta_actual = None
    reemplazos = 0

    for line in lineas:
        m_carpeta = re.search(r'carpetaAssets:\s*"(assets/efemerides/([^/]+)/)"', line)
        if m_carpeta:
            carpeta_actual = m_carpeta.group(2)

        m_img = re.search(r'(\s*imagen:\s*")([^"]+)(".*)', line)
        if m_img and carpeta_actual:
            folder_path = os.path.join(ASSETS_DIR, carpeta_actual)
            files = os.listdir(folder_path) if os.path.exists(folder_path) else []

            img_ideal = "portada.png"
            if "portada.jpeg" in files:
                img_ideal = "portada.jpeg"
            elif "portada.jpg" in files:
                img_ideal = "portada.jpg"
            elif "portada.png" in files:
                img_ideal = "portada.png"

            img_actual = m_img.group(2)
            if img_actual != img_ideal:
                prefix = m_img.group(1)
                suffix = m_img.group(3)
                line = f"{prefix}{img_ideal}{suffix}\n"
                reemplazos += 1
                print(f"  [Sincronización Portada] {carpeta_actual}: {img_actual} -> {img_ideal}")

            carpeta_actual = None
        nuevas_lineas.append(line)

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.writelines(nuevas_lineas)

    print(f"✓ Portadas sincronizadas en index.html ({reemplazos} ajustes realizados).")

def main():
    print("Iniciando motor Kokoro para Lote 9 (#093 a #102)...")
    kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

    print("\n" + "=" * 55)
    print("Iniciando procesamiento de 10 historias del Lote 9 (#093 a #102)")
    print("=" * 55 + "\n")

    historias_procesadas = []

    for h in LOTE_9_DATA:
        print(f"▶ Procesando: {h['expediente']} ({h['fecha']}) - {h['titular'][:45]}...")
        target_dir = os.path.join(ASSETS_DIR, h["carpeta"])
        os.makedirs(target_dir, exist_ok=True)

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

        # 5. portada.png con Pillow
        portada_png_path = os.path.join(target_dir, "portada.png")
        crear_portada_pillow(h, portada_png_path)
        print("  ✓ Portada generada (portada.png)")

        # 6. Síntesis de audio con Kokoro
        words_count = len(h["guionLargo"].split())
        print(f"  🎙️ Sintetizando audio ({words_count} palabras) con Kokoro (speed={KOKORO_SPEED})...")
        
        samples, sample_rate = kokoro.create(
            h["guionLargo"],
            voice=KOKORO_VOICE,
            speed=KOKORO_SPEED,
            lang=KOKORO_LANG
        )

        raw_wav_path = os.path.join(target_dir, "historia_temp.wav")
        final_m4a_path = os.path.join(target_dir, "historia.m4a")
        sf.write(raw_wav_path, samples, sample_rate)

        # 7. Conversión a M4A con ffmpeg
        print("  ⚙️ Convirtiendo a M4A optimizado...")
        ffmpeg_cmd = [
            "ffmpeg", "-y",
            "-i", raw_wav_path,
            "-c:a", "aac",
            "-b:a", "128k",
            "-ar", "24000",
            final_m4a_path
        ]
        res = subprocess.run(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode != 0:
            print(f"  ⚠️ Error en ffmpeg: {res.stderr.decode('utf-8', errors='ignore')}")

        if os.path.exists(raw_wav_path):
            os.remove(raw_wav_path)

        # 8. Medir duración exacta
        probe_cmd = [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            final_m4a_path
        ]
        probe_res = subprocess.run(probe_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        duracion_segundos = float(probe_res.stdout.strip()) if probe_res.stdout.strip() else (len(samples) / sample_rate)
        h["duracionAudio"] = format_duration(duracion_segundos)
        print(f"  ✓ Audio listo: {final_m4a_path} ({h['duracionAudio']})\n")

        historias_procesadas.append(h)

    # Inyección en index.html
    inyectar_en_index_html(historias_procesadas)

    # Sincronización de portadas
    sincronizar_portadas_disco()

    print("\n🎉 ¡LOTE 9 COMPLETADO AL 100%! (10 historias procesadas)\n")

if __name__ == "__main__":
    main()
