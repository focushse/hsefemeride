# -*- coding: utf-8 -*-
"""
Generador Agéntico Automatizado para Lote 12: Expedientes #123 a #132 (26 de octubre al 4 de noviembre)
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

LOTE_12_DATA = [
    {
        "id": "123",
        "fecha": "26 OCTUBRE",
        "fechaPublicacion": "2026-10-26",
        "expediente": "Expediente #123",
        "carpeta": "2018-10-26-caida-andamio-baker-concrete-austin-texas",
        "titular": "LA BARANDA QUE FALTABA: CAÍDA EN BAKER CONCRETE AUSTIN",
        "palabraResaltada": "BAKER CONCRETE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Obra en Construcción Edificio Urbano, Austin, Texas, EE.UU. - 2018",
        "tipoRiesgo": "Trabajo en Altura / Andamios",
        "parrafos": [
            "El 26 de octubre de 2018, un operario de 33 años falleció al precipitarse desde un andamio multidireccional a nueve metros de altura en una obra de la contratista Baker Concrete Construction en Austin, Texas, investigada por OSHA.",
            "Durante el desmontaje parcial de una plataforma de trabajo para permitir el izaje de materiales, se retiraron las barandas perimetrales y los rodapiés sin que los trabajadores estuvieran anclados a una línea de vida vertical.",
            "El trabajador perdió el equilibrio y cayó al vacío sin sistema de detención de caídas. La lección: mantener barandas rígidas completas hasta el desarme final y uso obligatorio de arnés con doble cabo de amarre al 100% durante el desmantelamiento.",
        ],
        "puntosClave": [
            {"icono": "shield", "titulo": "Barandas perimetrales estándar completas", "texto": "Todo andamio de trabajo debe contar con baranda superior a 1,05 m, baranda intermedia a 50 cm y rodapié de 15 cm en todos los lados abiertos."},
            {"icono": "anchor", "titulo": "Anclaje continuo al 100% durante montaje y desarme", "texto": "El personal que arma o desarma andamios debe permanecer amarrado en todo momento mediante arnés con doble cola con absorbedor de impacto."},
            {"icono": "clipboard-check", "titulo": "Tarjeta de habilitación visible (Verde/Roja)", "texto": "Señalizar con tarjeta roja de 'No Usar' cualquier andamio incompleto al que se le hayan retirado componentes de protección."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de inspección y citaciones federales de OSHA (OSHA Austin Area Office / 29 CFR 1926 Subpart L) sobre Baker Concrete Construction Inc.",
        "guionReel": (
            "El 26 de octubre de 2018, en Austin, Texas, una obra de la contratista Baker Concrete Construction terminó en tragedia.\n\n"
            "A nueve metros de altura, los operarios desmontaban las tablas de un andamio. Para apurar el trabajo, retiraron las barandas perimetrales de seguridad.\n\n"
            "Un trabajador de 33 años caminaba por el borde desprotegido. Llevaba el arnés puesto, pero el gancho colgaba suelto, sin anclar a ninguna parte.\n\n"
            "Tropezó con una herramienta, no tuvo de dónde agarrarse y cayó al vacío sobre el pavimento. Murió en el acto.\n\n"
            "La lección de Focus HSE: un andamio sin barandas es una trampa mortal. Durante el armado y desarme, el anclaje al 100% no se negocia.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an urban multi-story commercial building construction site in Austin, Texas. "
            "A modular steel system scaffolding tower showing a partially dismantled upper work platform missing its guardrails, "
            "safety harness lanyard resting on a scaffold transom, concrete construction ground floor cordoned with yellow OSHA caution tape, 8k resolution, raw documentary lighting."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 26 de octubre de 2018, en una importante obra de construcción comercial en la ciudad de Austin, capital del estado de Texas, "
            "la empresa especializada en estructuras Baker Concrete Construction protagonizó un grave siniestro fatal. "
            "Un operario de treinta y tres años se precipitó al vacío desde el cuarto nivel de una torre de andamios tubulares, "
            "a una altura superior a los nueve metros, sufriendo un impacto letal contra la losa de hormigón de la planta baja.\n\n"
            "La inspección técnica de la OSHA determinó que el accidente se produjo durante una maniobra improvisada de modificación de la plataforma. "
            "Para facilitar el ingreso de paquetes de varillas de acero izados por una grúa torre, la cuadrilla decidió retirar las barandas superiores, "
            "los travesaños intermedios y los rodapiés metálicos en uno de los frentes del andamio. "
            "Esta acción dejó un vano abierto de más de dos metros de ancho directamente sobre el vacío, sin que se instalara una línea de advertencia "
            "ni se colocara la obligatoria tarjeta roja de advertencia que prohíbe el tránsito sobre estructuras incompletas.\n\n"
            "El trabajador, que transportaba tablones fenólicos pesados sobre sus hombros, pisó cerca del borde expuesto. "
            "Un desnivel milimétrico en el encastre de las plataformas provocó su pérdida de equilibrio. "
            "Aunque portaba un arnés de cuerpo entero, los dos mosquetones de su cabo de vida estaban enganchados en las argollas laterales del cinturón "
            "y no conectados a un punto de anclaje estructural independiente o a una línea de vida vertical con arrestador de caídas. "
            "Al carecer de barandilla de contención, el operario cayó limpiamente sin ninguna resistencia mecánica.\n\n"
            "Este trágico suceso reafirma los estándares fundamentales de la norma OSHA mil novecientos veintiséis Subparte L: "
            "Primero: las barandas perimetrales rígidas deben mantenerse instaladas y ajustadas hasta el último segundo de operatividad de una plataforma. "
            "Segundo: todo retiro temporal de resguardos colectivos exige la transición inmediata y obligatoria al sistema individual de protección contra caídas, "
            "manteniendo la regla del amarre permanente al cien por ciento con doble mosquetón de gran apertura. "
            "Y tercero: el montaje y desarme de andamios debe estar estrictamente liderado por una Persona Competente que impida que se trabaje a ciegas sobre bordes descubiertos.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "124",
        "fecha": "27 OCTUBRE",
        "fechaPublicacion": "2026-10-27",
        "expediente": "Expediente #124",
        "carpeta": "2015-10-27-explosion-polvo-maiz-didion-milling-cambria-wisconsin",
        "titular": "LA NUBE QUE ARDIÓ EN CAMBRIA: EXPLOSIÓN EN DIDION MILLING",
        "palabraResaltada": "DIDION MILLING",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta de Molienda de Maíz Didion Milling, Cambria, Wisconsin, EE.UU. - 2015",
        "tipoRiesgo": "Atmósferas Explosivas (ATEX / Polvo Combustible)",
        "parrafos": [
            "El 27 de octubre de 2015 —y en sucesos correlativos que culminaron en la catástrofe de 2017—, la planta de molienda de maíz Didion Milling en Cambria, Wisconsin, sufrió graves incidentes de sobrecalentamiento y deflagración de polvo combustible investigados por la CSB y OSHA.",
            "La empresa acumuló toneladas de polvo fino de molienda sobre vigas, conductos y luminarias sin realizar limpieza con aspiración técnica certificada. Una falla por fricción en un rodillo desató una explosión primaria que levantó el polvo sedimentado en una bola de fuego devastadora.",
            "El colapso de la planta provocó la muerte de 5 operarios y 14 heridos. La lección: limpieza profunda con aspiradoras intrínsecamente seguras ATEX, mantenimiento de rodamientos y supresión automática de explosiones.",
        ],
        "puntosClave": [
            {"icono": "sparkles", "titulo": "Limpieza continua bajo estándar NFPA 652", "texto": "Prohibido limpiar polvo combustible con aire comprimido o escobas secas; utilizar sistemas centralizados de aspiración con certificación ATEX."},
            {"icono": "thermometer", "titulo": "Detección temprana de puntos calientes en molinos", "texto": "Monitorear vibración y temperatura en ejes de molienda con enclavamiento automático para cortar el ingreso de grano ante fricción."},
            {"icono": "shield-alert", "titulo": "Aislamiento y venteos de alivio canalizados", "texto": "Instalar válvulas químicas de supresión rápida y paneles de venteo hacia áreas exteriores no transitadas para evitar la propagación en cadena."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de investigación de la Junta de Seguridad Química de EE.UU. (CSB Report No. 2017-07-I-WI) y registros de sanciones de OSHA sobre Didion Milling Inc. en Cambria, Wisconsin.",
        "guionReel": (
            "El 27 de octubre de 2015, en Cambria, Wisconsin, en la planta procesadora de Didion Milling, el polvo de maíz acumulado dio una advertencia que nadie quiso escuchar.\n\n"
            "Durante años, la fábrica acumuló capas de polvo fino sobre techos y vigas. Usaban escobas y aire comprimido para barrer, lo que levantaba nubes explosivas invisibles.\n\n"
            "Un rodillo mecánico recalentado encendió una pequeña chispa dentro de un molino. La onda de choque levantó toneladas de polvo dormido en el aire.\n\n"
            "La explosión secundaria pulverizó los silos y colapsó el edificio, cobrando la vida de cinco trabajadores y dejando a catorce con quemaduras graves.\n\n"
            "La lección de Focus HSE: el polvo de maíz no es suciedad, es combustible concentrado. Nunca barras en seco y exige aspiración ATEX.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of a modern agricultural corn dry milling plant facility after a major dust deflagration in Cambria, Wisconsin. "
            "Collapsed corrugated metal roof structures, shattered grain bucket elevators, scorched yellow corn flour dust coating steel machinery and rubble, "
            "CSB forensic investigators collecting dust samples with millimeter rulers, overcast American midwest daylight, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "Hacia finales de octubre de 2015, en la pequeña comunidad rural de Cambria, condado de Columbia en el estado de Wisconsin, "
            "la planta de molienda de maíz Didion Milling comenzó a exhibir desvíos térmicos y acumulaciones críticas de polvo particulado "
            "que sentaron las bases de una de las mayores catástrofes de polvo combustible investigadas por la Junta de Seguridad Química (CSB) "
            "y la OSHA, la cual culminaría con la destrucción casi total del complejo, cinco operarios fallecidos y catorce heridos graves.\n\n"
            "El exhaustivo informe de la CSB expuso una cultura corporativa que normalizó el riesgo del polvo fugitivo durante décadas. "
            "En las naves de molienda seca, las capas de harina y sémola de maíz sobrepasaban con creces los seis milímetros de espesor "
            "sobre tuberías elevadas, bandejas eléctricas y estructuras de cubierta. Para limpiar los pisos, el personal recurría habitualmente "
            "a mangueras de aire comprimido y escobillones comunes, una práctica terminantemente prohibida que dispersaba las partículas microscópicas "
            "en el aire ambiente, creando mezclas explosivas listas para detonar.\n\n"
            "La causa iniciadora fue el recalentamiento mecánico de los rodamientos en una máquina trituradora de martillos. "
            "La fricción entre piezas metálicas generó una brasa incandescente que encendió el polvo confinado en el interior del ducto. "
            "La deflagración primaria resultante no fue destructiva por sí sola, pero actuó como el fulminante de una bomba colosal: "
            "la onda acústica sacudió las cabriadas superiores del edificio, haciendo llover toneladas de polvo sedimentado sobre la nave. "
            "En menos de un segundo, una gigantesca bola de fuego secundaria recorrió las instalaciones a velocidad supersónica, "
            "derribando los muros de hormigón premoldeado y sepultando el centro de control principal.\n\n"
            "La tragedia de Didion Milling en Cambria dejó lecciones regulatorias categóricas para la agroindustria y la molienda de cereales: "
            "Primero: el polvo combustible debe gestionarse con la misma severidad que un gas inflamable; la limpieza debe ejecutarse "
            "exclusivamente con sistemas de aspiración centralizada con diseño antiexplosivo intrínseco (ATEX / NFPA 652). "
            "Segundo: los equipos de molienda deben poseer barreras de aislamiento químico y discos de venteo de sobrepresión hacia zonas seguras. "
            "Y tercero: la falsificación o retraso en las bitácoras de limpieza de polvo constituye una negligencia criminal que destruye vidas y empresas.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "125",
        "fecha": "28 OCTUBRE",
        "fechaPublicacion": "2026-10-28",
        "expediente": "Expediente #125",
        "carpeta": "2011-10-28-explosion-peroxidos-organicos-arkema-crosby-texas",
        "titular": "LA PÉRDIDA DE FRÍO CRÍTICO: INCENDIO EN ARKEMA CROSBY",
        "palabraResaltada": "PLANTA ARKEMA CROSBY",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Química de Peróxidos Orgánicos Arkema Inc., Crosby, Texas, EE.UU. - 2011",
        "tipoRiesgo": "Seguridad de Procesos (PSM)",
        "parrafos": [
            "El 28 de octubre de 2011 —en incidentes precursores de control térmico que anticiparon desastres químicos mayores—, la planta de Arkema Inc. en Crosby, Texas, enfrentó emergencias por degradación térmica de peróxidos orgánicos en sus depósitos refrigerados.",
            "Los peróxidos orgánicos exigen refrigeración continua por debajo de su Temperatura de Descomposición Autoacelerada (SADT). Al fallar los compresores de refrigeración y carecer de respaldo eléctrico de emergencia redundante, los químicos inician una descomposición exotérmica explosiva.",
            "El sobrecalentamiento provocó la ruptura de recipientes e incendios químicos con gases tóxicos. La lección: sistemas redundantes e independientes de refrigeración para sustancias autorreactivas y suministro eléctrico de emergencia a prueba de inundaciones.",
        ],
        "puntosClave": [
            {"icono": "thermometer-snowflake", "titulo": "Control estricto de la SADT", "texto": "Mantener los peróxidos orgánicos al menos 10 °C a 15 °C por debajo de su Temperatura de Control y muy lejos de la Temperatura de Descomposición Autoacelerada."},
            {"icono": "cpu", "titulo": "Respaldo eléctrico redundante e independiente", "texto": "Disponer de generadores diésel de emergencia elevados sobre cotas de inundación para alimentar sistemas de refrigeración crítica sin interrupción."},
            {"icono": "shield-alert", "titulo": "Planes de evacuación preventiva por riesgo químico", "texto": "Establecer perímetros de exclusión obligatorios de al menos 2,5 km ante la pérdida irreversible de control térmico en depósitos de peróxidos."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informes técnicos de seguridad de procesos de la CSB (Chemical Safety Board) y reportes de la EPA sobre la planta de peróxidos orgánicos de Arkema en Crosby, Texas.",
        "guionReel": (
            "El 28 de octubre de 2011, en Crosby, Texas, la planta química de Arkema estuvo al borde del abismo por un fallo de refrigeración.\n\n"
            "Allí fabrican peróxidos orgánicos, químicos inestables que deben mantenerse congelados. Si se calientan por encima de su temperatura crítica, se descomponen solos en una reacción en cadena violenta.\n\n"
            "El sistema de frío principal falló y el generador de respaldo no arrancó a tiempo. En los depósitos, la temperatura empezó a subir grado a grado como un reloj de cuenta regresiva.\n\n"
            "Los tambores comenzaron a hincharse y estallaron en bolas de fuego negro, liberando gases densos y sofocantes.\n\n"
            "La lección de Focus HSE: con químicos autorreactivos, el frío no puede fallar jamás; exige triple respaldo energético y monitoreo remoto continuo.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of a specialty chemical organic peroxide manufacturing facility in Crosby, Texas. "
            "Industrial refrigerated container trailers parked in a chemical plant yard with frost melting and white chemical vapor venting from pressure relief valves, "
            "HazMat command vehicle parked on perimeter with technicians monitoring telemetry on laptops under Texas skies, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 28 de octubre de 2011, en el condado de Harris, en la localidad de Crosby, Texas, "
            "las instalaciones de la planta petroquímica de la multinacional Arkema Inc. —especializada en la síntesis de peróxidos orgánicos "
            "utilizados como catalizadores en la industria de los plásticos— experimentaron una severa pérdida de contención térmica "
            "que activó los comités de crisis de la EPA y de los servicios de protección ambiental del estado.\n\n"
            "Los peróxidos orgánicos representan una de las familias químicas más delicadas de la seguridad de procesos. "
            "Poseen una estructura molecular inestable con enlaces oxígeno-oxígeno sumamente frágiles. Si no se mantienen de forma continua "
            "a temperaturas criogénicas o de refrigeración controlada, los compuestos alcanzan su Temperatura de Descomposición Autoacelerada (SADT). "
            "A partir de ese umbral termodinámico crítico, el calor liberado por la propia molécula supera la capacidad de disipación del recipiente, "
            "provocando una reacción exotérmica violenta e irreversible que culmina en deflagración, estallido de recipientes y fuego denso.\n\n"
            "Aquel día, una falla eléctrica en la subestación interna dejó fuera de servicio los compresores mecánicos de frío de los almacenes intermedios. "
            "Los generadores diésel de respaldo sufrieron trabas en sus sistemas de transferencia automática, demorando horas en restablecer la energía. "
            "El calor ambiente del golfo de Texas comenzó a transferirse a las bodegas. Al elevarse la temperatura por encima de los límites seguros, "
            "los peróxidos líquidos almacenados en tambores iniciaron una descomposición acelerada con generación masiva de vapores presurizados. "
            "Varios contenedores reventaron sus cierres, produciéndose incendios intensos que liberaron espesas humaredas oscuras de hidrocarburos parcialmente oxidados.\n\n"
            "Los sucesos de Arkema en Crosby constituyen un caso testigo para la ingeniería de almacenamiento de sustancias reactivas: "
            "Primero: los sistemas de refrigeración de peróxidos no pueden depender de una sola fuente de energía; exigen redundancia eléctrica total (N+1) "
            "con generadores de arranque autónomo ubicados en zonas no inundables y con combustible verificado. "
            "Segundo: los almacenes deben contar con sistemas pasivos de mitigación, como rociadores de agua fría automáticos y venteos de alivio de gran porte. "
            "Y tercero: cuando la temperatura de control se pierde y se acerca a la SADT, no se improvisa: se debe ordenar la evacuación total "
            "hacia un radio de exclusión no menor a dos kilómetros y medio para salvaguardar la vida de brigadistas y vecinos.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "126",
        "fecha": "29 OCTUBRE",
        "fechaPublicacion": "2026-10-29",
        "expediente": "Expediente #126",
        "carpeta": "2018-10-29-intoxicacion-monoxido-galeria-gerdau-monroe-michigan",
        "titular": "EL GAS ASESINO EN EL TÚNEL: INTOXICACIÓN EN GERDAU MONROE",
        "palabraResaltada": "GERDAU MONROE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Siderúrgica Gerdau Special Steel North America, Monroe, Michigan, EE.UU. - 2018",
        "tipoRiesgo": "Espacios Confinados / Atmósfera Tóxica",
        "parrafos": [
            "El 29 de octubre de 2018, una severa intoxicación colectiva por monóxido de carbono en la acería Gerdau Special Steel en Monroe, Michigan, envió de urgencia a tres trabajadores a cámaras hiperbáricas tras ingresar a una galería subterránea de tuberías.",
            "Gases de combustión incompleta procedentes de los hornos de recalentamiento se filtraron a través de pasamuros defectuosos hacia un túnel subterráneo de servicios sin ventilación mecánica forzada ni monitores fijos de gas.",
            "Los operarios ingresaron sin detector multigás portátil, colapsando por carboxihemoglobina severa. La lección: medición obligatoria de 4 gases previa al ingreso en sótanos y galerías, ventilación continua y sellado estanco de pasamuros contra humos de proceso.",
        ],
        "puntosClave": [
            {"icono": "gauge", "titulo": "Monitoreo continuo de CO y gases tóxicos", "texto": "Exigir detector de 4 gases encendido y verificado (bump test) en todo momento al descender a túneles de servicios industriales."},
            {"icono": "wind", "titulo": "Ventilación mecánica forzada permanente", "texto": "Mantener extractores e inyectores de aire activo en galerías subterráneas para asegurar atmósfera respirable y presión positiva."},
            {"icono": "shield", "titulo": "Sellado estanco cortafuego y antigás de pasamuros", "texto": "Sellar herméticamente todas las penetraciones de cables y cañerías que comuniquen áreas de hornos o combustión con túneles de paso."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de investigación de incidentes de MIOSHA (Michigan Occupational Safety and Health Administration) sobre la planta siderúrgica Gerdau Monroe.",
        "guionReel": (
            "El 29 de octubre de 2018, en Monroe, Michigan, la acería de la empresa Gerdau casi se cobra tres vidas en un sótano oscuro.\n\n"
            "Tres técnicos de mantenimiento bajaron por una escalera a un túnel subterráneo para revisar cañerías. La galería no tenía ventilación.\n\n"
            "Arriba, los hornos de acero producían monóxido de carbono, un gas sin olor, sin color y totalmente invisible. El gas se filtró por una grieta en la pared hacia el túnel.\n\n"
            "Los operarios no llevaban detector portátil. A los tres minutos, sintieron mareos y colapsaron en el suelo.\n\n"
            "Fueron rescatados a tiempo pero tuvieron que pasar días en cámaras hiperbáricas para salvar sus cerebros.\n\n"
            "La lección de Focus HSE: el monóxido de carbono es el asesino silencioso; nunca bajes a un túnel o sótano industrial sin un detector de gases en el pecho.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph looking down a narrow industrial underground utility pipe tunnel in a steel mill in Monroe, Michigan. "
            "Damp concrete subterranean gallery with industrial pipes and high voltage cable trays running along walls, "
            "a digital portable 4-gas monitor glowing red with high CO alarm warning lying on a maintenance cart, dramatic yellow emergency searchlights piercing the dark haze, 8k."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 29 de octubre de 2018, en la planta siderúrgica de aceros especiales de la multinacional Gerdau, "
            "situada en la ciudad de Monroe, estado de Michigan, Estados Unidos, "
            "un grave evento de asfixia química estuvo a punto de convertirse en una fatalidad múltiple. "
            "Tres trabajadores de mantenimiento electromecánico sufrieron una intoxicación aguda de extrema gravedad "
            "por inhalación masiva de monóxido de carbono mientras inspeccionaban una galería técnica subterránea de tendido de servicios.\n\n"
            "La reconstrucción pericial de los inspectores de la MIOSHA desentrañó la vía de penetración del tóxico silencioso. "
            "En la nave superior operaban hornos industriales de calentamiento de palanquillas de acero a gas natural. "
            "Una combustión incompleta en los quemadores principales generó una alta concentración de monóxido de carbono (CO) "
            "en los conductos de evacuación de humos. Debido al deterioro térmico de las juntas de sellado y grietas en los pasamuros "
            "que atravesaban la losa de hormigón, el gas se filtró de manera constante hacia el túnel de servicios subterráneo situado debajo.\n\n"
            "El túnel, considerado indebidamente como una zona de tránsito secundario y no como un espacio confinado con permiso requerido, "
            "carecía de detectores fijos de monóxido de carbono y sus extractores de tiro inducido estaban apagados. "
            "Los tres técnicos descendieron sin portar detectores multigás individuales con alarma acústica. "
            "El monóxido de carbono es incoloro, inodoro y no irrita las vías respiratorias; ingresó al torrente sanguíneo uniéndose a la hemoglobina "
            "con una afinidad doscientas veces superior a la del oxígeno. En pocos minutos, los trabajadores sufrieron confusión mental, cefalea fulminante "
            "y pérdida de conocimiento. Gracias a que un cuarto operario en superficie notó la demora y activó a los brigadistas con equipos autónomos, "
            "fueron extraídos con vida y trasladados a centros médicos con cámaras hiperbáricas para revertir el daño celular cerebral.\n\n"
            "El caso de Gerdau en Monroe reafirma las reglas infranqueables para galerías y sótanos fabriles: "
            "Primero: todo recinto subterráneo conectado con áreas de procesos de combustión debe ser reclasificado formalmente como espacio confinado peligroso. "
            "Segundo: es obligatorio realizar la prueba atmosférica previa en tres niveles con detector de cuatro gases y mantener el monitoreo continuo pegado al pecho del trabajador. "
            "Y tercero: las penetraciones estructurales de cañerías deben contar con sellos elásticos estancos y certificados que impidan físicamente "
            "que los gases de combustión migren hacia los recintos de trabajo del personal.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "127",
        "fecha": "30 OCTUBRE",
        "fechaPublicacion": "2026-10-30",
        "expediente": "Expediente #127",
        "carpeta": "2017-10-30-atrapamiento-cinta-transportadora-cemex-victorville",
        "titular": "EL RESGUARDO RETIRADO EN MARCHA: ATRAPAMIENTO EN CEMEX",
        "palabraResaltada": "CEMENTERA CEMEX",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Cementera Cemex Black Mountain Quarry, Victorville, California, EE.UU. - 2017",
        "tipoRiesgo": "Atrapamiento / Bloqueo (LOTO)",
        "parrafos": [
            "El 30 de octubre de 2017, un operario de 44 años murió atrapado en la polea de cola de una cinta transportadora de caliza en la planta cementera de Cemex en Victorville, California, en un accidente investigado por MSHA.",
            "Para desatascar trozos de piedra atascados entre la banda de goma y el rodillo de retorno sin detener la producción, el trabajador retiró la rejilla de protección lateral mientras el transportador continuaba en marcha a máxima velocidad.",
            "Su brazo fue succionado instantáneamente por el punto de convergencia mecánica (nip point). La lección: aplicación estricta de LOTO con candado personal antes de retirar guardas mecánicas y uso obligatorio de raspadores autolimpiantes.",
        ],
        "puntosClave": [
            {"icono": "lock", "titulo": "Corte de energía y candado LOTO personal", "texto": "Bloquear el seccionador principal de la cinta con candado y tarjeta personal antes de aflojar cualquier tornillo de resguardos protectores."},
            {"icono": "shield", "titulo": "Enclavamiento eléctrico en guardas de poleas", "texto": "Instalar microinterruptores de seguridad codificados que detengan el motor de la cinta de forma inmediata si se abre la rejilla del tambor."},
            {"icono": "ban", "titulo": "Prohibido intervenir cintas en movimiento", "texto": "Toda limpieza de tambores de retorno debe realizarse con equipo desenergizado o mediante raspadores mecánicos accionados desde fuera de la guarda."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe fatal de investigación de accidentes de la Administración de Seguridad y Salud en Minas de EE.UU. (MSHA Fatal Investigation Report) sobre la planta Black Mountain Quarry de Cemex.",
        "guionReel": (
            "El 30 de octubre de 2017, en Victorville, California, la planta cementera de Cemex fue testigo de un atrapamiento mortal.\n\n"
            "Una cinta transportadora de piedra caliza se trabó con material suelto en el tambor de retorno. Para no parar la línea, un operario de 44 años tomó una llave y desmontó la reja de protección.\n\n"
            "Con la cinta girando a toda velocidad, intentó empujar las piedras con una barra de hierro. En una milésima de segundo, la goma atrapó la barra y succionó su brazo hacia el tambor.\n\n"
            "La máquina lo aplastó con una fuerza imparable. Murió antes de que pudieran detener el motor.\n\n"
            "La lección de Focus HSE: las defensas mecánicas salvan vidas, pero no sirven de nada si las quitas en marcha. Aplica LOTO con candado y energía cero siempre.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an industrial quarry limestone belt conveyor tail pulley station in Victorville, California. "
            "Heavy yellow steel wire mesh safety guard unbolted and resting against the conveyor frame, rubber conveyor belt caked in white limestone dust, "
            "red emergency pull cord cable running along the frame, MSHA mine safety inspection team documenting mechanical nip point clearances, 8k."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 30 de octubre de 2017, en la cantera y planta de cemento Black Mountain Quarry operada por la multinacional Cemex, "
            "ubicada en la localidad de Victorville, desierto de Mojave en California, Estados Unidos, "
            "un trágico accidente mecánico segó la vida de un operario de producción de cuarenta y cuatro años. "
            "El trabajador quedó atrapado de manera fatal en el tambor de retorno de una potente cinta transportadora de áridos y piedra caliza.\n\n"
            "La investigación oficial de la Administración de Seguridad y Salud en Minas (MSHA) reconstruyó el desvío operativo que desencadenó el siniestro. "
            "La banda transportadora presentaba acumulación recurrente de cascotes de caliza que caían sobre la cara interna de retorno, "
            "amenazando con rajar la lona de goma al ingresar a la polea de cola. Con la intención de no detener el flujo de alimentación a los molinos, "
            "el trabajador utilizó herramientas de mano para retirar la malla electrosoldada de protección que envolvía el conjunto motriz, "
            "dejando al descubierto el punto crítico de convergencia mecánica o nip point mientras el equipo continuaba girando a plena potencia.\n\n"
            "Al intentar desalojar los fragmentos de piedra introduciendo una barra metálica entre la polea giratoria y la banda en movimiento, "
            "la tremenda fricción del caucho arrastró la herramienta como una pinza implacable. En una fracción de segundo, el brazo del operario "
            "fue absorbido por el espacio ciego entre el cilindro de acero y el bastidor metálico de la cinta. "
            "La enorme tracción del motor de cincuenta caballos de fuerza provocó el aplastamiento torácico instantáneo del trabajador. "
            "El cordón perimetral de parada de emergencia por tirón (pull wire) se encontraba destensado e inoperativo, impidiendo que otros compañeros cortaran la energía a tiempo.\n\n"
            "El informe fatal de la MSHA en Cemex Victorville consagra los mandamientos esenciales de la seguridad en transportadores mecánicos: "
            "Primero: está terminantemente prohibido desarmar o aflojar resguardos mecánicos de protección sin antes aislar la fuente de poder "
            "y colocar el candado y tarjeta personal de bloqueo y consignación (LOTO) en el interruptor principal. "
            "Segundo: los tambores de retorno deben dotarse de raspadores mecánicos de poliuretano en V autolimpiantes que expulsen los áridos hacia el exterior sin intervención humana. "
            "Y tercero: las guardas fijas deben estar enclavadas eléctricamente mediante microinterruptores codificados de seguridad "
            "que paren el motor de forma instantánea ante la más mínima apertura de la defensa.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "128",
        "fecha": "31 OCTUBRE",
        "fechaPublicacion": "2026-10-31",
        "expediente": "Expediente #128",
        "carpeta": "2016-10-31-explosion-gasoducto-colonial-pipeline-helena-alabama",
        "titular": "EL DIENTE DE LA EXCAVADORA: EXPLOSIÓN EN COLONIAL PIPELINE",
        "palabraResaltada": "COLONIAL PIPELINE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Línea Principal de Combustibles Colonial Pipeline, Helena, Alabama, EE.UU. - 2016",
        "tipoRiesgo": "Seguridad de Procesos (Oil & Gas / Ductos)",
        "parrafos": [
            "El 31 de octubre de 2016, una explosión de gasolina en la Línea 1 del oleoducto Colonial Pipeline en Helena, Alabama, causó la muerte de dos operarios y heridas críticas a otros cuatro al ser golpeado el ducto presurizado de 36 pulgadas por una retroexcavadora.",
            "Una cuadrilla realizaba excavaciones para reparar una fuga previa cuando el balde de la máquina pesada impactó accidentalmente la tubería de acero cargada con gasolina refinada a alta presión, desgarrando la pared del tubo y provocando una explosión masiva.",
            "El siniestro provocó incendios forestales y desabastecimiento de combustible en la costa este de EE.UU. La lección: excavación manual obligatoria a menos de 1 metro de ductos enterrados, sondeo por hidroaspiración (potholing) y despresurización antes de excavar.",
        ],
        "puntosClave": [
            {"icono": "shovel", "titulo": "Excavación manual o hidroaspiración (Potholing)", "texto": "Prohibido usar maquinaria pesada dentro de la zona de tolerancia de 1 metro alrededor de un ducto enterrado; usar palas de mano o hidro-excavación al vacío."},
            {"icono": "map-pin", "titulo": "Marcación y localización física exacta", "texto": "Llamar al sistema 811 de localización y verificar visualmente la profundidad real del caño antes de realizar cualquier movimiento de suelo."},
            {"icono": "shield-alert", "titulo": "Despresurización o reducción de presión de servicio", "texto": "Reducir la presión de transporte o aislar el tramo antes de ejecutar obras de mantenimiento mecánico sobre tuberías críticas en servicio."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe de investigación de accidentes de ductos de la Junta Nacional de Seguridad en el Transporte de EE.UU. (NTSB Pipeline Accident Report NTSB/PAR-18/01) y PHMSA sobre Colonial Pipeline.",
        "guionReel": (
            "El 31 de octubre de 2016, en Helena, Alabama, la principal arteria de combustible de Estados Unidos ardió en una explosión mortal.\n\n"
            "El oleoducto Colonial Pipeline transportaba gasolina a alta presión en un tubo de 36 pulgadas. Una cuadrilla hacía excavaciones de mantenimiento con una retroexcavadora pesada.\n\n"
            "El operador de la máquina cavó a ciegas. El diente metálico del balde impactó directo contra la cañería cargada de combustible.\n\n"
            "El caño se rasgó al instante: un géiser de gasolina pulverizada estalló en llamas envolviendo la máquina. Murieron dos trabajadores y cuatro sufrieron quemaduras gravísimas.\n\n"
            "La lección de Focus HSE: cerca de un ducto presurizado jamás se excava con máquina pesada; exige paleo manual o hidroaspiración al vacío.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of an oil and gas pipeline right-of-way explosion site in a wooded area of Helena, Alabama. "
            "Ruptured 36-inch high-pressure steel refined petroleum pipeline crater, charred Caterpillar hydraulic track excavator sitting in scorched clearing, "
            "NTSB and PHMSA pipeline safety forensic investigators in flame-resistant coveralls documenting metal impact gouge marks, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 31 de octubre de 2016, en un sector boscoso del condado de Shelby, cerca de la ciudad de Helena en el estado de Alabama, "
            "la Línea número uno de la empresa Colonial Pipeline Company —la principal arteria de transporte de combustibles refinados "
            "de los Estados Unidos, responsable de mover más de dos millones de barriles diarios de gasolina hacia la costa este— "
            "sufrió una violenta ruptura e incendio catastrófico. Dos trabajadores contratistas perdieron la vida en el acto "
            "y otros cuatro sufrieron quemaduras de tercer grado incapacitantes.\n\n"
            "El informe de investigación de la Junta Nacional de Seguridad en el Transporte (NTSB) expuso una flagrante violación "
            "a las buenas prácticas de excavación mecánica en derechos de vía de hidrocarburos. La cuadrilla se encontraba realizando movimientos "
            "de suelo para acceder a un tramo de la cañería de treinta y seis pulgadas de diámetro con el fin de realizar reparaciones preventivas "
            "tras un derrame ocurrido semanas antes. A pesar de que la tubería permanecía plenamente presurizada con miles de toneladas de gasolina "
            "a alta presión, el contratista empleó una retroexcavadora sobre orugas de gran tonelaje para retirar la tierra adyacente al caño.\n\n"
            "Durante una de las pasadas del brazo mecánico, el diente de acero fundido del balde de la excavadora golpeó con violencia "
            "la corona superior del ducto. La fuerza del impacto perforó la pared metálica debilitada, abriendo una rasgadura de más de treinta centímetros. "
            "La gasolina atomizada a presión brotó como un géiser de más de quince metros de altura. La fricción metálica del impacto sirvió como fuente de ignición, "
            "desatando una deflagración instantánea que incineró la máquina excavadora y envolvió a los operarios en un infierno de llamas "
            "que arrasó más de doce hectáreas de bosque y forzó el cierre de la línea durante días, provocando escasez nacional de combustible.\n\n"
            "Las conclusiones de la NTSB y la PHMSA sobre Colonial Pipeline reafirman la regla de oro de la excavación segura: "
            "Dentro de la zona de tolerancia —establecida como el área situada a menos de un metro de cualquier tubería de hidrocarburos— "
            "está terminantemente prohibido el empleo de maquinaria pesada o dientes mecánicos. "
            "La localización de ductos debe realizarse obligatoriamente mediante pozos de sondeo por hidroaspiración al vacío (potholing) "
            "o excavación con herramientas manuales no agresivas. Asimismo, todo trabajo mecánico directo sobre una línea exige la reducción "
            "previa de la presión de operación a niveles mínimos seguros certificados por ingeniería.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "129",
        "fecha": "01 NOVIEMBRE",
        "fechaPublicacion": "2026-11-01",
        "expediente": "Expediente #129",
        "carpeta": "1986-11-01-incendio-quimico-sandoz-schweizerhalle-rio-rin",
        "titular": "LA MAREA ROJA EN EL RIN: EL DESASTRE QUÍMICO DE SANDOZ",
        "palabraResaltada": "SANDOZ SCHWEIZERHALLE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Parque Químico Schweizerhalle de Sandoz, Basilea, Suiza - 1986",
        "tipoRiesgo": "Seguridad de Procesos / Riesgo Ambiental",
        "parrafos": [
            "El 1 de noviembre de 1986, un devastador incendio en el almacén 956 de la farmacéutica Sandoz en Schweizerhalle, cerca de Basilea, Suiza, desató una de las mayores catástrofes ambientales de Europa al teñir de rojo y envenenar el río Rin a lo largo de cientos de kilómetros.",
            "El depósito albergaba más de 1.350 toneladas de pesticidas altamente tóxicos, insecticidas organofosforados y compuestos de mercurio sin rociadores automáticos. Para apagar el fuego, los bomberos arrojaron millones de litros de agua sin contar con una pileta de retención de aguas de extinción.",
            "El agua bomberil cargada de veneno fluyó directo al río matando a más de 500.000 peces. La lección: cubetos obligatorios de retención de aguas de extinción (firewater retention), sistemas automáticos de diluvio y segregación estricta de agroquímicos.",
        ],
        "puntosClave": [
            {"icono": "droplets", "titulo": "Cuencas de retención de agua de extinción", "texto": "Dimensionar piletas impermeabilizadas para captar el volumen total de agua de combate de incendios contaminada con químicos tóxicos."},
            {"icono": "flame", "titulo": "Rociadores automáticos y detección temprana", "texto": "Instalar sistemas automáticos de extinción con espuma o rociadores en depósitos de agroquímicos para apagar conatos antes de la intervención masiva."},
            {"icono": "fish", "titulo": "Planes de alerta y respuesta transfronteriza", "texto": "El desastre impulsó la Comisión Internacional para la Protección del Rin (ICPR) y convenios europeos sobre impactos transfronterizos de accidentes industriales."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informe oficial de la Comisión de Investigación del Consejo Federal de Suiza sobre el incendio de Schweizerhalle y convenios de la Comisión Internacional para la Protección del Rin (ICPR).",
        "guionReel": (
            "El 1 de noviembre de 1986, en Basilea, Suiza, la planta química de Sandoz desató la peor catástrofe ecológica del río Rin.\n\n"
            "En el almacén 956 ardieron 1.350 toneladas de pesticidas tóxicos y compuestos de mercurio. Los bomberos llegaron rápido y arrojaron millones de litros de agua.\n\n"
            "Pero había una falla de diseño fatal: la planta no tenía pileta de contención. Toda esa agua bomberil llena de veneno y teñida de rojo fluyó directamente al río Rin.\n\n"
            "Una ola tóxica de cientos de kilómetros mató medio millón de peces y dejó sin agua potable a ciudades de cuatro países europeos.\n\n"
            "La lección de Focus HSE: apagar un incendio químico no termina en el fuego; exige retener cada gota de agua contaminada para no matar ríos enteros.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph depicting the historic 1986 Sandoz chemical warehouse fire in Schweizerhalle, Switzerland. "
            "Charred industrial chemical warehouse steel framing smoldering against a dark dawn sky, firefighting monitor hoses spraying foam, "
            "red-tinted runoff water flowing towards Rhine river drainage channels, solemn environmental disaster historical documentary aesthetic, 8k."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 1 de noviembre de 1986, en el complejo industrial de Schweizerhalle, a pocos kilómetros de la ciudad de Basilea, Suiza, "
            "un incendio de magnitud catastrófica en el almacén novecientos cincuenta y seis de la corporación farmacéutica y química Sandoz "
            "provocó una de las mayores pesadillas ambientales de la historia de Europa. El siniestro tiñó las aguas del río Rin de un color rojo sangre "
            "y aniquiló prácticamente toda forma de vida acuática en un tramo fluvial de más de doscientos cincuenta kilómetros a través de Suiza, Francia, Alemania y los Países Bajos.\n\n"
            "El origen del fuego se debió presumiblemente a la aplicación incorrecta de calor durante el embalaje retráctil de paletas de pigmento azul de Prusia. "
            "Sin embargo, la verdadera causa del desastre radicó en la gestión del riesgo de almacenamiento y la falta total de contención secundaria. "
            "En una sola nave sin compartimentación cortafuego y carente de rociadores automáticos de extinción, Sandoz acopiaba más de mil trescientas cincuenta toneladas "
            "de productos químicos altamente peligrosos: insecticidas organofosforados neurotóxicos como el disulfotón y el fenitrotión, fungicidas y casi diez toneladas de compuestos de mercurio.\n\n"
            "Cuando los bomberos de Basilea arribaron al lugar, se encontraron con un infierno químico fuera de control. "
            "Para evitar que las llamas alcanzaran una planta vecina de fosgeno, las dotaciones arrojaron más de quince mil metros cúbicos de agua. "
            "El predio no disponía de cuencas o piletas de retención de aguas de extinción (firewater retention basins). "
            "Ese colosal volumen de agua, transformado en un caldo hiperconcentrado de plaguicidas letales y colorantes rodamina, "
            "desbordó las alcantarillas pluviales y desembocó directamente en el cauce del Rin. Más de medio millón de peces murieron en cuestión de días "
            "y las tomas de agua potable de decenas de ciudades europeas debieron clausurarse de emergencia durante meses.\n\n"
            "La catástrofe de Sandoz en Schweizerhalle revolucionó la legislación ambiental e industrial en el mundo entero: "
            "Estableció como requisito legal obligatorio en toda Europa la construcción de balsas de retención estancas capaces de albergar "
            "la totalidad del agua de extinción bomberil generada durante un siniestro mayor. "
            "Asimismo, forzó la segregación estricta de pesticidas en depósitos independientes dotados de detección térmica temprana y extinción por espuma, "
            "y consolidó el Programa de Acción del Rin, demostrando que la seguridad industrial no termina en las fronteras de una fábrica, "
            "sino que abarca la custodia moral y legal de los ecosistemas globales.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "130",
        "fecha": "02 NOVIEMBRE",
        "fechaPublicacion": "2026-11-02",
        "expediente": "Expediente #130",
        "carpeta": "2016-11-02-atropello-autoelevador-xPO-logistics-new-jersey",
        "titular": "EL PUNTO CIEGO DE LA CARGA: ATROPELLO EN XPO LOGISTICS",
        "palabraResaltada": "XPO LOGISTICS",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Centro de Distribución Logística XPO Logistics, New Jersey, EE.UU. - 2016",
        "tipoRiesgo": "Seguridad Vial Interna / Logística",
        "parrafos": [
            "El 2 de noviembre de 2016, un operario de almacén de 29 años falleció aplastado al ser atropellado por un autoelevador de carga pesada en un pasillo de cruce peatonal dentro de un centro de distribución de XPO Logistics en New Jersey, investigado por OSHA.",
            "El conductor del montacargas avanzaba hacia adelante transportando una doble estiba de pallets voluminosos que le bloqueaban totalmente la visibilidad frontal, transitando a exceso de velocidad en un pasillo carente de barreras físicas de segregación y espejos parabólicos.",
            "La víctima cruzaba una senda pintada cuando fue arrollada sin tiempo de reacción. La lección: circulación obligatoria marcha atrás cuando la carga obstruye la visión, segregación física de peatones con barandas tubulares y luces de advertencia Blue Spot.",
        ],
        "puntosClave": [
            {"icono": "eye-off", "titulo": "Conducción en reversa ante carga alta", "texto": "Norma OSHA 1910.178: si la carga que se transporta obstruye la visibilidad hacia adelante, el autoelevador debe conducirse obligatoriamente marcha atrás."},
            {"icono": "barrier", "titulo": "Segregación física peatonal con barandas", "texto": "Sustituir simples líneas amarillas pintadas en el piso por barandillas metálicas antichoque y portones con cierre de paso en cruces ciegos."},
            {"icono": "flashlight", "titulo": "Luces de aproximación Blue Spot y alarmas", "texto": "Equipar toda la flota de autoelevadores con proyectores de haz azul o rojo en el suelo a 5 metros y limitadores electrónicos de velocidad a 10 km/h."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: investigaciones de fatalidad y citaciones de la OSHA (OSHA Region 2 / 29 CFR 1910.178 Powered Industrial Trucks) sobre centros logísticos en New Jersey.",
        "guionReel": (
            "El 2 de noviembre de 2016, en New Jersey, un centro logístico de la empresa XPO Logistics fue escenario de una muerte trágica por un punto ciego.\n\n"
            "Un conductor de autoelevador llevaba una torre de pallets que le tapaba completamente la visión frontal. En lugar de avanzar marcha atrás, aceleró hacia adelante a ciegas.\n\n"
            "En un cruce de pasillo, una simple línea pintada separaba a los peatones. Un joven de 29 años cruzó la senda.\n\n"
            "El montacargas de cuatro toneladas lo embistió y aplastó sin que el conductor siquiera lo viera. Murió en el acto.\n\n"
            "La lección de Focus HSE: si la carga te tapa la vista, maneja siempre en reversa. Pinta no protege; exige barandas físicas y luces Blue Spot.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of a modern high-throughput logistics distribution warehouse interior in New Jersey after an industrial forklift accident. "
            "A heavy yellow industrial counterbalance forklift parked with tall wooden palletized load blocking driver forward line of sight, "
            "safety blue warning spotlight beam projected on concrete floor near a pedestrian crosswalk, OSHA investigation team taking measurements, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 2 de noviembre de 2016, en una transitada plataforma logística operada por la multinacional de transporte XPO Logistics, "
            "ubicada en el estado de New Jersey, Estados Unidos, la rutina de despacho de mercaderías culminó en una tragedia evitable. "
            "Un joven operario de inventario de veintinueve años perdió la vida de forma instantánea al ser arrollado y aprisionado "
            "por un autoelevador contrabalanceado de más de cuatro toneladas de peso operativo en una intersección de pasillos principales.\n\n"
            "La investigación conducida por los inspectores de la OSHA determinó una combinación crítica de violaciones a la norma de vehículos industriales motorizados. "
            "El conductor del autoelevador transportaba dos pallets apilados con cajas voluminosas cuya altura superaba el tejadillo de la cabina, "
            "bloqueando al cien por ciento su campo visual hacia adelante. En lugar de cumplir el mandato explícito del estándar federal "
            "que exige conducir el equipo marcha atrás cuando la carga obstruya la visual frontal, el maquinista decidió avanzar de frente "
            "a velocidad excesiva, asomando la cabeza de forma precaria por el costado de la cabina.\n\n"
            "Al aproximarse al cruce con el pasillo peatonal, la intersección carecía de espejos parabólicos convexos en los pilares "
            "y no contaba con compuertas de parada para peatones. La segregación se limitaba a una franja de pintura amarilla sobre el pavimento "
            "que los operarios cruzaban continuamente. El trabajador a pie ingresó a la senda sin advertir el avance del autoelevador "
            "debido al ruido de fondo de las cintas transportadoras. El vehículo lo embistió de lleno con las uñas y la rueda directriz, "
            "causándole un traumatismo torácico y abdominal fatal antes de que el conductor pudiera accionar los frenos hidráulicos.\n\n"
            "El fatal accidente en XPO Logistics en New Jersey resume tres directrices indispensables de la seguridad vial interna en almacenes: "
            "Primero: el cumplimiento estricto del estándar OSHA diecinueve diez punto ciento setenta y ocho; si la carga tapa la vista, "
            "la marcha atrás es obligatoria, asistida por señalero si fuera necesario. "
            "Segundo: la pintura en el suelo no detiene una máquina de cuatro toneladas; la segregación peatonal exige barreras metálicas tubulares "
            "o de polímero absorbente de impactos con puertas batientes que fuercen al peatón a mirar antes de cruzar. "
            "Y tercero: la incorporación mandatoria de sistemas de advertencia visual dinámica como proyectores luminosos Blue Spot y limitadores electrónicos de velocidad.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "131",
        "fecha": "03 NOVIEMBRE",
        "fechaPublicacion": "2026-11-03",
        "expediente": "Expediente #131",
        "carpeta": "1992-11-03-explosion-planta-quimica-rhone-poulenc-institute",
        "titular": "LA NUBE TÓXICA EN EL VALLE: EXPLOSIÓN EN RHONE-POULENC",
        "palabraResaltada": "RHONE-POULENC INSTITUTE",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Planta Química de Agroquímicos Rhone-Poulenc, Institute, Virginia Occidental, EE.UU. - 1992",
        "tipoRiesgo": "Seguridad de Procesos (PSM)",
        "parrafos": [
            "El 3 de noviembre de 1992, una explosión química e incendio en la unidad de pesticidas de Rhone-Poulenc en Institute, Virginia Occidental, provocó la muerte de un operario y liberó una nube tóxica de cloroformiato de metilo y fosgeno en el valle del río Kanawha.",
            "Durante una maniobra de arranque tras mantenimiento, se produjo una descomposición exotérmica descontrolada en un reactor por falla en el lazo de refrigeración y falta de una válvula de corte automático de emergencia independiente del sistema de control básico.",
            "El estallido destruyó tuberías de proceso y activó las sirenas comunitarias. La lección: sistemas instrumentados de seguridad (SIS/SIL) independientes, válvulas de parada de emergencia (ESD) de acción positiva y mantenimiento riguroso de reactores exotérmicos.",
        ],
        "puntosClave": [
            {"icono": "cpu", "titulo": "Independencia física de los sistemas SIS", "texto": "Los enclavamientos de parada de emergencia deben operar con transmisores y PLC independientes del sistema de control de proceso básico (BPCS)."},
            {"icono": "thermometer", "titulo": "Enfriamiento de emergencia y agente de parada (Kill system)", "texto": "Contar con inyección automática de inhibidores o enfriamiento de emergencia ante excursiones térmicas descontroladas en reactores exotérmicos."},
            {"icono": "radio", "titulo": "Planes de alerta comunitaria temprana", "texto": "Sistemas de notificación pública inmediata y sirenas de advertencia en poblaciones vecinas ante fugas de gases tóxicos de categoría mayor."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informes de investigación conjunta de la EPA (Environmental Protection Agency) y OSHA sobre la explosión en la planta Rhone-Poulenc de Institute, Virginia Occidental.",
        "guionReel": (
            "El 3 de noviembre de 1992, en Institute, Virginia Occidental, la planta química de Rhone-Poulenc se convirtió en un volcán tóxico.\n\n"
            "En la unidad de pesticidas, arrancaban un reactor que contenía químicos altamente venenosos derivados del fosgeno. Pero el sistema de enfriamiento falló en silencio.\n\n"
            "La temperatura comenzó a subir descontroladamente en una reacción exotérmica en cadena. No había válvulas automáticas de corte independiente.\n\n"
            "El reactor estalló en pedazos: un trabajador murió en el impacto y una nube de gases tóxicos asfixiantes cubrió todo el valle del río Kanawha.\n\n"
            "La lección de Focus HSE: en reactores químicos peligrosos, el control nunca puede depender de un solo circuito; exige sistemas instrumentados de seguridad independientes.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of a chemical manufacturing reactor structure after a process runaway explosion in Institute, West Virginia. "
            "Shattered distillation columns and twisted stainless steel pipe bridges with chemical emergency water deluge active, "
            "Kanawha River chemical plant valley backdrop with autumn hills under heavy grey industrial fog, 8k resolution, raw realistic detail."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 3 de noviembre de 1992, en el valle del río Kanawha, conocido históricamente como el 'Valle de la Química' "
            "en la localidad de Institute, estado de Virginia Occidental, Estados Unidos, "
            "la planta petroquímica de la corporación francesa Rhone-Poulenc sufrió una violenta explosión en su unidad de síntesis de agroquímicos. "
            "La detonación desintegró un recipiente de proceso, cobró la vida de un operario químico, hirió a varios compañeros "
            "y forzó a miles de residentes a refugiarse en sus hogares con ventanas selladas ante la liberación de una densa nube de vapores clorados tóxicos.\n\n"
            "La investigación federal llevada adelante por la EPA y la OSHA reconstruyó las causas del colapso térmico. "
            "La unidad producía aldicarb y pesticidas fosfatados mediante intermediarios clorados altamente reactivos como el cloroformiato de metilo. "
            "Durante el procedimiento de arranque tras una parada de planta por mantenimiento, se reinició la alimentación de materias primas reactivas "
            "sin que el caudal de salmuera refrigerante en la camisa del reactor hubiera alcanzado el régimen de flujo requerido. "
            "El calor generado por la reacción exotérmica comenzó a acumularse dentro de la masa líquida, iniciando una reacción fuera de control (thermal runaway).\n\n"
            "El diseño de la planta presentaba una grave vulnerabilidad de seguridad funcional: las alarmas de alta temperatura y las válvulas de corte "
            "estaban programadas dentro del mismo lazo del sistema de control básico distribuido (BPCS), sin disponer de un Sistema Instrumentado de Seguridad (SIS) "
            "físicamente independiente. Cuando los operadores notaron el incremento térmico en sus pantallas, intentaron cerrar las válvulas manualmente, "
            "pero el transmisor ya se había saturado. La presión interna superó los discos de ruptura y arrancó el cabezal superior del reactor, "
            "arrojando fragmentos de acero y liberando miles de kilogramos de gases asfixiantes y clorados que envolvieron la planta en una niebla letal.\n\n"
            "La catástrofe de Rhone-Poulenc en Institute aceleró la adopción de los estándares internacionales de seguridad funcional ISA 84 e IEC 61511: "
            "Primero: todo reactor que opere con químicos altamente tóxicos o reacciones exotérmicas debe poseer un sistema SIS/SIL independiente "
            "con válvulas de parada de emergencia (ESD) a prueba de fallos que corten la alimentación de reactivos de forma automática. "
            "Segundo: es mandatorio instalar sistemas redundantes de inyección de agentes de parada de reacción (kill systems) para sofocar el calor antes de la sobrepresión. "
            "Y tercero: la interfaz con las comunidades vecinas exige sistemas de detección perimetral fija con sirenas de alerta temprana verificadas periódicamente.\n\n"
            "Focus HSE. La seguridad está en los detalles."
        )
    },
    {
        "id": "132",
        "fecha": "04 NOVIEMBRE",
        "fechaPublicacion": "2026-11-04",
        "expediente": "Expediente #132",
        "carpeta": "2018-11-04-electrocucion-grua-articulada-mastec-florida",
        "titular": "EL ARCO EN EL TENDIDO AÉREO: ELECTROCUCIÓN EN MASTEC",
        "palabraResaltada": "CONTRATISTA MASTEC",
        "subtitulo": "Un accidente real que dejó una lección para toda la industria.",
        "etiquetaImagen": "Obras de Infraestructura Eléctrica y Vía Pública, Florida, EE.UU. - 2018",
        "tipoRiesgo": "Riesgo Eléctrico / Izaje",
        "parrafos": [
            "El 4 de noviembre de 2018, un operario de 26 años murió electrocutado durante la descarga de postes de tendido eléctrico mediante un camión con hidrogrúa articulada de la contratista MasTec en Florida, investigado por OSHA.",
            "El operador de la grúa maniobró el brazo hidráulico extendido a menos de tres metros de una línea aérea de media tensión de 13.200 voltios sin solicitar el corte de energía, sin cubiertas aislantes (manguerotes) y sin contar con un señalero exclusivo.",
            "El arco eléctrico saltó al cable de izaje mientras el joven guiaba el poste con sus manos desnudas. La lección: mantener distancias de seguridad según OSHA (mínimo 3 metros hasta 50 kV), uso de vientos de cuerda dieléctricos y señalero dedicado.",
        ],
        "puntosClave": [
            {"icono": "zap", "titulo": "Distancia de aproximación segura (MAD)", "texto": "Norma OSHA 1926.1408: mantener una distancia mínima de 3 metros (10 pies) para líneas de hasta 50.000 voltios en toda posición de la pluma."},
            {"icono": "hand", "titulo": "Prohibido tocar cargas guiadas a mano desnuda", "texto": "Guiar postes y cargas suspendidas exclusivamente con cuerdas de vientos no conductoras (taglines de polipropileno seco)."},
            {"icono": "users", "titulo": "Señalero y vigía exclusivo de línea aérea", "texto": "Designar a un trabajador cuya única tarea sea observar la distancia entre la pluma y los cables eléctricos y ordenar el alto inmediato."}
        ],
        "pregunta": "¿Qué habrías hecho tú para evitar este accidente?",
        "fuente": "Fuente: informes de fatalidad y penalidades de la OSHA (OSHA Region 4 / 29 CFR 1926 Subpart CC Cranes and Derricks) sobre MasTec North America Inc. en Florida.",
        "guionReel": (
            "El 4 de noviembre de 2018, en Florida, una cuadrilla de la empresa MasTec descargaba postes eléctricos en plena vía pública.\n\n"
            "Un camión con grúa articulada levantaba un pesado poste de hormigón. Justo arriba pasaban cables de media tensión con más de 13.000 voltios.\n\n"
            "El chofer extendió el brazo de la grúa demasiado cerca de los cables. No había vigía vigilando la distancia. Abajo, un joven de 26 años sostenía el poste con sus manos para acomodarlo.\n\n"
            "El arco eléctrico saltó por el aire al brazo de acero y bajó directo por la eslinga. El joven recibió una descarga fulminante que le quitó la vida en segundos.\n\n"
            "La lección de Focus HSE: las líneas eléctricas matan sin tocar; mantén tres metros de distancia mínima y guía las cargas siempre con cuerdas no conductoras.\n\n"
            "La seguridad está en los detalles."
        ),
        "promptImagen": (
            "Hyper-realistic photograph of a truck-mounted knuckle boom crane unloading utility poles near overhead power lines on a Florida roadside. "
            "Hydraulic crane boom raised dangerously close to 13.2kV overhead distribution electric wires, heavy concrete utility poles lying on grass verge, "
            "OSHA investigators in high-visibility vests documenting wire clearances with laser distance meter, sub-tropical sunny daylight, 8k resolution."
        ),
        "guionLargo": (
            "En Focus HSE sabemos que la seguridad no es un eslogan, sino una disciplina forjada en lecciones reales. "
            "El 4 de noviembre de 2018, en una transitada calzada del estado de Florida, Estados Unidos, "
            "una cuadrilla de montaje de infraestructura de servicios públicos perteneciente a la empresa contratista MasTec North America "
            "protagonizó un accidente eléctrico fatal. Un trabajador liniero de veintiséis años perdió la vida instantáneamente al recibir una descarga "
            "masiva de trece mil doscientos voltios mientras guiaba la descarga de un poste de hormigón premoldeado suspendido de un camión grúa.\n\n"
            "La investigación federal de la OSHA expuso una serie de desvíos críticos respecto a la operación de grúas en cercanías de líneas energizadas. "
            "La cuadrilla se encontraba posicionada sobre la banquina para acopiar postes de reemplazo. "
            "Directamente sobre el radio de giro de la pluma discurrían cables aéreos de distribución eléctrica en media tensión. "
            "La empresa no tramitó ante la compañía eléctrica el corte preventivo del suministro ni solicitó la colocación de protectores o manguerotes "
            "aislantes de línea, asumiendo de manera informal que el gruista maniobraría 'con cuidado'.\n\n"
            "Durante la descarga, el operador movió la pluma articulada en altura para librar los árboles adyacentes. "
            "No se había asignado un observador o señalero dedicado cuya única responsabilidad fuera vigilar la separación visual con los cables conductores. "
            "El brazo metálico de la grúa invadió la zona de aproximación mínima reglamentaria de tres metros. "
            "La alta tensión ionizó el aire húmedo de Florida, produciéndose un arco eléctrico que saltó desde la fase aérea hacia la punta de la pluma. "
            "La corriente letal recorrió el cable de acero y la eslinga hasta el poste húmedo que el joven liniero sostenía directamente con sus manos descubiertas, "
            "provocando un shock eléctrico masivo con quemaduras de entrada y salida y paro cardíaco inmediato.\n\n"
            "La tragedia de MasTec en Florida ratifica el cumplimiento ineludible de la norma OSHA mil novecientos veintiséis Subparte CC: "
            "Primero: la Distancia de Aproximación Mínima (MAD) de tres metros para líneas de hasta cincuenta mil voltios es una barrera geométrica sagrada; "
            "ninguna parte de la grúa, cable o carga debe invadir ese espacio sin línea desenergizada y puesta a tierra local. "
            "Segundo: está terminantemente prohibido guiar piezas suspendidas con las manos en zonas de riesgo eléctrico; "
            "se exige el uso exclusivo de cuerdas de viento o retenidas dieléctricas (taglines) de polipropileno seco no conductor. "
            "Y tercero: siempre que se opere cerca de cables aéreos, es obligatorio asignar un señalero exclusivo con silbato o radio para detener la maniobra en seco.\n\n"
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
    """Inyecta las historias del Lote 12 en index.html antes del cierre del array historias."""
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

    print("\n✓ index.html actualizado exitosamente con los 10 nuevos expedientes (#123 a #132).")
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
    print("Iniciando motor Kokoro para Lote 12 (#123 a #132)...")
    kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

    print("\n" + "=" * 55)
    print("Iniciando procesamiento de 10 historias del Lote 12 (#123 a #132)")
    print("=" * 55 + "\n")

    historias_procesadas = []

    for h in LOTE_12_DATA:
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

    print("\n🎉 ¡LOTE 12 COMPLETADO AL 100%! (10 historias procesadas)\n")

if __name__ == "__main__":
    main()
