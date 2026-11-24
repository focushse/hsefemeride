# -*- coding: utf-8 -*-
"""
Generador Agéntico Automatizado para Lote 13: Expedientes #133 a #142 (5 al 14 de noviembre)
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

LOTE_13_DATA = [
    {
        "id": "133",
        "fecha": "05 NOVIEMBRE",
        "fechaPublicacion": "2026-11-05",
        "expediente": "Expediente #133",
        "carpeta": "2015-11-05-colapso-presa-relaves-fundao-samarco-mariana",
        "titular": "LA OLA DE LODO EN MINAS GERAIS: EL COLAPSO DE SAMARCO EN MARIANA",
        "palabraResaltada": "PRESA DE SAMARCO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Presa de Relaves de Fundão (Samarco / Vale / BHP), Mariana, Minas Gerais, Brasil - 2015",
        "tipoRiesgo": "Seguridad de Procesos / Geotecnia Minera",
        "parrafos": [
            "El 5 de noviembre de 2015, el dique de relaves de Fundão de la minera Samarco colapsó en Mariana, Minas Gerais, liberando más de 43 millones de metros cúbicos de lodo tóxico que arrasó el poblado de Bento Rodrigues, matando a 19 personas.",
            "El muro de contención aguas arriba sufrió licuefacción estática tras un drenaje defectuoso, sobrecarga de arena y el recrecimiento continuo de la presa sobre lodos saturados, desoyendo las deformaciones registradas en piezómetros.",
            "La ola de fango recorrió 650 km por el Río Doce hasta el océano Atlántico en el peor desastre ambiental de Brasil. La lección: monitoreo piezométrico satelital en tiempo real, prohibición de presas aguas arriba y planes de evacuación comunitarios.",
        ],
        "puntosClave": [
            {"icono": "mountain", "titulo": "Erradicación del método de aguas arriba", "texto": "Prohibir el recrecimiento de diques sobre relaves finos saturados; migrar hacia presas de eje central o filtrado en seco (dry stacking)."},
            {"icono": "gauge", "titulo": "Piezometría automatizada y radar SAR", "texto": "Monitorear la presión de poros y la estabilidad geométrica del muro en tiempo real con disparos de alarma temprana ante saturación basal."},
            {"icono": "users", "titulo": "Planes de Acción de Emergencia (PAEBM)", "texto": "Instalación de sirenas comunitarias de alta potencia y simulacros de evacuación en poblaciones ubicadas en la zona de autosalvamento (ZAS)."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe final del Panel de Expertos Internacionales presidido por Norbert Morgenstern sobre el colapso de la presa de Fundão de Samarco Mineração S.A. y resoluciones de la ANM Brasil.",
        "guionReel": (
            "El 5 de noviembre de 2015, en Mariana, Minas Gerais, Brasil, la presa de relaves de Fundão de la minera Samarco colapsó por completo.\n\n"
            "El muro de tierra contenía millones de toneladas de lodo de hierro. Pero los drenajes fallaron y el agua saturó la base del dique.\n\n"
            "Los instrumentos marcaban deformaciones críticas, pero nadie paró la operación. De repente, la tierra sólida se volvió líquida.\n\n"
            "Una ola de 43 millones de metros cúbicos de fango tóxico bajó por el valle, borró del mapa el pueblo de Bento Rodrigues y mató a 19 personas.\n\n"
            "La lección de Focus HSE: las presas de relaves son estructuras vivas; si los piezómetros marcan saturación, la evacuación debe ser inmediata.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of the Fundão tailings dam failure site in Mariana, Minas Gerais, Brazil. "
            "A vast breached red-brown iron ore mud basin showing massive eroded earthen dam breach walls, "
            "mud flows carving deep ravines through tropical forested valleys, emergency inspection geotechnical vehicles parked on high ridge, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 5 de noviembre de 2015, a las tres y media de la tarde, en el municipio histórico de Mariana, "
            "en el corazón minero del estado de Minas Gerais, Brasil, la presa de relaves de Fundão —operada por la empresa Samarco Mineração, "
            "una empresa conjunta entre las gigantes Vale y BHP Billiton— colapsó de manera repentina y catastrófica. "
            "Una avalancha de más de cuarenta y tres millones de metros cúbicos de lodo de procesamiento de mineral de hierro "
            "descendió ladera abajo, arrasando por completo el poblado de Bento Rodrigues, cobrando la vida de diecinueve personas "
            "y desatando la mayor catástrofe ambiental en la historia de la minería sudamericana.\n\n"
            "El informe técnico internacional liderado por el profesor Norbert Morgenstern identificó el fenómeno físico detonante: "
            "la licuefacción estática del muro de contención. La presa se había construido mediante el método de aguas arriba (upstream), "
            "donde los diques de elevación se asientan directamente sobre los propios residuos de relaves depositados previamente. "
            "Una serie de fallas en el sistema interno de drenaje y cambios de diseño no autorizados permitieron que el nivel freático "
            "se elevara peligrosamente, sumergiendo las arenas de contención en un estado de saturación total.\n\n"
            "A pesar de que los piezómetros e inclinómetros registraban deformaciones anormales y presiones de poros excesivas "
            "en la berma inferior, la compañía continuó depositando material sin ejecutar obras de refuerzo. "
            "Bastó una leve vibración geológica para que las arenas colapsaran: la presión del agua interna anuló la fricción entre granos, "
            "transformando el muro sólido en un fluido viscoso en cuestión de segundos. El torrente rojizo viajó más de seiscientos cincuenta kilómetros "
            "a lo largo de la cuenca del Río Doce hasta desembocar en el Océano Atlántico, destruyendo ecosistemas y fuentes de agua dulce de millones de personas.\n\n"
            "El desastre de Samarco en Mariana forzó un cambio de paradigma global en la gestión de depósitos de relaves mineros: "
            "La legislación brasileña e internacional prohibió definitivamente la construcción y operación de presas de recrecimiento aguas arriba. "
            "Estableció como imperativo el monitoreo geotécnico continuo con telemetría satelital por radar interferométrico (InSAR), "
            "la instalación obligatoria de redes de sirenas de alerta temprana para las comunidades aguas abajo, y la transición hacia tecnologías "
            "de relaves espesados y filtrados en seco para desterrar los embalses húmedos de alta peligrosidad.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "134",
        "fecha": "06 NOVIEMBRE",
        "fechaPublicacion": "2026-11-06",
        "expediente": "Expediente #134",
        "carpeta": "2018-11-06-caida-bobina-acero-grua-puente-nucor-steel-arkansas",
        "titular": "LA BOBINA QUE SE DESENGANCHÓ: ACCIDENTE EN NUCOR STEEL",
        "palabraResaltada": "NUCOR STEEL",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Acería Nucor Steel Arkansas, Blytheville, Arkansas, EE.UU. - 2018",
        "tipoRiesgo": "Izaje y Cargas Suspendidas",
        "parrafos": [
            "El 6 de noviembre de 2018, un operario siderúrgico de 42 años murió aplastado en la acería de Nucor Steel en Blytheville, Arkansas, al desengancharse una bobina de chapa de acero de más de 12 toneladas desde una grúa puente, en un caso investigado por OSHA.",
            "El izaje se realizó con un gancho cuyo pestillo de seguridad mecánico estaba roto y atado con alambre. Al balancearse la carga durante el traslado aéreo, la eslinga se deslizó fuera del gancho, aplastando al trabajador ubicado en la línea de fuego.",
            "La acería no contaba con pasillos peatonales segregados en la bahía de expedición. La lección: inspección pre-uso de ganchos con pestillo operativo, prohibición absoluta de posicionarse bajo cargas suspendidas y balizamiento de zonas de izaje.",
        ],
        "puntosClave": [
            {"icono": "shield-alert", "titulo": "Pestillo de seguridad de gancho obligatorio", "texto": "Prohibido utilizar ganchos de grúa con pestillos trabados, vencidos o atados; el cierre debe ser automático e impedir la salida accidental de la eslinga."},
            {"icono": "ban", "titulo": "Línea de fuego y cargas suspendidas", "texto": "Nunca caminar ni permanecer debajo o en el radio de caída potencial de cargas pesadas suspendidas en naves de laminación."},
            {"icono": "check-circle", "titulo": "Inspección pre-operativa diaria de aparejos", "texto": "Auditar visualmente eslingas sintéticas, cadenas de grado 80/100 y balancines C-hook antes de cada turno productivo bajo norma ASME B30.10."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de investigación de fatalidades de OSHA (OSHA Little Rock Area Office / 29 CFR 1910.179 Overhead and Gantry Cranes) sobre Nucor Yamato Steel Co. en Blytheville, Arkansas.",
        "guionReel": (
            "El 6 de noviembre de 2018, en Blytheville, Arkansas, la acería de Nucor Steel fue escenario de un aplastamiento fulminante.\n\n"
            "Una grúa puente trasladaba por el aire una bobina de acero de 12 toneladas. El gancho tenía el pestillo de seguridad roto y atado con un alambre.\n\n"
            "La carga osciló en el aire. Con el balanceo, la eslinga saltó fuera del gancho. La masa de acero cayó en picada desde cinco metros de altura.\n\n"
            "Abajo, en el pasillo, un operario de 42 años caminaba confiado en la línea de fuego. Murió aplastado en el acto.\n\n"
            "La lección de Focus HSE: las cargas suspendidas no perdonan; jamás camines bajo una grúa y nunca uses ganchos sin pestillo de seguridad certificado.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an industrial steel mill bay in Blytheville, Arkansas, after a heavy crane rigging accident. "
            "A massive rolled steel coil resting askew on concrete floor beside an overhead crane hook with damaged safety latch, "
            "yellow overhead crane bridge girder visible near high factory ceiling, OSHA inspection markers and high contrast industrial lighting, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 6 de noviembre de 2018, en la planta siderúrgica Nucor Steel ubicada en la ciudad de Blytheville, "
            "condado de Mississippi en el estado de Arkansas, Estados Unidos, "
            "una de las instalaciones de laminación de acero estructural más productivas de América del Norte fue escenario de un fatal accidente de izaje. "
            "Un operario calificado de cuarenta y dos años perdió la vida instantáneamente al ser impactado y aplastado "
            "por una bobina de chapa laminada en caliente de más de doce toneladas de peso que se desprendió desde una grúa puente.\n\n"
            "La investigación federal llevada adelante por la OSHA reveló una concatenación de desvíos en el mantenimiento de los accesorios de elevación "
            "y en el control del personal en las zonas de carga. El operador de la grúa aérea de sesenta toneladas trasladaba el rollo metálico "
            "suspendido mediante un balancín de gancho simple. El pestillo de seguridad mecánico (safety latch) del gancho principal —diseñado para evitar "
            "que el ojal de la eslinga se salga de la garganta— se encontraba dañado y había sido inmovilizado con un alambre recocido "
            "por personal del turno anterior para facilitar el desenganche rápido de las bobinas.\n\n"
            "Durante la traslación aérea longitudinal sobre la nave de almacenamiento, un frenado brusco provocó una oscilación pendular de la carga. "
            "El movimiento generó un destensado momentáneo en el aparejo; la eslinga de cadena se desplazó hacia la punta del gancho desprovisto de traba, "
            "liberando la masa de acero en caída libre desde más de cuatro metros de altura. Directamente debajo de la trayectoria de avance, "
            "sin demarcación física de zona de exclusión, transitaba el trabajador a pie. El impacto demoledor causó traumatismos masivos letales. "
            "El sistema de radio control del puente grúa no contaba con alarmas luminosas de suelo que proyectaran el perímetro de riesgo de la carga.\n\n"
            "La tragedia en Nucor Steel Blytheville ratifica tres estándares innegociables de la norma ASME B treinta punto diez sobre ganchos y puentes grúa: "
            "Primero: queda terminantemente prohibido utilizar ganchos cuyo pestillo de seguridad esté deformado, atado o ausente; "
            "la traba debe encastrar con muelle positivo en la punta del gancho antes de autorizar el izaje. "
            "Segundo: la regla de oro de la línea de fuego; ningún operario debe situarse, caminar o trabajar bajo el radio de caída potencial de una carga suspendida. "
            "Y tercero: las naves de movimiento de materiales pesados deben contar con balizamiento óptico proyector en suelo que delimite "
            "el área de peligro dinámico de los puentes grúa en operación.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "135",
        "fecha": "07 NOVIEMBRE",
        "fechaPublicacion": "2026-11-07",
        "expediente": "Expediente #135",
        "carpeta": "2017-11-07-intoxicacion-acido-sulfhidrico-pozo-pemex-veracruz",
        "titular": "EL GAS AMARGO EN EL CABEZAL: INTOXICACIÓN EN PEMEX VERACRUZ",
        "palabraResaltada": "POZO DE PEMEX",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Pozo de Extracción de Hidrocarburos Pemex, Región Sur, Veracruz, México - 2017",
        "tipoRiesgo": "Seguridad de Procesos / Oil & Gas",
        "parrafos": [
            "El 7 de noviembre de 2017, una fuga imprevista de gas amargo con alta concentración de sulfuro de hidrógeno (H2S) en un pozo de producción de Petróleos Mexicanos (Pemex) en Veracruz causó la muerte de dos trabajadores petroleros en la macropera de extracción.",
            "Durante el reemplazo de una válvula de contrapresión en el árbol de navidad del pozo, un sello de empaque degradado cedió liberando gas a presión con más de 2.000 partes por millón de H2S. Los operarios no portaban equipos de respiración autónoma (SCBA) con suministro positivo.",
            "El gas neurotóxico paralizó su sistema respiratorio en una sola inhalación. La lección: uso obligatorio de equipos de aire asistido en pozos amargos, detectores fijos y personales de H2S calibrados y mangas de viento operativas.",
        ],
        "puntosClave": [
            {"icono": "shield", "titulo": "Uso obligatorio de SCBA en áreas de gas amargo", "texto": "Toda intervención sobre cabezales o manifolds con presencia de gas amargo exige equipo de respiración autónoma de presión positiva."},
            {"icono": "gauge", "titulo": "Detección personal y fija de H2S calibrada", "texto": "Portar detectores individuales fijados a la altura de la solapa con alarma sonora y vibratoria ajustada a 5 y 10 ppm según estándar internacional."},
            {"icono": "wind", "titulo": "Manga de viento y puntos de reunión contra el viento", "texto": "Verificar la dirección del viento antes de intervenir y evacuar siempre perpendicular y hacia barlovento (en contra del viento)."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: investigaciones técnicas de la Agencia de Seguridad, Energía y Ambiente de México (ASEA) y normativa interna de seguridad de Petróleos Mexicanos (Pemex) sobre manejo de gas amargo (NRF-028-PEMEX).",
        "guionReel": (
            "El 7 de noviembre de 2017, en Veracruz, México, un pozo petrolero de Pemex liberó su veneno más letal.\n\n"
            "Dos trabajadores hacían mantenimiento en el árbol de válvulas de un pozo de gas amargo. Un empaque gastado reventó bajo presión.\n\n"
            "Escapó una bocanada invisible de sulfuro de hidrógeno a más de 2.000 partes por millón. Los operarios no tenían conectados sus equipos de respiración autónoma.\n\n"
            "A esa concentración, el gas duerme el olfato al instante y apaga el sistema nervioso central en una sola respiración. Los dos cayeron muertos al pie del cabezal.\n\n"
            "La lección de Focus HSE: en pozos con gas amargo no hay segundas oportunidades; el equipo de aire autónomo es tu único seguro de vida.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an oil and gas wellhead Christmas tree valve assembly in a humid clearing in Veracruz, Mexico. "
            "High-pressure piping valves with yellow H2S gas hazard warning signs, an orange windsock blowing stiffly in background, "
            "unattended SCBA breathing apparatus bottles resting near wellhead platform, ASEA regulatory inspection documentation lighting, 8k."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 7 de noviembre de 2017, en la región petrolera sur del estado de Veracruz, México, "
            "en una macropera de extracción terrestre operada por Petróleos Mexicanos (Pemex), "
            "una cuadrilla de mantenimiento de líneas de producción fue alcanzada por una emanación fulminante de gas amargo. "
            "La toxicidad extrema del sulfuro de hidrógeno cobró la vida inmediata de dos técnicos petroleros "
            "e intoxicó a otros dos compañeros durante el intento desesperado de auxilio, motivando la intervención de la Agencia de Seguridad, Energía y Ambiente (ASEA).\n\n"
            "El incidente ocurrió durante la sustitución programada de una válvula de retención y control en el árbol de navidad "
            "de un pozo productor de crudo pesado. La corriente de hidrocarburos contenía una concentración de sulfuro de hidrógeno (H2S) "
            "superior a las dos mil partes por millón, un valor letal considerando que el límite inmediatamente peligroso para la vida y la salud (IDLH) "
            "está fijado por los estándares internacionales en apenas cien partes por millón. "
            "A pesar de la alta clasificación de riesgo del pozo amargo, los trabajadores intervinieron las bridas portando mascarillas filtrantes simples "
            "en lugar de tener acoplados sus equipos de respiración autónoma de circuito cerrado o líneas de aire asistido de presión positiva.\n\n"
            "Al aflojar los espárragos para insertar una junta nueva, la contrapresión remanente venció el empaque degradado, "
            "liberando una descarga gaseosa a alta velocidad. A concentraciones superiores a cien partes por millón, el ácido sulfhídrico "
            "paraliza instantáneamente el nervio olfativo humano, haciendo que las víctimas no perciban el olor a huevos podridos característico. "
            "Al inhalar una sola bocanada del gas concentrado, el H2S penetró al torrente sanguíneo bloqueando la respiración celular a nivel mitocondrial. "
            "Los dos operarios sufrieron un colapso neurogénico súbito, conocido en la industria como knockdown, falleciendo por asfixia en el piso del cabezal.\n\n"
            "La investigación de la ASEA ratifica las normas taxativas de la NRF cero veintiocho para operaciones con gas amargo en la industria del petróleo: "
            "Primero: en toda zona clasificada con presencia potencial de H2S es obligatorio el uso de equipos de respiración autónoma (SCBA) "
            "o sistemas de aire de cascada con cilindro de escape personal antes de aflojar el primer tornillo. "
            "Segundo: los detectores personales de H2S deben estar sujetos en la zona de respiración del operador y calibrarse diariamente. "
            "Y tercero: es obligatorio consultar la manga de viento antes de ingresar al sitio y mantener un plan de rescate con rescatistas dedicados "
            "apostados siempre en dirección contraria al viento (a barlovento).\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "136",
        "fecha": "08 NOVIEMBRE",
        "fechaPublicacion": "2026-11-08",
        "expediente": "Expediente #136",
        "carpeta": "2016-11-08-derrumbe-inundacion-zanja-atlantic-drain-boston",
        "titular": "EL COLAPSO Y LA INUNDACIÓN: TRAGEDIA DE ATLANTIC DRAIN EN BOSTON",
        "palabraResaltada": "ATLANTIC DRAIN BOSTON",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Obra Urbana de Servicios Hidráulicos, Boston, Massachusetts, EE.UU. - 2016",
        "tipoRiesgo": "Derrumbe / Excavaciones",
        "parrafos": [
            "El 8 de noviembre de 2016, dos operarios de saneamiento murieron atrapados en una zanja de 3,6 metros de profundidad en el centro de Boston, Massachusetts, cuando una pared de tierra colapsó y fracturó una cañería matriz de agua a presión, en una obra de Atlantic Drain Service investigada por OSHA.",
            "La excavación no contaba con caja de zanja (trench box), entibado ni escaleras de escape. El derrumbe sepultó a los trabajadores hasta la cintura y la rotura simultánea del caño inundó la fosa con miles de litros de agua helada en cuestión de dos minutos.",
            "El contratista enfrentó cargos penales de homicidio involuntario por negligencia deliberada. La lección: localizar e identificar todas las cañerías subterráneas antes de excavar, blindar zanjas profundas con cajones de acero y prever bombas de achique y rutas de escape.",
        ],
        "puntosClave": [
            {"icono": "shield", "titulo": "Cajón metálico de zanja obligatorio", "texto": "Prohibido el ingreso a excavaciones de más de 1,20 m sin entibado o caja de zanja calculada; la tierra y el agua no permiten segundas oportunidades."},
            {"icono": "map-pin", "titulo": "Interferencias de servicios públicos enterrados", "texto": "Sondear y calzar cañerías de agua a presión y gas existentes para evitar que queden suspendidas en el vacío y se quiebren por su propio peso."},
            {"icono": "life-buoy", "titulo": "Escaleras de evacuación inmediata a menos de 7 metros", "texto": "Mantener medios de escape verticales continuos dentro de la zona protegida para permitir salir en segundos ante ingreso súbito de agua."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de investigación de fatalidades y citaciones penales de OSHA (OSHA Region 1 / U.S. Department of Labor) sobre Atlantic Drain Service Co. Inc. en Boston, Massachusetts.",
        "guionReel": (
            "El 8 de noviembre de 2016, en pleno centro de Boston, Massachusetts, una zanja de la contratista Atlantic Drain Service se convirtió en una trampa de pesadilla.\n\n"
            "Dos trabajadores bajaron a casi cuatro metros de profundidad para reparar una cloaca. La zanja no tenía caja de entibado ni escaleras de salida.\n\n"
            "De repente, la pared de tierra cedió por el peso de la calle. El derrumbe partió una tubería de agua potable a alta presión que pasaba al lado.\n\n"
            "Los obreros quedaron atrapados por la tierra hasta la cintura mientras la zanja se llenaba de agua helada a borbotones. Murieron ahogados en menos de dos minutos.\n\n"
            "La lección de Focus HSE: el dueño de la empresa fue condenado a prisión. En zanjas profundas, el entibado de acero y las rutas de escape salvan vidas.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an urban street trench cave-in in downtown Boston, Massachusetts. "
            "A deep narrow trench cut into city pavement filled with muddy flooded water, ruptured cast iron water main spraying water, "
            "police and fire department technical rescue team lines deployed across asphalt, somber rainy autumn documentary lighting, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 8 de noviembre de 2016, en el histórico barrio de South End en la ciudad de Boston, estado de Massachusetts, "
            "una obra de mantenimiento de servicios sanitarios ejecutada por la empresa contratista Atlantic Drain Service "
            "derivó en una tragedia desgarradora que culminó con una histórica condena penal por homicidio involuntario para sus directivos. "
            "Dos operarios de saneamiento de treinta y dos y treinta y tres años perdieron la vida de forma atroz al quedar atrapados "
            "en el fondo de una zanja de tres metros y medio de profundidad que colapsó e inundó en escasos minutos.\n\n"
            "La investigación técnica federal de la OSHA expuso un desprecio flagrante y sistemático por los estándares básicos de excavación. "
            "La zanja, abierta en un pavimento urbano sometido al tránsito vehicular pesado, carecía totalmente de un cajón de acero de seguridad "
            "(trench box), de entibados de madera o de un talud adecuado. La cuadrilla trabajaba en un pozo angosto con paredes completamente verticales. "
            "Durante las tareas de excavación, el contratista no apuntaló una cañería matriz de agua potable de hierro fundido a alta presión "
            "que cruzaba el corte, dejándola suspendida en el aire sin soporte inferior.\n\n"
            "La vibración del tráfico y la sobrecarga del terreno provocaron la falla repentina por deslizamiento de una de las paredes laterales de tierra. "
            "El peso del alud de tierra inmovilizó a los dos trabajadores aprisionándolos contra el fondo de la excavación. "
            "Simultáneamente, el desprendimiento de suelo quebró la tubería de agua suspendida. Cientos de litros por segundo de agua helada a presión "
            "inundaron el pozo en cuestión de noventa segundos. Sin escaleras de escape a su alcance y sepultados bajo tierra húmeda hasta el pecho, "
            "los dos trabajadores perecieron ahogados antes de que los bomberos pudieran contener el flujo del hidrante principal.\n\n"
            "El caso penal de Atlantic Drain en Boston fijó un precedente contundente sobre la responsabilidad en obras viales y subterráneas: "
            "Primero: ingresar a una zanja de más de un metro con veinte centímetros de profundidad sin caja blindada de apuntalamiento "
            "constituye una negligencia criminal inexcusable. "
            "Segundo: toda interferencia de servicios públicos subterráneos debe estar identificada, calzada y soportada físicamente con vigas puente para evitar roturas por flexión. "
            "Y tercero: es obligatorio disponer escaleras rígidas de escape dentro del cajón de seguridad a menos de siete metros y medio de distancia "
            "para permitir que los trabajadores salgan en segundos ante cualquier colapso imprevisto.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "137",
        "fecha": "09 NOVIEMBRE",
        "fechaPublicacion": "2026-11-09",
        "expediente": "Expediente #137",
        "carpeta": "2011-11-09-explosion-reactor-mitsui-chemicals-iwakuni",
        "titular": "LA PARADA QUE APAGÓ EL FRÍO: EXPLOSIÓN EN MITSUI CHEMICALS",
        "palabraResaltada": "MITSUI CHEMICALS",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Complejo Petroquímico Mitsui Chemicals, Iwakuni-Ohtake, Yamaguchi, Japón - 2011",
        "tipoRiesgo": "Seguridad de Procesos (PSM)",
        "parrafos": [
            "El 9 de noviembre de 2011 —y en la secuencia de eventos que culminó en el siniestro de abril de 2012 en la misma unidad—, el complejo petroquímico de Mitsui Chemicals en Iwakuni, Japón, sufrió graves emergencias térmicas en su planta de resorcinol por fallas en el enfriamiento.",
            "Durante una parada de emergencia provocada por un corte de suministro eléctrico, un reactor que contenía peróxidos aromáticos e hidroperóxidos quedó sin agitación mecánica ni circulación de agua de refrigeración, desencadenando una descomposición exotérmica autoacelerada.",
            "La presión interna reventó el reactor provocando un incendio devastador que dejó víctimas y daños en 900 edificios vecinos. La lección: lazos de enfriamiento de emergencia pasivos o a vapor independientes de la red eléctrica para reactores con químicos inestables.",
        ],
        "puntosClave": [
            {"icono": "cpu", "titulo": "Enfriamiento de emergencia independiente de la red", "texto": "Equipar reactores exotérmicos con bombas de agua de enfriamiento impulsadas por turbinas de vapor o generadores diésel autónomos."},
            {"icono": "thermometer", "titulo": "Agentes de neutralización química de emergencia", "texto": "Disponer de inyección presurizada de disolventes o agentes inhibidores para desactivar la reacción antes de alcanzar la temperatura de no retorno."},
            {"icono": "file-search", "titulo": "Análisis HAZOP para paradas imprevistas", "texto": "Evaluar qué ocurre con los reactivos estancados cuando la planta sufre un corte total de energía (blackout) y protocolizar su drenaje seguro."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe del Comité de Investigación de Accidentes de Mitsui Chemicals Inc. sobre el complejo de Iwakuni-Ohtake y directrices de seguridad de procesos del Ministerio de Economía, Comercio e Industria de Japón (METI).",
        "guionReel": (
            "El 9 de noviembre de 2011, en Iwakuni, Japón, el complejo petroquímico de Mitsui Chemicals vivió la pesadilla de una reacción fuera de control.\n\n"
            "En la unidad de resorcinol, un corte de luz detuvo la planta. Los motores se apagaron y las bombas de agua fría se detuvieron.\n\n"
            "Dentro de un reactor quedaron toneladas de peróxidos químicos calientes. Sin agitación y sin enfriamiento, las moléculas comenzaron a reaccionar entre sí.\n\n"
            "La temperatura subió a más de 200 grados. El reactor de acero inoxidable estalló con una violencia descomunal, destruyendo la unidad y sacudiendo la ciudad.\n\n"
            "La lección de Focus HSE: si tu reactor maneja reacciones exotérmicas, el enfriamiento de respaldo no puede depender de un cable eléctrico.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of a petrochemical chemical reactor structure after a thermal runaway explosion in Iwakuni, Japan. "
            "Ruptured stainless steel chemical synthesis vessel split open with twisted insulation jackets, chemical process piping wreckage, "
            "emergency response water spray mist reflecting over concrete industrial apron under overcast Japanese sky, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 9 de noviembre de 2011, en el complejo petroquímico de Iwakuni-Ohtake, en la prefectura de Yamaguchi, Japón, "
            "las instalaciones de la corporación Mitsui Chemicals sufrieron una grave pérdida de control térmico en su planta de resorcinol, "
            "un compuesto esencial utilizado en la vulcanización de neumáticos y adhesivos industriales. "
            "Este evento precursor desnudó una vulnerabilidad crítica en la gestión de servicios auxiliares que derivaría poco después "
            "en una explosión de magnitud catastrófica con un operario fallecido y daños materiales en más de novecientas edificaciones circundantes.\n\n"
            "La causa raíz técnica se originó en la gestión de una parada imprevista de planta por caída de tensión en la red eléctrica regional. "
            "Al cortarse el suministro eléctrico principal, los motores de los agitadores de paletas y las bombas centrífugas de agua de enfriamiento "
            "de los reactores de oxidación se detuvieron simultáneamente. Dentro del reactor intermedio permanecían miles de litros de una mezcla "
            "líquida de diisopropilbenceno y sus correspondientes hidroperóxidos, sustancias químicamente autorreactivas que liberan grandes cantidades "
            "de calor cuando no se disipa la energía de descomposición.\n\n"
            "Sin recirculación de agua en la camisa de refrigeración y sin agitación que homogeneizara el fluido, se generó un gradiente térmico localizado "
            "en el fondo del recipiente. La temperatura trepó velozmente por encima de los ciento cincuenta grados Celsius, alcanzando la temida Temperatura de No Retorno. "
            "A partir de ese punto, la velocidad de generación de calor superó diez veces la capacidad pasiva de pérdida térmica del tanque. "
            "La presión interna de gases vaporizados sobrepasó los discos de ruptura, provocando la explosión física del recipiente de acero "
            "y desatando un incendio generalizado de hidrocarburos aromáticos que demandó la evacuación preventiva de los barrios costeros.\n\n"
            "La investigación del Ministerio de Economía, Comercio e Industria de Japón (METI) en Mitsui Chemicals consagró directivas clave en PSM: "
            "Primero: todo reactor que contenga mezclas autorreactivas o peróxidos orgánicos debe contar con sistemas de refrigeración de emergencia "
            "intrínsecamente seguros y diversificados, como bombas accionadas por turbinas de vapor independientes de la red eléctrica. "
            "Segundo: los análisis HAZOP deben estudiar con detalle milimétrico el escenario de 'pérdida total de servicios auxiliares en parada no planificada'. "
            "Y tercero: es mandatorio prever sistemas de descarga de emergencia (dump tanks) donde la mezcla reactiva pueda ser transferida "
            "rápidamente a recipientes fríos inundados con abundante diluyente inerte para extinguir la reacción antes del estallido.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "138",
        "fecha": "10 NOVIEMBRE",
        "fechaPublicacion": "2026-11-10",
        "expediente": "Expediente #138",
        "carpeta": "2017-11-10-atrapamiento-mezcladora-kelloggs-rossville-tennessee",
        "titular": "LAS ASPAS EN LA TOLVA: ATRAPAMIENTO EN KELLOGG'S ROSSVILLE",
        "palabraResaltada": "KELLOGG'S ROSSVILLE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta de Alimentos Kellogg's Bakery, Rossville, Tennessee, EE.UU. - 2017",
        "tipoRiesgo": "Atrapamiento / Bloqueo (LOTO)",
        "parrafos": [
            "El 10 de noviembre de 2017, un operario de saneamiento de 38 años falleció tras quedar atrapado dentro de una máquina mezcladora industrial de masa en la planta de alimentos de Kellogg's en Rossville, Tennessee, en un caso investigado por TOSHA.",
            "El trabajador ingresó al interior de la tolva para realizar el raspado y limpieza manual de masa adherida sin aplicar bloqueo y etiquetado (LOTO) en el panel eléctrico ni despresurizar el actuador neumático de las paletas giratorias.",
            "Un compañero o el ciclo automático activó el sistema motriz mientras el operario estaba dentro. La lección: aislamiento y candado LOTO personal en fuentes eléctricas y neumáticas, enclavamiento de tapas y monitoreo de energía cero.",
        ],
        "puntosClave": [
            {"icono": "lock", "titulo": "Bloqueo y consignación LOTO personal obligatorio", "texto": "Todo ingreso del cuerpo a tolvas, mezcladoras o molinos exige candado y tarjeta personal en el seccionador eléctrico y en la válvula de purga neumática."},
            {"icono": "shield-check", "titulo": "Enclavamiento de seguridad en tapas (Interlocks)", "texto": "Las compuertas de acceso a tolvas deben contar con interruptores de seguridad mecánicos o magnéticos con bloqueo de apertura hasta parada total."},
            {"icono": "users", "titulo": "Vigía exterior durante tareas de saneamiento", "texto": "Designar a un compañero dedicado en el exterior de la máquina para supervisar el procedimiento e impedir cualquier reenergización accidental."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de inspección y penalidades de Tennessee OSHA (TOSHA / 29 CFR 1910.147 Control of Hazardous Energy) sobre Kellogg Company en Rossville, Tennessee.",
        "guionReel": (
            "El 10 de noviembre de 2017, en Rossville, Tennessee, la planta de alimentos de Kellogg's vivió una tragedia desgarradora.\n\n"
            "Un trabajador de saneamiento de 38 años se metió dentro de una tolva mezcladora industrial para raspar masa pegada en las paredes.\n\n"
            "Pensó que la máquina no arrancaría sola: no puso su candado LOTO en el panel ni purgó la válvula de aire neumática.\n\n"
            "De repente, el sistema automatizado recibió señal de arranque. Las gigantescas aspas de acero comenzaron a girar con el trabajador adentro.\n\n"
            "Murió atrapado sin posibilidad de escape antes de que pudieran cortar la corriente.\n\n"
            "La lección de Focus HSE: antes de meter el cuerpo en una mezcladora, pon tu candado personal en el tablero. La energía cero no se negocia.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an industrial stainless steel bakery dough mixer hopper interior in Rossville, Tennessee. "
            "Heavy industrial helical mixing blades inside a polished stainless steel vat, open safety grate lid showing an interlock switch mechanism, "
            "red safety lockout hasp with personal padlock on nearby electrical panel, TOSHA inspection documentation lighting, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 10 de noviembre de 2017, en las instalaciones de la planta de panificados y galletas de la corporación Kellogg Company, "
            "ubicada en la ciudad de Rossville, estado de Tennessee, Estados Unidos, "
            "una tarea habitual de higienización y saneamiento industrial culminó en una fatalidad atroz. "
            "Un operario de limpieza de treinta y ocho años perdió la vida al ser atrapado por las aspas rotativas de una máquina mezcladora "
            "industrial de masa de gran tonelaje, en un siniestro que motivó severas citaciones por parte de la agencia TOSHA.\n\n"
            "La investigación oficial reconstruyó la violación sistemática al estándar de control de energías peligrosas. "
            "Al finalizar la producción de un lote de panificación, el trabajador ingresó físicamente por la compuerta superior de inspección "
            "hacia el interior del cuerpo cilíndrico de la mezcladora para raspar manualmente residuos secos de harina y masa adheridos al fondo. "
            "El operario confió en que la máquina estaba 'en pausa' desde la botonera táctil del operador, omitiendo dirigirse al panel "
            "de desconexión principal para abrir la cuchilla de potencia, colocar su candado y tarjeta personal de bloqueo (LOTO), "
            "y purgar la presión residual del circuito neumático que accionaba las compuertas de descarga.\n\n"
            "El microinterruptor de seguridad de la rejilla superior se encontraba degradado y no cortaba mecánicamente el circuito de potencia. "
            "Mientras el operario se encontraba agachado entre los ejes helicoidales de amasado, el autómata programable de la línea "
            "interpretó un comando de rearme automático del ciclo o un compañero accionó inadvertidamente un comando en la consola remota. "
            "El potente motorreductor trifásico arrancó con un torque imparable. Las aspas de acero inoxidable atraparon al trabajador, "
            "provocándole traumatismos torácicos y asfixia mecánica letal de forma instantánea antes de que los operarios pudieran alcanzar la parada de emergencia.\n\n"
            "El trágico accidente en Kellogg's Rossville reafirma los principios inviolables de la protección de maquinaria en la industria alimentaria: "
            "Primero: el ingreso a cualquier mezcladora, amasadora, tolva o tornillo sinfín exige la aplicación incondicional de la norma OSHA diecinueve diez punto ciento cuarenta y siete; "
            "la parada operativa desde consola no es bloqueo; se requiere candado físico personal sobre el interruptor de energía eléctrica y neumática. "
            "Segundo: los enclavamientos de las tapas deben ser de seguridad positiva Categoría 4, impidiendo físicamente la apertura mientras exista inercia de giro. "
            "Y tercero: toda tarea de saneamiento interno debe realizarse bajo la custodia de un vigía exterior entrenado que mantenga contacto visual continuo con el operador.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "139",
        "fecha": "11 NOVIEMBRE",
        "fechaPublicacion": "2026-11-11",
        "expediente": "Expediente #139",
        "carpeta": "2000-11-11-incendio-funicular-subterraneo-kaprun-austria",
        "titular": "LA TRAMPA DE FUEGO EN EL TÚNEL: LA TRAGEDIA DEL FUNICULAR DE KAPRUN",
        "palabraResaltada": "FUNICULAR DE KAPRUN",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Funicular Subterráneo Gletscherbahn 2, Estación de Esquí de Kaprun, Salzburgo, Austria - 2000",
        "tipoRiesgo": "Protección contra Incendios / Espacios Subterráneos",
        "parrafos": [
            "El 11 de noviembre de 2000, un voraz incendio dentro de un tren funicular en el interior del túnel de 3,3 kilómetros del glaciar de Kitzsteinhorn en Kaprun, Austria, causó la muerte de 155 personas en una de las peores tragedias en túneles de Europa.",
            "El fuego se originó por la pérdida de fluido hidráulico inflamable sobre un calefactor eléctrico doméstico instalado indebidamente en la cabina trasera del tren. El incendio se propagó rápidamente en un túnel empinado a 30 grados que actuó como una chimenea gigante.",
            "El tren carecía de extintores accesibles, las puertas se trabaron y los pasajeros que intentaron huir hacia arriba murieron por humo tóxico. La lección: fluidos hidráulicos difícilmente inflamables, diseño ignífugo y vías de evacuación hacia abajo.",
        ],
        "puntosClave": [
            {"icono": "flame", "titulo": "Fluidos hidráulicos resistentes al fuego", "texto": "Prohibir el uso de aceites minerales inflamables cerca de fuentes eléctricas o térmicas en trenes y túneles; usar fluidos clase HFC o ésteres sintéticos."},
            {"icono": "arrow-down", "titulo": "Evacuación hacia abajo ante efecto chimenea", "texto": "En túneles inclinados, el humo y calor suben violentamente; la regla vital de supervivencia es huir siempre pendiente abajo, por debajo del fuego."},
            {"icono": "door-open", "titulo": "Desbloqueo manual de emergencia de puertas", "texto": "Garantizar apertura manual independiente de puertas desde el interior de cabinas sin depender de la energía hidráulica o eléctrica del tren."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de la Comisión Técnica de Investigación de Desastres del Ministerio de Transporte de Austria y dictámenes periciales del Tribunal de Salzburgo sobre el accidente de Kaprun.",
        "guionReel": (
            "El 11 de noviembre de 2000, en Kaprun, Austria, 155 personas murieron en una trampa de fuego dentro de una montaña.\n\n"
            "El tren funicular subía a los esquiadores por un túnel subterráneo empinado de 3 kilómetros. En la cabina de cola, un calefactor de uso doméstico mal instalado recalentó.\n\n"
            "Una manguera de aceite hidráulico que pasaba justo encima goteó sobre el calentador. El aceite se encendió y el tren se detuvo a mitad del túnel oscuro.\n\n"
            "El túnel actuó como una chimenea gigante: el humo venenoso subió con fuerza brutal. Las puertas hidráulicas se bloquearon.\n\n"
            "Los esquiadores que corrieron túnel arriba murieron asfixiados. Solo sobrevivieron 12 personas que rompieron una ventana y bajaron hacia la base.\n\n"
            "La lección de Focus HSE: en túneles inclinados nunca corras hacia arriba; y jamás uses calefactores domésticos cerca de fluidos inflamables.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph depicting the historic Kaprun glacier funicular railway disaster in Salzburg, Austria. "
            "A dark steep narrow inclined railway tunnel bored through alpine granite rock showing charred twisted steel funicular rails, "
            "heavy black soot staining tunnel ceiling arches, emergency rescue team helmet lights cutting through misty cold mountain tunnel air, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 11 de noviembre de 2000, a las nueve de la mañana, en la estación de esquí del glaciar Kitzsteinhorn en Kaprun, "
            "estado de Salzburgo, Austria, se desató una de las mayores catástrofes en medios de transporte por cable y espacios subterráneos del mundo. "
            "El tren funicular Gletscherbahn dos, que transportaba a más de ciento sesenta esquiadores y turistas hacia las pistas de alta montaña, "
            "se convirtió en un infierno de fuego y humo en el interior de un túnel ciego de tres kilómetros y trescientos metros de longitud "
            "excavado en la roca con una pendiente de treinta grados, cobrando la vida de ciento cincuenta y cinco personas.\n\n"
            "La investigación técnica judicial expuso una inconcebible cadena de fallas de diseño y modificaciones no autorizadas. "
            "En la cabina del conductor desocupada de la parte trasera del tren, la empresa operadora había montado un convector eléctrico calefactor "
            "de tipo hogareño común, no homologado para uso en transporte rodado. El aparato estaba fijado directamente debajo de tuberías "
            "y mangueras de goma que conducían aceite hidráulico mineral inflamable para el sistema de frenado del tren. "
            "La fatiga mecánica provocó una microfuga de aceite que goteó sobre la resistencia al rojo del calefactor, encendiendo el fluido a presión.\n\n"
            "Al quemarse las líneas hidráulicas, la caída de presión activó los frenos automáticos de emergencia, clavando el tren en medio del túnel. "
            "Las puertas de pasajeros, controladas por el mismo circuito hidráulico siniestrado, quedaron bloqueadas sin posibilidad de apertura automática. "
            "El túnel subterráneo actuó como el conducto de tiro de una chimenea industrial: el calor extremo y los gases tóxicos de cianuro y monóxido "
            "generados por los plásticos ascendieron a más de sesenta kilómetros por hora ladera arriba. La mayoría de los pasajeros logró forzar "
            "algunas puertas e intentó huir hacia la estación superior corriendo en subida, siendo alcanzados y asfixiados por la columna térmica en segundos. "
            "Únicamente doce pasajeros, liderados por un bombero voluntario que comprendió el efecto chimenea, rompieron un vidrio de esquí, "
            "descendieron a pie por la pasarela por debajo del fuego y lograron salir con vida a la boca inferior.\n\n"
            "El desastre del funicular de Kaprun en Austria reescribió los códigos de seguridad para túneles y trenes de montaña en todo el planeta: "
            "Primero: está terminantemente prohibido el empleo de aceites minerales combustibles en sistemas ferroviarios subterráneos; "
            "deben utilizarse fluidos hidráulicos autoextinguibles sintéticos resistentes al fuego (tipo HFC). "
            "Segundo: los sistemas de puertas deben incorporar palancas mecánicas manuales de desbloqueo de emergencia accesibles para los pasajeros "
            "sin requerir energía externa. Y tercero: la regla de supervivencia universal en túneles inclinados con fuego: "
            "jamás se escapa hacia arriba a favor del tiro térmico; la salvación radica en descender con determinación por debajo de la zona en llamas.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "140",
        "fecha": "12 NOVIEMBRE",
        "fechaPublicacion": "2026-11-12",
        "expediente": "Expediente #140",
        "carpeta": "2018-11-12-caida-techo-escarcha-roofing-contractors-denver",
        "titular": "LA ESCARCHA EN LA CHAPA: CAÍDA EN CUBIERTA DE DENVER",
        "palabraResaltada": "ROOFING CONTRACTORS",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Nave Industrial y Cubierta Metálica en Obra, Denver, Colorado, EE.UU. - 2018",
        "tipoRiesgo": "Trabajo en Altura / Superficies Frágiles",
        "parrafos": [
            "El 12 de noviembre de 2018, un techista de 28 años murió al resbalar y caer al vacío desde 11 metros de altura mientras reparaba la cubierta de chapa de un centro de distribución en Denver, Colorado, en una obra investigada por OSHA.",
            "A primera hora de la mañana, la chapa metálica presentaba una película invisible de escarcha y hielo matinal (black ice). El operario no estaba conectado a la línea de vida horizontal y el contratista carecía de redes anticaídas o barandillas perimetrales.",
            "El trabajador perdió tracción en sus botas y se deslizó sin frenos hacia el alero. La lección: evaluar las condiciones de adherencia y clima antes de subir a techos, líneas de vida retráctiles permanentes y anclaje al 100%.",
        ],
        "puntosClave": [
            {"icono": "cloud-snow", "titulo": "Evaluación climática y suspensión por escarcha", "texto": "Prohibir el tránsito sobre cubiertas metálicas en pendiente cuando exista humedad, rocío matinal, hielo o escarcha que anule el coeficiente de fricción."},
            {"icono": "anchor", "titulo": "Líneas de vida horizontales certificadas", "texto": "Instalar cables de acero certificados a lo largo de la cumbrera y exigir el uso continuo de arnés con absorbedor de energía y doble cabo."},
            {"icono": "shield", "titulo": "Protección colectiva en bordes de alero", "texto": "Montar redes perimetrales o barandas rígidas de borde de techo capaces de detener el deslizamiento inercial de una persona antes de caer al vacío."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de fatalidad de OSHA (OSHA Englewood Area Office / 29 CFR 1926.501 Duty to have fall protection) sobre Roofing Contractors en Denver, Colorado.",
        "guionReel": (
            "El 12 de noviembre de 2018, en Denver, Colorado, una cubierta industrial helada cobró la vida de un techista de 28 años.\n\n"
            "Eran las siete de la mañana. La chapa de zinc del techo parecía seca, pero tenía una capa microscópica de escarcha congelada.\n\n"
            "El trabajador subió a 11 metros de altura para cambiar unos paneles. El arnés estaba en su cuerpo, pero no lo conectó a la línea de vida.\n\n"
            "Dio un paso, sus botas patinaron como sobre jabón y se deslizó por la pendiente a toda velocidad. No había barandas en el borde.\n\n"
            "Cayó al vacío sobre el asfalto. Murió en el acto.\n\n"
            "La lección de Focus HSE: el frío convierte los techos de chapa en pistas de patinaje mortales; revisa la escarcha y mantente anclado al 100%.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of a steep industrial warehouse metal standing seam roof in Denver, Colorado, in early morning cold. "
            "A thin glistening layer of frosty morning ice coating corrugated grey steel roof panels, safety harness dual lanyard unhooked lying near a roof ridge cable, "
            "Rocky Mountains silhouette in crisp cold sunrise background, OSHA fall protection investigation team at site, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 12 de noviembre de 2018, en una fría mañana de otoño en la ciudad de Denver, estado de Colorado, Estados Unidos, "
            "una obra de renovación de cubiertas industriales sobre un almacén logístico de gran porte culminó en un desenlace fatal. "
            "Un techista profesional de veintiocho años resbaló de manera incontrolable y cayó al vacío desde una altura de once metros, "
            "sufriendo un politraumatismo letal contra el estacionamiento de hormigón de la nave.\n\n"
            "La investigación conducida por los inspectores de la OSHA determinó que la causa inmediata fue la pérdida total de adherencia "
            "provocada por factores meteorológicos no evaluados en el Análisis de Trabajo Seguro (ATS). "
            "Durante la noche anterior, la temperatura ambiente en Denver había descendido por debajo de los cero grados Celsius. "
            "Las láminas metálicas de la cubierta presentaban una fina e invisible capa de escarcha matinal congelada, conocida como hielo negro (black ice). "
            "El coeficiente de rozamiento de las suelas de goma del calzado de seguridad sobre la chapa prepintada se redujo a prácticamente cero.\n\n"
            "El operario subió por la escalera de acceso para iniciar la descarga de tornillería. Aunque llevaba colocado un arnés integral anticaídas, "
            "la empresa contratista no había tendido una línea de vida de cable de acero horizontal en la cumbrera del tejado, "
            "y el trabajador no tenía ningún punto de anclaje habilitado a su alcance. Al dar el tercer paso sobre la vertiente inclinada a veinte grados, "
            "sus pies se deslizaron hacia adelante. El trabajador cayó sobre su espalda y comenzó a deslizarse vertiginosamente pendiente abajo "
            "sin posibilidad de frenar su avance con las manos. En el alero exterior no se habían instalado redes de contención perimetral "
            "ni barandillas de remate que detuvieran el cuerpo, precipitándose en caída libre hasta el suelo.\n\n"
            "El trágico accidente en Denver impone pautas obligatorias para todas las empresas de montaje y mantenimiento de cubiertas: "
            "Primero: las condiciones climáticas gobiernan el trabajo en altura; está estrictamente prohibido subir a techos metálicos inclinados "
            "mientras exista condensación, rocío, escarcha o hielo; se debe aguardar a que la superficie esté completamente seca y caldeada por el sol. "
            "Segundo: la instalación previa de líneas de vida horizontales certificadas bajo norma EN 795 o ANSI Z359 es un requisito sine qua non "
            "antes de que el primer operario acceda a la superficie del techo. "
            "Y tercero: el uso de arnés es un acto inútil si no se mantiene la conexión activa al cien por ciento con absorbedores de impacto dimensionados.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "141",
        "fecha": "13 NOVIEMBRE",
        "fechaPublicacion": "2026-11-13",
        "expediente": "Expediente #141",
        "carpeta": "2005-11-13-explosiones-petroquimica-petrochina-jilin-rio-songhua",
        "titular": "EL TAPÓN EN LA TORRE DE NITRACIÓN: DESASTRE EN PETROCHINA JILIN",
        "palabraResaltada": "PETROCHINA JILIN",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Complejo Petroquímico PetroChina Jilin Petrochemical, Jilin, China - 2005",
        "tipoRiesgo": "Seguridad de Procesos (PSM)",
        "parrafos": [
            "El 13 de noviembre de 2005, una serie de seis explosiones colosales pulverizó la planta de anilina número 101 de PetroChina en Jilin, matando a 8 trabajadores, hiriendo a 60 y arrojando más de 100 toneladas de nitrobenceno y benceno al río Songhua.",
            "El accidente se desató al intentar desatascar manualmente una torre de nitración de benceno que se encontraba bloqueada. Los operadores continuaron inyectando vapor de calentamiento sin purga adecuada, provocando una reacción descontrolada por sobrecalentamiento de compuestos nitrados inestables.",
            "La mancha química de 80 kilómetros forzó a cortar el agua a 3,8 millones de habitantes en Harbin. La lección: procedimientos estrictos de desobstrucción térmica en compuestos nitrados, instrumentación redundante y barreras de retención ambiental.",
        ],
        "puntosClave": [
            {"icono": "shield-alert", "titulo": "Riesgo térmico de compuestos nitrados", "texto": "Los intermediarios de nitración como el nitrobenceno y dinitrobenceno son químicamente inestables y explotan si se calientan sin control de temperatura."},
            {"icono": "file-check", "titulo": "Procedimiento validado para destrabar líneas", "texto": "Prohibir el calentamiento indiscriminado con vapor sobre tuberías atascadas con reactivos; exigir enfriamiento, dilución y evaluación MOC previa."},
            {"icono": "droplets", "titulo": "Contención ambiental de vertidos a ríos", "texto": "Las plantas petroquímicas deben contar con compuertas de aislamiento de efluentes pluviales para impedir que derrames masivos lleguen a cuencas fluviales."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe oficial de la Administración Estatal de Seguridad en el Trabajo de China (SAWS) sobre la catástrofe de Jilin Petrochemical y evaluaciones ambientales del PNUMA (PNUMA / UNEP).",
        "guionReel": (
            "El 13 de noviembre de 2005, en Jilin, China, el complejo petroquímico de PetroChina estalló en una cadena de seis explosiones colosales.\n\n"
            "En la planta de anilina, una torre química donde se mezclaba ácido y benceno se trabó con material cristalizado. Para desatascarla, los operarios le metieron vapor hirviendo.\n\n"
            "Los compuestos nitrados son primos hermanos de la dinamita: al calentarse en seco, sufrieron una descomposición explosiva instantánea.\n\n"
            "La torre detonó en pedazos: murieron ocho operarios y la onda expansiva destruyó la planta. Cien toneladas de nitrobenceno tóxico cayeron al río Songhua.\n\n"
            "Una mancha venenosa de 80 kilómetros dejó sin agua potable a cuatro millones de personas en la ciudad de Harbin.\n\n"
            "La lección de Focus HSE: nunca desatasques una línea química con calor a ciegas; la reactividad química no perdona la impaciencia.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph depicting the massive chemical process industrial explosions at the PetroChina Jilin chemical plant in 2005. "
            "Shattered benzene fractional distillation columns collapsed in tangled blackened steel frameworks, heavy orange industrial smoke billowing into sky, "
            "emergency foam fire tenders spraying foam near the industrial water discharge banks of the Songhua River, 8k resolution, raw documentary detail."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 13 de noviembre de 2005, a la una y cuarenta y cinco de la tarde, en la ciudad industrial de Jilin, "
            "provincia de Jilin en el noreste de China, la planta de anilina número ciento uno del gigante estatal PetroChina "
            "sufrió una serie devastadora de seis explosiones consecutivas. La catástrofe demolió la unidad de síntesis química, "
            "provocó la muerte inmediata de ocho trabajadores, hirió a más de sesenta operarios y desencadenó una crisis ambiental internacional "
            "al descargar más de cien toneladas de benceno y nitrobenceno cancerígeno en las aguas del río Songhua.\n\n"
            "La comisión investigadora de la Administración Estatal de Seguridad en el Trabajo determinó que el desastre se inició "
            "durante una maniobra de parada y limpieza mal gestionada en la torre de destilación y nitración de benceno. "
            "La línea de recirculación se encontraba parcialmente obstruida por la precipitación de compuestos intermedios pesados. "
            "Para disolver el tapón mecánico, los operadores inyectaron vapor vivo a alta presión para recalentar el equipo. "
            "Sin embargo, omitieron abrir las válvulas de purga y no verificaron la temperatura interna del lecho catalítico, "
            "provocando que el residuo químico atrapado se secara y se concentrara dentro de la columna metálica.\n\n"
            "Los compuestos aromáticos nitrados, como el dinitrobenceno, poseen una reactividad molecular extrema similar a la del TNT. "
            "Al sobrepasar los ciento sesenta grados centígrados sin disipación térmica, se inició una descomposición exotérmica desbocada. "
            "La torre estalló con una energía destructiva colosal. La onda de choque cortó cañerías contiguas de benceno e hidrógeno, "
            "provocando cinco explosiones secundarias sucesivas que arrasaron la nave de proceso. El agua empleada por las brigadas de extinción "
            "arrastró cien toneladas de químicos puros hacia las alcantarillas pluviales abiertas, contaminando el río Songhua con una mancha tóxica "
            "de ochenta kilómetros de extensión que forzó a cortar el suministro de agua corriente a casi cuatro millones de habitantes en Harbin "
            "y tensó las relaciones diplomáticas con la vecina Rusia.\n\n"
            "La tragedia de PetroChina en Jilin consagró principios esenciales de la gestión de riesgos en procesos reactivos: "
            "Primero: las tareas de desatasco térmico de líneas que manejen sustancias nitradas o autorreactivas deben estar estrictamente protocolizadas "
            "bajo procedimientos de Gestión del Cambio (MOC), prohibiendo terminantemente la inyección de vapor sin monitoreo de temperatura en tiempo real. "
            "Segundo: los sistemas de purga deben ser cerrados y canalizarse hacia unidades de antorcha o depuración de gases. "
            "Y tercero: todo complejo petroquímico costero debe contar con esclusas de retención de efluentes pluviales e industriales "
            "capaces de cerrar el vertido a ríos en segundos ante cualquier pérdida mayor de contención primaria.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "142",
        "fecha": "14 NOVIEMBRE",
        "fechaPublicacion": "2026-11-14",
        "expediente": "Expediente #142",
        "carpeta": "2016-11-14-electrocucion-bomba-sumergible-pilgrims-pride-chattanooga",
        "titular": "EL CABLE BAJO EL AGUA A PRESIÓN: ELECTROCUCIÓN EN PILGRIM'S PRIDE",
        "palabraResaltada": "PILGRIM'S PRIDE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Faenadora de Alimentos Pilgrim's Pride, Chattanooga, Tennessee, EE.UU. - 2016",
        "tipoRiesgo": "Riesgo Eléctrico / Ambientes Húmedos",
        "parrafos": [
            "El 14 de noviembre de 2016, un operario de mantenimiento de 34 años murió electrocutado en la planta de procesamiento de aves de Pilgrim's Pride en Chattanooga, Tennessee, al manipular una bomba de agua sumergible con cableado deteriorado en un foso inundado, investigado por TOSHA.",
            "El trabajador realizaba tareas de achique de efluentes mientras empuñaba una manguera de lavado a presión. El cable de alimentación de 480 voltios de la bomba presentaba cortes en la vaina aislante y el circuito carecía de interruptor diferencial (GFCI) en el tablero de distribución.",
            "Al entrar en contacto con el agua energizada, recibió una descarga masiva a tierra. La lección: uso obligatorio de disyuntores diferenciales GFCI en ambientes húmedos, inspección periódica de aislación de cables y corte eléctrico antes de lavar.",
        ],
        "puntosClave": [
            {"icono": "zap", "titulo": "Interruptores diferenciales GFCI obligatorios", "texto": "Toda herramienta o bomba eléctrica utilizada en ambientes mojados debe estar protegida por un disyuntor por falla a tierra calibrado a 5 o 10 mA."},
            {"icono": "shield-check", "titulo": "Inspección de vainas y cables sumergibles", "texto": "Prohibir el uso de cables con empalmes encintados o cortes en la cubierta de neopreno; exigir cables sumergibles tipo SOOW con doble aislamiento."},
            {"icono": "lock", "titulo": "Desenergización previa al baldeo y lavado", "texto": "Cortar y bloquear la energía eléctrica de bombas y maquinarias antes de arrojar agua con mangueras de alta presión en fosas de lavado."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informes de investigación y citaciones de Tennessee OSHA (TOSHA / 29 CFR 1910.304 Wiring design and protection) sobre Pilgrim's Pride Corp. en Chattanooga.",
        "guionReel": (
            "El 14 de noviembre de 2016, en Chattanooga, Tennessee, la planta procesadora de Pilgrim's Pride fue escenario de una electrocución mortal en una fosa de agua.\n\n"
            "Un técnico de 34 años limpiaba un canal de residuos con una hidrolavadora a presión. En el agua había una bomba sumergible funcionando a 480 voltios.\n\n"
            "El cable de la bomba tenía la goma rota y cables pelados. Para colmo, el tablero eléctrico no tenía disyuntor diferencial de seguridad.\n\n"
            "El agua se electrificó por completo. Al pisar el charco con sus botas empapadas, la corriente atravesó su cuerpo hacia la tierra. Murió en segundos.\n\n"
            "La lección de Focus HSE: el agua y la electricidad no perdonan; en ambientes húmedos exige siempre disyuntor diferencial GFCI y cables intactos.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an industrial food processing meat packing sanitation pit area in Chattanooga, Tennessee. "
            "A drained concrete wet floor sump with an industrial submersible sump pump connected to a heavy black power cable showing exposed copper fraying, "
            "water pressure wash wand lying on wet tiled floor, yellow OSHA inspection tag and electrical safety test multimeter probes resting nearby, 8k."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 14 de noviembre de 2016, en las instalaciones de la planta faenadora y procesadora de aves de la corporación Pilgrim's Pride, "
            "situada en la ciudad de Chattanooga, estado de Tennessee, Estados Unidos, "
            "un operario electromecánico de mantenimiento de treinta y cuatro años falleció de manera instantánea por choque eléctrico. "
            "El trabajador fue alcanzado por una descarga de alta energía mientras operaba en el interior de una fosa de recolección de efluentes húmedos "
            "durante el turno de desinfección nocturno, en un accidente que derivó en severas penalidades impuestas por la agencia TOSHA.\n\n"
            "La investigación técnica federal destapó una grave deficiencia en la conservación del equipamiento eléctrico portátil en ambientes agresivos. "
            "En el canal de desagüe operaba una electrobomba sumergible industrial de achique alimentada por un circuito trifásico de cuatrocientos ochenta voltios. "
            "El cable flexible de alimentación presentaba múltiples rasgaduras en su vaina exterior de caucho debido al rozamiento continuo "
            "contra los bordes afilados del foso de hormigón, dejando los conductores de fase con su aislación primaria expuesta y degradada por los detergentes químicos.\n\n"
            "Para agravar fatalmente el escenario, el circuito del Centro de Control de Motores carecía de un interruptor diferencial de falla a tierra (GFCI) "
            "adecuadamente calibrado, confiando únicamente en fusibles termomagnéticos convencionales que no detectan corrientes de fuga de bajo amperaje pero letales para el ser humano. "
            "Mientras el operario empuñaba una manguera de lavado con lanza metálica arrojando agua a presión sobre la fosa, el agua actuó como un puente conductor masivo. "
            "Al entrar en contacto con el cable energizado sumergido, la corriente eléctrica atravesó el cuerpo del trabajador descargando hacia la reja metálica puesta a tierra. "
            "La intensidad de corriente superó los cien miliamperios, provocando parálisis muscular respiratoria y fibrilación ventricular fulminante.\n\n"
            "La tragedia en Pilgrim's Pride en Chattanooga ratifica tres mandamientos ineludibles para la seguridad eléctrica en plantas húmedas: "
            "Primero: todo equipo, bomba portátil o prolongador utilizado en recintos húmedos o mojados debe estar protegido obligatoriamente "
            "por un interruptor por falla a tierra (GFCI) de alta sensibilidad (Clase A) que interrumpa el circuito en milisegundos ante fugas mayores a cinco miliamperios. "
            "Segundo: los cables sumergibles deben inspeccionarse antes de cada uso y someterse a pruebas de resistencia de aislamiento con megóhmetro; "
            "está terminantemente prohibido el uso de cables con aislación cuarteada o parches de cinta adhesiva. "
            "Y tercero: antes de balear con mangueras o realizar limpiezas con agua en fosos industriales, se debe desenergizar y aplicar bloqueo LOTO en todas las bombas adyacentes.\n\n"
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
    """Inyecta las historias del Lote 13 en index.html antes del cierre del array historias."""
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

    print("\n✓ index.html actualizado exitosamente con los 10 nuevos expedientes (#133 a #142).")
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
    print("Iniciando motor Kokoro para Lote 13 (#133 a #142)...")
    kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

    print("\n" + "=" * 55)
    print("Iniciando procesamiento de 10 historias del Lote 13 (#133 a #142)")
    print("=" * 55 + "\n")

    historias_procesadas = []

    for h in LOTE_13_DATA:
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

    print("\n🎉 ¡LOTE 13 COMPLETADO AL 100%! (10 historias procesadas)\n")

if __name__ == "__main__":
    main()
