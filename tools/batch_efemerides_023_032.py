# -*- coding: utf-8 -*-
"""
Generador Agéntico Automatizado para Lote 2: Expedientes #023 a #032 (18 al 27 de julio)
1. Crea directorios en assets/efemerides/
2. Genera README.md y contenido-completo.md
3. Guarda guion-reel.txt y prompt-portada.txt
4. Genera portada.png (16:9 alta resolución)
5. Sintetiza audio en Kokoro (speed 0.86, ~500 palabras -> ~3:15 min)
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

LOTE_2_DATA = [
    {
        "id": "023",
        "fecha": "18 JULIO",
        "fechaPublicacion": "2026-07-18",
        "expediente": "Expediente #023",
        "carpeta": "1984-07-18-explosion-recipiente-presion-gas",
        "titular": "LA SOLDADURA SIN ALIVIO TÉRMICO QUE FRACTURÓ LA PLANTA",
        "palabraResaltada": "SOLDADURA SIN ALIVIO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Complejo Petroquímico, Planta de Gas - 1984",
        "tipoRiesgo": "Seguridad de Procesos (PSM) / Recipientes a Presión",
        "parrafos": [
            "El 18 de julio de 1984, una columna de absorción de gas amargo en una planta petroquímica sufrió una rotura catastrófica mientras operaba bajo alta presión.",
            "Una reparación soldada previa no recibió el tratamiento térmico post-soldadura (PWHT) exigido. La presencia combinada de aminas y H2S generó microfisuras por corrosión bajo tensión.",
            "La fractura liberó instantáneamente miles de metros cúbicos de gas combustible, desatando una explosión e incendio masivo. El accidente reafirmó la exigencia de ensayos no destructivos periódicos."
        ],
        "puntosClave": [
            {"icono": "flame", "titulo": "Tratamiento térmico post-soldadura", "texto": "En aceros expuestos a gas amargo o aminas, el alivio de tensiones (PWHT) es indispensable para evitar agrietamiento."},
            {"icono": "scan-line", "titulo": "Ensayos no destructivos (END)", "texto": "Monitorear con ultrasonido y partículas magnéticas las zonas de unión soldada para detectar fisuras subclínicas."},
            {"icono": "shield-check", "titulo": "Integridad mecánica de recipientes", "texto": "Toda reparación en recipientes a presión debe alinearse estrictamente al código ASME Sección VIII y API 510."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: investigaciones de fallas en recipientes a presión del National Board of Boiler and Pressure Vessel Inspectors y normas API 510 / ASME VIII.",
        "guionReel": (
            "18 de julio de 1984. — En una planta petroquímica de procesamiento de gas... una columna de absorción operaba bajo intensa presión de proceso. — "
            "Meses antes... la pared metálica de la torre había sido reparada con una soldadura manual... pero para ahorrar tiempo de parada, "
            "se omitió el tratamiento térmico de alivio de tensiones. — "
            "En silencio... la acción corrosiva del sulfuro de hidrógeno y las aminas comenzó a desgarrar microscópicamente el acero. — "
            "Esa tarde... la costura cedió de golpe. "
            "La columna reventó como un proyectil... liberando una nube de gas combustible que detonó en una llamarada de más de cincuenta metros. — "
            "En recipientes a presión... no existen soldaduras sin control de ingeniería. — "
            "La seguridad... está en los detalles."
        ),
        "guionLargo": (
            "18 de julio de 1984. — En un complejo petroquímico dedicado a la purificación y tratamiento de gas natural... "
            "una imponente columna de absorción de más de treinta metros de altura procesaba corrientes de gas amargo bajo alta presión y temperatura. — "
            "Para eliminar los compuestos de sulfuro de hidrógeno y dióxido de carbono... la torre utilizaba una solución química líquida de aminas, "
            "un solvente altamente alcalino que circula de forma continua por el interior del recipiente metálico. — "
            "Meses antes de la tragedia... durante una parada programada de mantenimiento... los inspectores detectaron un leve desgaste localizado "
            "en una de las virolas intermedias de la vasija de presión. — "
            "Se decidió realizar una reparación mediante aporte de soldadura estructural en la chapa de acero al carbono. "
            "Sin embargo... para acelerar el reingreso en producción y evitar los elevados costos de alquilar equipos de inducción térmica... "
            "la supervisión omitió el tratamiento térmico post-soldadura exigido por el código ASME. — "
            "Muchos creen que una soldadura se considera terminada en cuanto el cordón se enfría al tacto. "
            "Pero en metalurgia... la soldadura genera tensiones residuales internas gigantescas en la zona afectada por el calor. "
            "Cuando ese acero tensionado entra en contacto con vapores calientes de aminas y trazas de sulfuro de hidrógeno... "
            "se desencadena un proceso implacable conocido como corrosión bajo tensión inducida por aminas. — "
            "En el interior del metal... microfisuras invisibles a simple vista comenzaron a ramificarse a lo largo de toda la zona de unión soldada. — "
            "La tarde del 18 de julio... mientras la planta operaba a régimen nominal con más de veinticinco bares de presión interna... "
            "la pared de la columna alcanzó su límite elástico crítico. — "
            "Sin previo aviso... una fisura de varios metros se propagó a la velocidad del sonido a través del cuerpo cilíndrico del recipiente. — "
            "La columna se desgarró longitudinalmente... despresurizándose de forma instantánea y catastrófica. "
            "Miles de metros cúbicos de hidrocarburos volátiles comprimidos se expandieron al instante... pulverizándose en forma de nube de vapor. — "
            "Al encontrar una fuente de ignición en los hornos de recalentamiento cercanos... la nube detonó con una onda expansiva masiva "
            "que derribó estructuras linderas, provocó múltiples víctimas y desató un incendio incontrolable que consumió la unidad durante horas. — "
            "La investigación metalúrgica oficial confirmó que la causa raíz fue el agrietamiento por corrosión bajo tensión en la soldadura no tratada térmicamente. "
            "Este desastre consolidó las pautas universales de integridad mecánica API 510 y NACE: "
            "en recipientes sometidos a medios amargos o cáusticos... el tratamiento térmico post-soldadura y los ensayos no destructivos por ultrasonido "
            "no son una opción: son la única barrera que impide la fractura frágil del acero. — "
            "En recipientes a presión... saltarse un procedimiento de soldadura es condenar la planta al colapso. — "
            "La seguridad... está en los detalles."
        ),
        "promptFoto": (
            "Historical petrochemical refinery photography, 35mm lens, 16:9 landscape aspect ratio. A massive steel amine gas absorption distillation tower "
            "in an oil and gas processing plant, 1984. Industrial piping, high-pressure flanges, weld seams, pressure gauges, scaffolding, "
            "dramatic overcast industrial sky, authentic analog film grain, National Geographic investigative engineering aesthetic, no text."
        )
    },
    {
        "id": "024",
        "fecha": "19 JULIO",
        "fechaPublicacion": "2026-07-19",
        "expediente": "Expediente #024",
        "carpeta": "2017-07-19-caida-carga-suspendida-izaje",
        "titular": "UNA ESLINGA SIN PROTECCIÓN Y LA LÍNEA DE FUEGO MORTAL",
        "palabraResaltada": "LÍNEA DE FUEGO MORTAL",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Patio de Maniobras Industriales - 2017",
        "tipoRiesgo": "Izaje y Cargas Suspendidas / Aplastamiento",
        "parrafos": [
            "El 19 de julio de 2017, en el patio logístico de una acería, una grúa puente izaba un paquete de vigas de acero de cuatro toneladas utilizando eslingas sintéticas de poliéster.",
            "Las eslingas fueron estranguladas directamente sobre los filos vivos de las vigas sin cantoneras de protección. La fricción y el filo cortaron la faja textil a mitad del trayecto.",
            "La carga cayó en picada sobre una senda peatonal donde transitaban dos trabajadores, causando una víctima mortal instantánea. El accidente demostró la falta de delimitación de la zona de izaje."
        ],
        "puntosClave": [
            {"icono": "shield-ban", "titulo": "Cantoneras obligatorias en filos vivos", "texto": "Proteger siempre las eslingas textiles con esquineros de poliuretano o acero para evitar cortes por rozamiento."},
            {"icono": "ban", "titulo": "Línea de fuego: zona cero personas", "texto": "Prohibir tajantemente ubicarse o transitar debajo de cualquier carga suspendida o dentro de su cono de caída."},
            {"icono": "search-check", "titulo": "Inspección pre-uso de eslingas", "texto": "Revisar costuras, etiqueta de capacidad legible y descartar fajas con cortes o quemaduras previas."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: normativas de izaje seguro ASME B30.9 (Slings), OSHA 1910.184 e informes periciales de siniestros en patios de maniobras.",
        "guionReel": (
            "19 de julio de 2017. — En un patio de maniobras industriales... una grúa izaba un paquete de perfiles de acero de más de cuatro toneladas. — "
            "Para atar la carga... se utilizaron eslingas sintéticas de tela apoyadas directamente contra los bordes afilados del metal... sin cantoneras de protección. — "
            "A tres metros de altura... el filo cortó la fibra sintética como si fuera papel. — "
            "En el suelo... un operario caminaba confiado justo por debajo de la carga suspendida. — "
            "Cuatro toneladas de acero cayeron a plomo sobre él en menos de un segundo. — "
            "Nunca te pares bajo una carga suspendida. Protege las eslingas en cada filo... y respeta la línea de fuego. — "
            "La seguridad... está en los detalles."
        ),
        "guionLargo": (
            "19 de julio de 2017. — En el patio de acopio y despacho de una importante planta metalúrgica... "
            "los equipos de izaje operaban sin descanso para cargar semirremolques con perfiles estructurales de acero. — "
            "El movimiento de cargas pesadas mediante grúas es una de las maniobras de mayor riesgo crítico en cualquier faena industrial. "
            "Exige aparejadores calificados, accesorios certificados, cálculo riguroso del centro de gravedad y una delimitación física estricta "
            "que impida que cualquier persona se interponga en la línea de fuego. — "
            "Esa tarde... el rigger preparó un paquete de vigas de acero de cuatro toneladas de peso. "
            "Para ahorrar tiempo y no buscar cadenas de acero o cantoneras protectoras... envolvió la carga con dos eslingas sintéticas planas de poliéster. — "
            "Las fajas textiles son ligeras y cómodas... pero tienen un punto débil fatal: son extremadamente vulnerables al corte por cizallamiento "
            "cuando entran en contacto directo con aristas metálicas afiladas. — "
            "El operador de la grúa elevó la carga a más de cuatro metros de altura y comenzó el desplazamiento horizontal hacia la bahía de carga. — "
            "Con el balanceo natural del movimiento... el borde vivo de la viga comenzó a aserrar las fibras de poliéster bajo la enorme tensión de cuatro toneladas. — "
            "Mientras tanto... en el suelo... dos trabajadores caminaban por el patio en dirección al comedor. "
            "El área de maniobra no estaba delimitada con vallas ni conos de peligro, y ningún señalero detuvo el tránsito peatonal. — "
            "Confiados en la rutina... los operarios cruzaron desprevenidamente justo por debajo de la carga suspendida. — "
            "En ese instante... la eslinga principal se cortó de golpe. — "
            "El paquete de acero perdió el equilibrio, zafó de la segunda faja y cayó en caída libre sobre la senda peatonal. — "
            "Uno de los trabajadores escuchó el crujido y logró arrojarse a un costado... pero el segundo compañero recibió el impacto directo del acero. — "
            "Falleció en el acto por politraumatismos masivos bajo el peso aplastante de la carga. — "
            "La investigación determinó dos fallas críticas insalvables: la omisión criminal de cantoneras en los filos vivos "
            "y la violación del principio más sagrado del izaje industrial: jamás, bajo ninguna circunstancia, se debe transitar o permanecer "
            "debajo del radio de acción de una carga suspendida. — "
            "Los accesorios de izaje se rompen. Por eso la única barrera infalible es estar fuera de su trayectoria de caída. — "
            "La seguridad... está en los detalles."
        ),
        "promptFoto": (
            "Industrial documentary photography, 35mm lens, 16:9 landscape aspect ratio. A heavy industrial crane yard with overhead gantry crane. "
            "Massive bundled steel I-beams suspended slightly above gravel ground, purple and green synthetic rigging slings showing sharp edge contact, "
            "warning red barrier tape, industrial yellow crane hook, realistic gritty metal yard textures, overcast afternoon lighting, no text."
        )
    },
    {
        "id": "025",
        "fecha": "20 JULIO",
        "fechaPublicacion": "2026-07-20",
        "expediente": "Expediente #025",
        "carpeta": "1991-07-20-explosion-tanques-coode-island",
        "titular": "EL PARQUE DE TANQUES QUE ARDIÓ POR FALTA DE INERTIZACIÓN",
        "palabraResaltada": "FALTA DE INERTIZACIÓN",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Isla Coode, Puerto de Melbourne, Australia - 1991",
        "tipoRiesgo": "Seguridad de Procesos / Almacenamiento Químico",
        "parrafos": [
            "El 20 de julio de 1991, en la terminal petroquímica de Coode Island en Melbourne, un tanque cargado con acrilonitrilo explotó violentamente, iniciando un incendio en cadena.",
            "El espacio de vapor de los tanques no contaba con inertización activa de nitrógeno ni arrestallamas efectivos. La acumulación de cargas electrostáticas encendió los vapores inflamables.",
            "Dieciséis tanques con más de ocho millones de litros de solventes tóxicos ardieron durante días, cubriendo Melbourne con una densa nube tóxica y transformando las regulaciones de almacenamiento."
        ],
        "puntosClave": [
            {"icono": "wind", "titulo": "Inertización con nitrógeno (Blanketing)", "texto": "Mantener una atmósfera inerte libre de oxígeno en el colchón de vapor de tanques que almacenan líquidos volátiles."},
            {"icono": "shield-alert", "titulo": "Arrestallamas certificados y limpios", "texto": "Instalar supresores de llama en los venteos y asegurar su inspección periódica para evitar el retroceso de llama."},
            {"icono": "sparkles", "titulo": "Puesta a tierra y disipación estática", "texto": "Garantizar continuidad eléctrica y tiempos de relajación en bombeos para disipar cargas electrostáticas."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de la Comisión de Investigación del Desastre de Coode Island, WorkSafe Victoria y guías NFPA 30 sobre líquidos inflamables.",
        "guionReel": (
            "20 de julio de 1991. — En el puerto de Melbourne, Australia... la terminal química de Coode Island almacenaba millones de litros de solventes y químicos volátiles. — "
            "En el tanque número ochenta y seis... miles de litros de acrilonitrilo líquido desprendían vapores altamente inflamables en su interior. — "
            "El tanque no contaba con un sistema de inertización con gas nitrógeno que desplazara el oxígeno... "
            "y los venteos carecían de arrestallamas adecuados. — "
            "Una pequeña chispa por acumulación de electricidad estática encendió la mezcla explosiva interna. — "
            "El tanque estalló en una gigantesca bola de fuego... desatando un efecto dominó que destruyó dieciséis tanques y cubrió la ciudad de humo tóxico. — "
            "Donde hay vapores volátiles... desplazar el oxígeno es la única barrera de prevención. — "
            "La seguridad... está en los detalles."
        ),
        "guionLargo": (
            "20 de julio de 1991. — En el puerto de Melbourne, en el estado australiano de Victoria... "
            "la terminal de Coode Island operaba como el mayor centro de almacenamiento y trasvase de productos químicos y solventes orgánicos del país. — "
            "Decenas de grandes tanques de almacenamiento vertical de techo fijo albergaban sustancias altamente inflamables y tóxicas, "
            "como benceno, acrilonitrilo, fenol y acetatos, destinadas al abastecimiento de la industria farmacéutica y plástica. — "
            "En el almacenamiento a granel de líquidos volátiles... el mayor peligro no radica en el líquido en sí, sino en el espacio de vapor libre "
            "que queda confinado entre la superficie del producto y el techo del tanque. — "
            "Si ese espacio de vapor contiene aire con veintiún por ciento de oxígeno y vapores de hidrocarburos dentro del rango de inflamabilidad... "
            "el tanque se convierte literalmente en una enorme cámara de combustión esperando únicamente una fuente mínima de energía para detonar. — "
            "Para evitar esta condición... las buenas prácticas de ingeniería exigen la inertización continua con nitrógeno gaseoso... "
            "un proceso conocido como blanketing, que desplaza el oxígeno del interior del tanque a niveles inferiores al cinco por ciento, "
            "imposibilitando físicamente cualquier combustión. — "
            "Sin embargo... en Coode Island, varios tanques operaban sin sistema de inertización activo y con dispositivos de venteo deficientes. — "
            "A primera hora de la mañana del 20 de julio... en el tanque ochenta y seis, cargado con acrilonitrilo... "
            "se inició el trasvase de producto. El flujo turbulento generó acumulación de cargas electrostáticas en la superficie. — "
            "Una pequeña descarga estática en el interior del colchón de vapor encendió la atmósfera no inertizada. — "
            "La explosión fue devastadora. La cúpula del tanque se desprendió como la tapa de una lata... y una bola de fuego de cientos de metros iluminó el puerto. — "
            "Los cubetos de retención colapsaron bajo el calor extremo... y el fuego comenzó a propagarse de tanque en tanque por radiación térmica en un efecto dominó imparable. — "
            "Dieciséis tanques de almacenamiento estallaron en serie... liberando más de ocho millones de litros de químicos en combustión. — "
            "Una gigantesca columna de humo negro y gases tóxicos con cianuro de hidrógeno y monóxido de carbono se desplazó sobre Melbourne... "
            "obligando a evacuar escuelas, cerrar puertos y declarar la emergencia química general en toda la metrópoli. — "
            "Más de cien bomberos combatieron las llamas durante casi tres días consecutivos hasta sofocar el infierno químico. — "
            "La catástrofe de Coode Island reescribió los estándares mundiales de almacenamiento en parques de tanques: "
            "todo líquido de bajo punto de inflamación exige colchón de gas inerte monitoreado, arrestallamas certificados en cada venteo "
            "y una separación física adecuada entre cubetos para evitar el efecto dominó. — "
            "Controlar el oxígeno en el vapor es la diferencia entre un parque de tanques seguro o una bomba incendiaria. — "
            "La seguridad... está en los detalles."
        ),
        "promptFoto": (
            "Historical wide documentary photograph, 35mm lens, 16:9 aspect ratio. An industrial bulk chemical tank storage terminal at Coode Island Melbourne, 1991. "
            "Rows of large white cylindrical storage tanks, yellow catwalks, steel containment bunds, pipeline manifolds, vapor recovery vents. "
            "Dramatic atmospheric morning sky, port cranes in distance, gritty industrial photorealistic style, no text."
        )
    },
    {
        "id": "026",
        "fecha": "21 JULIO",
        "fechaPublicacion": "2026-07-21",
        "expediente": "Expediente #026",
        "carpeta": "2016-07-21-atrapamiento-sinfin-agricola",
        "titular": "METER LA MANO EN EL SINFÍN: UN ATAJO QUE COSTÓ UN MIEMBRO",
        "palabraResaltada": "EN EL SINFÍN",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta de Acopio Agrícola, Córdoba, Argentina - 2016",
        "tipoRiesgo": "Atrapamiento / Protección de Máquinas / LOTO",
        "parrafos": [
            "El 21 de julio de 2016, en una planta de acopio de cereales en Córdoba, Argentina, un operario limpiaba una tolva de descarga cuando un tornillo sinfín transportador se trabó con maíz apelmazado.",
            "Para no demorar la descarga de camiones, el trabajador retiró la rejilla de protección superior e introdujo su mano para destrabar el grano sin desconectar el motor eléctrico ni aplicar candado LOTO.",
            "El cereal cedió súbitamente y el rotor sinfín comenzó a girar a toda velocidad, atrapando el brazo del operario. La herida provocó la amputación traumática del miembro superior."
        ],
        "puntosClave": [
            {"icono": "lock", "titulo": "Bloqueo y etiquetado (LOTO)", "texto": "Cortar el seccionador principal, colocar candado personal y verificar energía cero antes de tocar cualquier mecanismo."},
            {"icono": "shield", "titulo": "Enclavamiento en rejillas de protección", "texto": "Las rejillas de tolvas deben contar con interruptores de seguridad interlocked que corten el motor si se abren."},
            {"icono": "hand-metal", "titulo": "Herramientas de extensión manual", "texto": "Jamás utilizar las manos directamente para empujar o destrabar material; utilizar varas de madera o pértigas."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: registros periciales de siniestralidad agropecuaria de la SRT Argentina, manuales de seguridad en silos de INTA y normas OSHA 1910.212.",
        "guionReel": (
            "21 de julio de 2016. — En una planta de acopio cerealera en Córdoba, Argentina... una fila de camiones esperaba para descargar toneladas de maíz en la fosa principal. — "
            "El tornillo sinfín de fondo se atascó con una costra de cereal duro. — "
            "Para no detener la línea... un joven operario aflojó los tornillos de la rejilla de seguridad... "
            "y con el motor aún conectado a la red eléctrica... metió el brazo para remover el grano apelmazado con las manos. — "
            "Al liberarse la traba... la hélice de acero arrancó girando a más de cuatrocientas revoluciones por minuto. — "
            "El sinfín no tiene ojos ni frenos de emergencia. Atrapó su manga y le amputó el brazo en una fracción de segundo. — "
            "Ninguna máquina se destraba con la mano. Bloqueo de energía... antes de tocar. — "
            "La seguridad... está en los detalles."
        ),
        "guionLargo": (
            "21 de julio de 2016. — En una planta cerealera de la provincia de Córdoba, Argentina... "
            "las fosas de recepción de camiones trabajaban a plena marcha en el punto más alto de la cosecha de maíz. — "
            "En el fondo de cada tolva de descarga... gira de forma constante un tornillo sinfín transportador... "
            "un pesado eje de acero con espirales helicoidales afiladas que arrastran cientos de toneladas de grano por hora hacia las norias de elevación. — "
            "El sinfín es una de las máquinas más implacables y peligrosas de la industria: su diseño está pensado para triturar y empujar masa densa continua, "
            "con una fuerza de torque descomunal contra la cual la carne y el hueso humano no tienen la más mínima posibilidad de resistencia. — "
            "A media mañana... una carga de maíz con alta humedad formó un bloque apelmazado en la boca de entrada del transportador, "
            "haciendo que el sinfín patinara y dejara de arrastrar grano. — "
            "Afuera... varios camiones aguardaban en fila para descargar. La presión por no frenar la recepción era enorme. — "
            "Un operario de veintiséis años tomó una llave de tuercas, retiró la rejilla metálica de protección superior de la tolva "
            "y se inclinó sobre el conducto para desarmar el terrón de cereal apelmazado. — "
            "Cometió el error más común y trágico en la operación de maquinaria rotativa: creyó que como el eje estaba frenado por el grano, "
            "no era necesario caminar hasta el tablero general para bajar la térmica, colocar el candado LOTO y desenergizar el motor. — "
            "El interruptor del motor seguía en posición encendida... y el motor eléctrico continuaba enviando torque a la transmisión detenida. — "
            "El trabajador introdujo el brazo derecho dentro de la carcasa para remover el maíz con sus dedos. — "
            "Al deshacerse la costra que trababa la espiral... la resistencia mecánica desapareció instantáneamente. "
            "El tornillo sinfín arrancó con toda la fuerza del motor eléctrico a cientos de vueltas por minuto. — "
            "El borde de acero atrapó el guante y la manga del trabajador... succionando su extremidad hacia el fondo de la artesa en una milésima de segundo. — "
            "Los gritos desesperados del operario alertaron a un compañero que corrió a golpear la seta de parada de emergencia... pero el daño mecánico ya era irreversible. — "
            "El mecanismo provocó la amputación traumática completa del brazo del trabajador a la altura del codo. — "
            "La investigación técnica determinó que la rejilla protectora no contaba con microinterruptores de enclavamiento de seguridad que cortaran la corriente al abrirse, "
            "y que se toleraba la costumbre riesgosa de destrabar atascos en caliente para no demorar la logística. — "
            "Las máquinas no tienen criterio: si tienen energía, van a girar. "
            "Nunca retires una protección fija y jamás acerques tu cuerpo a un eje rotativo sin haber colocado tu propio candado de bloqueo en el tablero. — "
            "La seguridad... está en los detalles."
        ),
        "promptFoto": (
            "Agricultural industrial photography, 35mm lens, 16:9 landscape aspect ratio. An industrial grain receiving pit hopper with an exposed steel auger screw conveyor. "
            "Golden corn kernels scattered around the heavy metal grating, industrial drive belt motor, safety lock-out tag-out padlock station nearby on a concrete wall. "
            "Natural morning sunlight entering an open grain shed, solemn documentary style, no text."
        )
    },
    {
        "id": "027",
        "fecha": "22 JULIO",
        "fechaPublicacion": "2026-07-22",
        "expediente": "Expediente #027",
        "carpeta": "2004-07-22-explosion-gasoducto-compresora",
        "titular": "LA FUGA EN EL ARRANQUE QUE DETONÓ LA ESTACIÓN DE GAS",
        "palabraResaltada": "EN EL ARRANQUE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Estación de Gasoducto y Compresión - 2004",
        "tipoRiesgo": "Seguridad de Procesos / Gasoductos (Oil & Gas)",
        "parrafos": [
            "El 22 de julio de 2004, durante las maniobras de puesta en marcha de una estación compresora de gas natural tras tareas de mantenimiento, se produjo una fuga masiva a alta presión.",
            "Una brida en el múltiple de succión no fue torqueada siguiendo el patrón cruzado ni se realizó la prueba de estanqueidad previa (PSSR). Al presurizar con gas metano, la junta de espirometálica reventó.",
            "El gas a más de sesenta bares formó una nube explosiva en segundos que encontró ignición en un equipo no antiexplosivo, destruyendo la nave de compresión y cobrando vidas operativas."
        ],
        "puntosClave": [
            {"icono": "clipboard-check", "titulo": "Revisión pre-arranque (PSSR)", "texto": "Completar la lista de verificación formal antes de introducir hidrocarburos en cualquier sistema intervenido."},
            {"icono": "wrench", "titulo": "Torque cruzado y calibrado", "texto": "Apretar bridas con torquímetro certificado siguiendo el patrón en estrella para garantizar compresión homogénea de la junta."},
            {"icono": "radio", "titulo": "Áreas clasificadas y equipos Ex", "texto": "Prohibir fuentes de ignición o equipos eléctricos comunes en zonas clasificadas con potencial presencia de gas (API 500)."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: investigaciones sobre seguridad en redes de transporte de gas de la Comisión Europea, estándares API 6D y normativas ASME B31.8 de gasoductos.",
        "guionReel": (
            "22 de julio de 2004. — En una estación de compresión de gas natural... cuadrillas de mantenimiento terminaban de ensamblar una línea principal de sesenta bares de presión. — "
            "Para cumplir con el horario de entrega... se abrió la válvula troncal de gas sin realizar la prueba de fugas previa con gas inerte "
            "y sin verificar el torque cruzado en las bridas intervenidas. — "
            "En cuestión de segundos... la junta de sellado cedió ante la brutal presión. — "
            "Un chorro ensordecedor de gas metano comprimido inundó la sala de compresores a cientos de metros cúbicos por minuto. — "
            "Una chispa en un tablero no blindado encendió la nube en una explosión supersónica que demolió la instalación por completo. — "
            "En gasoductos... la prueba pre-arranque y el control de torque salvan vidas. — "
            "La seguridad... está en los detalles."
        ),
        "guionLargo": (
            "22 de julio de 2004. — En una estratégica estación de compresión y regulación de gasoductos troncales... "
            "el personal técnico finalizaba una compleja parada de mantenimiento sobre el tren principal de motocompresores de gas natural. — "
            "Los gasoductos operan bajo condiciones extremas: manejan millones de metros cúbicos diarios de gas metano seco a presiones que superan "
            "los sesenta y hasta los ochenta bares. A esas presiones... cualquier escape de gas no es una simple fuga: "
            "es un chorro con energía cinética sónica, capaz de desgarrar componentes, crear mezclas inflamables instantáneas y generar electricidad estática "
            "al friccionar contra las tuberías. — "
            "Esa mañana... los técnicos se preparaban para reintroducir el hidrocarburo en el sistema. "
            "El protocolo técnico de seguridad de procesos exigía realizar una Revisión de Seguridad Previa al Arranque... conocida como PSSR: "
            "verificar con nitrógeno la ausencia de pérdidas en cada junta desarmada, comprobar que los sellos mecánicos estuvieran lubricados "
            "y certificar que cada perno de brida hubiera sido apretado con torquímetro calibrado mediante el método de torque cruzado en estrella. — "
            "Sin embargo... ante la urgencia comercial por restablecer el suministro hacia la red urbana... se saltearon varios pasos de la lista de verificación. "
            "Una brida de seis pulgadas en el cabezal de succión había sido ajustada a pulso con llave de impacto neumática, sin control de torque homogéneo. — "
            "Los operadores comenzaron a abrir lentamente las válvulas de bloqueo para gasificar la línea. — "
            "A medida que la aguja del manómetro trepaba sobre los cuarenta bares... la junta espirometálica de la brida mal torqueada comenzó a deformarse. "
            "De repente... un ensordecedor silbido de alta frecuencia retumbó en la nave industrial. "
            "La junta fue expulsada por la presión... y un violento chorro de gas metano a alta velocidad inundó la sala en segundos. — "
            "El personal intentó activar el botón de aislamiento de emergencia en el exterior... pero la nube de gas alcanzó rápidamente una zona donde operaba un motor auxiliar "
            "que carecía de certificación eléctrica antiexplosiva. — "
            "La ignición fue inmediata y brutal. Una deflagración violenta sacudió los cimientos de la planta... destrozando techos de chapa, "
            "reventando cañerías secundarias y envolviendo la nave en una gigantesca bola de fuego que cobró la vida de los operadores de turno. — "
            "El informe pericial concluyó que el accidente fue el resultado directo de apresurar el arranque sin respetar los tiempos de prueba y torque. "
            "En la industria del gas... el momento del arranque es la fase de mayor vulnerabilidad operativa. "
            "Nunca introduzcas gas vivo sin haber probado la estanqueidad con nitrógeno y sin haber validado cada perno con torquímetro. — "
            "La seguridad... está en los detalles."
        ),
        "promptFoto": (
            "Industrial documentary photography, 35mm lens, 16:9 landscape aspect ratio. A natural gas pipeline compressor station facility. "
            "Heavy turquoise high-pressure gas pipes, steel flanges, massive industrial ball valves with actuators, gas detector sensors on pillars. "
            "Dramatic low-angle view against an overcast sky, photorealistic oil and gas engineering documentary style, no text."
        )
    },
    {
        "id": "028",
        "fecha": "23 JULIO",
        "fechaPublicacion": "2026-07-23",
        "expediente": "Expediente #028",
        "carpeta": "1984-07-23-explosion-refineria-union-oil",
        "titular": "LA TORRE DE AMINAS QUE ESTALLÓ COMO UN MISIL",
        "palabraResaltada": "COMO UN MISIL",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Refinería Union Oil, Romeoville, Illinois, EE.UU. - 1984",
        "tipoRiesgo": "Seguridad de Procesos (PSM) / Agrietamiento por Hidrógeno",
        "parrafos": [
            "El 23 de julio de 1984, una columna de absorción de aminas de dieciséis metros de altura estalló catastróficamente en la refinería Union Oil de Romeoville, Illinois.",
            "El equipo operaba con propano y butano a alta presión. El acero sufrió agrietamiento inducido por hidrógeno debido a la corrosión ácida, debilitando una soldadura no tratada térmicamente.",
            "La torre se partió en dos; la sección superior voló más de mil metros como un cohete. Las explosiones dejaron 17 muertos y transformaron la inspección de corrosión en refinerías."
        ],
        "puntosClave": [
            {"icono": "scan", "titulo": "Detección de agrietamiento por hidrógeno (HIC)", "texto": "Inspeccionar recipientes en servicio amargo con ultrasonido avanzado de arreglo de fases (PAUT) para hallar ampollas."},
            {"icono": "activity", "titulo": "Medición de espesores en servicio ácido", "texto": "Monitorear la tasa de corrosión interna periódica en torres donde coexisten sulfuro de hidrógeno y aminas."},
            {"icono": "shield-alert", "titulo": "Procedimientos de soldadura calificados", "texto": "Toda modificación o parche en recipientes a presión exige alivio térmico (PWHT) para restaurar la tenacidad del metal."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de investigación de desastres del National Bureau of Standards (NBS), OSHA y publicaciones técnicas del Center for Chemical Process Safety (CCPS).",
        "guionReel": (
            "23 de julio de 1984. — En la refinería Union Oil de Romeoville, Illinois... una torre absorbedora de aminas operaba con gases inflamables a trece bares de presión. — "
            "En el interior del acero... átomos invisibles de hidrógeno penetraron la estructura cristalina del metal... "
            "provocando un fenómeno silencioso y letal conocido como fragilización por hidrógeno. — "
            "A las seis de la tarde... una fisura microscópica se convirtió en una fractura completa. — "
            "La torre de sesenta toneladas se partió al medio. La mitad superior salió disparada hacia el cielo como un misil... volando más de mil metros de distancia. — "
            "Diecisiete personas perdieron la vida bajo las explosiones masivas que redujeron la planta a cenizas. — "
            "En recipientes a presión... la corrosión interna no se ve a simple vista: medir espesores salva vidas. — "
            "La seguridad... está en los detalles."
        ),
        "guionLargo": (
            "23 de julio de 1984. — En la localidad de Romeoville, en las afueras de Chicago, Illinois... "
            "la refinería Union Oil de California operaba como uno de los complejos de destilación y craqueo catalítico más importantes del Medio Oeste norteamericano. — "
            "En la unidad de tratamiento de gas licuado de petróleo... se alzaba una robusta columna de acero al carbono de dieciséis metros de alto y dos metros y medio de diámetro, "
            "construida a fines de los años sesenta para operar como torre absorbedora de aminas. — "
            "Por su interior circulaba una mezcla sumamente volátil y peligrosa: propano y butano gaseoso comprimido a trece bares de presión... "
            "junto con sulfuro de hidrógeno gaseoso y una solución acuosa de monoetanolamina. — "
            "Lo que nadie sospechaba en la refinería... era que en el corazón del acero se estaba gestando el enemigo más traicionero de la industria química: "
            "el agrietamiento inducido por hidrógeno. — "
            "Cuando el sulfuro de hidrógeno corroe el acero en presencia de agua... libera átomos libres de hidrógeno atómico. "
            "Al ser los átomos más pequeños del universo... penetran con facilidad dentro de los intersticios de la red cristalina del acero. "
            "En el interior del metal... los átomos se recombinan formando moléculas de gas hidrógeno que ya no pueden salir, "
            "generando presiones internas microscópicas de miles de atmósferas que provocan ampollamiento y fisuras subsuperficiales que vuelven al acero tan frágil como el vidrio. — "
            "Años antes... la torre había sido sometida a una reparación soldada que nunca recibió tratamiento térmico posterior. "
            "Esa zona de soldadura se convirtió en el punto de concentración de tensiones perfecto para el ataque del hidrógeno. — "
            "Hacia las seis de la tarde del 23 de julio... los operadores de campo advirtieron una pequeña fuga de gas en forma de vapor blanco en la base de la torre. "
            "Una brigada de respuesta se aproximó con mangueras para evaluar la situación. — "
            "En ese instante... la pared de acero de tres centímetros de espesor se desgarró por completo. — "
            "La descompresión explosiva fue de tal magnitud que la mitad superior de la torre... una masa de acero de más de cuarenta toneladas... "
            "se separó de la base y fue propulsada por la energía del gas como un cohete militar... elevándose cientos de metros en el aire "
            "y aterrizando a más de un kilómetro de distancia sobre una autopista cercana. — "
            "Las más de treinta toneladas de gas licuado liberadas detonaron en una serie de explosiones colosales que arrasaron la unidad... "
            "cobrándose la vida de diecisiete trabajadores, incluidos los brigadistas que intentaban contener la fuga, e hiriendo a más de veinte operarios. — "
            "La investigación federal llevada adelante por el National Bureau of Standards cambió la historia de la inspección en refinerías: "
            "demostró que los métodos visuales tradicionales son completamente inútiles frente al daño por hidrógeno. "
            "Desde entonces... los recipientes en servicio ácido deben ser inspeccionados con técnicas avanzadas de ultrasonido para mapear el daño antes de que sea fatal. — "
            "El acero puede lucir impecable por fuera mientras está podrido por dentro. — "
            "La seguridad... está en los detalles."
        ),
        "promptFoto": (
            "Historical archive documentary photograph, 35mm lens, 16:9 landscape aspect ratio. The Union Oil refinery in Romeoville Illinois, summer 1984. "
            "Heavy industrial refinery towers, catalytic cracking units, pipes, storage tanks under a warm dramatic late afternoon sky. "
            "Realistic 1980s film grain, authentic industrial photography style, somber and investigative atmosphere, no text."
        )
    },
    {
        "id": "029",
        "fecha": "24 JULIO",
        "fechaPublicacion": "2026-07-24",
        "expediente": "Expediente #029",
        "carpeta": "2018-07-24-intoxicacion-solventes-pintura",
        "titular": "UN BARBIJO COMÚN FRENTE A UNA NUBE MORTAL DE SOLVENTES",
        "palabraResaltada": "UN BARBIJO COMÚN",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Cabina de Pintura Industrial - 2018",
        "tipoRiesgo": "Higiene Industrial / Riesgo Químico (Solventes)",
        "parrafos": [
            "El 24 de julio de 2018, en un taller de pintura industrial de carrocerías, dos operarios aplicaban pintura poliuretánica con pistolas pulverizadoras dentro de una cabina cerrada.",
            "Para ahorrar energía y evitar ruidos molestos, el sistema de ventilación y extracción forzada estaba apagado. Como protección, los trabajadores usaban barbijos descartables contra polvo común.",
            "Los vapores de tolueno, xileno y poliisocianatos saturaron el recinto cerrado. Un pintor colapsó en el interior por depresión del sistema nervioso central, sufriendo daño cerebral irreversible."
        ],
        "puntosClave": [
            {"icono": "fan", "titulo": "Extracción y ventilación permanente", "texto": "La aplicación de pinturas y solventes exige ventilación localizada por tiro descendente funcionando de forma continua."},
            {"icono": "shield", "titulo": "Selección correcta de EPP respiratorio", "texto": "Los barbijos de polvo no retienen gases ni vapores; se requiere máscara con cartuchos para vapores orgánicos o aire asistido."},
            {"icono": "file-text", "titulo": "Consultar la Ficha de Datos de Seguridad", "texto": "Conocer los límites de exposición profesional (VLA/TLV) del solvente antes de autorizar la tarea."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: normativas de protección respiratoria OSHA 1910.134, guías de higiene industrial de NIOSH y fichas FDS de solventes orgánicos.",
        "guionReel": (
            "24 de julio de 2018. — En un taller de pintura industrial... dos operarios se encerraron en una cabina a pulverizar piezas metálicas con pintura poliuretánica. — "
            "El sistema de extracción de aire estaba apagado por fallas mecánicas... "
            "y para protegerse... los trabajadores se colocaron un barbijo descartable de papel común para polvo de obra. — "
            "Pero los vapores de tolueno y xileno atraviesan el papel como si no existiera nada. — "
            "En menos de veinte minutos... el solvente desplazó el aire y saturó sus pulmones. "
            "Uno de los pintores se desplomó inconsciente en el suelo con un paro cardiorrespiratorio. — "
            "Un barbijo de polvo no detiene químicos. Seleccionar el respirador correcto salva vidas. — "
            "La seguridad... está en los detalles."
        ),
        "guionLargo": (
            "24 de julio de 2018. — En una fábrica de carrocerías y estructuras industriales... "
            "la cabina de pintura operaba en jornadas extendidas para entregar un lote de remolques antes de fin de mes. — "
            "La pintura industrial de alto rendimiento emplea resinas epóxicas y poliuretanos diluidos en solventes orgánicos volátiles "
            "como tolueno, xileno, acetona e isocianatos. — "
            "Estas sustancias químicas tienen una particularidad sumamente nociva: sus moléculas gaseosas son extraordinariamente pequeñas "
            "y tienen una alta afinidad por los tejidos grasos del organismo, especialmente el cerebro y el sistema nervioso central. "
            "Al inhalarse en concentraciones elevadas... provocan mareos iniciales, euforia, pérdida de coordinación motriz "
            "y en pocos minutos la pérdida total de la conciencia y la parálisis del centro respiratorio del bulbo raquídeo. — "
            "Esa mañana... el extractor de aire principal de la cabina de pintura hacía un ruido mecánico ensordecedor debido a un rodamiento desgastado. "
            "Para no soportar el ruido y evitar el consumo eléctrico... los pintores decidieron apagar el sistema de ventilación forzada. — "
            "Cerraron las compuertas herméticas de la cabina y comenzaron a pulverizar pintura con pistolas de alta presión sin renovación de aire. — "
            "Y cometieron el segundo error fatal de la jornada: en lugar de utilizar máscaras de medio rostro con cartuchos químicos de carbón activado "
            "específicos para vapores orgánicos... o equipos con suministro de aire fresco asistido... "
            "tomaron de la caja de suministros barbijos descartables comunes de tela termosellada, de los que se usan para polvo de lijado. — "
            "Un filtro de tela para polvo retiene partículas sólidas microscópicas... pero no tiene ninguna capacidad física ni química "
            "para detener las moléculas de gas de un solvente orgánico. El vapor atraviesa la tela con la misma facilidad que el aire que respiramos. — "
            "En cuestión de quince minutos de pulverización continua... la atmósfera de la cabina se convirtió en una nube tóxica invisible. — "
            "El operario más joven comenzó a balbucear y a perder el equilibrio. Soltó la pistola de pintura y cayó desplomado al piso de rejilla de la cabina. — "
            "Su compañero... también mareado y desorientado por la intoxicación aguda... intentó arrastrarlo hacia la puerta... "
            "pero se desvaneció a pocos metros de la salida. — "
            "Fue un supervisor que pasaba por el pasillo quien miró por la mirilla de vidrio y vio a ambos hombres tirados en el suelo. — "
            "Abrió las puertas de inmediato y logró sacarlos al aire libre con ayuda de otros operarios. "
            "Uno de los trabajadores fue reanimado en el hospital... pero el joven que cayó primero sufrió un paro respiratorio prolongado "
            "que le ocasionó secuelas neurológicas irreversibles. — "
            "La investigación de los especialistas de higiene laboral demostró que la concentración de xileno superaba en diez veces el límite permisible. "
            "La lección es clara y contundente: jamás se debe aplicar pintura sin el sistema de extracción funcionando a pleno rendimiento, "
            "y nunca se debe usar un respirador sin consultar previamente la Ficha de Datos de Seguridad del producto químico. — "
            "Un barbijo de polvo no te protege de un veneno gaseoso. — "
            "La seguridad... está en los detalles."
        ),
        "promptFoto": (
            "Industrial hygiene documentary photography, 35mm lens, 16:9 landscape aspect ratio. Inside an industrial spray paint booth. "
            "Yellow spray painting equipment, hoses, freshly painted steel machinery parts, exhaust ventilation grates on the floor. "
            "Dramatic atmospheric lighting with faint airborne paint mist, dual-cartridge organic vapor respirator hanging on a tool hook, photorealistic, no text."
        )
    },
    {
        "id": "030",
        "fecha": "25 JULIO",
        "fechaPublicacion": "2026-07-25",
        "expediente": "Expediente #030",
        "carpeta": "2010-07-25-derrame-oleoducto-enbridge",
        "titular": "IGNORAR LAS ALARMAS: DIECISIETE HORAS BOMBEANDO CRUDO AL RÍO",
        "palabraResaltada": "IGNORAR LAS ALARMAS",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Oleoducto Línea 6B, Río Kalamazoo, Michigan, EE.UU. - 2010",
        "tipoRiesgo": "Seguridad de Procesos / Ductos / Gestión de Alarmas",
        "parrafos": [
            "El 25 de julio de 2010, la Línea 6B de la compañía Enbridge se fracturó cerca de Marshall, Michigan, derramando más de tres millones de litros de crudo pesado sobre el río Kalamazoo.",
            "En la sala de control en Canadá, los operadores interpretaron erróneamente las alarmas de caída de presión como un fenómeno de burbuja de aire y continuaron bombeando crudo durante 17 horas.",
            "Fue el mayor derrame en tierra en la historia de Norteamérica. La investigación de la NTSB expuso fallas severas en gestión de alarmas, cultura operativa y sesgo de confirmación."
        ],
        "puntosClave": [
            {"icono": "bell-off", "titulo": "Gestión efectiva de alarmas", "texto": "Diseñar sistemas de control SCADA que prioricen alarmas críticas para evitar la fatiga o desensibilización del operador."},
            {"icono": "brain", "titulo": "Combatir el sesgo de confirmación", "texto": "Ante una alarma de pérdida de presión, asumir siempre el peor escenario (fuga real) hasta descartarlo en campo."},
            {"icono": "hand", "titulo": "Autoridad para detener la operación", "texto": "Garantizar que todo operador tenga la facultad indiscutible de parar el bombeo ante lecturas contradictorias."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de investigación de accidentes de ductos de la National Transportation Safety Board (NTSB/PAR-12/01) y EPA.",
        "guionReel": (
            "25 de julio de 2010. — En un humedal de Michigan, Estados Unidos... el oleoducto subterráneo Línea 6B sufrió una rotura de dos metros por corrosión y fatiga. — "
            "A cientos de kilómetros de allí, en la sala de control de la empresa... las pantallas del sistema SCADA comenzaron a titilar en rojo: "
            "la presión se desplomaba de golpe. — "
            "Pero los operadores creyeron que se trataba de una falsa alarma por burbujas en la línea. — "
            "Durante diecisiete horas consecutivas... y a lo largo de dos cambios de turno... siguieron bombeando crudo pesado a plena potencia. — "
            "Más de tres millones de litros de petróleo contaminaron sesenta kilómetros del río Kalamazoo en el peor desastre de ductos en tierra. — "
            "Nunca justifiques una alarma crítica sin verificar el terreno. — "
            "La seguridad... está en los detalles."
        ),
        "guionLargo": (
            "25 de julio de 2010. — En las cercanías del poblado de Marshall, en el estado de Michigan... "
            "un oleoducto de setenta y seis centímetros de diámetro enterrado bajo los humedales del río Kalamazoo "
            "transportaba más de veintiocho millones de litros diarios de betún crudo diluido proveniente de las arenas petrolíferas de Canadá. — "
            "El ducto... construido en la década del sesenta y conocido como la Línea 6B... "
            "había acumulado múltiples defectos de corrosión externa bajo tensión y desprendimiento de su recubrimiento protector de cinta plástica. "
            "A pesar de que las inspecciones internas mediante herramientas inteligentes habían detectado fisuras en el metal... "
            "las reparaciones fueron postergadas sucesivamente por la gerencia. — "
            "A las cinco y cincuenta y ocho de la tarde del domingo 25 de julio... la delgada pared del ducto no resistió más la presión interna. "
            "Una fractura longitudinal de dos metros de largo se abrió en el acero... y un chorro continuo de petróleo pesado comenzó a brotar hacia el subsuelo. — "
            "A cientos de kilómetros de distancia, en la moderna sala de control centralizado de Edmonton, Canadá... "
            "el sistema SCADA disparó de inmediato múltiples alarmas críticas de caída de presión y desbalance volumétrico. — "
            "Aquí se desató una de las fallas humanas y organizacionales más graves en la historia de la ingeniería de transporte de fluidos: "
            "los operadores de la sala de control cayeron en el llamado sesgo de confirmación. — "
            "Convencidos de que la línea estaba sufriendo un fenómeno hidráulico conocido como separación de columna o bolsa de aire... "
            "desestimaron las alarmas de rotura. "
            "En lugar de cerrar las válvulas de bloqueo de seccionamiento de emergencia... reiniciaron las bombas en dos oportunidades distintas... "
            "inyectando crudo a alta presión durante diecisiete horas consecutivas a través de dos cambios de turno completos. — "
            "Fueron los propios vecinos del río Kalamazoo quienes... alertados por un insoportable olor a gas y azufre... "
            "llamaron a los bomberos locales a la mañana siguiente para denunciar que el río se había vuelto completamente negro. — "
            "Más de tres millones doscientos mil litros de petróleo pesado cubrieron más de sesenta kilómetros de cauces fluviales, "
            "destruyendo la fauna, obligando a evacuar comunidades ribereñas y desatando una operación de limpieza ambiental "
            "que demandó más de mil doscientos millones de dólares y más de cinco años de trabajo continuo. — "
            "El lapidario informe de la Junta Nacional de Seguridad en el Transporte... la NTSB... "
            "comparó la cultura de la empresa con los inspectores de la serie animada de los Keystone Kops, exponiendo la ceguera organizacional: "
            "las alarmas no son ruidos molestos que deban apagarse o justificarse; son la última barrera de defensa de un proceso. — "
            "Ante una alarma de desbalance de presión... la regla de oro debe ser detener el bombeo y cerrar las válvulas de inmediato, "
            "asumiendo que existe una fuga real hasta que el personal en campo demuestre fehacientemente lo contrario. — "
            "En la sala de control... dudar de las alarmas cuesta millones y destruye el entorno. — "
            "La seguridad... está en los detalles."
        ),
        "promptFoto": (
            "Environmental documentary photography, 35mm lens, 16:9 landscape aspect ratio. The Kalamazoo River in Michigan after the Enbridge oil pipeline spill, 2010. "
            "Heavy dark crude oil slick floating on tranquil river water near marsh reeds and weeping willows. Yellow oil containment booms stretched across the river bend. "
            "Atmospheric misty morning, photorealistic National Geographic investigative style, no text."
        )
    },
    {
        "id": "031",
        "fecha": "26 JULIO",
        "fechaPublicacion": "2026-07-26",
        "expediente": "Expediente #031",
        "carpeta": "2015-07-26-caida-techo-chapa-traslucida",
        "titular": "PISAR SOBRE LO INVISIBLE: LA CHAPA PLÁSTICA QUE CEDIO AL VACÍO",
        "palabraResaltada": "LA CHAPA PLÁSTICA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Cubierta de Galpón Industrial - 2015",
        "tipoRiesgo": "Trabajo en Altura / Superficies Frágiles",
        "parrafos": [
            "El 26 de julio de 2015, un operario de mantenimiento realizaba tareas de sellado de goteras en la cubierta de un galpón industrial a nueve metros de altura.",
            "Para desplazarse sobre el techo, caminó directamente sobre las chapas sin utilizar tablones de reparto de carga ni estar anclado a una línea de vida horizontal certificada.",
            "Pisó inadvertidamente una placa traslúcida de fibra de vidrio envejecida por el sol. La chapa plástica quebradiza se partió bajo su peso, provocando una caída libre fatal al vacío."
        ],
        "puntosClave": [
            {"icono": "footprints", "titulo": "Tablones de reparto de carga", "texto": "Jamás pisar directamente sobre chapas de techo; utilizar pasarelas o tablones apoyados sobre la estructura resistente."},
            {"icono": "shield-alert", "titulo": "Señalizar y proteger placas traslúcidas", "texto": "Pintar o colocar mallas metálicas resistentes anticaídas por encima o por debajo de todo tragaluz frágil."},
            {"icono": "cable", "titulo": "Línea de vida horizontal continua", "texto": "El arnés debe estar anclado permanentemente a un cable de acero certificado durante toda la permanencia en cubierta."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: estadísticas de fatalidades en techos de OSHA 1926.501, normas técnicas del INSST España sobre superficies frágiles y SRT Argentina.",
        "guionReel": (
            "26 de julio de 2015. — En el techo de un enorme galpón industrial... un trabajador de mantenimiento reparaba goteras a nueve metros sobre el suelo. — "
            "El techo combinaba chapas de chapa galvanizada con chapas plásticas traslúcidas de fibra de vidrio para dejar pasar la luz natural. — "
            "Con los años... la radiación solar y la intemperie habían vuelto el plástico tan quebradizo como una cáscara de huevo. — "
            "El trabajador dio un paso hacia atrás... y apoyó todo su peso sobre la chapa plástica. — "
            "La placa se partió en pedazos en un instante. — "
            "Sin línea de vida a la cual estar anclado... el operario cayó al vacío contra el piso de hormigón. — "
            "Los techos no son pisos. En superficies frágiles... anclaje continuo y pasarelas de madera. — "
            "La seguridad... está en los detalles."
        ),
        "guionLargo": (
            "26 de julio de 2015. — En un parque logístico e industrial... un equipo de mantenimiento edilicio "
            "tenía asignada la tarea de reparar filtraciones de agua y goteras en la cubierta superior de un depósito de almacenamiento de mercaderías. — "
            "A más de nueve metros sobre el suelo de hormigón... el techo a dos aguas estaba construido con chapas sinusoidales de chapa cincada... "
            "intercaladas cada varios metros con placas traslúcidas de poliéster y fibra de vidrio... "
            "diseñadas originalmente para permitir el ingreso de luz natural diurna hacia el interior del galpón. — "
            "Las cubiertas industriales con tragaluces de plástico constituyen una de las mayores trampas mortales en los trabajos de mantenimiento. "
            "Cuando son nuevas... las chapas de fibra de vidrio tienen cierta flexibilidad... "
            "pero con el paso de los años... la exposición constante a los rayos ultravioleta del sol, los cambios bruscos de temperatura y el granizo "
            "degradan los polímeros plásticos, volviéndolos extremadamente quebradizos y frágiles. "
            "Además... el polvo ambiental acumulado en la superficie hace que con el tiempo la chapa plástica se ensucie y tome un color grisáceo muy similar "
            "al de las chapas de metal linderas, volviéndose visualmente casi indistinguible a los ojos del operario. — "
            "Esa mañana... el trabajador caminaba por la cubierta acarreando un balde con sellador asfáltico y una brocha. "
            "No se habían instalado líneas de vida horizontales temporarias de cable de acero en la cumbrera del techo... "
            "y no se habían colocado tablones de madera o pasarelas de aluminio para repartir el peso del cuerpo entre las correas estructurales. — "
            "El operario llevaba puesto su arnés de seguridad... pero el cabo de amarre colgaba suelto a un costado de su pierna "
            "porque no encontraba ningún punto de anclaje certificado a su alcance. — "
            "Al concentrarse en pintar una unión de chapas... dio un paso hacia atrás para observar el trabajo. "
            "Su pie derecho pisó directamente en el centro de una chapa traslúcida envejecida. — "
            "El plástico no ofreció la más mínima resistencia estructural. Se desintegró al instante en cientos de astillas. — "
            "El trabajador atravesó el techo en una fracción de segundo, cayendo en picada desde nueve metros de altura "
            "hacia el interior del depósito sin que nada frenara su trayectoria. — "
            "El impacto contra la losa de hormigón armado de la planta baja fue letal de forma inmediata. — "
            "La investigación oficial de los inspectores de trabajo evidenció que el trabajo se autorizó sin un permiso de trabajo en altura "
            "y sin un análisis de trabajo seguro que identificara la presencia de superficies frágiles. — "
            "La normativa internacional de prevención en cubiertas es categórica: jamás se debe pisar directamente sobre las chapas de un techo. "
            "Todo tránsito exige pasarelas de distribución de carga apoyadas sobre las vigas resistentes, redes de protección anticaídas por debajo "
            "y una línea de vida continua donde el trabajador permanezca anclado de forma ininterrumpida. — "
            "Un tragaluz no es un piso: es un agujero esperando que alguien lo pise. — "
            "La seguridad... está en los detalles."
        ),
        "promptFoto": (
            "Documentary construction photography, 35mm lens, 16:9 landscape aspect ratio. The vast roof of an industrial warehouse showing galvanized metal corrugated sheets "
            "interspersed with weathered, yellowed fiberglass translucent skylight panels. 9 meters high against a pale morning sky, safety harness line, "
            "wooden walk boards, industrial maintenance setting, realistic National Geographic style, no text."
        )
    },
    {
        "id": "032",
        "fecha": "27 JULIO",
        "fechaPublicacion": "2026-07-27",
        "expediente": "Expediente #032",
        "carpeta": "2019-07-27-arco-electrico-tablero-tension",
        "titular": "EL RELÁMPAGO EN EL TABLERO: EL ARCO ELÉCTRICO QUE CONSUMIÓ TODO",
        "palabraResaltada": "EL RELÁMPAGO EN EL TABLERO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Subestación y Tablero Eléctrico Industrial - 2019",
        "tipoRiesgo": "Riesgo Eléctrico / Arc Flash (Arco Eléctrico)",
        "parrafos": [
            "El 27 de julio de 2019, un electricista industrial intervenía una celda de distribución de 480 voltios en una subestación tras el disparo de un disyuntor principal.",
            "Para no detener la planta completa, abrió la puerta del tablero energizado sin portar traje de protección contra arco eléctrico (Arc Flash) ni pantalla facial certificada.",
            "Al insertar una barra de medición, se produjo un cortocircuito que desató una explosión de arco a más de diez mil grados, causando quemaduras de tercer grado en el setenta por ciento del cuerpo."
        ],
        "puntosClave": [
            {"icono": "power", "titulo": "Desenergizar y verificar ausencia de tensión", "texto": "Aplicar las 5 Reglas de Oro eléctricas: cortar, bloquear, verificar tensión cero, poner a tierra y señalizar."},
            {"icono": "shield-check", "titulo": "EPP específico para Arc Flash", "texto": "Usar traje ignífugo con clasificación cal/cm2 acorde al estudio de energía incidente, guantes dieléctricos y careta."},
            {"icono": "zap", "titulo": "Estudios de arco eléctrico en tableros", "texto": "Etiquetar cada tablero con la frontera de aproximación segura y la categoría de riesgo de arco eléctrico según NFPA 70E."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: normativas de seguridad eléctrica en lugares de trabajo NFPA 70E, OSHA 1910 Subpart S y guías técnicas IEEE 1584.",
        "guionReel": (
            "27 de julio de 2019. — En una subestación eléctrica industrial... un disyuntor principal de cuatrocientos ochenta voltios saltó por sobrecarga. — "
            "Para no frenar los motores de la fábrica... un técnico electricista abrió el cofre metálico del tablero con las barras colectoras vivas y energizadas. — "
            "Llevaba puesta una remera de algodón común y guantes finos de trabajo. — "
            "Al acercar una herramienta... se generó un cortocircuito bifásico. — "
            "En una milésima de segundo... el aire se convirtió en plasma incandescente a más de quince mil grados centígrados. "
            "La explosión de arco eléctrico vaporizó el cobre en una ráfaga térmica que envolvió por completo al trabajador. — "
            "La electricidad no solo electrocuta: quema como el sol. Desenergizar antes de abrir salva vidas. — "
            "La seguridad... está en los detalles."
        ),
        "guionLargo": (
            "27 de julio de 2019. — En la sala de subestación eléctrica principal de una planta manufacturera continua... "
            "el sistema de distribución eléctrica alimentaba a decenas de motores de gran potencia a través de un centro de control de motores de cuatrocientos ochenta voltios. — "
            "Hacia el final del turno de trabajo... uno de los interruptores automáticos principales disparó por sobrecarga, "
            "dejando fuera de servicio una de las líneas secundarias de producción. — "
            "El electricista de turno acudió a la subestación para evaluar la causa del disparo. "
            "En el riesgo eléctrico industrial existe un fenómeno mucho más violento y destructivo que el choque eléctrico convencional: "
            "el llamado arco eléctrico o arc flash. — "
            "Un arco eléctrico ocurre cuando una corriente de cortocircuito ioniza el aire entre dos conductores o entre un conductor y tierra. "
            "En una fracción de segundo... el aire se convierte en plasma conductor de electricidad alcanzando temperaturas que pueden superar los quince mil grados centígrados... "
            "más de tres veces la temperatura de la superficie del sol. — "
            "A esa temperatura... los metales sólidos como el cobre y el aluminio se vaporizan de forma instantánea, expandiendo su volumen por más de sesenta y siete mil veces. "
            "Esta violenta expansión genera una onda de choque explosiva conocida como arc blast... "
            "que dispara esquirlas metálicas derretidas a velocidades supersónicas y emite una intensa radiación térmica y lumínica capaz de provocar ceguera instantánea. — "
            "El protocolo de seguridad eléctrica basado en la norma NFPA 70E establecía con absoluta claridad la regla de oro: "
            "para abrir una celda y trabajar en su interior, se debe desenergizar aguas arriba, colocar candados de bloqueo LOTO, "
            "verificar la ausencia total de tensión con un multímetro certificado y portar un traje ignífugo completo con careta facial clasificada para la energía incidente del tablero. — "
            "Sin embargo... ante la urgencia por rearmar el interruptor sin detener los otros sectores de la planta... "
            "el técnico abrió la puerta metálica de la celda con las barras energizadas a cuatrocientos ochenta voltios. "
            "Vestía únicamente una camisa de tela común, pantalón de jean y guantes finos de nitrilo. — "
            "Al introducir una punta de prueba metálica para verificar los contactos... la herramienta resbaló accidentalmente entre dos fases contiguas. — "
            "El cortocircuito franco desató un relámpago ensordecedor. "
            "Una gigantesca bola de fuego de plasma incandescente estalló en el rostro y el pecho del electricista... "
            "lanzándolo varios metros hacia atrás contra la pared de la sala. — "
            "La radiación térmica inflamó su ropa sintética de inmediato, fundiéndola sobre su piel. "
            "El trabajador sufrió quemaduras gravísimas de segundo y tercer grado en el setenta por ciento del cuerpo y daños severos en sus vías respiratorias por inhalar aire sobrecalentado. — "
            "Sobrevivió gracias a meses de internación en terapia intensiva en el centro de quemados... pero con secuelas físicas y cicatrices permanentes para el resto de su vida. — "
            "La investigación determinó que jamás debió abrirse un tablero bajo tensión sin aplicar las cinco reglas de oro de la seguridad eléctrica. "
            "La electricidad no da una segunda oportunidad. Desenergizar antes de intervenir y utilizar EPP ignífugo certificado contra arco eléctrico "
            "es la única defensa real frente al poder destructivo de la energía eléctrica. — "
            "La seguridad... está en los detalles."
        ),
        "promptFoto": (
            "Industrial electrical safety documentary photography, 35mm lens, 16:9 landscape aspect ratio. A heavy 480V motor control center electrical switchgear panel in a substation. "
            "Open steel cabinet door revealing insulated busbars, digital power meters, warning Arc Flash hazard warning labels, "
            "cal/cm2 rating label, lock-out tag-out hasp with red padlocks. Dark dramatic electrical room lighting, crisp photorealistic style, no text."
        )
    }
]

def procesar_lote_2(kokoro_instance):
    """Procesa las 10 historias del Lote 2."""
    procesadas = []

    for h in LOTE_2_DATA:
        carpeta_nombre = h["carpeta"]
        target_dir = os.path.join(ASSETS_DIR, carpeta_nombre)
        os.makedirs(target_dir, exist_ok=True)

        print(f"\n=======================================================")
        print(f"▶ Procesando: {h['expediente']} ({h['fecha']}) - {h['titular'][:45]}...")
        print(f"=======================================================")

        # 1. README.md
        readme_content = f"""# Efeméride: {h['fechaPublicacion']} {h['carpeta']}

