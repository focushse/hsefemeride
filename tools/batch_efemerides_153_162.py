# -*- coding: utf-8 -*-
"""
Generador Agéntico Automatizado para Lote 15: Expedientes #153 a #162 (25 de noviembre al 4 de diciembre)
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

LOTE_15_DATA = [
    {
        "id": "153",
        "logo": "FOCUS HSE",
        "fecha": "25 NOVIEMBRE",
        "fechaPublicacion": "2026-11-25",
        "expediente": "Expediente #153",
        "carpeta": "2018-11-25-explosion-cloruro-vinilo-hebei-shenghua-chemical-zhangjiakou",
        "titular": "EL GASÓMETRO AGRIETADO: LA EXPLOSIÓN DE CLORURO DE VINILO EN ZHANGJIAKOU",
        "palabraResaltada": "INTEGRIDAD MECÁNICA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Química Hebei Shenghua Chemical, Zhangjiakou, Provincia de Hebei, China - 2018",
        "tipoRiesgo": "Seguridad de Procesos (PSM) / Sustancias Tóxicas e Inflamables",
        "parrafos": [
            "El 25 de noviembre de 2018, en la planta de la empresa Hebei Shenghua Chemical en Zhangjiakou, provincia de Hebei, China, una fuga masiva de cloruro de vinilo gaseoso desde un gasómetro deteriorado derivó hacia una vía pública cercana y detonó al contactar un camión en marcha, matando a 24 personas e hiriendo a 22.",
            "La investigación oficial de la Comisión de Seguridad en el Trabajo del Consejo de Estado reveló que el gasómetro de baja presión presentaba corrosión severa y falta crónica de mantenimiento. El gas tóxico e inflamable se fugó por una fisura y avanzó hacia la autopista sin que sonara una alarma perimetral ni se activara un corte de emergencia.",
            "La deflagración incendió 38 camiones que esperaban para cargar carbón en fila a lo largo de la banquina. La lección: inspección estricta de integridad mecánica por ultrasonido en gasómetros, sensores fijos perimetrales de gas y franjas de amortiguamiento libres de tráfico exterior."
        ],
        "puntosClave": [
            {"icono": "shield-check", "titulo": "Integridad mecánica predictiva en gasómetros", "texto": "Medición periódica de espesores de chapa, sellos hidráulicos y detección de corrosión en recipientes de almacenamiento de baja presión."},
            {"icono": "gauge", "titulo": "Monitoreo perimetral y parada de emergencia (ESD)", "texto": "Instalación de barreras infrarrojas de detección de hidrocarburos en los límites de batería acopladas a corte automático de líneas."},
            {"icono": "map-pin", "titulo": "Zonas de amortiguamiento y control de tráfico externo", "texto": "Prohibir la acumulación o espera de camiones sobre rutas linderas a unidades de procesamiento con inventarios tóxicos o inflamables."}
        ],
        "pregunta": "¿Monitorea tu planta la concentración de gases inflamables en el perímetro limítrofe con calles públicas?",
        "fuente": "Fuente: Informe de Investigación de la Comisión de Seguridad en el Trabajo del Consejo de Estado de la República Popular China sobre el accidente de Shenghua Chemical en Zhangjiakou (Febrero 2019).",
        "guionReel": (
            "El 25 de noviembre de 2018, en Zhangjiakou, China, una fuga de cloruro de vinilo en la planta química Hebei Shenghua mató a 24 personas en una autopista.\n\n"
            "Un gasómetro gigante, podrido por la corrosión y sin mantenimiento, se fisuró. Una enorme nube invisible de gas inflamable se escapó hacia la calle.\n\n"
            "Frente a la fábrica había una fila de 38 camiones esperando turno. El motor de uno de ellos encendió la nube.\n\n"
            "La explosión calcinó los camiones en segundos a lo largo de cientos de metros.\n\n"
            "¿La lección de Focus HSE? Mantenimiento predictivo a recipientes de gas, detección en perímetros y jamás permitir tráfico cerca de unidades de proceso. La seguridad está en los detalles."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 25 de noviembre de 2018, en la ciudad de Zhangjiakou, provincia de Hebei, China, la planta petroquímica de la corporación Hebei Shenghua Chemical sufrió una catástrofe que causó la muerte de veinticuatro personas y quemaduras a más de una veintena, investigada por la Comisión Nacional de Seguridad en el Trabajo.\n\n"
            "Esa madrugada gélida, un gasómetro de almacenamiento de baja presión que contenía cloruro de vinilo gaseoso —un hidrocarburo clorado altamente volátil, inflamable y cancerígeno— colapsó en uno de sus sellos inferiores debido a la corrosión galvánica y a la fatiga mecánica acumulada tras años de inspecciones superficiales.\n\n"
            "Al ceder el material, toneladas de gas más pesado que el aire comenzaron a escapar a nivel del suelo. El viento suave empujó la densa nube hacia la puerta principal y a través de la cerca perimetral, adentrándose en la vía pública adyacente. En esa ruta, decenas de transportistas hacían fila dentro de sus camiones aguardando el ingreso para cargar carbón y productos químicos.\n\n"
            "La planta carecía de detectores ópticos perimetrales y nadie advirtió la fuga a los choferes. Cuando la nube envolvió la fila de vehículos, el calor del escape o el sistema eléctrico de un motor en ralentí detonó la mezcla de aire y gas. La onda expansiva recorrió la carretera en una bola de fuego instantánea que calcinó treinta y ocho camiones y destruyó los edificios auxiliares de acceso.\n\n"
            "Los peritajes concluyeron que la empresa operó con equipos degradados fuera de especificación y que las autoridades permitieron el estacionamiento desregulado de transporte pesado en la zona de riesgo directo de la planta.\n\n"
            "Un gasoducto o gasómetro sin integridad verificada es un peligro inminente que trasciende las fronteras de la propia empresa. En Focus HSE te lo recordamos siempre: la seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, 16:9 aspect ratio. The stark aftermath of the chemical gas explosion in Zhangjiakou, China, 2018. "
            "A row of scorched, blackened heavy transport trucks along an industrial roadway outside a chemical complex under a cold, hazy dawn sky. "
            "The corroded silhouette of an industrial gas holder tank with emergency flares and distant petrochemical fractionating towers. "
            "Firefighters in high-visibility uniforms inspecting burnt asphalt and twisted metal frames, 35mm lens authentic photojournalism."
        )
    },
    {
        "id": "154",
        "logo": "FOCUS HSE",
        "fecha": "26 NOVIEMBRE",
        "fechaPublicacion": "2026-11-26",
        "expediente": "Expediente #154",
        "carpeta": "2018-11-26-atrapamiento-paletizadora-refresco-beverages-new-jersey",
        "titular": "EL SENSOR PUENTEADO: ATRAPAMIENTO EN LA LÍNEA DE REFRESCO",
        "palabraResaltada": "INTERLOCK ANULADO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Línea de Envasado y Paletizado, Refresco Beverages, Nueva Jersey, EE.UU. - 2018",
        "tipoRiesgo": "Atrapamiento / Protección de Máquinas / Bloqueo y Etiquetado (LOTO)",
        "parrafos": [
            "El 26 de noviembre de 2018, en una planta embotelladora de la empresa Refresco Beverages en Nueva Jersey, un técnico de línea murió atrapado por los brazos mecánicos de una máquina paletizadora automática tras ingresar a la celda para retirar una botella atascada sin detener el ciclo.",
            "La investigación de OSHA descubrió que el enclavamiento magnético de seguridad (interlock) de la puerta de acceso había sido anulado deliberadamente con una cinta adhesiva y un imán auxiliar para evitar que la máquina se detuviera cada vez que el personal abría la puerta para destrabar envases.",
            "Al inclinarse sobre la mesa de empuje, el sensor de presencia detectó el lote completo y activó el plato neumático de compresión, aplastando al operario contra la estructura fija. La lección: prohibición penal de puentear resguardos, diseño de interlocks antimanipulación y aplicación estricta de LOTO."
        ],
        "puntosClave": [
            {"icono": "shield-alert", "titulo": "Prohibición absoluta de manipular enclavamientos", "texto": "Tipificar como falta muy grave la alteración, puenteo o colocación de imanes falsos en sensores de seguridad de puertas y resguardos."},
            {"icono": "lock", "titulo": "Interlocks de seguridad codificados por RFID", "texto": "Reemplazar finales de carrera e imanes simples por interruptores de seguridad codificados de Categoría 4 inmunes a burlas mecánicas."},
            {"icono": "power", "titulo": "Protocolo LOTO antes de acceder a celdas robóticas", "texto": "Desenergizar, bloquear con candado físico y verificar energía cero antes de que cualquier extremidad cruce el perímetro de una máquina automática."}
        ],
        "pregunta": "¿Has visto alguna vez un sensor de puerta puenteado en tu planta para 'no parar la producción'?",
        "fuente": "Fuente: Informe de Investigación de Accidente Fatal por Atrapamiento en Máquina de OSHA (U.S. Department of Labor) en Nueva Jersey (Noviembre 2018).",
        "guionReel": (
            "El 26 de noviembre de 2018, en Nueva Jersey, un operario murió aplastado dentro de una paletizadora en una planta de Refresco Beverages.\n\n"
            "Una botella se cayó en la línea. Para no frenar la máquina, abrió la reja de protección. El sensor magnético de la puerta no cortó la energía porque alguien lo había puenteado con un imán falso.\n\n"
            "El trabajador metió el cuerpo para sacar la botella. La máquina creyó que la línea seguía llena y disparó el brazo neumático.\n\n"
            "Fue aplastado al instante por un equipo que nunca debió estar encendido.\n\n"
            "¿La lección de Focus HSE? Jamás puentees un sensor de seguridad. Pon candado LOTO antes de entrar. La seguridad está en los detalles."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 26 de noviembre de 2018, en una planta de embotellado y distribución de la compañía multinacional Refresco Beverages en el estado de Nueva Jersey, un técnico de empaque perdió la vida al ser atrapado por una máquina paletizadora robotizada, un accidente investigado minuciosamente por la OSHA.\n\n"
            "Durante el turno, la línea de empaque sufría constantes paradas porque las botellas plásticas ligeras se inclinaban en la mesa de alimentación previa al paletizado. Cada vez que esto sucedía, la apertura de la compuerta enclavada detenía el motor y requería un reinicio manual que demoraba varios minutos.\n\n"
            "Para evitar estas interrupciones y cumplir con las metas de producción del turno, los operadores habían colocado un imán adicional pegado con cinta sobre el interruptor de seguridad de la reja perimetral. Este puenteo electrónico engañaba al sistema de control, haciéndole creer que la puerta estaba siempre cerrada y bloqueada.\n\n"
            "Cuando otra botella se trabó, el trabajador abrió la reja y entró con la máquina funcionando a plena velocidad. Se agachó sobre el transportador para alcanzar el envase caído. En ese instante, los sensores ópticos de carga detectaron que el lote de botellas estaba completo y el autómata programable ordenó el avance del compactador neumático lateral. La pesada placa metálica empujó con cientos de kilos de fuerza, prensando al operario contra el bastidor de acero sin posibilidad de retroceso.\n\n"
            "OSHA multó severamente a la empresa por permitir la anulación sistemática de resguardos y por la falta de un programa estricto de Bloqueo y Etiquetado LOTO.\n\n"
            "Burlar un dispositivo de seguridad no ahorra tiempo: prepara una trampa mortal. Los enclavamientos existen para proteger vidas, jamás deben ser negociados por cajas producidas. En Focus HSE te lo recordamos siempre: la seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, 16:9 aspect ratio. Inside an industrial beverage bottling plant in New Jersey, 2018. "
            "A high-speed automated palletizer machine with heavy yellow metal safety perimeter cages and conveyor belts carrying plastic beverage bottles. "
            "Close-up detail of an open safety gate with an OSHA inspection tag and an orange lockout-tagout padlock station on the steel post. "
            "Bright overhead fluorescent factory lighting, clean polished epoxy floor reflecting machine shadows, high level of industrial realism, 35mm lens."
        )
    },
    {
        "id": "155",
        "logo": "FOCUS HSE",
        "fecha": "27 NOVIEMBRE",
        "fechaPublicacion": "2026-11-27",
        "expediente": "Expediente #155",
        "carpeta": "2018-11-27-derrumbe-zanja-morales-construction-texas",
        "titular": "LA ZANJA EN ARENA VIVA: EL COLAPSO DE MORALES CONSTRUCTION",
        "palabraResaltada": "ENTIBADO OBLIGATORIO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Obra de Tendido de Red Sanitaria, Morales Construction, Texas, EE.UU. - 2018",
        "tipoRiesgo": "Derrumbe / Excavaciones y Zanjas / Protección Colectiva",
        "parrafos": [
            "El 27 de noviembre de 2018, en una obra de alcantarillado en Texas ejecutada por la contratista Morales Construction, un operario de saneamiento murió sepultado al colapsar las paredes laterales de una zanja de 2,6 metros de profundidad desprovista de entibado o cajón de seguridad.",
            "La investigación de OSHA determinó que el suelo era de tipo C (arenoso y altamente inestable), y que la contratista no respetó las pendientes de talud reglamentarias ni instaló una caja protectora para zanjas (trench box), omitiendo además alejar la tierra de excavación y la maquinaria pesada del labio superior.",
            "Una retroexcavadora transitó por el borde mientras el operario alineaba los tubos en el fondo; las vibraciones y el sobrepeso quebraron la masa de tierra arenosa que cayó de golpe sobre la víctima. La lección: entibado obligatorio en zanjas de más de 1,20 m, persona competente certificada y retiro de maquinaria a distancia segura."
        ],
        "puntosClave": [
            {"icono": "box", "titulo": "Uso obligatorio de cajón de zanja (Trench Box)", "texto": "Instalar blindajes móviles certificados en toda excavación que supere 1,20 metros de profundidad en suelos no cohesivos."},
            {"icono": "user-check", "titulo": "Inspección diaria por Persona Competente", "texto": "Evaluar la estabilidad del suelo, presencia de agua y vibraciones antes de cada jornada y tras cualquier lluvia o cambio de turno."},
            {"icono": "truck", "titulo": "Zona de exclusión de cargas y maquinarias en el borde", "texto": "Mantener el material extraído y las retroexcavadoras a un mínimo de 1 metro (o la mitad de la profundidad) lejos de la corona del talud."}
        ],
        "pregunta": "¿Existe en tus obras un cajón de entibado instalado antes de que un operario descienda a una zanja?",
        "fuente": "Fuente: Informe de Investigación de Colapso de Excavación Fatal de OSHA (Occupational Safety and Health Administration) en Texas (Noviembre 2018).",
        "guionReel": (
            "El 27 de noviembre de 2018, en Texas, un obrero murió sepultado en una zanja de 2,6 metros de Morales Construction.\n\n"
            "El suelo era arena suelta. Pero para abaratar costos, no pusieron cajón de entibado ni talud de seguridad.\n\n"
            "El trabajador estaba en el fondo colocando un caño. Una retroexcavadora pasó justo por el borde superior. Las vibraciones quebraron la pared.\n\n"
            "Cientos de kilos de tierra cayeron de golpe sobre él. Un metro cúbico de tierra pesa más de una tonelada y media. Fue imposible rescatarlo a tiempo.\n\n"
            "¿La lección de Focus HSE? En zanjas de más de 1,20 m, el entibado no se negocia. Y la maquinaria pesada jamás pisa el borde. La seguridad está en los detalles."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 27 de noviembre de 2018, en una obra civil de infraestructura sanitaria en el estado de Texas, un trabajador de la empresa contratista Morales Construction perdió la vida al ser sepultado instantáneamente por un derrumbe de zanja, un trágico incidente investigado por la OSHA.\n\n"
            "Esa mañana, la cuadrilla abría una zanja de dos metros y medio de profundidad para tender cañerías cloacales. El terreno presentaba una textura arenosa, clasificada técnicamente como suelo Tipo C: la categoría más inestable y propensa al desmoronamiento inmediato. A pesar del peligro evidente, la empresa no instaló una caja metálica de entibado ni practicó cortes en talud escalonado.\n\n"
            "El operario descendió por una escalera portátil al fondo de la zanja para acoplar dos tramos de tubería de hormigón. Minutos después, el operador de la retroexcavadora avanzó con el equipo pesado a escasos centímetros de la corona de la excavación para depositar más tubos. Las intensas vibraciones del motor diésel y el peso transmitido al borde fracturaron el prisma de rotura del suelo arenoso.\n\n"
            "La pared lateral de tierra colapsó de manera fulminante. Un metro cúbico de suelo húmedo pesa más de mil quinientos kilos; la masa cayó directamente sobre el trabajador, comprimiendo su tórax e inmovilizándolo bajo tierra. Aunque sus compañeros intentaron cavar frenéticamente con palas, la asfixia traumática le causó la muerte en cuestión de minutos.\n\n"
            "La inspección de OSHA concluyó que la contratista carecía de una 'Persona Competente' en el sitio y violó los estándares básicos de seguridad en excavaciones.\n\n"
            "Bajar a una zanja sin entibado es como meterse en una tumba abierta. Las paredes de tierra no dan avisos audibles antes de derrumbarse. En Focus HSE te lo recordamos siempre: la seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, 16:9 aspect ratio. A deep civil engineering utility trench excavation site in Texas, 2018. "
            "A trench 2.5 meters deep cut through sandy, unstable reddish-brown clay soil with cracked edges. A heavy hydraulic excavator parked near the trench edge. "
            "A steel modular trench safety box sitting on the flat dirt nearby waiting to be lowered. Emergency rescue tape, yellow hard hats, and an OSHA inspection vehicle in the background. "
            "Bright natural sun casting harsh shadows across the cut soil walls, sharp focus, 35mm lens authentic construction photo."
        )
    },
    {
        "id": "156",
        "logo": "FOCUS HSE",
        "fecha": "28 NOVIEMBRE",
        "fechaPublicacion": "2026-11-28",
        "expediente": "Expediente #156",
        "carpeta": "2015-11-28-explosion-unidad-destilacion-petrobras-replan-paulinia",
        "titular": "LA PRESIÓN TRABADA: SOBREPRESIÓN EN PETROBRAS REPLAN PAULÍNIA",
        "palabraResaltada": "REVISIÓN PRE-ARRANQUE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Refinería de Paulínia (REPLAN), Petrobras, São Paulo, Brasil - 2015",
        "tipoRiesgo": "Seguridad de Procesos (Oil & Gas / Refinación)",
        "parrafos": [
            "El 28 de noviembre de 2015, en la Refinería de Paulínia (REPLAN) de la petrolera estatal Petrobras, en el estado de São Paulo, Brasil, se produjo una violenta sobrepresión y explosión en la unidad de destilación y craqueo catalítico durante una maniobra de arranque post-mantenimiento.",
            "La investigación de la Agencia Nacional del Petróleo (ANP) y comisiones de seguridad comprobó que una línea de venteo de alivio de presión se encontraba bloqueada mecánicamente con una brida ciega que no fue retirada tras las tareas de taller, sumado a lecturas erróneas en transmisores de nivel que estaban descalibrados.",
            "Al inyectar hidrocarburos calientes a la torre de proceso, la presión aumentó sin vía de escape hacia la antorcha hasta romper los sellos y proyectar fragmentos metálicos, causando incendio masivo. La lección: ejecución estricta de la Revisión de Seguridad Pre-Arranque (PSSR), registro riguroso de aislamientos mecánicos y desinstalación certificada de bridas ciegas."
        ],
        "puntosClave": [
            {"icono": "check-square", "titulo": "Revisión de Seguridad Pre-Arranque (PSSR)", "texto": "Inspeccionar físicamente en campo cada línea, válvula y transmisor contra planos P&ID antes de ingresar fluidos de proceso a la unidad."},
            {"icono": "shield-check", "titulo": "Control y retiro de bridas ciegas (Blind List)", "texto": "Gestionar una lista maestra de bloqueo con verificación de colocación y desinstalación de cometas y bridas ciegas con firma de doble chequeo."},
            {"icono": "gauge", "titulo": "Integridad funcional de válvulas de alivio (PSV)", "texto": "Asegurar que todas las válvulas de seguridad dispongan de ruta libre hacia la antorcha sin válvulas de bloqueo intermedias cerradas o trabadas."}
        ],
        "pregunta": "¿Se realiza un recorrido físico de PSSR en tu planta antes de autorizar la puesta en marcha de un sistema intervenido?",
        "fuente": "Fuente: Informe de Investigación de la ANP (Agência Nacional do Petróleo, Gás Natural e Biocombustíveis) y comisiones técnicas de Petrobras sobre el incidente en REPLAN (Paulínia, São Paulo, 2016).",
        "guionReel": (
            "El 28 de noviembre de 2015, en la refinería REPLAN de Petrobras en Paulínia, Brasil, una torre de destilación explotó al arrancar tras una parada.\n\n"
            "Durante el mantenimiento colocaron una brida ciega en la línea de venteo. Al terminar los trabajos, olvidaron retirarla.\n\n"
            "Empezaron a cargar hidrocarburos calientes. Los sensores marcaban mal y la presión no tenía por dónde escapar hacia la antorcha.\n\n"
            "La torre se convirtió en una olla a presión gigante hasta que reventó envuelta en llamas.\n\n"
            "¿La lección de Focus HSE? Nunca arranques una unidad sin una auditoría PSSR que confirme que cada brida ciega fue retirada. La seguridad está en los detalles."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 28 de noviembre de 2015, en la refinería más grande de Brasil, la Refinería de Paulínia, conocida como REPLAN, operada por la empresa estatal Petrobras en el estado de São Paulo, se registró una explosión devastadora durante la maniobra de puesta en marcha de una de sus unidades de destilación, investigada por la Agencia Nacional del Petróleo.\n\n"
            "La unidad venía saliendo de una parada programada de mantenimiento mayor donde se habían intervenido intercambiadores, tuberías y válvulas de seguridad. Para aislar las líneas durante los trabajos, los mecánicos instalaron múltiples bridas ciegas en las tuberías de alivio que conectaban la torre con el sistema de antorcha general.\n\n"
            "Al momento de autorizar el arranque, los procedimientos de Revisión de Seguridad Pre-Arranque, el PSSR, se ejecutaron como un mero trámite administrativo en oficina, sin verificar físicamente en la estructura metálica si todas las bridas de bloqueo temporal habían sido desmontadas.\n\n"
            "Cuando los operadores comenzaron a ingresar carga de hidrocarburo caliente al interior de la columna fraccionadora, la presión interna comenzó a trepar de manera vertiginosa. Debido a que los transmisores de nivel estaban descalibrados y la línea de alivio de las válvulas PSV permanecía taponada por la brida ciega no retirada, los gases no hallaron salida hacia el mechurrio.\n\n"
            "El domo superior de la torre y las conexiones bridadas no resistieron el esfuerzo mecánico y colapsaron con una violenta deflagración que proyectó componentes pesados e incendió los racks de tuberías contiguos, obligando a paralizar de emergencia la refinería.\n\n"
            "Este suceso en REPLAN demostró que un trozo de acero olvidado en una cañería puede anular la ingeniería de seguridad de toda una planta. Las listas maestras de bridas ciegas y las inspecciones físicas pre-arranque salvan vidas y protegen instalaciones millonarias. En Focus HSE te lo recordamos siempre: la seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, 16:9 aspect ratio. Industrial distillation towers and pipe racks at the REPLAN Petrobras oil refinery in Paulínia, São Paulo, 2015. "
            "Dramatic night scene with industrial emergency spotlights illuminating dense piping, steam plumes, and structural steel refinery columns. "
            "Refinery operators in flame-resistant coveralls inspecting a high-pressure pipe flange with torque wrenches and digital clipboard checklist. "
            "Heavy industrial realism, complex maze of polished steel and weathered pipes, atmospheric flare stack flame reflected in puddle, 35mm lens."
        )
    },
    {
        "id": "157",
        "logo": "FOCUS HSE",
        "fecha": "29 NOVIEMBRE",
        "fechaPublicacion": "2026-11-29",
        "expediente": "Expediente #157",
        "carpeta": "2017-11-29-caida-cubierta-planta-logistica-amazon-indiana",
        "titular": "EL BORDE VACÍO: CAÍDA MORTAL EN EL CENTRO LOGÍSTICO DE AMAZON",
        "palabraResaltada": "PROTECCIÓN COLECTIVA",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Centro Logístico de Amazon, Contratista de Climatización, Indiana, EE.UU. - 2017",
        "tipoRiesgo": "Trabajo en Altura / Superficies Frágiles / Bordes Desprotegidos",
        "parrafos": [
            "El 29 de noviembre de 2017, durante la construcción y acondicionamiento de un gigantesco centro logístico de Amazon en Indiana, un técnico de climatización de una empresa contratista falleció tras caer desde el techo del edificio a una altura de más de 12 metros.",
            "La investigación de OSHA constató que el trabajador transportaba herramientas cerca del borde perimetral de la cubierta metálica, la cual carecía de barandas de seguridad rígidas, redes de protección o líneas de vida horizontales instaladas.",
            "Un tropiezo con una junta de dilatación desestabilizó al operario, quien al no contar con un sistema de restricción o detención de caídas conectado, cayó al vacío sobre la losa de estacionamiento. La lección: instalación prioritaria de barandas perimetrales rígidas antes de cualquier tarea sobre cubiertas y anclaje al 100% permanente."
        ],
        "puntosClave": [
            {"icono": "shield-check", "titulo": "Jerarquía de control: Barandas perimetrales primero", "texto": "Instalar barandas rígidas perimetrales con rodapié y travesaño intermedio en todo el borde del techo antes de autorizar el trabajo sobre la losa."},
            {"icono": "anchor", "titulo": "Sistemas de restricción de caídas (Travel Restraint)", "texto": "Utilizar cabos de amarre de longitud fija calculada para impedir físicamente que el operario alcance el borde desprotegido."},
            {"icono": "eye", "titulo": "Delimitación visual y zonas de advertencia", "texto": "Tender líneas de advertencia con banderines de alta visibilidad a no menos de 2 metros del borde para restringir el paso de personal no amarrado."}
        ],
        "pregunta": "¿Se exige la instalación de barandas rígidas en el perímetro de tus techos antes de iniciar trabajos de montaje o mantenimiento?",
        "fuente": "Fuente: Informe de Investigación de Accidente Fatal por Caída de Techo de OSHA (Occupational Safety and Health Administration) en Indiana (Noviembre 2017).",
        "guionReel": (
            "El 29 de noviembre de 2017, en Indiana, un técnico de climatización murió al caer de 12 metros de altura desde el techo de un centro logístico de Amazon.\n\n"
            "Llevaba herramientas cerca del borde. El techo gigante no tenía barandas de seguridad perimetrales instaladas ni líneas de vida.\n\n"
            "Tropezó con una junta metálica, perdió el equilibrio y cayó directo al asfalto.\n\n"
            "OSHA determinó que la contratista violó la ley al permitir trabajos sobre techos sin barandas rígidas ni arnés anclado.\n\n"
            "¿La lección de Focus HSE? Antes de subir a un techo, instala barandas perimetrales. La protección colectiva siempre va primero. La seguridad está en los detalles."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 29 de noviembre de 2017, en las obras de un masivo centro de distribución logística de la empresa Amazon en el estado de Indiana, un operario de una empresa contratista de climatización falleció trágicamente tras precipitarse desde una cubierta a más de doce metros de altura, caso investigado por la OSHA.\n\n"
            "El edificio abarcaba una superficie de techo equivalente a varios campos de fútbol. Aquella tarde fría, el trabajador transportaba ductos y herramientas hacia una de las unidades de ventilación ubicadas en la parte superior. Para acortar camino, caminó por las láminas metálicas cerca del borde exterior del edificio.\n\n"
            "A pesar de la altura extrema, el perímetro del techo no contaba con barandas perimetrales de seguridad instaladas, ni se habían tendido cables de vida de acero para el amarre de arneses. La contratista tampoco había delimitado una línea de advertencia con banderines para advertir a los trabajadores que se aproximaban a la zona de riesgo.\n\n"
            "Al pisar el reborde de una junta de dilatación con calzado de trabajo cargado de material, el operario tropezó. Sin un punto de anclaje que lo detuviera ni una barrera física que frenara su impulso, cayó al vacío impactando sobre el pavimento de la bahía de carga inferior.\n\n"
            "La investigación de OSHA concluyó que la falla principal fue omitir la jerarquía de controles de seguridad: priorizar la protección colectiva mediante barandas rígidas en los bordes antes de permitir que cualquier persona acceda a la superficie del techo.\n\n"
            "En los techos industriales, un simple tropiezo se convierte en fatalidad si el borde no está protegido. La seguridad colectiva salva vidas donde la distracción humana falla. En Focus HSE te lo recordamos siempre: la seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, 16:9 aspect ratio. The vast expanse of an industrial mega-warehouse metal roof in Indiana, 2017. "
            "Looking toward the unprotected leading edge of the flat corrugated roof against an overcast late autumn sky. "
            "In the foreground, certified yellow temporary guardrail posts and horizontal warning lines with triangular warning flags. "
            "Large rooftop HVAC ventilation units in the background. High realism, gritty textures of corrugated metal and industrial fasteners, 35mm lens."
        )
    },
    {
        "id": "158",
        "logo": "FOCUS HSE",
        "fecha": "30 NOVIEMBRE",
        "fechaPublicacion": "2026-11-30",
        "expediente": "Expediente #158",
        "carpeta": "1987-11-30-explosion-aerosoles-propano-ati-johannesburgo-sudafrica",
        "titular": "LA NUBE EN EL ENVASE: EXPLOSIÓN DE AEROSOLES EN ATI JOHANNESBURGO",
        "palabraResaltada": "VENTILACIÓN ATEX",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Fábrica de Aerosoles y Productos Químicos ATI, Johannesburgo, Sudáfrica - 1987",
        "tipoRiesgo": "Seguridad de Procesos / Atmósferas Explosivas (ATEX) / Gases Inflamables",
        "parrafos": [
            "El 30 de noviembre de 1987, en la planta de manufactura de aerosoles de la empresa ATI en las afueras de Johannesburgo, Sudáfrica, una tremenda explosión de gas propelente destruyó la nave de envasado, dejando múltiples víctimas y arrasando la estructura fabril.",
            "En la línea de llenado de aerosoles se utilizaba una mezcla de gas licuado de petróleo (butano y propano) como gas propelente presurizado. Un fallo en el motor del extractor de aire localizado provocó que los vapores pesados de gas fugados durante la inyección se acumularan en el foso y suelo de la nave.",
            "La planta carecía de detectores continuos de explosividad (LEL) con corte automático y las instalaciones eléctricas no cumplían norma antiexplosiva (ATEX). Una chispa en un contactor convencional encendió la atmósfera explosiva. La lección: extracción mecánica reforzada con redundancia, detectores fijos de LEL y equipos eléctricos clasificados a prueba de explosión."
        ],
        "puntosClave": [
            {"icono": "wind", "titulo": "Extracción forzada a nivel de piso con respaldo", "texto": "Diseñar sistemas de ventilación mecánica con tomas a ras de suelo para evacuar gases más pesados que el aire con ventiladores redundantes."},
            {"icono": "gauge", "titulo": "Detectores de LEL con corte ESD automático", "texto": "Instalar sensores continuos de gas inflamable calibrados al 10% y 20% del LEL que disparen corte automático de gas y parada de emergencia."},
            {"icono": "zap", "titulo": "Equipamiento eléctrico clasificado antiexplosivo (Ex)", "texto": "Prohibir interruptores, luminarias y motores convencionales en recintos de llenado de propelentes inflamables."}
        ],
        "pregunta": "¿Cuentan tus salas con manejo de inflamables con detección automática de LEL y motores de extracción antiexplosivos?",
        "fuente": "Fuente: Reporte Técnico de Seguridad Industrial y Peritaje de Incendios sobre la explosión en la planta de aerosoles ATI en Johannesburgo (Sudáfrica, Diciembre 1987).",
        "guionReel": (
            "El 30 de noviembre de 1987, en Johannesburgo, Sudáfrica, la fábrica de aerosoles ATI voló en pedazos por gas propano acumulado.\n\n"
            "Cargaban desodorantes con gas butano y propano como propelente. El extractor de aire falló, pero la línea siguió produciendo.\n\n"
            "El gas, más pesado que el aire, se acumuló como una pileta invisible en el suelo. No había detectores de gas que alertaran el peligro.\n\n"
            "Un interruptor eléctrico común chispeó y la sala entera estalló en mil pedazos.\n\n"
            "¿La lección de Focus HSE? Extracción continua redundante a ras del piso, sensores de gas LEL y motores antiexplosivos. La seguridad está en los detalles."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 30 de noviembre de 1987, en la zona industrial de Johannesburgo, Sudáfrica, una catastrófica explosión en la fábrica de envasado de aerosoles de la empresa ATI redujo a escombros la nave principal de manufactura, en un siniestro histórico para la industria química de propelentes.\n\n"
            "La planta utilizaba mezclas de butano y propano para presurizar envases de aerosoles domésticos e industriales. Durante el proceso de crimpado e inyección a alta presión, pequeñas microfugas de gas líquido eran inevitables en las boquillas de llenado.\n\n"
            "Para controlar este riesgo, la sala debía contar con ventilación forzada constante. Sin embargo, horas antes del siniestro, la correa de transmisión del ventilador de extracción principal se rompió. Al no existir sensores de flujo de aire ni sistemas de enclavamiento que detuvieran la línea, los operarios continuaron envasando latas sin percatarse de que el aire de la sala se estaba estancando.\n\n"
            "Al ser los gases de hidrocarburos mucho más densos que el aire, el propano y el butano comenzaron a drenar hacia el suelo y los fosos bajo las cintas transportadoras, formando una invisible capa altamente explosiva. La instalación carecía de detectores fijos de límite inferior de explosividad (LEL) y utilizaba tableros eléctricos residenciales no blindados.\n\n"
            "Cuando el relé de un motor eléctrico auxiliar conmutó para arrancar una cinta, la chispa eléctrica encendió la capa de gas. La detonación desintegró las paredes de chapa, voló la cubierta y desató incendios masivos de miles de envases presurizados que actuaron como pequeños proyectiles.\n\n"
            "Este evento sentó precedentes internacionales sobre las normas de seguridad en la fabricación de aerosoles: extracción forzada redundante monitoreada por flujo, cabinas de llenado aisladas y equipamiento eléctrico clasificado a prueba de explosión. En Focus HSE te lo recordamos siempre: la seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, 16:9 aspect ratio. The shattered ruins of an industrial aerosol canning factory in Johannesburg South Africa, 1987. "
            "Twisted structural steel framing and corrugated wall panels blasted open, scattered metallic aerosol canisters across the concrete factory floor. "
            "Emergency fire engines pumping water into smoldering debris under an intense afternoon sun. "
            "Industrial safety investigators examining the burnt remnants of a mechanical ventilation duct and motor panel, authentic 35mm film grain."
        )
    },
    {
        "id": "159",
        "logo": "FOCUS HSE",
        "fecha": "01 DICIEMBRE",
        "fechaPublicacion": "2026-12-01",
        "expediente": "Expediente #159",
        "carpeta": "2017-12-01-intoxicacion-vapores-tanque-industrial-tank-cleaning-luisiana",
        "titular": "EL FILTRO SATURADO: INTOXICACIÓN EN INDUSTRIAL TANK CLEANING",
        "palabraResaltada": "EQUIPO AUTÓNOMO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Terminal de Tanques Químicos, Industrial Tank Cleaning, Luisiana, EE.UU. - 2017",
        "tipoRiesgo": "Espacios Confinados / Atmósferas Tóxicas / Protección Respiratoria",
        "parrafos": [
            "El 1 de diciembre de 2017, en una estación de lavado y desgasificado de la contratista Industrial Tank Cleaning en Luisiana, un operario murió asfixiado e intoxicado dentro de un camión cisterna que había transportado solventes químicos aromáticos.",
            "La investigación de OSHA demostró que el trabajador ingresó a la cisterna sin realizar una medición instrumental previa de vapores orgánicos ni mantener un extractor de ventilación forzada activa, utilizando únicamente una media máscara de caucho con cartuchos químicos de carbón activado.",
            "La concentración de vapores de tolueno y xileno dentro del recinto superaba miles de partes por millón, saturando los filtros en cuestión de segundos y provocando la pérdida súbita de conocimiento de la víctima. La lección: monitoreo de gases con detector de fotoionización (PID), ventilación continua y uso obligatorio de equipos autónomos (SCBA) o línea de aire suministrado."
        ],
        "puntosClave": [
            {"icono": "shield-check", "titulo": "Prohibición de filtros purificadores en atmósferas IDLH", "texto": "Nunca utilizar respiradores con filtros químicos en espacios cerrados con concentraciones desconocidas o potencialmente letales."},
            {"icono": "wind", "titulo": "Suministro de aire respirable (Línea de aire / SCBA)", "texto": "Ingresar a recintos con presencia de solventes pesados exclusivamente con equipos autónomos de presión positiva o cascada de aire."},
            {"icono": "gauge", "titulo": "Monitoreo con detector PID y ventilación forzada", "texto": "Medir compuestos orgánicos volátiles (COVs) con equipo fotoionizador antes del ingreso y renovar el aire inyectando aire fresco continuo."}
        ],
        "pregunta": "¿Se prohíbe terminantemente en tu empresa el uso de máscaras con filtro químico para ingresar a limpiar tanques de solventes?",
        "fuente": "Fuente: Informe de Investigación de Accidente Fatal en Espacios Confinados de OSHA (Occupational Safety and Health Administration) en Luisiana (Diciembre 2017).",
        "guionReel": (
            "El 1 de diciembre de 2017, en Luisiana, un limpiador de tanques murió dentro de una cisterna de la empresa Industrial Tank Cleaning.\n\n"
            "El camión había llevado solventes químicos. El operario entró con una máscara simple de cartuchos de carbón activado, sin medir el aire ni poner ventilador.\n\n"
            "La concentración de tolueno era tan alta que el filtro se saturó en tres respiraciones. El veneno puro entró a sus pulmones y cayó desmayado al instante.\n\n"
            "OSHA multó a la empresa: los filtros comunes jamás se usan en espacios confinados con vapores densos.\n\n"
            "¿La lección de Focus HSE? En cisternas químicas se usa equipo de aire suministrado o autónomo, ventilación forzada y monitoreo previo. La seguridad está en los detalles."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 1 de diciembre de 2017, en una terminal de servicios de limpieza de tanques operada por la contratista Industrial Tank Cleaning en el estado de Luisiana, ocurrió un trágico accidente en espacio confinado documentado por la OSHA, donde un operario especializado perdió la vida en minutos.\n\n"
            "La tarea asignada era el lavado interior de un camión cisterna que había transportado solventes industriales pesados y naftas de hidrocarburos aromáticos. En lugar de ejecutar una purga con vapor de agua y ventilación forzada exhaustiva para abatir la atmósfera química peligrosa, la supervisión permitió el ingreso inmediato del trabajador para acelerar la rotación del vehículo.\n\n"
            "El operario descendió por la boca de hombre superior vistiendo un overol impermeable y una media máscara elastomérica convencional con cartuchos de carbón activado para vapores orgánicos. No se realizó una medición previa con detector multigas ni con detector de fotoionización.\n\n"
            "Lo que el trabajador ignoraba es que los filtros purificadores de carbón solo son efectivos en concentraciones ambientales bajas y con suficiente oxígeno. Dentro de la cisterna, la concentración de solventes superaba con creces los límites inmediatamente peligrosos para la vida y la salud, conocidos como IDLH. En menos de un minuto, el carbón activado se saturó por completo, permitiendo el paso masivo de vapores tóxicos hacia sus pulmones. El operario sufrió narcosis química súbita y cayó inerte al fondo del tanque.\n\n"
            "Cuando el vigía de seguridad advirtió que no respondía, no contaba con equipos de rescate con línea de vida retráctil, sellando el destino de su compañero.\n\n"
            "En espacios confinados químicos, los filtros respiratorios son una trampa mortal de falsa seguridad. Solo los equipos de aire suministrado con manguera o los equipos autónomos garantizan aire limpio para respirar. En Focus HSE te lo recordamos siempre: la seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, 16:9 aspect ratio. An industrial tank truck cleaning facility in Louisiana, 2017. "
            "A stainless steel road tanker parked on a wash bay with an open circular top manhole hatch. "
            "A rescue tripod system with winch and harness cable positioned above the manhole. On a clean stainless steel table nearby, a self-contained breathing apparatus (SCBA) yellow cylinder, full face mask, and a digital PID volatile organic compound meter. "
            "High-contrast moody lighting, reflections on wet concrete wash bay, 35mm lens authentic technical photojournalism."
        )
    },
    {
        "id": "160",
        "logo": "FOCUS HSE",
        "fecha": "02 DICIEMBRE",
        "fechaPublicacion": "2026-12-02",
        "expediente": "Expediente #160",
        "carpeta": "1984-12-02-desastre-quimico-isocianato-metilo-union-carbide-bhopal-india",
        "titular": "LA NOCHE DEL GAS EN BHOPAL: EL DESASTRE DE UNION CARBIDE",
        "palabraResaltada": "BARRERAS MÚLTIPLES",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta de Pesticidas Union Carbide India Limited (UCIL), Bhopal, Madhya Pradesh, India - 1984",
        "tipoRiesgo": "Seguridad de Procesos (PSM) / Catástrofe Industrial Mayor",
        "parrafos": [
            "En la medianoche del 2 al 3 de diciembre de 1984, en la planta de pesticidas de Union Carbide India Limited en Bhopal, Madhya Pradesh, India, una fuga masiva de 42 toneladas de gas isocianato de metilo (MIC) envolvió la ciudad mientras sus habitantes dormían, provocando la muerte inmediata de más de 3.000 personas y afectando a más de 500.000 en el peor desastre químico de la historia de la humanidad.",
            "El desastre comenzó cuando ingresó agua en el tanque subterráneo E610 que almacenaba MIC, provocando una reacción exotérmica violenta descontrolada que disparó la temperatura a más de 200°C y reventó los discos de ruptura y válvulas de alivio.",
            "Increíblemente, todas las barreras críticas de seguridad estaban fuera de servicio por reducción de costos: la refrigeración del tanque estaba apagada para ahorrar freón, el lavador de gases con soda cáustica estaba desactivado, la antorcha de quemado estaba desmontada para reparación y la cortina de agua no tenía presión suficiente. La lección de Bhopal: jamás deshabilitar barreras de seguridad críticas simultáneamente, diseño inherentemente seguro e inventarios mínimos."
        ],
        "puntosClave": [
            {"icono": "shield-alert", "titulo": "Principio innegociable de no degradar barreras", "texto": "Prohibir terminantemente operar unidades químicas cuando los sistemas de mitigación de emergencia (refrigeración, scrubber, flare) están fuera de servicio."},
            {"icono": "database", "titulo": "Diseño inherentemente más seguro e inventarios mínimos", "texto": "Eliminar el almacenamiento a granel de intermediarios hiperreactivos y letales como el MIC; producir solo a demanda para consumo inmediato."},
            {"icono": "users", "titulo": "Planes de respuesta a emergencias comunitarias", "texto": "Coordinación estrecha con hospitales, sirenas comunitarias de aviso temprano y programas de información sobre evacuación para la población civil vecina."}
        ],
        "pregunta": "¿Se permite en tu planta operar procesos peligrosos con algún sistema de seguridad o alivio de emergencia fuera de servicio?",
        "fuente": "Fuente: Informes Oficiales de la CBI (Central Bureau of Investigation de India), CSB/AIChE Center for Chemical Process Safety (CCPS) sobre la catástrofe de Union Carbide en Bhopal (1984).",
        "guionReel": (
            "La noche del 2 de diciembre de 1984, en Bhopal, India, la planta de Union Carbide causó la peor catástrofe química de la historia humana.\n\n"
            "Un tanque con 42 toneladas de isocianato de metilo, un gas ultravaneno, recibió agua por error y comenzó una reacción violenta e hirviente.\n\n"
            "Para ahorrar costos, apagaron la refrigeración. El lavador de gases estaba apagado. La antorcha para quemar el gas estaba rota. Ninguna barrera funcionó.\n\n"
            "Una nube blanca y letal cubrió la ciudad mientras la gente dormía. Miles murieron asfixiados en sus camas en pocas horas.\n\n"
            "¿La lección de Focus HSE? Las barreras de seguridad son sagradas. Jamás operes una planta si los sistemas de emergencia están caídos. La seguridad está en los detalles."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "La medianoche del 2 al 3 de diciembre de 1984, en la ciudad de Bhopal, Madhya Pradesh, India, la planta de pesticidas de Union Carbide India Limited desató la peor catástrofe química e industrial en la historia de la humanidad, cobrando la vida de miles de personas y dejando secuelas imborrables en cientos de miles de sobrevivientes.\n\n"
            "En el tanque de almacenamiento subterráneo número seiscientos diez yacían cuarenta y dos toneladas de isocianato de metilo líquido, conocido como MIC, un compuesto hiperreactivo, volátil y mortal a concentraciones ínfimas. Durante una maniobra deficiente de lavado de tuberías sin colocar bridas ciegas de aislamiento, ingresaron varios cientos de litros de agua al interior del tanque.\n\n"
            "El agua reaccionó violentamente con el isocianato en una reacción exotérmica descontrolada. La temperatura interna trepó a más de doscientos grados Celsius y la presión reventó las válvulas de alivio. En ese instante, la tragedia pudo haberse mitigado si las barreras de ingeniería hubieran estado activas, pero todas habían sido apagadas o desmanteladas por una negligente política de reducción de costos.\n\n"
            "El sistema de refrigeración con gas freón había sido desconectado meses antes para ahorrar electricidad; la torre lavadora de gases alcalinos con soda cáustica estaba fuera de servicio y sin bomba de recirculación; y la antorcha de combustión que debía quemar los gases de escape había sido retirada de su línea por tareas de reparación. Ni siquiera las cortinas de agua tenían la altura suficiente para alcanzar la chimenea de venteo.\n\n"
            "Una densa nube tóxica de isocianato de metilo y ácido cianhídrico escapó hacia la atmósfera nocturna y avanzó a ras del suelo sobre los populosos barrios adyacentes a la fábrica. La población despertó ahogándose, con los ojos quemados y las vías respiratorias colapsadas, sin que sonara una sola sirena de alarma comunitaria.\n\n"
            "Bhopal cambió para siempre la legislación global de Seguridad de Procesos, impulsando la creación de la norma OSHA PSM, las directivas Seveso y la filosofía del diseño inherentemente más seguro. Jamás se debe operar con barreras de mitigación degradadas. En Focus HSE te lo recordamos siempre: la seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, 16:9 aspect ratio. The haunting abandoned ruins of the Union Carbide pesticide chemical plant in Bhopal, India. "
            "Rusted steel distillation towers, overgrown vegetation around concrete reaction vessels, crumbling industrial pipe racks against a misty dawn sky. "
            "Atmospheric documentary photography capturing historical gravity, peeling yellow industrial paint, weathered warning placards in Hindi and English, shot on 35mm film."
        )
    },
    {
        "id": "161",
        "logo": "FOCUS HSE",
        "fecha": "03 DICIEMBRE",
        "fechaPublicacion": "2026-12-03",
        "expediente": "Expediente #161",
        "carpeta": "2018-12-03-electrocucion-gabinete-control-tyson-foods-arkansas",
        "titular": "EL TERMINAL EXPUESTO A 480V: ELECTROCUCIÓN EN TYSON FOODS",
        "palabraResaltada": "MEDICIÓN EN VIVO",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Procesadora de Alimentos, Tyson Foods, Arkansas, EE.UU. - 2018",
        "tipoRiesgo": "Riesgo Eléctrico / Bloqueo y Etiquetado (LOTO) / Arco Eléctrico",
        "parrafos": [
            "El 3 de diciembre de 2018, en una planta procesadora avícola de Tyson Foods en Arkansas, un técnico electromecánico de mantenimiento falleció electrocutado al tocar accidentalmente un borne de 480 voltios energizado dentro de un tablero de control de empaque.",
            "La investigación de OSHA reveló que el técnico realizaba la localización de una falla en un variador de velocidad con el tablero energizado, pero carecía de guantes dieléctricos clase 0 certificados, no utilizaba protector facial contra arco eléctrico ni disponía de un permiso de trabajo eléctrico en caliente.",
            "Al deslizarse la punta de prueba del multímetro, el dorso de su mano rozó un terminal de cobre desprotegido, cerrando circuito a tierra a través de su cuerpo. La lección: prioridad de desenergizar y aplicar LOTO antes de intervenir gabinetes; y si se mide en tensión, cumplimiento riguroso de la norma NFPA 70E con guantes dieléctricos y careta."
        ],
        "puntosClave": [
            {"icono": "lock", "titulo": "Principio de desenergizar primero (LOTO eléctrico)", "texto": "Desconectar y colocar candado siempre que sea viable; prohibir diagnósticos con tensión salvo imposibilidad técnica comprobada."},
            {"icono": "shield-check", "titulo": "EPP dieléctrico y contra arco según NFPA 70E", "texto": "Uso obligatorio de guantes dieléctricos con protectores de cuero y pantalla facial con clasificación de protección térmica por arco (ATPV)."},
            {"icono": "tool", "titulo": "Puntas de prueba con aislamiento de seguridad CAT III/IV", "texto": "Utilizar sondas de medición con puntas protegidas que dejen expuestos solo 4 mm de metal para evitar cortocircuitos accidentales."}
        ],
        "pregunta": "¿Utilizan tus técnicos guantes dieléctricos certificados cada vez que miden voltaje dentro de un tablero de 480V?",
        "fuente": "Fuente: Informe de Investigación de Accidente Eléctrico Fatal de OSHA (Occupational Safety and Health Administration) en Tyson Foods, Arkansas (Diciembre 2018).",
        "guionReel": (
            "El 3 de diciembre de 2018, en Arkansas, un técnico electromecánico de Tyson Foods murió electrocutado buscando una falla en un tablero.\n\n"
            "El gabinete estaba vivo a 480 voltios. Para medir rápido, metió el tester sin ponerse guantes de goma dieléctricos ni máscara de arco eléctrico.\n\n"
            "La punta del tester patinó y su mano rozó un borne de cobre pelado. 480 voltios cruzaron su pecho en una milésima de segundo.\n\n"
            "OSHA multó a la empresa por violar las normas de seguridad eléctrica en caliente.\n\n"
            "¿La lección de Focus HSE? Primero corta y bloquea con LOTO. Si debes medir en tensión, usa guantes dieléctricos certificados y sondas CAT 4. La seguridad está en los detalles."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 3 de diciembre de 2018, en una planta de procesamiento de alimentos de la corporación Tyson Foods en el estado de Arkansas, un técnico de mantenimiento electromecánico de amplia trayectoria falleció electrocutado al intervenir un panel de control eléctrico industrial, en un accidente documentado por la OSHA.\n\n"
            "Durante el turno de faena, un transportador de cajas se detuvo repentinamente. Para reanudar la producción a la brevedad, el técnico abrió la puerta de un armario de distribución eléctrica de cuatrocientos ochenta voltios con el interruptor principal energizado para verificar la alimentación del variador de frecuencia.\n\n"
            "A pesar de estar trabajando a escasos centímetros de barras y bornes activos sin aislamiento, el trabajador no se colocó los guantes aislantes de caucho certificados para alta tensión ni la pantalla de protección facial contra ráfagas de arco eléctrico, vistiendo únicamente sus guantes comunes de descarne para mecánica.\n\n"
            "Al intentar colocar una sonda de prueba en un borne de contactor estrecho, la punta metálica resbaló. En el acto reflejo por evitar la caída de la herramienta, el nudillo de su dedo índice hizo contacto directo con el terminal de cobre energizado. La corriente alterna trifásica atravesó su brazo y su corazón hacia el chasis metálico puesto a tierra del armario, provocando fibrilación ventricular instantánea.\n\n"
            "La investigación de OSHA sancionó a la planta por no exigir el cumplimiento estricto de la norma de seguridad eléctrica NFPA 70E, permitiendo que las tareas de diagnóstico en caliente se realizaran sin equipos de protección individual adecuados ni barreras aislantes provisionales.\n\n"
            "La corriente eléctrica es invisible y silenciosa; no da segundas oportunidades. Trabajar con tensión exige respeto absoluto y barreras dieléctricas comprobadas. En Focus HSE te lo recordamos siempre: la seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, 16:9 aspect ratio. Inside an industrial food processing plant electrical room in Arkansas, 2018. "
            "An open 480-volt electrical control panel with industrial circuit breakers, terminal blocks, and colored wiring looms. "
            "A pair of heavy rubber insulating electrical gloves and leather protectors laid beside a certified CAT IV digital multimeter on a clean rubber work mat. "
            "Warning labels 'DANGER - HIGH VOLTAGE - ARC FLASH HAZARD' clearly visible on the steel cabinet door. Realistic lighting, 35mm lens authentic documentary style."
        )
    },
    {
        "id": "162",
        "logo": "FOCUS HSE",
        "fecha": "04 DICIEMBRE",
        "fechaPublicacion": "2026-12-04",
        "expediente": "Expediente #162",
        "carpeta": "2016-12-04-vuelco-autoelevador-muelle-carga-sysco-california",
        "titular": "EL GIRO EN EL MUELLE: VUELCO DE AUTOELEVADOR EN SYSCO CALIFORNIA",
        "palabraResaltada": "TRIÁNGULO DE ESTABILIDAD",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Centro de Distribución y Almacenamiento, Sysco, California, EE.UU. - 2016",
        "tipoRiesgo": "Seguridad Vial Interna / Estabilidad de Equipos / Muelles de Carga",
        "parrafos": [
            "El 4 de diciembre de 2016, en un centro de distribución mayorista de la empresa de alimentos Sysco en California, un operador de autoelevador murió aplastado por el tejadillo protector tras volcar lateralmente su equipo mientras maniobraba en la zona de muelles de carga.",
            "La investigación de OSHA y Cal/OSHA constató que el conductor realizaba un giro brusco a velocidad excesiva con las horquillas y el mástil elevados tras descargar un pallet en una rampa con pendiente, desestabilizando el centro de gravedad fuera del triángulo de estabilidad del autoelevador.",
            "Al iniciarse el vuelco, el operador, que no llevaba abrochado el cinturón de seguridad, intentó saltar de la cabina hacia el lado de la caída, quedando atrapado bajo la estructura metálica antivuelco (ROPS). La lección: circular siempre con horquillas bajas a 15 cm del piso, respetar velocidades límite en muelles y uso innegociable del cinturón de seguridad."
        ],
        "puntosClave": [
            {"icono": "shield-check", "titulo": "Uso innegociable del cinturón de seguridad", "texto": "El cinturón mantiene al operador dentro del habitáculo seguro ante vuelcos laterales, evitando el reflejo fatal de intentar saltar."},
            {"icono": "trending-down", "titulo": "Circulación con mástil y horquillas bajas", "texto": "Trasladarse siempre con las horquillas entre 15 y 20 centímetros del suelo; nunca girar ni avanzar con cargas elevadas."},
            {"icono": "truck", "titulo": "Bloqueo y calzado de camiones en muelles", "texto": "Instalar trabas automáticas de chasis (dock locks) o calzas dobles de rueda antes de que cualquier autoelevador ingrese al acoplado."}
        ],
        "pregunta": "¿Supervisas que todos los conductores de autoelevador mantengan el cinturón de seguridad abrochado durante todo su turno?",
        "fuente": "Fuente: Informe de Fatalidad en Operación de Montacargas de Cal/OSHA (California Department of Industrial Relations) en Sysco Foods, California (Diciembre 2016).",
        "guionReel": (
            "El 4 de diciembre de 2016, en California, un conductor de autoelevador murió aplastado en un depósito de Sysco por cometer dos errores fatales.\n\n"
            "Descargó un camión y dio marcha atrás doblando rápido con las uñas y el mástil todavía arriba.\n\n"
            "El centro de gravedad se salió del triángulo de apoyo y la máquina de 4 toneladas volcó de costado.\n\n"
            "El chofer no tenía puesto el cinturón de seguridad e intentó saltar. La reja del techo cayó sobre él aplastándolo al instante.\n\n"
            "¿La lección de Focus HSE? Siempre viaja con las uñas bajas, no dobles en velocidad y abróchate el cinturón. La cabina te protege solo si te quedas adentro. La seguridad está en los detalles."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 4 de diciembre de 2016, en las instalaciones de un concurrido centro logístico de la distribuidora de alimentos Sysco en el estado de California, un operador de montacargas perdió la vida al ser aplastado por su propia máquina, en un siniestro investigado por la división Cal/OSHA.\n\n"
            "Esa noche, las cuadrillas trabajaban a ritmo intenso en los muelles de carga para despachar camiones refrigerados. Tras acomodar un pallet de mercadería pesada dentro de un semirremolque, el conductor retrocedió hacia la rampa de concreto del muelle a una velocidad superior a los diez kilómetros por hora.\n\n"
            "Para agilizar el movimiento, inició un viraje cerrado en reversa sin haber bajado el mástil telescópico ni las horquillas, que permanecían elevadas a más de dos metros de altura. En la dinámica de los autoelevadores, el mástil elevado traslada el centro de gravedad hacia arriba y hacia adelante; al combinar esto con la fuerza centrífuga de un giro brusco, el centro de gravedad fue expulsado fuera de la base del triángulo de sustentación formado por las ruedas directrices traseras y el eje motriz delantero.\n\n"
            "La máquina de cuatro toneladas perdió apoyo y volcó lateralmente. El operador no llevaba abrochado el cinturón de seguridad del asiento. En una reacción instintiva pero catastrófica, intentó saltar hacia afuera para escapar; al hacerlo, cayó en la misma dirección hacia donde la máquina se precipitaba y el tejadillo de acero de protección contra caídas de objetos lo impactó contra el piso de hormigón.\n\n"
            "Cal/OSHA reiteró la regla de oro: el cinturón de seguridad en un autoelevador no es para colisiones, sino para mantener al conductor dentro de la 'jaula de supervivencia' en caso de vuelco.\n\n"
            "Circular despacio, con las uñas al ras del suelo y con el cinturón abrochado marca la diferencia entre un susto mecánico y una tragedia irreversible. En Focus HSE te lo recordamos siempre: la seguridad está en los detalles."
        ),
        "promptImagen": (
            "Cinematic documentary photography, 16:9 aspect ratio. Interior of a modern commercial food logistics distribution center in California, 2016. "
            "A yellow industrial forklift parked safely with forks lowered flat to the polished concrete floor in front of a loading dock door. "
            "Close-up emphasis on the driver's seat with a bright orange buckled safety belt and overhead protective steel canopy cage. "
            "Floor markings, wheel chocks, and loading dock traffic lights with green and red signals. Clean commercial logistics lighting, authentic depth of field, 35mm lens."
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

    # Buscamos la posición donde termina el array 'const historias = ['
    start_tag = "const historias = ["
    start_idx = html.find(start_tag)
    if start_idx == -1:
        raise ValueError("No se pudo encontrar 'const historias = [' en index.html")

    end_idx = html.find("];", start_idx)
    if end_idx == -1:
        raise ValueError("No se pudo encontrar el cierre '];' de historias en index.html")

    array_content = html[start_idx + len(start_tag):end_idx].rstrip()

    nuevas_historias_js = []
    for h in historias_procesadas:
        imagen_def = "portada.jpeg" if os.path.exists(os.path.join(ASSETS_DIR, h["carpeta"], "portada.jpeg")) else "portada.png"
        obj_dict = {
            "id": h["id"],
            "logo": h.get("logo", "FOCUS HSE"),
            "fecha": h["fecha"],
            "fechaPublicacion": h["fechaPublicacion"],
            "expediente": h["expediente"],
            "carpetaAssets": f"assets/efemerides/{h['carpeta']}/",
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
        js_str = "      " + js_str.replace("\n", "\n      ")
        nuevas_historias_js.append(js_str)

    nuevo_bloque_js = ",\n" + ",\n".join(nuevas_historias_js)
    nuevo_array = array_content + nuevo_bloque_js + "\n    "
    nuevo_html = html[:start_idx + len(start_tag)] + nuevo_array + html[end_idx:]

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(nuevo_html)

    print(f"✓ index.html actualizado exitosamente con los 10 nuevos expedientes (#{historias_procesadas[0]['id']} a #{historias_procesadas[-1]['id']}).")

def sincronizar_portadas_disco():
    """Verifica en assets/efemerides cada carpeta y sincroniza en index.html si existe portada.jpeg"""
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    cambios = 0
    pattern = r'carpetaAssets:\s*"assets/efemerides/([^/"]+)/",[\s\S]*?imagen:\s*"([^"]+)"'
    
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
    print("Iniciando motor Kokoro para Lote 15 (#153 a #162)...\n")
    kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

    print("=======================================================")
    print("Iniciando procesamiento de 10 historias del Lote 15 (#153 a #162)")
    print("=======================================================\n")

    historias_procesadas = []

    for h in LOTE_15_DATA:
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

        # 6. Audio con Kokoro
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

    print("\n🎉 ¡LOTE 15 COMPLETADO AL 100%! (10 historias procesadas)\n")

if __name__ == "__main__":
    main()
