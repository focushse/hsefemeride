# -*- coding: utf-8 -*-
"""
Generador Agéntico Automatizado de Efemérides para Focus HSE
Genera 10 efemérides completas:
1. Dossier técnico (contenido-completo.md)
2. README.md
3. Portada oficial (portada.png) en formato horizontal 16:9
4. Audio narrado con Kokoro TTS local (velocidad calibrada a 0.86)
5. Conversión a M4A con ffmpeg y medición exacta de duración
6. Inyección de las 10 historias en index.html
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

HISTORIAS_DATA = [
    {
        "id": "013",
        "fecha": "8 JULIO",
        "fechaPublicacion": "2026-07-08",
        "expediente": "Expediente #013",
        "carpeta": "1969-07-08-derrumbe-zanja-queens",
        "titular": "EL TERRENO NO AVISA: CUATRO VIDAS BAJO LA TIERRA",
        "palabraResaltada": "BAJO LA TIERRA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Queens, Nueva York, Estados Unidos - 1969",
        "tipoRiesgo": "Excavaciones y Zanjas / Derrumbe",
        "parrafos": [
            "La tarde del 8 de julio de 1969, una cuadrilla trabajaba en una zanja de saneamiento de casi cuatro metros de profundidad en Queens, Nueva York, tras dos días de lluvias intensas.",
            "La excavación no contaba con entibado, cajón de protección ni talud adecuado. La arcilla saturada perdió cohesión y cedió súbitamente, sepultando a cuatro operarios en cuestión de segundos.",
            "La investigación demostró que el terreno fue clasificado erróneamente como estable y que no existían escaleras de escape cercanas, convirtiendo la zanja en una trampa mortal."
        ],
        "puntosClave": [
            {"icono": "shield-alert", "titulo": "Entibar toda zanja profunda", "texto": "Toda excavación mayor a 1,20 m exige entibado, tablaestacado o talud seguro acorde al tipo de suelo."},
            {"icono": "cloud-rain", "titulo": "Reevaluar tras lluvias", "texto": "El agua altera drásticamente la cohesión del suelo; antes de reingresar, una persona competente debe inspeccionar el talud."},
            {"icono": "footprints", "titulo": "Garantizar vías de escape", "texto": "Instalar escaleras o rampas de escape a no más de 7 metros de distancia de cada operario en el fondo."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: registros históricos de accidentes en construcción de Nueva York y normativa de excavaciones OSHA 29 CFR 1926 Subpart P.",
        "guionAudio": (
            "8 de julio de 1969. — En una obra civil de Queens, Nueva York, una cuadrilla de operarios "
            "trabajaba en el fondo de una zanja de casi cuatro metros de profundidad... mientras la jornada avanzaba con aparente normalidad. — "
            "Durante las cuarenta y ocho horas previas... una lluvia persistente había empapado el terreno. "
            "Para ahorrar tiempo y costos, la excavación se realizó con paredes verticales... sin entibado de madera, sin cajón de acero "
            "y sin ningún tipo de apuntalamiento. — "
            "En cuestión de una fracción de segundo... el terreno saturado de agua perdió toda su cohesión. "
            "Toneladas de arcilla y barro se desprendieron como una pared sólida... sepultando a cuatro trabajadores bajo la tierra. — "
            "Los compañeros intentaron cavar desesperadamente con palas y con las manos... pero la presión del suelo fue demoledora. "
            "Los cuatro operarios perdieron la vida por asfixia traumática. — "
            "El suelo no avisa antes de colapsar. Toda excavación de más de un metro con veinte centímetros exige protección física. — "
            "La seguridad... está en los detalles."
        )
    },
    {
        "id": "014",
        "fecha": "9 JULIO",
        "fechaPublicacion": "2026-07-09",
        "expediente": "Expediente #014",
        "carpeta": "2015-07-09-fuga-amoniaco-frigorifico",
        "titular": "EL GAS INVISIBLE QUE CONVIRTIÓ LA PLANTA EN UNA TRAMPA",
        "palabraResaltada": "GAS INVISIBLE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Frigorífica, Santa Fe, Argentina - 2015",
        "tipoRiesgo": "Riesgo Químico / Intoxicación por Amoníaco",
        "parrafos": [
            "La madrugada del 9 de julio de 2015, técnicos de mantenimiento intervenían una válvula en la sala de compresores de amoníaco de una planta frigorífica en Santa Fe, Argentina.",
            "La línea no fue purgada en su totalidad ni se despresurizó el amoníaco líquido atrapado. Al aflojar los pernos, una nube densa y cáustica se liberó a gran presión sobre los trabajadores.",
            "Los detectores fijos estaban inoperativos y los operarios carecían de equipos autónomos. La fuga obligó a evacuar a decenas de vecinos y dejó trabajadores hospitalizados con quemaduras químicas."
        ],
        "puntosClave": [
            {"icono": "lock", "titulo": "Aislamiento y purga total (LOTO)", "texto": "En amoníaco anhidro, despresurizar, bombear remanentes y colocar bridas ciegas antes de abrir cualquier brida."},
            {"icono": "bell-ring", "titulo": "Detectores y alarmas operativas", "texto": "Los sensores de NH3 y el enclavamiento de ventilación de emergencia deben probarse periódicamente."},
            {"icono": "shield-check", "titulo": "Respiración autónoma (SCBA)", "texto": "Toda apertura de circuito refrigerante exige máscara de presión positiva autónoma y traje de protección química."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informes técnicos de bomberos zapadores de Santa Fe, reportes de la Superintendencia de Riesgos del Trabajo (SRT) y guías IIAR de amoníaco.",
        "guionAudio": (
            "9 de julio de 2015. — En la sala de refrigeración de una importante planta frigorífica de Santa Fe, Argentina... "
            "un equipo de mantenimiento se preparaba para reemplazar una válvula en el circuito principal de amoníaco. — "
            "Se cerraron las válvulas manuales de paso... pero no se purgó el amoníaco líquido que permanecía atrapado en la sección de tubería, "
            "ni se colocaron bridas ciegas para aislar la energía química. — "
            "Al aflojar el último perno de la brida... el líquido presurizado se expandió instantáneamente en forma de gas tóxico y cáustico. "
            "Una densa nube blanca inundó la sala de compresores a más de doscientas partes por millón... cegando y quemando las vías respiratorias de los operarios. — "
            "Los detectores de fuga no se activaron y los trabajadores carecían de equipos de respiración autónoma. "
            "El pánico provocó una evacuación masiva en el barrio circundante... y dejó a varios operarios en terapia intensiva con graves quemaduras en los pulmones. — "
            "El amoníaco no perdona el exceso de confianza. En sustancias tóxicas... purgar y aislar es la única garantía de vida. — "
            "La seguridad... está en los detalles."
        )
    },
    {
        "id": "015",
        "fecha": "10 JULIO",
        "fechaPublicacion": "2026-07-10",
        "expediente": "Expediente #015",
        "carpeta": "1976-07-10-desastre-seveso",
        "titular": "LA NUBE BLANCA QUE CAMBIÓ LA SEGURIDAD QUÍMICA EN EUROPA",
        "palabraResaltada": "NUBE BLANCA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Química ICMESA, Meda y Seveso, Italia - 1976",
        "tipoRiesgo": "Seguridad de Procesos (PSM) / Reacción Exotérmica",
        "parrafos": [
            "El sábado 10 de julio de 1976, el reactor B-101 de la planta ICMESA en Meda, Italia, quedó apagado para el fin de semana tras producir triclorofenol, pero sin enfriamiento activo continuo.",
            "El calor residual en las paredes desató una reacción exotérmica no controlada. La presión superó los límites y el disco de ruptura venteó directamente al aire libre una nube con dioxina TCDD.",
            "El viento arrastró el veneno hacia el pueblo de Seveso. Miles de animales murieron, cientos de niños sufrieron cloracné y el desastre dio origen a las Directivas Seveso de la Unión Europea."
        ],
        "puntosClave": [
            {"icono": "flame", "titulo": "Control térmico residual", "texto": "Los reactores con potencial exotérmico deben mantener agitación y enfriamiento monitoreado aun durante paradas."},
            {"icono": "filter", "titulo": "Alivio a sistemas cerrados", "texto": "Los venteos de emergencia de químicos altamente tóxicos deben derivar a lavadores de gases o antorchas, nunca al aire libre."},
            {"icono": "megaphone", "titulo": "Planes de emergencia externa", "texto": "Las plantas de riesgo mayor deben coordinar alertas inmediatas y transparentes con la comunidad vecina."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe oficial de la Comisión Europea sobre el desastre de Seveso y documentación técnica de la Directiva Seveso I, II y III.",
        "guionAudio": (
            "10 de julio de 1976. — Al norte de Milán, en la planta química de ICMESA... el reactor de triclorofenol fue apagado al mediodía para iniciar el descanso del fin de semana. — "
            "Los operarios suspendieron la agitación mecánica... pero dejaron el reactor cargado y sin enfriamiento forzado continuo. "
            "En el interior del recipiente metálico... el calor residual comenzó a transferirse hacia la masa química... desatando una violenta reacción exotérmica fuera de control. — "
            "A las doce y treinta y siete del mediodía... la presión reventó el disco de ruptura de seguridad. "
            "Como la tubería de alivio no contaba con tanque de contención ni lavador de gases... una nube blanca de vapor químico se disparó directamente hacia el cielo de Seveso. — "
            "Entre los vapores viajaban varios kilogramos de dioxina TCDD... una de las sustancias más tóxicas conocidas por la ciencia. "
            "En pocos días... la vegetación se secó, más de ochenta mil animales murieron y casi doscientos niños desarrollaron severas deformaciones de cloracné en la piel. — "
            "Esta tragedia obligó a Europa a crear las Directivas Seveso... para exigir que todo riesgo químico mayor cuente con defensas en profundidad. — "
            "La seguridad... está en los detalles."
        )
    },
    {
        "id": "016",
        "fecha": "11 JULIO",
        "fechaPublicacion": "2026-07-11",
        "expediente": "Expediente #016",
        "carpeta": "2013-07-11-atrapamiento-silo-granos",
        "titular": "EL EFECTO PUENTE: ATRAPADO EN SEGUNDOS POR EL CEREAL",
        "palabraResaltada": "EFECTO PUENTE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Silo de Acopio, Región Pampeana, Argentina - 2013",
        "tipoRiesgo": "Espacios Confinados / Asfixia y Atrapamiento",
        "parrafos": [
            "La mañana del 11 de julio de 2013, un operario ingresó al interior de un silo vertical de soja en una planta de acopio en la Región Pampeana para destrabar cereal apelmazado en las paredes.",
            "El sistema de descarga inferior estaba en funcionamiento. El grano compactado formó una caverna hueca o 'puente' que colapsó repentinamente bajo su peso, hundiéndolo como arenas movedizas.",
            "El trabajador no contaba con arnés conectado ni vigía con sistema de rescate. En menos de veinte segundos quedó sepultado bajo toneladas de cereal, falleciendo por asfixia mecánica."
        ],
        "puntosClave": [
            {"icono": "ban", "titulo": "Prohibido ingresar con descarga activa", "texto": "Bloquear mecánicamente compuertas y roscas sinfín antes de permitir el ingreso de personas al silo."},
            {"icono": "life-buoy", "titulo": "Línea de vida tensa y arnés", "texto": "El operario debe portar arnés integral conectado a una línea de vida tensada que impida su hundimiento en el grano."},
            {"icono": "users", "titulo": "Vigía con trípode de rescate", "texto": "Presencia permanente de un vigía capacitado en la boca superior con sistema de izaje mecánico para rescate inmediato."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: investigaciones sobre atrapamiento en granos de OSHA, INTA Argentina y guías de seguridad en plantas de silos de la SRT.",
        "guionAudio": (
            "11 de julio de 2013. — En una planta de acopio de cereales en la pampa húmeda argentina... "
            "un operario bajó por la escalerilla interna hacia el interior de un inmenso silo vertical de soja. — "
            "Su objetivo era empujar con una varilla una costra de granos húmedos que impedía la salida del cereal por la tolva inferior. "
            "Para acelerar el vaciado... los transportadores de descarga seguían funcionando a plena marcha. — "
            "Lo que el trabajador no podía ver... era que debajo de la costra superficial se había formado un enorme vacío hueco... conocido en la industria como efecto puente. — "
            "Al dar un paso en falso... la corteza cedió como una trampa de arena movediza. "
            "En cuestión de cinco segundos... el operario quedó atrapado hasta la cintura... y antes de que pudiera pedir auxilio, el flujo descendente lo succionó por completo. — "
            "Sin arnés anticaídas y sin un vigía equipado con polea de rescate en el exterior... el rescate fue imposible a tiempo. "
            "Toneladas de granos ejercen una presión de cientos de kilos sobre el pecho, impidiendo respirar. — "
            "Jamás camines sobre material a granel en movimiento. — "
            "La seguridad... está en los detalles."
        )
    },
    {
        "id": "017",
        "fecha": "12 JULIO",
        "fechaPublicacion": "2026-07-12",
        "expediente": "Expediente #017",
        "carpeta": "2018-07-12-prensa-hidraulica-loto",
        "titular": "CONFIAR EN UN SENSOR COSTÓ LA VIDA EN LA PRENSA",
        "palabraResaltada": "CONFIAR EN UN SENSOR",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Metalmecánica - 2018",
        "tipoRiesgo": "Atrapamiento y Mecánico / Bloqueo LOTO",
        "parrafos": [
            "El 12 de julio de 2018, en una planta de estampado automotriz, un técnico ingresó al área de troquelado de una prensa hidráulica de 400 toneladas para limpiar virutas acumuladas en la matriz.",
            "Para no demorar la producción, no se aplicó el corte de energía principal ni se colocaron los calzos mecánicos de seguridad, confiando únicamente en la cortina óptica de seguridad.",
            "Una falla eléctrica imprevista en el circuito de control activó la válvula servohidráulica. El cilindro descendió a plena carrera, causando el aplastamiento mortal del trabajador."
        ],
        "puntosClave": [
            {"icono": "power-off", "titulo": "Energía cero real (LOTO)", "texto": "Cortar, candadear y despresurizar acumuladores hidráulicos antes de ingresar el cuerpo entre las matrices."},
            {"icono": "columns", "titulo": "Calzos mecánicos obligatorios", "texto": "Instalar trabas físicas de acero entre la bancada y el carro para impedir mecánicamente cualquier descenso accidental."},
            {"icono": "eye-off", "titulo": "Los sensores no son bloqueos", "texto": "Las cortinas de luz son protecciones operativas, jamás sustitutos de un procedimiento formal de consignación."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: normativas de seguridad en prensas mecánicas e hidráulicas OSHA 1910.217 e ISO 16092 sobre seguridad de máquinas.",
        "guionAudio": (
            "12 de julio de 2018. — En una concurrida planta metalmecánica... una prensa hidráulica de cuatrocientas toneladas producía piezas estampadas a ritmo vertiginoso. — "
            "Durante el cambio de turno... un operario advirtió restos de viruta metálica atorados en el centro de la matriz inferior. "
            "Para no reiniciar el ciclo del equipo ni perder tiempo de producción... decidió no realizar el bloqueo eléctrico ni despresurizar el circuito hidráulico. — "
            "Confiaba ciegamente en que la cortina de luz infrarroja detendría el movimiento si introducía sus manos. — "
            "Pero los componentes electrónicos pueden fallar. Un cortocircuito en el tablero secundario puenteó la señal de seguridad... "
            "y en una fracción de segundo... el pesado ariete superior descendió con una fuerza devastadora. — "
            "El operario fue aplastado al instante en la zona de troquelado. "
            "Ningún sensor electrónico reemplaza a un candado de consignación y a un calzo mecánico de acero que soporte físicamente la gravedad. — "
            "La seguridad... está en los detalles."
        )
    },
    {
        "id": "018",
        "fecha": "13 JULIO",
        "fechaPublicacion": "2026-07-13",
        "expediente": "Expediente #018",
        "carpeta": "2012-07-13-caida-altura-estructura-metalica",
        "titular": "UN SEGUNDO DESCONECTADO FUE LA DIFERENCIA ENTRE LA VIDA Y LA CAÍDA",
        "palabraResaltada": "DESCONECTADO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Montaje de Nave Industrial - 2012",
        "tipoRiesgo": "Trabajo en Altura / Caída a distinto nivel",
        "parrafos": [
            "La mañana del 13 de julio de 2012, montadores de estructuras metálicas colocaban correas de cubierta a once metros de altura en una obra industrial en expansión.",
            "Uno de los operarios portaba arnés de seguridad con un cabo simple. Al cambiar de viga, desenganchó su único mosquetón; en ese instante pisó una correa húmeda, resbaló y cayó al vacío.",
            "El impacto contra el suelo de hormigón fue instantáneo y fatal. La investigación comprobó la ausencia de líneas de vida horizontales continuas y la falta de cabo de vida doble."
        ],
        "puntosClave": [
            {"icono": "git-fork", "titulo": "100% anclado con cabo en Y", "texto": "Al desplazarse sobre vigas, un mosquetón debe estar anclado antes de desconectar el otro."},
            {"icono": "cable", "titulo": "Líneas de vida continuas", "texto": "Tender líneas de acero horizontales certificadas que permitan transitar sin desengancharse en los nudos."},
            {"icono": "truck", "titulo": "Priorizar plataformas elevadoras", "texto": "Sustituir el tránsito sobre vigas utilizando plataformas elevadoras móviles de personal (PEMP/manlift)."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: registros de accidentes laborales de construcción, estándares OSHA 1926 Subpart M (Fall Protection) y normas IRAM 3622.",
        "guionAudio": (
            "13 de julio de 2012. — En la construcción de una inmensa nave industrial... una cuadrilla de montadores completaba la estructura del techo a más de once metros sobre el suelo de hormigón. — "
            "El viento de la mañana soplaba con fuerza sobre las vigas de acero. "
            "Uno de los montadores más experimentados caminaba sobre las correas superiores... portando su arnés de seguridad. "
            "Sin embargo... utilizaba un cabo de amarre simple con un solo gancho... en lugar de un cabo doble en Y. — "
            "Al llegar a la columna principal... desenganchó el mosquetón para pasarlo al siguiente tramo. "
            "Fueron apenas dos segundos. Dos segundos en los que el trabajador quedó completamente desanclado a once metros de altura. — "
            "Una ráfaga de aire y una leve humedad sobre el metal le hicieron perder el equilibrio. Sin un punto de retención que lo frenara... cayó al vacío. — "
            "El impacto contra el piso fue fatal en el acto. "
            "En trabajos en altura... un segundo desconectado equivale a no llevar arnés. El compromiso debe ser cien por ciento anclado en todo momento. — "
            "La seguridad... está en los detalles."
        )
    },
    {
        "id": "019",
        "fecha": "14 JULIO",
        "fechaPublicacion": "2026-07-14",
        "expediente": "Expediente #019",
        "carpeta": "2019-07-14-intoxicacion-camara-septica",
        "titular": "EL EFECTO CASCADA: TRES COMPAÑEROS FALLECIDOS POR UN RESCATE IMPROVISADO",
        "palabraResaltada": "EFECTO CASCADA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Pozo de Bombeo y Cámara Séptica, Argentina - 2019",
        "tipoRiesgo": "Espacios Confinados / Sulfuro de Hidrógeno",
        "parrafos": [
            "El 14 de julio de 2019, operarios realizaban tareas de desobstrucción en un pozo de bombeo cloacal de cinco metros de profundidad sin realizar medición atmosférica previa.",
            "El primer trabajador descendió y colapsó instantáneamente debido a una bolsa concentrada de sulfuro de hidrógeno (H2S). Sus dos compañeros bajaron sucesivamente a rescatarlo y también cayeron.",
            "Los tres trabajadores fallecieron en el fondo del pozo. Más del sesenta por ciento de las muertes en espacios confinados corresponden a rescatistas que entran sin equipos autónomos."
        ],
        "puntosClave": [
            {"icono": "gauge", "titulo": "Medición de 4 gases previa", "texto": "Evaluar O2, explosividad, CO y H2S en la parte superior, media y profunda antes de retirar la tapa."},
            {"icono": "wind", "titulo": "Ventilación forzada continua", "texto": "Insuflar aire fresco con extractor/ventilador mecánico para desplazar gases pesados que se acumulan en el fondo."},
            {"icono": "heart-handshake", "titulo": "Prohibido el rescate a ciegas", "texto": "Jamás descender a rescatar sin equipo autónomo (SCBA) y línea de vida; el instinto sin equipo es mortal."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: estadísticas de fatalidades en espacios confinados de NIOSH, reportes de SRT Argentina y estándares OSHA 1910.146.",
        "guionAudio": (
            "14 de julio de 2019. — En un pozo de bombeo cloacal de cinco metros de profundidad... "
            "una cuadrilla de saneamiento municipal se preparaba para reparar una bomba sumergible atascada. — "
            "Confiados en que era una tarea rutinaria de pocos minutos... retiraron la pesada tapa de fundición sin encender el detector de cuatro gases "
            "y sin activar la ventilación mecánica forzada. — "
            "El primer operario descendió por la escalera marinera. Al llegar al tercer peldaño... inhaló una concentración mortal de sulfuro de hidrógeno... "
            "un gas venenoso que paraliza el sistema respiratorio en una sola inhalación. El trabajador cayó desvanecido al fondo. — "
            "Al ver a su compañero inmóvil... el segundo trabajador se arrojó desesperado a auxiliarlo por puro instinto... cayendo inconsciente sobre él a los pocos segundos. "
            "El tercer operario cometió el mismo error fatal intentando salvar a ambos. — "
            "Tres vidas se apagaron en menos de dos minutos por el llamado efecto cascada. "
            "En espacios confinados... el coraje sin equipo autónomo solo multiplica las víctimas. Medir la atmósfera y no ingresar sin protección salva vidas. — "
            "La seguridad... está en los detalles."
        )
    },
    {
        "id": "020",
        "fecha": "15 JULIO",
        "fechaPublicacion": "2026-07-15",
        "expediente": "Expediente #020",
        "carpeta": "1973-07-15-explosion-refineria-chiba",
        "titular": "LA VÁLVULA BLOQUEADA DESATÓ EL INFIERNO EN LA REFINERÍA",
        "palabraResaltada": "VÁLVULA BLOQUEADA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Refinería de Chiba, Bahía de Tokio, Japón - 1973",
        "tipoRiesgo": "Seguridad de Procesos (PSM) / Integridad de PSV",
        "parrafos": [
            "El 15 de julio de 1973, en la refinería de petróleo de Chiba, Japón, una columna de fraccionamiento de hidrocarburos operaba bajo alta presión y temperatura.",
            "Durante tareas previas de mantenimiento, una válvula de bloqueo manual situada antes de la válvula de seguridad (PSV) fue cerrada y no se volvió a abrir ni se colocó precinto de control.",
            "Una perturbación térmica elevó la presión de la torre; al no encontrar vía de alivio, la columna se fracturó violentamente, liberando toneladas de gases que detonaron en un incendio masivo."
        ],
        "puntosClave": [
            {"icono": "lock-keyhole", "titulo": "Control estricto de válvulas de alivio", "texto": "Toda válvula de bloqueo vinculada a una PSV debe estar precintada y candadeada en posición abierta (Car Seal Open)."},
            {"icono": "file-check", "titulo": "Revisión previa al arranque (PSSR)", "texto": "Antes de poner en marcha una unidad, verificar físicamente la posición de cada válvula crítica de alivio."},
            {"icono": "layers", "titulo": "Protección por sobrepresión independiente", "texto": "Los recipientes a presión deben contar con discos de ruptura o sistemas de enclavamiento instrumentado (SIS)."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de la Agencia de Manejo de Incendios y Desastres de Japón (FDMA), archivos de accidentes de API y guías CCPS sobre alivio de presión.",
        "guionAudio": (
            "15 de julio de 1973. — En la costa industrial de la bahía de Tokio... la refinería de Chiba procesaba miles de barriles diarios de crudo en sus torres de fraccionamiento continuo. — "
            "Días antes... personal de mantenimiento había realizado una inspección sobre una de las válvulas de seguridad principales. "
            "Para trabajar de forma segura... cerraron la válvula de corte manual ubicada debajo del dispositivo de alivio... "
            "pero al terminar la tarea... nadie volvió a abrirla ni a colocar el precinto de seguridad que garantizaba su posición abierta. — "
            "Durante el turno tarde del 15 de julio... un desajuste en el reflujo provocó un incremento súbito de temperatura y presión dentro de la columna. "
            "Cuando la presión interna superó los límites de diseño... la válvula de seguridad intentó disparar para salvar el equipo... "
            "pero el paso estaba ciego. La presión no tuvo salida. — "
            "La columna de acero colapsó por sobrepresión... desgarrándose en una brutal explosión que lanzó fragmentos de metal a cientos de metros "
            "e incendió la unidad completa durante días. — "
            "Una válvula de seguridad anulada es una bomba de tiempo. Nunca bloquees una línea de alivio sin control de ingeniería. — "
            "La seguridad... está en los detalles."
        )
    },
    {
        "id": "021",
        "fecha": "16 JULIO",
        "fechaPublicacion": "2026-07-16",
        "expediente": "Expediente #021",
        "carpeta": "2016-07-16-electrocucion-grua-pluma",
        "titular": "EL ARCO ELÉCTRICO INVISIBLE QUE MATÓ A DISTANCIA",
        "palabraResaltada": "ARCO ELÉCTRICO INVISIBLE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Obra Vial y Corredor Eléctrico - 2016",
        "tipoRiesgo": "Riesgo Eléctrico / Trabajo con Grúas cerca de Líneas",
        "parrafos": [
            "El 16 de julio de 2016, un camión hidrogrúa descargaba tuberías de hormigón en una obra vial cercana a una línea aérea de media tensión de 33 kilovoltios.",
            "El operador maniobró la pluma telescópica sin la asistencia de un señalero dedicado. Aunque la pluma no tocó físicamente el cable, se acercó a menos de un metro de distancia.",
            "La alta tensión saltó a través del aire mediante un arco eléctrico destructivo. La corriente viajó por la estructura metálica y electrocutó en el acto al operario que guiaba la carga con las manos."
        ],
        "puntosClave": [
            {"icono": "zap", "titulo": "Respetar distancias de seguridad", "texto": "La electricidad salta por el aire; mantener siempre una distancia mínima de 3 a 5 metros respecto a líneas aéreas."},
            {"icono": "user-check", "titulo": "Señalero exclusivo obligatorio", "texto": "Designar un rigger o señalero con vista despejada cuyo único rol sea alertar sobre la proximidad de cables."},
            {"icono": "shield", "titulo": "Vientos de guiado no conductores", "texto": "Utilizar cuerdas de fibra dieléctrica para orientar cargas suspendidas, jamás tocarlas directamente con las manos."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: investigaciones técnicas de accidentes por electrocución en grúas de OSHA 1926.1408 y normativas de seguridad eléctrica NFPA 70E.",
        "guionAudio": (
            "16 de julio de 2016. — En una obra de ampliación vial... un camión hidrogrúa realizaba maniobras de descarga de pesadas tuberías junto a la banquina. — "
            "A unos seis metros de altura... cruzaba una línea aérea de distribución eléctrica de treinta y tres kilovoltios. "
            "El operador de la grúa calculó la distancia a simple vista... sin un señalero dedicado que le indicara los ángulos ciegos "
            "y sin colocar balizas de delimitación física en el terreno. — "
            "Mientras izaba un tubo de hormigón... la pluma metálica giró y se aproximó a la línea eléctrica. "
            "Muchos creen que para electrocutarse se necesita tocar el cable... pero la media tensión no requiere contacto físico. — "
            "A menos de un metro... el aire se ionizó y un violento arco eléctrico de miles de voltios saltó desde la línea hacia la pluma. "
            "La corriente atravesó el acero de la grúa y descargó a tierra a través del cuerpo del ayudante... que en ese instante sostenía la carga con sus guantes comunes. — "
            "El trabajador falleció en el acto por shock eléctrico irreversible. "
            "La electricidad salta a distancia. En cercanía de líneas vivas... la distancia de seguridad no se negocia. — "
            "La seguridad... está en los detalles."
        )
    },
    {
        "id": "022",
        "fecha": "17 JULIO",
        "fechaPublicacion": "2026-07-17",
        "expediente": "Expediente #022",
        "carpeta": "1981-07-17-colapso-hyatt-regency",
        "titular": "UN CAMBIO DE DISEÑO EN OBRA PROVOCÓ EL COLAPSO MORTAL",
        "palabraResaltada": "CAMBIO DE DISEÑO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Hotel Hyatt Regency, Kansas City, Estados Unidos - 1981",
        "tipoRiesgo": "Ingeniería y Gestión del Cambio (MOC) / Integridad Estructural",
        "parrafos": [
            "La noche del 17 de julio de 1981, más de mil quinientas personas participaban en un baile en el atrio del Hotel Hyatt Regency de Kansas City, colmando las pasarelas aéreas suspendidas.",
            "Durante la construcción, el fabricante propuso cambiar el sistema de varillas continuas por varillas dobles escalonadas para facilitar el roscado, duplicando la carga sobre las vigas del cuarto piso.",
            "El cambio se aprobó informalmente sin recálculo de ingeniería. Las conexiones colapsaron repentinamente, dejando 114 fallecidos y más de 200 heridos en uno de los peores desastres estructurales de la historia."
        ],
        "puntosClave": [
            {"icono": "git-pull-request", "titulo": "Gestión del cambio de ingeniería (MOC)", "texto": "Toda modificación de planos o métodos de anclaje exige revisión y firma formal del calculista original."},
            {"icono": "clipboard-x", "titulo": "Prohibido acuerdos informales", "texto": "Nunca alterar detalles estructurales por conveniencia de montaje sin memoria de cálculo actualizada."},
            {"icono": "check-square-2", "titulo": "Inspección de conexiones críticas", "texto": "Los nudos y elementos sometidos a esfuerzos combinados de corte y tracción deben auditarse en campo antes del uso."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe final de investigación de desastres estructurales del National Bureau of Standards (NBS) e investigaciones de la ASCE.",
        "guionAudio": (
            "17 de julio de 1981. — En el moderno atrio del Hotel Hyatt Regency de Kansas City... más de mil quinientas personas bailaban y celebraban al compás de la música. — "
            "Muchos de los asistentes se congregaron en las espectaculares pasarelas peatonales suspendidas... que flotaban en el aire cruzando el lobby en los pisos segundo y cuarto. — "
            "Nadie en esa fiesta sospechaba que sobre sus cabezas pendía un error de ingeniería mortal. "
            "Durante la etapa de construcción... el taller metalúrgico propuso un cambio aparentemente menor en el diseño original: "
            "en lugar de usar varillas continuas de doce metros... colocaron varillas dobles escalonadas para enroscar las tuercas con mayor facilidad. — "
            "Nadie recalculó las cargas. Ese pequeño cambio duplicó el esfuerzo cortante sobre las vigas de la pasarela superior. — "
            "A las siete y cinco de la tarde... bajo el peso de la multitud... las tuercas de acero desgarraron las vigas. "
            "Las dos enormes pasarelas colapsaron una sobre otra... cayendo en picada desde decenas de metros sobre la multitud en la planta baja. — "
            "Ciento catorce personas perdieron la vida y más de doscientas resultaron gravemente heridas. "
            "En ingeniería y construcción... un cambio no analizado es una catástrofe asegurada. La gestión del cambio salva vidas. — "
            "La seguridad... está en los detalles."
        )
    }
]

def crear_portada_grafica(historia, output_path):
    """Genera una portada horizontal 16:9 (1920x1080) corporativa y elegante."""
    width, height = 1920, 1080
    img = Image.new("RGB", (width, height), color=(6, 17, 21))
    draw = ImageDraw.Draw(img)

    # Gradiente de fondo oscuro
    for y in range(height):
        factor = y / height
        r = int(6 + factor * 8)
        g = int(17 + factor * 14)
        b = int(21 + factor * 16)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Franja de acento superior neón
    draw.rectangle([0, 0, width, 12], fill=(25, 211, 230))

    # Cargar fuentes del sistema o usar default
    try:
        font_exp = ImageFont.truetype("arialbd.ttf", 36)
        font_title = ImageFont.truetype("arialbd.ttf", 62)
        font_sub = ImageFont.truetype("arial.ttf", 32)
        font_meta = ImageFont.truetype("arialbd.ttf", 28)
        font_badge = ImageFont.truetype("arialbd.ttf", 26)
    except:
        font_exp = ImageFont.load_default()
        font_title = font_exp
        font_sub = font_exp
        font_meta = font_exp
        font_badge = font_exp

    # Badge de cabecera: Expediente y Fecha
    badge_x = 100
    badge_y = 100
    draw.rectangle([badge_x, badge_y, badge_x + 380, badge_y + 54], fill=(25, 211, 230, 40), outline=(25, 211, 230), width=2)
    draw.text((badge_x + 18, badge_y + 12), f"{historia['fecha']} · {historia['expediente']}", font=font_badge, fill=(25, 211, 230))

    # Badge de tipo de riesgo
    draw.rectangle([width - 550, badge_y, width - 100, badge_y + 54], fill=(255, 77, 56, 40), outline=(255, 77, 56), width=2)
    draw.text((width - 530, badge_y + 12), historia['tipoRiesgo'], font=font_badge, fill=(255, 120, 100))

    # Marco decorativo tecnológico
    draw.rectangle([100, 200, width - 100, height - 160], outline=(151, 231, 255, 45), width=1)
    draw.line([100, 200, 160, 200], fill=(25, 211, 230), width=4)
    draw.line([100, 200, 100, 260], fill=(25, 211, 230), width=4)
    draw.line([width - 160, height - 160, width - 100, height - 160], fill=(25, 211, 230), width=4)
    draw.line([width - 100, height - 220, width - 100, height - 160], fill=(25, 211, 230), width=4)

    # Título principal (en varias líneas si es largo)
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
        y_text += 80

    # Subtítulo y lugar
    draw.text((140, y_text + 40), historia["subtitulo"], font=font_sub, fill=(196, 215, 220))
    draw.text((140, y_text + 100), f"📍 {historia['etiquetaImagen']}", font=font_meta, fill=(255, 212, 71))

    # Barra inferior Focus HSE
    draw.line([100, height - 120, width - 100, height - 120], fill=(151, 231, 255, 40), width=1)
    draw.text((140, height - 90), "FOCUS HSE · ARCHIVO HISTÓRICO DE SEGURIDAD", font=font_meta, fill=(25, 211, 230))
    draw.text((width - 480, height - 90), "LA SEGURIDAD ESTÁ EN LOS DETALLES", font=font_meta, fill=(159, 184, 192))

    img.save(output_path, "PNG")

def generar_archivos_efemeride(historia, kokoro_instance):
    """Genera carpeta, dossier markdown, README, audio y portada."""
    carpeta_nombre = historia["carpeta"]
    target_dir = os.path.join(ASSETS_DIR, carpeta_nombre)
    os.makedirs(target_dir, exist_ok=True)

    print(f"\n=======================================================")
    print(f"▶ Procesando: {historia['expediente']} ({historia['fecha']}) - {historia['titular'][:45]}...")
    print(f"=======================================================")

    # 1. README.md
    readme_content = f"""# Efeméride: {historia['fechaPublicacion']} {historia['carpeta']}

