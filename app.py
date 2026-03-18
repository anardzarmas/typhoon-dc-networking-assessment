import streamlit as st
from fpdf import FPDF
from datetime import date

# Configuración de la página
st.set_page_config(page_title="Datacenter Networking Assessment", layout="wide")

st.title("Formulario de Evaluación: Datacenter Networking para AI")
st.subheader("Partner de Cisco: Typhoon Technology")
st.write("Complete este cuestionario para descubrir la arquitectura de Data Center recomendada para cargas de trabajo de Inteligencia Artificial (AI).")

# --- SECCIÓN 1: Información General del Proyecto ---
st.header("1. Información General del Proyecto")
col1, col2 = st.columns(2)

with col1:
    empresa = st.text_input("Nombre de la empresa")
    contacto = st.text_input("Contacto principal")
    correo = st.text_input("Correo electrónico")
    puesto = st.text_input("Puesto")

with col2:
    am_cisco = st.text_input("AM de Cisco")
    resp_best = st.text_input("Responsable de Preventa")
    fecha = st.date_input("Fecha de evaluación", date.today())
    vertical = st.selectbox("Vertical de negocio", 
                            ["Finanzas", "Salud", "Retail", "Manufactura", "Educación", "Gobierno", "Tecnología", "Otro"])

# --- SECCIÓN 2: Dominios de Evaluación ---
st.header("2. Dominios de Evaluación de Red para AI")
st.write("Expanda cada sección para evaluar las prácticas actuales.")

respuestas = {}
notas = {}
abiertas = {}

# Section A: Network Architecture & Design
with st.expander("A. Arquitectura y Diseño de Red"):
    respuestas['arch_support'] = st.selectbox(
        "Soporte de la arquitectura actual para demandas de IA (alto rendimiento, baja latencia):", 
        ["Seleccione", 
         "Optimizado: Soporta tráfico sin pérdida (Spine-Leaf, RoCE v2, PFC, ECN).", 
         "Suficiente: Arquitectura moderna pero carece de ajustes específicos para IA.", 
         "Necesita Mejora: Arquitectura tradicional de 3 capas con cuellos de botella.", 
         "No Preparado: Requiere un rediseño completo."]
    )
    respuestas['arch_reference'] = st.selectbox(
        "Importancia de una arquitectura de referencia prevalidada (ej. NVIDIA ERA):", 
        ["Seleccione", 
         "Esencial: Priorizamos diseños probados para reducir riesgos.", 
         "Importante: Consideramos referencias pero personalizamos.", 
         "Opcional: Preferimos diseñar desde cero por flexibilidad.", 
         "No es un factor determinante."]
    )
    respuestas['arch_lossless'] = st.selectbox(
        "Implementación de Ethernet sin pérdidas (Lossless Ethernet):", 
        ["Seleccione", 
         "Proactivo y Ajustado: PFC y ECN en todos los switches.", 
         "Parcialmente Desplegado: Algunos mecanismos como PFC, sin ECN.", 
         "Solo Jumbo Frames: Sin PFC ni ECN.", 
         "Sin mecanismos sin pérdida: Ethernet estándar."]
    )
    respuestas['arch_congestion'] = st.selectbox(
        "Manejo de congestión de tráfico (Incast):", 
        ["Seleccione", 
         "Manejo Avanzado: Buffers profundos y algoritmos inteligentes (DCQCN).", 
         "QoS Estándar: Políticas estándar no diseñadas específicamente para incast.", 
         "Reactivo: Se solucionan problemas conforme surgen.", 
         "Incierto / No abordado."]
    )

