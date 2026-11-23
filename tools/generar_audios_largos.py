# -*- coding: utf-8 -*-
"""
Generador de Audios Extendidos (4 a 5 minutos) y Guiones de Reels para Focus HSE
Rehace los audios de los Expedientes #013 a #022 para alcanzar la duración oficial de la app (4-5 min)
a velocidad 0.86 con Kokoro TTS, y guarda los guiones cortos como guion-reel.txt.
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

BASE_DIR = r"C:\D DCT\programas\hsefemeride"
ASSETS_DIR = os.path.join(BASE_DIR, "assets", "efemerides")
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
MODEL_PATH = r"C:\kokoro\kokoro-v1.0.onnx"
VOICES_PATH = r"C:\kokoro\voices-v1.0.bin"

KOKORO_SPEED = 0.86
KOKORO_VOICE = "em_alex"
KOKORO_LANG = "es"

AUDIOS_LARGOS_DATA = [
    {
        "id": "013",
        "carpeta": "1969-07-08-derrumbe-zanja-queens",
        "fecha": "8 de julio de 1969",
        "guionLargo": (
            "8 de julio de 1969. — En un sector en desarrollo del distrito de Queens, en Nueva York, "
            "una cuadrilla de operarios de saneamiento trabajaba en la instalación de un colector de aguas pluviales. — "
            "La zanja alcanzaba casi cuatro metros de profundidad... con paredes excavadas prácticamente a noventa grados, en un corte vertical seco y recto. — "
            "Durante las cuarenta y ocho horas previas al trabajo... una persistente tormenta de verano había empapado todo el condado. "
            "El suelo, compuesto por capas de arcilla y arena limosa, había absorbido miles de litros de agua. "
            "En la obra, sin embargo, el cronograma estaba retrasado. "
            "Para no perder días de trabajo ni incurrir en los costos de alquiler de cajones metálicos de apuntalamiento, "
            "la supervisión tomó la decisión de continuar la excavación sin instalar entibados de madera, sin bermas de descanso y sin talud de seguridad. — "
            "Muchos de los trabajadores llevaban años en el oficio y confiaban en la supuesta firmeza de la arcilla compacta. "
            "Pero el agua subterránea actúa en silencio. Al saturar los poros de la tierra, el agua destruye la cohesión entre las partículas "
            "y multiplica el peso del talud por metro cúbico. La zanja se había convertido en una trampa con toneladas de presión invisible a los costados. — "
            "A media tarde... cuatro operarios se encontraban en el fondo de la excavación acoplando una tubería de hormigón. "
            "No tenían escaleras de escape cerca; la única salida estaba a más de veinticinco metros de distancia. — "
            "De repente... sin un solo crujido de advertencia... una sección de doce metros de pared se fracturó desde la corona superior. "
            "En una fracción de segundo, más de treinta toneladas de tierra húmeda y barro colapsaron sobre el fondo de la zanja. — "
            "El impacto fue demoledor. La masa de arcilla sepultó a los cuatro trabajadores bajo más de dos metros de tierra compacta. — "
            "Desde la superficie, los compañeros corrieron desesperados con palas y comenzaron a cavar con las manos desnudas... "
            "pero el peso de la tierra húmeda no permite mover un músculo. "
            "Cada metro cúbico de suelo pesa casi dos mil kilos. La presión sobre la caja torácica de una persona sepultada impide que los pulmones se expandan, "
            "provocando la asfixia traumática en menos de tres minutos. — "
            "Cuando las unidades de rescate del departamento de bomberos lograron apuntalar los bordes para excavar de forma segura... ya era demasiado tarde. "
            "Los cuatro trabajadores habían perdido la vida en el fondo del pozo. — "
            "La investigación oficial de la época demostró que la empresa omitió todos los estándares básicos de ingeniería de suelos. "
            "El terreno nunca fue clasificado formalmente, nadie evaluó el impacto de las lluvias previas y no existía un plan de contingencia. — "
            "De esta tragedia y de cientos de eventos similares nacieron las regulaciones modernas de excavación que hoy salvan miles de vidas en todo el mundo. — "
            "Toda zanja con más de un metro con veinte de profundidad exige entibado de madera, blindaje metálico o un ángulo de talud seguro. "
            "Y antes de ingresar tras una lluvia... el terreno debe ser inspeccionado rigurosamente por personal calificado. — "
            "El suelo nunca avisa antes de caer. En excavaciones y zanjas... no existe el exceso de confianza. — "
            "La seguridad... está en los detalles."
        ),
        "promptFoto": (
            "High-resolution 1969 historical documentary photograph, 35mm lens, 16:9 landscape aspect ratio. "
            "A deep, dangerous civil construction trench in Queens, New York after heavy rain. Muddy vertical dirt walls "
            "nearly 4 meters deep without any wooden shoring or trench boxes. Heavy vintage yellow backhoe excavator parked near the edge. "
            "Atmospheric overcast sky, wet mud puddles, caution cones, authentic vintage work clothes, National Geographic archival style, no text."
        )
    },
    {
        "id": "014",
        "carpeta": "2015-07-09-fuga-amoniaco-frigorifico",
        "fecha": "9 de julio de 2015",
        "guionLargo": (
            "9 de julio de 2015. — En una importante planta frigorífica ubicada en la provincia de Santa Fe, Argentina... "
            "la jornada transcurría bajo un esquema de guardia técnica durante un día feriado. — "
            "En el corazón operativo de la fábrica se encuentra la sala de máquinas... un laberinto de tuberías, compresores y recipientes a presión "
            "que contienen miles de litros de amoníaco anhidro líquido para el sistema de refrigeración industrial. — "
            "El amoníaco es un refrigerante sumamente eficiente... pero al mismo tiempo es un gas extremadamente tóxico, corrosivo e inflamable en ciertas concentraciones. "
            "Al entrar en contacto con la humedad de los ojos, la garganta y los pulmones, reacciona químicamente formando hidróxido de amonio, "
            "un compuesto cáustico que destruye el tejido vivo en cuestión de segundos. — "
            "Esa madrugada... un equipo de técnicos debía intervenir una válvula de control de flujo que presentaba desgaste. — "
            "El procedimiento exigía aislar la sección mediante bloqueo mecánico y colocación de bridas ciegas, "
            "purgar todo el amoníaco remanente hacia el sistema de evacuación y verificar con detectores portátiles la ausencia total de presión y químico. — "
            "Sin embargo... para acortar los tiempos de parada... los operarios se limitaron a cerrar una válvula manual de paso. "
            "Confiaron en que la válvula retenía perfectamente el líquido... sin colocar candados de consignación y sin realizar una purga completa de la línea. — "
            "Con herramientas de mano... comenzaron a desajustar los pernos de la brida de la válvula. "
            "Al retirar el último perno... la junta de sellado cedió. "
            "Una bolsa de amoníaco líquido atrapada a alta presión se liberó violentamente hacia la atmósfera cerrada de la sala de máquinas. — "
            "Al entrar a la presión ambiental... el amoníaco líquido se evaporó de forma instantánea, multiplicando su volumen por casi mil veces. "
            "Una densa niebla blanca y asfixiante cubrió la sala en segundos... con concentraciones que superaron ampliamente las trescientas partes por millón. — "
            "Los dos operarios intentaron escapar a ciegas... pero la nube cáustica les quemó de inmediato las córneas y les provocó espasmos respiratorios incontrolables. "
            "Para empeorar la situación... los detectores fijos de amoníaco de la sala se encontraban fuera de servicio por mantenimiento diferido, "
            "por lo que los extractores de emergencia no se activaron automáticamente. — "
            "Los operarios lograron salir arrastrándose al exterior gracias al auxilio desesperado de sus compañeros... pero sufrieron quemaduras pulmonares de gravedad. "
            "La fuga obligó a los bomberos zapadores y a la policía a evacuar a más de trescientas personas de los barrios linderos a la planta "
            "mientras brigadistas con trajes encapsulados y equipos autónomos ingresaban a cortar las líneas maestras. — "
            "La investigación posterior determinó que se violaron los protocolos más elementales de bloqueo, etiquetado y energía cero. "
            "En circuitos de amoníaco... nunca se debe abrir una tubería sin antes purgar, despresurizar, cegar físicamente y portar equipo de respiración autónoma. — "
            "El gas invisible no perdona atajos operativos. — "
            "La seguridad... está en los detalles."
        ),
        "promptFoto": (
            "Cinematic documentary photograph, 35mm lens, 16:9 landscape aspect ratio. Interior of an industrial ammonia refrigeration engine room. "
            "Large industrial steel compressors, insulated turquoise pipes with pressure gauges, warning hazard placards for anhydrous ammonia NH3. "
            "Atmospheric dim industrial lighting, subtle chemical haze in the air, wet concrete floors, photorealistic National Geographic quality, no text."
        )
    },
    {
        "id": "015",
        "carpeta": "1976-07-10-desastre-seveso",
        "fecha": "10 de julio de 1976",
        "guionLargo": (
            "10 de julio de 1976. — Al norte de Milán, en la región italiana de Lombardía... la fábrica química ICMESA "
            "operaba entre los tranquilos municipios de Meda y Seveso. — "
            "En el edificio B de la planta... el reactor químico B-101 se utilizaba para sintetizar triclorofenol... "
            "una sustancia base empleada en la fabricación de desinfectantes y herbicidas. — "
            "La reacción química requería calentar una mezcla reactiva con vapor de agua a más de ciento cincuenta grados centígrados, "
            "manteniendo una agitación mecánica continua para disipar el calor generado por el proceso. — "
            "Ese sábado al mediodía... la jornada laboral estaba por concluir para dar inicio al descanso del fin de semana. "
            "El operador a cargo suspendió la agitación mecánica y apagó el suministro de vapor principal... "
            "pero el reactor aún contenía la carga química completa sin enfriar. — "
            "Nadie advirtió una trampa termodinámica mortal: la turbina de vapor del sistema eléctrico había sido apagada minutos antes, "
            "lo que provocó que el vapor residual en la camisa del reactor alcanzara una temperatura anormalmente alta, cercana a los trescientos grados. — "
            "Sin agitación que distribuyera la temperatura... el calor comenzó a transferirse lentamente desde las paredes metálicas hacia la masa química inmóvil. "
            "A partir de los ciento ochenta grados... comenzó una reacción química secundaria no deseada: una reacción exotérmica descontrolada. — "
            "Durante más de seis horas en la soledad del fin de semana... la temperatura y la presión dentro del reactor aumentaron exponencialmente. "
            "A las doce y treinta y siete del mediodía... la presión interna superó las cuatro atmósferas y reventó el disco de ruptura de seguridad. — "
            "La tubería de alivio del disco apuntaba directamente al exterior del techo del edificio... sin ningún tanque de contención, "
            "sin filtros de carbón activado y sin sistema lavador de gases. — "
            "Una densa nube blanca en forma de aerosol químico fue expulsada con violencia hacia la atmósfera... elevándose a más de cincuenta metros de altura. — "
            "El viento cálido de verano empujó la nube hacia el sur... precipitándola directamente sobre el poblado de Seveso y localidades vecinas. — "
            "Entre las seis toneladas de químicos liberados... viajaban entre uno y dos kilogramos de dioxina TCDD... "
            "uno de los venenos más potentes, persistentes y cancerígenos jamás fabricados por el ser humano. — "
            "En las horas siguientes... las hojas de los árboles se tornaron marrones, miles de pájaros y conejos murieron en los jardines, "
            "y cientos de niños comenzaron a desarrollar hinchazones y deformaciones cutáneas severas conocidas como cloracné. — "
            "La empresa ocultó la presencia de dioxina durante más de diez días... retrasando la evacuación y agravando la exposición de miles de familias. "
            "Más de ochenta mil animales tuvieron que ser sacrificados y el suelo de cientos de hectáreas debió ser retirado por completo en barriles sellados. — "
            "El desastre de Seveso conmocionó al mundo y obligó a la Comunidad Europea a redactar la Directiva Seveso... "
            "la normativa pionera que hoy exige que toda industria química identifique sus riesgos mayores, mantenga defensas independientes "
            "y coordine planes de emergencia abiertos con la sociedad. — "
            "Los reactores químicos no descansan los fines de semana. En seguridad de procesos... el control del calor residual es una cuestión de supervivencia. — "
            "La seguridad... está en los detalles."
        ),
        "promptFoto": (
            "Historical wide documentary photograph, 35mm lens, 16:9 aspect ratio. The ICMESA chemical plant in Meda/Seveso Italy, July 1976. "
            "Brick industrial synthesis buildings, metal reactor distillation columns, pipes, surrounding rural trees showing subtle chemical wilting. "
            "A bright hazy summer sky, vintage 1970s Italian industrial setting, somber and investigative atmosphere, photorealistic, no text."
        )
    },
    {
        "id": "016",
        "carpeta": "2013-07-11-atrapamiento-silo-granos",
        "fecha": "11 de julio de 2013",
        "guionLargo": (
            "11 de julio de 2013. — En una planta de acopio y acondicionamiento de granos de la pampa húmeda argentina... "
            "la actividad de carga de camiones operaba a pleno ritmo durante la temporada de cosecha. — "
            "En el patio de almacenamiento se alzaban enormes silos verticales de chapa galvanizada... de más de veinte metros de altura, "
            "con capacidad para almacenar miles de toneladas de cereal a granel. — "
            "Esa mañana... el flujo de soja que caía hacia la tolva inferior de descarga comenzó a disminuir hasta detenerse por completo. "
            "Debido a la humedad ambiente de los días anteriores... una capa de cereal se había apelmazado y compactado en las paredes del silo, "
            "formando un bloqueo mecánico en el interior. — "
            "Un operario de planta subió por la escalerilla exterior hasta la cúpula del silo para destrabar el grano. "
            "Llevaba consigo una barra de hierro para golpear las costras de cereal... pero no portaba arnés de seguridad con cabo de vida conectado, "
            "ni solicitó un permiso de trabajo en espacios confinados. — "
            "Para acelerar la tarea... los transportadores de descarga de la base del silo se mantuvieron encendidos y funcionando. — "
            "El operario ingresó por la escotilla superior y comenzó a caminar sobre la superficie aparentemente sólida de la soja. "
            "Lo que no podía ver desde arriba... era el fenómeno más peligroso en el almacenamiento de granos: el llamado efecto puente. — "
            "Debajo de la capa superficial apelmazada... la descarga inferior había succionado el cereal, dejando una inmensa caverna hueca de varios metros de vacío. "
            "La costra sobre la que caminaba el trabajador tenía apenas unos centímetros de espesor. — "
            "Al clavar la barra metálica... la estructura de grano colapsó súbitamente bajo sus pies. — "
            "El cereal a granel se comporta físicamente exactamente igual que las arenas movedizas. "
            "En menos de tres segundos... el operario se hundió hasta la cintura. En cinco segundos... el grano lo cubrió hasta el pecho. — "
            "El trabajador intentó luchar con desesperación... pero cada movimiento hacía que el cereal fino fluyera hacia abajo, atrapándolo aún más. "
            "Para sacar a una persona enterrada hasta la cintura en grano se necesita una fuerza de tracción de casi doscientos kilos... "
            "y cuando el grano cubre el pecho, la fuerza requerida supera los cuatrocientos kilos, lo suficiente como para fracturar la columna. — "
            "Desde la escotilla... un compañero intentó arrojarle una cuerda común... pero en segundos el cono de succión se cerró por completo sobre la cabeza del operario. "
            "El cereal ejerce una presión aplastante sobre el tórax que impide que los pulmones inhalen aire, provocando la asfixia mecánica en minutos. — "
            "A pesar del trabajo de los bomberos voluntarios, que tuvieron que cortar las chapas inferiores del silo para vaciar el cereal... el rescate fue en vano. — "
            "Esta tragedia recuerda la regla de oro en el sector agroindustrial: nunca se debe ingresar a un silo con las descargas en marcha, "
            "y jamás se debe pisar el grano sin arnés de rescate, línea de vida tensada y un vigía equipado con trípode de izaje en la boca de acceso. — "
            "El grano no es piso firme. — "
            "La seguridad... está en los detalles."
        ),
        "promptFoto": (
            "Documentary agricultural industrial photography, 35mm lens, 16:9 landscape aspect ratio. Inside an enormous steel grain storage silo. "
            "Vast golden hills of bulk soybeans under dim dust-filled sunlight streaming through the roof hatch. "
            "Industrial steel access ladders, grain auger chute at the bottom, atmospheric dust particles floating in the air, solemn photorealistic style, no text."
        )
    },
    {
        "id": "017",
        "carpeta": "2018-07-12-prensa-hidraulica-loto",
        "fecha": "12 de julio de 2018",
        "guionLargo": (
            "12 de julio de 2018. — En una moderna planta de componentes metalmecánicos y autopartes... "
            "la línea de producción de chasis operaba a su máxima capacidad diaria. — "
            "En el centro de la celda de trabajo se encontraba una colosal prensa hidráulica de cuatrocientas toneladas... "
            "capaz de moldear gruesas láminas de acero en ciclos repetitivos de menos de diez segundos. — "
            "La máquina contaba con avanzados dispositivos de protección operativa... incluyendo cortinas ópticas de seguridad infrarrojas "
            "que detenían el ciclo si un objeto o persona cruzaba el haz de luz durante el trabajo normal. — "
            "Hacia el mediodía... el operador detectó que virutas y rebabas de metal se estaban acumulando en la matriz inferior, "
            "lo que amenazaba con rayar las piezas y detener la producción. — "
            "El procedimiento formal de la empresa exigía aplicar el protocolo LOTO: cortar el interruptor eléctrico principal, "
            "colocar un candado con tarjeta de consignación, despresurizar los acumuladores hidráulicos "
            "y colocar físicamente un calzo mecánico de acero macizo entre la bancada y el ariete superior. — "
            "Sin embargo... el operario consideró que realizar todo ese procedimiento le llevaría más de quince minutos... "
            "mientras que retirar la viruta le tomaría apenas veinte segundos. — "
            "Confiando en que la cortina de luz protegería su vida... el trabajador no apagó la máquina ni bloqueó la energía hidráulica. "
            "Introdujo el torso y los brazos directamente en el espacio entre ambas matrices. — "
            "Pero los dispositivos electrónicos y ópticos están diseñados para el ciclo de operación... no son barreras de aislamiento de energía para mantenimiento. — "
            "En ese preciso instante... una electroválvula del circuito servohidráulico sufrió un cortocircuito interno por vibración. "
            "La válvula conmutó inesperadamente... y el circuito hidráulico liberó cientos de bares de presión acumulada sobre el cilindro maestro. — "
            "A pesar de que el haz infrarrojo estaba interrumpido... el fallo en el tablero puenteó la señal de control. "
            "El pesado ariete de varias toneladas descendió a plena carrera con una violencia inaudita. — "
            "El operario fue atrapado al instante en la zona de la matriz... falleciendo en el acto por aplastamiento masivo sin posibilidad de reacción. — "
            "La investigación posterior de los inspectores de trabajo fue concluyente: ningún sensor, barrera óptica o paro de emergencia electrónico "
            "sustituye el corte físico de la energía principal y la colocación de trabas mecánicas. — "
            "La gravedad y la presión hidráulica no negocian. Si tu cuerpo va a ingresar en una zona de peligro... la energía debe ser absolutamente cero. — "
            "La seguridad... está en los detalles."
        ),
        "promptFoto": (
            "Industrial documentary photography, 35mm lens, 16:9 landscape aspect ratio. A heavy 400-ton industrial hydraulic metal stamping press. "
            "Massive steel ram, lower stamping die with oily metal shavings, yellow safety guardrails, warning danger signs. "
            "Overhead industrial factory lighting, reflections on polished steel and oily concrete, gritty realistic documentary look, no text."
        )
    },
    {
        "id": "018",
        "carpeta": "2012-07-13-caida-altura-estructura-metalica",
        "fecha": "13 de julio de 2012",
        "guionLargo": (
            "13 de julio de 2012. — En el predio de un nuevo parque logístico e industrial... "
            "cuadrillas de montadores de estructuras metálicas avanzaban a paso firme en la colocación de la cubierta de una nave de gran escala. — "
            "A más de once metros sobre el suelo de hormigón... los trabajadores caminaban sobre perfiles y correas de acero de apenas quince centímetros de ancho. — "
            "Hacer montaje en altura es una de las tareas más exigentes de la construcción. Exige destreza física, equilibrio constante "
            "y un respeto absoluto por los protocolos de protección contra caídas. — "
            "Esa mañana... el viento soplaba con ráfagas cambiantes y una llovizna temprana había dejado una fina película de humedad sobre la pintura epóxica de las vigas. — "
            "Uno de los montadores más capacitados del equipo se desplazaba sobre las correas superiores. "
            "Portaba su arnés de seguridad de cuerpo entero... pero su equipo estaba conectado a un cabo de amarre simple... con un solo mosquetón de seguridad. — "
            "Al llegar a la unión con la viga reticulada principal... el trabajador necesitaba pasar su anclaje al siguiente tramo de estructura. "
            "Para hacerlo con un cabo simple... debía desengancharse primero... dar un paso sobre la viga húmeda... y volver a engancharse en el nuevo punto. — "
            "Fueron escasos segundos. Dos segundos en los que el operario quedó completamente desprotegido a once metros del piso. — "
            "En ese instante... una ráfaga de viento repentina lo desestabilizó. Al intentar apoyar el pie... la suela de su bota resbaló sobre el metal mojado. "
            "El montador intentó aferrarse a la estructura con las manos... pero no encontró punto de apoyo y cayó al vacío. — "
            "Sin una línea de vida tensada a la que estuviera conectado... y sin redes de seguridad perimetrales instaladas debajo de la zona de trabajo... "
            "no hubo nada que detuviera la caída. — "
            "El impacto contra la losa de hormigón fue instantáneo y fatal. — "
            "La investigación demostró una falla sistémica en la cultura preventiva de la obra. "
            "Llevar puesto el arnés no sirve de nada si el trabajador queda desconectado durante los desplazamientos. "
            "En trabajos en altura... la norma internacional exige el uso obligatorio de cabos de vida dobles en Y... "
            "donde un gancho permanece firmemente anclado mientras el segundo se posiciona en el próximo punto, "
            "garantizando el principio de cien por ciento conectado en todo momento. — "
            "Y siempre que sea técnicamente viable... el montaje debe realizarse utilizando plataformas elevadoras móviles de personal "
            "para evitar que los trabajadores caminen sobre vigas descubiertas. — "
            "Un segundo desconectado es la diferencia entre regresar a casa con tu familia o no volver jamás. — "
            "La seguridad... está en los detalles."
        ),
        "promptFoto": (
            "Cinematic documentary photography, wide angle 28mm lens, 16:9 landscape aspect ratio. High-altitude steel beam construction of an industrial warehouse roof. "
            "Structural steel I-beams against an overcast, windy morning sky 11 meters high. Concrete floor far below, safety harnesses, cables, wet steel reflections. "
            "National Geographic authentic construction journalism style, photorealistic, solemn and respectful, no text."
        )
    },
    {
        "id": "019",
        "carpeta": "2019-07-14-intoxicacion-camara-septica",
        "fecha": "14 de julio de 2019",
        "guionLargo": (
            "14 de julio de 2019. — En una estación de bombeo de efluentes cloacales y cámara séptica... "
            "una cuadrilla de saneamiento municipal se preparaba para realizar el mantenimiento rutinario de una bomba sumergible atascada. — "
            "La cámara subterránea tenía más de cinco metros de profundidad... con acceso a través de una boca de registro circular en la superficie. — "
            "En las redes de saneamiento y tratamiento de aguas servidas... la descomposición anaeróbica de la materia orgánica genera de forma continua "
            "grandes concentraciones de sulfuro de hidrógeno... un gas altamente tóxico, conocido comúnmente como gas de alcantarilla o H2S. — "
            "El sulfuro de hidrógeno tiene una característica sumamente traicionera: a bajas concentraciones tiene un fuerte olor a huevos podridos... "
            "pero cuando la concentración supera las cien partes por millón... paraliza instantáneamente el nervio olfativo. "
            "La persona deja de olerlo y cree falsamente que el gas se ha disipado... cuando en realidad se encuentra en una atmósfera letal. — "
            "Esa mañana... los trabajadores retiraron la tapa de fundición de la cámara. "
            "Confiados en que la tarea tomaría apenas un par de minutos... no encendieron el detector portátil de cuatro gases "
            "ni instalaron el extractor de ventilación mecánica forzada para renovar el aire del fondo. — "
            "El primer operario comenzó a descender por los peldaños metálicos de la pared. "
            "Al llegar a la mitad de la cámara... entró en una bolsa concentrada de sulfuro de hidrógeno que había desplazado al oxígeno. "
            "En una sola inhalación... el gas le provocó el colapso respiratorio inmediato. El trabajador perdió el conocimiento y cayó desplomado al fondo. — "
            "En la superficie... sus dos compañeros escucharon el golpe y vieron a su amigo inmóvil en el agua servida. — "
            "Aquí se activó el mecanismo más desgarrador de los accidentes en espacios confinados: el llamado efecto cascada o rescate improvisado por instinto. — "
            "El segundo operario... impulsado por el amor a su compañero y la desesperación... se arrojó de inmediato al pozo sin equipo de respiración autónoma. "
            "A los cuatro peldaños... inhaló la misma nube letal y cayó desvanecido sobre su compañero. — "
            "El tercer trabajador... presa del pánico total... cometió exactamente el mismo error. Descendió al rescate y colapsó en segundos. — "
            "Tres vidas se perdieron en menos de tres minutos. — "
            "Las estadísticas de los organismos internacionales como OSHA y NIOSH demuestran una realidad brutal: "
            "más del sesenta por ciento de las personas que mueren en espacios confinados son compañeros que intentaron realizar un rescate heroico pero desprotegido. — "
            "En atmósferas peligrosas... el valor sin equipo no salva vidas: solo multiplica las tumbas. "
            "La regla es inviolable: medir cuatro gases en todo momento, ventilar de forma continua y jamás ingresar a rescatar sin equipo de respiración autónoma. — "
            "La seguridad... está en los detalles."
        ),
        "promptFoto": (
            "Documentary photography, 35mm lens, 16:9 landscape aspect ratio. A deep concrete underground sewage pumping chamber and manhole on an overcast day. "
            "Iron access rungs leading down into darkness, yellow safety tripod with winch at the surface, four-gas multi-detector device on a tripod, "
            "warning sign for confined space and toxic gas H2S. Dramatic industrial lighting, realistic textures, National Geographic investigative style, no text."
        )
    },
    {
        "id": "020",
        "carpeta": "1973-07-15-explosion-refineria-chiba",
        "fecha": "15 de julio de 1973",
        "guionLargo": (
            "15 de julio de 1973. — En la costa este de la bahía de Tokio... la refinería de petróleo de Chiba "
            "constituía uno de los complejos petroquímicos más grandes y modernos de Japón. — "
            "En la unidad de craqueo térmico... una imponente columna de fraccionamiento de hidrocarburos operaba de forma continua, "
            "separando corrientes de naftas, gases licuados y destilados bajo altas presiones y temperaturas superiores a los trescientos grados. — "
            "Para proteger la columna contra una sobrepresión catastrófica... la cima de la torre contaba con válvulas de seguridad y alivio de presión automáticas... "
            "diseñadas para disparar de inmediato si la presión interna superaba el límite de diseño. — "
            "Días antes del accidente... una de las válvulas de alivio principales presentó una pequeña fuga en su asiento. "
            "Para permitir que los técnicos revisaran el mecanismo sin detener la planta... se cerró una válvula de bloqueo manual instalada aguas abajo de la válvula de seguridad. — "
            "La reparación concluyó satisfactoriamente... pero ocurrió una omisión que resultaría fatal: "
            "el personal olvidó volver a abrir la válvula de bloqueo manual... y nadie colocó el precinto de control que certificaba su posición abierta. — "
            "Durante el turno tarde del 15 de julio... se produjo una perturbación en el sistema de agua de enfriamiento del condensador superior. "
            "Al disminuir la condensación... los vapores de hidrocarburos ligeros comenzaron a acumularse rápidamente en la parte superior de la columna, "
            "haciendo que la presión interna se disparara a niveles críticos. — "
            "Cuando la presión superó los veinticinco kilogramos por centímetro cuadrado... la válvula de seguridad se abrió mecánicamente como estaba previsto... "
            "pero el camino hacia la antorcha de alivio estaba completamente cerrado por la válvula de bloqueo olvidada. — "
            "La columna de destilación... sin ninguna vía de escape para aliviar los gases presurizados... se convirtió en una gigantesca bomba de acero. — "
            "La estructura no soportó la sobrepresión. La cúpula superior de la torre se desgarró con un estruendo ensordecedor. — "
            "Cientos de toneladas de hidrocarburos calientes se liberaron instantáneamente a la atmósfera... formando una nube de vapor que encontró ignición inmediata "
            "en los hornos de proceso cercanos. — "
            "La explosión sacudió la bahía de Tokio a kilómetros de distancia. Una bola de fuego colosal envolvió la unidad de craqueo... "
            "desatando incendios que ardieron durante más de cuatro días y cobraron la vida de múltiples operadores y brigadistas. — "
            "La tragedia de Chiba transformó para siempre los estándares mundiales de seguridad de procesos. "
            "A partir de este evento... la industria petrolera estableció la regla universal del car seal open: "
            "toda válvula de bloqueo ubicada antes o después de una válvula de seguridad debe estar permanentemente abierta, "
            "bloqueada con candado y precinto numerado... y auditada diariamente antes de cualquier arranque. — "
            "Una válvula de alivio bloqueada es una sentencia de muerte. — "
            "La seguridad... está en los detalles."
        ),
        "promptFoto": (
            "Historical documentary photography, 35mm lens, 16:9 landscape aspect ratio. An oil refinery distillation fractionating tower at dusk in Chiba Japan, 1973. "
            "Complex web of industrial piping, pressure relief valves PSV, steel catwalks, distillation columns with warning tags. "
            "Moody coastal twilight sky, warm sodium vapor industrial floodlights reflecting on steel pipes, authentic historical Japanese refinery setting, no text."
        )
    },
    {
        "id": "021",
        "carpeta": "2016-07-16-electrocucion-grua-pluma",
        "fecha": "16 de julio de 2016",
        "guionLargo": (
            "16 de julio de 2016. — En una obra de ampliación y repavimentación vial junto a una autopista interurbana... "
            "una cuadrilla de operarios realizaba tareas de descarga de pesadas tuberías de hormigón armado para desagües pluviales. — "
            "Para mover las piezas de más de dos toneladas cada una... la empresa utilizaba un camión con hidrogrúa articulada. — "
            "Paralela a la banquina donde operaba el camión... corría una línea aérea de distribución eléctrica de media tensión... "
            "con cables desnudos de treinta y tres mil voltios suspendidos sobre postes de hormigón a unos ocho metros de altura. — "
            "En el sector eléctrico existe un mito sumamente extendido y letal: muchas personas creen que para recibir una descarga eléctrica "
            "es obligatorio tocar físicamente el cable con la máquina o el cuerpo. — "
            "Esto es falso. La electricidad de media y alta tensión tiene la capacidad física de romper la resistencia dieléctrica del aire "
            "y generar un arco eléctrico violento a distancia... sin necesidad de contacto directo. — "
            "Esa mañana... el operador del camión grúa comenzó a maniobrar la pluma telescópica para izar una tubería desde la caja del camión hacia la banquina. "
            "La cuadrilla no había designado a un señalero o rigger exclusivo para vigilar la proximidad con la línea eléctrica... "
            "y no se habían colocado barreras físicas ni balizas de advertencia en el suelo. — "
            "Mientras el operador extendía el brazo hidráulico... la punta metálica de la pluma se aproximó a la línea aérea. "
            "Aunque la pluma nunca tocó el cable... llegó a ubicarse a menos de setenta centímetros de distancia del conductor de treinta y tres kilovoltios. — "
            "En una fracción de segundo... el aire se ionizó. "
            "Un ensordecedor arco eléctrico de miles de grados de temperatura saltó desde la línea aérea hacia la punta de la grúa. — "
            "La corriente eléctrica de miles de amperios viajó velozmente a través de la estructura de acero del camión buscando una vía de descarga hacia la tierra. — "
            "En el suelo... un joven ayudante de apenas veintidós años sostenía la tubería de hormigón con sus guantes de cuero para guiarla hacia la zanja. — "
            "La corriente encontró en el cuerpo del trabajador el camino más rápido hacia el suelo. "
            "La descarga eléctrica masiva atravesó sus órganos vitales, provocando un paro cardíaco instantáneo y quemaduras térmicas de extrema gravedad. — "
            "El ayudante falleció en el acto sobre la banquina. — "
            "La investigación posterior de las autoridades laborales remarcó las normas que jamás debieron ignorarse: "
            "ante la presencia de líneas eléctricas aéreas... se debe respetar rigurosamente una distancia mínima de seguridad de al menos tres a cinco metros, "
            "se debe contar siempre con un señalero dedicado con silbato... y las cargas suspendidas deben guiarse exclusivamente mediante vientos de fibra no conductora, "
            "jamás tocándolas directamente con las manos. — "
            "La electricidad mata a distancia. En cercanías de líneas vivas... la distancia de seguridad no se negocia. — "
            "La seguridad... está en los detalles."
        ),
        "promptFoto": (
            "Cinematic documentary photography, 35mm lens, 16:9 landscape aspect ratio. A heavy truck with an articulated hydraulic crane boom parked along a road construction site. "
            "Overhead, electrical distribution utility poles and 33kV power lines run parallel against an overcast morning sky. "
            "Heavy concrete drainage pipes on the gravel road shoulder, safety cones, danger electrical hazard signs, hyper-realistic documentary quality, no text."
        )
    },
    {
        "id": "022",
        "carpeta": "1981-07-17-colapso-hyatt-regency",
        "fecha": "17 de julio de 1981",
        "guionLargo": (
            "17 de julio de 1981. — En la ciudad de Kansas City, Estados Unidos... el moderno y lujoso Hotel Hyatt Regency "
            "celebraba un animado concurso de baile en su espectacular atrio central de cuatro pisos de altura. — "
            "Más de mil quinientas personas colmaban el lobby... bailando y disfrutando de la música de una orquesta en vivo. — "
            "La joya arquitectónica del edificio eran tres impresionantes pasarelas peatonales suspendidas en el aire... "
            "estructuras de acero y hormigón de más de treinta y seis metros de largo que cruzaban el atrio a gran altura, "
            "permitiendo a los huéspedes contemplar la fiesta desde los pisos segundo, tercero y cuarto. — "
            "Decenas de parejas se congregaron sobre las pasarelas para ver el espectáculo desde las alturas... "
            "sin sospechar jamás que sobre sus cabezas pendía un defecto de ingeniería estructural catastrófico. — "
            "Durante la etapa de construcción, un año antes... el diseño original de la firma de cálculo estructural "
            "especificaba que las pasarelas del cuarto y segundo piso debían colgar de un único conjunto continuo de varillas de acero roscadas, "
            "las cuales bajaban directamente desde las cerchas del techo atravesando ambas pasarelas. — "
            "Sin embargo... la empresa fabricante de las estructuras de acero consideró que fabricar y roscar varillas continuas de doce metros era demasiado difícil y costoso. — "
            "Por su cuenta... el taller propuso un cambio que parecía insignificante: dividir las varillas en dos tramos escalonados. "
            "El primer juego de varillas sostendría la pasarela del cuarto piso desde el techo... "
            "y un segundo juego de varillas colgaría la pasarela del segundo piso directamente de las vigas de la pasarela superior. — "
            "Nadie en el equipo de ingeniería recalculó las cargas. "
            "Ese cambio aparentemente menor duplicó la tensión cortante sobre las vigas cajón de la pasarela del cuarto piso. "
            "La viga superior ahora tenía que soportar no solo su propio peso y su gente... sino también todo el peso de la pasarela inferior suspendida de ella. — "
            "El cambio se aprobó de forma informal mediante bocetos telefónicos... sin una memoria de cálculo formal y sin la firma de los ingenieros responsables. — "
            "A las siete y cinco de la tarde del 17 de julio... bajo el peso de las personas que bailaban y se balanceaban al compás de la música... "
            "las tuercas de anclaje de la pasarela del cuarto piso colapsaron. "
            "Las vigas de acero se desgarraron en los puntos de unión... y la pasarela del cuarto piso se precipitó en caída libre sobre la pasarela del segundo piso, "
            "arrastrando ambas estructuras hacia el fondo del atrio sobre cientos de personas que se encontraban en la pista de baile. — "
            "El colapso dejó ciento catorce personas fallecidas y más de doscientas heridas de gravedad... "
            "convirtiéndose en el colapso estructural no sísmico más mortífero en la historia de los Estados Unidos. — "
            "La investigación federal del National Bureau of Standards determinó que la estructura colapsada apenas resistía el sesenta por ciento de la carga mínima requerida por el código. "
            "Los ingenieros responsables perdieron sus licencias profesionales y el caso dio origen al concepto moderno de Gestión del Cambio (MOC)... "
            "el cual establece que cualquier modificación en obra, por pequeña que parezca, debe ser formalmente recalculada y aprobada por escrito. — "
            "En ingeniería y construcción... un atajo no calculado cuesta vidas. — "
            "La seguridad... está en los detalles."
        ),
        "promptFoto": (
            "Historical architecture photography, 35mm lens, 16:9 landscape aspect ratio. The dramatic multi-story atrium lobby of the Hyatt Regency Hotel Kansas City, 1981. "
            "Vast modern concrete and glass hotel interior, elevated suspended pedestrian skywalks hanging from steel rods crossing the atrium. "
            "Warm interior hotel lighting, indoor greenery, 1980s architectural photography style, somber historical retrospective feel, photorealistic, no text."
        )
    }
]

def procesar_audio_largo(historia, kokoro_instance):
    """Genera el audio largo de 4-5 minutos, guarda el guion reel y el prompt de foto."""
    carpeta_nombre = historia["carpeta"]
    target_dir = os.path.join(ASSETS_DIR, carpeta_nombre)
    os.makedirs(target_dir, exist_ok=True)

    print(f"\n=======================================================")
    print(f"▶ Generando Audio Extendido: {historia['id']} ({historia['fecha']})")
    print(f"=======================================================")

    # 1. Guardar prompt para portada manual
    with open(os.path.join(target_dir, "prompt-portada.txt"), "w", encoding="utf-8") as f:
        f.write(historia["promptFoto"])

    # 2. Generar audio con Kokoro a 0.86
    wav_path = os.path.join(target_dir, "historia.wav")
    m4a_path = os.path.join(target_dir, "historia.m4a")

    palabras = len(historia["guionLargo"].split())
    print(f"  🎙️ Sintetizando audio ({palabras} palabras) con Kokoro (speed={KOKORO_SPEED})...")

    samples, sample_rate = kokoro_instance.create(
        historia["guionLargo"],
        voice=KOKORO_VOICE,
        speed=KOKORO_SPEED,
        lang=KOKORO_LANG
    )
    sf.write(wav_path, samples, sample_rate)

    # 3. Convertir a M4A con ffmpeg
    print("  ⚙️ Convirtiendo a M4A optimizado...")
    cmd_ffmpeg = [
        "ffmpeg", "-i", wav_path,
        "-c:a", "aac", "-b:a", "192k",
        "-y", m4a_path
    ]
    subprocess.run(cmd_ffmpeg, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    if os.path.exists(wav_path):
        os.remove(wav_path)

    # 4. Calcular duración real
    duracion_seg = len(samples) / float(sample_rate)
    minutos = int(duracion_seg // 60)
    segundos = int(duracion_seg % 60)
    texto_duracion = f"Audio de {minutos} minutos {segundos:02d} segundos"
    historia["duracionAudio"] = texto_duracion
    print(f"  ✓ Audio final listo: {m4a_path} ({texto_duracion})")

    # 5. Actualizar contenido-completo.md con la narración extendida
    md_path = os.path.join(target_dir, "contenido-completo.md")
    if os.path.exists(md_path):
        with open(md_path, "r", encoding="utf-8") as f:
            md_text = f.read()
        
        # Reemplazar la seccion En cuestion de minutos
        marcador_inicio = "# ⏱️ En cuestión de minutos...\n\n"
        marcador_fin = "\n\n---\n\n# 🦺 Tres puntos clave"
        pos1 = md_text.find(marcador_inicio)
        pos2 = md_text.find(marcador_fin)
        if pos1 != -1 and pos2 != -1:
            nueva_seccion = marcador_inicio + historia["guionLargo"].replace(" — ", "\n\n").replace("... ", "...\n\n")
            md_text = md_text[:pos1] + nueva_seccion + md_text[pos2:]
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(md_text)
            print("  ✓ contenido-completo.md actualizado con la crónica completa")

    return historia

def actualizar_duraciones_en_index(historias_procesadas):
    """Actualiza duracionAudio de cada historia en index.html."""
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    for h in historias_procesadas:
        id_str = f'id: "{h["id"]}",'
        pos_id = content.find(id_str)
        if pos_id != -1:
            pos_dur = content.find('duracionAudio: "', pos_id)
            if pos_dur != -1:
                pos_fin = content.find('",', pos_dur)
                dur_vieja = content[pos_dur:pos_fin+2]
                dur_nueva = f'duracionAudio: "{h["duracionAudio"]}",'
                content = content[:pos_dur] + dur_nueva + content[pos_fin+2:]
                print(f"  ✓ index.html actualizado para #{h['id']} -> {h['duracionAudio']}")

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    print("Iniciando motor Kokoro para regeneración de audios extendidos (4-5 minutos)...")
    kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

    procesadas = []
    for h in AUDIOS_LARGOS_DATA:
        try:
            h_proc = procesar_audio_largo(h, kokoro)
            procesadas.append(h_proc)
        except Exception as e:
            print(f"Error procesando {h['id']}: {e}", file=sys.stderr)

    actualizar_duraciones_en_index(procesadas)
    print("\n🎉 ¡TODOS LOS AUDIOS EXTENDIDOS GENERADOS Y ACTUALIZADOS!")

if __name__ == "__main__":
    main()
