# -*- coding: utf-8 -*-
"""
Generador Agéntico Automatizado para Lote 4: Expedientes #043 a #052 (7 al 16 de agosto)
1. Crea directorios en assets/efemerides/
2. Genera README.md y contenido-completo.md
3. Guarda guion-reel.txt y prompt-portada.txt
4. Genera portada.png (16:9 alta resolución con Pillow)
5. Sintetiza audio en Kokoro (speed 0.86, ~480-530 palabras -> ~3:00 a 3:30 min)
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

LOTE_4_DATA = [
    {
        "id": "043",
        "fecha": "07 AGOSTO",
        "fechaPublicacion": "2026-08-07",
        "expediente": "Expediente #043",
        "carpeta": "2018-08-07-caida-escalera-portatil-mantenimiento",
        "titular": "EL SOBREALCANCE EN LA ESCALERA: LA ILUSIÓN DE ESTABILIDAD",
        "palabraResaltada": "SOBREALCANCE EN LA ESCALERA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Industrial, Mantenimiento Eléctrico - 2018",
        "tipoRiesgo": "Trabajo en Altura / Escaleras Portátiles",
        "parrafos": [
            "El 7 de agosto de 2018, un técnico de mantenimiento sufrió traumatismos graves al precipitarse desde una altura de cuatro metros mientras reparaba una luminaria industrial.",
            "Utilizó una escalera extensible apoyada sobre un piso epóxico húmedo, sin atar la parte superior ni contar con zapatas de goma operativas. Para alcanzar la caja de conexión, estiró el torso hacia afuera perdiendo el centro de gravedad.",
            "La escalera resbaló y se desplazó lateralmente arrojando al operario. La investigación recordó que las escaleras portátiles son medios de paso, nunca plataformas para tareas complejas."
        ],
        "puntosClave": [
            {"icono": "maximize-2", "titulo": "Regla de la hebilla del cinturón", "texto": "Mantener siempre el centro del cuerpo (la hebilla) entre los largueros laterales; jamás sobreextenderse hacia los lados."},
            {"icono": "anchor", "titulo": "Fijación y zapatas antideslizantes", "texto": "Amarrar rígidamente el extremo superior a un elemento firme y asegurar que la base posea zapatas pivotantes sobre suelo seco."},
            {"icono": "alert-triangle", "titulo": "Medio de acceso, no plataforma", "texto": "Para tareas de mantenimiento que demanden ambas manos o fuerza mecánica, utilizar plataformas elevadoras o andamios certificados."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: estadísticas y guías de seguridad en escaleras de OSHA 1926.1053 y normativas europeas EN 131.",
        "guionReel": (
            "¿Sabías que la mayoría de las caídas fatales desde escaleras ocurren a menos de tres metros de altura?\n\n"
            "El 7 de agosto de 2018, en una planta industrial, un técnico debía cambiar una lámpara en altura. Para no perder tiempo buscando una plataforma elevadora, apoyó una escalera extensible contra la columna.\n\n"
            "El piso estaba resbaladizo, no ató la escalera arriba y no había nadie sosteniendo la base.\n\n"
            "Al trabajar, la caja eléctrica le quedaba a medio metro de distancia. En lugar de bajar y mover la escalera, estiró el cuerpo hacia un costado.\n\n"
            "La física no perdona: el centro de gravedad se salió de los parantes, la base patinó y cayó al vacío golpeando contra el suelo de hormigón.\n\n"
            "Una escalera es para subir y bajar, no para trabajar haciendo equilibrio. Mantén siempre tres puntos de apoyo.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Industrial plant interior documentary photography, fallen aluminum extension ladder sprawled across polished concrete factory floor. "
            "Scattered electrical tools, electrician hard hat on the floor, high bay warehouse lighting fixtures high overhead, "
            "wet floor caution signs, dramatic shadows and emergency industrial yellow tape, photorealistic professional photojournalism, 16:9 ratio."
        ),
        "guionLargo": (
            "El siete de agosto de dos mil dieciocho... en una transitada nave de producción manufacturera... un procedimiento considerado rutinario se convirtió en un siniestro incapacitante... "
            "Durante el turno vespertino, un técnico electromecánico con amplia experiencia fue asignado a la reparación de una luminaria cenital suspendida a cuatro metros y medio de altura... "
            "Apremiado por reiniciar la línea productiva... el operario descartó la utilización de una plataforma móvil de tijera que se encontraba en el depósito general... "
            "En su lugar, decidió utilizar una escalera de mano extensible de aluminio de dos cuerpos... "
            "Apoyó los largueros superiores contra una viga de acero... omitiendo amarrar el extremo con eslingas o sogas de retención... "
            "En la base... el suelo de pintura epóxica presentaba condensación y restos de lubricante... y las zapatas de goma antideslizantes de la escalera se encontraban completamente desgastadas... "
            "Para empeorar la situación, el trabajador ascendió en soledad... sin un compañero que mantuviera afianzada la base con sus pies... "
            "Una vez en el peldaño superior... descubrió que la caja de conexiones eléctricas quedaba a unos sesenta centímetros fuera del eje de la escalera... "
            "En lugar de descender tres metros para reposicionar el equipo... decidió sobreextender su cuerpo hacia el lado derecho... sujetando un alicate con una mano y haciendo palanca con la otra... "
            "Al sacar el torso fuera del plano de los parantes laterales... el centro de masa del conjunto sobrepasó el límite de estabilidad estática... "
            "La base de la escalera patinó de forma intempestiva sobre el piso aceitoso... y la estructura giró sobre su propio eje... precipitándose al vacío... "
            "El operario impactó violentamente contra el suelo de hormigón... sufriendo fractura de pelvis y traumatismo craneoencefálico severo... "
            "Las investigaciones de la autoridad laboral fueron concluyentes... Las escaleras portátiles están diseñadas como vías de tránsito vertical transitorio... jamás como puestos fijos de trabajo... "
            "Toda labor que requiera el uso de ambas manos o la aplicación de fuerza mecánica exige el uso de andamios o plataformas elevadoras... "
            "Y cuando deba usarse una escalera... la regla de oro es inviolable... mantener siempre tres puntos de contacto... y la hebilla del cinturón entre los largueros... "
            "Porque en altura... una falsa sensación de confianza dura solo una fracción de segundo."
        )
    },
    {
        "id": "044",
        "fecha": "08 AGOSTO",
        "fechaPublicacion": "2026-08-08",
        "expediente": "Expediente #044",
        "carpeta": "1956-08-08-desastre-minero-bois-du-cazier",
        "titular": "LA VAGONETA FUERA DE LUGAR: EL INCENDIO DE BOIS DU CAZIER",
        "palabraResaltada": "INCENDIO DE BOIS DU CAZIER",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Mina de Carbón Bois du Cazier, Marcinelle, Bélgica - 1956",
        "tipoRiesgo": "Incendio Subterráneo / Señalización y Comunicación",
        "parrafos": [
            "El 8 de agosto de 1956, una de las mayores catástrofes mineras de Europa cobró la vida de 262 mineros atrapados a casi mil metros bajo tierra en Marcinelle, Bélgica.",
            "Una vagoneta de carbón mal calzada en la jaula del pozo sobresalía parcialmente. Por una falta de confirmación de señales entre el fondo y la superficie, el malacate se activó prematuramente.",
            "Al ascender, la vagoneta arrancó vigas de madera, cercenó dos cables eléctricos de alta tensión y partió una tubería de aceite a presión. El arco encendió el aceite y el fuego asfixió las galerías."
        ],
        "puntosClave": [
            {"icono": "phone", "titulo": "Protocolos de comunicación en maniobras críticas", "texto": "Prohibido accionar sistemas de izaje sin confirmación bidireccional y enclavamientos automáticos de posición."},
            {"icono": "zap-off", "titulo": "Protección física de servicios esenciales", "texto": "Canalizar tuberías de aceite hidráulico lejos de conductores eléctricos de alta tensión para evitar ignición cruzada."},
            {"icono": "wind", "titulo": "Ventilación de emergencia y auto-rescatadores", "texto": "Diseño de pozos con flujo reversible y dotación de equipos de escape autónomo contra monóxido de carbono."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informes de la Comisión de Investigación del Desastre de Marcinelle y legislación europea sobre seguridad y salud en explotaciones mineras subterráneas.",
        "guionReel": (
            "¿Puede una simple vagoneta mal colocada provocar la muerte de 262 mineros en minutos?\n\n"
            "El 8 de agosto de 1956, en la mina Bois du Cazier en Bélgica, los operarios cargaban vagonetas de carbón en el elevador a casi mil metros bajo tierra.\n\n"
            "Una vagoneta quedó sobresaliendo apenas unos centímetros porque el mecanismo trabador falló.\n\n"
            "Arriba, el operador del malacate no esperó la confirmación y accionó el izaje. Al subir a toda velocidad, la vagoneta chocó contra las paredes del pozo, cortando cables eléctricos de alta tensión y partiendo un caño de aceite a presión.\n\n"
            "El arco eléctrico prendió fuego el aceite pulverizado y las vigas de madera. El humo negro y el monóxido de carbono inundaron los túneles.\n\n"
            "Doscientos sesenta y dos trabajadores murieron asfixiados en la peor tragedia minera del continente.\n\n"
            "En maniobras críticas de izaje, nunca asumas nada: la comunicación y los bloqueos salvan vidas.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Historical industrial documentary photography, August 8 1956, Bois du Cazier coal mine surface pit head in Marcinelle Belgium. "
            "Massive black smoke and fumes pouring out from the mine shaft pithead tower, crowd of anxious families and rescue miners gathered at gates, "
            "vintage 1950s rescue teams wearing oxygen breathing apparatus, somber overcast sky, highly detailed vintage black and white archival style with subtle sepia tones, 16:9."
        ),
        "guionLargo": (
            "El ocho de agosto de mil novecientos cincuenta y seis... en la cuenca carbonífera de Marcinelle, en Bélgica... el reloj marcaba las ocho y diez de la mañana cuando el infierno se desató en las entrañas de la tierra... "
            "En la mina Bois du Cazier... a novecientos setenta metros de profundidad... dos cuadrillas de mineros realizaban el intercambio de vagonetas en la jaula del pozo principal de extracción... "
            "Una de las vagonetas cargadas con carbón mineral no encajó de manera completa dentro del compartimiento... debido a un fallo en el retenedor automático... quedando su extremo sobresaliendo apenas treinta centímetros hacia el hueco del pozo... "
            "En el fondo de la galería... el enganchador intentó detener la maniobra... pero la comunicación con la sala de máquinas en la superficie se realizaba mediante un arcaico sistema de campanillas de golpe... "
            "En la superficie... el operador del malacate interpretó erróneamente una señal sonora previa... y accionó la palanca de izaje a máxima velocidad... "
            "Al iniciar el ascenso vertical... la vagoneta trabada colisionó brutalmente contra las vigas estructurales de soporte del pozo... arrancando la mampostería... "
            "En su violento recorrido... el hierro destruyó dos cables blindados de alta tensión... y cercenó simultáneamente una tubería de aceite hidráulico presurizada a cincuenta atmósferas... "
            "El aceite atomizado fue proyectado como una nube inflamable sobre los conductores seccionados... desatando un arco eléctrico masivo que encendió una llamarada incontrolable... "
            "En cuestión de segundos... el pozo de entrada de aire fresco se convirtió en una gigantesca chimenea de fuego que succionó el humo tóxico y el monóxido de carbono directamente hacia las galerías habitadas por cientos de obreros... "
            "El sistema de ventilación carecía de compuertas de inversión rápida... y los trabajadores no contaban con máscaras de escape auto-rescatadoras... "
            "Doscientos sesenta y dos mineros... en su mayoría trabajadores inmigrantes italianos... perdieron la vida por asfixia en la peor tragedia de la minería europea... "
            "El desastre de Marcinelle marcó el nacimiento de las primeras directivas comunitarias sobre seguridad industrial... demostrando que en operaciones subterráneas... los sistemas de comunicación no pueden admitir ambigüedades... y los tendidos de energía y fluidos jamás deben compartir el mismo espacio vulnerable... "
            "Porque bajo la tierra... un malentendido de tres segundos puede sepultar para siempre cientos de vidas."
        )
    },
    {
        "id": "045",
        "fecha": "09 AGOSTO",
        "fechaPublicacion": "2026-08-09",
        "expediente": "Expediente #045",
        "carpeta": "2017-08-09-explosion-neumatico-gigante-taller",
        "titular": "LA ONDA DE CHOQUE DEL ARO: EXPLOSIÓN EN EL TALLER DE NEUMÁTICOS",
        "palabraResaltada": "EXPLOSIÓN EN EL TALLER",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Taller de Mantenimiento de Maquinaria Pesada - 2017",
        "tipoRiesgo": "Energía Mecánica Almacenada / Aros Multipieza",
        "parrafos": [
            "El 9 de agosto de 2017, la explosión repentina durante el inflado de un neumático de camión minero fuera de ruta causó la muerte instantánea de un gomerista y destruyó el galpón de mantenimiento.",
            "La llanta utilizaba un aro multipieza con anillo de cierre metálico fatigado y deformado. El operario infló la cubierta a 110 PSI sin utilizar la jaula de seguridad y permaneciendo de pie justo frente a la pestaña.",
            "Al alcanzar la presión de trabajo, el aro se desencastró proyectando cientos de kilos de acero a velocidad supersónica. La energía contenida en un neumático gigante equivale a dinamita en potencia."
        ],
        "puntosClave": [
            {"icono": "box", "titulo": "Jaula de inflado certificada", "texto": "Todo neumático de camión o equipo pesado con aros multipieza debe colocarse dentro de una jaula estructural de contención."},
            {"icono": "maximize", "titulo": "Manguera larga y boquilla de acople", "texto": "Utilizar boquilla con traba automática y manguera de al menos 3 metros con regulador y manómetro en línea para operar fuera de la trayectoria."},
            {"icono": "search", "titulo": "Inspección de aros y pestañas", "texto": "Descartar de inmediato componentes de llanta con fisuras, corrosión severa o deformaciones mecánicas sin intentar enderezarlos con golpes."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: manual de seguridad en servicio de neumáticos y llantas multipieza de OSHA 1910.177 y recomendaciones de la Tire Industry Association (TIA).",
        "guionReel": (
            "¿Sabías que inflar un neumático de camión equivale a tener una granada de fragmentación lista para detonar?\n\n"
            "El 9 de agosto de 2017, en un taller de maquinaria pesada, un mecánico acababa de armar una rueda gigante con llanta de aros multipieza.\n\n"
            "Conectó la manguera y se quedó parado justo enfrente de la llanta, mirando el manómetro.\n\n"
            "No metió la rueda en la jaula de seguridad porque 'pesaba mucho moverla' y el aro de cierre estaba desgastado y con óxido.\n\n"
            "Al llegar a cien libras de presión, el anillo de acero se soltó con una violencia atroz: salió disparado como un misil, partiendo el techo del taller y matando al mecánico en el acto.\n\n"
            "La presión de aire es energía pura almacenada. Usa siempre la jaula de contención, manguera con manómetro a distancia y ponte fuera de la línea de fuego.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Documentary industrial maintenance photography, heavy equipment tire workshop, massive multi-piece mining truck wheel ruptured during inflation. "
            "Twisted steel lock ring projected into broken corrugated workshop wall, cracked concrete floor, scattered pneumatic air hoses and pressure gauges, "
            "prominent heavy steel tire inflation safety cage standing nearby empty, high contrast industrial workshop lighting, 16:9 ratio."
        ),
        "guionLargo": (
            "El nueve de agosto de dos mil diecisiete... un estallido con potencia equivalente a una detonación militar sacudió las instalaciones de una base de mantenimiento de equipos pesados... "
            "En el sector de gomería industrial... dos técnicos concluían el recambio de una cubierta para un camión volcador de sesenta toneladas... "
            "El ensamble utilizaba una llanta de acero del tipo multipieza... un sistema compuesto por la base del rin, una pestaña lateral móvil y un anillo de cierre elástico ranurado... "
            "Durante el montaje... el anillo de fijación presentaba evidencias visibles de corrosión galvánica y una leve curvatura producto de golpes de maza recibidos en montajes anteriores... "
            "Pese a que las normativas exigen retirar de circulación cualquier componente deformado... la pieza fue encastrada a la fuerza en la canaleta de retención... "
            "Llegado el momento del inflado... los operarios decidieron no trasladar el conjunto rodado hacia la jaula estructural de seguridad... argumentando que las dimensiones de la cubierta hacían engorroso el ingreso al habitáculo de contención... "
            "Uno de los trabajadores conectó un acople neumático directo... y se posicionó de cuclillas... justo en el plano perpendicular a la cara frontal de la llanta... sosteniendo el manómetro manual a menos de cincuenta centímetros de distancia... "
            "A medida que la presión interna trepaba por encima de los cien PSI... la tensión elástica sobre el anillo defectuoso creció de manera exponencial... "
            "De forma repentina y sin crujido previo... la pestaña de cierre se desencastró violentamente... "
            "La masa de acero de más de cuarenta kilogramos fue propulsada por la liberación supersónica de aire comprimido... impactando directamente contra el cuerpo del operario... "
            "La onda expansiva reventó las chapas del techo del taller y arrojó herramientas a decenas de metros... provocando la muerte instantánea del trabajador... "
            "Las investigaciones de los organismos de prevención recuerdan que el aire comprimido en neumáticos pesados es energía potencial acumulada de magnitud letal... "
            "El protocolo técnico es riguroso e innegociable... El inflado debe realizarse invariablemente dentro de una jaula certificada... empleando acoples de boquilla con traba... y operando el manómetro desde una manguera a distancia... manteniéndose siempre fuera de la trayectoria balística de la rueda... "
            "Porque ante la energía contenida en un neumático... la distancia es la única barrera infranqueable."
        )
    },
    {
        "id": "046",
        "fecha": "10 AGOSTO",
        "fechaPublicacion": "2026-08-10",
        "expediente": "Expediente #046",
        "carpeta": "2008-08-10-explosion-propano-sunrise-toronto",
        "titular": "EL TRASVASE PROHIBIDO: LA BLEVE DE SUNRISE PROPANE",
        "palabraResaltada": "BLEVE DE SUNRISE PROPANE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Distribuidora de GLP, Toronto, Canadá - 2008",
        "tipoRiesgo": "Seguridad de Procesos / Gas Licuado de Petróleo (GLP)",
        "parrafos": [
            "La madrugada del 10 de agosto de 2008, una descomunal explosión por BLEVE en la planta distribuidora Sunrise Propane iluminó el cielo de Toronto, obligando a evacuar a más de 12.000 residentes.",
            "El siniestro se originó durante una maniobra clandestina de trasvase directo de propano de camión cisterna a camión cisterna (truck-to-truck), práctica prohibida por la normativa por carecer de sistemas fijos de salvaguarda.",
            "Una manguera de trasvase colapsó liberando una inmensa nube de vapor que encontró ignición en un calentador comercial. El fuego envolvió los tanques principales desatando una reacción en cadena devastadora."
        ],
        "puntosClave": [
            {"icono": "ban", "titulo": "Prohibido trasvase móvil improvisado", "texto": "Las transferencias de GLP deben realizarse únicamente en islas fijas de carga homologadas con sistemas automáticos de control."},
            {"icono": "git-pull-request", "titulo": "Acoples de desacople rápido (Breakaway)", "texto": "Instalar válvulas de corte automático por tracción mecánica en mangueras para aislar el flujo ante movimiento o rotura."},
            {"icono": "shield-alert", "titulo": "Distancias de seguridad y zonificación urbana", "texto": "Impedir el emplazamiento de parques de almacenamiento de hidrocarburos a granel adyacentes a barrios residenciales."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de la Oficina del Jefe de Bomberos de Ontario y fallo judicial de la Corte de Justicia de Ontario sobre el desastre de Sunrise Propane.",
        "guionReel": (
            "¿Por qué está estrictamente prohibido pasar gas de un camión a otro camión en una playa de maniobras?\n\n"
            "El 10 de agosto de 2008, en Toronto, Canadá, una explosión colosal despertó a una ciudad entera a las tres de la mañana.\n\n"
            "En la planta Sunrise Propane, dos choferes realizaban un trasvase clandestino conectando una manguera flexible de un camión cisterna a otro para ganar tiempo.\n\n"
            "La manguera, fatigada y sin mantenimiento, reventó bajo presión. Toneladas de gas propileno y propano líquido se convirtieron en una densa nube blanca que cubrió el predio.\n\n"
            "El gas tocó el quemador de un secador y detonó. Las llamas rodearon los enormes tanques horizontales hasta provocar una explosión tipo BLEVE que lanzó fragmentos de acero a un kilómetro.\n\n"
            "Un bombero y un trabajador murieron, y doce mil vecinos tuvieron que ser evacuados de emergencia.\n\n"
            "En gas licuado, los procedimientos de diseño no son sugerencias: son barreras contra la catástrofe."
        ),
        "promptImagen": (
            "Dramatic nighttime industrial disaster documentary photography, August 10 2008 Sunrise Propane facility explosion Toronto Canada. "
            "Towering fireball and explosion mushroom rising into night sky, illuminated destroyed industrial buildings, shattered commercial truck tankers, "
            "suburban houses with blown-out windows in foreground, distant flashing red and blue emergency responder lights, high realism, 16:9 aspect ratio."
        ),
        "guionLargo": (
            "El diez de agosto de dos mil ocho... a las tres y treinta y cinco de la madrugada... una bola de fuego descomunal iluminó la noche de la ciudad de Toronto... semejando el impacto de un bombardeo aéreo... "
            "En el predio de la compañía distribuidora Sunrise Propane... ubicado peligrosamente pegado a un denso vecindario residencial... se almacenaban miles de metros cúbicos de gas licuado de petróleo... "
            "Durante esa madrugada, se llevaba a cabo una maniobra estrictamente prohibida por los códigos de seguridad canadienses... conocida como trasvase camión a camión... "
            "Para ahorrar tiempos de bombeo hacia los tanques estacionarios de almacenamiento... los operadores acostumbraban interconectar dos camiones cisterna mediante mangueras flexibles provisionales... transfiriendo el combustible líquido de una unidad a otra en plena playa abierta... "
            "Aquella noche... una de las mangueras de transferencia... que presentaba fisuras internas y fatiga por flexión... sufrió una rotura catastrófica bajo la presión de bombeo... "
            "Sin válvulas de cierre por exceso de flujo calibradas ni acoples de desacople rápido tipo breakaway... el gas licuado comenzó a salir a borbotones... "
            "El propano líquido se expandió doscientas setenta veces al entrar en contacto con el aire ambiente... formando una densa niebla a ras del piso que se deslizó hacia los galpones contiguos... "
            "Al tomar contacto con el sistema de calefacción de una oficina... la mezcla detonó en una deflagración masiva que envolvió instantáneamente a los camiones y a los tanques pulmón principales de la planta... "
            "El fuego abrasador sobrecalentó las paredes metálicas de los cilindros presurizados... debilitando la resistencia estructural del acero... "
            "Minutos más tarde... se produjo el fenómeno más temido en la seguridad de procesos... una explosión por expansión de vapor de líquido en ebullición... una masiva BLEVE... "
            "Uno de los tanques estalló como un misil supersónico... arrojando pedazos de acero incandescente a más de un kilómetro de distancia... destrozando cientos de viviendas vecinas... "
            "La tragedia costó la vida de un trabajador de la planta y de un valiente bombero... forzando la evacuación nocturna inmediata de más de doce mil residentes... "
            "El fallo judicial posterior impuso multas millonarias y sentó jurisprudencia mundial... Los trasvases no controlados son un acto de negligencia criminal... "
            "Porque cuando se reemplazan las instalaciones fijas y diseñadas por mangueras improvisadas... la seguridad deja de existir."
        )
    },
    {
        "id": "047",
        "fecha": "11 AGOSTO",
        "fechaPublicacion": "2026-08-11",
        "expediente": "Expediente #047",
        "carpeta": "2019-08-11-atrapamiento-rodillos-cinta-transportadora",
        "titular": "LA TELA ATRAPADA EN EL RODILLO: CUANDO LA MÁQUINA NO ESPERA",
        "palabraResaltada": "RODILLO: CUANDO LA MÁQUINA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Línea de Envasado y Empaque Industrial - 2019",
        "tipoRiesgo": "Atrapamiento Mecánico / Protección de Máquinas",
        "parrafos": [
            "El 11 de agosto de 2019, una operaria en una planta de embalaje continuo sufrió la pérdida traumática de su extremidad superior tras quedar atrapada en el tambor de retorno de una cinta transportadora.",
            "Intentó limpiar una acumulación de cartón apelmazado sobre el rodillo utilizando un trapo y guantes de tela sin detener la marcha de la máquina. La tela fue succionada por el punto de convergencia o pellizco.",
            "La línea carecía de guardas de protección fijas en el tambor tensor y el cable de parada de emergencia estaba fuera de alcance. La regla básica: partes en movimiento jamás se limpian en servicio."
        ],
        "puntosClave": [
            {"icono": "shield-off", "titulo": "Guardas en puntos de convergencia (Nip points)", "texto": "Instalar protecciones fijas enrejadas que impidan el acceso físico a tambores y rodillos motrices según ISO 13857."},
            {"icono": "scissors", "titulo": "Prohibido ropa holgada y guantes textiles", "texto": "En proximidades de ejes giratorios está terminantemente prohibido el uso de guantes, bufandas o prendas con partes sueltas."},
            {"icono": "lock", "titulo": "Parada total y LOTO para limpieza", "texto": "Toda limpieza, destrabe o mantenimiento exige detener el motor principal y aplicar bloqueo y candado de seguridad (energía cero)."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: criterios de resguardo mecánico de transportadores de cinta OSHA 1910.212 y normas de seguridad en maquinaria ANSI B20.1.",
        "guionReel": (
            "¿Cuánto tiempo tarda un rodillo industrial en atrapar un brazo humano?\n\n"
            "Menos de medio segundo.\n\n"
            "El 11 de agosto de 2019, en una planta de empaque, una operaria vio que se acumulaban restos de cartón en el rodillo inferior de una cinta transportadora.\n\n"
            "Para no parar la producción del turno, tomó un trapo y, con guantes de tela puestos, intentó limpiar el tambor mientras giraba a toda velocidad.\n\n"
            "El punto de pellizco entre la cinta de goma y el rodillo atrapó una hilacha del trapo. En un pestañeo, succionó el guante, los dedos, la mano y el brazo entero.\n\n"
            "La guarda metálica de protección había sido retirada meses atrás para facilitar la lubricación y el cable de parada de emergencia estaba roto.\n\n"
            "Jamás toques una máquina en movimiento. La limpieza y el mantenimiento se hacen únicamente con parada total y candado LOTO.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Industrial factory conveyor belt safety scene, heavy manufacturing packaging belt line with massive steel return roller. "
            "Torn piece of fabric caught in the pinch point between conveyor belt and metal drum, red pull-wire emergency stop cable running along the frame, "
            "yellow fixed wire mesh safety guards leaning removed against the industrial wall, realistic documentary photography, dramatic workshop light, 16:9 ratio."
        ),
        "guionLargo": (
            "El once de agosto de dos mil diecinueve... en el sector de clasificación y paletizado de una planta industrial de empaque... un segundo de distracción se transformó en una tragedia mutilante... "
            "La línea de transporte de bultos funcionaba a máxima cadencia operativa... desplazando cajas de cartón sobre bandas motorizadas de caucho... "
            "Al pasar junto al sector de retorno de una cinta transportadora principal... una operaria notó que varios restos de cartón y cinta adhesiva se habían apelmazado sobre la superficie metálica del tambor tensor... "
            "Preocupada por evitar un atasco que demorara el flujo de salida... decidió intervenir de inmediato... "
            "En lugar de pulsar el pulsador de parada de línea... bloqueando el interruptor seccionador con un candado de seguridad... la trabajadora tomó un paño de limpieza y se acercó a la máquina en marcha... "
            "Llevaba colocados guantes de tela de algodón con puño holgado... "
            "Al aproximar el paño al tambor giratorio para frotar el cilindro... se produjo el temido fenómeno mecánico conocido en seguridad como punto de convergencia o nip point... "
            "El ángulo agudo formado por la banda de goma entrando en contacto con el rodillo metálico actúa como un succionador implacable... "
            "Una hilacha del trapo fue atrapada por el tambor... En una fracción de segundo, la tracción arrastró el guante... los dedos de la mano... y la extremidad superior completa hacia el interior del mecanismo... "
            "El rodillo motriz, impulsado por un motorreductor de diez caballos de fuerza... no se detuvo... "
            "Desesperada, la operaria intentó accionar con su cuerpo la cuerda de tracción de parada de emergencia perimetral... pero el cable pull-cord se encontraba destensado e inoperativo desde hacía semanas... "
            "Fueron necesarios los gritos de auxilio para que un compañero a veinte metros cortara la corriente general... sufriendo la operaria una amputación traumática irreparable... "
            "El análisis posterior reveló graves omisiones de diseño... La máquina carecía de la guarda de enrejado físico obligatoria que debe blindar todo tambor inferior... "
            "Y la cultura operativa toleraba la intervención sobre equipos energizados... "
            "La lección es categórica... Frente a ejes rotativos, la tela y la confianza son letales... La limpieza mecánica se realiza exclusivamente con energía cero... candado colocado... y la máquina absolutamente detenida."
        )
    },
    {
        "id": "048",
        "fecha": "12 AGOSTO",
        "fechaPublicacion": "2026-08-12",
        "expediente": "Expediente #048",
        "carpeta": "2015-08-12-explosiones-puerto-tianjin-quimicos",
        "titular": "EL AGUA SOBRE EL FUEGO EQUIVOCADO: EL CATACLISMO DE TIANJIN",
        "palabraResaltada": "CATACLISMO DE TIANJIN",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Zona Portuaria de Binhai, Puerto de Tianjin, China - 2015",
        "tipoRiesgo": "Seguridad de Procesos / Almacenamiento Químico Incompatible",
        "parrafos": [
            "La noche del 12 de agosto de 2015, dos explosiones colosales pulverizaron el depósito logístico de químicos Ruihai en el puerto de Tianjin, provocando 173 muertos, incluidos 104 bomberos.",
            "El fuego se originó por el autocalentamiento de nitrocelulosa seca almacenada en contenedores sobrecalentados por el sol estival. El incendio se propagó a depósitos contiguos de nitrato de amonio y carburo de calcio.",
            "Desconociendo el inventario exacto, las brigadas aplicaron agua: el carburo de calcio reaccionó liberando acetileno inflamable que detonó 800 toneladas de nitrato. Una falla crítica de incompatibilidad y comunicación de riesgo."
        ],
        "puntosClave": [
            {"icono": "flame", "titulo": "Reactividad violenta con agua", "texto": "Sustancias como el carburo de calcio generan gases altamente explosivos al contacto con agua; jamás atacar con mangueras convencionales."},
            {"icono": "file-text", "titulo": "Fichas de seguridad (FDS) para bomberos", "texto": "Las brigadas de respuesta a emergencias deben disponer del inventario químico digitalizado en tiempo real antes de ingresar a la zona caliente."},
            {"icono": "layers", "titulo": "Segregación física y zonificación", "texto": "Respetar distancias mínimas entre depósitos de comburentes, inflamables y sustancias reactivas con agua según el Código IMDG."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe oficial del Consejo de Estado de la República Popular China sobre el desastre de Tianjin y directrices de la OMI (Organización Marítima Internacional).",
        "guionReel": (
            "¿Sabías que arrojar agua sobre un incendio químico puede provocar una explosión nuclear en potencia?\n\n"
            "La noche del 12 de agosto de 2015, en el gigantesco puerto de Tianjin, China, un cargamento de nitrocelulosa se recalentó por el calor del verano y comenzó a arder.\n\n"
            "Los bomberos llegaron al lugar sin tener las Fichas de Datos de Seguridad ni saber qué había adentro de los contenedores.\n\n"
            "Empezaron a regar el fuego con agua. Pero al lado había toneladas de carburo de calcio.\n\n"
            "Al tocar el agua, el carburo reaccionó liberando nubes masivas de gas acetileno. El gas encendió y detonó 800 toneladas de nitrato de amonio almacenadas ilegalmente a metros de distancia.\n\n"
            "El cataclismo fue atroz: 173 personas murieron, entre ellas 104 valientes bomberos que combatieron a ciegas un fuego equivocado.\n\n"
            "Con sustancias químicas, nunca ataques un incendio sin saber exactamente qué estás combatiendo.\n\n"
            "La información es la primera línea de supervivencia."
        ),
        "promptImagen": (
            "Panoramic archival documentary photograph, August 12 2015 Tianjin port chemical warehouse explosion aftermath. "
            "Massive smoking crater filled with dark toxic water where Ruihai warehouse stood, thousands of burned crumpled shipping containers stacked like matchsticks, "
            "burned-out vehicle parking lots with rows of white cars scorched to their frames, industrial harbor crane twisted, morning dawn lighting, high detail, 16:9 aspect ratio."
        ),
        "guionLargo": (
            "La noche del doce de agosto de dos mil quince... en el dinámico puerto marítimo de Tianjin, en el norte de China... se desencadenó uno de los desastres industriales más catastróficos del siglo veintiuno... "
            "Dentro de las instalaciones de la empresa logística Ruihai... autorizada irregularmente para operar a escasa distancia de barrios residenciales... se acumulaban miles de toneladas de sustancias químicas de máxima peligrosidad... "
            "Durante una sofocante jornada estival... varios barriles de nitrocelulosa... almacenados en contenedores metálicos expuestos a la radiación solar directa... sufrieron la evaporación de su agente humectante... "
            "Al secarse por completo... la nitrocelulosa inició un proceso de autocalentamiento por descomposición espontánea... derivando en un incendio dentro del contenedor... "
            "Las primeras dotaciones del cuerpo de bomberos acudieron con celeridad al recinto portuario... "
            "Sin embargo... la empresa no disponía de un registro de inventario actualizado ni entregó a los mandos de emergencia las Fichas de Datos de Seguridad de los materiales almacenados... "
            "Desconociendo la naturaleza química de la carga que los rodeaba... los rescatistas desplegaron líneas de manguera y comenzaron a arrojar caudales masivos de agua sobre el fuego... "
            "Pero contiguo al foco ígneo descansaban cientos de toneladas de carburo de calcio... "
            "En la química industrial, el carburo de calcio reacciona violentamente con el agua... liberando de forma instantánea grandes volúmenes de gas acetileno... un hidrocarburo extraordinariamente explosivo e inestable... "
            "El acetileno generado detonó... envolviendo en una llamarada a las brigadas de ataque y propagando el fuego hacia un parque donde se apilaban ochocientas toneladas de nitrato de amonio... "
            "Treinta segundos después... sobrevino la detonación principal... "
            "Una explosión equivalente a veintiún toneladas de TNT generó un terremoto de magnitud dos punto nueve en la escala Richter... y un cráter de cien metros de ancho... "
            "Ciento setenta y tres personas perdieron la vida... entre ellas ciento cuatro heroicos bomberos que murieron en cumplimiento del deber sin haber recibido la información técnica básica... "
            "La tragedia de Tianjin redefinió la gestión global de mercancías peligrosas en recintos portuarios... demostrando que almacenar sustancias incompatibles juntas es una bomba de tiempo... "
            "Y que jamás... bajo ninguna circunstancia... debe atacarse un siniestro químico sin identificar previamente los materiales involucrados."
        )
    },
    {
        "id": "049",
        "fecha": "13 AGOSTO",
        "fechaPublicacion": "2026-08-13",
        "expediente": "Expediente #049",
        "carpeta": "2016-08-13-golpe-calor-severo-cuadrilla-gasoducto",
        "titular": "EL COLAPSO TÉRMICO EN LA ZANJA: CUANDO EL CUERPO DICE BASTA",
        "palabraResaltada": "COLAPSO TÉRMICO EN LA ZANJA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Tendido de Ductos a Cielo Abierto, Zona Semiárida - 2016",
        "tipoRiesgo": "Higiene Industrial / Estrés Térmico por Calor",
        "parrafos": [
            "El 13 de agosto de 2016, un operario de 28 años sufrió un golpe de calor fulminante mientras trabajaba en el revestimiento y soldadura de una tubería en una zanja abierta a 41 °C de temperatura ambiente.",
            "El trabajador llevaba equipo de protección completo (mameluco ignífugo, guantes pesados y careta) y no estaba aclimatado. La cuadrilla no contaba con régimen de pausas en sombra ni reposición de sales minerales.",
            "Al desorientarse, fue dejado descansar bajo una carpa sin enfriamiento activo; su temperatura central superó los 42 °C causándole una falla multiorgánica. El estrés térmico es un peligro letal e invisible."
        ],
        "puntosClave": [
            {"icono": "thermometer", "titulo": "Monitoreo del índice WBGT y pausas", "texto": "Medir la temperatura de globo y bulbo húmedo para fijar ciclos obligatorios de trabajo y descanso bajo sombra fresca."},
            {"icono": "droplets", "titulo": "Hidratación con electrolitos", "texto": "Proveer agua fresca continua y sales de rehidratación; el agua pura sola no repone el sodio y potasio perdidos por sudoración."},
            {"icono": "heart-pulse", "titulo": "Enfriamiento inmediato como emergencia médica", "texto": "Ante confusión o piel caliente/seca, retirar EPP, aplicar agua fría y ventilación forzada sin demorar el traslado médico."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: recomendaciones de prevención de estrés térmico laboral de NIOSH (Pub. No. 2016-106) y normativas OSHA de trabajo en ambientes calurosos.",
        "guionReel": (
            "¿Sabías que el golpe de calor en el trabajo puede destruir tu cerebro y tus órganos en menos de una hora?\n\n"
            "El 13 de agosto de 2016, en una obra de tendido de gasoducto a cielo abierto, la temperatura superaba los 41 grados al rayo del sol.\n\n"
            "Un joven soldador llevaba traje ignífugo pesado, polainas y casco. Era su tercer día en la obra: su cuerpo no estaba aclimatado.\n\n"
            "Bebía poca agua y no tomaba sales minerales. Al mediodía empezó a marearse, arrastrar las palabras y tambalear dentro de la zanja.\n\n"
            "Sus compañeros creyeron que solo estaba 'cansado' y lo sentaron bajo una lona sin hielo ni atención médica. Una hora después, convulsionó y su corazón colapsó con 42 grados de fiebre interna.\n\n"
            "El golpe de calor es una emergencia médica letal. Exige pausas en sombra, agua con sales y enfriamiento inmediato al menor síntoma.\n\n"
            "Cuidar a tu compañero es la primera regla en el terreno."
        ),
        "promptImagen": (
            "Industrial hygiene outdoor documentary photography, remote pipeline construction site in semi-arid desert terrain under blazing harsh midday sun. "
            "A deep open trench with large diameter steel pipe, welding gear and gas cylinders by trench edge, heavy fire-retardant PPE work coveralls and hard hat discarded on ground, "
            "water coolers and shade canopy shelter in distance, heat haze shimmers on horizon, high realism, 16:9 ratio."
        ),
        "guionLargo": (
            "El trece de agosto de dos mil dieciséis... en una desolada planicie semiárida donde avanzaba la construcción de un gasoducto de alta presión... la carga térmica ambiental se convirtió en un enemigo silencioso e implacable... "
            "A las trece horas, los termómetros marcaban cuarenta y un grados a la sombra... con una radiación solar directa que elevaba la sensación térmica sobre el terreno pedregoso por encima de los cuarenta y siete grados... "
            "En el interior de una zanja de dos metros de profundidad... un operario recién ingresado a la cuadrilla realizaba tareas de amolado y biselado de juntas de tubería... "
            "Cumpliendo las directivas de seguridad contra arco eléctrico y chispas... el trabajador vestía un mameluco de tela ignífuga pesada... guantes de cuero de caña larga... polainas y careta protectora... "
            "Esta indumentaria hermética actuaba como una barrera aislante que impedía por completo la evaporación del sudor... el único mecanismo biológico eficaz que posee el cuerpo humano para disipar el calor... "
            "El operario apenas llevaba tres días en el proyecto... careciendo del período de aclimatación fisiológica de dos semanas indispensable para labores en climas extremos... "
            "Pese a que el sudor le empapaba la ropa... en la obra solo se suministraba agua común sin reposición de electrolitos... desatando un cuadro agudo de hiponatremia... "
            "Al promediar la tarde... el trabajador comenzó a balbucear... mostró signos de desorientación témporo-espacial y se desplomó contra el caño de acero... "
            "Sus compañeros... desconociendo la gravedad de la patología por calor... lo trasladaron caminando hasta un gazebo de lona... dejándolo reposar sin aplicarle paños fríos ni retirar el mameluco... "
            "Para cuando una ambulancia llegó al campamento remoto... el operario había entrado en coma con una temperatura interna superior a los cuarenta y dos grados... sufriendo un paro cardiorrespiratorio por golpe de calor severo... "
            "Las investigaciones de higiene industrial recordaron que el estrés térmico no es una simple fatiga... es un riesgo laboral crítico... "
            "Toda faena en ambientes extremos exige medir el índice WBGT... pautar regímenes de hidratación isotónica obligatoria... y capacitar a las cuadrillas para reconocer que ante un síntoma de confusión... el enfriamiento corporal inmediato es la única opción de rescate... "
            "Porque frente al calor extremo... la tolerancia humana tiene un límite biológico intransigente."
        )
    },
    {
        "id": "050",
        "fecha": "14 AGOSTO",
        "fechaPublicacion": "2026-08-14",
        "expediente": "Expediente #050",
        "carpeta": "2013-08-14-explosion-submarino-sindhurakshak",
        "titular": "EXPLOSIÓN EN LA CÁMARA DE TORPEDOS: LA CADENA DE FALLAS DEL SINDHURAKSHAK",
        "palabraResaltada": "SINDHURAKSHAK",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Base Naval de Bombay, Submarino INS Sindhurakshak - 2013",
        "tipoRiesgo": "Seguridad de Procesos / Manejo de Munición y Espacios Confinados",
        "parrafos": [
            "La madrugada del 14 de agosto de 2013, el submarino militar diésel-eléctrico INS Sindhurakshak sufrió múltiples explosiones internas y se hundió amarrado en el muelle de Bombay, muriendo sus 18 tripulantes.",
            "El desastre ocurrió durante la carga y estiba de torpedos y misiles en la cámara de proa. Una manipulación fuera de procedimiento provocó un cortocircuito eléctrico o una descarga estática que activó accidentalmente el motor de un misil.",
            "La combustión confinada desató la detonación por simpatía del resto de las ojivas de combate. La tragedia subrayó el valor supremo de la disciplina procedimental (SOP) al manipular explosivos militares o industriales."
        ],
        "puntosClave": [
            {"icono": "check-square", "titulo": "Disciplina procedimental absoluta (SOP)", "texto": "Prohibido alterar o acelerar pasos en manuales de carga de municiones, propelentes o explosivos industriales."},
            {"icono": "zap", "titulo": "Control estricto de estática y conexiones eléctricas", "texto": "Toma a tierra certificada continua y bloqueo de fuentes energéticas para evitar arcos en áreas con material reactivo."},
            {"icono": "users", "titulo": "Personal mínimo indispensable", "texto": "Restringir la permanencia dentro del recinto confinado exclusivamente a los operadores autorizados para la maniobra."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de la Junta de Investigación de la Marina de la India (Court of Inquiry) sobre el hundimiento del INS Sindhurakshak.",
        "guionReel": (
            "¿Qué ocurre cuando se comete un error en la carga de explosivos dentro de un espacio confinado de acero?\n\n"
            "El 14 de agosto de 2013, en la base naval de Bombay, el submarino Sindhurakshak estaba listo para zarpar.\n\n"
            "En la cámara de torpedos de proa, la tripulación cargaba misiles de crucero y torpedos pesados. Era una tarea de máxima precisión que exigía cumplir cada paso del manual.\n\n"
            "Pero hubo un fallo crítico: una mala conexión eléctrica o una descarga electrostática encendió accidentalmente el propelente de uno de los misiles.\n\n"
            "En segundos, el fuego confinó la cámara y detonó en cadena las cabezas de combate. Dos explosiones masivas abrieron el casco como una lata y el submarino se hundió en el muelle en minutos.\n\n"
            "Los dieciocho marineros murieron atrapados.\n\n"
            "Con sustancias energéticas y explosivas, los procedimientos operativos paso a paso no se negocian jamás.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Naval industrial dock documentary photography, night of August 14 2013, naval dockyard in Mumbai India. "
            "Submarine partially submerged and burned at naval berth, massive hole blown in forward hull section, smoke and emergency flares reflecting on dark water, "
            "dock cranes and naval rescue crews standing on pier with spotlight beams cutting through smoke, somber hyperrealistic atmosphere, 16:9."
        ),
        "guionLargo": (
            "La madrugada del catorce de agosto de dos mil trece... en el muelle militar de la base naval de Bombay, en la India... un siniestro de proporciones colosales conmocionó a las fuerzas armadas internacionales... "
            "El submarino de propulsión diésel-eléctrica de clase Kilo... bautizado como INS Sindhurakshak... se encontraba atracado completando las tareas de alistamiento para una misión de patrullaje prolongado... "
            "En el compartimiento número uno... ubicado en la proa de la nave... una dotación de especialistas realizaba la estiba y armado final de torpedos pesados y misiles de crucero antibuque tipo Klub... "
            "La manipulación de munición de combate en el interior de un submarino representa uno de los entornos de mayor exigencia de seguridad de procesos del mundo... por tratarse de un espacio confinado hermético repleto de explosivos y propelentes sólidos... "
            "Poco después de la medianoche... una secuencia irregular en el procedimiento operativo estandarizado durante la verificación de circuitos o una chispa producida por una descarga electrostática parásita... activó de forma accidental el encendedor del motor cohete de uno de los misiles... "
            "El propelente encendido despidió una masa de gases incandescentes a miles de grados dentro del estrecho recinto metálico... "
            "El calor extremo y el confinamiento provocaron en cuestión de segundos la detonación por simpatía de dos ojivas de combate adyacentes... "
            "Una doble explosión monumental reventó el casco de presión de acero especial... proyectando llamaradas que alcanzaron decenas de metros sobre el cielo portuario... "
            "El agua de mar irrumpió torrencialmente por las fracturas del casco... y la nave se fue a pique en el propio muelle en menos de diez minutos... "
            "Los dieciocho marinos y oficiales presentes a bordo fallecieron en el acto o perecieron atrapados sin posibilidad de evacuación... "
            "La investigación oficial de la corte naval reveló que la fatiga del personal... y el desvío de los pasos taxativos estipulados en los protocolos técnicos de armado... desencadenaron la ignición... "
            "El desastre del Sindhurakshak dejó una lección imperecedera para la gestión de explosivos industriales y militares... Las instrucciones paso a paso no son una guía sugerida... son mandatos inalterables... "
            "Porque ante sustancias detonantes... un solo milisegundo de desvío operativo... clausura cualquier posibilidad de retorno."
        )
    },
    {
        "id": "051",
        "fecha": "15 AGOSTO",
        "fechaPublicacion": "2026-08-15",
        "expediente": "Expediente #051",
        "carpeta": "2018-08-15-proyeccion-disco-amoladora-angular",
        "titular": "EL DISCO QUE SE VOLVIÓ METRALLA: LA AMOLADORA SIN GUARDA",
        "palabraResaltada": "AMOLADORA SIN GUARDA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Taller de Carpintería Metálica y Montaje - 2018",
        "tipoRiesgo": "Herramientas Portátiles / Proyección de Fragmentos a Alta Velocidad",
        "parrafos": [
            "El 15 de agosto de 2018, un operario metalúrgico sufrió heridas faciales devastadoras al desintegrarse el disco de una amoladora angular portátil de 115 milímetros.",
            "Para realizar un corte más profundo en una viga, el trabajador desmontó la guarda metálica protectora y colocó un disco de 180 milímetros diseñado para girar a 8.500 RPM, cuando la amoladora giraba a 11.000 RPM.",
            "La fuerza centrífuga sobrepasó la resistencia del aglomerado de resina, haciéndolo estallar en proyectiles a más de 300 km/h. La combinación de velocidad excesiva y falta de guarda facial resulta letal."
        ],
        "puntosClave": [
            {"icono": "shield", "titulo": "Guarda de seguridad inviolable", "texto": "Nunca retirar, rotar en sentido peligroso ni alterar la carcasa metálica protectora de fábrica de la amoladora."},
            {"icono": "gauge", "titulo": "Compatibilidad estricta de RPM", "texto": "Las revoluciones por minuto máximas del disco deben ser SIEMPRE iguales o mayores que las RPM en vacío de la herramienta."},
            {"icono": "eye", "titulo": "Protección facial integral obligatoria", "texto": "Usar pantalla facial completa de policarbonato además de gafas de seguridad para contener impactos de fragmentos balísticos."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: manuales de uso seguro de herramientas abrasivas de OSHA 1910.243 y normas internacionales de abrasivos aglomerados ANSI B7.1 / EN 12413.",
        "guionReel": (
            "¿Sabías a qué velocidad viajan los pedazos de un disco de amoladora cuando se parte?\n\n"
            "A más de 300 kilómetros por hora.\n\n"
            "El 15 de agosto de 2018, en un taller metalúrgico, un operario necesitaba hacer un corte profundo en un perfil de acero. Como el disco chico no alcanzaba, le quitó la guarda de protección a la amoladora y le clavó un disco mucho más grande.\n\n"
            "Cometió el error más básico de la mecánica: la amoladora chica giraba a 11.000 revoluciones por minuto, pero el disco grande solo resistía 8.500.\n\n"
            "Apenas encendió la máquina y tocó el metal, la fuerza centrífuga reventó el disco en decenas de esquirlas.\n\n"
            "Sin guarda protectora y usando solo anteojos comunes, un fragmento le partió la mandíbula y le causó pérdida de visión.\n\n"
            "Jamás quites la guarda metálica, revisa siempre las RPM del disco y usa máscara facial completa.\n\n"
            "Tu rostro no es un escudo."
        ),
        "promptImagen": (
            "Industrial safety documentary photo, metal fabrication workbench, shattered abrasive cutting grinding wheel disc exploded into sharp pieces. "
            "Handheld angle grinder lying on workbench with guard removed, heavy steel beams, blood-free shattered safety spectacles, clear polycarbonate face shield nearby, "
            "grinding sparks residue, high-detail macro photography, cinematic workshop lighting, 16:9 aspect ratio."
        ),
        "guionLargo": (
            "El quince de agosto de dos mil dieciocho... en un taller de carpintería metálica y montaje estructural... un acto común de imprudencia operativa culminó en una lesión traumática irreversible... "
            "Durante las tareas de fabricación de una estructura para techos... un soldador necesitaba seccionar un perfil de acero de doble pestaña... "
            "Al notar que el disco de corte convencional de ciento quince milímetros de su amoladora no alcanzaba la profundidad requerida... tomó una decisión extremadamente peligrosa... "
            "Desarmó y retiró por completo la guarda metálica semicircular provista por el fabricante de la herramienta... "
            "A continuación... montó un disco abrasivo de ciento ochenta milímetros... perteneciente a una máquina industrial de mayor porte... "
            "El operario ignoró la ley fundamental de las herramientas abrasivas rotativas... la relación de velocidad angular... "
            "Su pequeña amoladora angular giraba en vacío a más de once mil revoluciones por minuto... mientras que el disco de gran tamaño estaba diseñado para una velocidad de rotura periférica calculada a un máximo de ocho mil quinientas revoluciones... "
            "Para colmo... el trabajador solo llevaba puestas unas gafas plásticas de seguridad... prescindiendo de la pantalla facial completa... "
            "En el instante en que apoyó el filo del disco sobre la arista del perfil... las tensiones por cizallamiento y la descomunal fuerza centrífuga pulverizaron la matriz de fibra de vidrio y resina del abrasivo... "
            "El disco estalló como una granada de fragmentación... "
            "Múltiples trozos incandescentes salieron despedidos a una velocidad superior a los ochenta metros por segundo... más de trescientos kilómetros por hora... "
            "Uno de los fragmentos principales impactó de lleno en el rostro del trabajador... destrozando el maxilar superior y causándole un traumatismo ocular gravísimo con pérdida permanente de la visión... "
            "Las auditorías de seguridad en talleres recuerdan que la amoladora es una de las herramientas manuales más lesivas de la industria... "
            "La guarda metálica jamás debe retirarse bajo ningún pretexto... las revoluciones del disco deben ser siempre superiores a las de la máquina... y la careta facial de policarbonato es una barrera obligatoria e insustituible... "
            "Porque ante un disco girando a once mil vueltas... no existen los reflejos humanos capaces de esquivar la metralla."
        )
    },
    {
        "id": "052",
        "fecha": "16 AGOSTO",
        "fechaPublicacion": "2026-08-16",
        "expediente": "Expediente #052",
        "carpeta": "2014-08-16-intoxicacion-acido-sulfhidrico-lodos",
        "titular": "EL ASESINO SILENCIOSO DEL LODO: LA TRAMPA DEL SULFHÍDRICO",
        "palabraResaltada": "TRAMPA DEL SULFHÍDRICO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta de Tratamiento de Efluentes Industriales - 2014",
        "tipoRiesgo": "Riesgo Químico / Espacios Confinados y Ácido Sulfhídrico (H₂S)",
        "parrafos": [
            "El 16 de agosto de 2014, dos operarios fallecieron en una planta de tratamiento de efluentes al ingresar a una pileta de lodos biológicos para desobstruir una válvula de fondo.",
            "Al remover los sedimentos con una pala, liberaron bolsas de gas ácido sulfhídrico (H2S) atrapadas por digestión anaeróbica. El primer trabajador se desplomó en segundos al superar los 500 PPM.",
            "El segundo intentó rescatarlo sin equipo autónomo cayendo inconsciente de inmediato (efecto knock-down). La trampa del H2S: a concentraciones letales duerme el olfato, simulando que el peligro desapareció."
        ],
        "puntosClave": [
            {"icono": "wind", "titulo": "La trampa de la fatiga olfativa", "texto": "Por encima de 50 PPM, el H2S paraliza los nervios olfatorios; jamás confiar en el olor a huevo podrido para juzgar la seguridad."},
            {"icono": "radio", "titulo": "Detector de 4 gases personal obligatorio", "texto": "Monitoreo continuo en la solapa con alarma sonora y vibratoria calibrada para H2S a 10 y 15 PPM."},
            {"icono": "shield-alert", "titulo": "Prohibido rescates sin equipo ERA", "texto": "Más del 60% de las víctimas por gases en espacios confinados son compañeros que ingresan a rescatar sin protección autónoma."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: guías técnicas sobre riesgos de ácido sulfhídrico de OSHA (Safety and Health Topics: Hydrogen Sulfide) y normas de espacios confinados ANSI/ASSP Z117.1.",
        "guionReel": (
            "¿Sabías que el gas más traicionero de la industria química te hace creer que ya no está presente justo antes de matarte?\n\n"
            "El 16 de agosto de 2014, en una planta de efluentes, dos operarios debían destrabar una válvula en una fosa de lodos.\n\n"
            "Al mover el fango con una barra, liberaron ácido sulfhídrico concentrado. Al principio sintieron olor a huevo podrido, pero a los diez segundos ya no olían nada.\n\n"
            "Creyeron que el gas se había disipado... pero es la fatiga olfativa: el sulfhídrico destruye los receptores de tu nariz para que no puedas olerlo.\n\n"
            "El primer trabajador cayó desplomado en el acto. El segundo bajó desesperado a salvar a su amigo sin máscara de oxígeno... y cayó muerto encima de él.\n\n"
            "El ácido sulfhídrico te apaga en una sola respiración. Sin detector multigás y sin equipo autónomo, jamás bajes a una fosa.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Industrial wastewater treatment plant documentary photography, dark open concrete sludge pit basin filled with biological sediment. "
            "Warning sign prominent saying Danger Hydrogen Sulfide H2S Gas, safety harness and lifeline hanging into the pit edge, "
            "portable 4-gas atmospheric detector clipped to railing with flashing red warning LED, overcast gloomy industrial atmosphere, 16:9 ratio."
        ),
        "guionLargo": (
            "El dieciséis de agosto de dos mil catorce... en el sector de decantación y tratamiento de efluentes de un complejo fabril... la falta de percepción del riesgo desencadenó una tragedia doble por inhalación tóxica... "
            "Una fosa de hormigón de cuatro metros de profundidad... destinada a la acumulación de lodos orgánicos residuales... presentaba una obstrucción mecánica en la compuerta de drenaje inferior... "
            "Dos trabajadores de mantenimiento fueron encomendados para descender por una escalera marinera fija con el fin de liberar el fango acumulado... "
            "El equipo no emitió un permiso de ingreso a espacios confinados... no instaló mangas de ventilación forzada... y ninguno de los dos llevaba prendido en su pechera un detector portátil de cuatro gases... "
            "En el fondo de la pileta... la descomposición bacteriana en condiciones anaeróbicas había generado concentraciones masivas de ácido sulfhídrico... un gas incoloro, inflamable y extremadamente letal... más denso que el aire... "
            "Al introducir una barra metálica para revolver el sedimento... los operarios fracturaron las bolsas de gas comprimidas en el lodo... "
            "Al principio... el ambiente se impregnó de un penetrante hedor característico a huevos podridos... "
            "Sin embargo... a los pocos segundos el olor pareció esfumarse por completo... "
            "Esa es la trampa mortal del sulfhídrico... Al superar las cincuenta partes por millón... el gas paraliza de forma instantánea el nervio olfatorio humano... induciendo a la víctima a creer falsamente que el gas se ha ventilado... "
            "Cuando la concentración superó las quinientas partes por millón... el primer operario sufrió el temido efecto knock-down... un colapso neurológico fulminante que lo dejó inconsciente en el fango... "
            "Su compañero... presa del instinto heroico de rescate... descendió inmediatamente hacia el fondo sin colocarse un equipo de respiración autónoma... "
            "Bastó una sola inhalación profunda para que él también perdiera el conocimiento... falleciendo ambos minutos después por asfixia celular aguda... "
            "Las estadísticas globales de higiene laboral demuestran que más de la mitad de las muertes en recintos confinados corresponden a rescatistas no equipados... "
            "Frente al ácido sulfhídrico... la nariz es el peor detector posible... "
            "El ingreso a fosas de lodos exige invariablemente medición instrumental continua... ventilación extractiva... arnés con línea de rescate conectada a trípode exterior... y la certeza absoluta de que ante una emergencia... nadie entra sin protección respiratoria autónoma."
        )
    }
]

def procesar_lote_4(kokoro_instance):
    procesadas = []

    print(f"\n=======================================================")
    print(f"Iniciando procesamiento de {len(LOTE_4_DATA)} historias del Lote 4 (#043 a #052)")
    print(f"=======================================================\n")

    for h in LOTE_4_DATA:
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
            crear_portada_grafica_lote4(h, portada_path)
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

def crear_portada_grafica_lote4(historia, output_path):
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
    """Inyecta las historias del Lote 4 en index.html antes del cierre del array historias."""
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

    print("\n✓ index.html actualizado exitosamente con los 10 nuevos expedientes (#043 a #052).")
    return True

def main():
    print("Iniciando motor Kokoro para Lote 4 (#043 a #052)...")
    kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

    procesadas = procesar_lote_4(kokoro)

    if inyectar_en_index_html(procesadas):
        print(f"\n🎉 ¡LOTE 4 COMPLETADO AL 100%! ({len(procesadas)} historias procesadas)")

if __name__ == "__main__":
    main()