# Section B: Network Operations & Performance
with st.expander("B. Operaciones y Rendimiento de Red"):
    respuestas['ops_visibility'] = st.selectbox(
        "Nivel de visibilidad del tráfico específico de IA:", 
        ["Seleccione", 
         "Visibilidad Exhaustiva: Telemetría en tiempo real (RoCE v2, microbursts, PFC/ECN).", 
         "Monitoreo General: Métricas estándar (SNMP/CLI), sin insights de IA.", 
         "Monitoreo Básico: Revisiones manuales o esporádicas.", 
         "Sin visibilidad activa."]
    )
    respuestas['ops_automation'] = st.selectbox(
        "Madurez en automatización y despliegue:", 
        ["Seleccione", 
         "Altamente Maduro: Controlador centralizado basado en políticas (VLANs, VRFs, QoS).", 
         "Moderadamente Maduro: Scripts personalizados (Ansible, Python).", 
         "Etapa Temprana: Explorando automatización, dependencia de CLI manual.", 
         "No Maduro: Cambios puramente manuales vía CLI."]
    )
    respuestas['ops_troubleshoot'] = st.selectbox(
        "Solución de problemas de rendimiento (Troubleshooting):", 
        ["Seleccione", 
         "Proactivo y Automatizado: Plataformas de analítica impulsadas por IA para causa raíz.", 
         "Manual y Correlacionado: Recopilación manual de logs de múltiples dispositivos.", 
         "Reactivo: Revisión de switches individuales tras reportes de fallas.", 
         "Sin proceso formal."]
    )

# Section C: Network Strategy & Readiness
with st.expander("C. Estrategia y Preparación de Red"):
    respuestas['strat_training'] = st.selectbox(
        "Programas de entrenamiento para cargas de trabajo de IA:", 
        ["Seleccione", 
         "Programas Exhaustivos: Capacitación formal regular (RoCE, BGP-EVPN, automatización).", 
         "Algunos Programas: Sesiones ocasionales o autoaprendizaje.", 
         "Programas Limitados: Muy pocas oportunidades disponibles.", 
         "Sin programas formales."]
    )
    respuestas['strat_security'] = st.selectbox(
        "Adaptación del modelo de seguridad para IA:", 
        ["Seleccione", 
         "Zero-Trust / Microsegmentación: Políticas granulares y tráfico este-oeste cifrado.", 
         "Enfoque Perimetral: Seguridad enfocada en tráfico norte-sur, segmentación interna limitada.", 
         "ACLs Básicas: Listas de control de acceso estándar en el core.", 
         "Sin seguridad específica para IA."]
    )

# Section D: Network Security & Compliance
with st.expander("D. Seguridad de Red y Cumplimiento"):
    respuestas['sec_encryption'] = st.selectbox(
        "Estrategia de cifrado de datos en movimiento (Este-Oeste):", 
        ["Seleccione", 
         "Basado en Hardware: Cifrado a velocidad de línea (ej. MACsec) sin impacto en rendimiento.", 
         "Basado en Software: Consume ciclos de CPU/GPU.", 
         "Cifrado Perimetral: Solo tráfico que sale del Data Center.", 
         "Sin cifrado interno."]
    )
    respuestas['sec_monitoring'] = st.selectbox(
        "Monitoreo de amenazas internas o anomalías:", 
        ["Seleccione", 
         "Analítica de Red Integrada: Plataforma central que ingiere telemetría para detectar anomalías.", 
         "Herramientas Independientes: Análisis de tráfico no integrado, requiere correlación manual.", 
         "Solo Análisis de Logs: Syslog o NetFlow tradicional.", 
         "Sin monitoreo de amenazas internas."]
    )
    respuestas['sec_edge'] = st.selectbox(
        "Principales preocupaciones al llevar modelos de IA al Edge:", 
        ["Seleccione", 
         "Complejidad Operativa (múltiples entornos/herramientas).", 
         "Postura de Seguridad Inconsistente.", 
         "Falta de Automatización en entornos híbridos.", 
         "Poca Visibilidad (dificultad para troubleshooting end-to-end)."]
    )

# Section E: Front-End/Management Network
with st.expander("E. Red Front-End y de Gestión"):
    respuestas['front_traffic'] = st.selectbox(
        "Gestión del tráfico Norte-Sur (Gestión, almacenamiento, aplicación):", 
        ["Seleccione", 
         "Estratégico y Segmentado: Redes dedicadas con políticas claras.", 
         "Convergente con QoS: Priorización robusta en flujos norte-sur.", 
         "Convergencia Básica: Poca diferenciación de prioridades.", 
         "Área por definir: Sin plan claro aún."]
    )
    respuestas['front_scaling'] = st.selectbox(
        "Escalamiento de capacidad para tráfico norte-sur (Ingesta de datos):", 
        ["Seleccione", 
         "Escalado Proactivo: Capacidad dedicada y suficiente margen.", 
         "Actualizaciones Planeadas: Satisface necesidades iniciales pero requerirá mejora.", 
         "Cuello de Botella Anticipado: Requiere actualización significativa previa.", 
         "Evaluación Pendiente."]
    )
    respuestas['front_integration'] = st.selectbox(
        "Integración operativa entre red Front-End y Back-End:", 
        ["Seleccione", 
         "Plataforma Unificada: Control y visibilidad consolidada para este-oeste y norte-sur.", 
         "Integración Parcial: Monitoreo conjunto pero aprovisionamiento separado.", 
         "Estrategia de Gestión Separada.", 
         "Estrategia por definir."]
    )

