# -*- coding: utf-8 -*-
"""
Generador Agéntico Automatizado para Lote 6: Expedientes #063 a #072 (27 de agosto al 5 de septiembre)
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

LOTE_6_DATA = [
    {
        "id": "063",
        "fecha": "27 AGOSTO",
        "fechaPublicacion": "2026-08-27",
        "expediente": "Expediente #063",
        "carpeta": "1955-08-27-explosion-refineria-standard-oil-whiting",
        "titular": "EL REACTOR QUE VOLÓ COMO UN COHETE: STANDARD OIL WHITING",
        "palabraResaltada": "STANDARD OIL WHITING",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Refinería Standard Oil, Whiting, Indiana, EE.UU. - 1955",
        "tipoRiesgo": "Seguridad de Procesos (PSM) / Puesta en Marcha (Startup)",
        "parrafos": [
            "El 27 de agosto de 1955, la rotura catastrófica de un hidroformador catalítico de 80 metros de altura en la refinería Standard Oil de Whiting desató un incendio colosal que destruyó 70 tanques de crudo.",
            "Durante la presurización de arranque tras un mantenimiento, ingresó aire indeseado a la mezcla con nafta recirculada a 30 bares. La detonación fragmentó la torre proyectando piezas de 60 toneladas a 400 metros.",
            "El desastre transformó la ingeniería de procesos: purgas rigurosas con gas inerte antes de poner en marcha, distancias de seguridad entre unidades y contención en parques de tanques."
        ],
        "puntosClave": [
            {"icono": "refresh-cw", "titulo": "Purga e inertización pre-arranque", "texto": "Eliminar el 100% del oxígeno con nitrógeno antes de introducir hidrocarburos en cualquier circuito de alta presión."},
            {"icono": "layers", "titulo": "Distancias de separación entre unidades", "texto": "Separar físicamente los reactores de proceso de los parques de almacenamiento de hidrocarburos a granel."},
            {"icono": "shield-check", "titulo": "Procedimientos de arranque (PSSR)", "texto": "Revisión pre-arranque estricta donde cada paso de presurización requiera verificación analítica de atmósfera."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: registros históricos de investigación de incidentes mayores del American Petroleum Institute (API) y National Fire Protection Association (NFPA).",
        "guionReel": (
            "¿Sabías que una torre de refinería de 26 pisos puede partirse en pedazos y volar como un misil?\n\n"
            "El 27 de agosto de 1955, en la refinería Whiting en Indiana, estaban arrancando un reactor de hidroformado después de una parada técnica.\n\n"
            "Para ahorrar tiempo en la purga, no barrieron todo el aire del sistema. Cuando empezaron a meter gas a alta presión, el oxígeno formó una mezcla explosiva perfecta con los hidrocarburos calientes.\n\n"
            "La torre estalló como una bomba atómica. Pedazos de acero de sesenta toneladas volaron a cuatro cuadras de distancia, aplastando casas e incendiando setenta tanques gigantescos de petróleo.\n\n"
            "El fuego ardió durante ocho días seguidos.\n\n"
            "En puesta en marcha de procesos químicos, jamás arranques sin garantizar atmósfera inerte con nitrógeno.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Historical industrial documentary photography, August 27 1955 Whiting Indiana Standard Oil refinery catastrophic explosion. "
            "Giant shattered industrial catalytic reforming tower torn into massive jagged steel fragments, towering inferno and thick rolling black smoke covering horizon, "
            "rows of crushed and burning cylindrical oil storage tanks, vintage 1950s fire trucks spraying foam deluges, photorealistic archival style, 16:9 ratio."
        ),
        "guionLargo": (
            "El veintisiete de agosto de mil novecientos cincuenta y cinco... a las seis y doce de la mañana... la ciudad de Whiting en el estado de Indiana... fue sacudida por una explosión cuya onda expansiva quebró vidrios a más de cincuenta kilómetros a la redonda... "
            "En la histórica refinería de la Standard Oil... una de las plantas petroleras más avanzadas de la época... los técnicos se encontraban en plena maniobra de arranque de una flamante unidad de hidroformado catalítico... "
            "El reactor principal... una imponente mole de acero de más de ochenta metros de altura y paredes metálicas de cinco centímetros de espesor... contenía valiosos catalizadores de platino diseñados para elevar el octanaje de la nafta pesada... "
            "Durante las horas previas de presurización... un procedimiento deficiente de purga no logró desalojar el aire remanente de los circuitos de recirculación... "
            "Cuando los operadores introdujeron nafta caliente vaporizada y gas de reciclaje a más de treinta atmósferas de presión... el oxígeno atrapado en el sistema generó de forma instantánea una mezcla dentro de los límites de detonación... "
            "Una ignición interna imprevista provocó una onda de detonación supersónica que pulverizó la torre desde adentro... "
            "La gigantesca columna de acero colapsó desmembrada en más de una decena de secciones masivas... arrojando fragmentos de sesenta toneladas a más de cuatrocientos metros de distancia... como si fueran esquirlas de metralla... "
            "Uno de los trozos metálicos cayó sobre un vecindario adyacente destruyendo varias viviendas... mientras que otros proyectiles impactaron directamente sobre las cubiertas flotantes del parque de tanques contiguo... "
            "En cuestión de minutos... setenta tanques gigantescos de petróleo crudo y gasolina entraron en ignición encadenada... desatando una tormenta de fuego que tardó ocho días enteros en ser sofocada... "
            "La catástrofe de Whiting cambió para siempre la seguridad de procesos en la industria petroquímica... "
            "Estableció la obligatoriedad de realizar purgas analíticamente certificadas con nitrógeno puro antes de admitir hidrocarburos... y obligó a rediseñar los planos de las refinerías modernas... imponiendo distancias de seguridad infranqueables entre reactores y zonas de almacenamiento... "
            "Porque en el arranque de una planta... la prisa es el combustible más peligroso."
        )
    },
    {
        "id": "064",
        "fecha": "28 AGOSTO",
        "fechaPublicacion": "2026-08-28",
        "expediente": "Expediente #064",
        "carpeta": "2008-08-28-explosion-bayer-cropscience-institute",
        "titular": "EL TANQUE DE METOMILO QUE ESTALLÓ: BYPASS EN BAYER",
        "palabraResaltada": "BYPASS EN BAYER",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Química Bayer CropScience, Institute, Virginia Occidental - 2008",
        "tipoRiesgo": "Seguridad de Procesos (PSM) / Reacción Fuera de Control",
        "parrafos": [
            "El 28 de agosto de 2008, un reactor de tratamiento de residuos de pesticidas explotó violentamente en la planta química de Bayer CropScience en Institute, matando a dos operarios y dañando la unidad.",
            "Durante el arranque de un nuevo sistema de control digital, los operadores deshabilitaron los enclavamientos de seguridad críticos (bypasses) y cargaron solventes en un orden incorrecto sin capacitación previa.",
            "La descomposición exotérmica fuera de control generó una sobrepresión masiva que reventó el tanque de metomilo. Los fragmentos casi impactan un depósito contiguo con 18 toneladas de isocianato de metilo (MIC).",
        ],
        "puntosClave": [
            {"icono": "ban", "titulo": "Prohibido anular enclavamientos de seguridad", "texto": "Los interlocks y paradas de emergencia automatizadas jamás deben puentearse para acelerar una puesta en marcha."},
            {"icono": "git-pull-request", "titulo": "Gestión del cambio (MOC) en sistemas de control", "texto": "Toda migración o actualización a sistemas DCS exige capacitación formal y validación rigurosa de alarmas antes del arranque."},
            {"icono": "shield-alert", "titulo": "Revisión de seguridad pre-arranque (PSSR)", "texto": "Confirmar en campo que todos los sistemas de enfriamiento, venteo y dosificación operen nominalmente antes de cargar reactivos."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe final de investigación de la Junta de Seguridad Química de EE.UU. (CSB Report No. 2008-08-I-WV) sobre la explosión en Bayer CropScience.",
        "guionReel": (
            "¿Sabías que puentear un sistema de alarma en una planta química puede estar a centímetros de causar un desastre mundial?\n\n"
            "El 28 de agosto de 2008, en la planta de Bayer CropScience en Virginia Occidental, estaban probando un sistema de control digital nuevo para fabricar pesticidas.\n\n"
            "Como las alarmas no paraban de sonar y los retrasaban, los supervisores decidieron anular los bloqueos de seguridad automáticos y cargar los químicos manualmente.\n\n"
            "Cargaron el solvente a la temperatura equivocada. Se desató una reacción química en cadena fuera de control y el tanque de residuos estalló como una bomba, matando a dos trabajadores.\n\n"
            "Un pedazo gigante de acero voló y cayó a pocos metros de un tanque que guardaba dieciocho toneladas de isocianato de metilo, el mismo gas venenoso de Bhopal.\n\n"
            "Jamás anules un enclavamiento de seguridad. Si el sistema dice alto, es alto.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Chemical plant industrial explosion documentary photography, August 28 2008 Bayer CropScience facility in Institute West Virginia. "
            "Ruptured chemical waste treator vessel peeled open like peeled metal, scattered control room debris, emergency chemical wash monitors spraying deluge, "
            "industrial high-pressure piping severed, prominent chemical storage sphere tanks in background shrouded in smoke, photorealistic, 16:9 ratio."
        ),
        "guionLargo": (
            "El veintiocho de agosto de dos mil ocho... a las diez y treinta y cinco de la noche... una violenta detonación química sacudió el valle del río Kanawha en Institute, Virginia Occidental... "
            "En el complejo petroquímico de la empresa Bayer CropScience... se desarrollaban las maniobras de puesta en marcha de la unidad de síntesis de metomilo... un potente insecticida carbamato... "
            "La empresa acababa de instalar un moderno sistema de control digital distribuido para reemplazar los antiguos paneles neumáticos... "
            "Sin embargo... la capacitación del personal de sala de control sobre las nuevas pantallas y variables del proceso había sido superficial y apresurada... "
            "Durante las pruebas preliminares... los sensores de temperatura y nivel generaban lecturas discordantes... lo que provocaba que el sistema automático bloqueara reiteradamente el avance del arranque... "
            "Con el fin de evitar más demoras operativas... la supervisión autorizó una decisión fatal... puentear y deshabilitar los enclavamientos electrónicos de seguridad... conocidos en la jerga de procesos como bypasses... "
            "Los operadores comenzaron a transferir solventes y residuos concentrados de metomilo al tanque digestor... sin que el sistema pudiera regular la adición de líquido de enfriamiento ni verificar las concentraciones críticas... "
            "A una temperatura superior a los ciento treinta grados... el metomilo residual comenzó a descomponerse de manera térmica y descontrolada... "
            "La reacción exotérmica secundaria liberó calor y vapores a una velocidad exponencial que sobrepasó con creces la capacidad de alivio del disco de ruptura del recipiente... "
            "El tanque estalló en mil pedazos... arrancando vigas de hormigón y matando en el acto a dos trabajadores de la planta... "
            "La investigación posterior de la Junta de Seguridad Química reveló un hecho escalofriante... Uno de los fragmentos principales del tanque... de varias toneladas de peso... aterrizó a escasos metros de un depósito que almacenaba dieciocho toneladas de isocianato de metilo... la misma sustancia letal responsable de la catástrofe de Bhopal... "
            "El informe de la CSB concluyó que los enclavamientos de seguridad no son obstáculos operativos... son las últimas barreras de defensa contra la muerte... "
            "Ninguna puesta en marcha puede justificarse si los operadores no comprenden a fondo el sistema... y puentear un interlock sin un riguroso análisis de gestión del cambio... es jugar a la ruleta rusa con la planta entera."
        )
    },
    {
        "id": "065",
        "fecha": "29 AGOSTO",
        "fechaPublicacion": "2026-08-29",
        "expediente": "Expediente #065",
        "carpeta": "2018-08-29-atrapamiento-torno-paralelo-taller",
        "titular": "LA TELA EN EL TORNO: EL ATRAPAMIENTO EN EL HUSILLO",
        "palabraResaltada": "TELA EN EL TORNO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Taller Mecánico de Mecanizado y Matricería - 2018",
        "tipoRiesgo": "Atrapamiento / Protección de Máquinas Rotativas",
        "parrafos": [
            "El 29 de agosto de 2018, un tornero experimentado de 48 años falleció en el acto tras quedar atrapado por el plato giratorio de un torno paralelo convencional en un taller de mecanizado.",
            "El trabajador sostenía una tira de tela esmeril con ambas manos directamente sobre una barra de acero que giraba a 800 RPM para pulirla. Llevaba guantes de hilo y una camisa de mangas largas sin abotonar.",
            "La tela se trabó en una rebaba enrollando instantáneamente el guante y arrastrando al operario contra el husillo. Máquinas con ejes expuestos exigen ropa ceñida y prohibición absoluta de guantes.",
        ],
        "puntosClave": [
            {"icono": "ban", "titulo": "Prohibido guantes cerca de ejes rotativos", "texto": "Nunca utilizar guantes, anillos, cadenas ni ropa holgada al operar tornos, fresadoras o taladros de banco."},
            {"icono": "tool", "titulo": "Uso de soportes mecánicos para lijado", "texto": "Prohibido aplicar tela esmeril con las manos desnudas; emplear un mango de madera porta-lija apoyado sobre el carro."},
            {"icono": "shield", "titulo": "Pantalla protectora con microinterruptor", "texto": "Instalar resguardo basculante de policarbonato sobre el plato del torno con enclavamiento que impida el giro si está abierta."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: alertas de seguridad en tornos convencionales del Health and Safety Executive (HSE UK) y normas de protección de máquinas OSHA 1910.212.",
        "guionReel": (
            "¿Por qué un simple par de guantes de trabajo puede matarte frente a un torno?\n\n"
            "El 29 de agosto de 2018, en un taller metalúrgico, un tornero con veinte años de experiencia estaba puliendo una barra de acero.\n\n"
            "El torno giraba a 800 revoluciones por minuto. El operario tomó una tira de lija con las dos manos y la apretó contra la pieza en movimiento. Llevaba guantes de tela y mangas sueltas.\n\n"
            "Una pequeña rebaba de acero enganchó la lija. En una décima de segundo, la tracción arrastró el guante, la tela de la camisa y al tornero completo hacia el plato giratorio.\n\n"
            "El motor de cinco caballos no se frenó y el hombre murió aplastado en el acto.\n\n"
            "Frente a máquinas rotativas, los guantes y la ropa suelta están estrictamente prohibidos. El pulido manual se hace siempre con soporte mecánico.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Documentary metal machine shop photography, heavy conventional parallel metal lathe with three-jaw chuck stopped. "
            "Torn work glove and strip of emery cloth snagged on steel workpiece clamped in chuck, foot emergency stop brake bar along base, "
            "transparent polycarbonate chuck safety shield leaning raised, brass and steel turnings on chip pan tray, realistic gritty lighting, 16:9 ratio."
        ),
        "guionLargo": (
            "El veintinueve de agosto de dos mil dieciocho... en un concurrido taller de mecanizado y ajuste de piezas industriales... una práctica considerada habitual por generaciones de mecánicos cobró una vida de forma instantánea... "
            "Un tornero de cuarenta y ocho años... reconocido entre sus pares por su pericia en el torneado de precisión... finalizaba el dimensionamiento de un eje cilíndrico de acero aleado... "
            "Para lograr el acabado superficial especificado en el plano... el operario se dispuso a realizar el pulido final de la pieza... "
            "En lugar de montar una herramienta porta-lija fijada al carro transversal... o utilizar una tablilla de madera auxiliar para presionar el abrasivo desde una distancia segura... decidió aplicar el método manual directo... "
            "Tomó una tira de tela esmeril de grano fino con ambas manos... la envolvió parcialmente alrededor del eje metálico... y accionó la palanca de marcha del torno... haciendo girar la pieza a más de ochocientas revoluciones por minuto... "
            "El trabajador llevaba colocados guantes de tejido de algodón con motas de goma... y una camisa de trabajo con los puños desabotonados... "
            "En la dinámica del mecanizado... el contacto entre una tela abrasiva flexible y una superficie rotativa con microporosidades o virutas residuales representa un peligro letal... "
            "Una pequeña rebaba de acero mordió la tira de lija... trabándola en una fracción de milisegundo... "
            "La inmensa fuerza de torsión del husillo principal arrastró la lija... enrollando el guante textil y el puño de la camisa del operario con la velocidad de un relámpago... "
            "El cuerpo del trabajador fue succionado violentamente contra el plato de tres mordazas giratorio... sin que tuviera tiempo de presionar la barra perimetral de freno de pie... "
            "El impacto demoledor contra la bancada de fundición le provocó la muerte instantánea por politraumatismos severos... "
            "Las investigaciones laborales recordaron una regla de oro que jamás debe quebrantarse... Frente a máquinas herramientas con mecanismos giratorios expuestos... el uso de guantes, bufandas, anillos o mangas holgadas está estrictamente prohibido... "
            "El pulido manual con tela esmeril a mano alzada es una maniobra vedada por las normas internacionales... "
            "Porque ante la potencia implacable de un torno... un simple hilo de tela es suficiente para arrastrar una vida entera."
        )
    },
    {
        "id": "066",
        "fecha": "30 AGOSTO",
        "fechaPublicacion": "2026-08-30",
        "expediente": "Expediente #066",
        "carpeta": "2017-08-30-derrumbe-pared-demolicion-obra",
        "titular": "EL SOCAVAMIENTO DEL MURO: EL COLAPSO EN LA DEMOLICIÓN",
        "palabraResaltada": "SOCAVAMIENTO DEL MURO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Obra Urbana de Demolición y Remodelación - 2017",
        "tipoRiesgo": "Derrumbe / Demolición y Estabilidad Estructural",
        "parrafos": [
            "El 30 de agosto de 2017, dos obreros quedaron sepultados tras el derrumbe imprevisto de una pared medianera de ladrillos de cuatro metros de altura durante la demolición de una casona antigua.",
            "Para derribar el muro más rápido, los trabajadores picaron la base con martillos neumáticos intentando voltearlo de un solo golpe. El socavamiento desestabilizó el centro de gravedad colapsando sobre ellos.",
            "No existía apuntalamiento diagonal ni estudio de cargas compartidas con el edificio vecino. La regla de oro en demolición: demoler siempre de arriba hacia abajo, hilada por hilada.",
        ],
        "puntosClave": [
            {"icono": "arrow-down", "titulo": "Demolición descendente obligatoria", "texto": "Demoler estrictamente de arriba hacia abajo, piso por piso y tramo por tramo; jamás socavar las bases de una pared."},
            {"icono": "shield", "titulo": "Apuntalamiento previo de estructuras linderas", "texto": "Instalar puntales telescópicos y arriostramientos diagonales antes de intervenir muros medianeros compartidos."},
            {"icono": "file-text", "titulo": "Plan de demolición firmado por calculista", "texto": "Toda demolición exige memoria técnica que evalúe la vejez de los morteros, sobrecargas y método seguro de volteo."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: normativas de seguridad en trabajos de demolición de OSHA 1926.850 y guías del Instituto Nacional de Seguridad y Salud en el Trabajo (INSST).",
        "guionReel": (
            "¿Por qué picar la base de una pared para tirarla más rápido es una trampa mortal?\n\n"
            "El 30 de agosto de 2017, en una obra de remodelación urbana, dos albañiles debían tirar abajo una pared medianera de doce metros de largo y cuatro metros de alto.\n\n"
            "Para no subir a los andamios y desarmarla ladrillo por ladrillo, hicieron lo que muchos hacen por atajo: picaron toda la base con rotomartillos para que la pared cayera sola hacia adelante.\n\n"
            "Pero los morteros viejos de cal no avisan. Al debilitarse los apoyos, la enorme pared de diez toneladas no cayó hacia donde ellos querían: se partió al medio y colapsó verticalmente aplastándolos.\n\n"
            "Uno murió y el otro sobrevivió con lesiones permanentes.\n\n"
            "En demolición la regla es sagrada: siempre se demuele de arriba hacia abajo, hilada por hilada, y con apuntalamiento firme.\n\n"
            "La gravedad no negocia."
        ),
        "promptImagen": (
            "Urban construction demolition accident documentary photography, partially collapsed ancient brick masonry party wall inside urban renovation site. "
            "Piles of shattered historic clay bricks and pulverized mortar dust on ground, yellow electric demolition jackhammer crushed under fallen rubble, "
            "diagonal heavy steel shoring props propping remaining unstable wall sections, overcast city daylight, realistic photojournalism, 16:9 ratio."
        ),
        "guionLargo": (
            "El treinta de agosto de dos mil diecisiete... en una transitada arteria de un casco histórico urbano... una imprudencia metodológica en una obra de demolición terminó en un desenlace fatal... "
            "Una empresa constructora ejecutaba la reforma integral de una casona de principios del siglo veinte... con el fin de levantar un moderno edificio de oficinas... "
            "La tarea del día consistía en la demolición de una pesada pared medianera de ladrillos comunes... de cuatro metros de altura, treinta centímetros de espesor y doce metros de longitud... "
            "Para evitar el tiempo que demandaba armar un andamio de fachada e ir desmontando la estructura hilada por hilada desde la corona superior... los operarios decidieron emplear un método sumamente peligroso... conocido como socavamiento por cizalle inferior... "
            "Equipados con martillos electroneumáticos pesados... comenzaron a demoler y retirar los ladrillos de la franja inferior... a medio metro del suelo... con la intención de que el muro perdiera sustentación y cayera por gravedad hacia el terreno baldío... "
            "Omitieron colocar puntales telescópicos de apuntalamiento diagonal... y no realizaron una inspección estructural previa para evaluar el estado del mortero de cal y arena... el cual se encontraba degradado por décadas de humedad ascendente... "
            "Cuando la perforación de la base alcanzó los dos tercios del largo total de la pared... la distribución de cargas del macizo se alteró de manera catastrófica... "
            "En lugar de desplomarse hacia el frente en una sola pieza... el muro sufrió una fractura por flexión interna en el plano medio... "
            "Más de diez toneladas de mampostería colapsaron bruscamente hacia el interior de la excavación... donde se encontraban los dos albañiles accionando las herramientas... "
            "La masa de escombros los sepultó en una fracción de segundo... provocando el fallecimiento por aplastamiento de uno de los operarios y politraumatismos gravísimos en su compañero... "
            "Las investigaciones técnicas de siniestros en la construcción son unánimes... El socavamiento o zapado de muros en demoliciones está terminantemente vedado por las normas internacionales... "
            "La demolición debe ejecutarse invariablemente en sentido descendente... piso por piso... retirando primero las cargas superiores y apuntalando de forma continua las estructuras linderas... "
            "Porque ante toneladas de ladrillo debilitado... la gravedad nunca perdona los atajos."
        )
    },
    {
        "id": "067",
        "fecha": "31 AGOSTO",
        "fechaPublicacion": "2026-08-31",
        "expediente": "Expediente #067",
        "carpeta": "2016-08-31-intoxicacion-fosfina-fumigacion-granos",
        "titular": "EL GAS INVISIBLE DEL SILO: LA INTOXICACIÓN POR FOSFINA",
        "palabraResaltada": "FOSFINA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Terminal de Acopio de Granos y Depósito Portuario - 2016",
        "tipoRiesgo": "Higiene Industrial / Riesgo Químico y Fumigación",
        "parrafos": [
            "El 31 de agosto de 2016, dos operarios de una planta de acopio sufrieron intoxicación aguda por gas fosfina ($PH_3$) al retirar las lonas de una celda de granos tratada con pastillas de fosfuro de aluminio.",
            "Ingresaron al recinto confinado 24 horas antes de finalizar el plazo de cuarentena química estipulado y sin realizar mediciones con tubos colorimétricos ni usar equipos de respiración autónoma.",
            "El gas fosfina es incoloro, altamente tóxico y bloquea la respiración celular causando edema pulmonar fulminante. La lección: señalización estricta de cuarentena y medición de 0 PPM antes del reingreso.",
        ],
        "puntosClave": [
            {"icono": "clock", "titulo": "Respetar tiempos de exposición y ventilación", "texto": "Cumplir rigurosamente el período de cuarentena de la fumigación antes de autorizar la apertura o manipulación de lonas."},
            {"icono": "activity", "titulo": "Medición instrumental previa obligatoria", "texto": "Monitorear la concentración de fosfina con tubos colorimétricos o detectores fotoionizadores hasta constatar valores seguros (<0.05 PPM)."},
            {"icono": "shield", "titulo": "Protección respiratoria autónoma (ERA)", "texto": "Prohibido ingresar a recintos en proceso de aireación con barbijos comunes; exigir equipos de respiración autónoma o línea de aire."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: criterios de manejo seguro de fosfuro de aluminio de la EPA y normativas de higiene ocupacional en fumigación de granos OSHA 1910.1000.",
        "guionReel": (
            "¿Sabías que una simple pastilla para desinfectar granos genera un gas que puede matarte con solo respirarlo una vez?\n\n"
            "El 31 de agosto de 2016, en un galpón de acopio de trigo, dos trabajadores debían preparar un envío urgente de cereal.\n\n"
            "El grano había sido fumigado con fosfuro de aluminio y tapado con lonas plásticas herméticas. El cartel decía claro: no abrir antes de 72 horas.\n\n"
            "Pero como el camión esperaba afuera, se adelantaron 24 horas. Levantaron la lona sin barbijo especial y sin medir gases.\n\n"
            "El fosfuro reacciona con la humedad del aire y crea fosfina: un gas mortal que huele a pescado podrido y destruye los pulmones al instante.\n\n"
            "Los dos cayeron con náuseas violentas, asfixia y edema pulmonar agudo. Uno no logró sobrevivir.\n\n"
            "En fumigaciones agrícolas, la cuarentena química se respeta a rajatabla y no se entra sin medir cero partes por millón.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Industrial agricultural grain terminal documentary photography, massive interior warehouse flat grain storage covered in dark heavy tarpaulins. "
            "Warning skull and crossbones chemical fumigation sign posted on railing saying Danger Phosphine Gas Do Not Enter, "
            "discarded gas detection sampling pump tubes on concrete floor, full-face respirator with specialized chemical canister sitting on crate, 16:9 ratio."
        ),
        "guionLargo": (
            "El treinta y uno de agosto de dos mil dieciséis... en una terminal de acopio y acondicionamiento de granos de una región agroindustrial... la urgencia por acelerar un despacho comercial desencadenó una tragedia por intoxicación química... "
            "Una celda de almacenamiento que contenía más de tres mil toneladas de trigo había sido sometida a un tratamiento de fumigación curativa contra gorgojos y plagas... empleando pastillas de fosfuro de aluminio... "
            "El fosfuro de aluminio es un compuesto sólido que... al entrar en contacto con la humedad ambiental y la temperatura de los granos... reacciona químicamente liberando gas fosfina o fosfuro de hidrógeno... "
            "La fosfina es un gas incoloro, inflamable y extremadamente venenoso... clasificado con una toxicidad comparable a la del ácido cianhídrico... capaz de inhibir las enzimas respiratorias celulares y provocar colapso cardiovascular y edema pulmonar masivo a concentraciones ínfimas... "
            "El protocolo técnico del producto exigía un período mínimo de encarpado hermético de cinco días... seguido de cuarenta y ocho horas de ventilación forzada... "
            "Sin embargo... ante la llegada anticipada de una formación ferroviaria de tolvas de carga... el encargado del depósito ordenó a dos operarios retirar las lonas plásticas veinticuatro horas antes de que venciera el plazo de cuarentena... "
            "Los trabajadores ingresaron a la celda provistos únicamente de barbijos descartables comunes contra polvo... absolutamente inútiles para retener moléculas de gas... "
            "Al destapar las primeras mantas... una bolsa concentrada de fosfina atrapada en el seno del grano se liberó hacia el pasillo de tránsito... "
            "Un penetrante olor a carburo y pescado descompuesto inundó el ambiente... "
            "A los pocos segundos... ambos trabajadores comenzaron a padecer mareos intensos... vómitos violentos, opresión en el pecho y convulsiones... "
            "A pesar de los esfuerzos médicos de emergencia... uno de ellos falleció a las pocas horas por falla respiratoria refractaria... mientras que su compañero permaneció semanas en terapia intensiva... "
            "Las investigaciones de salud ocupacional agrícola ratificaron que el reingreso a recintos fumigados no admite excepciones... "
            "Exige el cumplimiento irrestricto de los tiempos de aireación... la medición analítica con tubos colorimétricos hasta confirmar concentraciones menores a cero punto cero cinco partes por millón... y el uso de equipos de respiración autónoma... "
            "Porque en el manejo de plaguicidas... la química es inflexible ante las prisas comerciales."
        )
    },
    {
        "id": "068",
        "fecha": "01 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-01",
        "expediente": "Expediente #068",
        "carpeta": "1992-09-01-explosion-refineria-la-mede-dead-legs",
        "titular": "EL TRAMO MUERTO EN LA TUBERÍA: LA EXPLOSIÓN DE LA MEDE",
        "palabraResaltada": "TRAMPO MUERTO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Complejo Petroquímico y Refinería de La Mède, Francia - 1992",
        "tipoRiesgo": "Seguridad de Procesos (Oil & Gas) / Integridad Mecánica (Dead Legs)",
        "parrafos": [
            "El 1 de septiembre de 1992, una explosión devastadora en la unidad de craqueo catalítico de la refinería de La Mède en Francia dejó 6 trabajadores fallecidos y pérdidas multimillonarias.",
            "Una tubería de derivación (bypass) de 8 pulgadas que permanecía fuera de servicio activo se rompió repentinamente por corrosión localizada bajo tensiones mecánicas. El espesor del acero se había reducido drásticamente sin ser detectado.",
            "La fuga liberó una inmensa nube de gas hidrocarburo a 40 bares que detonó al instante. El accidente creó conciencia mundial sobre la gestión de tramos ciegos o muertos (dead legs) en tuberías críticas.",
        ],
        "puntosClave": [
            {"icono": "search", "titulo": "Inspección de tramos muertos (Dead legs)", "texto": "Identificar y mapear todas las ramas cerradas y líneas de bypass donde se acumulan condensados corrosivos y agua."},
            {"icono": "gauge", "titulo": "Medición de espesores por ultrasonido 100%", "texto": "Monitorear periódicamente los codos y fondos de líneas inactivas según normativas API 570 de tuberías de proceso."},
            {"icono": "scissors", "titulo": "Eliminación física de tuberías en desuso", "texto": "Retirar y cegar mecánicamente con discos ciegos los tramos de cañería que ya no cumplen función operativa en la planta."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de investigación del Ministerio de Medio Ambiente de Francia (ARIA No. 3855) y normas de inspección de tuberías petroquímicas API 570.",
        "guionReel": (
            "¿Sabías que una cañería cerrada que no se usa puede ser la parte más peligrosa de toda una refinería?\n\n"
            "El 1 de septiembre de 1992, en la refinería de La Mède en Francia, una explosión colosal destruyó la unidad de craqueo catalítico y mató a seis operarios.\n\n"
            "¿Qué falló? No fue un reactor gigante: fue un pedazo de caño secundario de bypass que estaba cerrado con una válvula desde hacía meses.\n\n"
            "En la industria los llaman tramos muertos o dead legs. Como el gas no circula, el agua y los ácidos se quedan estancados en el fondo, corroyendo el metal por dentro como una carcoma invisible.\n\n"
            "La pared de acero se adelgazó tanto que reventó a 40 bares de presión, liberando una nube de gas que detonó en segundos.\n\n"
            "En tus circuitos de proceso, mapea e inspecciona con ultrasonido cada tramo muerto. Lo que no se mueve, también se destruye.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Massive petrochemical refinery explosion aftermath documentary photography, September 1 1992 La Mede refinery France. "
            "Cracked and shattered fluid catalytic cracking unit steel columns, heavy ruptured process pipeline dangling, extinguished charred steel frameworks, "
            "firefighters in silver reflective suits inspecting twisted wreckage, industrial harbor scenery in distant background, dramatic late summer lighting, 16:9 ratio."
        ),
        "guionLargo": (
            "El primero de septiembre de mil novecientos noventa y dos... a las cinco y veintidós de la madrugada... una explosión monumental sacudió la refinería de La Mède... a orillas de la laguna de Berre en el sur de Francia... "
            "El estallido destruyó por completo el bloque central de la unidad de craqueo catalítico en lecho fluido... cobrándose la vida de seis operadores de guardia y causando daños estructurales en un radio de varios kilómetros... "
            "La investigación técnica posterior descubrió que el origen del siniestro no se debió a un error de operación en los reactores principales... sino al fallo imprevisto de una línea de derivación secundaria de ocho pulgadas de diámetro... "
            "Aquel tramo de tubería... diseñado originalmente como un circuito de bypass para permitir maniobras transitorias de mantenimiento... permanecía habitualmente fuera de servicio... aislado por válvulas de compuerta cerradas... "
            "En la ingeniería de procesos... estos sectores de cañería estancada se denominan tramos muertos o dead legs... "
            "Al carecer de flujo continuo... los vapores pesados y el vapor de agua presentes en la corriente de gas hidrocarburo se condensaron en el interior de la rama inactiva... "
            "Durante años... el agua condensada y los compuestos sulfurosos y clorados generaron una corrosión ácida localizada de severidad extrema en la generatriz inferior del caño... "
            "Debido a que el programa de inspección de integridad mecánica de la planta se focalizaba primordialmente en las líneas principales de transporte continuo... el tramo ciego fue omitido sistemáticamente en las campañas de medición de espesores por ultrasonido... "
            "El espesor del acero... calculado originalmente en más de siete milímetros... se redujo progresivamente hasta medir menos de un milímetro en la zona del codo... "
            "Sometida a la presión operativa de cuarenta bares... la debilitada tubería colapsó de manera repentina... "
            "Cientos de metros cúbicos de gas combustible a alta temperatura escaparon violentamente hacia la atmósfera... formando una densa nube de vapor que halló un punto de ignición en los hornos adyacentes... desatando una catastrófica explosión... "
            "El desastre de La Mède revolucionó las normas internacionales API quinientos setenta... "
            "A partir de aquel día... la industria petrolera mundial adoptó la obligación de inventariar, mapear y auditar el cien por ciento de los tramos muertos... o proceder a su remoción física definitiva... "
            "Porque en tuberías industriales... lo que no se ve y no circula... es a menudo lo que más rápido destruye."
        )
    },
    {
        "id": "069",
        "fecha": "02 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-02",
        "expediente": "Expediente #069",
        "carpeta": "2019-09-02-caida-plataforma-elevadora-pemp-catapulta",
        "titular": "EL EFECTO CATAPULTA: LA CAÍDA DESDE LA PLATAFORMA ELEVADORA",
        "palabraResaltada": "EFECTO CATAPULTA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Nave Industrial y Centro Logístico en Construcción - 2019",
        "tipoRiesgo": "Trabajo en Altura / Plataformas Móviles de Personal (PEMP)",
        "parrafos": [
            "El 2 de septiembre de 2019, un montador de 34 años falleció tras ser eyectado desde la cesta de una plataforma elevadora articulada a diez metros de altura en un centro logístico.",
            "El operario desplazó el equipo con el brazo completamente extendido para cambiar de posición. Al pisar un pequeño desnivel en el piso de hormigón, la base transmitió una sacudida multiplicada hacia la cesta.",
            "Al no llevar su arnés de seguridad anclado al punto de anclaje certificado de la cesta, el efecto catapulta lo arrojó al vacío sin posibilidad de sujetarse. En PEMP, el anclaje del cabo de vida es innegociable.",
        ],
        "puntosClave": [
            {"icono": "anchor", "titulo": "Arnés anclado al 100% en cesta (PEMP)", "texto": "Conectar siempre el cabo de amarre corto con absorbedor al punto de anclaje certificado del fabricante dentro de la barquilla."},
            {"icono": "arrow-down", "titulo": "Bajar la cesta antes de trasladar el equipo", "texto": "Prohibido circular distancias largas o cruzar desniveles con el brazo elevado; descender a posición de transporte."},
            {"icono": "alert-triangle", "titulo": "Comprender el efecto catapulta", "texto": "Un desnivel de apenas 3 cm en las ruedas se multiplica por diez en la cesta debido al efecto palanca del mástil articulado."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: guías técnicas de operación segura de PEMP de IPAF (International Powered Access Federation) y normas OSHA 1926.453.",
        "guionReel": (
            "¿Sabías que un desnivel de solo tres centímetros en el suelo puede expulsarte por el aire a diez metros de altura?\n\n"
            "El 2 de septiembre de 2019, en una nave industrial, un montador trabajaba en una plataforma elevadora de brazo articulado.\n\n"
            "Para no perder tiempo bajando la cesta y volviendo a subir, decidió avanzar manejando el equipo con el brazo estirado a diez metros de altura.\n\n"
            "Tenía puesto el arnés, pero no había enganchado el cabo de vida al punto de anclaje de la canasta porque 'se sentía seguro dentro de las barandas'.\n\n"
            "Una rueda pisó un bache en el hormigón. El efecto palanca fue instantáneo: la cesta osciló violentamente hacia arriba como una catapulta y lo arrojó despedido por encima de las barandas.\n\n"
            "Cayó contra el piso y murió en el acto.\n\n"
            "En plataformas elevadoras, el arnés se ancla siempre y la cesta se baja antes de mover la máquina.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Industrial logistics warehouse construction site documentary photography, self-propelled articulating boom mobile elevating work platform (MEWP) standing extended. "
            "Basket tilted at angle ten meters high near steel roof truss structure, fallen safety harness and lanyard lying on polished concrete slab floor below, "
            "small deep trench pothole visible under front tire wheel, warning high-visibility safety barriers surrounding area, realistic dramatic daylight, 16:9 ratio."
        ),
        "guionLargo": (
            "El dos de septiembre de dos mil diecinueve... en el interior de una imponente nave logística en proceso de montaje de cañerías contra incendios... una omisión de procedimiento cobró una vida de forma fulminante... "
            "Un montador de instalaciones industriales realizaba la colocación de abrazaderas y tuberías de rociadores a más de diez metros de altura... utilizando una plataforma elevadora móvil de personal de brazo articulado... "
            "Para avanzar a lo largo de la nave sin tener que descender la estructura telescópica a nivel de piso en cada tramo... el operario maniobraba los mandos de traslación directamente desde la canasta en posición elevada... "
            "El trabajador llevaba colocado un arnés de cuerpo completo... pero había dejado el mosquetón de su cabo de vida suelto... sin anclarlo a la argolla de fijación certificada provista en el suelo de la cesta... asumiendo falsamente que el enrejado de las barandas metálicas perimetrales le brindaba una contención suficiente... "
            "Sin embargo... en la física de las plataformas elevadoras... existe un fenómeno dinámico extraordinariamente peligroso conocido como el efecto catapulta... "
            "Debido a la gran longitud del brazo mecánico... cualquier pequeña irregularidad que impacte sobre las ruedas del chasis en el suelo... como un desnivel de tres centímetros, un pozo de dilatación o un obstáculo en el pavimento... se amplifica geométricamente a lo largo del mástil... "
            "Al cruzar una junta de hormigón mal terminada... la rueda delantera izquierda cayó bruscamente en el desnivel... "
            "El chasis se inclinó apenas unos grados... pero en la punta del brazo... a diez metros de elevación... la cesta experimentó una aceleración vertical súbita y violenta... "
            "La estructura osciló como una catapulta... proyectando al trabajador hacia arriba y por encima de las barandas de seguridad... "
            "Sin un cabo de amarre que lo mantuviera vinculado al habitáculo... el operario se precipitó al vacío... falleciendo en el acto al impactar contra la losa de hormigón... "
            "Las directivas internacionales de la federación IPAF y los manuales de seguridad son taxativos... En plataformas móviles de brazo articulado o telescópico... el uso de un arnés con cabo de amarre corto es obligatorio y permanente... "
            "Y la orden de operación es inalterable... Antes de mover la máquina... la canasta debe descender a posición de transporte... "
            "Porque en altura... la física convierte un tropiezo insignificante en una caída fatal."
        )
    },
    {
        "id": "070",
        "fecha": "03 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-03",
        "expediente": "Expediente #070",
        "carpeta": "1991-09-03-incendio-imperial-food-puertas-bloqueadas",
        "titular": "PUERTAS CON CANDADO EN EL INFIERNO: IMPERIAL FOOD PRODUCTS",
        "palabraResaltada": "IMPERIAL FOOD PRODUCTS",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Procesadora Imperial Food Products, Hamlet, EE.UU. - 1991",
        "tipoRiesgo": "Evacuación y Protección contra Incendios / Salidas de Emergencia",
        "parrafos": [
            "El 3 de septiembre de 1991, un incendio en la planta avícola Imperial Food Products en Hamlet, Carolina del Norte, provocó la muerte de 25 trabajadores al encontrarse las salidas de emergencia cerradas con candado.",
            "Una rotura en una manguera hidráulica pulverizó aceite a 55 bares sobre los quemadores de gas de una freidora industrial desatando un fuego incontrolable. Al intentar evacuar, los operarios hallaron las puertas bloqueadas desde el exterior.",
            "La gerencia las había trabado con candado para evitar robos de mercadería. El siniestro marcó un hito en la legislación: las salidas de emergencia deben abrir siempre hacia afuera con barras antipánico sin trabas.",
        ],
        "puntosClave": [
            {"icono": "door-open", "titulo": "Prohibido bloquear salidas de emergencia", "texto": "Las puertas de escape jamás deben tener candados, cadenas ni pestillos que impidan la apertura inmediata desde el interior."},
            {"icono": "flame", "titulo": "Líneas hidráulicas lejos de fuentes de ignición", "texto": "Blindar y alejar tuberías de aceite presurizado respecto de hornos, freidoras o quemadores de gas para evitar sprays inflamables."},
            {"icono": "bell", "titulo": "Sistemas de detección y rociadores automáticos", "texto": "Instalar rociadores automáticos (sprinklers) y alarmas audibles vinculadas al sistema de ventilación de humo en naves industriales."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de investigación de desastres por incendio de la NFPA y reporte especial de OSHA sobre la tragedia de Imperial Food Products en Hamlet.",
        "guionReel": (
            "¿Te imaginas correr desesperado hacia la salida de emergencia de una fábrica en llamas y encontrarla cerrada con candado?\n\n"
            "El 3 de septiembre de 1991, en la procesadora de pollos Imperial Food en Carolina del Norte, una manguera de aceite explotó sobre una freidora industrial gigante.\n\n"
            "Una llamarada colosal llenó la fábrica de humo negro y monóxido de carbono. Cien trabajadores corrieron hacia las puertas de escape.\n\n"
            "Pero los dueños de la planta habían cerrado las puertas con candados y cadenas desde afuera para que los empleados 'no se robaran pollos'.\n\n"
            "Veinticinco trabajadores murieron asfixiados amontonados contra las puertas de hierro que no pudieron abrir.\n\n"
            "Una salida de emergencia cerrada con llave es un crimen. Deben abrir siempre con barra antipánico y estar despejadas las 24 horas.\n\n"
            "La vida humana vale infinitamente más que cualquier inventario."
        ),
        "promptImagen": (
            "Historical industrial disaster documentary photography, September 3 1991 Imperial Food Products chicken processing plant fire Hamlet North Carolina. "
            "Heavy industrial steel emergency exit door charred by thick black smoke with broken padlock and heavy chain hanging from latch, "
            "emergency responder searchlights cutting through dense smoke, scattered work boots and white processing hairnets on pavement outside, somber archival style, 16:9."
        ),
        "guionLargo": (
            "El tres de septiembre de mil novecientos noventa y uno... en la pequeña localidad de Hamlet, en Carolina del Norte... se produjo uno de los siniestros industriales más repudiables de la historia contemporánea... "
            "En la planta procesadora de alimentos Imperial Food Products... cerca de cien operarios trabajaban en el turno matutino cortando, empanando y cocinando trozos de pollo frito a escala industrial... "
            "En la línea de cocción... una tubería flexible de fluido hidráulico que alimentaba los motores de la cinta transportadora... operando a más de cincuenta bares de presión... presentaba una reparación casera deficiente... "
            "A las ocho y media de la mañana... la manguera se desprendió bruscamente... pulverizando un chorro atomizado de aceite mineral directamente sobre los quemadores de gas abiertos de una freidora de ocho metros de largo que contenía miles de litros de grasa hirviendo... "
            "La mezcla se encendió de manera instantánea en una bola de fuego colosal... "
            "El techo de la nave... cubierto por paneles aislantes combustibles de espuma plástica... comenzó a arder con voracidad... desprendiendo una humareda negra saturada de gases tóxicos y cianuro de hidrógeno... "
            "Las luces se apagaron y la planta quedó sumida en una oscuridad asfixiante... "
            "Los trabajadores... en su mayoría mujeres y madres de familia... corrieron desesperadamente hacia las nueve salidas de escape del edificio... "
            "Pero al llegar a las puertas... se toparon con una realidad aterradora... "
            "La gerencia de la fábrica había ordenado trabar y bloquear deliberadamente las salidas de emergencia con candados y cadenas desde el exterior... bajo el pretexto de impedir que los empleados sustrajeran mercadería o salieran a fumar... "
            "Atrapados en un callejón sin salida... los obreros golpearon las chapas blindadas con sus puños y extinguidores vacíos... sin lograr derribarlas... "
            "Veinticinco personas murieron por asfixia amontonadas contra las puertas cerradas... y más de cincuenta sufrieron quemaduras y lesiones respiratorias de extrema gravedad... "
            "La tragedia de Hamlet conmocionó a los Estados Unidos y forzó una reforma radical en las leyes de seguridad laboral... "
            "Las normativas internacionales consagraron un principio inviolable... Las puertas de emergencia jamás pueden tener cerrojos, candados o trabas... Deben abrir siempre en el sentido de la evacuación mediante barras antipánico accionables con un simple empujón... "
            "Porque ante un incendio... una puerta cerrada con llave no es una medida de seguridad patrimonial... es una sentencia de muerte."
        )
    },
    {
        "id": "071",
        "fecha": "04 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-04",
        "expediente": "Expediente #071",
        "carpeta": "2018-09-04-electrocucion-hidrolavadora-piso-humedo",
        "titular": "AGUA Y ELECTRICIDAD: LA HIDROLAVADORA SIN DISYUNTOR",
        "palabraResaltada": "AGUA Y ELECTRICIDAD",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Lavadero Industrial y Playón de Mantenimiento - 2018",
        "tipoRiesgo": "Riesgo Eléctrico / Ambientes Húmedos y Doble Aislamiento",
        "parrafos": [
            "El 4 de septiembre de 2018, un operario de 26 años falleció electrocutado mientras lavaba un camión cisterna utilizando una hidrolavadora eléctrica de alta presión sobre un piso encharcado.",
            "El cable prolongador presentaba un empalme precario con cinta aislante deteriorada que tomó contacto con el agua. El tablero de alimentación carecía de interruptor diferencial (disyuntor de 30 mA) y la descarga a tierra estaba cortada.",
            "La corriente atravesó el charco y el cuerpo del trabajador causándole fibrilación ventricular. En ambientes mojados, la protección diferencial calibrada y la tierra efectiva son las únicas barreras de supervivencia.",
        ],
        "puntosClave": [
            {"icono": "shield-check", "titulo": "Interruptor diferencial obligatorio (30 mA)", "texto": "Toda toma eléctrica para herramientas portátiles en áreas mojadas debe contar con disyuntor de alta sensibilidad verificado periódicamente."},
            {"icono": "zap-off", "titulo": "Puesta a tierra continua y sin empalmes", "texto": "Prohibido utilizar cables prolongadores con empalmes caseros; exigir cables de doble aislamiento con fichas industriales blindadas IP67."},
            {"icono": "droplets", "titulo": "Uso de calzado dieléctrico para agua", "texto": "Utilizar botas de goma con resistencia dieléctrica certificada y verificar que el equipo posea carcasa con aislamiento reforzado."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: normativas de seguridad eléctrica en ambientes húmedos de la NFPA 70E, OSHA 1910.304 y reglamento de la Asociación Electrotécnica Argentina (AEA 90364).",
        "guionReel": (
            "¿Sabías que un charco de agua con un cable roto puede matarte antes de que sientas que te estás quemando?\n\n"
            "El 4 de septiembre de 2018, un joven de 26 años lavaba camiones en un playón industrial con una hidrolavadora eléctrica potente.\n\n"
            "El piso estaba completamente inundado. El alargue que usaba tenía una unión casera tapada con cinta aislante común, tirada directo en el agua.\n\n"
            "Para colmo, en el tablero general alguien había sacado el disyuntor diferencial 'porque saltaba a cada rato' y el enchufe no tenía la pata de puesta a tierra.\n\n"
            "El agua filtró en el empalme y energizó todo el charco a 220 voltios. Al pisar el agua, la electricidad atravesó su cuerpo y su corazón se detuvo en el acto.\n\n"
            "Con agua y electricidad no se juega: cables enteros sin empalmes, enchufes estancos y disyuntor diferencial de 30 miliamperios obligatorio.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Industrial vehicle wash bay electrical hazard documentary photography, concrete floor flooded with standing water and soap suds. "
            "Heavy industrial high-pressure pressure washer trolley with cracked electrical extension cord submerged in water puddle, loose safety plug without ground pin, "
            "yellow electrical hazard danger sign standing in water, discarded heavy rubber insulated boots, realistic sharp focus, 16:9 ratio."
        ),
        "guionLargo": (
            "El cuatro de septiembre de dos mil dieciocho... en el sector de lavado y desinfección de flota pesada de una compañía de transporte... una serie de improvisaciones eléctricas terminó con la vida de un joven trabajador... "
            "El operario... con apenas seis meses de antigüedad en la empresa... realizaba la limpieza intensiva del chasis y las ruedas de un camión cisterna... utilizando una hidrolavadora eléctrica industrial de agua a presión... "
            "El entorno de trabajo presentaba condiciones de riesgo eléctrico severo... El suelo de hormigón se encontraba totalmente inundado por charcos continuos de agua con detergente desengrasante... una sustancia que reduce drásticamente la resistencia eléctrica de la piel humana y del pavimento... "
            "Para conectar el equipo a la red de energía... el trabajador había extendido un cable prolongador de más de veinte metros... el cual presentaba un empalme casero de conductores de cobre... recubierto únicamente con un par de vueltas de cinta aisladora plástica deteriorada... "
            "El empalme reposaba sumergido directamente en el agua sucia... "
            "La ficha de conexión en el extremo del cable carecía del borne de puesta a tierra... el cual había sido cortado con un alicate en el pasado para poder enchufarlo en tomacorrientes bipolares antiguos... "
            "Pero la falla más grave radicaba en el tablero de distribución eléctrica de la nave... "
            "Debido a que el interruptor diferencial de cabecera disparaba frecuentemente por fugas de humedad... el personal de mantenimiento había puenteado el disyuntor... dejando la línea protegida únicamente por un interruptor termomagnético de gran calibre... un dispositivo diseñado para proteger cables contra incendios... pero completamente incapaz de proteger una vida humana frente a una fuga a tierra... "
            "En medio de la tarea... el agua jabonosa penetró en el empalme del cable... "
            "Una corriente de fuga energizó instantáneamente todo el charco de agua a doscientos veinte voltios de tensión... "
            "Al desplazarse para alcanzar otra parte del vehículo... la corriente eléctrica atravesó el cuerpo del operario desde sus pies hacia la lanza metálica conectada a tierra... desencadenando una fibrilación ventricular letal... "
            "Las investigaciones periciales recordaron que en ambientes húmedos... la electricidad exige barreras técnicas infalibles... "
            "Queda terminantemente prohibido el uso de alargues con empalmes caseros... Las conexiones deben realizarse mediante fichas y tomas estancas industriales con grado de protección IP sesenta y siete... y toda línea debe contar con un disyuntor diferencial de alta sensibilidad de treinta miliamperios verificado periódicamente... "
            "Porque ante el agua y la corriente... un disyuntor puenteado es una trampa que no da aviso."
        )
    },
    {
        "id": "072",
        "fecha": "05 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-05",
        "expediente": "Expediente #072",
        "carpeta": "2015-09-05-lesion-ocular-proyeccion-escoria-soldadura",
        "titular": "EL DESTELLO Y LA ESCORIA: LA LESIÓN OCULAR EN SOLDADURA",
        "palabraResaltada": "LESIÓN OCULAR",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Taller de Fabricación Metalúrgica y Montaje de Cañerías - 2015",
        "tipoRiesgo": "Trabajo en Caliente / Salud Ocular y Protección Facial",
        "parrafos": [
            "El 5 de septiembre de 2015, un soldador calificado sufrió la incrustación profunda de escoria incandescente en la córnea y queratitis por radiación UV durante la fabricación de un manifold de tuberías.",
            "Al terminar el cordón con electrodo revestido, levantó la careta de soldar e inmediatamente picó la escoria caliente con la piqueta sin tener puestas gafas de seguridad transparentes debajo de la máscara.",
            "Un fragmento de escoria a 600 °C penetró en su globo ocular causándole perforación y pérdida parcial de visión. Además, compañeros en puestos contiguos sufrieron fotoqueratitis por falta de biombos ignífugos.",
        ],
        "puntosClave": [
            {"icono": "eye", "titulo": "Gafas de seguridad bajo la careta", "texto": "Usar siempre gafas de seguridad transparentes de policarbonato debajo de la pantalla de soldar para protegerse al picar la escoria."},
            {"icono": "shield", "titulo": "Biombos y cortinas de protección UV", "texto": "Delimitar cada puesto de soldadura con mamparas o biombos filtrantes de radiación UV para proteger a terceros de la fotoqueratitis."},
            {"icono": "flame", "titulo": "Extintor ABC y retiro de combustibles", "texto": "Despejar un radio de 10 metros de todo material combustible y mantener un extintor verificado al alcance de la mano (NFPA 51B)."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: normativas de prevención en operaciones de soldadura y corte de OSHA 1910.252, normas de protección ocular ANSI Z87.1 y estándar NFPA 51B.",
        "guionReel": (
            "¿Sabías cuál es el momento más peligroso para los ojos de un soldador?\n\n"
            "No es cuando está soldando: es cuando levanta la careta para mirar el cordón.\n\n"
            "El 5 de septiembre de 2015, en una metalúrgica, un soldador terminó una costura con electrodo revestido. Con el metal al rojo vivo, se levantó la máscara y le pegó con la piqueta para sacar la cáscara de escoria.\n\n"
            "No tenía puestos los anteojos de seguridad transparentes abajo de la careta.\n\n"
            "Un pedazo de escoria hirviendo a seiscientos grados salió disparado directo a su ojo derecho, incrustándose en la córnea y perforando el tejido.\n\n"
            "Para colmo, no había biombos y los compañeros de al lado sufrieron quemaduras en los ojos por el destello.\n\n"
            "Regla de oro: los anteojos transparentes nunca se sacan, van siempre puestos debajo de la careta de soldar.\n\n"
            "Tus ojos no se pueden reemplazar."
        ),
        "promptImagen": (
            "Industrial metal welding workshop documentary photography, welding workbench with heavy steel pipes and freshly welded seam joints. "
            "Welding chipping slag hammer lying next to smoking red-hot weld bead, welding helmet with flip-up visor raised, shattered polycarbonate safety glasses, "
            "amber translucent UV welding safety curtains partitioning the workshop bay, dramatic atmospheric welding sparks in background, 16:9 ratio."
        ),
        "guionLargo": (
            "El cinco de septiembre de dos mil quince... en una nave industrial dedicada a la prefabricación de tuberías y recipientes sometidos a presión... una práctica viciada pero sumamente extendida provocó una lesión oftalmológica invalidante... "
            "Un soldador calificado realizaba la unión de dos bridas de acero al carbono utilizando el proceso de soldadura manual por arco con electrodo revestido... conocido técnicamente como proceso SMAW... "
            "Al depositar el cordón... el fundente químico del electrodo se funde junto con el metal... flotando hacia la superficie para formar una capa protectora solidificada de escoria vítrea que aísla el baño de fusión del oxígeno atmosférico... "
            "Apenas concluyó la pasada de raíz... el operario levantó la pantalla facial de soldar hacia arriba... con el fin de inspeccionar visualmente la penetración del cordón... "
            "Omitió una de las exigencias más elementales de la norma técnica ANSI Z ochenta y siete... la obligación de portar anteojos de seguridad de policarbonato transparente ajustados a la cara de manera permanente debajo de la careta fotosensible... "
            "Con la escoria todavía incandescente a más de seiscientos grados centígrados... el trabajador tomó la piqueta metálica y comenzó a golpear el cordón con fuerza para descascarillar el recubrimiento... "
            "Durante el enfriamiento rápido... la escoria sufre severas tensiones mecánicas internas... volviéndose quebradiza y explosiva... "
            "Al impactar el martillo... un fragmento puntiagudo al rojo vivo se desprendió a gran velocidad... saliendo proyectado directamente hacia el rostro desprotegido del soldador... "
            "La escoria caliente impactó en el ojo derecho... incrustándose profundamente en el estroma corneal y perforando la cámara anterior... provocando una quemadura térmica y química combinada... "
            "El operario fue trasladado de urgencia a un centro oftalmológico... requiriendo intervenciones quirúrgicas complejas que no lograron evitar una pérdida del setenta por ciento de la agudeza visual de ese ojo... "
            "Asimismo... la investigación detectó que el puesto carecía de mamparas o biombos ignífugos de protección perimetral... lo que provocó que dos compañeros situados en bancos adyacentes sufrieran queratoconjuntivitis actínica aguda por exposición al resplandor ultravioleta... "
            "La seguridad en trabajos en caliente es categórica... Los lentes de seguridad jamás se retiran en el taller... deben permanecer colocados de forma ininterrumpida debajo de la careta de soldador... "
            "Y todo puesto de soldadura debe estar confinado por biombos que filtren la radiación UV... "
            "Porque frente a una chispa de escoria incandescente... no existe tiempo de pestañear."
        )
    }
]

def procesar_lote_6(kokoro_instance):
    procesadas = []

    print(f"\n=======================================================")
    print(f"Iniciando procesamiento de {len(LOTE_6_DATA)} historias del Lote 6 (#063 a #072)")
    print(f"=======================================================\n")

    for h in LOTE_6_DATA:
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
            crear_portada_grafica_lote6(h, portada_path)
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

def crear_portada_grafica_lote6(historia, output_path):
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
    """Inyecta las historias del Lote 6 en index.html antes del cierre del array historias."""
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

    print("\n✓ index.html actualizado exitosamente con los 10 nuevos expedientes (#063 a #072).")
    return True

def main():
    print("Iniciando motor Kokoro para Lote 6 (#063 a #072)...")
    kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

    procesadas = procesar_lote_6(kokoro)

    if inyectar_en_index_html(procesadas):
        print(f"\n🎉 ¡LOTE 6 COMPLETADO AL 100%! ({len(procesadas)} historias procesadas)")

if __name__ == "__main__":
    main()