Guarda aquí los archivos de esta historia:

- `portada.png`: imagen principal.
- `historia.m4a`: audio narrado.
- `contenido-completo.md`: texto completo original de la efeméride.

Rutas configuradas en `historiaDelDia`:

```js
carpetaAssets: "assets/efemerides/{carpeta_nombre}/",
imagen: "portada.png",
audio: "historia.m4a",
```

Datos base:

- Expediente: `{historia['expediente']}`
- Fecha: `{historia['fecha']}`
- Lugar: `{historia['etiquetaImagen']}`
- Titular: `{historia['titular']}`
- Tipo de Riesgo: `{historia['tipoRiesgo']}`
"""
    with open(os.path.join(target_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

    # 2. contenido-completo.md
    md_content = f"""# 📁 ARCHIVO HSE

## {historia['expediente']}

# 📅 {historia['fechaPublicacion']}

# **"{historia['titular']}"**

### 📍 {historia['etiquetaImagen']}
**Tipo de Riesgo:** {historia['tipoRiesgo']}

---

# ¿Qué ocurrió?

{historia['parrafos'][0]}

{historia['parrafos'][1]}

{historia['parrafos'][2]}

---

# ⏱️ En cuestión de minutos...

{historia['guionAudio'].replace(' — ', '\n\n').replace('... ', '...\n\n')}

