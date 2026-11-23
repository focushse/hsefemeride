# -*- coding: utf-8 -*-
"""
Generador Agéntico Automatizado para Lote 8: Expedientes #083 a #092 (16 al 25 de septiembre)
1. Crea directorios en assets/efemerides/
2. Genera README.md y contenido-completo.md
3. Guarda guion-reel.txt y prompt-portada.txt
4. Genera portada.png (16:9 alta resolución con Pillow)
5. Sintetiza audio en Kokoro (speed 0.86, ~370-430 palabras -> ~2:15 a 2:50 min)
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

LOTE_8_DATA = [
    {
        "id": "083",
        "fecha": "16 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-16",
        "expediente": "Expediente #083",
        "carpeta": "1961-09-16-explosion-planta-gas-scrubber-texas",
        "titular": "GOLPE DE LÍQUIDO EN EL COMPRESOR: LA EXPLOSIÓN EN LA PLANTA DE GAS DE TEXAS",
        "palabraResaltada": "GOLPE DE LÍQUIDO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta de Tratamiento y Compresión de Gas Natural, Texas, EE.UU. - 1961",
        "tipoRiesgo": "Seguridad de Procesos (Oil & Gas)",
        "parrafos": [
            "El 16 de septiembre de 1961, una violenta explosión destruyó la sala de compresores de una planta de tratamiento de gas natural en Texas, provocando la muerte instantánea de tres operadores.",
            "El sensor de flotante del separador de succión (scrubber) se trabó por suciedad y parafinas, impidiendo el drenaje automático de hidrocarburos líquidos. Los condensados ingresaron masivamente a los cilindros del compresor reciprocante.",
            "Al ser los líquidos incompresibles, la sobrepresión mecánica reventó la culata del cilindro a alta presión, liberando una nube de gas inflamable que detonó al instante. La lección: redundancia en alarmas de alto nivel y paradas de emergencia (ESD) automáticas.",
        ],
        "puntosClave": [
            {"icono": "gauge", "titulo": "Redundancia en sensores de nivel", "texto": "Instalar instrumentación diversa e independiente (flotante, radar o diferencial) con lógica 2oo3 en separadores de entrada."},
            {"icono": "shield-alert", "titulo": "Enclavamiento ESD de compresores", "texto": "El compresor debe disparar a parada segura (ESD) de forma inmediata ante nivel muy alto (LAHH) sin intervención humana."},
            {"icono": "wrench", "titulo": "Mantenimiento de drenajes y purgas", "texto": "Inspeccionar periódicamente líneas de drenaje de condensados para evitar obstrucción por hidratos o ceras pesadas."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: análisis de incidentes de compresión de gas de la API (American Petroleum Institute RP 14C / API 618) y lecciones del Center for Chemical Process Safety (CCPS).",
        "guionReel": (
            "¿Sabías que un compresor de gas puede explotar si le entra una sola gota de líquido?\n\n"
            "16 de septiembre de 1961. Planta de gas en Texas. Los compresores rugen a máxima potencia cuando el separador de succión falla en silencio.\n\n"
            "El flotante de nivel se trabó con impurezas. Los hidrocarburos líquidos no se drenaron y viajaron directo al compresor reciprocante. Pero los líquidos no se comprimen.\n\n"
            "El golpe hidráulico destrozó la culata de acero como si fuera vidrio. Miles de metros cúbicos de gas a alta presión se liberaron en segundos, encontrando una chispa en los motores.\n\n"
            "La explosión mató a tres operadores al instante.\n\n"
            "La lección de HSE es tajante: nunca confíes en un solo sensor de nivel. Exige enclavamientos de parada automática redundantes y purgas operativas.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic dramatic photograph of a 1961 Texas natural gas processing plant compressor station after a catastrophic mechanical failure. "
            "Shattered massive cast steel compressor cylinder head with fractured metal edges, hissing pressurized vapor clouds, twisted industrial piping, "
            "vintage pressure gauges with broken glass, harsh industrial safety lighting penetrating the haze, solemn documentary style, cinematic wide angle, "
            "detailed metal textures, oil splatters, no people, photorealistic 8k, moody atmospheric lighting."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 16 de septiembre de 1961, en una planta de tratamiento y acondicionamiento de gas natural en Texas, "
            "la rutina del turno noche fue interrumpida por un estruendo que estremeció las instalaciones en kilómetros a la redonda. "
            "La sala de compresión de alta presión había colapsado tras la detonación violenta de una nube de gas combustible.\n\n"
            "La investigación técnica posterior reconstruyó la cadena causal con precisión quirúrgica. "
            "Antes de que el gas natural ingrese a los pistones de los compresores reciprocantes, debe pasar obligatoriamente "
            "por un recipiente separador o depurador de succión, conocido técnicamente como scrubber. Su función crítica es "
            "remover cualquier condensado líquido de hidrocarburo o agua, ya que las máquinas reciprocantes están diseñadas "
            "exclusivamente para comprimir fluidos en fase gaseosa.\n\n"
            "Aquella madrugada, el sensor de nivel tipo flotante del separador se atascó mecánicamente debido a la acumulación "
            "de parafinas y sedimentos arrastrados por la corriente de pozo. La válvula automática de purga de fondo nunca abrió. "
            "El nivel de condensados comenzó a subir en silencio dentro del recipiente hasta rebalsar la línea superior de succión.\n\n"
            "Cuando una masa continua de líquido incompresible ingresó a la cámara del cilindro en plena carrera de compresión, "
            "las presiones internas superaron instantáneamente los límites de resistencia del metal. "
            "La culata de acero fundido reventó con la fuerza de un proyectil de artillería, arrojando fragmentos metálicos "
            "y liberando una corriente masiva de gas a más de setenta bares de presión. La mezcla inflamable encontró rápidamente "
            "ignición en los colectores calientes y equipos eléctricos circundantes, provocando una explosión fulminante "
            "que cobró la vida de tres operadores e incineró la nave completa.\n\n"
            "Este siniestro transformó para siempre el diseño de los sistemas instrumentados de seguridad en el sector petrolero. "
            "Estableció como estándar innegociable la redundancia total en los recipientes separadores de entrada: "
            "dos o tres sensores de nivel con tecnologías independientes, alarmas de nivel muy alto y enclavamientos automáticos de parada "
            "de emergencia, capaces de cortar la alimentación de gas y detener las máquinas motrices en milisegundos, "
            "sin requerir jamás la intervención o confirmación de un operador humano.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "084",
        "fecha": "17 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-17",
        "expediente": "Expediente #084",
        "carpeta": "2018-09-17-aplastamiento-caida-estiba-deposito-logistico",
        "titular": "LA PIRÁMIDE INESTABLE: APLASTAMIENTO POR CAÍDA DE ESTIBA EN DEPÓSITO",
        "palabraResaltada": "PIRÁMIDE INESTABLE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Centro de Distribución Logística y Almacenamiento - 2018",
        "tipoRiesgo": "Almacenamiento y Manejo de Materiales",
        "parrafos": [
            "El 17 de septiembre de 2018, un operario de depósito de 28 años murió aplastado cuando una torre de tres pallets con bolsas de 25 kilos colapsó repentinamente sobre el pasillo de tránsito peatonal.",
            "Las tarimas de madera de la base estaban rajadas y las bolsas habían sido apiladas a más de cuatro metros de altura sin film stretch envolvente ni trabado cruzado. El leve roce de la uña de un autoelevador desestabilizó la columna.",
            "Más de tonelada y media de carga sepultó al trabajador. La lección de HSE: respetar las alturas máximas de estiba, descartar pallets dañados y prohibir la circulación peatonal en zonas de maniobra de cargas elevadas.",
        ],
        "puntosClave": [
            {"icono": "package", "titulo": "Límites de altura y estabilidad", "texto": "Respetar la relación de esbeltez; en estibas libres nunca superar tres niveles o la altura recomendada por el fabricante sin estanterías racks."},
            {"icono": "shield-check", "titulo": "Inspección y descarte de pallets", "texto": "Retirar de servicio tarimas con tacos rotos, tablas rajadas o clavos salientes; la base es el cimiento de la carga."},
            {"icono": "navigation", "titulo": "Segregación peatonal estricta", "texto": "Delimitar sendas peatonales con barreras físicas y prohibir terminantemente el paso bajo o junto a estibas en altura."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: normas de seguridad en almacenamiento y manejo de materiales de OSHA 1910.176 y recomendaciones del Instituto Nacional de Seguridad y Salud en el Trabajo (INSST España).",
        "guionReel": (
            "¿Alguna vez viste un pallet torcido en un depósito y pensaste: 'ya lo van a acomodar'?\n\n"
            "17 de septiembre de 2018. Un centro logístico opera a contrarreloj. En un pasillo peatonal, bolsas de 25 kilos están apiladas a más de cuatro metros sobre pallets de madera deteriorados.\n\n"
            "Sin film de contención. Sin trabado cruzado. Un autoelevador maniobra cerca y roza la base apenas con la punta de una uña.\n\n"
            "La columna cedió en una fracción de segundo. Más de tonelada y media de peso cayó a plomo sobre un operario de 28 años que caminaba por el lugar.\n\n"
            "No hubo tiempo de reaccionar.\n\n"
            "En logística, la gravedad no perdona: respeta las alturas máximas de estiba, destruye los pallets rotos y mantén a los peatones separados de las cargas.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of a modern logistics warehouse aisle after a catastrophic collapse of stacked heavy palletized bags. "
            "Ruptured paper bags spilling fine industrial powder, fractured wooden pallets with splintered timber, yellow painted pedestrian walkway lines partially covered in debris, "
            "tall industrial storage racks in background, forklift hazard lights blinking in the distance, high contrast industrial warehouse lighting, "
            "documentary realism, 8k resolution, wide cinematic angle, poignant HSE inspection atmosphere."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 17 de septiembre de 2018, en un centro de distribución logística de alta rotación, "
            "la presión por despachar pedidos culminó en una tragedia evitable. Un joven operario de almacén de veintiocho años "
            "perdió la vida aplastado bajo una avalancha de bolsas de productos químicos granulados, "
            "en pleno pasillo de circulación interna.\n\n"
            "El análisis de las condiciones de almacenamiento reveló múltiples desvíos normalizados durante meses. "
            "Para ahorrar espacio en las estanterías metálicas, los supervisores habían autorizado el apilamiento libre de pallets en el suelo, "
            "superando los cuatro metros y medio de altura en tres niveles continuos. "
            "Las tarimas de madera utilizadas en la base presentaban tacos fisurados y tablas desclavadas, "
            "comprometiendo la horizontalidad de la carga. Además, las bolsas no contaban con film stretch plástico envolvente "
            "ni con un patrón de trabado cruzado que garantizara la cohesión interna del bloque.\n\n"
            "Bastó una mínima perturbación mecánica: un autoelevador que retrocedía rozó levemente una de las esquinas del pallet inferior. "
            "La pérdida de verticalidad generó un momento de vuelco incontrolable. "
            "En menos de dos segundos, más de mil seiscientos kilogramos de carga cayeron sobre el operario que transitaba a pie "
            "por una senda mal delimitada, sufriendo traumatismos mortales instantáneos por compresión torácica.\n\n"
            "Este lamentable hecho subraya tres pilares insustituibles en la gestión de depósitos. "
            "Primero: el establecimiento estricto de coeficientes de esbeltez y alturas máximas permitidas para cada tipo de mercadería, "
            "utilizando sistemas de estanterías industriales calculadas siempre que se supere la altura de hombros. "
            "Segundo: la inspección pre-uso y descarte sistemático de cualquier pallet que presente daños estructurales. "
            "Y tercero: la segregación física total entre la circulación peatonal y las zonas operativas de carga y descarga de materiales pesados.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "085",
        "fecha": "18 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-18",
        "expediente": "Expediente #085",
        "carpeta": "2004-09-18-desastre-pirotecnia-seest-kolding",
        "titular": "LA CHISPA EN EL POLVORÍN: EL DESASTRE PIROTÉCNICO DE SEEST",
        "palabraResaltada": "DESASTRE PIROTÉCNICO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Fábrica y Almacén de Fuegos Artificiales N. P. Johnsen, Seest, Dinamarca - 2004",
        "tipoRiesgo": "Seguridad de Procesos / Almacenamiento",
        "parrafos": [
            "El 18 de septiembre de 2004, una serie de explosiones colosales pulverizó el depósito de pirotecnia N. P. Johnsen en Seest, Dinamarca, destruyendo 355 viviendas y obligando a evacuar a 2.000 residentes.",
            "Durante la descarga manual, la caída brusca de una caja con cohetes detonó por fricción una mezcla pirotécnica altamente sensible. El fuego se propagó velozmente a contenedores no autorizados que almacenaban más de 800 toneladas de explosivos.",
            "La onda expansiva mató a un bombero voluntario e hirió a decenas de personas. El desastre demostró que almacenar materiales explosivos dentro del tejido urbano sin muros de contención ni separación física es una amenaza inadmisible.",
        ],
        "puntosClave": [
            {"icono": "flame", "titulo": "Control estricto de carga máxima", "texto": "Nunca exceder las cantidades netas de materia explosiva autorizadas y mantener distancias de seguridad según la tabla de compatibilidad."},
            {"icono": "sparkles", "titulo": "Manipulación antideslizante y antiestática", "texto": "Prohibir impactos bruscos, utilizar herramientas de bronce antidetonantes y garantizar conductividad estática en pisos y calzado."},
            {"icono": "shield", "titulo": "Búnkeres aislados y barreras de tierra", "texto": "Almacenar pirotecnia en celdas blindadas independientes con taludes de tierra perimetrales para confinar cualquier deflagración."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe oficial de la Comisión de Investigación del Gobierno de Dinamarca sobre el desastre de Seest y directiva europea Seveso III (2012/18/UE).",
        "guionReel": (
            "¿Qué pasa cuando se acumulan 800 toneladas de pólvora pegadas a un barrio residencial?\n\n"
            "18 de septiembre de 2004. Seest, Dinamarca. En un depósito de fuegos artificiales, dos operarios manipulan cajas pesadas.\n\n"
            "Una caja resbala y cae al piso de hormigón. La fricción enciende una mezcla química inestable. El fuego se extiende a contenedores marítimos abarrotados que triplicaban el límite legal permitido.\n\n"
            "Quince minutos después, sobrevino el infierno: detonaciones masivas arrasaron 355 casas, provocando un cráter inmenso y la muerte de un bombero.\n\n"
            "Dos mil vecinos tuvieron que huir con lo puesto.\n\n"
            "La lección de HSE fue contundente: los explosivos exigen búnkeres aislados con taludes de tierra y estricto control de masa neta lejos de las ciudades.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic dramatic wide-angle shot of the aftermath of the 2004 Seest fireworks depot explosion in Denmark. "
            "Scattered burnt debris, collapsed industrial warehouse steel frames glowing with embers, deep craters in the soil, "
            "shattered roofs of nearby residential houses visible under a dusk sky filled with dense smoke and flashing emergency lights, "
            "firetrucks in distance, photojournalistic documentary aesthetics, 8k resolution, raw textures, atmospheric dusk lighting."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 18 de septiembre de 2004, la apacible localidad de Seest, en los suburbios de Kolding, Dinamarca, "
            "fue sacudida por una de las catástrofes pirotécnicas más devastadoras de la historia europea moderna. "
            "La fábrica y depósito N. P. Johnsen se convirtió en un volcán de fuego y metralla que arrasó trescientas cincuenta y cinco viviendas "
            "y demandó la evacuación de urgencia de más de dos mil vecinos.\n\n"
            "Todo comenzó alrededor de las tres de la tarde con un incidente menor en apariencia. "
            "Mientras dos trabajadores descargaban un contenedor, una caja que contenía artefactos pirotécnicos cayó bruscamente al suelo. "
            "El impacto generó una fricción suficiente para encender la mezcla de pólvora negra y sales oxidantes. "
            "El incendio inicial se propagó de inmediato a pilas de cajas contiguas almacenadas sin separación ignífuga.\n\n"
            "Lo que convirtió este conato en un cataclismo fue la violación flagrante de los límites de almacenamiento. "
            "El complejo albergaba más de ochocientas toneladas de material pirotécnico, una masa que excedía con creces "
            "la capacidad habilitada por la autoridad de bomberos. Las naves y contenedores marítimos actuaron como bombas de confinamiento. "
            "A las diecisiete horas, una serie de tres explosiones descomunales pulverizó el predio, "
            "proyectando proyectiles a más de un kilómetro de distancia, provocando la muerte de un bombero voluntario "
            "e hiriendo a decenas de socorristas y civiles.\n\n"
            "El desastre de Seest impulsó una reforma drástica en las directivas europeas de sustancias peligrosas Seveso. "
            "Demostró la imposibilidad técnica de controlar incendios pirotécnicos masivos una vez iniciados "
            "y consagró tres principios preventivos obligatorios: la prohibición absoluta de emplazar polvorines en cercanías de zonas urbanas, "
            "la compartimentación estricta en búnkeres reforzados protegidos por terraplenes de tierra absorbentes de ondas expansivas, "
            "y el pesaje y auditoría rigurosa de la masa explosiva neta en cada etapa de la cadena logística.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "086",
        "fecha": "19 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-19",
        "expediente": "Expediente #086",
        "carpeta": "2017-09-19-derrumbe-edificio-industrial-sobrecarga-sismo-mexico",
        "titular": "EL PESO INVISIBLE: COLAPSO ESTRUCTURAL POR SOBRECARGA EN SISMO",
        "palabraResaltada": "PESO INVISIBLE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Edificio de Manufactura y Oficinas Industriales, Ciudad de México - 2017",
        "tipoRiesgo": "Seguridad Estructural / Emergencias",
        "parrafos": [
            "El 19 de septiembre de 2017, durante el terremoto de Puebla-Morelos en México, un edificio fabril colapsó en su planta baja provocando la muerte de trabajadores atrapados bajo los escombros.",
            "Años atrás, la gerencia había instalado en la azotea y pisos superiores tanques de agua pesados y maquinaria textil industrial sin realizar un cálculo de resistencia estructural ni tramitar permisos de Gestión del Cambio (MOC).",
            "La sobrecarga acumulada en niveles superiores incrementó las fuerzas de torsión e inercia durante el sismo, provocando la falla por cortante de las columnas principales. La lección: cualquier peso añadido exige peritaje civil previo.",
        ],
        "puntosClave": [
            {"icono": "building", "titulo": "Gestión del cambio estructural (MOC)", "texto": "Prohibir la instalación de equipos, tanques o sobrepisos sin la memoria de cálculo y firma de un ingeniero estructural colegiado."},
            {"icono": "activity", "titulo": "Inspecciones pos-sísmicas certificadas", "texto": "Tras eventos sísmicos o modificaciones edilicias, evaluar grietas diagonales en columnas, vigas y losas antes de autorizar el reingreso."},
            {"icono": "users", "titulo": "Vías de evacuación libres y simulacros", "texto": "Mantener escaleras de emergencia despejadas, señalizadas y libres de almacenamiento temporal para permitir una evacuación fluida."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: dictámenes técnicos de Protección Civil del Gobierno de la Ciudad de México (Sismo 19S) y códigos de diseño estructural y seguridad de vida NFPA 101 / IBC (International Building Code).",
        "guionReel": (
            "¿Tu empresa agregó maquinaria pesada o tanques en el techo sin consultar a un calculista estructural?\n\n"
            "19 de septiembre de 2017. Terremoto en Ciudad de México. En cuestión de segundos, un edificio industrial se desplomó como un castillo de naipes.\n\n"
            "Durante años, la empresa sumó telares pesados en pisos altos y enormes depósitos de agua en la azotea. Nadie calculó el peso extra.\n\n"
            "Al temblar la tierra, esa masa acumulada arriba actuó como un péndulo demoledor. Las columnas de la planta baja sufrieron una falla por cortante y colapsaron por completo.\n\n"
            "Varios trabajadores quedaron sepultados.\n\n"
            "La lección de HSE es vital: cualquier cambio de carga exige Gestión del Cambio y peritaje estructural. El peso invisible no perdona cuando la tierra se mueve.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic dramatic photograph of an industrial multi-story building structural failure after an earthquake in Mexico City. "
            "Pancaked concrete slabs with exposed twisted rebar, heavy machinery and water tanks tilted precariously on the ruined rooftop, "
            "dust clouds hanging in the afternoon sun, emergency cordon tape, rescue equipment staged in foreground, "
            "solemn and respectful civil engineering forensic documentation style, 8k resolution, authentic rubble textures, high dynamic range."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 19 de septiembre de 2017, a exactamente treinta y dos años del trágico terremoto de 1985, "
            "un violento sismo de magnitud siete coma uno sacudió el centro de México. Entre las decenas de colapsos estructurales, "
            "un edificio de uso mixto fabril y comercial en la Ciudad de México cedió por completo en sus niveles inferiores, "
            "sepultando a operarios que no lograron alcanzar las salidas de emergencia.\n\n"
            "Los peritajes forenses de ingeniería civil revelaron una causa raíz que iba mucho más allá de la aceleración sísmica del terreno. "
            "La estructura original, concebida en la década de 1970 para oficinas ligeras, había sufrido sucesivas modificaciones "
            "ilegales a lo largo de los años. En los pisos superiores se habían montado pesadas máquinas industriales y telas de alto tonelaje, "
            "mientras que en la azotea se instalaron grandes tanques de agua y estructuras metálicas de soporte sin ningún cálculo de resistencia.\n\n"
            "Durante las ondas telúricas, esta masa masiva concentrada en la parte superior actuó como un efecto péndulo invertido. "
            "Las fuerzas de inercia y torsión generadas superaron drásticamente la capacidad de corte de las columnas de hormigón armado, "
            "que además presentaban el típico fenómeno de entrepiso blando en la planta baja. Las columnas estallaron frágilmente, "
            "provocando el aplastamiento tipo sándwich de los niveles inferiores en escasos segundos.\n\n"
            "Esta catástrofe dejó una enseñanza fundamental para la seguridad industrial y la gestión del riesgo: "
            "la Gestión del Cambio debe aplicarse con rigor implacable a las estructuras físicas. "
            "Ninguna máquina pesada, depósito de fluidos o modificación de tabiquería puede ejecutarse sin la memoria técnica "
            "y firma de un ingeniero estructural colegiado. Asimismo, destaca la obligatoriedad de realizar simulacros realistas de repliegue "
            "y evacuación, garantizando que las vías de escape permanezcan libres de todo obstáculo que retrase la salida en una emergencia.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "087",
        "fecha": "20 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-20",
        "expediente": "Expediente #087",
        "carpeta": "2016-09-20-intoxicacion-vapores-nitrosos-decapado-tanques",
        "titular": "EL GAS QUE MATA EN SILENCIO: INTOXICACIÓN POR VAPORES NITROSOS",
        "palabraResaltada": "VAPORES NITROSOS",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Taller de Fabricación de Cubas de Acero Inoxidable - 2016",
        "tipoRiesgo": "Riesgo Químico / Higiene Industrial",
        "parrafos": [
            "El 20 de septiembre de 2016, dos operarios sufrieron intoxicación química grave tras realizar tareas de decapado con pasta de ácido nítrico y fluorhídrico en el interior de un tanque de acero inoxidable.",
            "El trabajo se efectuó en un galpón cerrado sin ventilación mecánica forzada ni monitores de gases. Al reaccionar el ácido con el metal se generó dióxido de nitrógeno (NO2), un gas pardo rojizo de baja solubilidad.",
            "Los trabajadores solo sintieron una leve irritación inicial, pero ocho horas después en sus hogares desarrollaron edema agudo de pulmón por daño alveolar químico diferido. La lección: extracción localizada y vigilancia médica obligatoria.",
        ],
        "puntosClave": [
            {"icono": "wind", "titulo": "Ventilación mecánica forzada y localizada", "texto": "Extraer los vapores pesados en el punto exacto de emisión hacia sistemas de neutralización lavadores de gases (scrubbers)."},
            {"icono": "shield-alert", "titulo": "Uso de respiradores con cartuchos específicos", "texto": "Exigir protección respiratoria con cartuchos para gases ácidos/NOx o equipos de línea de aire en recintos semicerrados."},
            {"icono": "heart-pulse", "titulo": "Protocolo de observación médica diferida", "texto": "Los vapores nitrosos destruyen los alvéolos sin causar tos inmediata; todo expuesto debe permanecer bajo observación clínica al menos 24 horas."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: fichas de datos de seguridad (FDS) de ácidos decapantes, guías de higiene industrial de ACGIH y protocolos de manejo de edema pulmonar tóxico de NIOSH.",
        "guionReel": (
            "¿Sabías que existe un gas industrial que puedes inhalar hoy sintiendo solo un cosquilleo, y ahogarte en tu cama esta noche?\n\n"
            "20 de septiembre de 2016. Taller metalúrgico. Dos operarios aplican ácido nítrico para decapar soldaduras dentro de una cuba de acero inoxidable.\n\n"
            "El galpón no tiene extractores. Al tocar el metal, el ácido libera dióxido de nitrógeno: una niebla parda y pesada. Los operarios usan barbijos comunes que no retienen gases.\n\n"
            "Terminan el turno cansados pero tranquilos. Ocho horas después, en sus casas, despiertan sin poder respirar: edema pulmonar agudo por destrucción de los alvéolos.\n\n"
            "Tuvieron que ingresar a terapia intensiva.\n\n"
            "La lección de HSE es crítica: con vapores nitrosos se exige extracción forzada, máscaras químicas específicas y vigilancia médica diferida obligatoria.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an industrial stainless steel tank fabrication workshop. "
            "Inside the large cylindrical vessel, faint reddish-brown nitrous vapor haze hangs in the air, "
            "pickling paste brush containers resting on metal floor, high-powered inspection lamp creating sharp atmospheric light shafts through chemical fumes, "
            "acid warning signage on workshop wall, stark and dramatic industrial hygiene documentary shot, 8k resolution, photorealistic stainless steel reflections."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 20 de septiembre de 2016, en un taller de construcciones metalmecánicas pesadas, "
            "dos operarios especializados concluyeron una larga jornada de abrillantado y decapado químico de cordones de soldadura "
            "en el interior de grandes cubas de acero inoxidable. Al finalizar el turno, reportaron apenas una leve sequedad en la garganta "
            "y se retiraron a sus hogares. Nadie imaginaba que horas después lucharían por sus vidas en una sala de cuidados intensivos.\n\n"
            "La causa del incidente radicó en la naturaleza traicionera de los agentes químicos empleados. "
            "Las pastas y soluciones de decapado contienen una mezcla concentrada de ácido nítrico y fluorhídrico. "
            "Al reaccionar con el metal y los óxidos residuales a temperatura ambiente, liberan mezclas de óxidos de nitrógeno, "
            "principalmente dióxido de nitrógeno, un gas de tono pardo rojizo más pesado que el aire. "
            "El recinto semicerrado carecía de ventilación forzada o extracción localizada, y los operarios portaban mascarillas descartables "
            "para polvo, totalmente inútiles frente a vapores ácidos.\n\n"
            "A diferencia de otros gases irritantes como el cloro o el amoníaco, los vapores nitrosos tienen una solubilidad en agua muy baja. "
            "No provocan espasmos inmediatos ni tos violenta en las vías aéreas superiores, lo que genera una falsa sensación de tolerancia. "
            "El gas penetra profundamente hasta los bronquiolos y alvéolos, donde reacciona con la humedad biológica formando ácido nítrico. "
            "Entre seis y veinticuatro horas después de la exposición, las paredes capilares colapsan por necrosis celular, "
            "inundando los pulmones con líquido y desatando un edema pulmonar diferido potencialmente mortal.\n\n"
            "Este grave caso resalta lecciones ineludibles de higiene industrial: "
            "todo decapado químico debe considerarse una maniobra de alto riesgo químico, exigiendo ventilación con extracción de tiro forzado "
            "y neutralización en scrubber, protección respiratoria con cartuchos combinados para gases ácidos o suministro de aire asistido, "
            "y la aplicación de un protocolo estricto de vigilancia clínica que mantenga a cualquier operario expuesto "
            "bajo control médico preventivo por al menos veinticuatro horas.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "088",
        "fecha": "21 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-21",
        "expediente": "Expediente #088",
        "carpeta": "2001-09-21-explosion-planta-quimica-azf-toulouse",
        "titular": "EL HANGAR 221: LA DETONACIÓN MASIVA DE AZF EN TOULOUSE",
        "palabraResaltada": "AZF EN TOULOUSE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta de Fertilizantes AZF (Grande Paroisse), Toulouse, Francia - 2001",
        "tipoRiesgo": "Seguridad de Procesos (PSM)",
        "parrafos": [
            "El 21 de septiembre de 2001, una detonación masiva en el hangar 221 de la fábrica de fertilizantes AZF en Toulouse dejó un cráter de 7 metros de profundidad, 31 muertos y más de 2.500 heridos.",
            "Un operario de una empresa contratista arrojó por error un saco de 500 kilos de dicloroisocianurato de sodio (un compuesto clorado de tratamiento de aguas) sobre un montículo de 300 toneladas de nitrato de amonio fuera de especificación.",
            "La reacción química exotérmica entre el cloro y el nitrato generó tricloruro de nitrógeno inestable, desencadenando la detonación global del hangar. La lección: segregación estricta y trazabilidad total en depósitos de residuos.",
        ],
        "puntosClave": [
            {"icono": "alert-triangle", "titulo": "Incompatibilidad química absoluta", "texto": "El nitrato de amonio jamás debe tener contacto con sustancias cloradas, aceites o materiales reductores; la mezcla es altamente detonante."},
            {"icono": "clipboard-check", "titulo": "Trazabilidad de productos fuera de norma", "texto": "Los lotes degradados o barridos de suelo deben identificarse con rótulo inequívoco y almacenarse en áreas exclusivas bajo doble control."},
            {"icono": "building", "titulo": "Distancias de seguridad urbana (Ley Bachelot)", "texto": "La catástrofe de Toulouse impulsó en Europa leyes estrictas de planificación urbana para alejar las industrias Seveso de las zonas residenciales."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe oficial de la Comisión de Investigación del Gobierno Francés sobre la catástrofe de AZF Toulouse y directrices de seguridad de fertilizantes de la EFMA (Fertilizers Europe).",
        "guionReel": (
            "¿Puede un simple error de limpieza causar una explosión equivalente a 40 toneladas de TNT?\n\n"
            "21 de septiembre de 2001. Toulouse, Francia. Planta química AZF. Un operario contratista junta 500 kilos de un polvo blanco de un suelo y cree que es nitrato de amonio.\n\n"
            "Lo lleva al Hangar 221 y lo vierte sobre 300 toneladas de fertilizante degradado. Pero el saco contenía cloro para piscinas.\n\n"
            "Al entrar en contacto el cloro con el nitrato, se desató una violenta reacción química que formó tricloruro de nitrógeno, un compuesto hipersensible. Quince minutos después, sobrevino la catástrofe.\n\n"
            "Un cráter de siete metros de profundidad, 31 muertos y 2.500 heridos. La onda expansiva rompió ventanas a 5 kilómetros.\n\n"
            "La lección de HSE es eterna: jamás mezcles residuos químicos sin análisis previo de compatibilidad y trazabilidad estricta.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic dramatic photograph of the industrial ruins at the AZF chemical plant in Toulouse after the 2001 explosion. "
            "A massive blast crater surrounded by shredded structural steel columns, pulverized concrete slabs, fragmented storage hangars, "
            "smoke rising into a pale morning sky, industrial pipelines torn like straw, solemn investigative forensic documentation, "
            "cinematic wide lens, ultra detailed debris textures, atmospheric haze, 8k resolution, raw documentary aesthetics."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 21 de septiembre de 2001, a las diez y diecisiete de la mañana, la ciudad de Toulouse en el suroeste de Francia "
            "fue sacudida por un terremoto artificial de magnitud tres coma cuatro en la escala de Richter. "
            "El complejo petroquímico AZF de Grande Paroisse acababa de sufrir una de las mayores detonaciones industriales "
            "en tiempos de paz: un cráter de setenta metros de diámetro y siete de profundidad, treinta y una personas fallecidas, "
            "más de dos mil quinientos heridos y severos daños materiales en un radio de cinco kilómetros.\n\n"
            "La rigurosa investigación forense oficial determinó que la tragedia se originó en el Hangar doscientos veintiuno, "
            "utilizado para acopiar nitrato de amonio fuera de especificación y residuos de barrido de planta. "
            "Aproximadamente quince minutos antes del estallido, un operario de una empresa contratista de limpieza "
            "recogió un saco de quinientos kilos rotulado erróneamente, que en realidad contenía dicloroisocianurato de sodio, "
            "un compuesto fuertemente clorado utilizado en el tratamiento de aguas. Creyendo que se trataba de nitrato, "
            "lo arrojó sobre el montículo de trescientas toneladas de nitrato de amonio que descansaba en el suelo húmedo.\n\n"
            "La interacción química fue inmediata y fatal. El cloro reaccionó con el catión amonio en presencia de humedad ácida, "
            "generando tricloruro de nitrógeno, un compuesto líquido aceitoso con una extrema sensibilidad al choque y al calor. "
            "La descomposición inicial actuó como un potente cebo detonante que transmitió la onda de choque al volumen masivo "
            "de nitrato de amonio, alcanzando velocidades de detonación supersónicas equivalentes a cuarenta toneladas de trinitrotolueno.\n\n"
            "La catástrofe de Toulouse transformó radicalmente la legislación europea sobre seguridad de procesos y gestión de riesgos mayores. "
            "Dio origen en Francia a la histórica Ley Bachelot, que impuso planes de prevención de riesgos tecnológicos (PPRT) "
            "con zonas de amortiguamiento urbano obligatorias. Para los profesionales de HSE, la lección es axiomática: "
            "las sustancias oxidantes como el nitrato de amonio exigen segregación física absoluta de productos incompatibles, "
            "eliminación de hangares de residuos a granel sin trazabilidad, y la prohibición terminante de que tareas de manipulación química "
            "crítica sean ejecutadas por personal sin capacitación específica en riesgos reactivos.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "089",
        "fecha": "22 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-22",
        "expediente": "Expediente #089",
        "carpeta": "2018-09-22-electrocucion-cambio-luminaria-fase-neutro",
        "titular": "LA TRAMPA DEL NEUTRO CORTADO: ELECTROCUCIÓN EN ALTURA",
        "palabraResaltada": "NEUTRO CORTADO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Nave Industrial Metalmecánica - 2018",
        "tipoRiesgo": "Riesgo Eléctrico / LOTO",
        "parrafos": [
            "El 22 de septiembre de 2018, un electricista de mantenimiento de 34 años falleció electrocutado sobre una plataforma tijera mientras reemplazaba una campana LED en la nave de una fábrica.",
            "El técnico apagó la tecla unipolar de pared confiando en que el circuito estaba desenergizado. Sin embargo, una conexión errónea antigua cortaba el conductor neutro en lugar de la fase viva de 220 voltios.",
            "Al manipular los bornes sin verificar ausencia de tensión ni cortar la térmica bipolar en el tablero general, recibió una descarga letal a través del tórax hacia el chasis metálico. La regla de oro: comprobar siempre con tester o multímetro.",
        ],
        "puntosClave": [
            {"icono": "zap", "titulo": "Corte bipolar y bloqueo en tablero general", "texto": "Nunca intervenir una línea eléctrica confiando solo en una llave unipolar de pared; abrir y bloquear el disyuntor y la llave termomagnética general."},
            {"icono": "gauge", "titulo": "Verificación efectiva de ausencia de tensión", "texto": "Tercera Regla de Oro eléctrica: comprobar tensión entre fase-tierra, fase-neutro y neutro-tierra con un voltímetro previamente verificado."},
            {"icono": "shield", "titulo": "Uso de guantes dieléctricos y herramientas aisladas", "texto": "Utilizar guantes para la tensión de trabajo (Clase 00 o 0) y herramientas con aislamiento certificado a 1.000 voltios según IEC 60900."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: estándar NFPA 70E sobre seguridad eléctrica en lugares de trabajo, 5 Reglas de Oro eléctricas y norma OSHA 1910.333.",
        "guionReel": (
            "¿Confías en la tecla de la pared antes de tocar un cable con las manos desnudas?\n\n"
            "22 de septiembre de 2018. Nave industrial. Un electricista de 34 años sube en una tijera elevadora a seis metros de altura para cambiar una luminaria LED.\n\n"
            "Presiona el interruptor de la pared. La luz se apaga. Confiado, sube sin guantes dieléctricos y toma los cables con los dedos.\n\n"
            "Pero el interruptor tenía un error de instalación: cortaba el neutro, no la fase. La línea seguía energizada con 220 voltios vivos.\n\n"
            "La corriente atravesó su corazón y descargó por la barandilla metálica de la plataforma. Murió en el acto.\n\n"
            "En electricidad nunca se supone: aplica LOTO en el tablero general y comprueba siempre la ausencia de tensión con multímetro.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an elevated industrial scissor lift platform inside a manufacturing facility at high ceiling level. "
            "Dismantled high-bay industrial LED lamp fixture with hanging copper wires, multimeter probe resting on yellow insulated tool tray, "
            "warning lock on general electrical breaker box below, crisp technical lighting with soft shadows, "
            "documentary forensic safety recreation style, 8k resolution, photorealistic steel trusses and electrical conduits."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 22 de septiembre de 2018, en una nave industrial metalmecánica de gran porte, "
            "una tarea habitual de mantenimiento correctivo terminó en fatalidad. Un técnico electricista de treinta y cuatro años, "
            "con más de una década de oficio, sufrió una descarga eléctrica letal mientras cambiaba una campana de iluminación LED "
            "suspendida de las cabriadas del techo a seis metros del suelo.\n\n"
            "La reconstrucción del accidente evidenció una trampa técnica que suele cobrar vidas en instalaciones no auditadas. "
            "Antes de subir a la plataforma elevadora tipo tijera, el operario accionó el interruptor unipolar ubicado en la pared del sector. "
            "Al ver que las luces se apagaban, asumió con absoluta certeza que el circuito carecía de potencial eléctrico. "
            "Sin embargo, debido a una modificación antigua y defectuosa en la caja de empalmes, el interruptor estaba instalado en serie "
            "sobre el conductor neutro y no sobre la fase viva.\n\n"
            "Cuando el técnico tomó los cables de alimentación para conectar la nueva bornera, sin guantes dieléctricos "
            "y sin haber utilizado un multímetro para constatar la energía cero, sus dedos tocaron directamente el conductor de fase a doscientos veinte voltios. "
            "Al estar apoyado contra la barandilla metálica de la cesta elevadora, la corriente cerró el circuito a través de su brazo, "
            "atravesó su cavidad torácica provocando fibrilación ventricular instantánea, y descargó a tierra por la estructura del equipo.\n\n"
            "Este trágico suceso recuerda con crudeza por qué las Cinco Reglas de Oro de la seguridad eléctrica "
            "son de cumplimiento estricto y secuencial. Primero: el corte de energía debe ser visible y bipolar en el tablero seccional, "
            "bloqueando la llave termomagnética con candado y tarjeta LOTO. Segundo: jamás debe considerarse un interruptor de pared como un medio de aislamiento seguro. "
            "Y tercero: la comprobación de ausencia de tensión es obligatoria en todos y cada uno de los conductores, "
            "midiendo fase contra neutro y ambos respecto a tierra con un instrumento de medición probado inmediatamente antes y después de la maniobra.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "090",
        "fecha": "23 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-23",
        "expediente": "Expediente #090",
        "carpeta": "2015-09-23-caida-techo-efecto-vela-viento-chapa",
        "titular": "EL EFECTO VELA: LA RÁFAGA QUE DERRIBÓ AL TECHISTA",
        "palabraResaltada": "EFECTO VELA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Cubierta Metálica de Tinglado Industrial - 2015",
        "tipoRiesgo": "Trabajo en Altura / Factores Climáticos",
        "parrafos": [
            "El 23 de septiembre de 2015, un techista de 42 años cayó desde ocho metros de altura al vacío mientras reparaba la cubierta de chapa de un depósito durante una jornada de vientos racheados.",
            "El operario trasladaba manualmente sobre sus hombros un panel trapezoidal de seis metros de largo. Una ráfaga imprevista de 50 km/h embolsó la lámina metálica generando un violento efecto vela que lo levantó de la pasarela.",
            "El trabajador llevaba arnés colocado pero la cola de amarre no estaba enganchada a la línea de vida de acero. Falleció por politraumatismo severo. La lección: suspender trabajos en techos ante vientos y mantener amarre al 100%.",
        ],
        "puntosClave": [
            {"icono": "wind", "titulo": "Límites de velocidad del viento", "texto": "Suspender el montaje y acarreo manual de chapas metálicas cuando la velocidad del viento supere los 35 a 40 km/h o existan ráfagas bruscas."},
            {"icono": "anchor", "titulo": "Anclaje continuo al 100%", "texto": "El trabajador debe estar permanentemente conectado a una línea de vida horizontal certificada mediante absorbedor de impacto y doble cabo de amarre."},
            {"icono": "truck", "titulo": "Izaje mecánico de paneles", "texto": "Prohibir el traslado manual de paneles largos en techos empinados; utilizar eslingas textiles y guías de viento con cuerdas desde el suelo."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: normativas de prevención en trabajos sobre cubiertas y techos de OSHA 1926 Subpart M, norma IRAM 3622-1 y guías técnicas del INSST sobre caídas de altura.",
        "guionReel": (
            "¿Llevarías una chapa de seis metros al hombro sobre un techo a ocho metros de altura con viento fuerte?\n\n"
            "23 de septiembre de 2015. Reparación de cubierta industrial. El viento sopla en ráfagas de 50 kilómetros por hora, pero el trabajo no se frena.\n\n"
            "Un techista experimentado carga una chapa metálica trapezoidal. De repente, una ráfaga entra por debajo de la lámina: el temido 'efecto vela'.\n\n"
            "La chapa actuó como un ala gigantesca y lo levantó de la pasarela. Llevaba arnés puesto, pero la cola de amarre colgaba suelta, sin conectar a la línea de vida.\n\n"
            "La caída libre desde ocho metros fue mortal.\n\n"
            "La lección de HSE es inflexible: con viento superior a 35 km/h se suspende el trabajo de techos, y el arnés solo salva vidas si está anclado al 100%.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an industrial warehouse rooftop repair site in gusty windy weather. "
            "Large trapezoidal corrugated metal roof sheets stacked near edge, safety harness and dual lanyard with shock absorber resting on an empty stainless steel lifeline cable, "
            "dramatic overcast stormy sky with dark moving clouds, industrial skyline in background, high depth of field, documentary realism, "
            "cinematic composition highlighting heights and wind hazards, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 23 de septiembre de 2015, en una obra de reacondicionamiento de cubiertas industriales, "
            "un operario techista calificado de cuarenta y dos años perdió la vida al precipitarse al vacío desde una altura de ocho metros. "
            "La combinación de condiciones climáticas adversas y la falsa sensación de seguridad por portar equipo sin anclar "
            "fueron los detonantes de una caída fatal.\n\n"
            "Durante aquella mañana, el clima presentaba ráfagas intermitentes de viento que superaban los cincuenta kilómetros por hora. "
            "A pesar de los avisos meteorológicos, el equipo continuó con el reemplazo de paneles de zinc deteriorados. "
            "El operario transportaba sobre su hombro una lámina sinusoidal de seis metros de longitud y casi un metro de ancho, "
            "caminando sobre una pasarela técnica angosta. Al alcanzar la cumbrera del techo, un vórtice de viento embolsó la superficie plana "
            "de la chapa generando un instantáneo y violento empuje aerodinámico, conocido en la industria como efecto vela.\n\n"
            "La fuerza ascensional desestabilizó al trabajador, arrancándole la chapa de las manos y arrojándolo fuera de la pasarela. "
            "Aunque llevaba puesto un arnés integral de cuerpo entero, el mosquetón de su cabo de vida colgaba enganchado "
            "a la propia anilla dorsal del arnés, sin haber sido conectado a la línea de vida horizontal de cable de acero instalada en el techo. "
            "El impacto contra el piso de hormigón de la nave le causó la muerte instantánea por politraumatismos.\n\n"
            "Este accidente ratifica dos premisas indeclinables del trabajo seguro en altura. "
            "Primero: las variables ambientales imponen límites operativos estrictos. El manejo manual de elementos laminares de gran superficie "
            "debe suspenderse de inmediato cuando la velocidad sostenida del viento supere los treinta y cinco a cuarenta kilómetros por hora, "
            "o existan ráfagas turbulentas impredecibles. Y segundo: el arnés es un sistema pasivo de retención que carece por completo de utilidad "
            "si no se mantiene la conexión activa y continua al cien por ciento a un punto de anclaje o línea de vida certificada.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "091",
        "fecha": "24 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-24",
        "expediente": "Expediente #091",
        "carpeta": "2019-09-24-corte-antebrazo-cuter-desembalaje",
        "titular": "EL FILO HACIA EL CUERPO: CORTE SEVERO EN LÍNEA DE DESEMBALAJE",
        "palabraResaltada": "FILO HACIA EL CUERPO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Sector de Recepción y Desembalaje de Mercaderías - 2019",
        "tipoRiesgo": "Herramientas Manuales / Cortes",
        "parrafos": [
            "El 24 de septiembre de 2019, una operaria de logística sufrió un corte profundo en el antebrazo con compromiso de la arteria radial y tendones flexores mientras abría cajas de cartón con zunchos plásticos.",
            "Utilizaba un cúter tradicional con traba rota y la hoja expuesta trabada hacia afuera. Para cortar un zuncho tenso, tiró de la herramienta con fuerza hacia su propio cuerpo y sin utilizar guantes de protección mecánica.",
            "Al seccionarse el fleje de golpe, la hoja continuó su trayectoria clavándose en su brazo izquierdo. La lección: cuchillas autorretráctiles obligatorias, técnica de corte hacia el exterior y guantes anticorte Nivel 4 o 5.",
        ],
        "puntosClave": [
            {"icono": "scissors", "titulo": "Cúters de seguridad autorretráctiles", "texto": "Sustituir trinchetas comunes por cuchillos de seguridad con resorte que retraen la hoja automáticamente al perder contacto con el material."},
            {"icono": "shield", "titulo": "Guantes anticorte certificados (EN 388)", "texto": "Uso obligatorio de guantes con fibra de polietileno de alto rendimiento (HPPE) o Kevlar con nivel mínimo D o E contra cortes severos."},
            {"icono": "hand", "titulo": "Técnica y dirección de corte segura", "texto": "Instruir al personal en cortar siempre hacia afuera, en dirección opuesta al cuerpo y con la mano libre ubicada detrás de la línea de corte."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: directrices de seguridad para herramientas de corte manual de OSHA 1910.242, norma europea EN 388 sobre guantes de protección mecánica y manuales de ergonomía industrial.",
        "guionReel": (
            "¿Cuántas veces viste abrir una caja tirando del cúter hacia el propio cuerpo?\n\n"
            "24 de septiembre de 2019. Área de recepción de un depósito. Una operaria corta zunchos de plástico tensos en palets de mercadería.\n\n"
            "Usa un cúter convencional de librería con la traba rota y la hoja totalmente expuesta. No lleva guantes anticorte.\n\n"
            "Tira con fuerza hacia su pecho para cortar un fleje rebelde. El plástico cede de golpe y la cuchilla vuela directo a su antebrazo izquierdo.\n\n"
            "Corte profundo, sección de tendones y compromiso de la arteria radial. Una hemorragia masiva que casi le cuesta la vida.\n\n"
            "La lección de HSE es básica pero vital: prohíbe los cúters comunes, exige cuchillas autorretráctiles, guantes anticorte y corta SIEMPRE hacia afuera.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic forensic photograph of an industrial packing and unboxing station. "
            "A heavy cardboard box with sliced thick plastic strapping bands, a modern ergonomic spring-loaded safety cutter resting beside a pair of high-visibility level D cut-resistant gloves, "
            "first aid kit in soft focus background, clean warehouse stainless steel workbench, high detail macro texture, professional HSE training presentation visual, "
            "dramatic studio lighting, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 24 de septiembre de 2019, en el sector de recepción y expedición de una importante planta logística, "
            "una tarea aparentemente inofensiva de desembalaje de mercadería derivó en una emergencia médica crítica. "
            "Una operaria de veintinueve años sufrió un corte lacerante profundo en la cara anterior de su antebrazo izquierdo, "
            "con sección de tres tendones flexores y perforación de la arteria radial.\n\n"
            "El análisis ergonómico y operativo del accidente puso al descubierto hábitos de trabajo peligrosamente arraigados. "
            "La trabajadora empleaba una trincheta o cúter estándar de hoja segmentada descartable, cuya pestaña de bloqueo "
            "estaba rota y fijada con cinta adhesiva, manteniendo el filo extendido más de cuatro centímetros. "
            "Para seccionar un zuncho de polipropileno altamente tensado que envolvía un pallet, la operaria posicionó su mano izquierda "
            "sosteniendo el fleje y tiró de la cuchilla con fuerza en dirección ascendente hacia su propio torso, sin utilizar guantes de protección.\n\n"
            "Al cortarse el plástico bruscamente por fatiga mecánica, la resistencia que ofrecía la pieza desapareció en un instante. "
            "La inercia del movimiento proyectó la hoja afilada sin control contra el brazo de apoyo que sujetaba la carga. "
            "La hoja penetró profundamente en el tejido blando, generando una profusa hemorragia arterial que demandó la aplicación urgente "
            "de un torniquete por parte de brigadistas de planta antes de su traslado quirúrgico de urgencia.\n\n"
            "Este incidente impulsó la erradicación total de herramientas de corte improvisadas en la industria moderna. "
            "La prevención eficaz en operaciones de desembalaje exige tres medidas intransigibles: "
            "la sustitución obligatoria de cúters convencionales por cuchillos de seguridad con sistema inteligente de autorretracción de hoja o guías ocultas de corte, "
            "la provisión y uso indiscutible de guantes de protección mecánica certificados bajo norma EN 388 con resistencia al corte de nivel cuatro o superior, "
            "y la capacitación continua en técnica postural para garantizar que el filo viaje siempre en sentido opuesto al cuerpo y las manos del operador.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "092",
        "fecha": "25 SEPTIEMBRE",
        "fechaPublicacion": "2026-09-25",
        "expediente": "Expediente #092",
        "carpeta": "1998-09-25-explosion-planta-gas-esso-longford",
        "titular": "FRACTURA A MENOS 48 GRADOS: EL DESASTRE DE ESSO LONGFORD",
        "palabraResaltada": "ESSO LONGFORD",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta de Procesamiento de Gas de Esso, Longford, Victoria, Australia - 1998",
        "tipoRiesgo": "Seguridad de Procesos (Oil & Gas)",
        "parrafos": [
            "El 25 de septiembre de 1998, una colosal explosión e incendio en la planta de gas Esso en Longford, Australia, causó la muerte de dos operarios y dejó sin gas a toda la provincia de Victoria durante dos semanas.",
            "Una falla en una bomba provocó la pérdida de flujo del aceite de calefacción en la unidad de absorción. Sin calor, el gas líquido continuó evaporándose, enfriando el intercambiador de calor de acero al carbono hasta alcanzar los -48 °C.",
            "Sin percatarse de que el metal se había vuelto frágil como el vidrio, los operadores reinyectaron aceite caliente a 230 °C. El choque térmico provocó la fractura frágil instantánea del recipiente, liberando gas que detonó al tocar los hornos.",
        ],
        "puntosClave": [
            {"icono": "thermometer-snowflake", "titulo": "Temperatura mínima de diseño del metal (MDMT)", "texto": "Respetar estrictamente los límites criogénicos del acero al carbono; por debajo de la temperatura de transición dúctil-frágil, cualquier impacto o choque térmico fractura el metal."},
            {"icono": "file-text", "titulo": "Procedimientos operativos ante pérdida de calor", "texto": "Capacitar a los operadores en diagramas de fase y prohibir la reintroducción de fluidos calientes en equipos subenfriados sin un protocolo gradual y presurización controlada."},
            {"icono": "shield-alert", "titulo": "Gestión del cambio organizativo y presencia de ingeniería", "texto": "La reducción de ingenieros de proceso en planta limitó la comprensión de la termodinámica del incidente; la experiencia técnica in situ es insustituible."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe oficial de la Comisión Real de Investigación del Gobierno de Victoria sobre el accidente de Esso Longford (Hopkins, Andrew - 'Lessons from Longford') y normas API 579 sobre aptitud para el servicio (Fitness-For-Service).",
        "guionReel": (
            "¿Sabías que el acero de un tanque de gas puede quebrarse como si fuera de cristal si se enfría demasiado?\n\n"
            "25 de septiembre de 1998. Planta de gas Esso Longford en Australia. Una falla detuvo la bomba de aceite caliente que calefaccionaba un intercambiador de calor.\n\n"
            "Sin calor, el gas líquido evaporándose congeló el recipiente de acero al carbono a menos 48 grados Celsius. A esa temperatura, el acero pierde toda ductilidad y se vuelve frágil.\n\n"
            "Los operadores, sin ingenieros en planta y sin entender el fenómeno criogénico, decidieron reinyectar de golpe aceite hirviendo a 230 grados.\n\n"
            "El choque térmico partió el tanque en dos como una taza de porcelana. Miles de toneladas de gas detonaron en una inmensa bola de fuego.\n\n"
            "Murieron dos operarios y toda la provincia se quedó sin gas dos semanas. La termodinámica no perdona la falta de capacitación.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic cinematic photograph of the massive industrial gas plant explosion and fire at Esso Longford in 1998. "
            "Twisted fractured cryogenic heat exchanger vessels frosted with rime ice near burning gas pipeline flares, "
            "towering black smoke plume against an overcast Australian industrial sky, emergency shutdown control room boards flashing red warnings, "
            "forensic chemical process safety documentary aesthetic, wide angle, photorealistic metal fractures, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 25 de septiembre de 1998, a las doce y veintiséis del mediodía, una catastrófica explosión sacudió la planta de procesamiento "
            "de gas de Esso en Longford, en el estado australiano de Victoria. La explosión y el pavoroso incendio resultante "
            "cobraron la vida de dos operarios, dejaron a ocho heridos de gravedad y paralizaron el suministro de gas natural "
            "a más de un millón y medio de hogares y miles de industrias durante casi tres semanas, "
            "provocando pérdidas económicas multimillonarias.\n\n"
            "La exhaustiva Comisión Real de Investigación expuso un encadenamiento de fallas termodinámicas, de diseño y organizacionales. "
            "Cuatro horas antes del siniestro, una bomba de recirculación de aceite térmico sufrió una falla mecánica. "
            "Este aceite caliente suministraba calor a los reboilers de la torre de absorción para separar hidrocarburos pesados. "
            "Al cortarse el flujo de calor pero continuar la entrada de condensados de gas licuado, "
            "el líquido continuó auto-refrigerándose por evaporación flash. "
            "La temperatura del intercambiador de calor GP novecientos cinco descendió drásticamente hasta alcanzar los menos cuarenta y ocho grados Celsius, "
            "cubriendo el equipo de una densa capa de hielo blanco.\n\n"
            "El recipiente estaba fabricado con acero al carbono convencional, cuya temperatura mínima de diseño para evitar fractura frágil "
            "era sustancialmente superior. Por debajo de esa temperatura crítica, el metal sufre una transición de estado dúctil a quebradizo, "
            "comportándose como vidrio templado. Los operadores del panel, desorientados por una avalancha de alarmas incesantes "
            "y sin contar con el respaldo de ingenieros de proceso en la planta —quienes habían sido reubicados en oficinas centrales en Melbourne "
            "tras una reestructuración corporativa—, decidieron restablecer el flujo de aceite caliente a doscientos treinta grados centígrados.\n\n"
            "El colosal choque térmico generó tensiones mecánicas brutales que el acero congelado no pudo disipar. "
            "El intercambiador se quebró violentamente a lo largo de su soldadura longitudinal, liberando instantáneamente "
            "una nube colosal de gas hidrocarburo vaporizado. La nube encontró ignición en los quemadores de los calentadores contiguos, "
            "desatando una explosión masiva que pulverizó la unidad.\n\n"
            "Las 'Lecciones de Longford', analizadas magistralmente por el profesor Andrew Hopkins, "
            "son hoy cátedra obligatoria en Seguridad de Procesos a nivel global. Demostraron que la Gestión del Cambio Organizacional "
            "es tan crítica como la técnica: nunca debe alejarse el conocimiento ingenieril del terreno operativo. "
            "Asimismo, consagraron la obligatoriedad de respetar los límites criogénicos de los materiales (MDMT), "
            "diseñar enclavamientos que impidan calentar recipientes subenfriados sin despresurización previa, "
            "y gestionar activamente la saturación de alarmas en consolas de control para evitar que los operadores tomen decisiones a ciegas.\n\n"
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

    # Patrón de fondo industrial
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=(16, 36, 44), width=1)
    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill=(16, 36, 44), width=1)

    # Viñeta oscura perimetral
    for i in range(120):
        alpha = int(i * 1.5)
        color = (5, 16, 20)
        draw.rectangle([i, i, width - i, height - i], outline=color, width=1)

    # Cargar fuentes
    try:
        font_title = ImageFont.truetype("arialbd.ttf", 62)
        font_sub = ImageFont.truetype("arial.ttf", 34)
        font_meta = ImageFont.truetype("arialbd.ttf", 26)
        font_badge = ImageFont.truetype("arialbd.ttf", 22)
    except:
        font_title = font_sub = font_meta = font_badge = ImageFont.load_default()

    # Badges
    badge_x = 100
    badge_y = 100
    draw.rectangle([badge_x, badge_y, badge_x + 380, badge_y + 54], fill=(25, 211, 230, 40), outline=(25, 211, 230), width=2)
    draw.text((badge_x + 18, badge_y + 12), f"{historia['fecha']} · {historia['expediente']}", font=font_badge, fill=(25, 211, 230))

    draw.rectangle([width - 550, badge_y, width - 100, badge_y + 54], fill=(255, 77, 56, 40), outline=(255, 77, 56), width=2)
    draw.text((width - 530, badge_y + 12), historia['tipoRiesgo'][:30], font=font_badge, fill=(255, 120, 100))

    # Recuadro central
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

    # Pie institucional
    draw.line([100, height - 120, width - 100, height - 120], fill=(151, 231, 255, 40), width=1)
    draw.text((140, height - 90), "FOCUS HSE · ARCHIVO HISTÓRICO DE SEGURIDAD", font=font_meta, fill=(25, 211, 230))
    draw.text((width - 480, height - 90), "LA SEGURIDAD ESTÁ EN LOS DETALLES", font=font_meta, fill=(159, 184, 192))

    img.save(output_path, "PNG")

def inyectar_en_index_html(historias_procesadas):
    """Inyecta las historias del Lote 8 en index.html antes del cierre del array historias."""
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

    print("\n✓ index.html actualizado exitosamente con los 10 nuevos expedientes (#083 a #092).")
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
    print("Iniciando motor Kokoro para Lote 8 (#083 a #092)...")
    kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

    print("\n" + "=" * 55)
    print("Iniciando procesamiento de 10 historias del Lote 8 (#083 a #092)")
    print("=" * 55 + "\n")

    historias_procesadas = []

    for h in LOTE_8_DATA:
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

    print("\n🎉 ¡LOTE 8 COMPLETADO AL 100%! (10 historias procesadas)\n")

if __name__ == "__main__":
    main()
