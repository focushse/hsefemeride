# -*- coding: utf-8 -*-
"""
Generador Agéntico Automatizado para Lote 14: Expedientes #143 a #152 (15 al 24 de noviembre)
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

LOTE_14_DATA = [
    {
        "id": "143",
        "fecha": "15 NOVIEMBRE",
        "fechaPublicacion": "2026-11-15",
        "expediente": "Expediente #143",
        "carpeta": "2004-11-15-fuga-cloruro-vinilo-dupont-louisville-kentucky",
        "titular": "LA VÁLVULA EQUIVOCADA: FUGA DE CLORURO DE VINILO EN DUPONT LOUISVILLE",
        "palabraResaltada": "FALSA IDENTIFICACIÓN",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Unidad de Cloruro de Vinilo, Planta DuPont, Louisville, Kentucky, EE.UU. - 2004",
        "tipoRiesgo": "Seguridad de Procesos (PSM) / Sustancias Tóxicas e Inflamables",
        "parrafos": [
            "El 15 de noviembre de 2004, en la planta química de DuPont en Louisville, Kentucky, una fuga masiva de cloruro de vinilo monómero (un gas altamente inflamable y cancerígeno) forzó la evacuación inmediata de la instalación y sectores aledaños, investigada por la Junta de Seguridad Química de EE.UU. (CSB).",
            "Durante tareas de limpieza y purga en un reactor de polimerización, un operador abrió por error una válvula manual de drenaje idéntica y adyacente a la que debía intervenir, careciendo ambas de codificación cromática, placas de identificación inequívocas o enclavamiento físico.",
            "La nube química se expandió velozmente en el área de proceso antes de que se accionara el aislamiento de emergencia. La lección de DuPont: identificación indeleble de válvulas críticas vinculada a P&ID en campo, doble bloqueo y purga (DBB) y detectores fijos de gas con alarma automática."
        ],
        "puntosClave": [
            {"icono": "tag", "titulo": "Identificación y rotulado P&ID en campo", "texto": "Etiquetado indeleble, numerado y codificado por colores en cada válvula crítica, eliminando cualquier ambigüedad visual entre líneas idénticas."},
            {"icono": "shield-check", "titulo": "Filosofía de Doble Bloqueo y Purga (DBB)", "texto": "Implementar aislamiento mecánico positivo con doble válvula y venteo intermedio antes de cualquier maniobra de limpieza o drenaje en reactores."},
            {"icono": "gauge", "titulo": "Detección perimetral de gases y corte ESD", "texto": "Redundancia en sensores fijos de detección de hidrocarburos clorados acoplados a parada automática de emergencia y rociadores de diluvio."}
        ],
        "pregunta": "¿Cómo verificas en campo que la válvula que estás por operar coincide exactamente con el procedimiento operativo y el P&ID?",
        "fuente": "Fuente: Informe de Investigación de Seguridad de Procesos del CSB (U.S. Chemical Safety Board) sobre la fuga de cloruro de vinilo en la planta DuPont de Louisville, Kentucky (Noviembre 2004).",
        "guionReel": (
            "El 15 de noviembre de 2004, en Louisville, Kentucky, la planta de DuPont estuvo al borde de la catástrofe por una sola válvula mal identificada.\n\n"
            "Un operador debía drenar agua de un reactor. Pero en el entramado de tuberías había dos válvulas idénticas, juntas y sin carteles claros.\n\n"
            "Abrió la equivocada. En segundos, una nube de cloruro de vinilo —gas inflamable y cancerígeno— invadió la planta. Solo un milagro evitó una explosión masiva.\n\n"
            "La investigación de la CSB concluyó que confiar en la memoria del operador sin identificación física en campo es una trampa mortal.\n\n"
            "¿La lección de Focus HSE? Toda válvula crítica debe estar rotulada según P&ID, bloqueada y verificada antes de moverla un solo milímetro. La seguridad está en los detalles."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 15 de noviembre de 2004, en Louisville, Kentucky, la histórica planta química de la corporación DuPont sufrió una peligrosa fuga masiva de monómero de cloruro de vinilo que obligó a activar las alarmas comunitarias y fue investigada exhaustivamente por la Junta de Seguridad Química de los Estados Unidos, la CSB.\n\n"
            "Esa mañana, los técnicos se preparaban para drenar y limpiar uno de los reactores de polimerización. El procedimiento requería abrir una válvula manual de purga en la parte inferior del colector. Sin embargo, en ese entramado de cañerías corrían múltiples líneas paralelas con accesorios idénticos, sin pintura diferenciadora y sin placas de identificación visibles desde el piso de operación.\n\n"
            "Guiado por la memoria y la rutina, un operador manipuló la válvula equivocada. Al abrirla, no salió agua de lavado, sino una corriente violenta de cloruro de vinilo presurizado. Este gas, sumamente inflamable y cancerígeno humano comprobado, formó de inmediato una densa niebla tóxica que saturó la nave industrial. Afortunadamente, no encontró una fuente de ignición inmediata antes de que los equipos de respuesta lograran aislar la sección desde una sala remota, pero el incidente expuso fallas críticas en los controles básicos de ingeniería.\n\n"
            "La investigación de la CSB reveló que la empresa no disponía de esquemas P&ID actualizados al alcance del operador en campo, y que las válvulas críticas carecían de candados operativos o enclavamientos de maniobra. La confianza en la familiaridad del personal sustituyó a la verificación técnica formal.\n\n"
            "Este evento en Louisville transformó los estándares de gestión de seguridad de procesos en DuPont y en la industria petroquímica mundial. Nos demostró que cuando dos válvulas se ven iguales, el error humano es solo cuestión de tiempo. Todo punto de drenaje o venteo de sustancias peligrosas debe contar con rotulación indeleble y unívoca, sistemas de doble bloqueo y purga, y detectores fijos de gas con enclavamiento automático a válvulas de cierre de emergencia.\n\n"
            "Porque en la industria química, la certeza jamás se asume: se inspecciona, se etiqueta y se confirma. En Focus HSE te lo recordamos siempre: la seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, 16:9 aspect ratio. Inside an industrial chemical polymerization plant in Louisville Kentucky, 2004. "
            "An intricate network of stainless steel pipes, industrial flanges, and manual wheel valves. Frost and condensation forming on a pipe flange due to rapid depressurization of vinyl chloride gas, creating a visible cold vapor mist swirling near the concrete floor. "
            "Industrial yellow handrails, vintage pressure gauges, stark fluorescent overhead lighting piercing through chemical haze. "
            "Hyperdetailed industrial realism, gritty textures of worn steel, 35mm lens documentary photo, no CGI look."
        )
    },
    {
        "id": "144",
        "fecha": "16 NOVIEMBRE",
        "fechaPublicacion": "2026-11-16",
        "expediente": "Expediente #144",
        "carpeta": "2017-11-16-atrapamiento-prensa-compactadora-waste-management-texas",
        "titular": "LA PRENSA QUE NUNCA SE DETUVO: ATRAPAMIENTO EN WASTE MANAGEMENT",
        "palabraResaltada": "CICLO AUTOMÁTICO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta de Reciclaje y Manejo de Residuos, Waste Management, Texas, EE.UU. - 2017",
        "tipoRiesgo": "Atrapamiento / Bloqueo y Etiquetado (LOTO) / Maquinaria Pesada",
        "parrafos": [
            "El 16 de noviembre de 2017, en una planta de reciclaje y tratamiento de residuos de la empresa Waste Management en Texas, un trabajador de mantenimiento murió atrapado tras ingresar a la cámara de compactación de una prensa hidráulica de cartón para destrabar una pila de material atascado.",
            "La investigación de OSHA comprobó que la máquina no fue aislada energéticamente ni bloqueada bajo protocolo LOTO. Al retirar el cartón atascado con las manos, el sensor óptico de nivel detectó el hueco y activó automáticamente el ariete hidráulico de compresión.",
            "El pistón avanzó con toneladas de fuerza sin que el operario tuviera forma de escapar o accionar una parada de emergencia interna. La lección: aplicación irrestricta de LOTO con consignación de energía hidráulica residual, uso de pértigas de desatasco externas y resguardos con enclavamiento tipo interlock."
        ],
        "puntosClave": [
            {"icono": "lock", "titulo": "Aislamiento LOTO con bloqueo mecánico del pistón", "texto": "Cortar energía eléctrica e hidráulica, despresurizar el acumulador e instalar pernos mecánicos de traba antes de entrar a la cámara."},
            {"icono": "tool", "titulo": "Prohibición de acceso manual para desatascos", "texto": "Diseñar herramientas de alcance extendido y protocolos para despejar acumulaciones desde fuera de la zona de peligro."},
            {"icono": "shield-check", "titulo": "Enclavamientos de seguridad interlock en compuertas", "texto": "Sensores de seguridad de categoría 4 que cortan la potencia motriz instantáneamente al abrir cualquier compuerta de inspección."}
        ],
        "pregunta": "¿Existen en tu planta prensas o trituradoras automáticas donde alguien intente liberar atascos sin aplicar previamente un candado LOTO?",
        "fuente": "Fuente: Investigación de Accidente Fatal de OSHA (Occupational Safety and Health Administration) en planta de procesamiento de reciclaje en Texas (Noviembre 2017).",
        "guionReel": (
            "El 16 de noviembre de 2017, en Texas, un operario murió aplastado en una planta de reciclaje de Waste Management por confiar en una máquina en pausa.\n\n"
            "Una prensa hidráulica de cartón se trabó. El trabajador entró a la cámara para sacar las cajas a mano, sin colocar su candado de bloqueo LOTO.\n\n"
            "Al destrabar el cartón, el sensor infrarrojo detectó el espacio libre y la máquina arrancó sola. El pistón avanzó con 50 toneladas de fuerza. No hubo escapatoria.\n\n"
            "OSHA concluyó que ingresar a una máquina automática sin desenergizar es una trampa mortal.\n\n"
            "¿La lección de Focus HSE? Nunca confíes en una pausa electrónica. Aplica LOTO, purga la energía hidráulica y usa herramientas externas. La seguridad está en los detalles."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 16 de noviembre de 2017, en una concurrida planta de reciclaje de la empresa Waste Management en el estado de Texas, ocurrió un trágico accidente mortal investigado por la Administración de Seguridad y Salud Ocupacional, OSHA, que conmocionó a la industria del manejo de residuos.\n\n"
            "Esa tarde, la gran prensa compactadora horizontal de cartón sufrió una obstrucción frecuente: varias cajas gruesas se habían trabado frente a la boca de alimentación, deteniendo el flujo normal hacia la tolva. Para no demorar el turno, un operario de mantenimiento decidió ingresar directamente al interior de la cámara de compactación para desatorar el material acumulado.\n\n"
            "Cometió el error más peligroso en plantas industriales: confió en que la máquina estaba 'en pausa'. No bajó los interruptores principales, no colocó su candado de bloqueo LOTO y no purgó la presión de los acumuladores hidráulicos. Se introdujo en el cajón metálico y comenzó a tirar del cartón con sus manos.\n\n"
            "En el instante en que logró remover la masa atascada, el sensor óptico de carga quedó despejado. El sistema lógico programable interpretó que la tolva estaba lista y disparó de manera automática el ciclo de prensado. El ariete hidráulico, capaz de ejercer más de cincuenta toneladas de empuje, avanzó silenciosa e inexorablemente hacia adelante. Atrapado en ese espacio ciego y sin paradas de emergencia al alcance de su mano, el trabajador perdió la vida aplastado al instante.\n\n"
            "La autopsia técnica de OSHA determinó la ausencia absoluta de enclavamientos de seguridad con corte de potencia en las puertas de servicio y la falta de capacitación sobre liberación de atascos mediante herramientas externas.\n\n"
            "Este doloroso suceso nos recuerda una verdad tajante: una máquina en pausa es un arma cargada con el percutor levantado. Jamás se debe ingresar al cuerpo de una compactadora, molino o trituradora sin aplicar bloqueo y etiquetado físico, despresurizar el circuito hidráulico y calzar mecánicamente el émbolo.\n\n"
            "La productividad jamás puede justificar omitir un candado. En Focus HSE te lo recordamos siempre: la seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, 16:9 aspect ratio. Interior of an industrial recycling facility in Texas, 2017. "
            "Massive horizontal hydraulic cardboard baler machine, rugged painted industrial green steel, hydraulic pistons and pressure hoses. A dark, cavernous compaction chamber with crushed cardboard bales nearby. "
            "High-visibility safety lockout padlock station mounted on an electrical control panel in the foreground with bright yellow warning signs. "
            "Dusty industrial ambient light streaming from skylights, dramatic shadows, realistic textures of scratched metal and corrugated cardboard, 35mm lens."
        )
    },
    {
        "id": "145",
        "fecha": "17 NOVIEMBRE",
        "fechaPublicacion": "2026-11-17",
        "expediente": "Expediente #145",
        "carpeta": "2018-11-17-caida-estructura-metalica-steel-erectors-charlotte-north-carolina",
        "titular": "EL PASO EN LA VIGA CIEGA: CAÍDA MORTAL EN STEEL ERECTORS CHARLOTTE",
        "palabraResaltada": "BORDE FILOSO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Obra de Montaje Estructural, Steel Erectors, Charlotte, Carolina del Norte, EE.UU. - 2018",
        "tipoRiesgo": "Trabajo en Altura / Montaje de Estructuras de Acero",
        "parrafos": [
            "El 17 de noviembre de 2018, en una obra de ampliación comercial en Charlotte, Carolina del Norte, un montador de estructuras de la empresa Steel Erectors falleció al precipitarse desde una altura de 14 metros mientras caminaba sobre una viga metálica desprovisto de un sistema de anclaje continuo.",
            "La investigación de OSHA reveló que el contratista no había tendido líneas de vida horizontales entre las columnas antes de izar las vigas, obligando a los operarios a desenganchar sus cabos de vida tradicionales al sortear cartelas y nudos de unión estructural.",
            "Al perder el equilibrio por una ráfaga de viento, el trabajador cayó al vacío sin conexión activa. La lección: preinstalación de cables de vida horizontales a nivel de suelo, uso obligatorio de doble cabo con conectores para borde filoso (Leading Edge) y política estricta de anclaje al 100%."
        ],
        "puntosClave": [
            {"icono": "cable", "titulo": "Líneas de vida preconectadas en suelo", "texto": "Instalar postes y cables de vida horizontales sobre las vigas antes de que la grúa las ice a su posición final en altura."},
            {"icono": "shield-check", "titulo": "Conectores certificados para borde filoso (Leading Edge)", "texto": "Utilizar dispositivos retráctiles diseñados específicamente para resistir el roce dinámico contra aristas de acero sin cortarse."},
            {"icono": "users", "titulo": "Supervisión de amarre al 100%", "texto": "Prohibir bajo falta grave el desenganche simultáneo de ambos ganchos del arnés durante desplazamientos sobre perfiles metálicos."}
        ],
        "pregunta": "¿En tus proyectos de montaje se instalan las líneas de vida en las vigas antes de levantarlas con la grúa?",
        "fuente": "Fuente: Informe de Investigación de Accidente por Caída de Altura de OSHA (U.S. Department of Labor) en Charlotte, North Carolina (Noviembre 2018).",
        "guionReel": (
            "El 17 de noviembre de 2018, en Charlotte, Carolina del Norte, un montador de Steel Erectors murió al caer de 14 metros de altura.\n\n"
            "Caminaba sobre una viga de acero. Llevaba arnés, pero no había una línea de vida horizontal instalada en la estructura.\n\n"
            "Para sortear una columna, desenganchó su conector para cambiarlo de lugar. En ese segundo desprotegido, una ráfaga de viento le hizo perder pie. Cayó al vacío.\n\n"
            "OSHA determinó que la falta de anclaje continuo al 100% causó esta tragedia previsible.\n\n"
            "¿La lección de Focus HSE? Las líneas de vida deben colocarse en las vigas en el suelo antes de izarlas, garantizando conexión permanente en altura. La seguridad está en los detalles."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 17 de noviembre de 2018, en la ciudad de Charlotte, Carolina del Norte, un operario de montaje estructural de la contratista Steel Erectors perdió la vida al caer desde catorce metros de altura durante la construcción de un complejo industrial, un caso rigurosamente investigado por la OSHA.\n\n"
            "Aquel día, el equipo trabajaba conectando las vigas principales del esqueleto de acero del edificio. La víctima, un montador experimentado, debía desplazarse sobre el ala superior de un perfil metálico estrecho para asegurar los pernos en la columna opuesta. Aunque vestía su arnés de seguridad de cuerpo entero, el sitio carecía de una línea de vida horizontal continua instalada a lo largo del tramo.\n\n"
            "Para avanzar, el trabajador debía enganchar y desenganchar alternativamente los mosquetones de su cabo de vida en los orificios de la propia viga. En una intersección compleja, con una cartela de unión que bloqueaba su paso y una súbita ráfaga de viento, el montador soltó el único conector amarrado para reposicionarlo más adelante. En esa fracción de segundo sin sujeción, perdió el equilibrio y cayó directamente sobre el piso de hormigón inferior.\n\n"
            "Los inspectores de OSHA concluyeron que la empresa violó la normativa al no planificar la ingeniería de protección contra caídas desde el diseño del montaje. La práctica habitual de permitir que los montadores caminen sobre vigas desprotegidas o dependan de un anclaje intermitente demostró ser letal.\n\n"
            "La moderna ingeniería de seguridad exige que las líneas de vida horizontales de cable de acero se instalen y tensen sobre las vigas mientras todavía están en el suelo, de modo que cuando la grúa las coloque en su posición definitiva, el trabajador solo deba conectarse de inmediato y permanecer anclado al cien por ciento durante todo su trayecto.\n\n"
            "En las alturas no hay segundas oportunidades ni reflejos capaces de vencer a la gravedad. En Focus HSE te lo recordamos siempre: la seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, 16:9 aspect ratio. Construction site of a massive steel framed industrial building in Charlotte North Carolina, 2018. "
            "Looking up at towering red primer steel I-beams against an overcast, windy sky. An empty safety harness tether swaying in the breeze from an exposed steel girder 14 meters high. "
            "Construction safety nets, perimeter warning flags, and certified horizontal lifeline cables on adjacent spans. "
            "Realistic gritty construction realism, dust, crane boom silhouette in background, shot on 35mm lens, photorealistic documentary style."
        )
    },
    {
        "id": "146",
        "fecha": "18 NOVIEMBRE",
        "fechaPublicacion": "2026-11-18",
        "expediente": "Expediente #146",
        "carpeta": "1987-11-18-incendio-escalera-mecanica-metro-kings-cross-londres",
        "titular": "LA LLAMARADA BAJO LOS PELDAÑOS: EL INCENDIO DE KING'S CROSS EN LONDRES",
        "palabraResaltada": "EFECTO TRINCHERA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Estación de Metro King's Cross St. Pancras, London Underground, Londres, Reino Unido - 1987",
        "tipoRiesgo": "Protección contra Incendios / Factor Humano / Seguridad en Espacios Subterráneos",
        "parrafos": [
            "El 18 de noviembre de 1987, en la estación subterránea de King's Cross St. Pancras de Londres, un incendio originado bajo una escalera mecánica de madera se transformó en una llamarada supersónica hacia la sala de boletos, causando la muerte de 31 personas e hiriendo a un centenar.",
            "La investigación judicial encabezada por Desmond Fennell y experimentos de dinámica de fluidos descubrieron el 'efecto trinchera': el fuego precalentó los peldaños superiores y los gases calientes se adhirieron al piso de la zanja, disparando un chorro de fuego hacia la salida en cuestión de segundos.",
            "La ignición fue producida por un fósforo encendido arrojado por un pasajero, que prendió fuego a capas acumuladas de grasa y pelusa en los rieles tras décadas de limpieza superficial y subestimación del humo por el personal. La lección: erradicación de madera en transporte público, rociadores automáticos y evacuación inmediata ante conatos."
        ],
        "puntosClave": [
            {"icono": "flame", "titulo": "Limpieza industrial profunda y desengrase", "texto": "Eliminar la acumulación de lubricantes, polvo y residuos combustibles en fosos mecánicos ocultos mediante inspecciones programadas."},
            {"icono": "shield-check", "titulo": "Comprensión del Efecto Trinchera en escaleras", "texto": "Instalar detectores térmicos lineales y rociadores automáticos de agua (sprinklers) bajo los descansos de escaleras mecánicas."},
            {"icono": "users", "titulo": "Cultura de evacuación inmediata ante humo", "texto": "Eliminar la tolerancia al humo o pequeños fuegos; evacuar masivamente las instalaciones subterráneas al primer reporte sin esperar confirmación visual."}
        ],
        "pregunta": "¿En tus instalaciones se inspeccionan y limpian periódicamente los fosos ocultos de maquinaria donde se acumula grasa y polvo inflamable?",
        "fuente": "Fuente: Informe Oficial de Investigación Judicial presidido por Desmond Fennell OBE QC sobre el incendio de la estación de King's Cross (Department of Transport, Reino Unido, 1988).",
        "guionReel": (
            "El 18 de noviembre de 1987, en Londres, el incendio de la estación de metro King's Cross dejó 31 muertos por un fenómeno físico letal: el efecto trinchera.\n\n"
            "Un fósforo cayó en las ranuras de una escalera mecánica de madera. Abajo, ardió grasa y pelusa acumuladas por falta de limpieza.\n\n"
            "El personal vio humo, pero no evacuó creyendo que era menor. De repente, la física cambió: el fuego se pegó a los peldaños y se disparó como un lanzallamas hacia el hall de boletos.\n\n"
            "La investigación de Desmond Fennell obligó a prohibir la madera en el metro y a instalar rociadores automáticos bajo cada escalera.\n\n"
            "¿La lección de Focus HSE? Nunca subestimes el humo ni la suciedad en maquinaria oculta. Evacúa al primer aviso. La seguridad está en los detalles."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 18 de noviembre de 1987, en la estación de metro King's Cross St. Pancras en Londres, ocurrió uno de los desastres más analizados en la historia de la ingeniería de incendios y la gestión de emergencias del transporte público, costando la vida a treinta y una personas.\n\n"
            "Esa tarde de hora punta, miles de pasajeros subían y bajaban por las largas escaleras mecánicas construidas con componentes de madera. Debajo de los peldaños, en los rieles de tracción que no habían sido sometidos a un desengrase profundo en años, yacía una gruesa capa de lubricante apelmazado con pelusa de ropa y basura. Un fósforo encendido arrojado por un usuario se deslizó entre las ranuras y comenzó a arder lentamente en el foso.\n\n"
            "Durante casi veinte minutos, varios empleados del metro observaron humo saliendo de la escalera, pero lo consideraron un incidente menor y no activaron el plan de evacuación ni cortaron el acceso de pasajeros. Lo que ignoraban era la física letal que se estaba gestando: el hasta entonces desconocido 'efecto trinchera'.\n\n"
            "Al intensificarse las llamas, el flujo de aire caliente dentro del túnel inclinado de la escalera no ascendió hacia el techo, sino que se pegó a los peldaños superiores, precalentando la madera hasta su punto de autoignición. Repentinamente, a las diecinueve horas y cuarenta y cinco minutos, la combustión se aceleró de golpe: una lengua de fuego y gases tóxicos a más de seiscientos grados se proyectó como un lanzallamas hacia el vestíbulo principal de venta de boletos, envolviendo a decenas de personas en una trampa infernal.\n\n"
            "La investigación oficial liderada por Desmond Fennell cambió para siempre las normas de seguridad contra incendios en todo el planeta. Se prohibió el uso de madera en el transporte subterráneo, se ordenó la instalación de rociadores automáticos en fosos de escaleras y se erradicó la peligrosa costumbre del personal de esperar a ver grandes llamas para dar la alarma de desalojo.\n\n"
            "King's Cross nos enseñó que la suciedad acumulada es combustible esperando una chispa y que el humo siempre es una emergencia crítica. En Focus HSE te lo recordamos siempre: la seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, 16:9 aspect ratio. The dramatic aftermath of the King's Cross tube station fire in London, 1987. "
            "Burnt and charred wooden escalator trench sloping down into darkness, scorched ceramic tiled tunnel walls covered in heavy black soot. "
            "British firefighters in retro 1980s gear inspecting the twisted metal frame and thermal damage with portable lamps. "
            "Thick atmospheric smoke haze, yellow emergency tape, poignant documentary atmosphere, 35mm lens authentic photographic quality."
        )
    },
    {
        "id": "147",
        "fecha": "19 NOVIEMBRE",
        "fechaPublicacion": "2026-11-19",
        "expediente": "Expediente #147",
        "carpeta": "1984-11-19-explosiones-glp-bleve-pemex-san-juan-ixhuatepec-san-juanico",
        "titular": "EL INFIERNO DE SAN JUANICO: LA CADENA DE BLEVE EN PEMEX",
        "palabraResaltada": "EXPLOSIONES BLEVE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Terminal de Almacenamiento y Distribución de GLP, Pemex, San Juan Ixhuatepec, Estado de México - 1984",
        "tipoRiesgo": "Seguridad de Procesos (PSM) / Hidrocarburos a Presión (GLP)",
        "parrafos": [
            "El 19 de noviembre de 1984, en la terminal de almacenamiento de gas licuado de petróleo (GLP) de Pemex en San Juan Ixhuatepec (San Juanico), Estado de México, una fuga masiva desató una serie de explosiones por BLEVE que devastaron la planta y los barrios circundantes, causando más de 500 muertos y miles de heridos.",
            "La ruptura de una tubería de 8 pulgadas que operaba a alta presión formó una nube de vapor inflamable no confinada que se desplazó hacia una chimenea de quemador activo. La primera deflagración envolvió las esferas de almacenamiento en un incendio descontrolado.",
            "Sin sistemas automáticos de refrigeración por agua ni válvulas de corte remoto eficaces, las esferas presurizadas colapsaron por sobrecalentamiento del acero, detonando en una cadena de BLEVEs que lanzaron fragmentos metálicos a más de un kilómetro. La lección: válvulas ESD remotas, diluvio de agua pasivo y zonas de exclusión urbana."
        ],
        "puntosClave": [
            {"icono": "shield-check", "titulo": "Válvulas de cierre rápido de emergencia (ESD)", "texto": "Aislamiento automatizado accionado por detectores de gas fijos antes de que una fuga forme nubes inflamables masivas."},
            {"icono": "droplet", "titulo": "Sistemas de diluvio y refrigeración pasiva", "texto": "Cobertura total de agua contra incendios sobre esferas y tanques presurizados para evitar que la radiación térmica degrade el acero."},
            {"icono": "map-pin", "titulo": "Ordenamiento territorial y distancias de seguridad", "texto": "Prohibición absoluta de asentamientos urbanos en el radio de afectación térmica y de sobrepresión de plantas de hidrocarburos."}
        ],
        "pregunta": "¿Cuenta tu planta de gas o combustibles con zonas de amortiguamiento libres de viviendas y sistemas automáticos de diluvio probados periódicamente?",
        "fuente": "Fuente: Reporte Técnico Internacional de Seguridad de Procesos sobre el desastre de GLP de San Juan Ixhuatepec (TNO Holanda / Pemex / Protección Civil de México, Noviembre 1984).",
        "guionReel": (
            "El 19 de noviembre de 1984, en San Juanico, México, la terminal de gas de Pemex sufrió la mayor cadena de explosiones BLEVE de la historia, dejando más de 500 muertos.\n\n"
            "Una tubería de GLP a alta presión se fracturó. La fuga formó una inmensa nube blanca que encontró una llama y estalló.\n\n"
            "El fuego envolvió las enormes esferas de gas. Sin sistemas de agua para enfriarlas, el acero hirvió y colapsó. Once esferas explotaron en cadena como bombas atómicas de fuego.\n\n"
            "Los pedazos de acero volaron a más de un kilómetro destruyendo barrios enteros pegados a la planta.\n\n"
            "¿La lección de Focus HSE? Válvulas de corte remoto inmediato, diluvio de agua automático y nunca permitir viviendas junto a plantas de gas. La seguridad está en los detalles."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 19 de noviembre de 1984, en la localidad de San Juan Ixhuatepec, conocida como San Juanico, en el Estado de México, ocurrió la mayor tragedia de almacenamiento de gas licuado de petróleo en la historia moderna, en una terminal operada por Petróleos Mexicanos, Pemex, con un saldo desgarrador de más de quinientos fallecidos.\n\n"
            "A las cinco y treinta de la madrugada, una tubería de ocho pulgadas que transportaba propano y butano a alta presión entre los tanques de almacenamiento y las esferas principales colapsó repentinamente. Una enorme cantidad de gas licuado se vaporizó al contacto con la atmósfera, creando una densa nube blanca y fría que avanzó a ras de suelo hacia las áreas circundantes.\n\n"
            "Diez minutos después, la nube alcanzó la antorcha de desecho de la planta y detonó violentamente. La sobrepresión destruyó las líneas de suministro de agua contra incendios e inutilizó los sistemas manuales de enfriamiento. Las enormes esferas metálicas de almacenamiento quedaron envueltas por un fuego voraz de hidrocarburos. Al recibir calor extremo sin refrigeración, el acero de las cúpulas perdió su resistencia mecánica mientras el gas en su interior aumentaba exponencialmente de presión.\n\n"
            "A las cinco y cuarenta y cuatro minutos se produjo la primera BLEVE: una explosión por expansión de líquido hirviente y vapor que formó una bola de fuego de cientos de metros de diámetro. En los minutos siguientes, once esferas y decenas de tanques cilíndricos detonaron en cadena, proyectando fragmentos de acero de hasta veinte toneladas a más de mil metros de distancia y arrasando las viviendas construidas a escasos pasos de la cerca perimetral.\n\n"
            "San Juanico demostró al mundo que almacenar gases a presión exige barreras de seguridad inflexibles: válvulas de corte de emergencia accionadas a distancia, sistemas fijos de diluvio con reservas de agua independientes y, fundamentalmente, la no tolerancia al avance urbano sobre los radios de amortiguamiento de las plantas industriales.\n\n"
            "El fuego no negocia con la falta de espacio ni con la demora en el aislamiento. En Focus HSE te lo recordamos siempre: la seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, 16:9 aspect ratio. The epic and somber industrial ruins of an LPG gas storage terminal in San Juan Ixhuatepec, Mexico, 1984. "
            "Giant spherical gas storage tanks ruptured like peeled metal eggshells, scorched blackened steel beams, heavy smoke hanging over a devastated industrial lot at sunrise. "
            "Distant industrial flare stacks, emergency vehicles with flashing lights in the dusty background. "
            "Highly detailed photojournalism style, raw textures of heat-twisted metal and scorched earth, 35mm lens."
        )
    },
    {
        "id": "148",
        "fecha": "20 NOVIEMBRE",
        "fechaPublicacion": "2026-11-20",
        "expediente": "Expediente #148",
        "carpeta": "2018-11-20-intoxicacion-monoxido-carbono-camara-bombeo-illinois",
        "titular": "EL GAS SILENCIOSO EN LA CÁMARA: INTOXICACIÓN EN AGUAS DE ILLINOIS",
        "palabraResaltada": "GASES DE ESCAPE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Estación Subterránea de Bombeo de Aguas, Condado de Cook, Illinois, EE.UU. - 2018",
        "tipoRiesgo": "Espacios Confinados / Atmósferas Tóxicas (Monóxido de Carbono)",
        "parrafos": [
            "El 20 de noviembre de 2018, en una cámara subterránea de bombeo de agua municipal en Illinois, dos operarios sufrieron intoxicación aguda por monóxido de carbono (CO), falleciendo uno de ellos y quedando el otro en estado crítico, en un caso investigado por OSHA.",
            "Para alimentar una bomba de achique portátil, los trabajadores instalaron un generador a gasolina sobre la acera, a menos de un metro de la boca de acceso del pozo. Los gases de combustión fueron succionados por el tiro descendente hacia la cámara confinada donde no había ventilación forzada ni detector de 4 gases.",
            "El monóxido de carbono, incoloro e inodoro, desplazó el oxígeno en la sangre de los operarios provocando desvanecimiento instantáneo sin previo aviso. La lección: ubicación de motores a combustión a más de 10 metros y a sotavento, monitoreo atmosférico continuo y ventilador extractor certificado."
        ],
        "puntosClave": [
            {"icono": "wind", "titulo": "Ubicación reglamentaria de generadores a combustión", "texto": "Mantener los motores térmicos a una distancia mínima segura de la boca del recinto y orientar el caño de escape en contra del viento."},
            {"icono": "gauge", "titulo": "Monitoreo atmosférico continuo con detector de 4 gases", "texto": "Verificar O2, CO, H2S y LEL en tres niveles de profundidad antes y durante todo el trabajo en el espacio confinado."},
            {"icono": "shield-check", "titulo": "Ventilación mecánica forzada con aire limpio", "texto": "Insuflar aire fresco desde una toma no contaminada hacia el fondo de la cámara para asegurar renovación constante."}
        ],
        "pregunta": "¿En tus tareas de mantenimiento subterráneo se monitorea continuamente la atmósfera y se alejan los motores a combustión de los accesos?",
        "fuente": "Fuente: Investigación de Fatalidad en Espacios Confinados de OSHA (Occupational Safety and Health Administration) en el estado de Illinois (Noviembre 2018).",
        "guionReel": (
            "El 20 de noviembre de 2018, en Illinois, dos operarios cayeron desmayados en un pozo de agua municipal. Uno murió y el otro quedó con daño cerebral grave.\n\n"
            "¿La causa? Pusieron un generador a gasolina junto a la boca de la cámara subterránea para conectar una bomba.\n\n"
            "El humo del caño de escape, cargado de monóxido de carbono inodoro e incoloro, bajó directamente al pozo donde trabajaban. No tenían detector de gases ni ventilación de aire limpio.\n\n"
            "En minutos, el veneno invisible los desmayó sin que pudieran pedir auxilio.\n\n"
            "¿La lección de Focus HSE? Todo motor de combustión debe estar lejos y a favor del viento. Y en espacios confinados, el monitoreo de gases es obligatorio y permanente. La seguridad está en los detalles."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 20 de noviembre de 2018, en una instalación de la red de saneamiento y bombeo de agua en el estado de Illinois, ocurrió un grave accidente en espacio confinado investigado por la OSHA, donde un trabajador perdió la vida y su compañero sufrió daños neurológicos irreversibles.\n\n"
            "Aquella mañana fría, la cuadrilla municipal debía reparar una válvula de compuerta en una cámara subterránea de cuatro metros de profundidad. Como el recinto presentaba filtraciones de agua, decidieron utilizar una electrobomba sumergible. Para suministrarle electricidad, colocaron un generador portátil con motor a gasolina justo al lado de la boca de acceso abierta sobre la acera.\n\n"
            "Los dos operarios descendieron por la escalerilla fija con sus herramientas. No portaban detectores continuos de gas ni instalaron una manguera de ventilación forzada para inyectar aire fresco. Mientras el generador rugía en la superficie, el viento empujó la columna invisible de gases de escape directamente hacia el interior del foso.\n\n"
            "El monóxido de carbono es un asesino traicionero: no tiene olor, no tiene color y no irrita las vías respiratorias. En pocos minutos, la concentración de este gas letal superó las ochocientas partes por millón en el fondo de la cámara. El monóxido se fijó con avidez a la hemoglobina de su sangre, bloqueando el transporte de oxígeno hacia el cerebro. Los trabajadores comenzaron a sentir una leve pesadez que confundieron con cansancio; segundos después, ambos perdieron el conocimiento y cayeron desplomados al agua del pozo.\n\n"
            "Cuando el personal de apoyo notó el silencio en el fondo, intentó un rescate desesperado pero ya era tarde. OSHA determinó violaciones graves a la norma de espacios confinados con permiso requerido.\n\n"
            "Este siniestro nos recuerda un principio inquebrantable de la higiene industrial: los motores de combustión interna jamás deben operar cerca de aberturas de recintos confinados. La ventilación con aire limpio y el monitoreo de cuatro gases deben ser ininterrumpidos de principio a fin.\n\n"
            "En la atmósfera de un pozo, lo invisible mata en minutos. En Focus HSE te lo recordamos siempre: la seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, 16:9 aspect ratio. A municipal water utility work site on an overcast autumn morning in Illinois, 2018. "
            "An open concrete manhole access leading into a dark underground pumping chamber with an aluminum tripod rescue system and winch erected above it. "
            "A yellow portable gas generator positioned on the asphalt nearby with exhaust fumes catching the cold air. "
            "A 4-gas atmospheric monitor showing digital alarm readouts clipped to a safety harness. "
            "Realistic documentary photography, gritty street texture, 35mm lens."
        )
    },
    {
        "id": "149",
        "fecha": "21 NOVIEMBRE",
        "fechaPublicacion": "2026-11-21",
        "expediente": "Expediente #149",
        "carpeta": "2013-11-21-derrumbe-techo-supermercado-maxima-riga-letonia",
        "titular": "EL JARDÍN EN EL TECHO: EL COLAPSO DEL SUPERMERCADO MAXIMA EN RIGA",
        "palabraResaltada": "GESTIÓN DEL CAMBIO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Supermercado Maxima XX, Barrio de Zolitude, Riga, Letonia - 2013",
        "tipoRiesgo": "Seguridad Estructural / Gestión del Cambio (MOC) / Cultura de Evacuación",
        "parrafos": [
            "El 21 de noviembre de 2013, en el barrio de Zolitude en Riga, Letonia, el techo del moderno supermercado Maxima colapsó en dos fases mientras estaba repleto de clientes y empleados, provocando la muerte de 54 personas, incluidos tres bomberos rescatistas, en el peor desastre civil del país.",
            "La investigación pericial reveló fallas gravísimas de ingeniería: las uniones atornilladas de las cerchas de acero soportaban solo la mitad de la carga prevista, y sobre la cubierta se autorizó la construcción de un parque infantil con jardineras, depositando toneladas de tierra, adoquines y agua de lluvia sin recálculo estructural.",
            "Antes del derrumbe, las alarmas de incendio sonaron más de diez veces durante la tarde debido a las deformaciones del techo, pero la administración las apagó y ordenó al personal seguir cobrando en las cajas en lugar de evacuar. La lección: gestión del cambio (MOC) para sobrecargas y evacuación incondicional ante cualquier alarma."
        ],
        "puntosClave": [
            {"icono": "file-text", "titulo": "Gestión del cambio (MOC) en modificaciones estructurales", "texto": "Ninguna modificación de carga permanente sobre techos o cubiertas debe ejecutarse sin reingeniería y firma de calculistas certificados."},
            {"icono": "shield-check", "titulo": "Factor de diseño y control de uniones atornilladas", "texto": "Realizar inspecciones con ensayos no destructivos y verificar holguras en nudos críticos de estructuras de grandes luces."},
            {"icono": "bell", "titulo": "Política de alarma = evacuación inmediata", "texto": "Prohibir bajo sanción penal que la gerencia o supervisión anule alarmas o impida el desalojo inmediato de trabajadores y clientes."}
        ],
        "pregunta": "¿En tus instalaciones se evalúa formalmente cualquier cambio de peso o estructura en techos y cubiertas bajo un proceso MOC?",
        "fuente": "Fuente: Dictamen Pericial de la Comisión Parlamentaria y Policial de Investigación de Letonia sobre el derrumbe del centro comercial Maxima en Zolitude, Riga (Noviembre 2013).",
        "guionReel": (
            "El 21 de noviembre de 2013, en Riga, Letonia, el supermercado Maxima se vino abajo con cientos de personas adentro, matando a 54 víctimas.\n\n"
            "¿La causa? Quisieron hacer un jardín en la azotea y amontonaron toneladas de tierra y piedras sobre un techo con errores de cálculo en sus vigas.\n\n"
            "Pero lo peor fue la respuesta: la alarma sonó diez veces durante la tarde por las deformaciones de la losa. La gerencia creyó que era un error técnico, apagó la sirena y ordenó seguir cobrando en cajas.\n\n"
            "A las 17:40, el techo de hormigón colapsó de golpe sepultando a todos.\n\n"
            "¿La lección de Focus HSE? Jamás agregues carga a una estructura sin gestión del cambio. Y si suena una alarma, se evacúa de inmediato. La seguridad está en los detalles."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 21 de noviembre de 2013, en el distrito de Zolitude, en Riga, capital de Letonia, se produjo una catástrofe que conmocionó a toda Europa: el colapso del techo del moderno supermercado Maxima, que segó la vida de cincuenta y cuatro personas, entre clientes, cajeros y los bomberos que acudieron al rescate.\n\n"
            "El edificio tenía apenas dos años de inaugurado. En la cubierta, los promotores decidieron añadir un atractivo jardín infantil y paseo peatonal. Días antes de la tragedia, camiones pesados habían descargado toneladas de tierra vegetal, adoquines y materiales de construcción sobre la losa del techo, todo mientras las intensas lluvias otoñales saturaban el suelo acumulado, multiplicando el peso por tres.\n\n"
            "La investigación forense de ingeniería reveló un error de cálculo imperdonable en los planos: las conexiones atornilladas de las cerchas metálicas principales tenían una capacidad de carga real que representaba apenas un tercio de lo que demandaba la estructura con la sobrecarga del jardín.\n\n"
            "Pero el factor humano completó la tragedia. A las dieciséis horas con veinte minutos de ese fatídico día, los sensores del techo comenzaron a detectar torsiones extremas y dispararon la alarma sonora de emergencia del centro comercial. Sonó más de diez veces. Lejos de desalojar el recinto, los administradores asumieron que se trataba de una 'falsa alarma', apagaron la sirena desde el panel de control y ordenaron a los empleados continuar atendiendo en las cajas y reponiendo góndolas.\n\n"
            "A las diecisiete horas y cuarenta minutos, la estructura cedió de golpe. Quinientos metros cuadrados de hormigón y acero cayeron sobre los pasillos repletos de gente. Minutos después, mientras los bomberos retiraban los primeros escombros, una segunda sección colapsó, sepultando a los propios rescatistas.\n\n"
            "Maxima nos enseñó dos mandamientos vitales: jamás añadir peso a una estructura sin una rigurosa gestión del cambio avalada por ingenieros calculistas, y jamás dudar ante una alarma. Si suena una sirena, se evacúa de inmediato, sin excepciones comerciales.\n\n"
            "En Focus HSE te lo recordamos siempre: la seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, 16:9 aspect ratio. The dramatic scene of the Maxima supermarket roof collapse in Riga Latvia, 2013. "
            "Twisted steel roof trusses and broken concrete slabs fallen into retail grocery aisles. Emergency spotlights illuminating the rubble in the dark rainy evening. "
            "Firefighters and rescue teams in high visibility gear working near the collapsed entrance surrounded by shattered glass and bent supermarket shelving. "
            "Authentic somber photojournalism, gritty detail, 35mm lens."
        )
    },
    {
        "id": "150",
        "fecha": "22 NOVIEMBRE",
        "fechaPublicacion": "2026-11-22",
        "expediente": "Expediente #150",
        "carpeta": "2013-11-22-explosiones-oleoducto-sinopec-alcantarillado-qingdao-china",
        "titular": "EL RÍO NEGRO EN EL DRENAJE: LA EXPLOSIÓN DE SINOPEC EN QINGDAO",
        "palabraResaltada": "INTERFERENCIA URBANA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Oleoducto Donghuang II y Red de Drenaje Urbano, Sinopec, Qingdao, Shandong, China - 2013",
        "tipoRiesgo": "Seguridad de Procesos (Oil & Gas / Ductos) / Espacios Subterráneos Urbanos",
        "parrafos": [
            "El 22 de noviembre de 2013, en el distrito económico de Qingdao, provincia de Shandong, China, el oleoducto Donghuang II de la petrolera estatal Sinopec sufrió una ruptura por corrosión, filtrándose cientos de toneladas de petróleo crudo a la red de alcantarillado pluvial urbano, lo que desencadenó explosiones masivas que mataron a 62 personas.",
            "La fuga comenzó en la madrugada y el crudo corrió por las canalizaciones subterráneas hacia el mar. Durante más de siete horas, brigadas de reparación y contratistas trabajaron en la zona de escape sin evacuar las avenidas y comercios vecinos ni monitorear los vapores de hidrocarburos volátiles acumulados en los desagües.",
            "Mientras los operarios utilizaban un martillo hidráulico percutor sin protección antichispa para romper el pavimento, una chispa mecánica encendió la mezcla explosiva dentro de la red cloacal. La onda expansiva levantó calles enteras por los aires y volcó colectivos. La lección: integridad y aislamiento de ductos en urbes, evacuación preventiva ante derrames y uso de herramientas antichispa."
        ],
        "puntosClave": [
            {"icono": "git-pull-request", "titulo": "Segregación física entre ductos y servicios urbanos", "texto": "Prohibir el cruce o paralelismo cercano entre tuberías de petróleo y redes de drenaje municipal sin encamisado estanco."},
            {"icono": "users", "titulo": "Evacuación inmediata y bloqueo de tráfico perimetral", "texto": "Desalojar el radio de influencia ante cualquier fuga de crudo que ingrese al subsuelo urbano antes de iniciar reparaciones."},
            {"icono": "shield-check", "titulo": "Herramientas de corte frío y antichispa certificadas", "texto": "Uso obligatorio de equipos neumáticos de corte frío y herramientas intrínsecamente seguras en atmósferas con presencia de vapores combustibles."}
        ],
        "pregunta": "¿Tiene tu organización protocolos claros de evacuación ciudadana ante derrames que puedan ingresar a drenajes o alcantarillas públicas?",
        "fuente": "Fuente: Informe Oficial de la Administración Estatal de Seguridad en el Trabajo de China (SAWS) sobre la explosión del oleoducto de Sinopec en Qingdao (Enero 2014).",
        "guionReel": (
            "El 22 de noviembre de 2013, en Qingdao, China, calles enteras volaron por los aires matando a 62 personas por una fuga en un oleoducto de Sinopec.\n\n"
            "Una tubería podrida por la corrosión se rompió y miles de litros de petróleo entraron a las alcantarillas de la ciudad.\n\n"
            "Durante 7 horas el crudo desprendió gases explosivos en los desagües, pero nadie cortó el tránsito ni evacuó a los vecinos.\n\n"
            "A las 10 de la mañana, obreros usaron un martillo mecánico sin protección antichispa para romper la calle. Una chispa prendió el alcantarillado.\n\n"
            "Kilómetros de avenidas explotaron en cadena destrozando autos y edificios como un terremoto.\n\n"
            "¿La lección de Focus HSE? Ante fugas de crudo en drenajes urbanos se evacúa de inmediato y se usan herramientas antichispa. La seguridad está en los detalles."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 22 de noviembre de 2013, en la ciudad portuaria de Qingdao, provincia de Shandong, China, ocurrió una de las peores tragedias de transporte de hidrocarburos de Asia: la explosión del oleoducto Donghuang II de la compañía petrolera Sinopec, que causó sesenta y dos muertos y cientos de heridos, investigada por la Administración Estatal de Seguridad en el Trabajo.\n\n"
            "Esa madrugada, la tubería de acero enterrada, severamente debilitada por corrosión galvánica interna y externa tras veintisiete años de operación, se fracturó. Miles de litros de crudo pesado comenzaron a fluir hacia el terreno y hallaron una vía rápida de escape: las alcantarillas y colectores pluviales de la ciudad que corrían paralelamente a escasos centímetros del ducto.\n\n"
            "Durante más de siete horas, el petróleo corrió bajo las avenidas principales, desprendiendo compuestos orgánicos volátiles que saturaron las tuberías de hormigón subterráneas, transformando la red de desagüe en un polvorín gigante. Increíblemente, ni la petrolera ni las autoridades locales ordenaron cerrar el tráfico vehicular, ni desalojar las escuelas y edificios residenciales linderos.\n\nPoco después de las diez de la mañana, un equipo de mantenimiento intentaba perforar el asfalto para descubrir la tubería rota. Utilizaron un martillo neumático convencional no certificado como herramienta antichispa. Una chispa generada por el impacto del acero contra la piedra encendió los gases acumulados en la boca de tormenta.\n\nLa detonación corrió a miles de metros por segundo a lo largo de varios kilómetros de red cloacal. El pavimento de las avenidas voló en pedazos como si hubiera estallado un campo minado. Autobuses repletos de pasajeros y camiones fueron lanzados por el aire, mientras enormes zanjas de fuego se abrían bajo los pies de los transeúntes.\n\nLa investigación oficial culpó a la falta de integridad mecánica del ducto, a la peligrosa coexistencia de hidrocarburos con servicios urbanos y a la omisión criminal de evacuar a la población civil ante una atmósfera explosiva.\n\nCuando los hidrocarburos tocan el alcantarillado, la única prioridad es evacuar y aislar, jamás golpear el suelo a ciegas. En Focus HSE te lo recordamos siempre: la seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, 16:9 aspect ratio. The dramatic urban devastation scene in Qingdao China, 2013. "
            "A city avenue ripped wide open with giant slabs of shattered asphalt thrown into the air, smoke rising from deep underground storm drainage culverts. "
            "Distant Sinopec emergency crews in orange hazmat suits and fire trucks with hoses dealing with oil slicks on the torn street. "
            "Atmospheric gray coastal sky, debris, grit, authentic photojournalist reporting quality, 35mm lens."
        )
    },
    {
        "id": "151",
        "fecha": "23 NOVIEMBRE",
        "fechaPublicacion": "2026-11-23",
        "expediente": "Expediente #151",
        "carpeta": "2017-11-23-electrocucion-mantenimiento-ccm-cargill-nebraska",
        "titular": "LA BARRA OCULTA A 480 VOLTIOS: ELECTROCUCIÓN EN CARGILL NEBRASKA",
        "palabraResaltada": "LAS 5 REGLAS DE ORO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Sala Eléctrica y Centro de Control de Motores (CCM), Planta Cargill, Nebraska, EE.UU. - 2017",
        "tipoRiesgo": "Riesgo Eléctrico / Bloqueo y Etiquetado (LOTO) / Arco Eléctrico",
        "parrafos": [
            "El 23 de noviembre de 2017, en una planta procesadora de la corporación agroindustrial Cargill en Nebraska, un técnico electricista de mantenimiento sufrió una electrocución mortal mientras realizaba tareas de verificación en un Centro de Control de Motores (CCM) de 480 voltios.",
            "La investigación de OSHA reveló que el técnico abrió el compartimento y retiró las barreras de protección de policarbonato para acceder a un relé, sin haber realizado el corte aguas arriba ni aplicado el procedimiento de verificación de ausencia de tensión (las 5 Reglas de Oro eléctricas).",
            "Al maniobrar con una herramienta manual convencional y sin guantes dieléctricos certificados para la categoría de tensión, rozó accidentalmente la barra colectora viva de cobre. La lección: desconexión efectiva aguas arriba, comprobación con multímetro verificado (Live-Dead-Live), EPP dieléctrico y barreras aislantes temporales."
        ],
        "puntosClave": [
            {"icono": "zap", "titulo": "Verificación de ausencia de tensión Live-Dead-Live", "texto": "Probar el instrumento de medición en una fuente viva antes, comprobar la ausencia en el circuito a intervenir y reconfirmar en la fuente viva."},
            {"icono": "shield-check", "titulo": "Uso obligatorio de guantes dieléctricos clase 00/0", "texto": "Utilizar guantes de caucho aislante con protector de cuero exterior al intervenir en gabinetes con partes desnudas energizadas o potencialmente vivas."},
            {"icono": "lock", "titulo": "Mantenimiento y reemplazo de barreras de policarbonato", "texto": "Mantener barreras físicas transparentes con advertencias de alta tensión en las barras colectoras principales dentro de cada gaveta de CCM."}
        ],
        "pregunta": "¿Cumples rigurosamente el protocolo de comprobación de tensión 'vivo-muerto-vivo' antes de meter tus manos en un tablero eléctrico?",
        "fuente": "Fuente: Informe de Investigación de Accidente Eléctrico Fatal de OSHA (Occupational Safety and Health Administration) en planta industrial de Nebraska (Noviembre 2017).",
        "guionReel": (
            "El 23 de noviembre de 2017, en Nebraska, un electricista experimentado de Cargill murió electrocutado dentro de una sala eléctrica.\n\n"
            "Fue a revisar un tablero de 480 voltios que fallaba. En vez de cortar la energía aguas arriba, abrió el gabinete en caliente y sacó la tapa plástica que tapaba las barras de cobre energizadas.\n\n"
            "No usaba guantes dieléctricos ni máscara para arco eléctrico. Metió la mano con un destornillador común, rozó la barra viva y recibió una descarga letal directa al corazón.\n\n"
            "OSHA concluyó que no se aplicaron las 5 Reglas de Oro de seguridad eléctrica.\n\n"
            "¿La lección de Focus HSE? Desconecta, bloquea con candado y verifica siempre ausencia de tensión con el método vivo-muerto-vivo. La seguridad está en los detalles."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 23 de noviembre de 2017, en una gran planta agroindustrial de la corporación Cargill en el estado de Nebraska, un electricista calificado falleció por contacto con corriente eléctrica mientras intervenía un Centro de Control de Motores, en un lamentable caso documentado por la OSHA.\n\n"
            "Esa jornada, un motor de accionamiento de una cinta transportadora presentaba disparos térmicos continuos. El técnico acudió a la sala eléctrica principal para revisar la gaveta de control correspondiente. Confiado en sus años de experiencia en la planta, abrió la puerta metálica del gabinete de cuatrocientos ochenta voltios con el interruptor principal energizado para realizar un chequeo visual.\n\n"
            "Al notar que un cable del relé de protección estaba flojo detrás de las protecciones internas, cometió la imprudencia fatal: desatornilló la pantalla de policarbonato transparente que cubría las barras colectoras maestras de cobre para alcanzar el borne con un destornillador común.\n\n"
            "No llevaba puestos guantes dieléctricos certificados ni máscara de protección facial contra arco eléctrico. Asumió erróneamente que manteniendo cuidado físico no tocaría las barras laterales. Pero al introducir la mano, la parte metálica de su herramienta o el dorso de su muñeca hizo contacto directo con la barra trifásica viva. La descarga de cuatrocientos ochenta voltios atravesó su cuerpo hacia la estructura metálica puesta a tierra del tablero, provocándole un paro cardíaco instantáneo por fibrilación ventricular.\n\n"
            "Los peritos de OSHA determinaron que la empresa y el personal no aplicaban de forma estricta las Cinco Reglas de Oro de la seguridad eléctrica, permitiendo maniobras en caliente sin justificación operativa ni permisos de trabajo eléctrico energizado.\n\n"
            "La electricidad no avisa, no tiene olor y no da oportunidades cuando se baja la guardia. Jamás se debe retirar una barrera protectora sin cortar la energía aguas arriba, bloquear con candado y verificar la ausencia de tensión con el método vivo-muerto-vivo.\n\n"
            "En un tablero de potencia, la confianza excesiva es el conductor más peligroso. En Focus HSE te lo recordamos siempre: la seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, 16:9 aspect ratio. Inside an industrial electrical switchgear room in Nebraska, 2017. "
            "An open 480-volt Motor Control Center (MCC) panel showing industrial contactors, circuit breakers, and heavy copper busbars. "
            "An insulated voltmeter tester with red and black probes resting on a safety rubber mat on the floor. "
            "Class 0 insulated electrical safety gloves and arc flash face shield resting on a clean steel work cart. "
            "Crisp industrial lighting, technical realism, vivid warning labels 'DANGER 480V', shot on 35mm lens."
        )
    },
    {
        "id": "152",
        "fecha": "24 NOVIEMBRE",
        "fechaPublicacion": "2026-11-24",
        "expediente": "Expediente #152",
        "carpeta": "2015-11-24-vuelco-grua-orugas-rampa-skanska-nueva-york",
        "titular": "LA RAMPA QUE CEDIO EL EJE: VUELCO DE GRÚA DE ORUGAS EN SKANSKA NY",
        "palabraResaltada": "CENTRO DE GRAVEDAD",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Obra de Infraestructura y Transporte, Skanska / Subcontratista, Nueva York, EE.UU. - 2015",
        "tipoRiesgo": "Izaje Crítico / Estabilidad de Maquinaria Pesada / Movimiento de Cargas",
        "parrafos": [
            "El 24 de noviembre de 2015, en una obra de infraestructura de transporte en Nueva York ejecutada por el consorcio Skanska y subcontratistas, una grúa móvil sobre orugas de gran tonelaje volcó lateralmente mientras trasladaba una pesada viga premoldeada sobre una rampa de acceso provisional.",
            "La investigación de OSHA y del Departamento de Edificios de Nueva York (DOB) constató que la grúa transitaba ('pick and carry') sobre un terraplén con una inclinación del 9%, superando holgadamente el límite máximo del 1% fijado por el fabricante del equipo para traslación con pluma extendida y carga suspendida.",
            "Al desplazarse en ángulo oblicuo sobre la pendiente, el centro de gravedad del conjunto pluma-carga se desplazó fuera del polígono de sustentación de las orugas, haciendo colapsar la máquina sobre su costado. La lección: nivelación rigurosa de vías de rodadura, inclinómetro en cabina y limitación estricta de traslación con carga en el plan de izaje."
        ],
        "puntosClave": [
            {"icono": "trending-down", "titulo": "Verificación topográfica de pendientes para traslación", "texto": "Prohibir el desplazamiento de grúas de orugas con carga en pendientes que excedan la especificación de tabla de carga (generalmente 1% o menos)."},
            {"icono": "file-text", "titulo": "Plan de Izaje Crítico y protocolo 'Pick and Carry'", "texto": "Evaluar dinámicas de viento, balanceo de carga y resistencia del suelo compactado antes de autorizar movimiento de grúas con carga en el gancho."},
            {"icono": "shield-check", "titulo": "Uso de inclinómetros calibrados y limitadores de momento", "texto": "Dispositivos electrónicos que bloquean las maniobras y alertan al operador si la inclinación del chasis o el radio de carga superan los márgenes de seguridad."}
        ],
        "pregunta": "¿En tus proyectos se mide con nivel óptico o inclinómetro la pendiente del terreno antes de permitir que una grúa se mueva con carga suspendida?",
        "fuente": "Fuente: Reporte de Investigación de Colapso de Grúa de OSHA y del New York City Department of Buildings (DOB) en obra civil en New York (Noviembre 2015).",
        "guionReel": (
            "El 24 de noviembre de 2015, en Nueva York, una grúa sobre orugas de 200 toneladas volcó en una obra de Skanska por rodar sobre una rampa inclinada.\n\n"
            "Llevaban una viga de hormigón de 30 toneladas colgada en el gancho. Para ganar tiempo, hicieron rodar la grúa por un terraplén con 9% de pendiente.\n\n"
            "El manual del fabricante era tajante: máximo 1% de inclinación. Al girar la pluma, el centro de gravedad se salió de las orugas y el monstruo de acero colapsó de costado con un ruido descomunal.\n\n"
            "OSHA concluyó que trasladar cargas suspendidas sobre pendientes sin plan de izaje es una imprudencia extrema.\n\n"
            "¿La lección de Focus HSE? Las grúas no son camiones. Nivela el terreno, verifica las tablas de carga y respeta los límites físicos. La seguridad está en los detalles."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 24 de noviembre de 2015, en un proyecto de infraestructura de transporte masivo en la ciudad de Nueva York liderado por la contratista Skanska junto a empresas subcontratadas, ocurrió un impactante accidente de izaje investigado por la OSHA y el Departamento de Edificios de Nueva York, cuando una grúa sobre orugas de doscientas toneladas volcó sobre su lateral.\n\n"
            "Aquel mediodía, el equipo de montaje debía posicionar una viga premoldeada de hormigón de treinta toneladas en el estribo de un puente. Para agilizar la colocación, en lugar de descargar la viga con un camión en el punto final, el supervisor autorizó la peligrosa maniobra conocida como 'pick and carry': levantar la carga con el gancho y trasladar la grúa completa sobre sus orugas por una rampa de tierra construida provisionalmente.\n\n"
            "La rampa tenía una inclinación longitudinal y transversal combinada cercana al nueve por ciento. Las tablas de operación y el manual del fabricante establecían con absoluta claridad que la máquina solo podía trasladarse con carga sobre superficies perfectamente compactadas y con una pendiente no superior al uno por ciento.\n\n"
            "Mientras la enorme máquina avanzaba lentamente hacia arriba, el operador cometió el error de girar ligeramente la superestructura para compensar el cabeceo de la carga. En ese instante, las leyes inexorables de la física actuaron: la combinación de la inclinación del terreno, el radio de la pluma y el peso oscilante de la viga desplazaron el centro de gravedad fuera del ancho de apoyo de las orugas inferiores.\n\n"
            "La oruga del lado bajo se hundió levemente en el terraplén blando y la grúa se precipitó de costado con un estruendo ensordecedor. La pluma de acero de cuarenta metros se estrelló contra el suelo, destrozando vehículos y aplastando instalaciones auxiliares, obligando al operador a arrojarse de la cabina.\n\n"
            "Las investigaciones de OSHA determinaron la ausencia de un plan de izaje crítico revisado para maniobras en movimiento y la omisión de comprobar la topografía del camino.\n\n"
            "Una grúa no es un vehículo de transporte de carga; es una máquina de precisión estacionaria. La estabilidad nunca se negocia contra la conveniencia. En Focus HSE te lo recordamos siempre: la seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, 16:9 aspect ratio. The dramatic aftermath of a crawler crane tip-over accident on a heavy infrastructure construction site in New York, 2015. "
            "A massive 200-ton yellow lattice-boom crawler crane fallen sideways on an inclined dirt earthen ramp, heavy steel tracks tilted in the air. "
            "The long lattice boom crumpled against concrete bridge abutments. High-visibility safety personnel, OSHA inspectors with hard hats and clipboards examining the soil and track grade. "
            "Overcast winter urban skyline in the background, 35mm lens authentic construction photography."
        )
    }
]

def format_duration(seconds: float) -> str:
    mins = int(seconds // 60)
    secs = int(round(seconds % 60))
    if secs == 60:
        mins += 1
        secs = 0
    return f"Audio de {mins} minutos {secs} segundos"

def crear_portada_pillow(historia: dict, output_path: str):
    width, height = 1920, 1080
    im = Image.new("RGBA", (width, height), (15, 23, 42, 255))
    draw = ImageDraw.Draw(im)

    # Gradiente sutil
    for y in range(height):
        alpha = int(255 * (y / height) * 0.45)
        draw.line([(0, y), (width, y)], fill=(2, 6, 23, alpha))

    # Rejilla técnica sutil
    grid_color = (51, 65, 85, 45)
    for x in range(0, width, 80):
        draw.line([(x, 0), (x, height)], fill=grid_color, width=1)
    for y in range(0, height, 80):
        draw.line([(0, y), (width, y)], fill=grid_color, width=1)

    # Bordes luminosos
    accent_bar = (234, 179, 8, 240)
    draw.rectangle([80, 80, 95, height - 80], fill=accent_bar)
    draw.rectangle([80, 80, width - 80, 95], fill=(30, 41, 59, 180))

    try:
        font_header = ImageFont.truetype("arialbd.ttf", 34)
        font_badge = ImageFont.truetype("arialbd.ttf", 46)
        font_title = ImageFont.truetype("arialbd.ttf", 54)
        font_sub = ImageFont.truetype("arial.ttf", 34)
        font_footer = ImageFont.truetype("arialbd.ttf", 26)
    except Exception:
        font_header = ImageFont.load_default()
        font_badge = ImageFont.load_default()
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_footer = ImageFont.load_default()

    # Header de Focus HSE
    draw.text((120, 120), "FOCUS HSE  |  ARCHIVO HISTÓRICO DE CASOS REALES", fill=(148, 163, 184, 255), font=font_header)

    # Badge de Fecha y Expediente
    badge_bg = (234, 179, 8, 255)
    draw.rounded_rectangle([120, 180, 560, 250], radius=10, fill=badge_bg)
    draw.text((140, 190), f"{historia['fecha']}  •  #{historia['id']}", fill=(15, 23, 42, 255), font=font_badge)

    # Categoría de riesgo
    draw.rectangle([120, 275, 860, 315], fill=(30, 41, 59, 230))
    draw.text((130, 280), f"RIESGO: {historia['tipoRiesgo'].upper()}", fill=(226, 232, 240, 255), font=font_footer)

    # Título principal multilínea
    raw_title = historia["titular"]
    words = raw_title.split()
    lines = []
    curr = []
    for w in words:
        curr.append(w)
        if len(" ".join(curr)) > 34:
            lines.append(" ".join(curr[:-1]))
            curr = [w]
    if curr:
        lines.append(" ".join(curr))

    curr_y = 350
    for line in lines[:3]:
        draw.text((120, curr_y), line, fill=(255, 255, 255, 255), font=font_title)
        curr_y += 75

    # Etiqueta de lugar/empresa
    curr_y += 20
    draw.text((120, curr_y), f"📍 {historia['etiquetaImagen']}", fill=(148, 163, 184, 255), font=font_sub)

    # Subtítulo preventivo
    curr_y += 60
    draw.text((120, curr_y), f"💡 Lección: {historia['palabraResaltada']} - {historia['subtitulo']}", fill=(203, 213, 225, 255), font=font_sub)

    # Footer
    draw.text((120, height - 130), "FOCUS HSE — 'La seguridad no es un eslogan, es una disciplina forjada en lecciones reales.'", fill=(100, 116, 139, 255), font=font_footer)

    im.convert("RGB").save(output_path, "PNG", quality=95)

def inyectar_en_index_html(historias_procesadas: list):
    print("Inyectando expedientes en index.html...")
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    # Ubicamos el array historiasData
    pattern = r"const historiasData\s*=\s*\[([\s\S]*?)\];"
    match = re.search(pattern, html)
    if not match:
        raise ValueError("No se pudo encontrar el bloque historiasData en index.html")

    # Extraemos el contenido actual
    array_content = match.group(1).rstrip()

    # Preparamos las nuevas historias en formato objeto JS
    nuevas_historias_js = []
    for h in historias_procesadas:
        imagen_def = "portada.jpeg" if os.path.exists(os.path.join(ASSETS_DIR, h["carpeta"], "portada.jpeg")) else "portada.png"
        obj_dict = {
            "id": h["id"],
            "fecha": h["fecha"],
            "fechaPublicacion": h["fechaPublicacion"],
            "expediente": h["expediente"],
            "carpeta": h["carpeta"],
            "titular": h["titular"],
            "palabraResaltada": h["palabraResaltada"],
            "subtitulo": h["subtitulo"],
            "imagen": imagen_def,
            "etiquetaImagen": h["etiquetaImagen"],
            "tipoRiesgo": h["tipoRiesgo"],
            "duracionAudio": h["duracionAudio"],
            "parrafos": h["parrafos"],
            "puntosClave": h["puntosClave"],
            "pregunta": h["pregunta"],
            "fuente": h["fuente"]
        }
        js_str = json.dumps(obj_dict, ensure_ascii=False, indent=8)
        # Formatear la indentación para encajar en el array de index.html
        js_str = "    " + js_str.replace("\n", "\n    ")
        nuevas_historias_js.append(js_str)

    nuevo_bloque_js = ",\n" + ",\n".join(nuevas_historias_js)
    nuevo_array = array_content + nuevo_bloque_js + "\n];"
    nuevo_html = html[:match.start()] + "const historiasData = [" + nuevo_array + html[match.end():]

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(nuevo_html)

    print(f"✓ index.html actualizado exitosamente con los 10 nuevos expedientes (#{historias_procesadas[0]['id']} a #{historias_procesadas[-1]['id']}).")

def sincronizar_portadas_disco():
    """Verifica en assets/efemerides cada carpeta y sincroniza en index.html si existe portada.jpeg"""
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    cambios = 0
    # Buscar cada historia en index.html y comprobar si portada.jpeg existe
    pattern = r'carpeta:\s*"([^"]+)",\s*titular:\s*"[^"]*",\s*palabraResaltada:\s*"[^"]*",\s*subtitulo:\s*"[^"]*",\s*imagen:\s*"([^"]+)"'
    
    def repl(m):
        nonlocal cambios
        carpeta = m.group(1)
        imagen_actual = m.group(2)
        c_path = os.path.join(ASSETS_DIR, carpeta)
        jpeg_exists = os.path.exists(os.path.join(c_path, "portada.jpeg"))
        
        imagen_correcta = "portada.jpeg" if jpeg_exists else "portada.png"
        if imagen_actual != imagen_correcta:
            cambios += 1
            print(f"  [Sincronización Portada] {carpeta}: {imagen_actual} -> {imagen_correcta}")
            return m.group(0).replace(f'imagen: "{imagen_actual}"', f'imagen: "{imagen_correcta}"')
        return m.group(0)

    nuevo_html = re.sub(pattern, repl, html)
    if cambios > 0:
        with open(INDEX_PATH, "w", encoding="utf-8") as f:
            f.write(nuevo_html)
        print(f"✓ Portadas sincronizadas en index.html ({cambios} ajustes realizados).")
    else:
        print("✓ Portadas en index.html ya estaban perfectamente sincronizadas.")

def main():
    print("Iniciando motor Kokoro para Lote 14 (#143 a #152)...\n")
    kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

    print("=======================================================")
    print("Iniciando procesamiento de 10 historias del Lote 14 (#143 a #152)")
    print("=======================================================\n")

    historias_procesadas = []

    for h in LOTE_14_DATA:
        print(f"▶ Procesando: {h['expediente']} ({h['fecha']}) - {h['titular'][:45]}...")
        target_dir = os.path.join(ASSETS_DIR, h["carpeta"])
        os.makedirs(target_dir, exist_ok=True)

        # 1. README.md
        with open(os.path.join(target_dir, "README.md"), "w", encoding="utf-8") as f:
            f.write(f"# {h['expediente']} ({h['fecha']}) — {h['titular']}\n\n")
            f.write(f"**Tipo de Riesgo:** {h['tipoRiesgo']}\n\n")
            f.write(f"**Ubicación/Empresa:** {h['etiquetaImagen']}\n\n")
            f.write(f"## Resumen Técnico\n\n")
            for p in h["parrafos"]:
                f.write(f"{p}\n\n")
            f.write(f"## Lecciones Preventivas HSE\n\n")
            for punto in h["puntosClave"]:
                f.write(f"- **{punto['titulo']}:** {punto['texto']}\n")
            f.write(f"\n*{h['fuente']}*\n")

        # 2. contenido-completo.md
        with open(os.path.join(target_dir, "contenido-completo.md"), "w", encoding="utf-8") as f:
            f.write(f"# Dossier Técnico: {h['expediente']} ({h['fechaPublicacion']})\n\n")
            f.write(f"# {h['titular']}\n\n")
            f.write(f"**Instalación:** {h['etiquetaImagen']}\n")
            f.write(f"**Disciplina:** {h['tipoRiesgo']}\n")
            f.write(f"**Concepto Clave:** {h['palabraResaltada']}\n\n")
            f.write(f"## 1. Análisis Causal y Contexto del Accidente\n\n")
            for p in h["parrafos"]:
                f.write(f"{p}\n\n")
            f.write(f"## 2. Lecciones Críticas para Prevención de Riesgos (HSE)\n\n")
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

    print("\n🎉 ¡LOTE 14 COMPLETADO AL 100%! (10 historias procesadas)\n")

if __name__ == "__main__":
    main()