Guarda aquí los archivos de esta historia:

- `portada.png`: imagen principal.
- `historia.m4a`: audio narrado extendido (app).
- `guion-reel.txt`: guion corto de 1 minuto para redes.
- `prompt-portada.txt`: prompt para generar imagen en Gemini Imagen 3.
- `contenido-completo.md`: texto completo original de la efeméride.

Rutas configuradas en `historiaDelDia`:

```js
carpetaAssets: "assets/efemerides/{carpeta_nombre}/",
imagen: "portada.png",
audio: "historia.m4a",
```

Datos base:

- Expediente: `{h['expediente']}`
- Fecha: `{h['fecha']}`
- Lugar: `{h['etiquetaImagen']}`
- Titular: `{h['titular']}`
- Tipo de Riesgo: `{h['tipoRiesgo']}`
"""
        with open(os.path.join(target_dir, "README.md"), "w", encoding="utf-8") as f:
            f.write(readme_content)

        # 2. guion-reel.txt
        with open(os.path.join(target_dir, "guion-reel.txt"), "w", encoding="utf-8") as f:
            f.write(h["guionReel"])

        # 3. prompt-portada.txt
        with open(os.path.join(target_dir, "prompt-portada.txt"), "w", encoding="utf-8") as f:
            f.write(h["promptFoto"])

        # 4. contenido-completo.md
        md_content = f"""# 📁 ARCHIVO HSE

