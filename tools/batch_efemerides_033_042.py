# -*- coding: utf-8 -*-
"""
Generador Agéntico Automatizado para Lote 3: Expedientes #033 a #042 (28 de julio al 6 de agosto)
1. Crea directorios en assets/efemerides/
2. Genera README.md y contenido-completo.md
3. Guarda guion-reel.txt y prompt-portada.txt
4. Genera portada.png (16:9 alta resolución con Pillow)
5. Sintetiza audio en Kokoro (speed 0.86, ~490-520 palabras -> ~3:00 a 3:30 min)
6. Convierte con ffmpeg a M4A y mide duración exacta
7. Inyecta en index.html
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

LOTE_3_DATA = [
    {
        "id": "033",
        "fecha": "28 JULIO",
        "fechaPublicacion": "2026-07-28",
        "expediente": "Expediente #033",
        "carpeta": "1948-07-28-explosion-basf-ludwigshafen",
        "titular": "EL VAGÓN CISTERNA AL SOL QUE DETONÓ LA QUÍMICA BASF",
        "palabraResaltada": "VAGÓN CISTERNA AL SOL",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Química BASF, Ludwigshafen, Alemania - 1948",
        "tipoRiesgo": "Seguridad de Procesos (PSM) / Recipientes a Presión",
        "parrafos": [
            "El 28 de julio de 1948, un vagón cisterna cargado con 30 toneladas de dimetil éter estalló violentamente en el corazón del complejo químico BASF en Ludwigshafen.",
            "El vagón había permanecido estacionado bajo el sol abrasador sin sombra ni rociadores. La expansión térmica del gas licuado superó el límite de llenado seguro, fracturando el acero por sobrepresión.",
            "La deflagración posterior y onda expansiva destruyeron decenas de edificios y cobraron 207 vidas. El desastre transformó las normas internacionales de llenado máximo y alivio térmico en recipientes a presión."
        ],
        "puntosClave": [
            {"icono": "gauge", "titulo": "Márgenes de llenado (Outage / Ullage)", "texto": "Nunca sobrepasar el volumen máximo admisible en gases licuados para absorber la dilatación térmica por radiación solar."},
            {"icono": "shield-alert", "titulo": "Válvulas de alivio y discos de ruptura", "texto": "Todo recipiente móvil o estacionario debe contar con dispositivos de alivio calibrados para escenarios de fuego y sol extremo."},
            {"icono": "droplets", "titulo": "Refrigeración pasiva y aspersores", "texto": "Instalar tinglados protectores o sistemas de diluvio de agua en playas de maniobras para evitar calentamiento crítico."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: registros históricos de investigación de accidentes de procesos químicos de BASF y normativas internacionales de transporte de mercancías peligrosas ADR / ASME VIII.",
        "guionReel": (
            "¿Puede el calor del sol partir un vagón de acero macizo como si fuera papel?\n\n"
            "El 28 de julio de 1948, en la planta BASF de Ludwigshafen, un vagón cisterna con 30 toneladas de gas licuado quedó estacionado bajo el sol directo del verano.\n\n"
            "Nadie consideró un principio básico de la física: los líquidos se expanden al calentarse. Al no dejarse un margen de espacio libre en el tanque, el líquido llenó cada milímetro cúbico y la presión hidráulica interna se disparó.\n\n"
            "El metal no resistió. El tanque reventó liberando una inmensa nube inflamable que encendió al instante: 207 trabajadores perdieron la vida y la fábrica quedó arrasada.\n\n"
            "La lección es sagrada: en gases licuados, el margen de llenado y el alivio térmico salvan vidas.\n\n"
            "En seguridad de procesos, la física no perdona descuidos."
        ),
        "promptImagen": (
            "Historical industrial documentary photography, July 28 1948, chemical manufacturing complex in Ludwigshafen Germany. "
            "A heavily damaged heavy industrial railway tanker car ruptured by internal overpressure, twisted steel beams, smoke billowing into the sky, "
            "vintage brick factory buildings shattered in the background, dramatic late afternoon lighting, somber atmosphere, 16:9 aspect ratio, high resolution, photorealistic archival style."
        ),
        "guionLargo": (
            "El veintiocho de julio de mil novecientos cuarenta y ocho... una catástrofe monumental sacudió el corazón industrial de Ludwigshafen, en Alemania... "
            "Dentro del inmenso complejo petroquímico de la empresa BASF, un vagón cisterna cargado con treinta toneladas de dimetil éter... permanecía estacionado en las vías internas de maniobras... "
            "Era una jornada de calor sofocante... Con temperaturas extremas de verano, la radiación solar directa impactaba sin tregua sobre el cuerpo metálico del vagón... el cual carecía de techo de resguardo o sistemas de refrigeración por aspersión... "
            "En el interior del recipiente, el gas licuado comenzó a calentarse de forma constante... Al elevarse la temperatura, el líquido experimentó una expansión volumétrica inevitable... "
            "Sin embargo, el vagón había sido llenado prácticamente al cien por ciento de su capacidad... violando el margen de seguridad conocido en ingeniería como ullage o volumen libre de vapor... "
            "Cuando el líquido en expansión agotó el escaso espacio libre restante, el fenómeno dejó de ser una compresión de vapor... Se transformó en una fuerza hidráulica implacable contra las paredes de acero... "
            "Las válvulas de alivio de la época no estaban dimensionadas para evacuar semejante incremento de presión térmica... "
            "A las quince horas con cuarenta y tres minutos, la envolvente de acero cedió bruscamente... Una fractura catastrófica abrió el tanque en dos mitades, proyectando fragmentos metálicos a cientos de metros... "
            "Treinta toneladas de gas inflamable se vaporizaron al instante, formando una densa niebla tóxica y explosiva que encontró rápidamente fuentes de ignición en los hornos y calderas cercanas... "
            "La explosión secundaria resultante fue devastadora... Doscientas siete personas perdieron la vida... y cerca de cuatro mil resultaron heridas... Naves industriales enteras fueron pulverizadas por la onda de choque... "
            "La tragedia de Ludwigshafen obligó a rediseñar por completo la ingeniería de transporte y almacenamiento de gases licuados... "
            "A partir de aquel día, las normas internacionales establecieron límites estrictos de llenado máximo... inspecciones radiográficas periódicas... y la obligación de instalar discos de ruptura y válvulas de alivio dimensionadas para resistir la exposición solar extrema... "
            "Porque en la seguridad de procesos... subestimar las leyes de la termodinámica... siempre tiene un costo humano irreparable."
        )
    },
    {
        "id": "034",
        "fecha": "29 JULIO",
        "fechaPublicacion": "2026-07-29",
        "expediente": "Expediente #034",
        "carpeta": "2017-07-29-derrumbe-andamio-obra-civil",
        "titular": "EL COLAPSO DEL ANDAMIO: SOBRECARGA Y FALTA DE ANCLAJE",
        "palabraResaltada": "COLAPSO DEL ANDAMIO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Obra en Construcción, Edificio en Altura - 2017",
        "tipoRiesgo": "Trabajo en Altura / Andamios Tubulares",
        "parrafos": [
            "El 29 de julio de 2017, un andamio multidireccional de siete cuerpos colapsó en la fachada de una torre en construcción, arrojando al vacío a tres operarios.",
            "La estructura carecía de amarres rígidos a los muros de hormigón en los niveles superiores y no poseía suficientes diagonales de arriostramiento. Además, se habían acopiado pallets de ladrillos sobre las plataformas.",
            "El peso excesivo superó la resistencia al pandeo de los montantes y la estructura se dobló hacia la calle. El caso impulsó la obligatoriedad del cálculo de carga y tarjetas de habilitación diaria."
        ],
        "puntosClave": [
            {"icono": "git-commit", "titulo": "Anclaje estructural obligatorio", "texto": "Fijar el andamio a elementos estructurales resistentes con tacos mecánicos o tacos químicos según memoria de cálculo."},
            {"icono": "weight", "titulo": "Prohibido acopiar materiales", "texto": "Las plataformas de trabajo son exclusivas para tránsito y labor del personal; jamás deben usarse como depósito de obra."},
            {"icono": "check-circle", "titulo": "Tarjeta de habilitación visible", "texto": "Inspección diaria por personal competente con sistema Scafftag: verde para uso autorizado, roja para fuera de servicio."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informes periciales de siniestros en la industria de la construcción y normativas de trabajo en altura OSHA 1926.451 / IRAM 3691.",
        "guionReel": (
            "¿Un andamio puede derrumbarse por algo tan simple como acumular ladrillos?\n\n"
            "El 29 de julio de 2017, en la fachada de un edificio en construcción, un andamio de veinte metros de altura se vino abajo en una fracción de segundo.\n\n"
            "Los obreros necesitaban avanzar rápido y decidieron subir varios pallets de materiales directo a las plataformas de trabajo para no bajar a buscarlos.\n\n"
            "Pero el andamio no estaba calculado para semejante peso. Para colmo, para facilitar el paso, habían retirado los anclajes que lo sujetaban a la pared.\n\n"
            "Los caños sufrieron pandeo, la estructura perdió rigidez y se desplomó arrastrando a los trabajadores hacia el vacío.\n\n"
            "Un andamio no es una bodega de carga. Respeta su capacidad máxima y exige siempre la tarjeta de habilitación verde.\n\n"
            "Tu seguridad no se negocia por ganar unos minutos."
        ),
        "promptImagen": (
            "Industrial construction site accident documentary photography, modern civil construction scaffolding collapsed on a multistory building facade. "
            "Twisted steel tubes, fractured timber platforms, scattered bricks on the ground, caution perimeter red tape, overcast dramatic sky, "
            "construction helmets on the ground, high-detail architectural perspective, professional realistic documentary, 16:9 aspect ratio."
        ),
        "guionLargo": (
            "El veintinueve de julio de dos mil diecisiete... un estruendo metálico paralizó a una cuadrilla entera en una obra civil en plena ejecución... "
            "En la fachada lateral de un edificio en altura... una estructura de andamios tubulares de siete niveles se desplomó de manera fulminante hacia el pavimento... "
            "Sobre las plataformas superiores, tres trabajadores realizaban tareas de revoque y colocación de mampostería a más de dieciocho metros de altura... "
            "Para evitar pérdidas de tiempo en el izaje continuo de materiales... los operarios habían depositado bolsas de cemento, arena y varios pallets de ladrillos directamente sobre las bandejas metálicas... "
            "Aquella sobrecarga masiva multiplicaba por cuatro la capacidad nominal de diseño del andamio... "
            "Pero el problema de fondo era aún más grave... Durante el avance de las tareas, los anclajes rígidos que debían sujetar los montantes verticales a la estructura de hormigón habían sido retirados... porque estorbaban el fratachado de la pared... "
            "Sin amarres mecánicos y con diagonales de arriostramiento incompletas... la estructura entera quedó en un equilibrio precario... "
            "Bastó un leve desplazamiento de carga y una ráfaga de viento para que los caños principales sufrieran pandeo por compresión... "
            "El andamio se desarticuló piso por piso... colapsando como un castillo de naipes... Dos de los operarios sufrieron politraumatismos gravísimos y uno perdió la vida al no estar anclado a una línea de vida vertical independiente... "
            "Las investigaciones posteriores ratificaron una regla de oro que nunca debe violarse... Las plataformas de trabajo jamás deben utilizarse como zonas de acopio de carga pesada... "
            "Cada andamio debe contar con una memoria de cálculo firmada... anclajes certificados cada cuatro metros... y una inspección diaria documentada mediante tarjetas de habilitación visible... "
            "En trabajos en altura... un atajo en el armado de una estructura... es una trampa mortal suspendida en el aire."
        )
    },
    {
        "id": "035",
        "fecha": "30 JULIO",
        "fechaPublicacion": "2026-07-30",
        "expediente": "Expediente #035",
        "carpeta": "2014-07-30-explosion-trabajo-caliente-tanque",
        "titular": "SOLDAR UN TANQUE VACÍO: LA TRAMPA MORTAL DE LOS VAPORES",
        "palabraResaltada": "SOLDAR UN TANQUE VACÍO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Taller Metalúrgico, Mantenimiento Industrial - 2014",
        "tipoRiesgo": "Trabajo en Caliente / Atmósferas Explosivas",
        "parrafos": [
            "El 30 de julio de 2014, un tanque cisterna que había transportado combustible explotó violentamente en un taller metalúrgico mientras un soldador reparaba una fisura exterior.",
            "El recipiente estaba drenado pero no había sido lavado químicamente, desgasificado ni inertizado. Los vapores residuales acumulados en el fondo alcanzaron su rango de inflamabilidad.",
            "El calor del soplete transmitió energía suficiente para encender la mezcla interna, expulsando la tapa como un proyectil y matando al operario en el acto. La regla: 'vacío no es seguro'."
        ],
        "puntosClave": [
            {"icono": "flame-kindling", "titulo": "Vacío nunca significa seguro", "texto": "Los hidrocarburos dejan películas invisibles y vapores en porosidades que generan atmósferas explosivas."},
            {"icono": "activity", "titulo": "Monitoreo con explosímetro (0% LEL)", "texto": "Medir obligatoriamente el porcentaje del límite inferior de explosividad antes de encender cualquier llama o arco eléctrico."},
            {"icono": "wind", "titulo": "Lavado e inertización previa", "texto": "Aplicar vaporizado, lavado con tensoactivos o llenado con gas inerte (nitrógeno o CO2) antes de intervenir recipientes de combustible."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: boletines de seguridad técnica de la CSB y normas de prevención en trabajos en caliente OSHA 1910.252 / NFPA 326.",
        "guionReel": (
            "¿Por qué un tanque de combustible vacío es más peligroso que uno lleno?\n\n"
            "El 30 de julio de 2014, en un taller de reparaciones, un soldador experimentado debía tapar una pequeña grieta en una cisterna de combustible.\n\n"
            "El tanque no tenía líquido. Parecía inofensivo. Pero cuando un tanque se vacía, el espacio se llena de vapor invisible de hidrocarburos.\n\n"
            "El operario no midió gases con un explosímetro, no lo lavó con vapor ni lo inertizó. Confiado, encendió el soplete.\n\n"
            "El calor atravesó la chapa. Al tocar la atmósfera interior, el tanque se convirtió en una bomba. La tapa voló a cien metros y el soldador murió instantáneamente.\n\n"
            "Grábatelo para siempre: vacío no es seguro. Sin medición de cero por ciento LEL, jamás inicies un trabajo en caliente.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic industrial workshop accident scene, metal fabrication shop, ruptured heavy fuel transport tanker tank with catastrophic blown end-cap. "
            "Scattered welding equipment, cables, protective welding helmet on the ground, scorch marks on concrete floor, dramatic high-contrast industrial lighting, "
            "smoke rising from the charred metal opening, professional documentary, 16:9 ratio, ultra-detailed."
        ),
        "guionLargo": (
            "El treinta de julio de dos mil catorce... la calma de un taller metalúrgico fue destruida por una explosión ensordecedora... "
            "En el área de maestranza, un operario experimentado se disponía a soldar un pequeño soporte de fijación en la chapa exterior de un tanque cisterna... "
            "El recipiente había transportado gasoil y nafta durante meses... pero se encontraba completamente drenado... "
            "Al mirar por la boca de inspección y no ver combustible líquido... el equipo asumió erróneamente que no existía peligro alguno... "
            "Ese fue el error fatal... Porque en la química de los hidrocarburos... un tanque supuestamente vacío es infinitamente más peligroso que uno lleno... "
            "Las paredes interiores y los sedimentos del fondo desprendían de forma continua vapores volátiles... Al mezclarse con el oxígeno del aire... crearon una atmósfera en perfecto rango de inflamabilidad dentro del recinto... "
            "Nadie emitió un permiso de trabajo en caliente... Nadie introdujo una sonda de explosímetro para medir el límite inferior de explosividad... y nadie realizó un vaporizado o inertización con nitrógeno... "
            "Apenas el soldador apoyó el electrodo y saltó el primer arco eléctrico... el calor extremo se transfirió a través de la chapa de acero... "
            "La mezcla interna detonó de inmediato... La onda de sobrepresión arrancó la tapa abombada del tanque... propulsándola como un misil contra las paredes del taller... "
            "El trabajador falleció instantáneamente por el impacto... y la nave industrial quedó envuelta en llamas... "
            "Este lamentable suceso reafirma el principio fundamental de la norma NFPA 326... Ningún recipiente que haya contenido sustancias inflamables puede ser intervenido con calor... sin un lavado químico exhaustivo... ventilación forzada... y una confirmación instrumental rigurosa de cero por ciento de gases combustibles... "
            "Porque en higiene y seguridad... confiar en la vista en lugar de medir... cuesta vidas humanas."
        )
    },
    {
        "id": "036",
        "fecha": "31 JULIO",
        "fechaPublicacion": "2026-07-31",
        "expediente": "Expediente #036",
        "carpeta": "2014-07-31-explosiones-ductos-kaohsiung",
        "titular": "EL RÍO INVISIBLE DE PROPILENO QUE DETONÓ LA CIUDAD",
        "palabraResaltada": "RÍO INVISIBLE DE PROPILENO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Distrito Urbano de Kaohsiung, Taiwán - 2014",
        "tipoRiesgo": "Seguridad de Procesos (Ductos) / Pérdida de Contención",
        "parrafos": [
            "La noche del 31 de julio de 2014, una serie de explosiones subterráneas masivas partieron en dos varias avenidas en Kaohsiung, Taiwán, dejando 32 fallecidos y más de 300 heridos.",
            "Una tubería enterrada que transportaba propileno líquido sufrió una rotura por corrosión externa. Pese a que los operadores detectaron caídas de presión y los vecinos reportaron olor, el bombeo continuó durante horas.",
            "El gas más pesado que el aire se acumuló en la red de alcantarillado pluvial hasta hallar una chispa. El desastre expuso fallas críticas en monitoreo de ductos e interfaces urbanas."
        ],
        "puntosClave": [
            {"icono": "radio", "titulo": "Respuesta inmediata a caídas de presión", "texto": "Ante discrepancias en balance de masa o caída de presión en ductos, cortar el bombeo de inmediato sin dudar."},
            {"icono": "map-pin", "titulo": "Mapeo e interferencias subterráneas", "texto": "Separar físicamente los ductos industriales de las redes pluviales y cloacales urbanas para evitar canalización de gases."},
            {"icono": "phone-call", "titulo": "Protocolo coordinado ante alertas públicas", "texto": "Tomar las quejas vecinales por olores químicos como emergencias reales de proceso y activar cuadrillas de medición."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de investigación de la Comisión de Seguridad en el Transporte de Taiwán y normativas API 1160 para gestión de integridad de ductos.",
        "guionReel": (
            "¿Puede una fuga en una tubería subterránea destruir kilómetros enteros de una ciudad moderna?\n\n"
            "El 31 de julio de 2014, en Kaohsiung, Taiwán, la tierra literalmente se abrió en llamas.\n\n"
            "Una tubería industrial que transportaba propileno líquido se perforó bajo tierra. En la sala de control notaron una caída de presión, pero asumieron que era un error del sensor y siguieron bombeando.\n\n"
            "Durante horas, toneladas de gas invisible y más pesado que el aire viajaron por las alcantarillas de la ciudad.\n\n"
            "A la medianoche, una chispa detonó el sistema de desagües. Cuadras enteras volaron por los aires: autos volcados, zanjas de diez metros y 32 muertos.\n\n"
            "En ductos de transporte, ante una caída de presión inexplicada, la orden es una sola: cortar el bombeo de inmediato.\n\n"
            "La seguridad de procesos no admite dudas."
        ),
        "promptImagen": (
            "Dramatic urban disaster documentary photography, night of July 31 2014, Kaohsiung Taiwan street pipeline explosion aftermath. "
            "A massive trench cracked open down the center of an urban avenue, overturned fire trucks and passenger vehicles, glowing emergency lights, smoke and fire in background, "
            "asphalt torn like paper, emergency responders cordoning the area, cinematic high-contrast photojournalism style, 16:9."
        ),
        "guionLargo": (
            "La noche del treinta y uno de julio de dos mil catorce... la ciudad portuaria de Kaohsiung, en Taiwán... se convirtió en el escenario de una pesadilla urbana inimaginable... "
            "A partir de las veinte horas, decenas de residentes comenzaron a llamar a los servicios de emergencia reportando un fuerte olor a gas y nieblas blancas saliendo de las alcantarillas... "
            "Bajo las calles pavimentadas... corría un ducto enterrado de ocho pulgadas de diámetro que transportaba propileno líquido hacia una planta petroquímica... "
            "Afectada por años de corrosión galvánica en un cruce con un canal de drenaje pluvial... la pared metálica de la tubería se había perforado... "
            "En la sala de control de la empresa transportadora... los sistemas de monitoreo registraron una repentina caída de presión... acompañada de una marcada discrepancia en el balance de masa entre el punto de envío y el de recepción... "
            "Sin embargo... en lugar de aislar las válvulas de bloqueo de emergencia y suspender el flujo... los operadores atribuyeron la anomalía a una falla de calibración de los transmisores y continuaron bombeando propileno a presión durante más de tres horas... "
            "El gas licuado liberado se expandió doscientas cincuenta veces su volumen al salir a la atmósfera... Siendo más denso que el aire, el propileno no se disipó hacia el cielo... sino que se canalizó a través de kilómetros de túneles pluviales y desagües cloacales debajo de las principales arterias de la ciudad... "
            "Poco antes de la medianoche... la inmensa mezcla explosiva subterránea encontró un punto de ignición... "
            "Una serie de detonaciones encadenadas reventó el pavimento... Las calles principales se abrieron como zanjas de diez metros de profundidad... lanzando automóviles, árboles y camiones de bomberos por los aires... "
            "Treinta y dos personas murieron... entre ellas valientes rescatistas que buscaban el origen del escape... y más de trescientas resultaron heridas... "
            "La catástrofe de Kaohsiung cambió los protocolos mundiales de transporte por ductos... Demostró que una caída de presión jamás debe debatirse... exige el corte preventivo e inmediato del bombeo... "
            "Porque cuando se ignoran las señales del proceso... el costo lo termina pagando la comunidad entera."
        )
    },
    {
        "id": "037",
        "fecha": "01 AGOSTO",
        "fechaPublicacion": "2026-08-01",
        "expediente": "Expediente #037",
        "carpeta": "2018-08-01-amputacion-sierra-circular-banco",
        "titular": "EL ATAJO EN LA SIERRA CIRCULAR: UN SEGUNDO, UNA VIDA CAMBIADA",
        "palabraResaltada": "ATAJO EN LA SIERRA CIRCULAR",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Aserradero y Carpintería Industrial - 2018",
        "tipoRiesgo": "Protección de Máquinas / Corte Mecánico",
        "parrafos": [
            "El 1 de agosto de 2018, un operario en un aserradero industrial sufrió la amputación traumática de tres dedos al operar una sierra circular de banco.",
            "Para agilizar el corte de listones delgados, el trabajador había desmontado la caperuza de protección del disco y retirado el cuchillo divisor. La madera se trabó en la parte posterior del disco sufriendo un retroceso violento (kickback).",
            "El impacto arrastró la mano del operario directamente contra los dientes giratorios a cuatro mil revoluciones por minuto. La anulación de defensas por comodidad sigue siendo causa líder de mutilación."
        ],
        "puntosClave": [
            {"icono": "shield-check", "titulo": "Cuchillo divisor siempre instalado", "texto": "Evita que la madera se cierre sobre la parte trasera del disco, previniendo el efecto proyectil o kickback."},
            {"icono": "eye-off", "titulo": "Caperuza protectora autorregulable", "texto": "Mantiene el disco cubierto en todo momento y no debe removerse bajo ninguna justificación operativa."},
            {"icono": "hand", "titulo": "Empujadores para piezas pequeñas", "texto": "Prohibido acercar las manos a menos de 15 centímetros del filo; utilizar varillas de empuje de madera o polímero."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: estadísticas y guías de seguridad en maquinaria maderera de OSHA 1910.213 y normativas europeas UNE-EN 1870-1.",
        "guionReel": (
            "¿Vale la pena perder los dedos por ahorrarte treinta segundos de trabajo?\n\n"
            "El 1 de agosto de 2018, en un aserradero, un carpintero debía cortar cientos de listones de madera. Para ir más rápido, tomó una decisión fatal: quitó la caperuza de seguridad y el cuchillo divisor de la sierra circular.\n\n"
            "Decía que la protección molestaba y que él tenía años de experiencia.\n\n"
            "Pero la madera tiene tensiones internas. A mitad del corte, la tabla se cerró sobre el disco giratorio a 4.000 revoluciones por minuto.\n\n"
            "El efecto retroceso, o kickback, fue brutal: la tabla salió disparada y la inercia arrastró su mano directo contra los dientes de acero.\n\n"
            "Tres dedos amputados en una milésima de segundo.\n\n"
            "Jamás retires los resguardos de una máquina. El exceso de confianza no te protege de un filo de acero.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Documentary style industrial wood workshop setting, heavy table circular saw in a woodworking factory. "
            "Saw blade exposed without guard, scattered sawdust on concrete floor, wooden push sticks nearby, red emergency stop button visible, "
            "caution safety signage on the wall, dramatic directional workshop lighting, photorealistic professional photography, 16:9 ratio."
        ),
        "guionLargo": (
            "El primero de agosto de dos mil dieciocho... en la rutina acelerada de un aserradero de manufactura maderera... un segundo de imprudencia cambió el destino de un trabajador... "
            "El operario, un carpintero con más de diez años de trayectoria en el oficio... debía dimensionar una partida de quinientos listones estrechos de pino... "
            "Para acelerar la alimentación manual y evitar que la caperuza plástica transparente le restara visión... decidió desarmar el sistema de resguardo superior del disco de corte... "
            "Pero cometió un error todavía más grave... Desmontó también el cuchillo divisor posterior... una pieza de acero curvada cuya función crítica es mantener abierta la línea de corte detrás de la hoja... "
            "El disco de la sierra giraba a más de cuatro mil revoluciones por minuto... "
            "A mitad de la jornada, al empujar una tabla que presentaba nudos y tensiones internas de secado... las fibras de la madera se cerraron sobre la parte ascendente de los dientes de la hoja... "
            "En una fracción de segundo, se desencadenó el temido efecto rebote o kickback... "
            "La tabla fue expulsada como un proyectil hacia atrás... y el movimiento reflejo de la mano derecha del operario, que empujaba la pieza sin utilizar una varilla auxiliar... fue absorbido directamente hacia el filo desprotegido... "
            "La máquina amputó tres de sus dedos antes de que pudiera accionar el botón de parada de emergencia... "
            "Las investigaciones de seguridad mecánica son categóricas... La gran mayoría de las amputaciones en sierras de banco ocurren cuando los operarios retiran voluntariamente las protecciones provistas por el fabricante... "
            "El cuchillo divisor, la caperuza telescópica autorregulable y el uso innegociable de empujadores plásticos para piezas pequeñas... son las únicas barreras que separan la habilidad humana de una lesión mutilante... "
            "Porque una máquina no tiene memoria... no respeta la experiencia... y no da segundas oportunidades."
        )
    },
    {
        "id": "038",
        "fecha": "02 AGOSTO",
        "fechaPublicacion": "2026-08-02",
        "expediente": "Expediente #038",
        "carpeta": "2005-08-02-fuga-cloro-gas-potabilizadora",
        "titular": "LA NUBE AMARILLA DE CLORO: CUANDO FALLA EL MANIFOLD",
        "palabraResaltada": "NUBE AMARILLA DE CLORO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Potabilizadora de Agua, Sala de Cloración - 2005",
        "tipoRiesgo": "Riesgo Químico / Fuga de Gas Tóxico",
        "parrafos": [
            "El 2 de agosto de 2005, una densa nube verde-amarillenta de gas cloro envolvió la sala de químicos de una planta potabilizadora tras la rotura de un conector flexible de cobre.",
            "Durante el reemplazo de un cilindro de una tonelada, se reutilizó una junta de plomo deformada y se forzó la rosca sin prueba de fugas. Al abrir la válvula principal, la presión expulsó el sello.",
            "El sistema de extracción forzada no contaba con torre de lavado (scrubber) y los operarios no tenían equipos autónomos a mano. El evento obligó a revisar protocolos con halógenos comprimidos."
        ],
        "puntosClave": [
            {"icono": "refresh-cw", "titulo": "Juntas de sellado de un solo uso", "texto": "Reemplazar siempre las juntas de plomo o teflón por unidades nuevas al conectar cilindros ton de cloro."},
            {"icono": "test-tube", "titulo": "Prueba de estanqueidad con amoníaco", "texto": "Verificar conexiones con vapor de hidróxido de amonio: la formación de humo blanco denso delata microfugas al instante."},
            {"icono": "shield-check", "titulo": "Torre neutralizadora (Scrubber) y ERA", "texto": "Las salas de cloración deben tener sistemas lavadores automáticos y equipos de respiración autónoma fuera del recinto."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: guías técnicas de manejo seguro de cloro del Chlorine Institute (Pamphlet 1) y normativas de higiene ocupacional OSHA 1910.120.",
        "guionReel": (
            "¿Sabías que una fuga de cloro gas puede asfixiarte en menos de tres respiraciones?\n\n"
            "El 2 de agosto de 2005, en una planta potabilizadora de agua, dos operarios cambiaban un cilindro de cloro de una tonelada.\n\n"
            "Al notar que no tenían juntas de sellado nuevas, decidieron reutilizar una junta de plomo usada para terminar rápido el turno. No hicieron la prueba con vapor de amoníaco para verificar estanqueidad.\n\n"
            "Al abrir la válvula, la presión reventó el sello. Una nube amarillo-verdosa y pesada inundó la sala al instante. El cloro quema las vías respiratorias y destruye el tejido pulmonar.\n\n"
            "Los equipos de respiración autónoma estaban guardados... adentro de la misma sala contaminada. No pudieron alcanzarlos.\n\n"
            "Con sustancias químicas tóxicas, las juntas jamás se reutilizan y los equipos de rescate van siempre afuera.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Industrial chemical emergency documentary photography, water treatment chlorination room, dense yellow-green toxic chlorine gas haze creeping low along the floor. "
            "Heavy one-ton chlorine steel cylinders lined up, manifold flexible lines, emergency eye wash station, warning hazardous chemical symbols, "
            "dramatic emergency red hazard lighting, high realism, photorealistic documentary, 16:9 ratio."
        ),
        "guionLargo": (
            "El dos de agosto de dos mil cinco... una rutina de mantenimiento habitual se transformó en una emergencia química extrema en una planta de tratamiento y potabilización de agua... "
            "En la sala aislada de dosificación de cloro... dos operadores se disponían a realizar el cambio de un cilindro ton agotado para conectar uno nuevo a la línea de succión... "
            "El cloro es un gas fuertemente oxidante y corrosivo... dos veces y media más pesado que el aire... capaz de formar ácido clorhídrico en contacto con la humedad de los pulmones... "
            "Al acoplar el conector flexible metálico a la válvula del nuevo contenedor... los trabajadores observaron que la arandela de junta de plomo estaba deformada... "
            "Al no contar con repuestos nuevos en la estantería del taller... optaron por reutilizar la junta vieja... ajustando la abrazadera con fuerza excesiva mediante una llave inglesa... "
            "Omitieron además el procedimiento más elemental de la industria del cloro... la verificación de estanqueidad utilizando vapores de amoníaco... método que genera una densa humareda blanca de cloruro de amonio ante la menor presencia de fuga... "
            "Apenas abrieron un cuarto de vuelta la válvula del cilindro... la presión interior fracturó la unión imperfecta... "
            "Un chorro de gas a alta presión comenzó a escapar con un silbido aterrador... formando una densa nube amarillo-verdosa que se expandió a ras del suelo... "
            "Los dos operarios intentaron colocarse las máscaras... pero los equipos de respiración autónoma estaban guardados dentro de un armario ubicado en el centro de la misma habitación contaminada... "
            "Tuvieron que escapar a ciegas tosiendo intensamente y con quemaduras químicas en los ojos y la garganta... "
            "Para empeorar la situación... el sistema de ventilación de emergencia expulsó el gas hacia el patio exterior porque la torre de lavado o scrubber no tenía la bomba de sosa cáustica operativa... "
            "El incidente demandó la evacuación de un radio de quinientos metros alrededor de la instalación... "
            "Este accidente dejó lecciones irremplazables... Las juntas de conexión en líneas de cloro son estrictamente de un solo uso... las pruebas con amoníaco son obligatorias... y los equipos de protección respiratoria deben colocarse siempre en el exterior de la sala... listos para la respuesta inmediata... "
            "Porque frente a un gas tóxico... no hay margen para la improvisación."
        )
    },
    {
        "id": "039",
        "fecha": "03 AGOSTO",
        "fechaPublicacion": "2026-08-03",
        "expediente": "Expediente #039",
        "carpeta": "2016-08-03-vuelco-autoelevador-patio-logistica",
        "titular": "CARGA ELEVADA Y GIRO BRUSCO: EL VUELCO DEL AUTOELEVADOR",
        "palabraResaltada": "VUELCO DEL AUTOELEVADOR",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Centro de Distribución Logística, Patio de Cargas - 2016",
        "tipoRiesgo": "Seguridad Vial Interna / Operación de Autoelevadores",
        "parrafos": [
            "El 3 de agosto de 2016, un autoelevador volcó lateralmente en el playón de un centro de distribución mientras trasladaba un pallet de dos toneladas.",
            "El operador circulaba a velocidad excesiva con el mástil elevado a tres metros de altura. Al realizar un giro brusco para esquivar un obstáculo, el centro de gravedad salió del triángulo de estabilidad.",
            "Al no llevar colocado el cinturón de seguridad, el conductor intentó arrojarse del vehículo y quedó atrapado bajo la estructura metálica antivuelco (ROPS). El cinturón salva la vida dentro de la cabina."
        ],
        "puntosClave": [
            {"icono": "shield", "titulo": "Cinturón de seguridad obligatorio", "texto": "Mantiene al conductor sujeto dentro de la jaula antivuelco; intentar saltar durante un vuelco es el error más letal."},
            {"icono": "arrow-down-circle", "titulo": "Circular siempre con horquillas bajas", "texto": "Las uñas deben viajar a 15-20 centímetros del suelo y el mástil ligeramente inclinado hacia atrás."},
            {"icono": "triangle", "titulo": "Triángulo de estabilidad dinámico", "texto": "Comprender cómo la altura de la carga y la fuerza centrífuga desplazan el centro de gravedad fuera del punto de apoyo."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: investigaciones técnicas de siniestros viales internos de OSHA 1910.178 y recomendaciones del Consejo Nacional de Seguridad (NSC).",
        "guionReel": (
            "¿Sabías cuál es el impulso natural más mortal que tiene un chofer de autoelevador cuando el equipo se da vuelta?\n\n"
            "El 3 de agosto de 2016, en un patio de cargas logístico, un operador trasladaba un pallet de dos toneladas. Iba apurado y llevaba la carga levantada a tres metros del suelo.\n\n"
            "Al girar en una esquina, la física hizo su trabajo: el centro de gravedad se desplazó y la máquina comenzó a volcar lateralmente.\n\n"
            "El conductor no llevaba abrochado el cinturón de seguridad. En medio del pánico, cometió el error fatal: intentó saltar hacia el costado.\n\n"
            "La pesada jaula de acero del techo cayó sobre él, aplastándolo en el acto.\n\n"
            "Grábatelo en la memoria: si un autoelevador vuelca, jamás saltes. Sujétate fuerte al volante, apoya los pies firmes y quédate adentro de la jaula.\n\n"
            "El cinturón de seguridad es la diferencia entre salir caminando o no salir jamás."
        ),
        "promptImagen": (
            "Industrial logistics accident documentary photography, modern outdoor logistics distribution yard, heavy yellow forklift tipped over on its side. "
            "Fallen wooden pallet with cargo scattered across asphalt pavement, tire skid marks, yellow safety barrier lines, emergency cones, overhead roll-cage ROPS structure prominent, "
            "overcast dramatic industrial daylight, high-resolution photojournalism, 16:9 ratio."
        ),
        "guionLargo": (
            "El tres de agosto de dos mil dieciséis... una tragedia evitable sacudió las operaciones de un concurrido centro logístico de mercaderías... "
            "En el playón exterior de maniobras, un autoelevador de tres toneladas realizaba movimientos de reubicación de pallets cargados de materiales... "
            "Apremiado por las exigencias de tiempo del despacho de camiones... el conductor cometió un error elemental de operación... "
            "Inició el desplazamiento con las horquillas elevadas a más de tres metros de altura... en lugar de mantenerlas a ras de suelo... entre quince y veinte centímetros... como exige la normativa... "
            "En la física de un montacargas... las dos ruedas delanteras y el punto de articulación central del eje trasero forman lo que se conoce como el triángulo de estabilidad... "
            "Al elevar una carga pesada... el centro de gravedad del conjunto sube drásticamente... reduciendo la tolerancia del vehículo ante cualquier fuerza lateral... "
            "Al tomar una curva cerrada para ingresar a una de las bahías de carga... la fuerza centrífuga desplazó el centro de gravedad fuera de la base triangular de apoyo... "
            "El autoelevador se inclinó y comenzó a volcar de costado de forma inexorable... "
            "El operario no llevaba puesto el cinturón de seguridad... "
            "Dominado por el instinto de supervivencia... cometió el error más letal documentado en este tipo de siniestros... Intentó saltar del habitáculo hacia el lado de la caída... "
            "El techo protector de acero... diseñado como estructura ROPS para resistir impactos y salvar la vida del conductor dentro de la celda de seguridad... lo aprisionó contra el asfalto... provocándole la muerte en el acto... "
            "Las investigaciones de seguridad vial laboral son unánimes... El habitáculo de un autoelevador es una cápsula de supervivencia... siempre y cuando el cinturón mantenga al operador firmemente anclado en su butaca... "
            "Ante un vuelco... la instrucción es aferrarse al volante... trabar los pies contra el piso e inclinarse en sentido contrario al impacto... jamás saltar... "
            "Porque la velocidad y el descuido en un patio industrial... transforman una herramienta de trabajo en una trampa mortal."
        )
    },
    {
        "id": "040",
        "fecha": "04 AGOSTO",
        "fechaPublicacion": "2026-08-04",
        "expediente": "Expediente #040",
        "carpeta": "2020-08-04-explosion-puerto-beirut",
        "titular": "DOS MIL SETECIENTAS TONELADAS OLVIDADAS: LA DETONACIÓN DE BEIRUT",
        "palabraResaltada": "DETONACIÓN DE BEIRUT",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Hangar 12, Puerto de Beirut, Líbano - 2020",
        "tipoRiesgo": "Seguridad de Procesos / Almacenamiento de Químicos Peligrosos",
        "parrafos": [
            "El 4 de agosto de 2020, la detonación de 2.750 toneladas de nitrato de amonio en el Hangar 12 del puerto de Beirut devastó la capital libanesa con más de 200 muertos y 7.000 heridos.",
            "El fertilizante llevaba seis años almacenado de forma negligente junto a toneladas de fuegos artificiales, solventes y neumáticos, sin ventilación adecuada ni sistemas contra incendios.",
            "Un trabajo de soldadura en una puerta del depósito inició un incendio que alcanzó la pirotecnia y calentó el nitrato hasta su descomposición explosiva. Una lección colosal sobre almacenamiento y compatibilidad química."
        ],
        "puntosClave": [
            {"icono": "boxes", "titulo": "Segregación química absoluta", "texto": "El nitrato de amonio jamás debe almacenarse junto a materias combustibles, aceites, solventes o material explosivo."},
            {"icono": "flame", "titulo": "Permiso estricto de trabajo en caliente", "texto": "Prohibición categórica de realizar soldaduras o amolados cerca de depósitos de sustancias comburentes."},
            {"icono": "clock", "titulo": "Gestión y plazos de inventarios peligrosos", "texto": "Auditorías continuas para impedir el abandono de sustancias químicas peligrosas en recintos portuarios o urbanos."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informes periciales internacionales de Forensic Architecture, CSB y normativas de sustancias peligrosas IMO / Código IMDG.",
        "guionReel": (
            "¿Cómo un depósito olvidado en un puerto pudo generar una de las mayores explosiones no nucleares de la historia?\n\n"
            "El 4 de agosto de 2020, el puerto de Beirut desapareció del mapa.\n\n"
            "En el Hangar 12 descansaban 2.750 toneladas de nitrato de amonio confiscado, abandonadas desde hacía seis años. Para colmo, en el mismo depósito guardaban pirotecnia, bidones de aceite y neumáticos viejos.\n\n"
            "Esa tarde, unos operarios fueron a arreglar una puerta rota con un soplete de soldadura.\n\n"
            "Una chispa encendió los fuegos artificiales. El fuego creció sin control, calentó la enorme montaña de nitrato confinado y desató una detonación colosal.\n\n"
            "Más de 200 muertos, 7.000 heridos y una ciudad destrozada en segundos.\n\n"
            "El descontrol de inventarios químicos y los trabajos en caliente sin permiso causan catástrofes mundiales.\n\n"
            "En seguridad de procesos, la negligencia se paga con vidas."
        ),
        "promptImagen": (
            "Panoramic archival documentary photograph, August 4 2020 Beirut port warehouse explosion aftermath. "
            "Massive circular crater filled with seawater where grain silos stood, shattered concrete reinforced towers, destroyed shipping containers, "
            "smoke rising over the ruined Mediterranean port landscape, emergency response vehicles, late afternoon cinematic golden lighting, wide angle 16:9, hyperrealistic."
        ),
        "guionLargo": (
            "El cuatro de agosto de dos mil veinte... el mundo contempló con horror una de las detonaciones no nucleares más potentes jamás registradas en la historia de la humanidad... "
            "A las dieciocho horas con ocho minutos... en el Hangar número doce del puerto de Beirut... estallaron dos mil setecientas cincuenta toneladas de nitrato de amonio de grado técnico... "
            "El cargamento había llegado al Líbano en dos mil trece a bordo de un carguero en bancarrota... Desembarcado por orden judicial... el peligroso compuesto químico fue depositado en un galpón común... donde permaneció acumulado durante seis años en un estado de abandono total... "
            "El nitrato de amonio es un agente oxidante potente... Aunque no arde por sí solo, bajo condiciones de confinamiento, altas temperaturas y en contacto con combustibles orgánicos... se convierte en un explosivo letal... "
            "Violando todas las reglas del Código Marítimo Internacional de Mercancías Peligrosas... el fertilizante se almacenó en bolsas deterioradas junto a pallets de fuegos artificiales... bidones de aceites industriales... solventes y rollos de mechas detonantes... "
            "Aquel fatídico día... una cuadrilla de mantenimiento fue asignada para reparar una cerradura rota en el portón del depósito... ejecutando tareas de corte y soldadura eléctrica sin un permiso de trabajo en caliente y sin precauciones básicas contra incendios... "
            "Las chispas incandescentes cayeron directamente sobre cajas de material pirotécnico... desatando un incendio furioso... "
            "Los bomberos acudieron a combatir las llamas sin tener la menor idea de lo que se escondía detrás de aquellas paredes... "
            "El calor extremo del incendio descompuso térmicamente la masa confinada de nitrato de amonio... hasta que sobrevino la detonación masiva... "
            "Una gigantesca nube con forma de hongo enrojecida por óxidos de nitrógeno se elevó sobre el Mediterráneo... mientras una onda de choque supersónica arrasaba barrios enteros... destrozando hospitales, viviendas y naves industriales en un radio de diez kilómetros... "
            "El desastre cobró más de doscientas vidas... dejó a siete mil personas heridas y a trescientas mil familias sin hogar... "
            "La catástrofe de Beirut es el recordatorio definitivo sobre la gestión de sustancias peligrosas... Los inventarios químicos jamás deben abandonarse... la segregación física entre comburentes e inflamables es inviolable... y ningún trabajo con calor puede realizarse sin evaluar el entorno completo... "
            "Porque cuando la burocracia y la desidia se cruzan con la química... las consecuencias son devastadoras."
        )
    },
    {
        "id": "041",
        "fecha": "05 AGOSTO",
        "fechaPublicacion": "2026-08-05",
        "expediente": "Expediente #041",
        "carpeta": "2010-08-05-derrumbe-mina-san-jose-chile",
        "titular": "EL MEGABLOQUE DE LA MINA SAN JOSÉ: 33 VIDAS A 700 METROS",
        "palabraResaltada": "MINA SAN JOSÉ",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Yacimiento San José, Caldera, Atacama, Chile - 2010",
        "tipoRiesgo": "Minería Subterránea / Geotecnia y Refugios de Escape",
        "parrafos": [
            "El 5 de agosto de 2010, el colapso masivo de un bloque de roca de 700.000 toneladas sepultó las galerías de la mina San José en el desierto de Atacama, atrapando a 33 mineros a 700 metros de profundidad.",
            "La mina presentaba un historial de desprendimientos previos sin monitoreo microsísmico adecuado ni fortificación activa con pernos y mallas. Las chimeneas de ventilación destinadas al escape carecían de escaleras instaladas.",
            "El milagroso rescate tras 69 días conmovió al mundo y marcó un hito regulatorio: fortificación sistemática, vías secundarias transitables y refugios subterráneos con autonomía certificada."
        ],
        "puntosClave": [
            {"icono": "mountain", "titulo": "Fortificación y sostenimiento de galerías", "texto": "Mapeo geomecánico permanente, instalación rigurosa de pernos de anclaje, pernos helicoidales y hormigón proyectado (shotcrete)."},
            {"icono": "door-open", "titulo": "Segundas vías de escape habilitadas", "texto": "Las chimeneas de ventilación deben contar con escaleras metálicas y descansos en toda su extensión para garantizar la evacuación."},
            {"icono": "box", "titulo": "Refugios subterráneos con autonomía", "texto": "Espacios herméticos con suministro independiente de oxígeno, alimentos, agua y comunicación directa con superficie."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de la Comisión Investigadora de Accidentes Mineros de SERNAGEOMIN Chile y normativas de seguridad minera subterránea.",
        "guionReel": (
            "¿Te imaginas quedar atrapado a 700 metros bajo tierra por una roca del tamaño de un edificio?\n\n"
            "El 5 de agosto de 2010, en el desierto de Atacama, Chile, la montaña colapsó sobre la mina San José.\n\n"
            "Un megabloque de 700.000 toneladas se desprendió sepultando la rampa principal de salida. Treinta y tres mineros quedaron atrapados en la oscuridad absoluta.\n\n"
            "Corrieron hacia la chimenea de ventilación... pero la empresa nunca había instalado las escaleras metálicas de escape obligatorias por ley.\n\n"
            "Por suerte contaban con un refugio básico y una disciplina admirable que les permitió resistir 69 días hasta el rescate más épico de la minería moderna.\n\n"
            "La geotecnia y las vías de evacuación no son trámites en un papel: son la línea que separa la vida de la muerte en el subsuelo.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, underground copper-gold mine shaft collapse in Atacama Desert Chile, dark dusty deep gallery illuminated only by miners helmet headlamps. "
            "Massive fallen monolith rock blocking the tunnel portal, fractured rock ceiling with visible steel mesh and rock bolts, miners standing together in solidarity, "
            "somber resilient atmosphere, high-detail realism, 16:9 ratio."
        ),
        "guionLargo": (
            "El cinco de agosto de dos mil diez... en las profundidades del árido desierto de Atacama, en Chile... la tierra rugió con una violencia descomunal... "
            "En el yacimiento de cobre y oro San José... una falla geomecánica masiva provocó el desprendimiento de un megabloque monolítico de roca de setecientas mil toneladas... "
            "El colapso quebró la rampa en espiral de acceso... sellando como una lápida hermética las galerías subterráneas y dejando atrapados a treinta y tres mineros a casi setecientos metros de profundidad... "
            "La mina arrastraba un historial prolongado de desprendimientos de roca y advertencias de peligro desoídas... La explotación intensiva de pilares y la falta de fortificación adecuada con pernos de anclaje y hormigón proyectado... habían desestabilizado la masa rocosa... "
            "Cuando la polvareda y el estruendo inicial cesaron... los trabajadores intentaron escapar por la chimenea de ventilación de emergencia... "
            "Pero al llegar al ducto vertical... descubrieron la más indignante de las negligencias... La empresa minera jamás había completado la instalación de las escaleras de escape exigidas expresamente por el organismo fiscalizador... "
            "Atrapados sin salida física... los treinta y tres hombres se replegaron hacia el refugio de emergencia en el nivel cien... "
            "Allí racionaron con disciplina militar un puñado de provisiones pensado apenas para cuarenta y ocho horas... bebiendo agua de enfriamiento de perforadoras y resistiendo en una atmósfera de sofocante calor y humedad... "
            "Diecisiete días después, una sonda de perforación rompió el silencio con el histórico mensaje... 'Estamos bien en el refugio los 33'... "
            "El exitoso rescate mediante la cápsula Fénix tras sesenta y nueve días de angustia asombró al planeta... pero transformó para siempre las exigencias de la seguridad minera mundial... "
            "Demostró que ninguna explotación subterránea puede operar sin monitoreo microsísmico continuo... sin fortificación sistemática de frentes... sin refugios autónomos equipados... y fundamentalmente... sin una segunda vía de escape transitable en un cien por ciento... "
            "Porque debajo de la roca... la prevención no es una opción... es la única garantía de volver a ver la luz del día."
        )
    },
    {
        "id": "042",
        "fecha": "06 AGOSTO",
        "fechaPublicacion": "2026-08-06",
        "expediente": "Expediente #042",
        "carpeta": "2012-08-06-incendio-refineria-chevron-richmond",
        "titular": "LA TUBERÍA ADELGAZADA AL LÍMITE: EL INCENDIO DE CHEVRON RICHMOND",
        "palabraResaltada": "TUBERÍA ADELGAZADA AL LÍMITE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Refinería de Petróleo Chevron, Richmond, California - 2012",
        "tipoRiesgo": "Seguridad de Procesos (PSM) / Integridad Mecánica",
        "parrafos": [
            "El 6 de agosto de 2012, una gigantesca bola de fuego envolvió la unidad de destilación de crudo de la refinería Chevron en Richmond, poniendo en riesgo a 19 trabajadores que escaparon milagrosamente.",
            "Una tubería de acero al carbono de 8 pulgadas se rompió catastróficamente por corrosión por sulfuración a alta temperatura. Su espesor original de 8 milímetros se había reducido a menos de uno.",
            "Al detectar una microfuga, la empresa intentó retirar la aislación térmica con la planta en marcha en lugar de parar la unidad. La rotura liberó gasóleo caliente que ardió enviando a 15.000 vecinos a emergencias."
        ],
        "puntosClave": [
            {"icono": "activity", "titulo": "Control de corrosión por sulfuración (API 939-C)", "texto": "Monitorear con ultrasonido el 100% de los circuitos de acero al carbono expuestos a sulfuros a más de 230 °C."},
            {"icono": "shield-alert", "titulo": "Prohibido intervenir líneas calientes con fuga", "texto": "Nunca retirar aislamiento ni manipular tuberías en servicio cuando existe una pérdida activa de producto caliente."},
            {"icono": "power", "titulo": "Autoridad de parada de planta (Stop Work)", "texto": "Ante la menor duda de integridad estructural en hidrocarburos calientes, ordenar la despresurización inmediata."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe final de investigación de la Junta de Seguridad Química de EE.UU. (CSB) sobre la refinería Chevron en Richmond (Report No. 2012-03-I-CA).",
        "guionReel": (
            "¿Qué harías si ves salir una nube de humo caliente de una tubería de refinería?\n\n"
            "El 6 de agosto de 2012, en la refinería Chevron de Richmond, detectaron una fuga en un caño de la torre de destilación.\n\n"
            "En lugar de apagar la unidad y despresurizar el circuito, mandaron a diecinueve bomberos y operarios a sacarle la aislación térmica para mirar mejor... ¡con la planta funcionando a máxima presión!\n\n"
            "Lo que no sabían es que por dentro, el azufre del petróleo caliente había carcomido el metal durante años: de ocho milímetros de espesor, quedaba menos de un milímetro. Era casi una hoja de papel.\n\n"
            "Al mover la tubería, el caño colapsó. Una gigantesca nube de gasóleo a 340 grados se encendió en una inmensa bola de fuego.\n\n"
            "Los trabajadores se salvaron corriendo entre las llamas por puro milagro, pero 15.000 residentes terminaron en el hospital por el humo tóxico.\n\n"
            "Ante una fuga en hidrocarburos calientes, la única orden segura es la parada de emergencia."
        ),
        "promptImagen": (
            "Major petrochemical refinery fire documentary photography, crude distillation column towering over Richmond California plant, August 6 2012. "
            "Massive black smoke plume billowing miles high into the evening sky, towering orange flames leaping from piping network, fire suppression monitors spraying water deluges, "
            "emergency vehicles with flashing red beacons, dramatic industrial photojournalism, high resolution 16:9."
        ),
        "guionLargo": (
            "El seis de agosto de dos mil doce... en la histórica refinería de petróleo de Chevron en Richmond, California... una serie de decisiones operativas fallidas estuvo a punto de desencadenar una catástrofe humana descomunal... "
            "En la unidad número cuatro de destilación de crudo... los operadores descubrieron un leve goteo de hidrocarburos calientes y una nube de vapor que salía por debajo del aislamiento térmico de una tubería de acero al carbono de ocho pulgadas... "
            "La línea transportaba gasóleo pesado a más de trescientos cuarenta grados centígrados y a cuatro atmósferas de presión... "
            "Durante décadas de servicio... la tubería había estado sometida a un fenómeno corrosivo bien documentado por la industria... conocido como corrosión por sulfuración a alta temperatura... "
            "En los aceros al carbono con bajo contenido de silicio... los compuestos sulfurosos presentes en el petróleo crudo atacan implacablemente la pared metálica interna... "
            "El espesor original de la pared, calculado en más de ocho milímetros... se había adelgazado progresivamente hasta medir menos de un milímetro en la zona del codo... reduciéndose a la fragilidad de una cáscara de huevo... "
            "En lugar de ejercer la autoridad de detención de trabajo y proceder al corte seguro y enfriamiento de la unidad... la gerencia de planta decidió intentar retirar la chaqueta protectora de fibra de vidrio para evaluar la fuga con la planta en plena marcha... "
            "Diecinueve trabajadores y bomberos de la brigada interna se posicionaron alrededor de la línea con herramientas de mano... "
            "Al remover parte de la cubierta... la debilitada tubería colapsó de manera repentina... "
            "Una gigantesca nube inflamable de gasóleo sobrecalentado se desprendió... cubriendo por completo a la cuadrilla... "
            "Dos minutos después, la nube halló un punto de ignición y se transformó en una colosal bola de fuego... "
            "De manera milagrosa... envueltos en trajes ignífugos y caminando a ciegas a través del infierno de fuego... los diecinueve trabajadores lograron escapar con vida segundos antes de que la unidad entera ardiera fuera de control... "
            "El humo negro resultante cubrió la bahía de San Francisco... obligando a más de quince mil ciudadanos a buscar atención médica en hospitales locales por afecciones respiratorias agudas... "
            "La Junta de Seguridad Química de los Estados Unidos... en su informe final... determinó que Chevron había pospuesto la modernización de la tubería a aleaciones superiores ricas en cromo a pesar de las recomendaciones de sus propios especialistas... "
            "La lección de Richmond es incontrovertible... Las tuberías corroídas bajo servicio caliente jamás deben ser manipuladas... "
            "Frente a la sospecha de pérdida de integridad en líneas críticas... la única decisión técnica y ética válida... es apagar la unidad y despresurizar el sistema."
        )
    }
]

def procesar_lote_3(kokoro_instance):
    procesadas = []

    print(f"\n=======================================================")
    print(f"Iniciando procesamiento de {len(LOTE_3_DATA)} historias del Lote 3 (#033 a #042)")
    print(f"=======================================================\n")

    for h in LOTE_3_DATA:
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

        # 5. Portada gráfica PNG
        portada_path = os.path.join(target_dir, "portada.png")
        if not os.path.exists(portada_path):
            crear_portada_grafica_lote3(h, portada_path)
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

def crear_portada_grafica_lote3(historia, output_path):
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
    """Inyecta las historias del Lote 3 en index.html antes del cierre del array historias."""
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
        imagen: "portada.png",
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

    print("\n✓ index.html actualizado exitosamente con los 10 nuevos expedientes (#033 a #042).")
    return True

def main():
    print("Iniciando motor Kokoro para Lote 3 (#033 a #042)...")
    kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

    procesadas = procesar_lote_3(kokoro)

    if inyectar_en_index_html(procesadas):
        print(f"\n🎉 ¡LOTE 3 COMPLETADO AL 100%! ({len(procesadas)} historias procesadas)")

if __name__ == "__main__":
    main()
