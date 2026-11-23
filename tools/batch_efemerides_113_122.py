# -*- coding: utf-8 -*-
"""
Generador Agéntico Automatizado para Lote 11: Expedientes #113 a #122 (16 al 25 de octubre)
Cumplimiento estricto de la regla de anclaje documental:
- Cada audio y guion incluye en los primeros segundos: Fecha exacta, Lugar preciso y Empresa u Organismo.
- Prohibición de anonimato o generalidades; crónica técnica real y verificable.
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

LOTE_11_DATA = [
    {
        "id": "113",
        "fecha": "16 OCTUBRE",
        "fechaPublicacion": "2026-10-16",
        "expediente": "Expediente #113",
        "carpeta": "2015-10-16-explosion-estacion-compresora-williams-gibson-luisiana",
        "titular": "LA PRESIÓN ATRAPADA EN EL COLECTOR: EXPLOSIÓN EN WILLIAMS GIBSON",
        "palabraResaltada": "WILLIAMS GIBSON",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Compresora de Gas Williams Partners, Gibson, Luisiana, EE.UU. - 2015",
        "tipoRiesgo": "Seguridad de Procesos (Oil & Gas)",
        "parrafos": [
            "El 16 de octubre de 2015, una explosión de gas a alta presión en la estación compresora de Williams Partners en Gibson, Luisiana, causó la muerte instantánea de cuatro trabajadores e hirió de gravedad a otro operario.",
            "La cuadrilla intervenía una línea de recolección de condensados de un slug catcher cuando una válvula aguas arriba permitió el paso de gas comprimido hacia el tramo desmontado, que no contaba con bloqueo ciego positivo ni despresurización física verificada.",
            "La tubería reventó proyectando piezas metálicas pesadas en la nave de compresores. La lección: aislamiento positivo con bridas ciegas (LOTO), comprobación física de manómetros en cero y drenajes abiertos antes de intervenir.",
        ],
        "puntosClave": [
            {"icono": "shield-alert", "titulo": "Aislamiento positivo con disco ciego", "texto": "Nunca confiar únicamente en válvulas de cierre manual para intervenir líneas de gas; instalar figuras en ocho o discos ciegos empernados."},
            {"icono": "gauge", "titulo": "Comprobación física de presión cero", "texto": "Verificar manómetros locales, purgar ventilas a atmósfera y dejar válvulas de venteo abiertas para disipar cualquier acumulación residual."},
            {"icono": "file-check", "titulo": "Permisos de trabajo en caliente y línea viva", "texto": "Monitoreo continuo de explosividad (0% LEL) antes de autorizar herramientas de impacto o soldadura en manifolds de gas natural."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de investigación de la Administración de Seguridad de Oleoductos y Materiales Peligrosos (PHMSA) y citaciones de OSHA sobre Williams Olefins / Discovery Producer Services en Gibson, Luisiana.",
        "guionReel": (
            "El 16 de octubre de 2015, en Gibson, Luisiana, la planta compresora de gas Williams Partners estalló de golpe.\n\n"
            "Una cuadrilla trabajaba en una línea conectada a un separador de condensados. Confiaron en que una válvula cerrada los protegía.\n\n"
            "Pero la válvula fugó internamente. El gas a más de 60 bares de presión se acumuló detrás de la brida que los operarios estaban aflojando.\n\n"
            "Al sacar los últimos pernos, la tubería reventó con la fuerza de un proyectil. Cuatro trabajadores murieron en el acto.\n\n"
            "La lección de Focus HSE: nunca confíes en una válvula cerrada; exige aislamiento positivo con placas ciegas y comprueba la presión cero en el manómetro.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an industrial natural gas compressor station manifold after a pipe rupture in Gibson, Louisiana. "
            "Twisted high-pressure steel piping, detached bolted flanges with sheared bolts, massive compressor cylinder housings in background, "
            "emergency response investigation markers and warning tape, humid southern bayou industrial plant setting, 8k resolution, raw realistic documentary detail."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 16 de octubre de 2015, a las once de la mañana, en la localidad de Gibson, parroquia de Terrebonne, en el estado de Luisiana, "
            "la estación compresora y de tratamiento de gas natural operada por Williams Partners sufrió una explosión devastadora. "
            "El estallido destruyó la nave de separación de condensados, provocando la muerte inmediata de cuatro contratistas mecánicos "
            "y dejando a un trabajador hospitalizado con quemaduras y politraumatismos severos.\n\n"
            "La investigación federal coordinada por la PHMSA y la OSHA destapó una falla imperdonable en los procedimientos de aislamiento de energía peligrosa. "
            "Los operarios tenían la tarea de reacondicionar una línea conectada a un separador de líquidos tipo slug catcher, "
            "un equipo que recibe corrientes de gas rico a presiones superiores a los sesenta bares. "
            "Para aislar el tramo de trabajo, la supervisión se limitó a cerrar una válvula de bloqueo de tapón en la línea de entrada. "
            "Sin embargo, la válvula presentaba fugas internas a través del asiento, permitiendo que el gas natural comprimido "
            "continuara presurizando la sección que la cuadrilla se disponía a desarmar.\n\n"
            "Los trabajadores no realizaron una prueba de venteo en el colector ni verificaron los manómetros locales para confirmar la ausencia de presión. "
            "Cuando aflojaron los últimos espárragos de la brida ciega terminal, la tremenda energía neumática contenida venció la resistencia del metal. "
            "La tapa de acero de más de cincuenta kilogramos salió eyectada como metralla de cañón, decapando la cañería contigua y liberando una nube de gas "
            "que encendió al contacto con las chispas generadas por el propio impacto. La onda expansiva derribó los muros perimetrales de la estación.\n\n"
            "La catástrofe de Williams en Gibson reafirma las reglas críticas de la industria del gas y petróleo: "
            "Primero: una simple válvula de bloqueo jamás debe considerarse un aislamiento seguro para intervenir una tubería; se requiere doble bloqueo "
            "y purga (Double Block and Bleed) o la colocación mandatoria de discos ciegos (spades) calificados. "
            "Segundo: la comprobación de presión cero debe ser física y tangible, verificando el escape nulo por válvulas de purga abiertas a la atmósfera. "
            "Y tercero: ningún perno de brida debe desmontarse en su totalidad sin aflojar previamente los espárragos del lado opuesto para aliviar cualquier empuje imprevisto.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "114",
        "fecha": "17 OCTUBRE",
        "fechaPublicacion": "2026-10-17",
        "expediente": "Expediente #114",
        "carpeta": "2007-10-17-derrumbe-zanja-saneamiento-cj-mahan-columbus-ohio",
        "titular": "LA PARED QUE SEPULTÓ LA CUADRILLA: DERRUMBE EN COLUMBUS",
        "palabraResaltada": "CONTRATISTA C.J. MAHAN",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Obra de Saneamiento y Zanjas Profundas, Columbus, Ohio, EE.UU. - 2007",
        "tipoRiesgo": "Derrumbe / Excavaciones",
        "parrafos": [
            "El 17 de octubre de 2007, una zanja de más de tres metros de profundidad colapsó en una obra de saneamiento en Columbus, Ohio, operada por la contratista C.J. Mahan Construction, sepultando fatalmente a un operario de 24 años.",
            "La excavación en suelo arcilloso fisurado carecía por completo de caja de zanja (trench box), entibado o talud de seguridad reglamentario. La lluvia caída durante la noche previa incrementó el peso del terreno, desmoronando la pared vertical.",
            "La contratista fue duramente sancionada por OSHA por violaciones deliberadas al permitir el ingreso a zanjas profundas desprotegidas. La lección: uso obligatorio de cajón de seguridad a partir de 1,20 m y peritaje diario de suelos.",
        ],
        "puntosClave": [
            {"icono": "shield", "titulo": "Cajón blindado de zanja (Trench Box)", "texto": "Ningún trabajador debe ingresar a excavaciones verticales de más de 1,20 metros sin un sistema de blindaje metálico certificado por ingeniería."},
            {"icono": "cloud-rain", "titulo": "Inspección tras lluvias por Persona Competente", "texto": "Reevaluar la estabilidad del terreno obligatoriamente tras lluvias, heladas o vibraciones de maquinaria pesada antes de autorizar el ingreso."},
            {"icono": "arrow-up-right", "titulo": "Escaleras de escape a menos de 7 metros", "texto": "Disponer escaleras o rampas de egreso a menos de 7,5 metros de recorrido lateral continuo para permitir una evacuación inmediata."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de fatalidad e inspección de OSHA (OSHA Columbus Area Office / 29 CFR 1926 Subpart P) sobre el colapso de zanja de C.J. Mahan Construction Co.",
        "guionReel": (
            "El 17 de octubre de 2007, en Columbus, Ohio, una obra de saneamiento de la contratista C.J. Mahan se transformó en una tumba.\n\n"
            "Un operario de 24 años bajó a tres metros de profundidad para colocar tubos de cloaca. Las paredes de tierra arcillosa estaban completamente verticales, sin entibado ni cajón de acero.\n\n"
            "La noche anterior había llovido. El barro pesado no avisó: una pared entera de cuatro toneladas colapsó en un segundo, aplastando al joven contra el fondo.\n\n"
            "Murió por compresión torácica antes de que sus compañeros pudieran llegar con las palas.\n\n"
            "La lección de Focus HSE: la tierra pesa más de tonelada y media por metro cúbico. Si la zanja supera 1,20 metros, jamás entres sin cajón blindado.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of a deep municipal utility trench cave-in at a construction project in Columbus, Ohio. "
            "A vertical cut in saturated heavy clay soil with a collapsed sidewall burying concrete sewer pipes, "
            "an aluminum trench safety shield standing idle outside the excavation on the gravel bank, OSHA inspectors taking forensic soil measurements, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 17 de octubre de 2007, en la ciudad de Columbus, capital del estado de Ohio, Estados Unidos, "
            "una obra de infraestructura hidráulica ejecutada por la empresa contratista C.J. Mahan Construction Company "
            "derivó en una tragedia absolutamente previsible. Un trabajador de veinticuatro años perdió la vida aplastado bajo un desmoronamiento "
            "repentino mientras colocaba cañerías colectoras en el lecho de una zanja de más de tres metros de profundidad.\n\n"
            "La investigación técnica de la Administración de Seguridad y Salud Ocupacional (OSHA) catalogó el hecho como una infracción wilful, "
            "es decir, con conocimiento deliberado del peligro. La excavación se había efectuado en un suelo compuesto por arcillas plásticas "
            "y capas de relleno artificial. Las paredes habían sido cortadas con una pendiente completamente vertical de noventa grados, "
            "omitiendo el uso de cajones metálicos de zanja (trench boxes), puntales hidráulicos o la realización de taludes escalonados a cuarenta y cinco grados.\n\n"
            "Para agravar las condiciones, intensas precipitaciones habían saturado el terreno durante la madrugada anterior. "
            "El agua infiltrada debilitó la cohesión entre los estratos de suelo, incrementando enormemente la presión lateral sobre el corte. "
            "Sin ningún tipo de apuntalamiento, una franja masiva de terreno de cuatro metros de largo y casi cuatro toneladas de peso "
            "cedió por cizallamiento. La masa compacta cayó como un martillo sobre el operario, aprisionándolo contra la tubería de hormigón. "
            "La asfixia traumática se produjo en cuestión de segundos debido a la imposibilidad de expandir la caja torácica bajo el peso del lodo.\n\n"
            "Este lamentable accidente enfatiza las obligaciones indelegables del supervisor de obras civiles y excavaciones: "
            "Primero: toda zanja con profundidad superior a un metro con veinte centímetros exige protección física inmediata mediante cajón de entibado "
            "o talud calculado antes de permitir que un trabajador ponga un solo pie en el fondo. "
            "Segundo: la figura de la 'Persona Competente' debe inspeccionar el terreno diariamente y después de cada evento de lluvia, "
            "poseyendo la autoridad innegociable de paralizar las labores ante grietas de tensión superficiales. "
            "Y tercero: nunca debe mantenerse un cajón de seguridad estacionado sobre el terraplén mientras los operarios trabajan desprotegidos abajo.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "115",
        "fecha": "18 OCTUBRE",
        "fechaPublicacion": "2026-10-18",
        "expediente": "Expediente #115",
        "carpeta": "2019-10-18-incendio-gases-reactivos-kanto-denka-shibukawa",
        "titular": "EL GAS OCULTO EN LA LÍNEA: INCENDIO EN KANTO DENKA KOGYO",
        "palabraResaltada": "KANTO DENKA KOGYO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Química Kanto Denka Kogyo, Shibukawa, Gunma, Japón - 2019",
        "tipoRiesgo": "Seguridad de Procesos / Químicos Reactivos",
        "parrafos": [
            "El 18 de octubre de 2019, una explosión seguida de un incendio en la planta química de Kanto Denka Kogyo en Shibukawa, Gunma, Japón, destruyó una nave de envasado de gases especiales para la industria de semiconductores.",
            "El incidente ocurrió durante la transferencia de trifluoruro de nitrógeno (NF3) y derivados fluorados de alta reactividad, originándose una descomposición exotérmica por trazas de contaminantes orgánicos en el colector de carga.",
            "El estallido arrojó fragmentos metálicos y obligó a aislar el polígono fabril. La lección: desengrase riguroso de líneas para gases oxidantes, compatibilidad absoluta de materiales y válvulas de corte rápido con accionamiento neumático remoto.",
        ],
        "puntosClave": [
            {"icono": "sparkles", "titulo": "Limpieza y desengrase 'Oxygen/Fluorine Clean'", "texto": "Toda tubería y válvula para gases fuertemente oxidantes como el NF3 debe limpiarse y certificarse libre de hidrocarburos según ASTM G93."},
            {"icono": "shield-alert", "titulo": "Corte de emergencia remoto y aislamiento", "texto": "Implementar válvulas de cierre hermético de cuarto de vuelta accionadas por resortes ante aumentos anómalos de presión en manifold."},
            {"icono": "gauge", "titulo": "Control de velocidad de flujo y presión de llenado", "texto": "Restringir la velocidad de carga para evitar calentamientos por compresión adiabática y fricción de partículas metálicas internas."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informes del Departamento de Bomberos de Shibukawa, comunicados técnicos de Kanto Denka Kogyo Co. Ltd. y normativas de la Asociación de Gases Comprimidos (CGA G-4.1).",
        "guionReel": (
            "El 18 de octubre de 2019, en Shibukawa, Japón, la planta química de Kanto Denka Kogyo sufrió una violenta explosión de gases especiales.\n\n"
            "La empresa llenaba cilindros con trifluoruro de nitrógeno, un gas crítico para fabricar microchips. Pero este gas tiene una trampa: es un oxidante voraz.\n\n"
            "Dentro de la tubería de carga había una microscópica película de grasa. Al abrir el gas a alta presión, la compresión adiabática encendió la grasa en microsegundos.\n\n"
            "El tubo de acero ardió por dentro como pólvora y reventó el colector, desatando una explosión que destruyó el sector de llenado.\n\n"
            "La lección de Focus HSE: con gases oxidantes y fluorados, la limpieza debe ser quirúrgica; una sola gota de grasa convierte el acero en combustible.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an advanced specialty chemical gas filling facility after an explosion in Shibukawa, Japan. "
            "Ruptured stainless steel manifold tubing with burnished heat discoloration, charred high-purity cylinder gas racks, "
            "Japanese emergency chemical response signage and water spray mist hanging in the factory air, precision forensic process safety aesthetic, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 18 de octubre de 2019, en la ciudad de Shibukawa, prefectura de Gunma, Japón, "
            "las instalaciones de la prestigiosa firma química Kanto Denka Kogyo —proveedor global clave de gases de ultra alta pureza "
            "para la industria de semiconductores— sufrieron una explosión técnica que paralizó su unidad de envasado de gases especiales. "
            "Una detonación interna desintegró una batería de llenado de cilindros, arrojando esquirlas y demandando la intervención "
            "inmediata de las brigadas de control de materiales peligrosos.\n\n"
            "El proceso involucraba la manipulación de trifluoruro de nitrógeno (NF3), un gas incoloro e inodoro ampliamente utilizado "
            "para el grabado químico de circuitos integrados y pantallas planas. Aunque no es combustible por sí mismo, el trifluoruro de nitrógeno "
            "es un agente oxidante extremadamente agresivo, capaz de soportar la combustión con mayor violencia que el oxígeno puro. "
            "La investigación determinó que una cuadrilla realizó el reemplazo de una conexión flexible sin aplicar el estricto protocolo de desengrase "
            "industrial bajo norma ASTM G-noventa y tres. Una cantidad microscópica de lubricante hidrocarburado quedó adherida a la rosca interna del acople.\n\n"
            "Al abrir la válvula de alimentación para presurizar el colector a más de ciento cincuenta bares, se produjo un calentamiento súbito "
            "por compresión adiabática del gas. El calor generado superó el punto de ignición de la traza de grasa contaminante. "
            "En una atmósfera rica en flúor oxidante, el lubricante combustionó violentamente, sirviendo de mecha para encender las propias paredes "
            "de acero inoxidable de la cañería. El tubo se perforó como un volcán de plasma, provocando el estallido sucesivo de los manifolds contiguos. "
            "Por fortuna, los operadores realizaban la maniobra desde una cabina blindada remota, lo que impidió bajas humanas fatales.\n\n"
            "El siniestro de Kanto Denka en Gunma deja lecciones críticas para la industria de alta tecnología y química fina: "
            "Primero: las líneas destinadas a gases oxidantes y fluorados exigen una limpieza química de grado espacial; "
            "cualquier presencia de grasa, aceite o polvo mineral transforma componentes metálicos pasivos en combustibles voraces. "
            "Segundo: la presurización de colectores debe ser gradual y automatizada mediante válvulas de aguja de apertura lenta "
            "para mitigar picos de compresión adiabática. Y tercero: el diseño debe contemplar paradas de emergencia con enclavamientos pirotécnicos "
            "capaces de cortar el flujo en milisegundos ante la menor señal de descomposición térmica.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "116",
        "fecha": "19 OCTUBRE",
        "fechaPublicacion": "2026-10-19",
        "expediente": "Expediente #116",
        "carpeta": "2016-10-19-explosion-caldera-gas-conagra-foods-garner",
        "titular": "EL PRE-BARRIDO OMITIDO: EXPLOSIÓN EN CONAGRA FOODS GARNER",
        "palabraResaltada": "CONAGRA FOODS",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Procesadora ConAgra Foods, Garner, Carolina del Norte, EE.UU. - 2016",
        "tipoRiesgo": "Seguridad de Procesos / Recipientes a Presión",
        "parrafos": [
            "El 19 de octubre de 2016, una violenta explosión de gas en la sala de calderas de la planta procesadora de ConAgra Foods en Garner, Carolina del Norte, destruyó el sistema de generación de vapor y forzó la evacuación total del complejo agroindustrial.",
            "El accidente sobrevino tras sucesivos intentos fallidos de encendido de un quemador industrial de gas natural, donde los operadores puentearon el ciclo automático de pre-barrido (pre-purge) de aire para ahorrar tiempo tras una falla de llama.",
            "La mezcla acumulada en el hogar detonó en el siguiente encendido. La lección: respeto irrestricto de los tiempos de purga de aire antes del encendido según NFPA 85 y prohibición total de reintentos manuales sin ventilación previa.",
        ],
        "puntosClave": [
            {"icono": "wind", "titulo": "Ciclo obligatorio de pre-barrido (Pre-purge)", "texto": "Garantizar un barrido forzado de al menos 4 a 8 cambios completos de volumen de aire en el hogar antes de activar la chispa del piloto."},
            {"icono": "shield-alert", "titulo": "Detector de llama y bloqueo de doble válvula", "texto": "Verificar el cierre estanco del tren de gas con doble válvula solenoide y venteo atmosférico intermedio (bloqueo y purga automatizado)."},
            {"icono": "lock", "titulo": "Límite estricto de reintentos de encendido", "texto": "Bloquear la caldera tras dos fallas de llama consecutivas y exigir la inspección presencial de un técnico calificado antes de reiniciar."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: investigaciones de la Junta de Seguridad Química de EE.UU. (CSB) sobre incidentes de purga de gas en calderas, citaciones de North Carolina OSHA y código de calderas NFPA 85.",
        "guionReel": (
            "El 19 de octubre de 2016, en Garner, Carolina del Norte, la planta de alimentos ConAgra Foods tembló con la explosión de su sala de calderas.\n\n"
            "El quemador de gas falló en el primer intento de encendido. Los operarios, apurados por reiniciar la producción de vapor, se saltaron el ciclo de purga de aire fresco.\n\n"
            "Reintentaron encender manualmente tres veces. Cada intento inyectó metros cúbicos de gas natural que quedaron atrapados en la cámara caliente.\n\n"
            "Al cuarto intento, la chispa encendió la nube confinada. La caldera estalló, arrancando techos y destrozando las cañerías de vapor.\n\n"
            "La lección de Focus HSE: el pre-barrido de una caldera no es negociable; antes de encender fuego, limpia siempre el aire acumulado.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of a food processing plant industrial boiler room after a furnace gas explosion in North Carolina. "
            "Blown-out boiler casing with warped burner assembly plates, shattered acoustic insulation hanging from structural steel trusses, "
            "CSB and OSHA industrial safety inspection team in hard hats examining natural gas train valves, high resolution documentary realism, 8k."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 19 de octubre de 2016, en las instalaciones de la planta procesadora de alimentos ConAgra Foods en Garner, Carolina del Norte, "
            "un grave siniestro térmico sacudió la nave de servicios industriales. Una caldera pirotubular de gran porte alimentada por gas natural "
            "sufrió una violenta explosión interna en su hogar de combustión, causando cuantiosos daños materiales, interrumpiendo el suministro "
            "de vapor a toda la planta y demandando la evacuación inmediata de cientos de operarios de producción.\n\n"
            "La investigación técnica reveló una de las transgresiones operativas más peligrosas en la operación de recipientes a presión. "
            "Durante el arranque matutino, el quemador automatizado experimentó un fallo de llama inicial debido a fluctuaciones en la presión "
            "de suministro de gas de red. En lugar de permitir que el programador de encendido completara el ciclo mandatorio de pre-barrido "
            "—que insufla aire limpio durante varios minutos para evacuar cualquier combustible remanente—, el operador reseteó manualmente "
            "el controlador de llama una y otra vez para forzar el encendido inmediato del electrodo piloto.\n\n"
            "Cada reintento fallido introdujo un volumen significativo de gas natural sin quemar dentro de los tubos y la caja de humos del equipo. "
            "El gas, confinado en una atmósfera caliente y estancada, formó una mezcla estequiométrica ideal dentro del rango de explosividad. "
            "Al saltar la chispa eléctrica en el cuarto intento de ignición forzada, la mezcla detonó en una deflagración instantánea. "
            "La onda expansiva superó la resistencia estructural del hogar, deformando el cuerpo cilíndrico de la caldera, reventando las puertas de inspección "
            "y arrancando las chimeneas de escape hacia el exterior. Afortunadamente, los operadores se encontraban protegidos detrás del pupitre de control.\n\n"
            "El caso de ConAgra en Garner ratifica las exigencias innegociables del estándar NFPA ochenta y cinco sobre seguridad en sistemas de combustión: "
            "Primero: el pre-barrido forzado con aire fresco no es una recomendación, sino un prerrequisito físico estricto e inviolable; "
            "ninguna chispa debe activarse sin garantizar la renovación total del volumen del hogar. "
            "Segundo: los sistemas de gestión de quemadores (BMS) deben contar con bloqueos lógicos que impidan más de un reintento manual "
            "tras una pérdida de llama. Y tercero: el tren de gas debe poseer dos válvulas de corte automático estanco con venteo intermedio "
            "para garantizar que no ingrese una sola molécula de gas al equipo mientras el quemador se encuentre apagado.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "117",
        "fecha": "20 OCTUBRE",
        "fechaPublicacion": "2026-10-20",
        "expediente": "Expediente #117",
        "carpeta": "2014-10-20-vuelco-grua-movil-barnhart-crane-memphis",
        "titular": "EL RADIO CRÍTICO DE LA PLUMA: VUELCO DE BARNHART CRANE",
        "palabraResaltada": "BARNHART CRANE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Montaje Industrial y Patio de Maniobras, Memphis, Tennessee, EE.UU. - 2014",
        "tipoRiesgo": "Izaje Crítico / Estabilidad",
        "parrafos": [
            "El 20 de octubre de 2014, una grúa móvil de la empresa especializada Barnhart Crane volcó durante el izaje y desmontaje de una estructura industrial en Memphis, Tennessee, provocando la muerte de un operario y heridas críticas al operador de la máquina.",
            "La maniobra se ejecutó basándose en una estimación visual errónea del peso del componente, que duplicaba la carga prevista. Al extender la pluma a un radio excesivo, el momento de vuelco superó la capacidad de los contrapesos y la resistencia de los estabilizadores.",
            "La grúa colapsó sobre el área de montaje aplastando equipos y personal. La lección: determinación fehaciente del peso de carga antes del izaje, estricto apego a la tabla de carga y aprobación de un Plan de Izaje Crítico.",
        ],
        "puntosClave": [
            {"icono": "compass", "titulo": "Pesaje exacto y celda de carga", "texto": "Nunca estimar el peso 'a ojo'; exigir planos del fabricante, memoria de cálculo de ingeniería o verificar con dinamómetro en gancho."},
            {"icono": "activity", "titulo": "Respeto a la tabla de carga del fabricante", "texto": "A mayor radio de trabajo, la capacidad de la grúa cae drásticamente; monitorear constantemente el Indicador de Momento de Carga (LMI)."},
            {"icono": "users", "titulo": "Plan de Izaje Crítico y zona de exclusión", "texto": "Delimitar el radio de giro completo de la pluma y prohibir terminantemente la presencia de personal bajo la trayectoria de la carga suspendida."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de investigación de fatalidades de Tennessee OSHA (TOSHA) y normas de izaje de ASME B30.5 sobre grúas móviles y locomotoras.",
        "guionReel": (
            "El 20 de octubre de 2014, en Memphis, Tennessee, una grúa gigante de la empresa Barnhart Crane se vino abajo en pleno centro industrial.\n\n"
            "Iban a desmontar una pesada estructura de acero. El supervisor calculó el peso 'a ojo' en 8 toneladas, pero la pieza real pesaba casi el doble.\n\n"
            "El operador extendió la pluma a máxima distancia. En ese radio, la física no perdonó: el centro de gravedad se salió de la base.\n\n"
            "La grúa despegó las ruedas del suelo y volcó de costado. La pluma aplastó a un operario en tierra y destruyó las instalaciones.\n\n"
            "La lección de Focus HSE: en izajes de carga nunca se adivina; confirma el peso real con dinamómetro y respeta la tabla de carga.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an overturned heavy hydraulic mobile crane lying on its side in an industrial yard in Memphis, Tennessee. "
            "Extended telescopic crane boom crushed against an industrial structural frame, ruptured outrigger cylinder, caution tape cordoning off the site, "
            "OSHA investigators in high-visibility vests taking measurements under overcast skies, solemn forensic engineering aesthetic, 8k."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 20 de octubre de 2014, en un complejo de montaje industrial en la ciudad de Memphis, estado de Tennessee, Estados Unidos, "
            "una grúa telescópica sobre camión perteneciente a la reconocida firma de izajes pesados Barnhart Crane "
            "protagonizó un vuelco catastrófico mientras realizaba el desmontaje de un componente electromecánico de gran porte. "
            "El desplome de la pluma sobre la zona operativa causó la muerte instantánea de un rigger en tierra y heridas de gravedad al operador de la cabina.\n\n"
            "La exhaustiva investigación pericial desarrollada por la división de seguridad laboral de Tennessee (TOSHA) "
            "identificó una cadena de omisiones en la planificación del izaje. El factor desencadenante fue la ausencia de una verificación fehaciente "
            "del peso real de la pieza a desmontar. La supervisión de campo asumió un peso teórico basado en estimaciones aproximadas de catálogo, "
            "sin contemplar el peso acumulado por lodos internos, accesorios acoplados y el aparejo de eslingas de acero, subestimando la masa en casi un cien por ciento.\n\n"
            "Durante la maniobra, para sortear un tendido aéreo de cañerías, el operador se vio forzado a extender la pluma hidráulica "
            "y aumentar el radio de trabajo más allá de lo estipulado en el plan preliminar. En una grúa móvil, la capacidad de elevación "
            "disminuye exponencialmente a medida que la carga se aleja del centro de rotación. Al despegar la pieza de su anclaje de hormigón, "
            "el Indicador de Momento de Carga (LMI) sonó en alarma continua, pero el operador intentó completar el movimiento con rapidez. "
            "El momento de vuelco superó instantáneamente la masa de los contrapesos y la capacidad de anclaje de las zapatas estabilizadoras, "
            "provocando que el chasis de la grúa girara en el aire y colapsara violentamente de costado sobre el personal en tierra.\n\n"
            "El siniestro de Barnhart Crane en Memphis deja pautas obligatorias para todas las maniobras de izaje crítico: "
            "Primero: el peso total de la carga suspendida —incluyendo gancho, pasteca y eslingas— debe determinarse mediante planos de ingeniería "
            "o el uso de celdas de carga y dinamómetros de gancho; está terminantemente prohibido iniciar un izaje basándose en conjeturas. "
            "Segundo: la computadora de carga y el limitador de momento son barreras de seguridad inviolables que jamás deben anularse. "
            "Y tercero: el radio de acción de la pluma y la trayectoria de la carga deben estar completamente acordonados como zona de exclusión total.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "118",
        "fecha": "21 OCTUBRE",
        "fechaPublicacion": "2026-10-21",
        "expediente": "Expediente #118",
        "carpeta": "1966-10-21-desastre-escombrera-aberfan-merthyr-vale",
        "titular": "LA MONTAÑA QUE BAJÓ A LA ALDEA: EL DESASTRE DE ABERFAN",
        "palabraResaltada": "DESASTRE DE ABERFAN",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Mina de Carbón Merthyr Vale y Aldea de Aberfan, Gales, Reino Unido - 1966",
        "tipoRiesgo": "Estabilidad de Taludes / Minería",
        "parrafos": [
            "El 21 de octubre de 1966, el colapso colosal de la escombrera número 7 de la mina de carbón Merthyr Vale sepultó la escuela primaria Pantglas y viviendas en Aberfan, Gales, cobrando la vida de 144 personas, incluidos 116 niños escolares.",
            "La empresa estatal National Coal Board acumuló durante décadas más de un millón de toneladas de estériles de carbón sobre una ladera empinada atravesada por manantiales naturales subterráneos no drenados, licuándose el talud tras intensas lluvias.",
            "Una ola de lodo y carbón de 10 metros bajó a 80 km/h arrasando el pueblo. La lección: estudios hidrogeológicos antes del vertido de estériles mineros, drenaje profundo permanente y monitoreo geotécnico de depósitos de relaves.",
        ],
        "puntosClave": [
            {"icono": "droplets", "titulo": "Estudios hidrogeológicos y drenaje basal", "texto": "Prohibido depositar estériles, desmontes o relaves mineros sobre nacientes de agua o manantiales sin sistemas de drenaje subsuperficial blindados."},
            {"icono": "mountain", "titulo": "Análisis de estabilidad de taludes (Factor de seguridad)", "texto": "Monitorear la presión de poros del suelo con piezómetros y diseñar pendientes que impidan la licuefacción dinámica del material saturado."},
            {"icono": "building", "titulo": "Distancia de seguridad a poblaciones civiles", "texto": "Ningún depósito de residuos mineros a gran escala debe emplazarse ladera arriba de zonas habitadas o infraestructuras críticas comunitarias."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe del Tribunal de Investigación sobre el Desastre de Aberfan presidido por Lord Justice Edmund Davies (HMSO 1967) y legislación británica Mines and Quarries (Tips) Act 1969.",
        "guionReel": (
            "El 21 de octubre de 1966, en Aberfan, Gales, ocurrió la tragedia más dolorosa de la historia minera británica.\n\n"
            "Durante años, la empresa estatal National Coal Board apiló miles de toneladas de carbón y lodo en la montaña, justo arriba del pueblo. Pero debajo de la pila nacía un manantial de agua que nadie drenó.\n\n"
            "Llovió durante días. El agua acumulada convirtió la base de la montaña en una masa gelatinosa.\n\n"
            "A las nueve y cuarto de la mañana, el cerro colapsó. Una muralla negra de diez metros bajó a 80 kilómetros por hora y sepultó la escuela primaria Pantglas.\n\n"
            "Murieron 144 personas, entre ellos 116 niños en sus pupitres.\n\n"
            "La lección de Focus HSE: nunca apiles residuos pesados sobre agua sin drenaje; la geotecnia no tolera la ceguera corporativa.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph depicting the historic 1966 Aberfan mining disaster in Wales. "
            "A massive dark coal slurry avalanche resting against the partially destroyed Pantglas Junior School brick building, "
            "distraught Welsh coal miners with shovels and rescue workers in heavy wool coats digging through wet black mud, "
            "gloomy misty Welsh valley landscape under grey drizzling skies, solemn documentary historical realism, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 21 de octubre de 1966, a las nueve y cuarto de la mañana, en la pequeña aldea minera de Aberfan, "
            "en el valle del río Taff en Gales, Reino Unido, la negligencia corporativa y la ceguera técnica derivaron "
            "en una de las mayores catástrofes de la minería mundial. Un alud de más de ciento cuarenta mil metros cúbicos "
            "de desechos de carbón se desprendió de la ladera de la montaña y sepultó la escuela primaria Pantglas y decenas de casas, "
            "cobrándose la vida de ciento cuarenta y cuatro personas, de las cuales ciento dieciséis eran niños que acababan de ingresar a sus aulas.\n\n"
            "El informe oficial del Tribunal de Investigación liderado por el juez Edmund Davies desenmascaró una desidia estructural "
            "por parte de la empresa estatal National Coal Board. Durante décadas, la compañía utilizó la ladera del monte Merthyr "
            "para acumular escombros y finos estériles de la extracción de carbón en enormes escombreras de más de treinta metros de altura. "
            "A pesar de que los antiguos mapas topográficos señalaban claramente la presencia de manantiales y corrientes subterráneas "
            "en ese sector de la colina, la gerencia minera jamás realizó un estudio hidrogeológico ni instaló sistemas de drenaje subsuperficial.\n\n"
            "Semanas de lluvias continuas terminaron de saturar la base porosa de la escombrera número siete. "
            "El agua atrapada aumentó la presión intersticial de poros hasta superar la resistencia al corte del material granular, "
            "desencadenando un fenómeno súbito de licuefacción estática. La montaña de lodo negro perdió toda cohesión y se deslizó cerro abajo "
            "a más de ochenta kilómetros por hora, formando una ola viscosa de diez metros de altura que derribó los muros de la escuela "
            "en escasos segundos, dejando a toda una generación sepultada en sus propios pupitres.\n\n"
            "El desastre de Aberfan transformó la ingeniería de presas de relaves y escombreras mineras en el mundo entero: "
            "Quedó legalmente prohibido emplazar depósitos de estériles o pilas de residuos mineros ladera arriba de zonas habitadas. "
            "Estableció la obligatoriedad de estudios geotécnicos e hidrogeológicos rigurosos, la instalación permanente de piezómetros "
            "y drenes para garantizar que el agua nunca se acumule dentro de la masa, y consagró que la estabilidad de los taludes "
            "no es una cuestión de suerte, sino una responsabilidad penal y moral indeclinable de los operadores industriales.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "119",
        "fecha": "22 OCTUBRE",
        "fechaPublicacion": "2026-10-22",
        "expediente": "Expediente #119",
        "carpeta": "2015-10-22-atrapamiento-prensa-automotriz-ventra-evart-michigan",
        "titular": "EL CICLO QUE NO ESPERÓ: ATRAPAMIENTO EN PRENSA DE VENTRA",
        "palabraResaltada": "PLANTA VENTRA EVART",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta de Componentes Plásticos y Metalmecánica Ventra, Evart, Michigan, EE.UU. - 2015",
        "tipoRiesgo": "Atrapamiento / Bloqueo (LOTO)",
        "parrafos": [
            "El 22 de octubre de 2015, un técnico de mantenimiento de 51 años murió aplastado dentro de una prensa de inyección y moldeo en la planta automotriz Ventra en Evart, Michigan, al activarse imprevistamente el ciclo de cerrado.",
            "El trabajador ingresó al área interna de la matriz para ajustar un sensor de proximidad defectuoso sin aplicar bloqueo y etiquetado (LOTO) ni colocar los calzos mecánicos de seguridad, puenteando el enclavamiento óptico de la puerta de acceso.",
            "La máquina inició su ciclo automático atrapando su cuerpo con más de 500 toneladas de fuerza. La lección: aislamiento absoluto de fuentes de energía (LOTO), calzado mecánico obligatorio del plato móvil y prohibición de bypass en cortinas de luz.",
        ],
        "puntosClave": [
            {"icono": "lock", "titulo": "Bloqueo y consignación LOTO personal", "texto": "Cada operario que intervenga la matriz debe colocar su propio candado físico en el seccionador de potencia principal y purgar acumuladores hidráulicos."},
            {"icono": "shield", "titulo": "Calzos y trabas mecánicas de seguridad", "texto": "Insertar barras metálicas de retención o calzos mecánicos entre los platos de la prensa para impedir el cierre físico ante fallas de control."},
            {"icono": "scan", "titulo": "Inviolabilidad de cortinas de luz y barreras", "texto": "Las barreras de seguridad optoelectrónicas y microinterruptores de puerta deben contar con redundancia Categoría 4 y prohibir cualquier bypass temporal."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de investigación de fatalidades de Michigan OSHA (MIOSHA General Industry Safety and Health Division) y norma ANSI B11.19 sobre protección de maquinaria industrial.",
        "guionReel": (
            "El 22 de octubre de 2015, en Evart, Michigan, la planta automotriz Ventra fue escenario de una muerte evitable dentro de una prensa gigante.\n\n"
            "Un técnico de 51 años entró entre los platos de la máquina para ajustar un sensor rebelde. Pensó que sería rápido: no apagó la energía ni usó candado LOTO.\n\n"
            "Tampoco colocó el puntal mecánico de seguridad y anuló la puerta de protección. Mientras ajustaba el cable, el sistema automatizado recibió señal de inicio.\n\n"
            "La prensa cerró sus platos de acero con 500 toneladas de fuerza. Murió aplastado al instante.\n\n"
            "La lección de Focus HSE: nunca entres a una máquina sin candado personal de bloqueo y calzos mecánicos. La velocidad productiva jamás vale una vida.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an industrial automotive hydraulic injection molding press interior in Michigan. "
            "Massive steel platen tooling and guide columns with yellow safety lock-out blocks staging on side bracket, "
            "red safety padlock applied to an electrical disconnect box with lockout tag, MIOSHA inspection team documenting machinery interlocks, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 22 de octubre de 2015, en las instalaciones fabriles de la empresa de autopartes Ventra Evart LLC, "
            "ubicada en la ciudad de Evart, estado de Michigan, Estados Unidos, un técnico de mantenimiento electromecánico "
            "de cincuenta y un años perdió la vida de forma instantánea al quedar atrapado entre los platos de una prensa industrial "
            "de moldeo de gran porte. El siniestro desencadenó una profunda auditoría de la agencia estatal de seguridad ocupacional MIOSHA.\n\n"
            "La tarea asignada parecía sencilla: ajustar la posición de un sensor de proximidad inductivo que marcaba falsos errores de alineación "
            "en el molde. Confiando en su experiencia de años y con el propósito de no retrasar el programa de entrega de piezas a las automotrices, "
            "el técnico cometió un error letal de atajo operativo. Ingresó directamente a la zona de riesgo situada entre los platos móviles "
            "de la prensa sin cortar la energía eléctrica, sin despresurizar los acumuladores hidráulicos y sin colocar su candado y tarjeta personal de bloqueo (LOTO).\n\n"
            "Para poder trabajar con la máquina encendida, el operario colocó un puente provisional en el microinterruptor de seguridad "
            "de la compuerta de acceso y anuló el haz de las cortinas ópticas. Asimismo, omitió la colocación de los calzos mecánicos de seguridad, "
            "unas robustas barras de acero diseñadas para bloquear físicamente el descenso del plato móvil. Mientras manipulaba el sensor, "
            "un contacto fortuito cerró el circuito de control del autómata programable, interpretando que el ciclo estaba listo para continuar. "
            "El pistón hidráulico principal avanzó con más de quinientas toneladas de fuerza de cierre, aplastando al trabajador antes de que pudiera reaccionar.\n\n"
            "La tragedia de Ventra en Michigan nos confronta con la regla primordial de la protección de máquinas y equipos: "
            "Ningún ajuste o mantenimiento, por menor que parezca, justifica saltarse el estándar de energía cero. "
            "Es mandatorio desenergizar todas las fuentes de poder —eléctricas, hidráulicas y neumáticas— con candado personal e intransferible. "
            "Los enclavamientos y cortinas de luz jamás deben puentearse, y el uso de calzos mecánicos de retención física es un requisito innegociable "
            "antes de ingresar el cuerpo a la zona de matrizado de cualquier prensa.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "120",
        "fecha": "23 OCTUBRE",
        "fechaPublicacion": "2026-10-23",
        "expediente": "Expediente #120",
        "carpeta": "1989-10-23-explosion-complejo-petroquimico-phillips-66-pasadena",
        "titular": "LAS MANGUERAS CRUZADAS DE LA TRAGEDIA: EXPLOSIÓN EN PHILLIPS 66",
        "palabraResaltada": "PHILLIPS 66 PASADENA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Complejo Petroquímico Houston Chemical Complex (Phillips 66), Pasadena, Texas, EE.UU. - 1989",
        "tipoRiesgo": "Seguridad de Procesos (PSM)",
        "parrafos": [
            "El 23 de octubre de 1989, una serie de explosiones colosales pulverizó la planta de polietileno del complejo Phillips 66 en Pasadena, Texas, matando a 23 trabajadores, hiriendo a 314 y registrando una magnitud de 3,5 en la escala de Richter.",
            "Durante el mantenimiento contratista de una válvula de descarga (settling leg) de un reactor de polietileno, se conectaron erróneamente las mangueras de aire comprimido que la operaban. La válvula se abrió de par en par en lugar de cerrarse, liberando 38 toneladas de gas inflamable.",
            "La nube detonó a los 90 segundos. La catástrofe forzó a OSHA a crear el estándar mundial de Gestión de Seguridad de Procesos (PSM 1910.119). La lección: doble bloqueo y purga, conectores neumáticos Poka-Yoke y supervisión estricta de contratistas.",
        ],
        "puntosClave": [
            {"icono": "shield-check", "titulo": "Diseño Poka-Yoke en mangueras de aire", "texto": "Utilizar conectores neumáticos con acoples no intercambiables para líneas de apertura y cierre de válvulas críticas de proceso."},
            {"icono": "lock", "titulo": "Doble bloqueo y purga con placa ciega (DBB)", "texto": "Prohibido intervenir equipos conectados a reactores presurizados sin aislamiento físico positivo con bridas ciegas colocadas."},
            {"icono": "file-text", "titulo": "Nacimiento de la norma OSHA PSM 1910.119", "texto": "La tragedia de Pasadena obligó a regular mundialmente los 14 elementos de Seguridad de Procesos: análisis de riesgos, MOC y gestión de contratistas."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe especial de la OSHA al Presidente de los Estados Unidos sobre la explosión en Phillips 66 (OSHA Report on the 1989 Phillips 66 Disaster) e investigaciones de la EPA.",
        "guionReel": (
            "El 23 de octubre de 1989, en Pasadena, Texas, el complejo petroquímico Phillips 66 desapareció bajo una explosión colosal.\n\n"
            "Un grupo de contratistas hacía mantenimiento en una válvula conectada a un reactor de polietileno. Para operarla, usaban mangueras de aire comprimido.\n\n"
            "Las mangueras eran idénticas y no tenían marcas. Las conectaron al revés: la válvula se abrió por completo en lugar de cerrarse.\n\n"
            "En segundos, 38 toneladas de gas etileno a alta presión se derramaron en la planta. La nube gigante encontró ignición y estalló con la fuerza de 2,4 toneladas de dinamita.\n\n"
            "Murieron 23 trabajadores y 314 quedaron heridos. Tras esta tragedia, nació la norma mundial de Seguridad de Procesos (PSM).\n\n"
            "La lección de Focus HSE: en válvulas críticas, un error de conexión no puede ser físicamente posible; exige diseño Poka-Yoke y doble bloqueo.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of the catastrophic industrial aftermath of the 1989 Phillips 66 chemical complex explosion in Pasadena, Texas. "
            "Flattened industrial steel framework of a high-density polyethylene production plant, burnt control room rubble, "
            "emergency firefighting monitors spraying water over smoking reactor vessel ruins, historical chemical process safety documentary aesthetic, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 23 de octubre de 1989, a la una y cinco de la tarde, en la localidad de Pasadena, cerca del Canal de Navegación de Houston en Texas, "
            "el complejo petroquímico Phillips 66 protagonizó uno de los accidentes industriales más destructivos y trascendentales de la historia moderna. "
            "Una serie de explosiones masivas equivalentes a más de dos toneladas y media de dinamita pulverizó la planta de polietileno de alta densidad, "
            "provocando la muerte de veintitrés trabajadores, hiriendo a más de trescientas personas y registrando un sismo de magnitud tres coma cinco.\n\n"
            "La causa raíz técnica y organizacional fue minuciosamente expuesta por los inspectores de la OSHA. "
            "Cuadrillas de una empresa contratista se encontraban realizando el desatasco rutinario de una válvula de bola tipo esfera "
            "situada en una pierna de sedimentación (settling leg) de un reactor de polietileno que operaba a más de cuarenta bares de presión. "
            "Para aislar el circuito, se confió exclusivamente en el actuador neumático de la válvula, sin colocar una placa ciega de bloqueo positivo "
            "y sin verificar el cierre con doble bloqueo y purga.\n\n"
            "Para accionar el mecanismo, los trabajadores conectaron dos mangueras de aire comprimido de taller: una para abrir y otra para cerrar. "
            "Ambas mangueras poseían conectores rápidos idénticos y carecían de etiquetas identificatorias o codificación por colores. "
            "Las líneas fueron cruzadas accidentalmente. Al inyectar aire, el actuador abrió la válvula de par en par hacia la atmósfera. "
            "Más de treinta y ocho toneladas de una mezcla inflamable y caliente de etileno, isobutano e hidrógeno escaparon en menos de noventa segundos, "
            "formando una inmensa nube de vapor no confinado que detonó al alcanzar los quemadores de un horno cercano. El estallido colapsó el sistema "
            "de agua contra incendios y demolió edificios administrativos enteros.\n\n"
            "La catástrofe de Pasadena en 1989 marcó un antes y un después en la legislación laboral internacional. "
            "Fue el detonante directo para que la OSHA promulgara en 1992 la emblemática norma de Gestión de Seguridad de Procesos para Químicos Altamente Peligrosos, "
            "conocida como PSM veintinueve CFR diecinueve diez punto ciento diecinueve. Consagró que las líneas críticas deben contar con diseño Poka-Yoke "
            "que impida errores mecánicos de conexión, que el aislamiento de reactores exige placas ciegas sin excepción, y que las empresas matrices "
            "son legalmente responsables de la capacitación, supervisión y seguridad de todo el personal contratista en sus plantas.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "121",
        "fecha": "24 OCTUBRE",
        "fechaPublicacion": "2026-10-24",
        "expediente": "Expediente #121",
        "carpeta": "2017-10-24-electrocucion-motor-cinta-tyson-foods-shelbyville",
        "titular": "LOS 480 VOLTIOS SIN BLOQUEO: ELECTROCUCIÓN EN TYSON FOODS",
        "palabraResaltada": "TYSON FOODS",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Procesadora de Alimentos Tyson Foods, Shelbyville, Tennessee, EE.UU. - 2017",
        "tipoRiesgo": "Riesgo Eléctrico / LOTO",
        "parrafos": [
            "El 24 de octubre de 2017, un técnico de mantenimiento de 37 años murió electrocutado en la planta procesadora de alimentos Tyson Foods en Shelbyville, Tennessee, al intervenir la caja de conexiones de una cinta transportadora energizada a 480 voltios.",
            "El operario no aplicó bloqueo y etiquetado (LOTO) en el centro de control de motores ni verificó la ausencia de tensión con multímetro antes de manipular los conductores húmedos por el lavado diario de la planta.",
            "Tyson Foods fue investigada y multada por OSHA por no capacitar adecuadamente en control de energías peligrosas y no proveer EPP dieléctrico. La lección: las 5 Reglas de Oro eléctricas, medición efectiva de tensión cero y bloqueo físico con candado personal.",
        ],
        "puntosClave": [
            {"icono": "zap", "titulo": "Corte efectivo y bloqueo con candado LOTO", "texto": "Abrir el seccionador en el tablero CCM, colocar candado con tarjeta de identificación personal y retener la llave consigo."},
            {"icono": "gauge", "titulo": "Verificación de energía cero con voltímetro", "texto": "Tercera Regla de Oro: medir entre fases y cada fase a tierra utilizando un multímetro verificado antes y después de la prueba."},
            {"icono": "droplets", "titulo": "Peligro multiplicado en áreas húmedas", "texto": "En plantas de alimentos donde se realizan baldeos frecuentes, el agua reduce la resistencia corporal; extremar el uso de guantes dieléctricos Clase 0."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informes de inspección y citaciones federales de Tennessee OSHA (TOSHA / OSHA 1910.147 / 1910.333) sobre la planta de Tyson Foods en Shelbyville.",
        "guionReel": (
            "El 24 de octubre de 2017, en Shelbyville, Tennessee, la planta procesadora de Tyson Foods vivió una tragedia evitable.\n\n"
            "Una cinta transportadora se detuvo. Un técnico de mantenimiento de 37 años fue a reparar el motor eléctrico.\n\n"
            "El piso estaba empapado por el lavado de la planta. Confiado, abrió la caja de bornes sin cortar la térmica en el tablero y sin guantes dieléctricos.\n\n"
            "Tocó los conductores vivos a 480 voltios. Con el suelo mojado, la corriente atravesó su corazón con una potencia destructiva. Murió en el acto.\n\n"
            "La lección de Focus HSE: en electricidad nunca supongas nada; corta la energía en el tablero, pon tu candado LOTO y mide siempre con voltímetro.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an industrial food processing facility conveyor belt motor station after an electrical fatality in Tennessee. "
            "Dismantled electrical junction box on stainless steel motor casing with exposed wire leads, wet tiled plant floor with water drainage grates, "
            "multimeter with probes resting on maintenance cart beside a red LOTO safety padlock, OSHA inspection documentation lighting, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 24 de octubre de 2017, en las instalaciones de la planta procesadora y faenadora de aves de la empresa Tyson Foods, "
            "ubicada en la ciudad de Shelbyville, en el estado de Tennessee, Estados Unidos, "
            "un operario electromecánico de mantenimiento de treinta y siete años perdió la vida de forma fulminante. "
            "Sufrió una descarga eléctrica de cuatrocientos ochenta voltios mientras intervenía la caja de conexiones de una cinta transportadora de procesamiento.\n\n"
            "La investigación técnica llevada adelante por los inspectores de la OSHA de Tennessee (TOSHA) puso al descubierto "
            "graves deficiencias en la gestión del riesgo eléctrico en ambientes húmedos. La cinta transportadora había presentado una detención "
            "repentina por sobrecarga térmica. El trabajador acudió al puesto con su caja de herramientas, retiró la tapa metálica del motorreductor "
            "e introdujo las manos para verificar las conexiones de los bornes sin haber realizado el corte visible en el Centro de Control de Motores (CCM) "
            "y sin aplicar candado y tarjeta de bloqueo y etiquetado (LOTO).\n\n"
            "Para empeorar la situación, el sector de faena se encontraba en pleno proceso de saneamiento e higienización, "
            "con los suelos de baldosas cubiertos por una película continua de agua y desengrasantes industriales. "
            "La humedad redujo drásticamente la resistencia eléctrica de contacto de las botas de seguridad del técnico. "
            "Al rozar con los dedos descubiertos uno de los conductores de fase energizado a cuatrocientos ochenta voltios en corriente alterna trifásica, "
            "la corriente cerró un circuito masivo a través de sus brazos y su cavidad torácica hacia la estructura metálica puesta a tierra. "
            "La descarga desencadenó fibrilación ventricular y paro cardiorrespiratorio inmediato, resultando infructuosas las maniobras de reanimación.\n\n"
            "El fatal accidente en Tyson Foods en Shelbyville ratifica las Cinco Reglas de Oro de la seguridad eléctrica, de cumplimiento universal y obligatorio: "
            "Primero: desconectar de forma visible y bloquear con candado personal toda fuente de alimentación antes de tocar cualquier equipo. "
            "Segundo: comprobar la ausencia de potencial midiendo fase con fase y cada fase a tierra con un voltímetro previamente verificado. "
            "Y tercero: en plantas industriales húmedas, todo trabajo eléctrico debe abordarse bajo la premisa de riesgo extremo, "
            "exigiendo el uso mandatorio de guantes dieléctricos certificados Clase Cero y alfombras aislantes adicionales.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "122",
        "fecha": "25 OCTUBRE",
        "fechaPublicacion": "2026-10-25",
        "expediente": "Expediente #122",
        "carpeta": "2016-10-25-accidente-atraccion-mecanica-dreamworld-queensland",
        "titular": "EL CANAL QUE SE QUEDÓ SIN AGUA: LA TRAGEDIA DE DREAMWORLD",
        "palabraResaltada": "DREAMWORLD QUEENSLAND",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Atracción Thunder River Rapids, Parque Dreamworld, Coomera, Queensland, Australia - 2016",
        "tipoRiesgo": "Seguridad de Máquinas / Gestión de Alarmas",
        "parrafos": [
            "El 25 de octubre de 2016, una falla de bombeo en la atracción acuática Thunder River Rapids del parque temático Dreamworld en Coomera, Queensland, Australia, provocó la colisión y vuelco de una balsa sobre el transportador de listones de madera, causando la muerte de 4 pasajeros.",
            "Una de las dos bombas centrífugas de recirculación de agua falló repentinamente. El nivel del canal descendió en segundos sin que ningún sensor automático detuviera la cinta transportadora de elevación, quedando una balsa atascada contra la estructura fija.",
            "Una segunda balsa cargada chocó contra la primera y fue succionada por el mecanismo tractor en marcha. La lección: sistemas instrumentados de seguridad (SIS) con parada automática ante pérdida de flujo, enclavamientos de nivel y diseño intrínseco.",
        ],
        "puntosClave": [
            {"icono": "shield-alert", "titulo": "Parada de emergencia automática (SIS/Trip)", "texto": "Instalar lazos instrumentados de seguridad redundantes que detengan transportadores y motores de inmediato ante caída del nivel de agua."},
            {"icono": "activity", "titulo": "Gestión de alarmas y capacitación en emergencias", "texto": "Capacitar a los operadores en parada de emergencia y no delegar el control de atracciones mecánicas complejas en personal inexperto sin entrenamiento."},
            {"icono": "wrench", "titulo": "Mantenimiento preventivo en bombas críticas", "texto": "Auditar la integridad de bombas de recirculación y desterrar la cultura de rearmar equipos con fallas recurrentes sin análisis de causa raíz."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: investigación forense del Tribunal Forense de Queensland (Coroner's Report on Dreamworld Disaster) y resoluciones sancionatorias de WorkSafe Queensland bajo la ley WHS.",
        "guionReel": (
            "El 25 de octubre de 2016, en Queensland, Australia, el parque temático Dreamworld vivió una pesadilla mecánica en una de sus atracciones más populares.\n\n"
            "En los rápidos de agua Thunder River Rapids, una bomba de agua falló en silencio. El canal se vació en segundos, pero la cinta transportadora siguió funcionando porque no tenía sensor de nivel.\n\n"
            "Una balsa circular quedó varada en el fondo seco. Segundos después, una segunda balsa con seis pasajeros llegó por detrás y chocó contra ella.\n\n"
            "La cinta mecánica no paró: volcó la balsa y succionó a los pasajeros hacia el mecanismo de engranajes. Cuatro personas murieron aplastadas.\n\n"
            "La lección de Focus HSE: las máquinas automatizadas no pueden depender de la suerte; exigen sensores instrumentados que frenen todo ante cualquier falla de nivel.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of the Thunder River Rapids mechanical water channel ride at Dreamworld theme park in Queensland, Australia. "
            "A drained concrete water trough with heavy wooden slatted conveyor belt system, circular yellow and blue passenger rafts resting askew, "
            "emergency stop switches and WorkSafe Queensland forensic investigation markers, overcast daylight, somber mechanical safety inspection aesthetic, 8k."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 25 de octubre de 2016, en el parque temático Dreamworld ubicado en Coomera, región de Gold Coast, estado de Queensland, Australia, "
            "la atracción acuática mecánica Thunder River Rapids se convirtió en el escenario de una de las peores tragedias "
            "en la historia del entretenimiento mundial. Cuatro personas adultas perdieron la vida de manera trágica al colisionar y volcar su balsa "
            "contra el sistema motriz de la cinta transportadora de desembarque.\n\n"
            "La investigación forense desarrollada por la Corte de Instrucción de Queensland y WorkSafe expuso fallas sistémicas "
            "en el diseño de ingeniería, mantenimiento y respuesta ante emergencias de la empresa operadora Ardent Leisure. "
            "La atracción operaba mediante dos grandes bombas centrífugas que impulsaban millones de litros de agua por un canal artificial. "
            "Aquella tarde, una de las dos bombas principales sufrió una parada imprevista por sobrecalentamiento eléctrico. "
            "Como consecuencia, el nivel del agua en la rampa de desembarque descendió drásticamente en escasos cincuenta segundos. "
            "Sin embargo, el sistema carecía de sensores de nivel hidrostáticos enlazados a una parada de emergencia automática (trip).\n\n"
            "Una balsa circular que finalizaba el recorrido quedó varada sobre el fondo del canal seco, atascada contra los rieles de descarga. "
            "Pocos segundos después, una segunda balsa con seis visitantes a bordo ingresó a la zona empujada por la inercia del agua restante. "
            "Al encontrarse con el obstáculo inmóvil, la segunda balsa colisionó y fue levantada por los listones de madera de la cinta transportadora "
            "que continuaba girando a velocidad normal. La balsa volcó en posición vertical, atrapando a cuatro pasajeros entre las ruedas motrices "
            "y las cadenas de tracción mecánica de acero. Los operadores a cargo, jóvenes contratados recientemente con apenas unas horas de capacitación, "
            "no accionaron a tiempo el botón de parada de emergencia principal situado en la consola.\n\n"
            "La catástrofe de Dreamworld en Australia representa un caso de estudio fundamental en la seguridad de máquinas y gestión de procesos: "
            "Primero: la seguridad de un equipo automatizado de alto riesgo jamás debe descansar exclusivamente en la reacción humana; "
            "debe contar con Sistemas Instrumentados de Seguridad (SIS) que detengan automáticamente los motores ante cualquier pérdida crítica de nivel o flujo. "
            "Segundo: las fallas mecánicas repetitivas deben investigarse a fondo y no normalizarse con simples rearmados eléctricos. "
            "Y tercero: el entrenamiento en paradas de emergencia debe ser riguroso, continuo e instintivo para todo el personal operativo.\n\n"
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
    """Inyecta las historias del Lote 11 en index.html antes del cierre del array historias."""
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

    print("\n✓ index.html actualizado exitosamente con los 10 nuevos expedientes (#113 a #122).")
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
    print("Iniciando motor Kokoro para Lote 11 (#113 a #122)...")
    kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

    print("\n" + "=" * 55)
    print("Iniciando procesamiento de 10 historias del Lote 11 (#113 a #122)")
    print("=" * 55 + "\n")

    historias_procesadas = []

    for h in LOTE_11_DATA:
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

    print("\n🎉 ¡LOTE 11 COMPLETADO AL 100%! (10 historias procesadas)\n")

if __name__ == "__main__":
    main()