## {h['expediente']}

# 📅 {h['fechaPublicacion']}

# **"{h['titular']}"**

### 📍 {h['etiquetaImagen']}
**Tipo de Riesgo:** {h['tipoRiesgo']}

---

# ¿Qué ocurrió?

{h['parrafos'][0]}

{h['parrafos'][1]}

{h['parrafos'][2]}

---

# ⏱️ En cuestión de minutos...

{h['guionLargo'].replace(' — ', '\n\n').replace('... ', '...\n\n')}

---

# 🦺 Tres puntos clave para controlar un evento similar

### 1️⃣ {h['puntosClave'][0]['titulo']}
{h['puntosClave'][0]['texto']}

---

### 2️⃣ {h['puntosClave'][1]['titulo']}
{h['puntosClave'][1]['texto']}

---

### 3️⃣ {h['puntosClave'][2]['titulo']}
{h['puntosClave'][2]['texto']}

---

# 💬 Para reflexionar

{h['pregunta']}

> **"La seguridad está en los detalles."** — *Focus HSE*

---

# 📚 Fuentes

• {h['fuente']}
"""
        with open(os.path.join(target_dir, "contenido-completo.md"), "w", encoding="utf-8") as f:
            f.write(md_content)

        # 5. Portada gráfica PNG
        portada_path = os.path.join(target_dir, "portada.png")
        if not os.path.exists(portada_path):
            crear_portada_grafica_lote2(h, portada_path)
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
        print(f"  ✓ Audio listo: {m4a_path} ({texto_duracion})")

        procesadas.append(h)

    return procesadas

def crear_portada_grafica_lote2(historia, output_path):
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
    """Inyecta las historias del Lote 2 en index.html antes del cierre del array historias."""
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

    print("\n✓ index.html actualizado exitosamente con los 10 nuevos expedientes (#023 a #032).")
    return True

def main():
    print("Iniciando motor Kokoro para Lote 2 (#023 a #032)...")
    kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

    procesadas = procesar_lote_2(kokoro)

    if inyectar_en_index_html(procesadas):
        print(f"\n🎉 ¡LOTE 2 COMPLETADO AL 100%! ({len(procesadas)} historias procesadas)")

if __name__ == "__main__":
    main()