---

# 🦺 Tres puntos clave para controlar un evento similar

### 1️⃣ {historia['puntosClave'][0]['titulo']}
{historia['puntosClave'][0]['texto']}

---

### 2️⃣ {historia['puntosClave'][1]['titulo']}
{historia['puntosClave'][1]['texto']}

---

### 3️⃣ {historia['puntosClave'][2]['titulo']}
{historia['puntosClave'][2]['texto']}

---

# 💬 Para reflexionar

{historia['pregunta']}

> **"La seguridad está en los detalles."** — *Focus HSE*

---

# 📚 Fuentes

• {historia['fuente']}
"""
    with open(os.path.join(target_dir, "contenido-completo.md"), "w", encoding="utf-8") as f:
        f.write(md_content)

    # 3. Portada PNG
    portada_path = os.path.join(target_dir, "portada.png")
    if not os.path.exists(portada_path):
        crear_portada_grafica(historia, portada_path)
        print("  ✓ Portada generada (portada.png)")

    # 4. Síntesis de audio con Kokoro
    wav_path = os.path.join(target_dir, "historia.wav")
    m4a_path = os.path.join(target_dir, "historia.m4a")

    print(f"  🎙️ Sintetizando audio con Kokoro (speed={KOKORO_SPEED})...")
    samples, sample_rate = kokoro_instance.create(
        historia["guionAudio"],
        voice=KOKORO_VOICE,
        speed=KOKORO_SPEED,
        lang=KOKORO_LANG
    )
    sf.write(wav_path, samples, sample_rate)

    # 5. Conversión a M4A con ffmpeg
    print("  ⚙️ Convirtiendo a M4A optimizado...")
    cmd_ffmpeg = [
        "ffmpeg", "-i", wav_path,
        "-c:a", "aac", "-b:a", "192k",
        "-y", m4a_path
    ]
    subprocess.run(cmd_ffmpeg, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    # Eliminar WAV temporal
    if os.path.exists(wav_path):
        os.remove(wav_path)

    # Duración calculada
    duracion_seg = len(samples) / float(sample_rate)
    minutos = int(duracion_seg // 60)
    segundos = int(duracion_seg % 60)
    texto_duracion = f"Audio de {minutos} minutos {segundos:02d} segundos" if minutos > 0 else f"Audio de {segundos} segundos"
    historia["duracionAudio"] = texto_duracion
    print(f"  ✓ Audio listo: {m4a_path} ({texto_duracion})")

    return historia

def inyectar_en_index_html(historias_procesadas):
    """Inyecta las historias en el array historias de index.html."""
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Ubicar el final de Lac-Megantic (#012)
    marcador = 'carpetaAssets: "assets/efemerides/2013-07-07-lac-megantic/",'
    if marcador not in content:
        print("ERROR: No se encontró el marcador de Lac-Mégantic en index.html", file=sys.stderr)
        return False

    # Generar bloques JS
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

    # Insertar antes del cierre del array `    ];`
    pos_cierre = content.find("    ];\n\n    // Placeholder visual")
    if pos_cierre == -1:
        pos_cierre = content.find("    ];\r\n\r\n    // Placeholder visual")
    if pos_cierre == -1:
        # Fallback
        pos_cierre = content.find("    ];")

    if pos_cierre == -1:
        print("ERROR: No se encontró el cierre de historias en index.html", file=sys.stderr)
        return False

    nuevo_content = content[:pos_cierre] + texto_a_insertar + "\n" + content[pos_cierre:]

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(nuevo_content)

    print("\n✓ index.html actualizado exitosamente con las 10 nuevas efemérides.")
    return True

def main():
    print("Iniciando motor Kokoro...")
    kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

    procesadas = []
    for h in HISTORIAS_DATA:
        try:
            h_proc = generar_archivos_efemeride(h, kokoro)
            procesadas.append(h_proc)
        except Exception as e:
            print(f"Error procesando {h['expediente']}: {e}", file=sys.stderr)

    if inyectar_en_index_html(procesadas):
        print("\n🎉 ¡PROCESO AGÉNTICO COMPLETADO AL 100%!")
        print(f"Total procesadas: {len(procesadas)} historias")

if __name__ == "__main__":
    main()