# Section F: Open Ended
with st.expander("F. Preguntas Abiertas"):
    abiertas['open_concerns'] = st.text_area(
        "Más allá de las necesidades actuales, ¿cuáles son sus principales preocupaciones para soportar futuras iniciativas de IA (nuevos modelos, volúmenes de datos, Edge)?", 
        placeholder="Ingrese sus comentarios aquí..."
    )
    abiertas['open_scaling'] = st.text_area(
        "¿Cómo planea escalar el ancho de banda y densidad de puertos en los próximos 12-24 meses para acomodar el crecimiento de IA?", 
        placeholder="Ingrese sus comentarios aquí..."
    )

# --- SECCIÓN 3: Información Estratégica (BANT) ---
st.header("3. Información Estratégica (BANT)")
st.write("Calificación de la oportunidad comercial.")

col_bant1, col_bant2 = st.columns(2)
with col_bant1:
    bant_reto = st.selectbox("¿Cuál es el reto principal?", 
                             ["Seleccione", "Despliegue de Fabric para IA", "Refresco Tecnológico de Data Center", "Falta de Visibilidad y Automatización", "Segmentación y Seguridad Interna", "Migración a Nube Híbrida/Edge"])
    bant_presupuesto = st.selectbox("Presupuesto", 
                                    ["Seleccione", "Sí, presupuesto aprobado", "En proceso de aprobación", "Sin presupuesto asignado aún"])
with col_bant2:
    bant_tiempo = st.selectbox("Tiempo de implementación", 
                               ["Seleccione", "0 a 3 meses", "3 a 6 meses", "6 a 12 meses", "Más de 12 meses"])
    bant_comp = st.selectbox("Plataformas evaluadas (Competencia)", 
                             ["Seleccione", "Arista Networks", "NVIDIA / Mellanox", "Juniper Networks", "VMWare NSX", "Ninguna / Solo Cisco", "Otras"])

bant_notas = st.text_area("Detalles adicionales de la estrategia", 
                          placeholder="Ej. El cliente busca implementar un clúster de GPU en Q3 y necesita actualizar sus switches Core y Leaf...")

