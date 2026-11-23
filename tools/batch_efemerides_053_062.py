# -*- coding: utf-8 -*-
"""
Generador Agéntico Automatizado para Lote 5: Expedientes #053 a #062 (17 al 26 de agosto)
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

LOTE_5_DATA = [
    {
        "id": "053",
        "fecha": "17 AGOSTO",
        "fechaPublicacion": "2026-08-17",
        "expediente": "Expediente #053",
        "carpeta": "2009-08-17-accidente-hidroelectrica-sayano-shushenskaya",
        "titular": "LA ROTURA DE LA TURBINA DOS: EL DESASTRE DE SAYANO-SHÚSHENSKAYA",
        "palabraResaltada": "SAYANO-SHÚSHENSKAYA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Central Hidroeléctrica Sayano-Shúshenskaya, Jakasia, Rusia - 2009",
        "tipoRiesgo": "Seguridad de Procesos / Integridad Mecánica y Vibraciones",
        "parrafos": [
            "El 17 de agosto de 2009, la Central Hidroeléctrica de Sayano-Shúshenskaya sufrió una catástrofe sin precedentes cuando la turbina número dos fue eyectada de su fosa, cobrando la vida de 75 trabajadores.",
            "La unidad operaba de manera prolongada en una zona prohibida de severas vibraciones hidrodinámicas. Los ochenta pernos de sujeción de la tapa sufrieron fatiga cíclica de material hasta fracturarse en masa.",
            "Una columna colosal de agua a alta presión inundó la sala de máquinas destruyendo nueve generadores. La tragedia demostró el peligro mortal de ignorar las alertas de vibración en grandes máquinas rotativas."
        ],
        "puntosClave": [
            {"icono": "activity", "titulo": "Mantenimiento predictivo por vibraciones", "texto": "Monitorear continuamente el espectro vibratorio y detener inmediatamente turbinas que superen los umbrales de seguridad admisibles."},
            {"icono": "alert-octagon", "titulo": "Respetar las bandas de potencia prohibidas", "texto": "Prohibido operar de forma sostenida en regímenes de carga donde se generan vórtices y resonancias mecánicas destructivas."},
            {"icono": "shield-check", "titulo": "Integridad de pernos y cierre de compuertas", "texto": "Ensayos no destructivos periódicos en uniones roscadas críticas y sistemas de compuertas de caída por gravedad independientes de la energía de planta."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe técnico de la Comisión de Investigación de Rostekhnadzor sobre el accidente de la central Sayano-Shúshenskaya y normas de integridad hidroeléctrica de la IEEE.",
        "guionReel": (
            "¿Sabías que una turbina hidráulica de mil toneladas puede salir disparada por el aire como el corcho de una botella?\n\n"
            "El 17 de agosto de 2009, en la gigantesca central rusa de Sayano-Shúshenskaya, la turbina número dos vibraba con tanta violencia que sacudía el piso de hormigón.\n\n"
            "Los directivos sabían que la máquina operaba en una zona prohibida de potencia, pero necesitaban entregar energía a la red y desoyeron las alarmas.\n\n"
            "Los 80 pernos de acero que sujetaban la tapa sufrieron fatiga extrema. A las ocho de la mañana, se partieron todos juntos.\n\n"
            "El agua a presión del embalse eyectó la turbina entera hacia el techo. Un torrente descomunal inundó la sala de máquinas matando a 75 trabajadores.\n\n"
            "En maquinaria rotativa, las vibraciones no son ruido de fondo: son el aviso final antes del colapso estructural.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Massive industrial disaster documentary photography, August 17 2009 Sayano-Shushenskaya hydroelectric power plant turbine hall disaster. "
            "Catastrophically flooded turbine machine hall, massive twisted metal turbine rotor displaced, shattered concrete, crushed overhead industrial gantry crane, "
            "roaring water foaming through ruins, emergency response rescue teams in orange reflective vests with flashlights, wide angle 16:9, hyperrealistic."
        ),
        "guionLargo": (
            "El diecisiete de agosto de dos mil nueve... a orillas del caudaloso río Yeniséi en la República de Jakasia, en Rusia... se produjo el accidente más devastador en la historia de la energía hidroeléctrica mundial... "
            "La colosal presa de Sayano-Shúshenskaya... una maravilla de la ingeniería soviética con más de doscientos cuarenta metros de altura... albergaba diez turbinas gigantescas capaces de suministrar miles de megavatios a la red industrial siberiana... "
            "Durante meses... la turbina número dos... una máquina rotativa de más de mil quinientas toneladas... venía operando de manera recurrente dentro de una zona de potencia restringida... conocida como banda de carga prohibida... "
            "En ese régimen operativo particular... el flujo del agua generaba intensos vórtices hidrodinámicos y cavitación severa... desatando vibraciones mecánicas que superaban con holgura los límites de alarma establecidos por los fabricantes... "
            "Sin embargo... para cumplir con las exigencias comerciales de regulación de frecuencia del sistema eléctrico... la administración de la planta continuó operando la unidad... posponiendo las paradas de mantenimiento... "
            "Las vibraciones periódicas sometieron a los ochenta pernos de acero que anclaban la pesada tapa de la turbina al pozo de hormigón a un proceso continuo de fatiga de bajo número de ciclos... "
            "Aquel fatídico amanecer... seis de los pernos ya estaban completamente fracturados y la mayoría presentaba grietas microscópicas terminales... "
            "A las ocho horas con trece minutos... la resistencia estructural del acero llegó a su punto de rotura... "
            "En una fracción de segundo... los pernos restantes se decapitaron en simultáneo... "
            "La descomunal presión hidrostática del embalse... equivalente a más de doscientas atmósferas de empuje ascendente... expulsó la tapa y el gigantesco rotor de la turbina por los aires... destrozando el cielorraso de la sala de máquinas... "
            "Un géiser colosal de agua fría... a un caudal de más de trescientos metros cúbicos por segundo... irrumpió con furia arrasadora en la nave principal... "
            "La corriente destruyó tableros de control... cortó las fuentes de suministro eléctrico y ahogó de manera instantánea a decenas de operarios y técnicos de mantenimiento... cobrándose la vida de setenta y cinco trabajadores... "
            "El desastre demostró que los sistemas de mantenimiento predictivo no pueden subordinarse a metas de despacho eléctrico... "
            "Frente a vibraciones anómalas en turbomáquinas... el respeto a los parámetros de diseño es sagrado... y la parada de emergencia debe ser automática e ineludible."
        )
    },
    {
        "id": "054",
        "fecha": "18 AGOSTO",
        "fechaPublicacion": "2026-08-18",
        "expediente": "Expediente #054",
        "carpeta": "2017-08-18-atropello-retroceso-camion-volcador-obra",
        "titular": "PUNTO CIEGO Y RETROCESO: EL ATROPELLO EN LA OBRA VIAL",
        "palabraResaltada": "PUNTO CIEGO Y RETROCESO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Frente de Pavimentación y Obra Vial en Construcción - 2017",
        "tipoRiesgo": "Seguridad Vial Interna / Movimiento de Equipos Pesados",
        "parrafos": [
            "El 18 de agosto de 2017, un topógrafo de 32 años murió aplastado por el retroceso de un camión volcador de cuatro ejes mientras realizaba mediciones en una traza vial en construcción.",
            "El chofer maniobró en reversa guiándose solo por los espejos laterales, desconociendo el enorme cono ciego que abarca la parte posterior. La alarma sonora de retroceso del camión había sido desconectada.",
            "La obra carecía de señalero o vigía asignado y no había segregación física entre el tránsito de maquinaria y el personal a pie. Maniobras en reversa sin vigía son una de las principales causas de muerte en obra civil."
        ],
        "puntosClave": [
            {"icono": "user-check", "titulo": "Señalero o vigía dedicado obligatorio", "texto": "Ningún camión o máquina pesada puede retroceder en frentes de obra activos sin un banderillero ubicado en posición visible."},
            {"icono": "volume-2", "titulo": "Alarmas de retroceso y cámaras traseras", "texto": "Prohibido operar equipos con la bocina de reversa anulada; complementar con sensores de proximidad ultrasónicos y cámaras de cabina."},
            {"icono": "shield", "titulo": "Segregación física peatón-vehículo", "texto": "Delimitar sendas de circulación exclusivas con barandas o new jerseys para que el personal de a pie nunca comparta calzada con camiones."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: estudios de zonas de peligro y puntos ciegos en obras de construcción de OSHA 1926.601 y guías técnicas de NIOSH (Highway Work Zone Safety).",
        "guionReel": (
            "¿Sabías que detrás de un camión volcador hay una zona ciega del tamaño de un colectivo donde el chofer no puede verte?\n\n"
            "El 18 de agosto de 2017, en una obra de pavimentación, un topógrafo verificaba niveles con su trípode en medio de la calzada.\n\n"
            "Un camión cargado con treinta toneladas de asfalto puso marcha atrás para posicionarse en la terminadora. Para no molestar a los vecinos, el chofer le había desconectado los cables a la alarma sonora de retroceso.\n\n"
            "El trabajador estaba concentrado mirando por el visor, de espaldas al camión. El chofer miró por los espejos laterales, pero en el medio había un punto ciego absoluto.\n\n"
            "El camión lo arrolló sin que nadie pudiera advertirlo.\n\n"
            "La regla en obra pesada es innegociable: jamás se retrocede sin un señalero visible guiando la maniobra y con la alarma sonando.\n\n"
            "En la línea de fuego, un segundo de distracción no perdona."
        ),
        "promptImagen": (
            "Civil construction highway roadwork documentary photography, heavy yellow dump truck stopped in reverse position on fresh asphalt paving site. "
            "Surveying tripod and high-precision laser level instrument crushed on the ground, high-visibility orange safety vest, safety cones perimeter, "
            "road rollers and asphalt paving machines working in background, bright afternoon sunlight with long dramatic shadows, realistic photojournalism, 16:9."
        ),
        "guionLargo": (
            "El dieciocho de agosto de dos mil diecisiete... en un extenso tramo de ensanche y pavimentación de una autopista interurbana... un incidente vial laboral terminó con la vida de un joven profesional de la construcción... "
            "En el frente de avance de obra... convivían en un espacio sumamente estrecho cuadrillas de operarios a pie, equipos topográficos, rodillos compactadores y una incesante fila de camiones volcadores de gran porte... "
            "Un técnico topógrafo se encontraba abocado a la verificación de cotas y pendientes... posicionado de pie detrás de su trípode de nivelación... concentrado en la calibración óptica del instrumental... "
            "A unos treinta metros de distancia... un camión volcador de cuatro ejes y treinta toneladas de tara inició una maniobra de retroceso para descargar material bituminoso caliente frente a la máquina pavimentadora... "
            "El conductor acomodó los retrovisores laterales... pero en los camiones de gran porte... la geometría de la caja de carga genera un cono de sombra visual posterior que abarca más de diez metros en línea recta... un punto ciego absoluto donde la visibilidad es nula... "
            "Para agravar la situación... la chicharra acústica de marcha atrás había sido desconectada deliberadamente mediante un interruptor casero en la cabina... debido a quejas reiteradas por ruidos molestos en el vecindario... "
            "Tampoco se había designado un señalero o vigía de maniobras que guiara el desplazamiento con chaleco reflectivo y silbato reglamentario... "
            "El topógrafo... situado de espaldas al camión y con los protectores auditivos de copa colocados debido al estruendo de los motores diésel cercanos... no percibió la aproximación de la mole de acero... "
            "El vehículo lo impactó por detrás... causándole la muerte instantánea por aplastamiento... "
            "Las investigaciones de seguridad vial laboral subrayaron una deficiencia organizativa fundamental... la ausencia de segregación física entre hombres y máquinas... "
            "En todo frente de trabajo con maquinaria rodante... la zona de tránsito peatonal debe estar acordonada e independizada del radio de giro y maniobra de los camiones... "
            "Y el protocolo de retroceso es estricto... sin alarma sonora activa y sin la presencia física y visual de un señalero... ningún equipo pesado puede dar un solo metro hacia atrás."
        )
    },
    {
        "id": "055",
        "fecha": "19 AGOSTO",
        "fechaPublicacion": "2026-08-19",
        "expediente": "Expediente #055",
        "carpeta": "1996-08-19-incompatibilidad-quimica-residuos-industriales",
        "titular": "ÁCIDOS Y ÁLCALIS EN EL MISMO TANQUE: LA REACCIÓN IMPREVISTA",
        "palabraResaltada": "ÁCIDOS Y ÁLCALIS",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta de Tratamiento y Reciclaje de Residuos Industriales - 1996",
        "tipoRiesgo": "Riesgo Químico / Incompatibilidad y Control de Recepción",
        "parrafos": [
            "El 19 de agosto de 1996, una violenta reacción química en una planta de tratamiento de residuos industriales en Hampshire, Inglaterra, provocó una masiva nube tóxica que obligó a evacuar a miles de personas.",
            "Un camión cisterna que transportaba una solución ácida de desecho fue descargado por error en un tanque de almacenamiento que contenía lodos alcalinos con sulfuros. No se realizó el ensayo analítico previo de compatibilidad en laboratorio.",
            "La neutralización exotérmica descontrolada elevó la temperatura a 120 °C desprendiendo una densa pluma de ácido sulfhídrico ($H_2S$) y dióxido de azufre ($SO_2$). Una lección vital sobre control estricto en recepción de residuos.",
        ],
        "puntosClave": [
            {"icono": "test-tube-2", "titulo": "Prueba de compatibilidad previa (Jar test)", "texto": "Realizar obligatoriamente un ensayo a pequeña escala en vaso de laboratorio mezclando muestras reales antes de autorizar la descarga."},
            {"icono": "git-merge", "titulo": "Acoples diferenciados por familia química", "texto": "Implementar conexiones físicas incompatibles entre líneas de ácidos y bases para imposibilitar el error humano mecánico."},
            {"icono": "tag", "titulo": "Trazabilidad documental y etiquetado inequívoco", "texto": "Verificar la carta de porte, número UN y ficha de datos de seguridad antes de permitir el ingreso del camión al área de descarga."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de investigación del Health and Safety Executive (HSE UK) sobre incidentes de incompatibilidad química en plantas de transferencia y tratamiento de residuos.",
        "guionReel": (
            "¿Qué sucede si juntas por error un camión de ácido con un tanque de residuos alcalinos?\n\n"
            "El 19 de agosto de 1996, en una planta de tratamiento en Inglaterra, llegó un camión cisterna cargado con miles de litros de efluentes químicos.\n\n"
            "El operador de recepción estaba apurado. Asumió lo que decía la etiqueta del remito y no subió al laboratorio a hacer la prueba básica de compatibilidad en un vasito.\n\n"
            "Conectó la manguera y comenzó a descargar ácido clorhídrico dentro de un tanque que contenía residuos alcalinos con sulfuros.\n\n"
            "La química no perdona: la reacción exotérmica hirvió el tanque en segundos y liberó una nube monstruosa de ácido sulfhídrico que cubrió varios pueblos.\n\n"
            "En residuos industriales, jamás descargues nada sin la prueba previa de compatibilidad y acoples mecánicos codificados.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Industrial chemical waste treatment plant documentary photography, chemical tanker truck connected by heavy hose to large industrial bulk storage tank. "
            "Ruptured pressure relief vent expelling thick dense yellowish-white chemical vapor cloud into the sky, warning corrosive hazard placards on tank, "
            "emergency siren beacon flashing, chemical operators in hazmat suits retreating, atmospheric dramatic lighting, 16:9 ratio."
        ),
        "guionLargo": (
            "El diecinueve de agosto de mil novecientos noventa y seis... en una planta autorizada para la gestión, neutralización y tratamiento de residuos industriales en el condado de Hampshire, en el Reino Unido... una secuencia de omisiones desató una emergencia química masiva... "
            "A primera hora de la mañana, un camión cisterna arribó a la playa de maniobras transportando veinticinco mil litros de desechos líquidos procedentes de una fábrica de galvanoplastia... "
            "La remisión de transporte identificaba la carga de manera genérica... como solución acuosa de lavado inorgánico... "
            "El procedimiento operativo de la compañía establecía de forma taxativa que... antes de autorizar la conexión de cualquier manguera de trasvase... el personal de recepción debía tomar una muestra representativa del compartimiento y llevarla al laboratorio de control de calidad... "
            "Allí se debía efectuar el ensayo de compatibilidad... una prueba rápida en vaso de precipitado consistente en mezclar una pequeña alícuota del residuo entrante con el contenido del tanque receptor para observar cambios de temperatura, efervescencia o formación de gases... "
            "Sin embargo... ante la congestión de camiones en el playón de descarga... el supervisor decidió omitir la verificación analítica... "
            "Instruyó al conductor para acoplar la manguera flexible directamente a la brida de alimentación del tanque de almacenamiento número siete... "
            "Aquel tanque contenía miles de litros de lodos fuertemente alcalinos mezclados con sales de sulfuro y cianuros disueltos... mientras que la cisterna ingresante contenía una concentración masiva de ácido sulfúrico residual... "
            "Apenas comenzó el bombeo... el violento choque químico entre el ácido concentrado y la matriz alcalina desencadenó una neutralización exotérmica incontrolable... "
            "La temperatura interior trepó en cuestión de segundos por encima de los ciento veinte grados centígrados... haciendo entrar en ebullición la mezcla... "
            "La brusca caída de acidez provocó la descomposición inmediata de los sulfuros... liberando miles de metros cúbicos de ácido sulfhídrico y dióxido de azufre a través de las válvulas de alivio y escotillas... "
            "Una densa y asfixiante nube tóxica de olor nauseabundo se elevó sobre el complejo... desplazándose hacia las zonas urbanas linderas y obligando a las autoridades a evacuar a más de tres mil personas y decretar el confinamiento domiciliario de dos localidades... "
            "El informe oficial del organismo de seguridad británico concluyó que confiar en declaraciones documentales sin confirmación analítica es una imprudencia extrema... "
            "Las plantas de residuos deben contar con terminales de carga con acoples codificados geométricamente por tipo de químico... y una regla innegociable... sin ensayo físico de compatibilidad... ninguna válvula puede abrirse jamás."
        )
    },
    {
        "id": "056",
        "fecha": "20 AGOSTO",
        "fechaPublicacion": "2026-08-20",
        "expediente": "Expediente #056",
        "carpeta": "2015-08-20-caida-fosa-mantenimiento-taller-mecanico",
        "titular": "EL HUECO EN LA PENUMBRA: LA CAÍDA EN LA FOSA DEL TALLER",
        "palabraResaltada": "HUECO EN LA PENUMBRA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Taller de Mantenimiento de Flota de Transporte Pesado - 2015",
        "tipoRiesgo": "Caídas a Distinto Nivel / Orden, Limpieza e Iluminación",
        "parrafos": [
            "El 20 de agosto de 2015, un mecánico de 45 años sufrió fracturas múltiples y contusiones graves al caer dentro de una fosa de inspección vehicular de dos metros de profundidad en un taller de transporte.",
            "La fosa había quedado desocupada tras retirar un colectivo, pero los operarios del turno anterior no colocaron las rejillas cobertoras ni instalaron las cadenas perimetrales de advertencia.",
            "El sector carecía de iluminación adecuada durante el relevo de guardia y el piso presentaba manchas de grasa. El accidente recordó que toda fosa abierta es una caída en altura encubierta en el suelo."
        ],
        "puntosClave": [
            {"icono": "grid", "titulo": "Cobertura o barandilla en fosas desocupadas", "texto": "Toda fosa sin vehículo sobre ella debe cerrarse de inmediato con tapas rígidas transitables o cercarse con postes y cadenas."},
            {"icono": "sun", "titulo": "Nivel de iluminación reglamentario", "texto": "Garantizar un mínimo de 200 a 300 lux en pasillos de tránsito de talleres para eliminar sombras y zonas ciegas de penumbra."},
            {"icono": "check-circle-2", "titulo": "Señalización y demarcación perimetral", "texto": "Pintar los bordes con franjas diagonales amarillo y negro reflectivas y zócalos de advertencia en todo el contorno."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: normativas de prevención de caídas en talleres de mantenimiento de OSHA 1910.28 y directrices del Instituto Nacional de Seguridad y Salud en el Trabajo (INSST España).",
        "guionReel": (
            "¿Pensabas que para sufrir una caída de altura grave hay que subir a un techo o a un andamio?\n\n"
            "El 20 de agosto de 2015, en un taller de colectivos, un mecánico terminó en terapia intensiva caminando por el suelo plano.\n\n"
            "Habían sacado un colectivo de la fosa de lubricación de dos metros de profundidad. Los del turno tarde terminaron y se fueron sin poner las tablas de cobertura ni las cadenas de protección.\n\n"
            "El taller tenía luces quemadas y había sombras en ese rincón. Durante el cambio de turno, el mecánico entró caminando con una caja de herramientas, pisó en falso en el borde engrasado y cayó en seco al fondo de hormigón.\n\n"
            "Fractura de cadera, muñeca y traumatismo de cráneo.\n\n"
            "Una fosa abierta sin vehículo es una trampa mortal en el piso. O la tapas de inmediato, o le colocas barandas perimetrales.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Industrial mechanical workshop accident scene documentary photography, deep concrete vehicle inspection pit sunken into garage floor. "
            "Pit completely open without safety covers or guardrails, scattered tools and dropped metal toolbox at bottom of pit, yellow and black chevron painted edges chipped, "
            "heavy fleet buses parked in background, dim industrial ceiling lighting creating harsh contrasting shadows, realistic photojournalism, 16:9 ratio."
        ),
        "guionLargo": (
            "El veinte de agosto de dos mil quince... en las instalaciones centrales de mantenimiento de una empresa de transporte público de pasajeros... la falta de orden y protección colectiva ocasionó un siniestro de graves consecuencias... "
            "El taller disponía de cuatro fosas longitudinales de inspección y lubricación excavadas en el piso de hormigón... con una profundidad de un metro con noventa centímetros y casi veinte metros de largo... "
            "Al finalizar la jornada diurna... una cuadrilla completó el cambio de aceite y engrase de diferenciales de una unidad de transporte... retirando el ómnibus hacia la playa exterior de estacionamiento... "
            "Concluidas las tareas... los operarios omitieron desplegar el sistema de cubiertas de madera articuladas... diseñadas específicamente para sellar el vano de la fosa cuando no hay un rodado posicionado encima... "
            "Tampoco colocaron los postes móviles con cadenas de advertencia en los laterales... dejando una hendidura abierta y profunda en medio de la nave de trabajo... "
            "Minutos antes del inicio del turno nocturno... el nivel de iluminación general en esa bahía era deficiente... debido a dos luminarias de vapor de sodio que se encontraban fuera de servicio desde hacía semanas... "
            "Un mecánico del turno entrante... transportando en sus brazos un compresor portátil y una caja metálica de herramientas... cruzaba el taller en dirección a su puesto de labor... "
            "La carga voluminosa le restaba visibilidad frontal hacia el suelo... y la penumbra del entorno camuflaba la silueta del pozo... "
            "Al pisar sobre el borde de la fosa... que se encontraba impregnado con restos de grasa y líquido de frenos... su calzado perdió adherencia... "
            "El trabajador trastabilló y cayó al vacío sin posibilidad de sujetarse... impactando de lleno contra el piso de cemento y los rieles metálicos inferiores... "
            "Sufrió fractura de fémur, fisura de costillas y un traumatismo encéfalo-craneano con pérdida de conocimiento... "
            "Las estadísticas de accidentalidad laboral demuestran que las caídas en fosas de taller representan una de las principales fuentes de incapacidad permanente en la industria del transporte... "
            "La regla técnica es terminante... Toda abertura en el suelo que supere el medio metro de profundidad debe considerarse riesgo de caída en altura... "
            "Apenas un vehículo abandona la fosa... la prioridad inmediata y absoluta antes de iniciar cualquier otra labor... es colocar las tapas o tender las barandas perimetrales rígidas... "
            "Porque un hueco desprotegido en la oscuridad... no da tiempo de reacción."
        )
    },
    {
        "id": "057",
        "fecha": "21 AGOSTO",
        "fechaPublicacion": "2026-08-21",
        "expediente": "Expediente #057",
        "carpeta": "1986-08-21-desastre-lago-nyos-asfixia-co2",
        "titular": "EL ALIENTO DE LA MONTAÑA: LA ASFIXIA MASIVA DEL LAGO NYOS",
        "palabraResaltada": "ASFIXIA MASIVA DEL LAGO NYOS",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Lago Volcánico Nyos, Noroeste de Camerún - 1986",
        "tipoRiesgo": "Riesgo Ambiental e Industrial / Asfixia por Gases Pesados (CO₂)",
        "parrafos": [
            "La noche del 21 de agosto de 1986, una erupción límnica en el lago Nyos, Camerún, liberó repentinamente 1,6 millones de toneladas de dióxido de carbono ($CO_2$), asfixiando a 1.746 personas y miles de animales.",
            "El gas, disuelto a gran profundidad bajo alta presión hidrostática, se saturó hasta romper el equilibrio. Siendo una vez y media más pesado que el aire, el $CO_2$ bajó por las laderas como un río invisible desplazando el oxígeno.",
            "Poblaciones enteras a 25 kilómetros murieron mientras dormían sin advertir el peligro. El desastre es la mayor lección sobre el comportamiento de gases densos que se acumulan en hondonadas, sótanos y zanjas.",
        ],
        "puntosClave": [
            {"icono": "cloud", "titulo": "Comportamiento de gases densos", "texto": "Gases como el CO₂, propano o H₂S pesan más que el aire y se desplazan como líquidos hacia depresiones, zanjas y sótanos."},
            {"icono": "wind", "titulo": "Asfixia mecánica por desplazamiento de O₂", "texto": "El CO₂ no tiene olor ni color a bajas concentraciones y mata no por toxicidad directa inicial, sino al expulsar el oxígeno atmosférico."},
            {"icono": "gauge", "titulo": "Medición atmosférica a nivel de piso", "texto": "En plantas industriales y excavaciones, la sonda del detector de gases debe colocarse a ras de suelo para detectar estratificaciones pesadas."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: investigaciones científicas vulcanológicas del USGS y lecciones de seguridad industrial sobre dispersión de gases pesados del Center for Chemical Process Safety (CCPS).",
        "guionReel": (
            "¿Sabías que un gas completamente invisible e inodoro puede borrar del mapa a miles de personas en una sola noche?\n\n"
            "La noche del 21 de agosto de 1986, en el lago Nyos en Camerún, ocurrió un fenómeno geológico aterrador llamado erupción límnica.\n\n"
            "En el fondo del lago había acumuladas más de un millón de toneladas de dióxido de carbono a altísima presión.\n\n"
            "Un derrumbe de tierra desestabilizó el agua y el gas se liberó de golpe, igual que cuando abres una gaseosa batida.\n\n"
            "El dióxido de carbono pesa un 50% más que el aire. En lugar de subir al cielo, formó una nube invisible que bajó por los valles como un río silencioso, expulsando todo el oxígeno.\n\n"
            "Mil setecientas cuarenta y seis personas murieron asfixiadas en sus camas sin escuchar una sola explosión.\n\n"
            "En la industria química pasa lo mismo: el CO₂, el propano y el sulfhídrico se acumulan en pozos y zanjas. Mide siempre los gases a ras del suelo.\n\n"
            "La física no se ve, pero se siente."
        ),
        "promptImagen": (
            "Haunting historical documentary aerial photography, August 21 1986 Lake Nyos disaster Cameroon. "
            "High crater volcanic lake with tranquil reddish-brown stained waters, deep green tropical valleys descending from the caldera rim shrouded in low eerie creeping ground mist, "
            "silent abandoned village settlements visible in valley basin, dramatic somber sunrise lighting, photorealistic archival style, 16:9 ratio."
        ),
        "guionLargo": (
            "La noche del veintiuno de agosto de mil novecientos ochenta y seis... en las tierras altas del noroeste de Camerún... se desató uno de los fenómenos naturales más escalofriantes e insólitos jamás documentados por la ciencia... "
            "El lago Nyos... un ojo de agua cristalina ubicado en el cráter de un antiguo volcán extinto... albergaba en sus profundidades de más de doscientos metros una trampa letal en constante gestación... "
            "Durante siglos... emanaciones de magma subterráneo inyectaban de manera continua dióxido de carbono en las capas más frías y profundas del fondo del lago... "
            "Bajo la gigantesca presión hidrostática de la columna de agua... el gas permanecía completamente disuelto... en una concentración de saturación crítica... "
            "Aquella noche... un pequeño deslizamiento de rocas o un cambio térmico rompió el delicado equilibrio de estratificación acuática... "
            "El fenómeno fue idéntico al destape violento de una botella de bebida carbonatada... Más de un millón seiscientas mil toneladas de dióxido de carbono puro se desprendieron en masa hacia la superficie... "
            "En la física de los gases... el dióxido de carbono posee una densidad cincuenta por ciento superior a la del aire ambiente que respiramos... "
            "Al emerger a la atmósfera... la colosal nube invisible y gélida no ascendió al firmamento... sino que se derramó por los bordes del cráter... comportándose como un fluido pesado que descendió a gran velocidad encauzado por los valles y quebradas... "
            "A medida que avanzaba a ras del suelo... la masa de gas desplazó por completo el aire respirable... reduciendo la concentración de oxígeno a niveles incompatibles con la vida... "
            "Poblados enteros situados a más de veinticinco kilómetros de distancia quedaron sumergidos en la corriente silenciosa... "
            "Mil setecientas cuarenta y seis personas... y más de tres mil cabezas de ganado... perecieron por asfixia mecánica en cuestión de minutos... la inmensa mayoría mientras dormía plácidamente en sus chozas... sin haber percibido explosión, olor ni fuego alguno... "
            "La tragedia del lago Nyos aportó una enseñanza monumental para la seguridad de procesos y la higiene industrial... "
            "Demostró el comportamiento implacable de los gases densos... como el dióxido de carbono, el butano o el ácido sulfhídrico... sustancias que tienden a viajar por gravedad... acumulándose en sótanos, trincheras de cañerías, pozos y recintos confinados... "
            "En cualquier entorno industrial... la medición atmosférica jamás debe realizarse únicamente a la altura de la vista... debe rastrearse milímetro a milímetro contra el suelo... "
            "Porque los asesinos invisibles más pesados que el aire... atacan desde abajo."
        )
    },
    {
        "id": "058",
        "fecha": "22 AGOSTO",
        "fechaPublicacion": "2026-08-22",
        "expediente": "Expediente #058",
        "carpeta": "2018-08-22-salpicadura-soda-caustica-trasvase-tambores",
        "titular": "EL TRASVASE MANUAL: LA SALPICADURA DE SODA CÁUSTICA",
        "palabraResaltada": "SODA CÁUSTICA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Depósito de Reactivos Químicos y Limpieza Industrial - 2018",
        "tipoRiesgo": "Riesgo Químico / EPP Específico y Procedimientos de Trasiego",
        "parrafos": [
            "El 22 de agosto de 2018, un operario de limpieza sufrió quemaduras químicas de tercer grado en el rostro y ceguera parcial al salpicarle hidróxido de sodio concentrado (soda cáustica líquida al 50%).",
            "Intentó trasvasar el químico inclinando un bidón de 25 litros a pulso sobre un balde abierto, sin utilizar bomba de trasiego ni embudo. Vestía solo anteojos de seguridad comunes y guantes de descarne de cuero.",
            "El chorro golpeó el fondo rebotando hacia su cara y penetrando el cuero absorbente de los guantes. La soda cáustica saponifica las grasas y destruye el tejido vivo en segundos si no hay lavaojos inmediato."
        ],
        "puntosClave": [
            {"icono": "shield", "titulo": "Pantalla facial y antiparras herméticas", "texto": "Para trasvase de corrosivos es obligatorio combinar gafas de copa hermética bajo una pantalla facial completa de policarbonato."},
            {"icono": "corner-down-right", "titulo": "Prohibido trasvase manual por volteo", "texto": "Utilizar bombas manuales de sifón, bombas neumáticas de diafragma o dispensadores sellados; jamás volcar a pulso recipientes pesados."},
            {"icono": "eye", "titulo": "Ducha y lavaojos a menos de 10 segundos", "texto": "El lavado con agua continua inmediata durante al menos 15 minutos es la única barrera para evitar la penetración profunda de la soda en los ojos."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: fichas de datos de seguridad (FDS) de hidróxido de sodio y normativas de protección facial y dérmica OSHA 1910.132 / 1910.133.",
        "guionReel": (
            "¿Sabías por qué la soda cáustica es uno de los químicos más destructivos para el cuerpo humano?\n\n"
            "Porque no te quema con fuego: saponifica tus tejidos. Convierte tu grasa y tus proteínas en jabón líquido en segundos.\n\n"
            "El 22 de agosto de 2018, un operario necesitaba sacar soda cáustica al 50% de un bidón grande a un balde chico. Para no buscar la bomba de trasvase, levantó el bidón a pulso y empezó a volcarlo.\n\n"
            "Tenía anteojos de seguridad comunes de patilla abierta y guantes de cuero de obra.\n\n"
            "El chorro pesado pegó en el fondo del balde y salpicó hacia arriba. El químico entró por los costados de los anteojos y empapó los guantes.\n\n"
            "Perdió la visión de un ojo y sufrió quemaduras atroces en la cara y las manos.\n\n"
            "Con corrosivos fuertes no se improvisa: bomba de trasiego, careta facial completa, guantes de nitrilo y la ducha lavaojos a mano.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Industrial chemical handling safety documentary photograph, industrial chemical room floor covered in alkaline liquid chemical spill. "
            "Overturned 25-liter plastic chemical jerrycan, yellow chemical hazard bucket, burned damaged leather work gloves, pitted splash-stained safety glasses, "
            "emergency eye wash and safety shower station visible in background with running water test, realistic macro photography, 16:9 ratio."
        ),
        "guionLargo": (
            "El veintidós de agosto de dos mil dieciocho... en el sector de preparación de reactivos de una planta manufacturera... una maniobra de trasvase rutinaria se convirtió en una tragedia de salud ocupacional irreversible... "
            "Un auxiliar de servicios generales fue asignado a fraccionar una partida de soda cáustica líquida... una solución concentrada de hidróxido de sodio al cincuenta por ciento... empleada en los procesos de desengrase y limpieza de tanques... "
            "La soda cáustica es una de las bases químicas más agresivas de la industria... Al entrar en contacto con la piel humana desata una reacción exotérmica de saponificación alcalina... disolviendo lípidos y proteínas celulares y penetrando con extrema rapidez hacia las capas tisulares profundas... "
            "El trabajador debía llenar un balde plástico de diez litros a partir de un bidón de polietileno de veinticinco kilogramos... "
            "Al no encontrar la bomba manual de trasiego de pistón que debía estar asignada al sector... optó por realizar la maniobra por el método directo de vuelco manual... "
            "Apoyó el bidón sobre su rodilla e inclinó el cuello del envase sobre el borde del balde abierto... "
            "Su equipamiento de protección personal era absolutamente inadecuado para el riesgo corrosivo... Portaba únicamente gafas de patilla abierta de seguridad mecánica... y guantes de vaqueta de descarne de cuero... "
            "A mitad del vertido... la entrada irregular de aire por la boca del bidón generó un efecto de golpe de ariete o gluglú... "
            "Un chorro intermitente de líquido espeso cayó bruscamente contra el fondo... salpicando con violencia en abanico ascendente... "
            "Las gotas cáusticas sobrepasaron los laterales abiertos de las gafas... impactando de lleno en la córnea y los párpados del operario... mientras el líquido empapaba los guantes de cuero... los cuales absorbieron el químico transfiriéndolo directamente a la piel de sus manos... "
            "Presa de un dolor enceguecedor... el trabajador intentó correr hacia la ducha lavaojos... pero el equipo de emergencia se encontraba a más de treinta metros de distancia... y el acceso estaba bloqueado por pallets de madera... "
            "El retraso en el lavado ocular le provocó lesiones cáusticas de tercer grado con perforación corneal y la pérdida irreversible de la visión en su ojo derecho... "
            "Las investigaciones de higiene industrial recordaron que los trasvases por vertido manual de corrosivos deben estar expresamente prohibidos en toda empresa... "
            "La transferencia exige circuitos cerrados o bombas de trasvase... guantes de butilo o nitrilo pesado... y una pantalla facial envolvente sobre gafas estancas... "
            "Porque ante una gota de soda cáustica... un segundo de retraso significa una secuela para toda la vida."
        )
    },
    {
        "id": "059",
        "fecha": "23 AGOSTO",
        "fechaPublicacion": "2026-08-23",
        "expediente": "Expediente #059",
        "carpeta": "2000-08-23-estatica-trasvase-solventes-inflamables",
        "titular": "LA CHISPA INVISIBLE: ESTÁTICA EN EL TRASVASE DE SOLVENTES",
        "palabraResaltada": "CHISPA INVISIBLE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Fraccionadora de Solventes e Hidrocarburos - 2000",
        "tipoRiesgo": "Atmósferas Explosivas / Electricidad Estática (Grounding & Bonding)",
        "parrafos": [
            "El 23 de agosto de 2000, un devastador incendio por deflagración destruyó un depósito de fraccionamiento de solventes en Indiana al encenderse vapores de tolueno durante el llenado de un contenedor.",
            "El operario cargaba el solvente por caída libre desde el techo del tanque sin tubo buzo sumergido, generando turbulencia. La pinza de conexión equipotencial (bonding) y puesta a tierra no estaba conectada.",
            "La fricción electrostática acumuló miles de voltios en la superficie líquida hasta descargar una chispa hacia la boca metálica. En sustancias inflamables, la puesta a tierra es la única barrera contra la estática."
        ],
        "puntosClave": [
            {"icono": "zap", "titulo": "Puesta a tierra y puente equipotencial (Bonding)", "texto": "Conectar pinzas de cobre con cable a tierra verificadas (resistencia menor a 10 ohmios) antes de abrir cualquier contenedor de solvente."},
            {"icono": "arrow-down", "titulo": "Llenado por tubo sumergido (Dip pipe)", "texto": "Prohibido el llenado por caída libre o splash filling; la lanza de carga debe llegar al fondo del recipiente para minimizar estática."},
            {"icono": "gauge", "titulo": "Control de velocidad inicial de bombeo", "texto": "Limitar la velocidad de flujo a menos de 1 metro por segundo hasta que el extremo del tubo quede completamente sumergido (NFPA 77)."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: normas de control de electricidad estática en operaciones con líquidos inflamables NFPA 77 y directrices técnicas de prevención de la Chemical Safety Board (CSB).",
        "guionReel": (
            "¿Sabías que un líquido cayendo dentro de un tambor puede generar más de diez mil voltios de electricidad estática sin que te des cuenta?\n\n"
            "El 23 de agosto del año 2000, en una planta fraccionadora en Indiana, un operador llenaba un contenedor metálico con tolueno.\n\n"
            "Metió la manguera apenas por la tapa y empezó a bombear a toda velocidad. El líquido caía como una cascada, chapoteando y generando fricción.\n\n"
            "El operador vio la pinza de puesta a tierra tirada en el suelo, pero no la conectó porque pensó que 'era solo un tamborcito'.\n\n"
            "La carga electrostática subió en el líquido hasta que saltó una chispa invisible hacia el metal. La nube de vapores de tolueno detonó en una bola de fuego instantánea.\n\n"
            "La planta ardió por completo y el operario sufrió quemaduras críticas.\n\n"
            "Con líquidos inflamables, el puente equipotencial y la puesta a tierra no son opcionales: salvan tu vida.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Dramatic industrial explosion documentary photography, petrochemical solvent packaging facility engulfed in sudden flash fire, August 23 2000. "
            "Ruptured metallic intermediate bulk container (IBC) surrounded by intense orange flames and black smoke, grounded copper bonding cables and clamp lying loose on floor, "
            "safety fire deluge foam nozzles activating overhead, industrial concrete warehouse backdrop, cinematic high contrast, 16:9 ratio."
        ),
        "guionLargo": (
            "El veintitrés de agosto del año dos mil... en un establecimiento dedicado al envasado, fraccionamiento y distribución de productos petroquímicos en el estado de Indiana... la física de la electricidad estática cobró un precio altísimo... "
            "En la bahía de llenado... un trabajador realizaba la carga de un contenedor metálico industrial de mil litros con tolueno puro... un solvente hidrocarburo ampliamente utilizado en pinturas y adhesivos... "
            "El tolueno posee una característica electroquímica crítica... es un líquido dieléctrico de muy baja conductividad eléctrica... lo que significa que retiene con enorme facilidad las cargas electrostáticas que se generan durante su transporte o manipulación... "
            "El operario introdujo el pico de la manguera de llenado a escasos centímetros de la boca superior... iniciando el bombeo a caudal máximo... "
            "Este método... conocido en ingeniería química como llenado por salpicadura o splash filling... provoca una turbulencia severa... donde la fricción entre las moléculas del solvente... las gotas pulverizadas y el aire... actúa como un descomunal generador electrostático... "
            "Junto al contenedor descansaba el cable con la pinza de puesta a tierra y puente equipotencial... cuyo propósito es disipar las cargas estáticas hacia la malla de tierra del edificio... igualando el potencial eléctrico entre la manguera y el tambor... "
            "Confiado por años de labor sin incidentes... el trabajador no conectó la pinza al chasis del recipiente... "
            "A medida que el nivel subía... la diferencia de potencial electrostático en la superficie del líquido trepó por encima de los quince mil voltios... "
            "En el espacio de cabeza del contenedor... la mezcla de vapores de tolueno y aire se encontraba en pleno rango de inflamabilidad... "
            "Bastó que el operario acercara la mano a la boca de carga metálica para que la tensión acumulada encontrara un camino de descarga... "
            "Una chispa electrostática invisible cruzó el espacio de vapor... desatando una violenta deflagración... "
            "La tapa del contenedor salió despedida... y una llamarada voraz envolvió al trabajador y a las líneas de suministro... provocando un incendio generalizado que consumió las instalaciones en cuestión de minutos... "
            "La norma internacional NFPA 77 es concluyente... La electricidad estática es un riesgo latente y traicionero en todo trasvase de solventes... "
            "La regla es inviolable... Primero se conectan las pinzas de puesta a tierra certificadas... se verifica la continuidad de resistencia menor a diez ohmios... y se utiliza siempre un tubo buzo sumergido hasta el fondo... antes de bombear una sola gota de inflamable."
        )
    },
    {
        "id": "060",
        "fecha": "24 AGOSTO",
        "fechaPublicacion": "2026-08-24",
        "expediente": "Expediente #060",
        "carpeta": "2019-08-24-atrapamiento-prensa-plegadora-pedal",
        "titular": "EL PIE EN EL PEDAL: EL ATRAPAMIENTO EN LA PLEGADORA",
        "palabraResaltada": "PIE EN EL PEDAL",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Taller de Plegado y Deformación de Chapas Metálicas - 2019",
        "tipoRiesgo": "Protección de Máquinas / Prensas Plegadoras Hidráulicas",
        "parrafos": [
            "El 24 de agosto de 2019, un operario metalúrgico de 29 años sufrió el aplastamiento y amputación de cuatro dedos al descender la matriz de una prensa plegadora hidráulica de 80 toneladas.",
            "Mientras sostenía con sus manos una pieza metálica pequeña dentro de la zona de peligro, pisó accidentalmente el pedal de accionamiento. El pedal carecía de la cubierta protectora superior antivandálica y de enclavamiento.",
            "La máquina tenía la cortina óptica de seguridad alineada incorrectamente para piezas cortas y no se utilizaron pinzas de sujeción. La lección: pedales con capuchón protector y barreras fotoeléctricas activas.",
        ],
        "puntosClave": [
            {"icono": "shield-check", "titulo": "Pedales con capuchón envolvente", "texto": "El pedal de accionamiento debe poseer protección superior y lateral rígida con pestillo mecánico para impedir pisadas involuntarias."},
            {"icono": "scan", "titulo": "Cortinas fotoeléctricas AOPD calibradas", "texto": "Sistemas de detección óptica multihaz que frenan instantáneamente la cuchilla si una mano cruza el plano de plegado."},
            {"icono": "tool", "titulo": "Herramientas auxiliares de sujeción", "texto": "Prohibido ingresar las manos en la matriz; utilizar pinzas magnéticas o ventosas para posicionar piezas de chapa cortas."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: normas de seguridad en prensas mecánicas e hidráulicas de OSHA 1910.217 y directrices de protección de plegadoras ANSI B11.3.",
        "guionReel": (
            "¿Sabías que un pedal de máquina sin protección es una trampa que tú mismo puedes activar sin darte cuenta?\n\n"
            "El 24 de agosto de 2019, en un taller metalúrgico, un joven operario doblaba piezas chicas de chapa en una prensa plegadora hidráulica de ochenta toneladas.\n\n"
            "Para que la pieza quedara derecha, metió los dedos dentro de la matriz de corte. En ese mismo instante, perdió el equilibrio y apoyó el pie sobre el pedal de marcha.\n\n"
            "El pedal era plano, sin capuchón protector de fábrica porque se lo habían sacado para 'estar más cómodos'.\n\n"
            "La cuchilla bajó con ochenta toneladas de fuerza en una milésima de segundo, aplastándole cuatro dedos de la mano izquierda.\n\n"
            "Las manos jamás se meten en la matriz: usa pinzas magnéticas, cortinas de luz calibradas y exige siempre el pedal con protección superior.\n\n"
            "Tu comodidad no vale una mano mutilada."
        ),
        "promptImagen": (
            "Industrial metal stamping press machinery accident documentary photography, modern hydraulic CNC press brake metal bending machine. "
            "Bent steel sheet caught in heavy upper punch and lower V-die tooling, unprotected electrical foot pedal switch on concrete workshop floor, "
            "optical light curtain sensor laser beam aligned along bed, discarded magnetic sheet handler tool on table, high realism, 16:9 ratio."
        ),
        "guionLargo": (
            "El veinticuatro de agosto de dos mil diecinueve... en una planta metalmecánica dedicada a la transformación y plegado de chapa de acero... un desvío operativo común desencadenó una mutilación irreversible... "
            "En el sector de conformado, un operario trabajaba en una prensa plegadora hidráulica de control numérico... un equipo capaz de ejercer una fuerza de cierre de ochenta toneladas... "
            "El trabajo consistía en realizar pestañas de doblado en una serie de pequeñas placas metálicas de apenas diez centímetros de longitud... "
            "Debido al tamaño reducido de las piezas... el trabajador sostenía la chapa directamente con la yema de sus dedos... posicionando sus manos a escasos centímetros de la línea de fuego... el punto de apriete entre el punzón superior móvil y la matriz inferior en V... "
            "En lugar de utilizar pinzas de sujeción neumáticas o herramientas magnéticas de manipulación que mantuvieran sus manos fuera de la zona de pellizco... el operario confiaba en su destreza manual... "
            "A mitad del turno... mientras reacomodaba una chapa rebelde... el operario balanceó su peso corporal hacia adelante... "
            "De manera totalmente involuntaria... su pie descendió sobre el pedal eléctrico de accionamiento posicionado sobre el piso de cemento... "
            "Aquel pedal carecía de la campana metálica de protección superior... una carcasa envolvente obligatoria provista por los fabricantes para impedir que un objeto caído o un traspié accidental accione el contacto de marcha... "
            "La cortina fotoeléctrica de seguridad láser multihaz... que debía detener instantáneamente el descenso de la viga si un cuerpo extraño invadía el plano de la matriz... había sido puenteada o configurada en modo silenciado para piezas pequeñas... "
            "El pesado punzón descendió con fuerza demoledora en una fracción de segundo... aplastando la chapa y triturando cuatro dedos de la mano izquierda del trabajador... "
            "Las investigaciones periciales subrayaron que las prensas plegadoras son una de las máquinas herramientas de mayor siniestralidad en la industria metalúrgica... "
            "La seguridad mecánica en prensas descansa sobre barreras de ingeniería innegociables... El pedal debe poseer siempre capuchón protector y traba de seguridad... las barreras ópticas AOPD deben auditarse a diario... y las manos jamás deben ingresar al espacio de matrizado bajo ninguna circunstancia."
        )
    },
    {
        "id": "061",
        "fecha": "25 AGOSTO",
        "fechaPublicacion": "2026-08-25",
        "expediente": "Expediente #061",
        "carpeta": "2012-08-25-explosion-refineria-amuay-gas",
        "titular": "LA NUBE EN EL PATIO DE TANQUES: LA EXPLOSIÓN DE AMUAY",
        "palabraResaltada": "EXPLOSIÓN DE AMUAY",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Complejo Refinador de Paraguaná (CRP), Refinería de Amuay, Venezuela - 2012",
        "tipoRiesgo": "Seguridad de Procesos (Oil & Gas) / Pérdida Catastrófica de Contención",
        "parrafos": [
            "La madrugada del 25 de agosto de 2012, una masiva explosión por nube de vapor de gas inflamable (VCE) destruyó el bloque 23 de la refinería de Amuay en Venezuela, cobrando la vida de 42 personas.",
            "Una fuga descontrolada de gas licuado en los sellos de bombas de olefinas no fue detectada ni aislada a tiempo. La densa nube de hidrocarburos pesados avanzó por el patio de tanques hacia un destacamento de guardia vecino.",
            "Al hallar una fuente de ignición en vehículos encendidos, la nube detonó incendiando nueve tanques de nafta y destrozando viviendas. El desastre expuso fallas críticas en mantenimiento de sellos y sistemas fijos de detección.",
        ],
        "puntosClave": [
            {"icono": "radio", "titulo": "Detección fija perimetral de gas (F&G)", "texto": "Sensores infrarrojos y electroquímicos de gas combustible con alarmas comunitarias audibles en toda el área de proceso."},
            {"icono": "shield-alert", "titulo": "Mantenimiento preventivo de sellos mecánicos", "texto": "Monitoreo continuo de presiones y temperatura en sistemas de sellado de bombas de olefinas según API 682."},
            {"icono": "map-pin", "titulo": "Zonificación y amortiguamiento urbano", "texto": "Mantener distancias de amortiguamiento físico infranqueables entre parques de almacenamiento y cuarteles o zonas pobladas."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informes periciales independientes del Centro de Orientación en Energía (COENER) y normativas internacionales de seguridad de procesos API 752 / OSHA 1910.119.",
        "guionReel": (
            "¿Qué ocurre cuando una fuga de gas en una refinería se ignora durante más de una hora?\n\n"
            "La madrugada del 25 de agosto de 2012, en la refinería de Amuay en Venezuela, una falla en los sellos de unas bombas liberó una gigantesca cantidad de olefinas y gas licuado.\n\n"
            "El gas era pesado. En vez de elevarse, formó una densa niebla a ras del piso que comenzó a arrastrarse por el patio de tanques, cubriendo avenidas y llegando a un destacamento militar lindero.\n\n"
            "Los detectores de gas no sonaron y las válvulas de corte de emergencia no se activaron.\n\n"
            "A la una de la mañana, un vehículo en marcha o una chispa encendió la nube. La explosión fue brutal: nueve tanques de combustible ardieron en llamas, 42 personas murieron y cientos quedaron heridas.\n\n"
            "En plantas petroquímicas, una fuga de gas no se vigila: se aísla de inmediato con corte de emergencia.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Massive oil refinery disaster archival documentary photography, night of August 25 2012 Amuay refinery explosion Venezuela. "
            "Colossal wall of fire leaping from multiple burning spherical and floating-roof fuel storage tanks, thick black smoke billows into nighttime sky, "
            "crumpled structural steel columns, destroyed emergency vehicles, flashing red beacons of fire engines fighting blaze from perimeter, 16:9 ratio."
        ),
        "guionLargo": (
            "La madrugada del veinticinco de agosto de dos mil doce... en la península de Paraguaná, en el occidente de Venezuela... la refinería de Amuay... una de las instalaciones de refinación de petróleo más grandes del planeta... fue escenario de una tragedia dantesca... "
            "En el bloque número veintitrés de la planta... destinado al almacenamiento de componentes livianos y esferas de gas licuado de petróleo... una avería mecánica en los sellos de estanqueidad de una batería de bombas de olefinas provocó una fuga masiva de hidrocarburos altamente volátiles... "
            "El propileno y butano liberados a presión experimentaron una evaporación violenta... "
            "Al ser gases con un peso molecular superior al del aire ambiente... y bajo condiciones meteorológicas de calma de viento... no se elevaron ni se dispersaron hacia la atmósfera superior... "
            "En su lugar... conformaron una densa sábana blanca de vapor combustible que comenzó a desplazarse a nivel del terreno... inundando canales de desagüe... calles internas de la refinería y las inmediaciones del Destacamento de la Guardia Nacional adyacente al complejo... "
            "A pesar de los reportes iniciales de fuerte olor a gas... los sistemas fijos de detección y alarma de gas y fuego no respondieron eficazmente... y las válvulas de aislamiento motorizadas no fueron accionadas para seccionar la fuga... "
            "Durante casi una hora... la nube de vapor inflamable continuó expandiéndose sin control... hasta alcanzar una concentración dentro de los límites de explosividad... "
            "Poco después de la una de la mañana... la masa de gas encontró un punto de ignición en el encendido de un motor de vehículo o en las instalaciones eléctricas no clasificadas del cuartel lindero... "
            "La explosión por deflagración de nube de vapor fue apocalíptica... Una onda expansiva de tremenda potencia arrasó con edificaciones de hormigón... cuarteles militares y viviendas civiles en un radio de varios kilómetros... "
            "La onda ígnea encendió nueve tanques de almacenamiento de nafta y destilados livianos... desatando un incendio colosal que ardió durante cuatro días... "
            "Cuarenta y dos personas perdieron la vida... en su mayoría efectivos militares y familiares que dormían en el destacamento... y más de ochenta resultaron con quemaduras severas... "
            "El desastre de Amuay evidenció fallas críticas de gestión de integridad mecánica y mantenimiento preventivo en sellos de bombeo de fluidos volátiles... "
            "Y dejó una lección imperecedera sobre la gestión del riesgo territorial... Los puestos de control, cuarteles y urbanizaciones jamás deben situarse en la línea de fuego de un parque de tanques petroquímico."
        )
    },
    {
        "id": "062",
        "fecha": "26 AGOSTO",
        "fechaPublicacion": "2026-08-26",
        "expediente": "Expediente #062",
        "carpeta": "2016-08-26-electrocucion-traslado-andamio-linea-aerea",
        "titular": "EL ARCO EN EL TENDIDO AÉREO: EL TRASLADO DEL ANDAMIO",
        "palabraResaltada": "ARCO EN EL TENDIDO AÉREO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Obra de Mantenimiento de Fachadas y Vía Pública - 2016",
        "tipoRiesgo": "Riesgo Eléctrico / Trabajo en Altura y Líneas Aéreas Energizadas",
        "parrafos": [
            "El 26 de agosto de 2016, dos obreros fallecieron electrocutados y un tercero sufrió quemaduras de extrema gravedad al desplazar un andamio tubular metálico sobre ruedas que rozó una línea aérea de media tensión.",
            "Para evitar el tiempo de desarme y rearmado, la cuadrilla empujó la torre de seis metros de altura armada por la vereda. La baranda superior tocó un cable de 13.200 voltios, energizando la estructura al instante.",
            "La obra carecía de relevamiento de interferencias eléctricas y no se respetó la distancia mínima de seguridad de 3 metros. El traslado de andamios armados cerca de líneas vivas es una práctica letal y prohibida.",
        ],
        "puntosClave": [
            {"icono": "zap-off", "titulo": "Distancias de seguridad eléctrica infranqueables", "texto": "Mantener como mínimo 3 metros en baja tensión y 5 metros en media tensión (13.2 kV) respecto a cualquier elemento metálico."},
            {"icono": "arrow-down-left", "titulo": "Desarmar antes de trasladar", "texto": "Prohibido desplazar andamios armados de más de un cuerpo; desmontar por módulos para garantizar que la altura esté fuera del radio eléctrico."},
            {"icono": "eye", "titulo": "Vigía y relevamiento previo de líneas vivas", "texto": "Identificar todos los tendidos aéreos antes de iniciar faenas y gestionar con la distribuidora eléctrica la colocación de fundas aislantes o el corte de tensión."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: directrices de seguridad eléctrica en proximidad de líneas de energía de OSHA 1926.451 / 1926.1408 y normativas de seguridad en construcción de la NFPA 70E.",
        "guionReel": (
            "¿Por qué ahorrarte media hora desarmando un andamio puede costarte la vida?\n\n"
            "El 26 de agosto de 2016, tres pintores terminaban la fachada de un edificio. Para pintar el frente de al lado, decidieron no desarmar el andamio tubular de seis metros de altura.\n\n"
            "Lo empujaron entre los tres sobre las ruedas por la vereda, mirando hacia el piso para esquivar las baldosas rotas.\n\n"
            "Arriba pasaba un tendido eléctrico de media tensión de 13.200 voltios.\n\n"
            "Ni siquiera tuvieron que tocar el cable: al acercarse a pocos centímetros, la corriente saltó en un arco eléctrico brutal.\n\n"
            "El andamio entero se energizó en un milisegundo. Dos de los trabajadores murieron electrocutados en el acto y el tercero sufrió quemaduras gravísimas.\n\n"
            "Cerca de cables eléctricos, los andamios se desarman siempre antes de moverlos y se respeta la distancia de seguridad.\n\n"
            "La electricidad no avisa."
        ),
        "promptImagen": (
            "Urban electrical accident documentary photography, modern street sidewalk facade maintenance site with high mobile modular steel scaffolding tower. "
            "Scaffolding top rail dangerously close to low-hanging overhead utility power lines, burned scorch marks on metal tubes, abandoned work boots and safety gear on sidewalk, "
            "police perimeter red caution tape, emergency utility power bucket truck arriving in background, realistic dramatic photojournalism, 16:9 ratio."
        ),
        "guionLargo": (
            "El veintiséis de agosto de dos mil dieciséis... en una concurrida avenida comercial durante la ejecución de trabajos de pintura y refacción de una fachada urbana... una decisión operativa apresurada provocó una fatalidad eléctrica instantánea... "
            "Una cuadrilla de tres trabajadores había concluido el hidrolavado y sellado de grietas en el frente de un inmueble de dos plantas... "
            "Para realizar la tarea... habían montado una torre de andamio tubular metálico multidireccional de tres cuerpos... con una altura total superior a los seis metros... montada sobre cuatro ruedas giratorias de poliuretano con freno... "
            "Llegado el momento de trasladarse hacia el inmueble lindero para continuar con el cronograma del día... los operarios evaluaron que desarmar los caños horizontales, diagonales y plataformas metálicas demandaría más de una hora de labor... "
            "Con el fin de evitar esa demora... destrabaron los frenos de las ruedas y decidieron empujar la estructura completa armada a lo largo de la vereda... "
            "Los tres trabajadores se posicionaron en la base... ejerciendo fuerza física contra los parantes inferiores mientras miraban hacia el suelo para esquivar desniveles en las baldosas y árboles... "
            "Nadie fue designado para mirar hacia arriba y vigilar la trayectoria del extremo superior de la torre... "
            "Por encima de la acera... a seis metros y medio de altura... discurría un tendido aéreo de distribución de media tensión de trece mil doscientos voltios... sostenido por postes de hormigón... "
            "Al empujar el andamio sobre un badén... la estructura osciló levemente hacia el cordón de la calle... "
            "En la física de la media tensión... el aire puede sufrir una ruptura dieléctrica sin necesidad de contacto mecánico directo... "
            "A escasos centímetros de distancia... un arco voltaico de tremenda energía ionizó el aire y se transfirió a la baranda superior del andamio... "
            "Una corriente de miles de amperios descendió de manera instantánea por los caños de acero hacia la tierra... atravesando el cuerpo de los tres trabajadores que sujetaban la estructura... "
            "Dos de ellos fallecieron en el acto por fibrilación ventricular... mientras que el tercero sufrió quemaduras de cuarto grado con amputación de extremidades... "
            "Las normativas internacionales de seguridad eléctrica en la construcción son categóricas... El traslado de andamios armados de más de un módulo está estrictamente prohibido... "
            "Frente a conductores energizados... la distancia mínima de seguridad de cinco metros es una barrera sagrada... y todo movimiento exige desmontar la torre por secciones... "
            "Porque ante la media tensión... la confianza y el descuido cobran la vida en una fracción de milisegundo."
        )
    }
]

def procesar_lote_5(kokoro_instance):
    procesadas = []

    print(f"\n=======================================================")
    print(f"Iniciando procesamiento de {len(LOTE_5_DATA)} historias del Lote 5 (#053 a #062)")
    print(f"=======================================================\n")

    for h in LOTE_5_DATA:
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
            crear_portada_grafica_lote5(h, portada_path)
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

def crear_portada_grafica_lote5(historia, output_path):
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
    """Inyecta las historias del Lote 5 en index.html antes del cierre del array historias."""
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

    print("\n✓ index.html actualizado exitosamente con los 10 nuevos expedientes (#053 a #062).")
    return True

def main():
    print("Iniciando motor Kokoro para Lote 5 (#053 a #062)...")
    kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

    procesadas = procesar_lote_5(kokoro)

    if inyectar_en_index_html(procesadas):
        print(f"\n🎉 ¡LOTE 5 COMPLETADO AL 100%! ({len(procesadas)} historias procesadas)")

if __name__ == "__main__":
    main()
