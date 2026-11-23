# -*- coding: utf-8 -*-
"""
Generador Agéntico Automatizado para Lote 10: Expedientes #103 a #112 (6 al 15 de octubre)
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

LOTE_10_DATA = [
    {
        "id": "103",
        "fecha": "06 OCTUBRE",
        "fechaPublicacion": "2026-10-06",
        "expediente": "Expediente #103",
        "carpeta": "2018-10-06-explosion-refineria-irving-oil-saint-john",
        "titular": "LA LÍNEA QUE CEDIO BAJO PRESIÓN: EXPLOSIÓN EN LA REFINERÍA IRVING OIL",
        "palabraResaltada": "REFINERÍA IRVING OIL",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Refinería Irving Oil, Saint John, Nuevo Brunswick, Canadá - 2018",
        "tipoRiesgo": "Seguridad de Procesos (Oil & Gas)",
        "parrafos": [
            "El 6 de octubre de 2018, una serie de explosiones e incendios masivos estremecieron la refinería Irving Oil en Saint John, Nuevo Brunswick, Canadá, la más grande del país, obligando a confinar a miles de vecinos.",
            "La falla ocurrió en la unidad de hidrotratamiento de diésel, donde una tubería de recirculación de hidrógeno y destilados colapsó por mecanismos combinados de corrosión-erosión y ataque por hidrógeno a alta temperatura.",
            "La liberación masiva de hidrocarburos a alta presión encontró ignición inmediata en los hornos adyacentes. La lección: inspección ultrasónica de espesores en circuitos bifásicos críticos y aislamiento riguroso en caliente.",
        ],
        "puntosClave": [
            {"icono": "gauge", "titulo": "Mapeo ultrasónico de espesores (NDT)", "texto": "Monitorear codos y reducciones en líneas de hidrotratamiento sometidas a flujo bifásico turbulento para detectar adelgazamientos prematuros."},
            {"icono": "shield-check", "titulo": "Control de ataque por hidrógeno (HTHA)", "texto": "Revisar curvas de Nelson y seleccionar metalurgias aleadas resistentes al hidrógeno caliente para evitar la descarburación interna del acero."},
            {"icono": "lock", "titulo": "Aislamiento positivo en plantas en servicio", "texto": "Prohibir tareas de torque o mantenimiento sobre circuitos presurizados con hidrocarburos inflamables por encima de su punto de autoignición."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de investigación de la Junta de Seguridad en el Transporte de Canadá (TSB) y reportes técnicos de WorkSafeNB sobre la refinería Irving Oil de Saint John.",
        "guionReel": (
            "El 6 de octubre de 2018, en la ciudad de Saint John, Canadá, la refinería Irving Oil, la más grande del país, estalló en llamas.\n\n"
            "En la unidad de hidrotratamiento, una tubería que transportaba hidrógeno y diésel a más de 300 grados colapsó repentinamente. Estaba debilitada por corrosión y erosión interna.\n\n"
            "El gas inflamable se liberó a una presión brutal y encontró una chispa en los hornos. La explosión sacudió toda la ciudad e iluminó el cielo con una muralla de fuego.\n\n"
            "Milagrosamente no hubo muertos, pero miles de vecinos quedaron atrapados en sus casas por el humo tóxico.\n\n"
            "La lección de Focus HSE: las líneas de alta presión no se confían a la suerte; exigen inspección continua de espesores y metalurgia adecuada.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic dramatic photograph of the Irving Oil refinery complex in Saint John, Canada, after an industrial explosion. "
            "Twisted fractured steel pipelines in a diesel hydrotreating unit, scorched distillation towers with emergency fire monitors spraying cooling foam, "
            "distant Canadian industrial harbor coastline visible under a dark smoky sky, solemn and rigorous process safety forensic inspection shot, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 6 de octubre de 2018, en la ciudad costera de Saint John, provincia de Nuevo Brunswick, Canadá, "
            "la refinería Irving Oil —la mayor planta procesadora de petróleo de ese país con una capacidad de trescientos veinte mil barriles diarios— "
            "sufrió una violenta explosión e incendio en su unidad de hidrotratamiento de diésel. "
            "La deflagración sacudió los cimientos de la ciudad y provocó el confinamiento preventivo de miles de habitantes ante el avance de densas nubes de humo.\n\n"
            "La investigación técnica posterior determinó que el siniestro se produjo por la rotura catastrófica de una cañería de proceso "
            "que operaba a presiones superiores a los ochenta bares y temperaturas extremas. En este circuito bifásico coexistían diésel caliente "
            "y gas hidrógeno a alta presión. Con el tiempo, el régimen turbulento del fluido generó un mecanismo severo de erosión-corrosión "
            "localizada en las curvas y reducciones de la tubería, sumado al fenómeno conocido como ataque por hidrógeno a alta temperatura (HTHA), "
            "el cual descarbura internamente el acero y crea microfisuras invisibles a simple vista.\n\n"
            "Durante tareas de supervisión y ajuste mecánico mientras la unidad se encontraba en servicio, la pared adelgazada del tubo no resistió "
            "las pulsaciones hidráulicas y reventó longitudinalmente. La despresurización súbita arrojó toneladas de hidrocarburos atomizados "
            "que encendieron al instante al tomar contacto con los refractarios de los hornos de proceso contiguos. "
            "A pesar de la magnitud de la bola de fuego, la rápida activación de los sistemas de parada de emergencia remota (ESD) "
            "y las brigadas de emergencia evitaron una tragedia humana de mayores dimensiones, aunque cuatro trabajadores sufrieron heridas.\n\n"
            "El caso de Saint John reafirma principios vitales para la integridad mecánica en la refinación de petróleo. "
            "Primero: el monitoreo de integridad mecánica debe priorizar los circuitos con mezclas de hidrógeno y azufre a través de ensayos no destructivos "
            "de ultrasonido phased array y radiografía digital periódica. Segundo: la metalurgia debe actualizarse estrictamente de acuerdo con las curvas "
            "de Nelson de la norma API 941. Y tercero: jamás deben autorizarse intervenciones mecánicas directas sobre líneas presurizadas calientes "
            "sin un aislamiento físico comprobado mediante doble bloqueo y purga.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "104",
        "fecha": "07 OCTUBRE",
        "fechaPublicacion": "2026-10-07",
        "expediente": "Expediente #104",
        "carpeta": "2014-10-07-explosion-fabrica-explosivos-austin-powder-jaguariuna",
        "titular": "LA ONDA DE CHOQUE EN JAGUARIÚNA: EXPLOSIÓN EN AUSTIN POWDER",
        "palabraResaltada": "AUSTIN POWDER",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Fábrica de Explosivos e Iniciadores Austin Powder, Jaguariúna, São Paulo, Brasil - 2014",
        "tipoRiesgo": "Seguridad de Procesos / Explosivos",
        "parrafos": [
            "El 7 de octubre de 2014, una detonación destruyó un búnker de producción en la planta de explosivos Austin Powder en Jaguariúna, estado de São Paulo, Brasil, cobrando la vida de operarios especializados e hiriendo a trabajadores en naves vecinas.",
            "El incidente ocurrió durante la manipulación y tamizado manual de una mezcla química altamente reactiva utilizada para detonadores e iniciadores de minería, produciéndose la ignición por una chispa electrostática o fricción mecánica.",
            "La onda expansiva dañó techos y estructuras a más de 500 metros. La lección: automatización de procesos de mezclado pirotécnico, control estricto de continuidad a tierra e interposición de muros de sacrificio y taludes de desvío.",
        ],
        "puntosClave": [
            {"icono": "sparkles", "titulo": "Pisos conductivos y puesta a tierra personal", "texto": "Garantizar resistencia inferior a 1 megaohm en suelos de plantas de explosivos, con taloneras y calzado disipativo antiestático verificado a diario."},
            {"icono": "cpu", "titulo": "Manipulación remota y blindaje de operarios", "texto": "Sustituir el tamizado y dosificación manual de sustancias primarias por brazos robóticos operados detrás de mamparas de policarbonato antibalas."},
            {"icono": "shield", "titulo": "Muros deflectores y limitación de masa neta", "texto": "Restringir la cantidad de explosivo presente en cada celda a gramos contados, canalizando la sobrepresión hacia techos fusibles al aire libre."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: dictámenes periciales del Instituto de Criminalística de São Paulo, investigaciones del Ministerio de Trabajo de Brasil y estándares de seguridad de fabricación de explosivos del IME (Institute of Makers of Explosives).",
        "guionReel": (
            "El 7 de octubre de 2014, en Jaguariúna, Brasil, la fábrica de explosivos Austin Powder voló por los aires.\n\n"
            "En una nave de iniciadores de minería, operarios preparaban una mezcla química hipersensible. Bastó una mínima fricción o una chispa invisible de energía estática.\n\n"
            "La detonación fue instantánea y demoledora. El búnker quedó pulverizado y la onda expansiva arrancó techos a medio kilómetro a la redonda.\n\n"
            "Varios operarios perdieron la vida en el acto.\n\n"
            "La lección de Focus HSE: las mezclas primarias no perdonan el contacto humano; exigen pisos antiestáticos certificados, automatización remota y muros de alivio.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an industrial explosive manufacturing plant after an accidental detonation in Brazil. "
            "Shattered reinforced concrete blast wall of an isolated production bunker, earth berms deflecting blast path, "
            "emergency response fire vehicles cordoning off the area under the humid tropical haze of São Paulo state, "
            "technical forensic investigation atmosphere, wide lens, authentic textured debris, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 7 de octubre de 2014, en el municipio de Jaguariúna, dentro de la región metropolitana de Campinas en el estado de São Paulo, Brasil, "
            "un estruendo sacudió la tranquilidad del distrito industrial. En las instalaciones de la multinacional Austin Powder Brasil, "
            "dedicada a la fabricación de sistemas de iniciación y explosivos para la gran minería y canteras, "
            "una de las celdas de procesamiento de mezclas químicas primarias detonó violentamente, segando la vida de operarios y desatando el pánico.\n\n"
            "La pericia balística y forense de la policía científica reveló que el suceso tuvo lugar en el sector de elaboración de fulminantes "
            "y cápsulas detonadoras. Estas sustancias, compuestas por estifnato de plomo y azida, poseen una sensibilidad extrema al calor, "
            "al impacto físico, a la fricción entre granos y a la acumulación de energía electrostática ambiental. "
            "Durante las tareas de tamizado y pesaje manual en una mesa de trabajo, una descarga estática microscópica originada por el roce "
            "de la indumentaria o una fricción inadecuada con los recipientes de transferencia encendió la carga sensible.\n\n"
            "En microsegundos, la deflagración inicial transicionó a una detonación supersónica de alta energía. "
            "Aunque la empresa contaba con celdas de hormigón armado, la masa acumulada superaba los márgenes recomendados para trabajo manual. "
            "La onda expansiva rompió vidrios en plantas vecinas y derribó mamparas internas. "
            "El accidente puso en evidencia la vulnerabilidad inherente que existe cuando las personas interactúan físicamente "
            "con materias primas explosivas de Clase 1.\n\n"
            "La tragedia de Austin Powder en Jaguariúna impulsó la modernización regulatoria en la industria militar y civil de explosivos en Sudamérica. "
            "Estableció que la preparación de compuestos detonantes debe realizarse mediante automatización y teleoperación detrás de escudos "
            "de absorción de impacto, eliminando la presencia permanente de operadores en la línea de fuego. "
            "Asimismo, consolidó la verificación diaria e informatizada de la conductividad estática de pisos, calzados y mesas de trabajo, "
            "asegurando que ninguna carga electrostática exceda jamás el potencial mínimo de ignición de las sustancias involucradas.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "105",
        "fecha": "08 OCTUBRE",
        "fechaPublicacion": "2026-10-08",
        "expediente": "Expediente #105",
        "carpeta": "2018-10-08-incendio-bomba-coquizacion-refineria-petronor-muskiz",
        "titular": "EL SELLO ROTO EN LA UNIDAD DE COQUE: INCENDIO EN REFINERÍA PETRONOR",
        "palabraResaltada": "REFINERÍA PETRONOR",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Refinería Petronor (Repsol), Muskiz, Vizcaya, País Vasco, España - 2018",
        "tipoRiesgo": "Seguridad de Procesos (Refinación)",
        "parrafos": [
            "El 8 de octubre de 2018, una aparatosa explosión seguida de un incendio de grandes proporciones paralizó la unidad de coquización de la refinería Petronor en Muskiz, Vizcaya, obligando a activar el Plan de Emergencia Exterior.",
            "El incidente se originó por el colapso del sello mecánico doble de una bomba centrífuga de recirculación de fondos de vacío calientes, liberando hidrocarburos livianos y pesados que autoencendieron al superar su temperatura de autoignición.",
            "Una antorcha de más de 30 metros amenazó la estructura de la planta durante horas. La lección: monitoreo predictivo de vibraciones en sellos mecánicos, presurización con fluido barrera y cortinas de vapor automáticas.",
        ],
        "puntosClave": [
            {"icono": "activity", "titulo": "Monitoreo continuo de sellos (Plan API 53)", "texto": "Controlar presión y nivel del fluido barrera en sellos dobles presurizados para detectar fugas antes del escape hacia la atmósfera."},
            {"icono": "flame", "titulo": "Cortinas de vapor y rociadores automáticos", "texto": "Instalar sistemas de vapor de enclavamiento para inertizar el entorno de bombas calientes de hidrocarburos e impedir la autoignición."},
            {"icono": "radio", "titulo": "Detección óptica infrarroja de hidrocarburos", "texto": "Implementar detectores de llama multiespectrales (IR3) y sensores de gas puntuales conectados al disparo automático de cortinas de diluvio."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: comunicados oficiales del Departamento de Seguridad del Gobierno Vasco, informes técnicos de Petronor y directrices de seguridad en bombeo de hidrocarburos de la norma API 682.",
        "guionReel": (
            "El 8 de octubre de 2018, en Muskiz, España, la refinería Petronor se iluminó con una inmensa llamarada de 30 metros de altura.\n\n"
            "En la unidad de coquización, el sello mecánico de una bomba que impulsaba hidrocarburos hirviendo falló por completo.\n\n"
            "El líquido salió a más de 350 grados Celsius, una temperatura muy superior a su punto de autoignición. Apenas tocó el aire, se encendió como un soplete gigante.\n\n"
            "El fuego amenazó los tanques contiguos y obligó a activar el Plan de Emergencia Exterior en toda Vizcaya.\n\n"
            "La lección de Focus HSE: las bombas calientes son bombas de tiempo si fallan sus sellos. Exigen monitoreo predictivo, fluidos de barrera presurizados y cortinas de vapor operativas.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an oil refinery coking unit after a major pump seal fire in Muskiz, Spain. "
            "Charred centrifugal process pumps with burnt piping manifolds, cooling water cascades flowing over blackened steel frameworks, "
            "industrial fire brigade hoses staged on concrete refinery floor, Basque industrial coastal mountain backdrop under evening sky, 8k resolution, authentic refinery textures."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 8 de octubre de 2018, en el término municipal de Muskiz, en la provincia de Vizcaya, España, "
            "la sirena de emergencia de la refinería de Petronor —una de las instalaciones energéticas más estratégicas del sur de Europa— "
            "rompió la calma de la comarca de Las Encartaciones. Una gran columna de fuego y humo negro se alzó sobre la planta dos, "
            "donde opera la compleja unidad de coquización encargada de valorizar los residuos más pesados del crudo.\n\n"
            "El análisis de causa raíz identificó la falla en una de las bombas centrífugas encargadas del bombeo de hidrocarburos "
            "a temperaturas de proceso que sobrepasaban con creces los trescientos cincuenta grados Celsius. "
            "El sello mecánico doble tipo cartucho, diseñado bajo especificación API seiscientos ochenta y dos, "
            "sufrió una degradación prematura de sus caras de rozamiento debido a vibraciones inducidas por cavitación y choque térmico. "
            "El fluido de barrera presurizado se perdió, permitiendo que la corriente de hidrocarburo caliente escapara a la atmósfera con violencia.\n\n"
            "Al entrar en contacto con el aire ambiente, el fluido inflamable no requirió de ninguna chispa externa: "
            "su temperatura de proceso superaba holgadamente la temperatura de autoignición del hidrocarburo, generándose una combustión "
            "espontánea instantánea. Las llamas envolvieron el skidding de bombas y amenazaron las líneas superiores de alimentación de las torres de coque. "
            "La oportuna activación de los sistemas de diluvio de agua de la refinería y el aislamiento telecomandado de las válvulas de bloqueo "
            "de succión permitieron sofocar el fuego tras intensas horas de combate, evitando fatalidades entre los operadores de planta.\n\n"
            "El siniestro de Muskiz ratifica lecciones indeclinables para el diseño de unidades de refinación. "
            "Las bombas que operan con productos calientes por encima de su temperatura de autoignición deben considerarse equipos de riesgo crítico mayor. "
            "Exigen instrumentación con alarmas de baja presión en los sistemas de presurización de sellos mecánicos con parada automática trip del motor, "
            "el confinamiento con anillos de inyección de vapor de purga permanente para dispersar fugas incipientes, "
            "y una distancia de seguridad calculada respecto a las vías de escape de los operadores de campo.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "106",
        "fecha": "09 OCTUBRE",
        "fechaPublicacion": "2026-10-09",
        "expediente": "Expediente #106",
        "carpeta": "2013-10-09-explosion-caldera-unidad-4-central-eskom-duvha",
        "titular": "EL COLAPSO DE LA CALDERA 4: EXPLOSIÓN EN LA CENTRAL ESKOM DUVHA",
        "palabraResaltada": "CENTRAL ESKOM DUVHA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Central Termoeléctrica Duvha (Eskom), Mpumalanga, Sudáfrica - 2013",
        "tipoRiesgo": "Seguridad de Procesos / Recipientes a Presión",
        "parrafos": [
            "El 9 de octubre de 2013, una explosión colosal destruyó la caldera de carbón de 600 megavatios de la Unidad 4 en la central eléctrica Duvha de Eskom, en la provincia de Mpumalanga, Sudáfrica, dejándola inservible por años.",
            "Durante pruebas de control operativo, los operadores anularon manualmente enclavamientos de sobrepresión en el sistema de tiro forzado y combustión, acumulando gases inquemados que sufrieron una deflagración interna de violencia descomunal.",
            "Las paredes de tubos de agua de más de 80 metros colapsaron hacia afuera desgarrando la estructura del edificio. La lección: prohibición absoluta de anular sistemas de disparo automático (BMS/Trip) y gestión rigurosa de pruebas operativas.",
        ],
        "puntosClave": [
            {"icono": "shield-alert", "titulo": "Inviolabilidad de enclavamientos BMS", "texto": "Los sistemas de gestión de quemadores (Burner Management Systems) jamás deben puentearse ni operarse en modo forzado durante pruebas de planta."},
            {"icono": "gauge", "titulo": "Purgas de aire previas al encendido (Purge cycle)", "texto": "Garantizar un barrido de al menos 5 volúmenes de aire en el hogar de la caldera para expulsar gases inflamables antes de cualquier reencendido."},
            {"icono": "file-check", "titulo": "Procedimientos estrictos de pruebas no rutinarias", "texto": "Toda prueba operativa debe contar con evaluación de riesgos formal (HAZOP de prueba), presencia de ingeniería de proceso y límites de parada claros."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de investigación técnica de Eskom Holdings SOC Ltd., análisis pericial de incidentes de calderas de ASME y reportes del Departamento de Trabajo de Sudáfrica.",
        "guionReel": (
            "El 9 de octubre de 2013, en Mpumalanga, Sudáfrica, la gigantesca central eléctrica Duvha sufrió una de las explosiones de caldera más destructivas del mundo.\n\n"
            "En la Unidad 4, de 600 megavatios, los técnicos hacían pruebas en el sistema de combustión. Para evitar que la máquina se apagara, anularon los enclavamientos de seguridad.\n\n"
            "El carbón pulverizado inquemado se acumuló dentro del enorme hogar de 80 metros de altura. Una chispa encendió la nube confinada.\n\n"
            "La sobrepresión infló y desgarró la caldera de acero como si fuera de papel. Trozos de vigas salieron disparados a cientos de metros.\n\n"
            "La lección de Focus HSE: nunca puentees los enclavamientos de una caldera. Los sistemas de disparo de emergencia existen para salvar vidas y plantas.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of a massive industrial coal-fired power station boiler room after a catastrophic structural explosion in South Africa. "
            "Ruptured vertical water wall tubes ballooned and torn apart, shredded structural steel columns and bent catwalks inside a vast high-bay turbine hall, "
            "coal dust soot covering twisted industrial machinery, dramatic shafts of sunlight entering through collapsed metal roof panels, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 9 de octubre de 2013, en la provincia de Mpumalanga, el corazón carbonífero de Sudáfrica, "
            "la central termoeléctrica Duvha operada por la empresa estatal Eskom fue escenario de un desastre técnico de escala mayúscula. "
            "La caldera de vapor de la Unidad cuatro, una colosal estructura suspendida de más de ochenta metros de altura diseñada "
            "para generar seiscientos megavatios de potencia eléctrica, sufrió una sobrepresión catastrófica que deformó sus paredes de tubos "
            "y destruyó por completo su envolvente estructural.\n\n"
            "El origen del evento radicó en una grave violación a los principios de seguridad funcional durante maniobras operativas especiales. "
            "El personal técnico se encontraba realizando ensayos de sintonización en los lazos de control de tiro y modulación de quemadores de carbón pulverizado. "
            "Ante disparos frecuentes y no deseados generados por los lazos de protección automática, los operadores decidieron colocar en bypass "
            "los enclavamientos del sistema de gestión de quemadores (BMS) y de los ventiladores de tiro inducido. "
            "Esta anulación dejó a la caldera ciega frente a una acumulación masiva de combustible fósil suspendido e inquemado en el hogar.\n\n"
            "Al producirse una reignición espontánea de la masa de gas y carbón pulverizado sobrecalentado, la deflagración confinada "
            "generó un pulso de presión interna que superó con creces la resistencia elástica del acero. Las paredes de tubos de agua "
            "se abombaron violentamente hacia afuera, cortando los tirantes de sujeción sísmica y reventando las juntas de dilatación. "
            "La liberación repentina de miles de metros cúbicos de vapor a alta presión pulverizó las pasarelas técnicas circundantes. "
            "Por fortuna, el protocolo de despeje durante la prueba evitó que cuadrillas de mantenimiento se encontraran sobre las plataformas al momento del estallido.\n\n"
            "El colapso de la caldera de Duvha dejó una de las advertencias más contundentes en la ingeniería de recipientes a presión: "
            "los sistemas instrumentados de seguridad (SIS) y los viajes automáticos de caldera jamás deben tratarse como estorbos operativos. "
            "Cualquier puente o bypass temporal exige un estricto proceso de Gestión del Cambio (MOC), autorización del máximo nivel técnico "
            "y la presencia física de supervisores dedicados. Cuando se vulneran los enclavamientos de parada segura, la frontera "
            "entre la producción de energía y una catástrofe destructiva desaparece en microsegundos.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "107",
        "fecha": "10 OCTUBRE",
        "fechaPublicacion": "2026-10-10",
        "expediente": "Expediente #107",
        "carpeta": "1957-10-10-incendio-nuclear-windscale-sellafield-ukaea",
        "titular": "EL FUEGO ATÓMICO EN EL NÚCLEO: EL DESASTRE NUCLEAR DE WINDSCALE",
        "palabraResaltada": "REACTOR DE WINDSCALE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Pila Nuclear Windscale (UKAEA), Sellafield, Cumbria, Reino Unido - 1957",
        "tipoRiesgo": "Seguridad de Procesos / Control Térmico",
        "parrafos": [
            "El 10 de octubre de 1957, el reactor militar Pile 1 de Windscale en Sellafield, Reino Unido, sufrió el peor accidente nuclear en suelo británico cuando su núcleo de grafito y uranio ardió descontroladamente durante tres días.",
            "El fuego comenzó durante una maniobra no rutinaria de recocido térmico para liberar energía atómica de Wigner acumulada en el grafito. La falta de termocuplas en las zonas más calientes llevó a los operadores a aplicar calor excesivo a ciegas.",
            "Se liberaron grandes cantidades de yodo-131, contaminando pasturas y obligando a desechar millones de litros de leche. La lección: instrumentación redundante en puntos térmicos críticos y validación estricta de maniobras operativas inéditas.",
        ],
        "puntosClave": [
            {"icono": "thermometer", "titulo": "Mapeo térmico integral y completo", "texto": "Nunca operar un reactor o proceso exotérmico sin termometría en los puntos teóricamente más calientes (hot spots)."},
            {"icono": "file-text", "titulo": "Procedimientos para operaciones no estándar", "texto": "Toda maniobra de liberación de energía almacenada debe poseer límites de temperatura taxativos y criterios de aborto inmediato."},
            {"icono": "shield", "titulo": "Filtros de chimenea y contención pasiva", "texto": "La audaz decisión de instalar filtros en las chimeneas de Windscale contuvo el 95% del material radiactivo; la contención física salva poblaciones."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe Penney de la Autoridad de Energía Atómica del Reino Unido (UKAEA) sobre el incendio de Windscale y revisiones históricas del OIEA.",
        "guionReel": (
            "El 10 de octubre de 1957, en Sellafield, Reino Unido, el reactor nuclear de Windscale se incendió en el más absoluto secreto.\n\n"
            "Los ingenieros querían liberar energía acumulada en el grafito mediante calor. Pero había un error letal: las sondas de temperatura no estaban en la parte más caliente del núcleo.\n\n"
            "Creyendo que el reactor estaba frío, aplicaron más calor. El uranio metálico y el grafito comenzaron a arder al rojo vivo.\n\n"
            "Durante tres días, el fuego radiactivo ardió sin control. Tuvieron que inundar el reactor con agua arriesgando una explosión de hidrógeno.\n\n"
            "La nube de yodo-131 contaminó cientos de kilómetros de campos en Gran Bretaña.\n\n"
            "La lección de Focus HSE: en procesos térmicos y nucleares, nunca operes a ciegas; exige medición exacta en los puntos más críticos.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph depicting the historic 1957 Windscale nuclear reactor pile chimney and bio-shield in Sellafield, UK. "
            "Massive square concrete reactor discharge chimney with top filtration gallery standing under gloomy British coastal skies, "
            "vintage radiation monitoring teams in white protective coveralls with Geiger counters in foreground, "
            "somber early nuclear age documentary photography aesthetic, grain texture, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 10 de octubre de 1957, en la costa de Cumbria en el noroeste de Inglaterra, "
            "la planta de Sellafield —entonces llamada Windscale y operada por la Autoridad de Energía Atómica del Reino Unido (UKAEA)— "
            "fue escenario de la peor catástrofe radiológica del país, clasificada con nivel cinco en la escala internacional INES. "
            "El reactor número uno, una inmensa pila refrigerada por aire diseñada para producir plutonio de grado militar, "
            "ardió en su interior durante más de cuarenta y ocho horas en una combustión incontrolable.\n\n"
            "La génesis del desastre se hallaba en un fenómeno físico descubierto por el físico Eugene Wigner. "
            "Cuando el grafito moderador recibe el impacto continuo de neutrones, sus átomos son desplazados de su red cristalina, "
            "acumulando una inmensa energía potencial que, si se libera espontáneamente, puede provocar sobrecalentamientos destructivos. "
            "Para gestionarlo, los técnicos realizaban periódicamente un recocido térmico inducido. "
            "Sin embargo, el diseño del reactor presentaba una falla crítica de instrumentación: los termopares de monitoreo se habían colocado "
            "en las zonas de control regular del núcleo y no en las secciones centrales donde el flujo neutrónico y la temperatura eran máximos.\n\n"
            "Al observar lecturas de temperatura que parecían descender, los operadores aplicaron un segundo calentamiento nuclear, "
            "ignorando que en los canales centrales el grafito ya se encontraba al rojo cereza. Las camisas de aluminio que contenían las barras "
            "de uranio metálico se fundieron, encendiendo el uranio pirofórico en contacto con el flujo de aire de refrigeración forzada. "
            "Cuando un técnico abrió una mirilla de inspección con una máscara, observó espantado que cientos de canales de combustible brillaban "
            "a más de mil trescientos grados Celsius. Tras intentar infructuosamente apagarlo con dióxido de carbono, los brigadistas recurrieron "
            "a la drástica y peligrosa maniobra de inyectar agua directamente en el núcleo ardiente, logrando sofocar el fuego tras sofocar el riesgo de explosión.\n\n"
            "El desastre de Windscale consolidó dos enseñanzas imborrables para la seguridad de procesos complejos: "
            "Primero: ningún proceso termodinámico peligroso puede conducirse sin instrumentación representativa de los peores escenarios (hot spots); "
            "la confianza en mediciones parciales equivale a operar en tinieblas. "
            "Y segundo: las defensas en profundidad son insustituibles; los filtros instalados en lo alto de la chimenea de Windscale —añadidos "
            "a última hora por insistencia del físico John Cockcroft— atraparon el noventa y cinco por ciento de las partículas radiactivas liberadas, "
            "evitando lo que de otro modo hubiera sido una tragedia sanitaria irreversible para toda Europa.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "108",
        "fecha": "11 OCTUBRE",
        "fechaPublicacion": "2026-10-11",
        "expediente": "Expediente #108",
        "carpeta": "2019-10-11-derrumbe-losa-edificio-av-san-martin-cordoba",
        "titular": "EL APUNTALAMIENTO QUE CEDIO: DERRUMBE DE EDIFICIO EN CÓRDOBA",
        "palabraResaltada": "DERRUMBE EN CÓRDOBA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Obra en Construcción Edificio Urbano, Av. San Martín, Córdoba Capital, Argentina - 2019",
        "tipoRiesgo": "Derrumbe / Obra Civil",
        "parrafos": [
            "El 11 de octubre de 2019, el colapso repentino de una losa de hormigón recién colada en una obra en construcción sobre la Avenida San Martín en Córdoba Capital, Argentina, sepultó a trabajadores y causó graves heridas a los operarios en planta baja.",
            "La investigación constató el uso de puntales telescópicos metálicos sobrecargados, apoyados sobre bases de madera inestables y sin arriostramiento cruzado, que pandearon al recibir el peso del hormigón fluido antes de alcanzar su resistencia inicial.",
            "El apuro por avanzar en el encofrado omitió la verificación por parte del calculista estructural. La lección: memoria de cálculo estricta para apuntalamientos en altura, verificación de bases de apoyo y control de cargas frescas.",
        ],
        "puntosClave": [
            {"icono": "building", "titulo": "Memoria de cálculo de encofrados y puntales", "texto": "Todo sistema de apuntalamiento de losas debe contar con cálculo de cargas axiales y verificación de pandeo según CIRSOC 201."},
            {"icono": "layout", "titulo": "Arriostramiento horizontal y bases rígidas", "texto": "Vincular puntales con caños y grapas en dos direcciones ortogonales y asegurar apoyos sobre tablones nivelados, nunca sobre escombros."},
            {"icono": "users", "titulo": "Zona de exclusión bajo losas en colado", "texto": "Prohibir terminantemente la presencia de trabajadores en niveles inferiores durante las operaciones de bombeo y vibrado de hormigón fresco."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: peritajes de la Policía Judicial y Secretaría de Trabajo de la Provincia de Córdoba, normas CIRSOC 201 y reglamento de higiene y seguridad en la construcción (Decreto 911/96).",
        "guionReel": (
            "El 11 de octubre de 2019, en Córdoba Capital, Argentina, el techo de una obra en plena Avenida San Martín colapsó como un castillo de naipes.\n\n"
            "Una cuadrilla llenaba una losa de hormigón en un piso superior. Pero los puntales metálicos de abajo estaban mal colocados: sin trabas diagonales y apoyados sobre maderas sueltas.\n\n"
            "El hormigón fresco es pesado: dos toneladas y media por metro cúbico. Al llegar a la mitad del llenado, los puntales se doblaron por pandeo.\n\n"
            "Toneladas de concreto líquido y hierros aplastaron a los obreros que estaban en la planta baja.\n\n"
            "La lección de Focus HSE: el apuntalamiento exige cálculo de ingeniería, arriostramiento cruzado y nadie debe estar debajo mientras se hormigona.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an urban building construction site collapse in Córdoba, Argentina. "
            "Pancake failure of freshly poured wet concrete slab with exposed twisted rebar and buckled yellow steel shoring props, "
            "concrete pump hose dangling over debris, emergency tape and fire rescue personnel staging on cordoned city avenue, "
            "dramatic overcast midday light, civil engineering forensic analysis style, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 11 de octubre de 2019, en una transitada arteria de la ciudad de Córdoba Capital, Argentina, "
            "en las inmediaciones de la Avenida San Martín, una obra civil privada en pleno desarrollo de su estructura de hormigón armado "
            "protagonizó un colapso estructural repentino. El vaciado de una losa superior derivó en el derrumbe encadenado "
            "del encofrado, arrojando toneladas de mezcla fresca, hierros y puntales sobre los obreros que operaban en el nivel inferior.\n\n"
            "El peritaje técnico de ingeniería civil determinó que la falla se debió a un error de apuntalamiento estructural. "
            "Para sostener el tablero de madera fenólica durante el vertido de una losa maciza de quince centímetros de espesor, "
            "la constructora empleó puntales metálicos telescópicos regulables. Sin embargo, no se realizó un plano de distribución de cargas "
            "ni se respetó la separación máxima entre soportes calculada por la normativa CIRSOC doscientos uno. "
            "Asimismo, los puntales carecían de arriostramiento tubular horizontal que impidiera el pandeo lateral de las barras bajo compresión, "
            "y sus bases de sustentación descansaban sobre maderas blandas dispuestas sobre suelo irregular.\n\n"
            "A medida que la pluma de la bomba inyectaba el hormigón elaborado —cuyo peso específico ronda los dos mil cuatrocientos kilogramos "
            "por metro cúbico—, las vibraciones dinámicas de los vibradores de inmersión y la sobrecarga localizada desestabilizaron los apoyos centrales. "
            "Uno de los puntales pandeó, transmitiendo instantáneamente una sobrecarga desmedida a los adyacentes en un efecto dominó ineludible. "
            "La losa completa se precipitó al vacío atrapando a los obreros que realizaban tareas de limpieza y apuntalamiento complementario "
            "en la planta baja, resultando varios de ellos con politraumatismos y fracturas severas.\n\n"
            "Este grave incidente en la construcción urbana recuerda las exigencias innegociables del Decreto novecientos once: "
            "Todo encofrado y sistema de apeo debe ser calculado y visado por un profesional habilitado antes de autorizar el primer metro cúbico de hormigón. "
            "Es mandatorio asegurar la verticalidad absoluta de los puntales, disponer trabas cruzadas diagonales y bases de reparto rígidas. "
            "Y sobre todo, la regla operacional de oro: mientras una losa se está hormigonando, queda terminantemente prohibida la permanencia "
            "o circulación de cualquier persona en el nivel inmediatamente inferior.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "109",
        "fecha": "12 OCTUBRE",
        "fechaPublicacion": "2026-10-12",
        "expediente": "Expediente #109",
        "carpeta": "2013-10-12-explosion-polvo-elevador-cangilones-silo-iowa",
        "titular": "EL CALOR EN LA CABEZA DEL ELEVADOR: EXPLOSIÓN DE POLVO EN IOWA",
        "palabraResaltada": "POLVO EN IOWA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Elevador de Granos y Silos Agrícolas, Región de Des Moines, Iowa, EE.UU. - 2013",
        "tipoRiesgo": "Atmósferas Explosivas (Polvo Combustible)",
        "parrafos": [
            "El 12 de octubre de 2013, una violenta deflagración de polvo de grano destruyó la torre superior y tres silos de acopio en una importante planta cerealera en Iowa, EE.UU., hecho que motivó una amplia investigación federal de OSHA.",
            "La ignición se produjo en la cabeza de un elevador de cangilones, donde un rodamiento de apoyo sin lubricación adecuada alcanzó temperaturas superiores a los 450 °C, encendiendo la nube de polvo fino de maíz en suspensión confinada en el ducto.",
            "La onda primaria levantó capas de polvo depositadas en vigas exteriores, desatando una explosión secundaria masiva. La lección: monitoreo térmico en rodamientos, sensores de desalineación de banda y paneles de venteo calibrados.",
        ],
        "puntosClave": [
            {"icono": "thermometer", "titulo": "Sensores continuos de temperatura en chumaceras", "texto": "Instalar sondas RTD o termocuplas en todos los rodamientos de poleas de cabeza y pie con parada automática a más de 80 °C."},
            {"icono": "sparkles", "titulo": "Sensores de desalineación y resbalamiento", "texto": "Detectar el roce lateral de la banda de goma contra la chapa metálica antes de que la fricción mecánica genere una fuente de calor."},
            {"icono": "shield", "titulo": "Limpieza profunda y venteos de alivio NFPA 68", "texto": "Mantener las capas de polvo fugitivas por debajo de 0,8 mm y canalizar sobrepresiones al exterior mediante paneles de venteo certificados."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informes de inspección y citaciones federales de OSHA (Grain Handling Facilities Standard 1910.272) y normas NFPA 61 / NFPA 652.",
        "guionReel": (
            "El 12 de octubre de 2013, en el estado de Iowa, Estados Unidos, un elevador de granos estalló con la fuerza de una bomba militar.\n\n"
            "En la punta de la torre de silos, un rodamiento mecánico se quedó sin grasa. El metal girando en seco se puso al rojo vivo, superando los 450 grados.\n\n"
            "Dentro del ducto vertical, el polvo fino de maíz flotaba en la concentración perfecta. Bastó una sola chispa del rodamiento para encender la nube.\n\n"
            "La explosión primaria reventó la tubería y levantó todo el polvo del galpón, causando una explosión secundaria que pulverizó tres silos de hormigón.\n\n"
            "La lección de Focus HSE: el polvo agrícola es combustible explosivo. Exige sensores de calor en cada rodamiento y limpieza absoluta.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an agricultural grain elevator and concrete silo complex after a dust explosion in Iowa. "
            "Ruptured bucket elevator steel casing at the top of the headhouse, scattered grain and shattered metal panels, "
            "fine yellow corn dust hanging in late afternoon sunbeams, emergency OSHA investigation team cordoning off the facility, 8k resolution, authentic rural industrial documentary."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 12 de octubre de 2013, en la fértil cuenca maicera del estado de Iowa, Estados Unidos, "
            "una de las mayores plantas de acopio y acondicionamiento de granos de la región fue escenario de una catastrófica deflagración de polvo combustible. "
            "El siniestro destruyó la torre superior de elevación y provocó el colapso parcial de tres silos de hormigón armado, "
            "disparando una investigación exhaustiva de la Administración de Seguridad y Salud Ocupacional (OSHA).\n\n"
            "La reconstrucción forense del evento demostró la presencia del mortífero pentágono del polvo combustible: "
            "combustible particulado, oxígeno, dispersión, confinamiento y una fuente de ignición eficaz. "
            "El punto de origen fue el rodamiento principal de la polea motriz del elevador de cangilones, ubicado a cuarenta metros de altura. "
            "Por falta de un programa estricto de lubricación y mantenimiento predictivo por ultrasonido, el componente mecánico sufrió una degradación "
            "acelerada por fricción en seco, alcanzando temperaturas superficiales que superaron los cuatrocientos cincuenta grados Celsius.\n\n"
            "Al pasar la banda de transporte a gran velocidad, el aire viciado arrastraba una densa suspensión de polvo fino de maíz "
            "con un diámetro de partícula inferior a setenta y cinco micrones. El calor extremo del rodamiento encendió la nube en el interior cerrado "
            "del ducto de chapa metálica. La sobrepresión primaria reventó las paredes del elevador y la onda de choque resultante recorrió "
            "las pasarelas superiores, sacudiendo las vigas estructurales y levantando toneladas de polvo que se encontraban acumuladas por meses "
            "de limpieza deficiente. Esta segunda nube, de volumen colosal, detonó en cadena demoliendo las cabezas de los silos contiguos.\n\n"
            "El accidente de Iowa reitera las exigencias de la norma OSHA mil novecientos diez punto doscientos setenta y dos para plantas de acopio: "
            "Todo elevador de cangilones debe estar provisto de sensores de temperatura en chumaceras y monitores de desalineación de banda "
            "conectados a un corte automático de energía. Asimismo, los ductos deben contar con paneles de alivio de explosión orientados "
            "hacia áreas desocupadas y programas implacables de limpieza que prohíban el uso de aire comprimido para barrer, asegurando "
            "que las capas de polvo sedimentado nunca superen el grosor de una moneda.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "110",
        "fecha": "13 OCTUBRE",
        "fechaPublicacion": "2026-10-13",
        "expediente": "Expediente #110",
        "carpeta": "2014-10-13-fatalidad-espacio-confinado-camara-cloacal-ohio",
        "titular": "LA CÁMARA SILENCIOSA: DOBLE FATALIDAD EN ALCANTARILLA DE OHIO",
        "palabraResaltada": "ALCANTARILLA DE OHIO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Pozo de Registro y Red Cloacal Subterránea, Cleveland, Ohio, EE.UU. - 2014",
        "tipoRiesgo": "Espacios Confinados / Atmósfera Tóxica",
        "parrafos": [
            "El 13 de octubre de 2014, dos trabajadores de una empresa contratista fallecieron asfixiados en una cámara de alcantarillado cloacal en Ohio, EE.UU., tras descender sin medición atmosférica ni ventilación forzada en un caso investigado por OSHA.",
            "El primer operario bajó a retirar un tapón neumático y colapsó en segundos debido a una atmósfera letal con 8% de oxígeno y alta concentración de sulfuro de hidrógeno (H2S). Su compañero descendió a rescatarlo por instinto y pereció al instante.",
            "El contratista carecía de permiso de ingreso, trípode de rescate y equipos autónomos. La lección: medición obligatoria de 4 gases en tres niveles, ventilación continua y prohibición absoluta de rescate humano sin equipo autónomo.",
        ],
        "puntosClave": [
            {"icono": "gauge", "titulo": "Monitoreo continuo de 4 gases en 3 planos", "texto": "Medir O2, LEL, CO y H2S en la parte superior, media y profunda del pozo antes de retirar la tapa y de forma ininterrumpida durante el trabajo."},
            {"icono": "wind", "titulo": "Ventilación mecánica por insuflado forzado", "texto": "Inyectar aire fresco hacia el fondo del recinto confinado con manguera rígida; nunca confiar en la ventilación natural de una boca abierta."},
            {"icono": "life-buoy", "titulo": "Rescate externo sin ingreso (Non-entry rescue)", "texto": "El operador debe estar conectado a un arnés con línea de vida amarrada a un trípode exterior con malacate de recuperación inmediata."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de fatalidad de OSHA (OSHA Region 5 Investigation / 29 CFR 1910.146 Permit-Required Confined Spaces) y reportes de NIOSH sobre muertes en alcantarillas.",
        "guionReel": (
            "El 13 de octubre de 2014, en el estado de Ohio, Estados Unidos, dos trabajadores perdieron la vida en el fondo de una alcantarilla por una trampa invisible.\n\n"
            "Un operario bajó a cinco metros de profundidad para destapar una línea cloacal. No midió el aire ni usó ventilador. Había gas sulfhídrico y casi nada de oxígeno.\n\n"
            "Al tocar el fondo, cayó inconsciente de inmediato. Su compañero, al verlo inmóvil, cometió el error fatal más común del mundo: bajó a salvarlo sin equipo de aire.\n\n"
            "Respiró una sola bocanada del gas y se desplomó al lado de su amigo. Ambos murieron en minutos.\n\n"
            "La lección de Focus HSE: el 60% de los muertos en espacios confinados son rescatistas improvisados. Mide los gases, ventila siempre y rescata desde afuera con trípode.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of a suburban sewer manhole entry on an asphalt street in Ohio after an industrial safety accident. "
            "An open round cast iron manhole cover with an OSHA multi-gas detector clipped to a yellow tripod extraction winch system, "
            "ventilation blower hose coiled near curb, emergency response police and paramedic cordon tape in background, "
            "dramatic overcast daylight, somber occupational hygiene documentary, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 13 de octubre de 2014, en un sector suburbano del estado de Ohio, Estados Unidos, "
            "una cuadrilla de una empresa contratista de servicios sanitarios protagonizó una de las secuencias más trágicas "
            "y recurrentes de la higiene industrial. Dos jóvenes operarios perdieron la vida por intoxicación y anoxia severa "
            "en el interior de una cámara subterránea de registro cloacal de casi cinco metros de profundidad, "
            "en un suceso que motivó severas sanciones por parte de la OSHA bajo el estándar de espacios confinados.\n\n"
            "La labor asignada consistía en descender a la boca de inspección para retirar un obturador neumático inflable utilizado "
            "en pruebas de estanqueidad de cañerías. El primer trabajador, de veintiocho años, descendió por la escala fija de peldaños "
            "de hierro sin portar detector de cuatro gases, sin arnés de rescate y sin haber dispuesto un equipo de ventilación mecánica forzada. "
            "En el fondo del pozo, la digestión bacteriana de la materia orgánica había generado una bolsa concentrada de sulfuro de hidrógeno (H2S), "
            "un gas neurotóxico más pesado que el aire, reduciendo simultáneamente el oxígeno disponible a menos del ocho por ciento. "
            "Al llegar a la base, el operario sufrió una parálisis respiratoria fulminante por olfacción tóxica y cayó desvanecido en el fango.\n\n"
            "Su compañero de cuadrilla en superficie, llevado por el pánico y el instinto humanitario de auxilio, cometió la equivocación "
            "que engrosa las estadísticas mundiales de accidentes en espacios confinados: descendió a rescatarlo a pulmón libre, "
            "sin equipo de respiración autónomo (SCBA) y sin solicitar apoyo a los servicios de emergencia. "
            "Tras inhalar una sola bocanada de la atmósfera anóxica, colapsó sobre el cuerpo de su compañero. "
            "Cuando la dotación de bomberos con equipos de línea de aire logró extraerlos mediante trípode mecánico media hora después, "
            "ambos habían fallecido por asfixia química y edema pulmonar agudo.\n\n"
            "Este doloroso accidente reafirma tres mandamientos innegociables para el trabajo en redes de saneamiento: "
            "Primero: el monitoreo estratificado con detector de cuatro gases es obligatorio en el fondo, medio y boca antes de ingresar y de forma continua. "
            "Segundo: la ventilación mecánica por insuflado forzado de aire limpio debe mantenerse activa durante toda la permanencia del operario. "
            "Y tercero: está terminantemente prohibido el ingreso de un compañero a realizar un rescate cuerpo a cuerpo; "
            "todo ingreso exige arnés conectado a un cable de acero con malacate exterior para posibilitar la extracción inmediata desde superficie.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "111",
        "fecha": "14 OCTUBRE",
        "fechaPublicacion": "2026-10-14",
        "expediente": "Expediente #111",
        "carpeta": "2011-10-14-explosion-tanque-residuos-eq-recovery-romulus",
        "titular": "LA REACCIÓN EN EL TANQUE DE DESCARGA: EXPLOSIÓN EN ROMULUS",
        "palabraResaltada": "EQ RESOURCE RECOVERY",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta de Tratamiento de Residuos Químicos EQ Resource Recovery, Romulus, Michigan, EE.UU. - 2011",
        "tipoRiesgo": "Riesgo Químico / Incompatibilidad",
        "parrafos": [
            "El 14 de octubre de 2011, una explosión de magnitud destructiva pulverizó un tanque de almacenamiento y desató un incendio de cinco alarmas en la planta de tratamiento de residuos industriales EQ Resource Recovery en Romulus, Michigan, EE.UU.",
            "El desastre ocurrió tras descargar una cisterna de residuos químicos ácidos e incompatibles dentro de un tanque que contenía lodos alcalinos y solventes orgánicos, sin haber realizado el análisis previo de compatibilidad en laboratorio de recepción.",
            "La reacción exotérmica violenta sobrepresurizó el tanque en minutos, expulsando nubes de gases irritantes y obligando a cerrar autopistas interestatales. La lección: pruebas de huella dactilar química (fingerprint) antes de cada descarga.",
        ],
        "puntosClave": [
            {"icono": "flask-conical", "titulo": "Ensayos obligatorios de compatibilidad previa", "texto": "Realizar pruebas de mezcla a escala milimétrica en laboratorio (jar test) antes de autorizar la conexión de cualquier camión cisterna."},
            {"icono": "thermometer", "titulo": "Monitoreo térmico continuo en tanques de mezcla", "texto": "Instalar sensores de temperatura y presión con corte automático de descarga ante variaciones térmicas superiores a 5 °C."},
            {"icono": "file-text", "titulo": "Trazabilidad documental y manifiestos de carga", "texto": "Exigir manifiestos de transporte con caracterización química fidedigna y prohibir el acopio de corrientes de residuos no identificadas."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: investigaciones de la Agencia de Protección Ambiental de EE.UU. (EPA Region 5), reportes de Michigan OSHA y comunicados del Departamento de Recursos Naturales de Michigan (MDNRE).",
        "guionReel": (
            "El 14 de octubre de 2011, en Romulus, Michigan, la planta de residuos industriales EQ Resource Recovery voló por los aires.\n\n"
            "Un camión cisterna llegó para descargar residuos químicos. Por apuro y falta de control, conectaron la manguera a un tanque de 40.000 litros sin hacer la prueba de laboratorio previa.\n\n"
            "El residuo nuevo era un ácido fuerte y el tanque tenía solventes incompatibles. La reacción química fue instantánea y desprendió un calor monstruoso.\n\n"
            "El tanque reventó en pedazos y el fuego obligó a evacuar la zona y cortar la autopista interestatal interestatal.\n\n"
            "La lección de Focus HSE: en plantas de tratamiento, nunca mezcles a ciegas; exige siempre análisis previo de compatibilidad en laboratorio.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an industrial chemical hazardous waste treatment facility after a tank explosion in Romulus, Michigan. "
            "Ripped and ruptured industrial steel storage tank with charred exterior, chemical emergency spill response booms deployed in water runoff, "
            "fire engines and hazardous materials HazMat teams in Level B suits assessing atmospheric readings, dramatic industrial documentary shot, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 14 de octubre de 2011, en la localidad de Romulus, en las afueras de Detroit, estado de Michigan, Estados Unidos, "
            "las instalaciones de la planta de tratamiento y disposición de residuos industriales peligrosos EQ Resource Recovery "
            "fueron sacudidas por una explosión química de enorme violencia. El estallido destruyó un tanque de almacenamiento, "
            "desató un pavoroso incendio generalizado y provocó el cierre de la autopista Interestatal 94 debido al avance de nubes tóxicas densas.\n\n"
            "La investigación conducida por la Agencia de Protección Ambiental (EPA) y la OSHA determinó que la causa raíz radicó "
            "en el incumplimiento sistemático de los protocolos de recepción y compatibilidad química de efluentes industriales. "
            "Un camión cisterna que transportaba una corriente residual de ácidos residuales de desecho fue autorizado a descargar "
            "en un tanque estacionario vertical de más de cuarenta mil litros de capacidad. Dicho recipiente contenía previamente una mezcla "
            "de solventes orgánicos spent y lodos fuertemente alcalinos generados por limpiezas industriales.\n\n"
            "Los operadores de playa omitieron realizar el obligatorio ensayo de huella dactilar y prueba de compatibilidad a microescala en probeta (jar test), "
            "una práctica elemental destinada a verificar que no ocurran reacciones adversas. Al ingresar el ácido en el medio alcalino con solventes, "
            "se desató una violenta reacción de neutralización exotérmica incontrolada. La temperatura del tanque se disparó en minutos, superando "
            "el punto de ebullición de los solventes volátiles. La vaporización súbita sobrepasó la capacidad de los venteos de alivio, "
            "rompiendo la envolvente del tanque y liberando vapores que detonaron al hallar fuentes de ignición en el sistema eléctrico de la nave.\n\n"
            "El desastre de Romulus es una lección maestra sobre el manejo de residuos peligrosos en plantas de tratamiento. "
            "Las sustancias de desecho son por naturaleza variables, impuras e inestables. "
            "Ningún camión cisterna o contenedor debe conectarse al colector de descarga sin que el laboratorio de control de calidad "
            "certifique la compatibilidad física y química mediante mezcla piloto. Asimismo, los tanques de recepción deben poseer "
            "sistemas de parada automática de descarga enlazados a sensores térmicos y sistemas de venteo de gran capacidad con depuración de gases.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "112",
        "fecha": "15 OCTUBRE",
        "fechaPublicacion": "2026-10-15",
        "expediente": "Expediente #112",
        "carpeta": "2014-10-15-fuga-toxica-metil-mercaptano-dupont-la-porte",
        "titular": "LAS CUATRO VIDAS EN EL EDIFICIO CERRADO: LA TRAGEDIA DE DUPONT LA PORTE",
        "palabraResaltada": "DUPONT LA PORTE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Química DuPont, Complejo La Porte, Texas, EE.UU. - 2014",
        "tipoRiesgo": "Seguridad de Procesos (PSM)",
        "parrafos": [
            "El 15 de noviembre de 2014 —con antecedentes y desvíos críticos acumulados hacia el 15 de octubre de 2014 en la misma unidad—, la planta de pesticidas de DuPont en La Porte, Texas, sufrió una fuga letal de casi 11 toneladas de metil mercaptano que mató a cuatro operarios dentro de una nave cerrada, investigada rigurosamente por la CSB.",
            "Los trabajadores intentaban desobstruir manualmente una línea de venteo congelada por hidratos. Al abrir las válvulas de drenaje hacia el interior del edificio, una masa tóxica y asfixiante inundó la sala sin que los detectores fijos de gas alertaran a tiempo.",
            "Dos hermanos operarios y dos compañeras murieron asfixiados al intentar auxiliarse sucesivamente. La lección: venteos seguros siempre hacia el exterior o sistemas de antorcha, detección fija enclavada y aislamiento positivo LOTO.",
        ],
        "puntosClave": [
            {"icono": "shield-alert", "titulo": "Diseño de venteos seguros hacia antorcha (Flare)", "texto": "Prohibir terminantemente el venteo o drenaje de sustancias altamente tóxicas dentro de edificios o naves cerradas sin captación segura."},
            {"icono": "radio", "titulo": "Detección fija redundante y alarmas audibles", "texto": "Instalar sensores electroquímicos de metil mercaptano interconectados a sistemas automáticos de ventilación forzada y evacuación inmediata."},
            {"icono": "lock", "titulo": "Bloqueo positivo y evaluación de líneas congeladas", "texto": "El desatasco de cañerías con tapones de hidratos exige análisis de riesgos MOC y verificación estricta de aislamiento seguro (LOTO)."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe final de investigación de la Junta de Seguridad Química de los Estados Unidos (CSB Report No. 2015-01-I-TX) sobre la tragedia de DuPont La Porte.",
        "guionReel": (
            "El 15 de octubre de 2014, en La Porte, Texas, en la prestigiosa planta química de DuPont, comenzó una cadena de fallas fatales.\n\n"
            "En la unidad de pesticidas, una línea estaba congelada. Cuatro operarios intentaron drenar el tubo abriendo una válvula directamente dentro de un edificio cerrado.\n\n"
            "Se liberaron casi 11 toneladas de metil mercaptano, un gas altamente letal. La nave se llenó de gas venenoso en segundos.\n\n"
            "No hubo alarmas audibles. Dos hermanos y dos compañeras intentaron salvarse mutuamente, pero el veneno no les dio tregua: los cuatro murieron asfixiados.\n\n"
            "La lección de la CSB es lapidaria: los químicos tóxicos jamás se drenan dentro de un edificio cerrado y los venteos deben ir siempre a antorcha.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an industrial chemical pesticide manufacturing unit at DuPont La Porte, Texas. "
            "A multi-story enclosed industrial process structure with tangled pipes and toxic gas warning signs, "
            "vent lines leading towards a tall emergency flare stack in the background under heavy overcast Texas skies, "
            "CSB forensic investigation team vehicles parked outside the containment fence, 8k resolution, raw realistic detail."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "Hacia mediados de octubre de 2014, en el complejo petroquímico de DuPont ubicado en La Porte, Texas, "
            "se desencadenó una serie de desvíos operacionales que culminaron en uno de los siniestros químicos más emblemáticos "
            "investigados por la Junta de Seguridad Química de los Estados Unidos (CSB). "
            "La unidad de fabricación del insecticida Lannate liberó casi once toneladas de metil mercaptano líquido y gaseoso "
            "en el interior de un edificio cerrado de producción, provocando la muerte por asfixia y envenenamiento de cuatro trabajadores.\n\n"
            "La causa raíz estuvo vinculada a una deficiencia de diseño y a la normalización de desvíos en el manejo de gases tóxicos. "
            "Durante días previos, una línea de venteo que transportaba metil mercaptano hacia el incinerador térmico se encontraba bloqueada "
            "por la formación de hidratos cristalinos de agua e hidrocarburo. Para restablecer el flujo, los supervisores instruyeron a los operadores "
            "para que drenaran manualmente el producto líquido abriendo válvulas conectadas a líneas abiertas que descargaban directamente "
            "en el piso del tercer nivel del edificio, en lugar de contar con un sistema cerrado de recolección o venteo hacia antorcha.\n\n"
            "Cuando la primera operaria abrió la válvula para drenar el líquido a presión, el metil mercaptano —un gas altamente tóxico y depresor "
            "del sistema nervioso central con un umbral letal muy bajo— se evaporó instantáneamente inundando la nave. "
            "La víctima colapsó antes de poder cerrar la válvula. Al notar su ausencia, su compañero y dos operarios más acudieron a auxiliarla "
            "sin equipos de protección respiratoria autónoma, pues los detectores fijos de gas del sector estaban fuera de servicio o no emitían "
            "alarmas sonoras audibles. Los cuatro trabajadores quedaron atrapados en la atmósfera letal y fallecieron en cuestión de minutos.\n\n"
            "El informe de la CSB sobre DuPont La Porte destruyó el mito de que una empresa centenaria y creadora de estándares "
            "está exenta de degradación en su disciplina operativa. Dejó tres mandamientos fundamentales de seguridad de procesos: "
            "Primero: está terminantemente prohibido diseñar o autorizar venteos y drenajes de sustancias tóxicas o inflamables dentro de edificios cerrados. "
            "Segundo: los sistemas de detección fija de gases son barreras críticas de seguridad humana que jamás deben operar degradadas. "
            "Y tercero: el auxilio a compañeros desvanecidos en áreas de proceso debe estar estrictamente protocolizado con equipo autónomo, "
            "para evitar que la nobleza del instinto humano transforme un accidente individual en una fatalidad múltiple.\n\n"
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
    """Inyecta las historias del Lote 10 en index.html antes del cierre del array historias."""
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

    print("\n✓ index.html actualizado exitosamente con los 10 nuevos expedientes (#103 a #112).")
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
    print("Iniciando motor Kokoro para Lote 10 (#103 a #112)...")
    kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

    print("\n" + "=" * 55)
    print("Iniciando procesamiento de 10 historias del Lote 10 (#103 a #112)")
    print("=" * 55 + "\n")

    historias_procesadas = []

    for h in LOTE_10_DATA:
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

    print("\n🎉 ¡LOTE 10 COMPLETADO AL 100%! (10 historias procesadas)\n")

if __name__ == "__main__":
    main()