# --- LÓGICA DE RECOMENDACIÓN DE PRODUCTOS ---
def generar_recomendaciones(resp):
    recomendaciones = []
    
    # Arquitectura & Diseño (Nexus 9000 & ACI/NDFC)
    if any(palabra in resp['arch_support'] for palabra in ["Necesita Mejora", "No Preparado"]) or \
       any(palabra in resp['arch_lossless'] for palabra in ["Solo Jumbo", "Sin mecanismos"]):
        recomendaciones.append("- **Cisco Nexus 9000 Series & ACI / NDFC:** Para establecer un fabric Leaf-Spine de alto rendimiento, baja latencia y preparado para IA, soportando RoCEv2 de forma nativa con gestión automatizada de congestión (PFC/ECN).")
    
    # Operaciones & Visibilidad (Nexus Dashboard)
    if any(palabra in resp['ops_visibility'] for palabra in ["General", "Básico", "Sin visibilidad"]) or \
       any(palabra in resp['ops_troubleshoot'] for palabra in ["Manual", "Reactivo", "Sin proceso"]):
        recomendaciones.append("- **Cisco Nexus Dashboard Insights (NDI):** Para habilitar telemetría avanzada, detección de anomalías proactiva y visibilidad profunda (microbursts, análisis de flujos) potenciada por IA en todo el fabric.")
        
    # Seguridad & Cifrado (Secure Workload & MACsec)
    if any(palabra in resp['sec_encryption'] for palabra in ["Software", "Perimetral", "Sin cifrado"]) or \
       any(palabra in resp['strat_security'] for palabra in ["Perimetral", "ACLs", "Sin seguridad"]):
        recomendaciones.append("- **Cisco Secure Workload (Tetration):** Para implementar una estrategia robusta de microsegmentación Zero-Trust, protegiendo los flujos de tráfico este-oeste a nivel de carga de trabajo.")
        recomendaciones.append("- **Cisco Nexus MACsec:** Se recomienda activar el cifrado basado en hardware a velocidad de línea en los switches Nexus para asegurar el tráfico entre nodos GPU y almacenamiento sin afectar el rendimiento.")

    # Edge & Front-End (NDFC / Multicloud)
    if "Complejidad" in resp['sec_edge'] or "Separada" in resp['front_integration']:
        recomendaciones.append("- **Cisco Nexus Dashboard Fabric Controller (NDFC):** Para simplificar la complejidad operativa proporcionando un panel de cristal único que automatiza y unifica la gestión de redes de Front-End, Back-End y despliegues en el Edge.")

    if not recomendaciones:
        recomendaciones.append("- **Cisco Success Tracks / EA Data Center:** Su arquitectura actual está altamente madura. Recomendamos evaluar acuerdos empresariales (EA) para optimizar el consumo de licencias o Success Tracks para mantener la salud operativa de sus despliegues de IA.")
        
    return recomendaciones

# --- GENERACIÓN DE PDF ---
def crear_pdf(empresa, contacto, correo, puesto, am_cisco, resp_best, fecha, vertical, bant_reto, bant_presupuesto, bant_tiempo, bant_comp, bant_notas, respuestas, abiertas, recomendaciones):
    pdf = FPDF()
    pdf.add_page()
    
    def clean_txt(texto):
        if not texto: return "N/A"
        return str(texto).encode('latin-1', 'replace').decode('latin-1')
        
    # Cabecera
    pdf.set_font("Arial", 'B', 16)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 10, clean_txt("Acta de Evaluación - Datacenter Networking para AI"), ln=True, align='C')
    pdf.set_font("Arial", 'I', 11)
    pdf.cell(0, 6, clean_txt("Elaborado por: Best - Typhoon Technology"), ln=True, align='C')
    pdf.ln(8)
    
    # 1. Info General
    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 8, clean_txt("1. Información General del Cliente"), ln=True)
    pdf.set_font("Arial", '', 10)
    
    # Filas de datos
    datos = [
        ("Empresa:", empresa, "Vertical:", vertical),
        ("Contacto:", contacto, "Fecha:", fecha),
        ("Correo:", correo, "AM Cisco:", am_cisco),
        ("Puesto:", puesto, "Preventa:", resp_best)
    ]
    for eti1, val1, eti2, val2 in datos:
        pdf.cell(30, 6, clean_txt(eti1), border=0)
        pdf.cell(65, 6, clean_txt(val1), border=0)
        pdf.cell(30, 6, clean_txt(eti2), border=0)
        pdf.cell(65, 6, clean_txt(val2), border=0, ln=True)
    pdf.ln(5)
    
    # 2. Cuestionario
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, clean_txt("2. Resumen de Evaluación Técnica"), ln=True)
    
    # Helper para imprimir secciones
    def add_section_to_pdf(titulo, llaves_respuestas):
        pdf.set_font("Arial", 'B', 10)
        pdf.cell(0, 6, clean_txt(titulo), ln=True)
        pdf.set_font("Arial", '', 9)
        for val in llaves_respuestas:
            pdf.set_x(10)
            pdf.multi_cell(0, 5, clean_txt(f"- {respuestas[val]}"))
        pdf.ln(3)

    add_section_to_pdf("A. Arquitectura y Diseño de Red", ['arch_support', 'arch_reference', 'arch_lossless', 'arch_congestion'])
    add_section_to_pdf("B. Operaciones y Rendimiento de Red", ['ops_visibility', 'ops_automation', 'ops_troubleshoot'])
    add_section_to_pdf("C. Estrategia y Preparación de Red", ['strat_training', 'strat_security'])
    add_section_to_pdf("D. Seguridad de Red y Cumplimiento", ['sec_encryption', 'sec_monitoring', 'sec_edge'])
    add_section_to_pdf("E. Red Front-End y Gestión", ['front_traffic', 'front_scaling', 'front_integration'])
    
    # Abiertas
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, 6, clean_txt("F. Preguntas Abiertas (Comentarios del Cliente)"), ln=True)
    pdf.set_font("Arial", 'I', 9)
    pdf.set_x(10)
    pdf.multi_cell(0, 5, clean_txt(f"Preocupaciones futuras: {abiertas['open_concerns']}"))
    pdf.set_x(10)
    pdf.multi_cell(0, 5, clean_txt(f"Plan de escalabilidad: {abiertas['open_scaling']}"))
    pdf.ln(5)

    # 3. BANT
    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 8, clean_txt("3. Información Estratégica (BANT)"), ln=True)
    pdf.set_font("Arial", '', 10)
    pdf.set_x(10)
    pdf.multi_cell(0, 6, clean_txt(f"Reto Principal: {bant_reto} | Presupuesto: {bant_presupuesto}"))
    pdf.set_x(10)
    pdf.multi_cell(0, 6, clean_txt(f"Tiempo: {bant_tiempo} | Competencia: {bant_comp}"))
    pdf.set_font("Arial", 'I', 9)
    pdf.set_text_color(50, 50, 50)
    pdf.set_x(10)
    pdf.multi_cell(0, 5, clean_txt(f"Detalles Adicionales: {bant_notas}"))
    pdf.ln(5)
    
    # 4. Recomendaciones
    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 8, clean_txt("4. Arquitectura Cisco Data Center Recomendada"), ln=True)
    pdf.set_font("Arial", '', 10)
    for rec in recomendaciones:
        texto_limpio = rec.replace("**", "")
        pdf.set_x(10)
        pdf.multi_cell(0, 5, clean_txt(texto_limpio))
        pdf.ln(2)
        
    # Disclaimer
    pdf.ln(8)
    pdf.set_font("Arial", 'I', 8)
    pdf.set_text_color(100, 100, 100)
    disclaimer = "Nota importante: Esta información es una sugerencia preliminar enfocada en arquitecturas de IA. Sujeta a validación técnica y diseño formal por un Arquitecto de Soluciones de Typhoon Technology."
    pdf.set_x(10)
    pdf.multi_cell(0, 4, clean_txt(disclaimer))
    
    # Exportación
    salida_pdf = pdf.output(dest="S")
    if isinstance(salida_pdf, str):
        return salida_pdf.encode("latin-1")
    else:
        return bytes(salida_pdf)

# --- BOTÓN DE GENERACIÓN ---
st.divider()

def checar_completado(dict_respuestas, list_bant):
    for val in dict_respuestas.values():
        if "Seleccione" in str(val): return False
    for val in list_bant:
        if "Seleccione" in str(val): return False
    return True

if st.button("Generar Evaluación y Preparar PDF"):
    lista_bant = [bant_reto, bant_presupuesto, bant_tiempo, bant_comp]
    
    if not empresa:
        st.warning("Por favor, introduzca al menos el nombre de la empresa en la Información General.")
    elif not checar_completado(respuestas, lista_bant):
        st.warning("Asegúrese de responder todas las preguntas desplegables (Información Estratégica y Dominios) antes de generar el reporte.")
    else:
        recomendaciones = generar_recomendaciones(respuestas)
        
        st.success("¡Análisis completado exitosamente!")
        st.subheader("Sugerencia de Soluciones (Vista Previa):")
        for r in recomendaciones:
            st.markdown(r)
            
        pdf_bytes = crear_pdf(empresa, contacto, correo, puesto, am_cisco, resp_best, fecha, vertical, 
                              bant_reto, bant_presupuesto, bant_tiempo, bant_comp, bant_notas, 
                              respuestas, abiertas, recomendaciones)
                              
        nombre_archivo = f"DC_AI_Networking_Assessment_{empresa.replace(' ', '_')}.pdf"
        
        st.download_button(
            label="📄 Descargar PDF de la Evaluación",
            data=pdf_bytes,
            file_name=nombre_archivo,
            mime="application/pdf"
        )