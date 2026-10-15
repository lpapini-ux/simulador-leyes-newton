import math
import streamlit as st

G = 9.81

st.set_page_config(page_title="Simulador de Leyes de Newton", page_icon="⚙️", layout="wide")

st.title("Simulador de las Leyes de Newton")
st.caption("Principios Físicos para Ingeniería | Universidad Autónoma del Perú")
st.markdown(
    "Esta versión web permite explorar la **Segunda Ley de Newton** en cuatro escenarios. "
    "Introduce los datos y pulsa **Calcular** para ver resultados y desarrollo matemático."
)

with st.sidebar:
    st.header("Escenario")
    escenario = st.selectbox(
        "Selecciona un problema",
        ["Superficie plana", "Plano inclinado", "Polea Atwood", "Bloques conectados"]
    )
    st.divider()
    st.write("**Constante utilizada**")
    st.write(f"Gravedad: {G} m/s²")

def mostrar_resultados(items):
    st.subheader("Resultados")
    columnas = st.columns(4)
    for i, (nombre, valor) in enumerate(items):
        with columnas[i % 4]:
            st.metric(nombre, valor)

def mostrar_desarrollo(texto):
    with st.expander("Ver desarrollo matemático", expanded=True):
        st.code(texto, language=None)

if escenario == "Superficie plana":
    st.subheader("Bloque sobre una superficie plana")
    c1, c2, c3 = st.columns(3)
    with c1:
        fuerza = st.number_input("Fuerza aplicada (N)", min_value=0.0, value=100.0, step=1.0)
    with c2:
        masa = st.number_input("Masa (kg)", min_value=0.01, value=5.0, step=0.5)
    with c3:
        mu = st.number_input("Coeficiente de fricción μ", min_value=0.0, value=0.2, step=0.05)

    if st.button("Calcular", type="primary"):
        peso = masa * G
        normal = peso
        friccion = mu * normal
        fuerza_neta = fuerza - friccion
        aceleracion = fuerza_neta / masa
        mostrar_resultados([
            ("Fuerza aplicada", f"{fuerza:.2f} N"),
            ("Fricción", f"{friccion:.2f} N"),
            ("Fuerza neta", f"{fuerza_neta:.2f} N"),
            ("Aceleración", f"{aceleracion:.2f} m/s²"),
            ("Masa", f"{masa:.2f} kg"),
            ("Peso", f"{peso:.2f} N"),
            ("Normal", f"{normal:.2f} N"),
            ("μ", f"{mu:.2f}")
        ])
        desarrollo = (
            f"Peso:\nP = m × g = {masa:.2f} × {G:.2f} = {peso:.2f} N\n\n"
            f"Normal:\nN = P = {normal:.2f} N\n\n"
            f"Fricción:\nf = μ × N = {mu:.2f} × {normal:.2f} = {friccion:.2f} N\n\n"
            f"Fuerza neta:\nΣF = F - f = {fuerza:.2f} - {friccion:.2f} = {fuerza_neta:.2f} N\n\n"
            f"Segunda Ley de Newton:\na = ΣF / m = {fuerza_neta:.2f} / {masa:.2f} = {aceleracion:.2f} m/s²"
        )
        mostrar_desarrollo(desarrollo)
        st.info("Sin fricción si μ = 0. La fricción se opone al movimiento y reduce la fuerza neta disponible.")

elif escenario == "Plano inclinado":
    st.subheader("Bloque sobre un plano inclinado")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        fuerza = st.number_input("Fuerza aplicada (N)", min_value=0.0, value=0.0, step=1.0)
    with c2:
        masa = st.number_input("Masa (kg)", min_value=0.01, value=5.0, step=0.5)
    with c3:
        mu = st.number_input("Coeficiente de fricción μ", min_value=0.0, value=0.0, step=0.05)
    with c4:
        angulo = st.number_input("Ángulo (°)", min_value=0.0, max_value=89.0, value=30.0, step=1.0)

    if st.button("Calcular", type="primary"):
        rad = math.radians(angulo)
        peso = masa * G
        peso_x = peso * math.sin(rad)
        peso_y = peso * math.cos(rad)
        normal = peso_y
        friccion = mu * normal
        # Se conserva la convención de signos del programa de escritorio original.
        fuerza_neta = fuerza + friccion - peso_x
        aceleracion = fuerza_neta / masa
        mostrar_resultados([
            ("Fuerza aplicada", f"{fuerza:.2f} N"),
            ("Fricción", f"{friccion:.2f} N"),
            ("Fuerza neta", f"{fuerza_neta:.2f} N"),
            ("Aceleración", f"{aceleracion:.2f} m/s²"),
            ("Masa", f"{masa:.2f} kg"),
            ("Peso", f"{peso:.2f} N"),
            ("Normal", f"{normal:.2f} N"),
            ("μ", f"{mu:.2f}")
        ])
        desarrollo = (
            f"Peso:\nP = m × g = {masa:.2f} × {G:.2f} = {peso:.2f} N\n\n"
            f"Componente paralela:\nPx = P × sen(θ) = {peso:.2f} × sen({angulo:.2f}°) = {peso_x:.2f} N\n\n"
            f"Componente perpendicular:\nPy = P × cos(θ) = {peso:.2f} × cos({angulo:.2f}°) = {peso_y:.2f} N\n\n"
            f"Normal:\nN = Py = {normal:.2f} N\n\n"
            f"Fricción:\nf = μ × N = {mu:.2f} × {normal:.2f} = {friccion:.2f} N\n\n"
            f"Fuerza neta (convención del programa original):\nΣF = F + f - Px = {fuerza:.2f} + {friccion:.2f} - {peso_x:.2f} = {fuerza_neta:.2f} N\n\n"
            f"Segunda Ley:\na = ΣF / m = {fuerza_neta:.2f} / {masa:.2f} = {aceleracion:.2f} m/s²"
        )
        mostrar_desarrollo(desarrollo)
        st.info("La aceleración es positiva o negativa según el eje elegido; en este escenario el eje positivo se toma hacia arriba del plano.")

elif escenario == "Polea Atwood":
    st.subheader("Sistema de dos masas conectadas por una polea de Atwood")
    c1, c2 = st.columns(2)
    with c1:
        masa_a = st.number_input("Masa A (kg)", min_value=0.01, value=5.5, step=0.5)
    with c2:
        masa_b = st.number_input("Masa B (kg)", min_value=0.01, value=10.0, step=0.5)

    if st.button("Calcular", type="primary"):
        masa_total = masa_a + masa_b
        aceleracion = abs(masa_b - masa_a) * G / masa_total
        if masa_b > masa_a:
            tension = masa_a * (G + aceleracion)
            direccion = "B desciende; A asciende"
            desarrollo_t = f"B desciende y A asciende:\nT = mA × (g + a) = {masa_a:.2f} × ({G:.2f} + {aceleracion:.4f}) = {tension:.2f} N"
        elif masa_a > masa_b:
            tension = masa_b * (G + aceleracion)
            direccion = "A desciende; B asciende"
            desarrollo_t = f"A desciende y B asciende:\nT = mB × (g + a) = {masa_b:.2f} × ({G:.2f} + {aceleracion:.4f}) = {tension:.2f} N"
        else:
            tension = masa_a * G
            direccion = "Equilibrio"
            desarrollo_t = f"Equilibrio:\nT = mA × g = {masa_a:.2f} × {G:.2f} = {tension:.2f} N"
        peso_a = masa_a * G
        peso_b = masa_b * G
        mostrar_resultados([
            ("Masa A", f"{masa_a:.2f} kg"),
            ("Masa B", f"{masa_b:.2f} kg"),
            ("Masa total", f"{masa_total:.2f} kg"),
            ("Aceleración", f"{aceleracion:.2f} m/s²"),
            ("Tensión", f"{tension:.2f} N"),
            ("Peso A", f"{peso_a:.2f} N"),
            ("Peso B", f"{peso_b:.2f} N"),
            ("Dirección", direccion)
        ])
        desarrollo = (
            f"Peso de A:\nPA = mA × g = {masa_a:.2f} × {G:.2f} = {peso_a:.2f} N\n\n"
            f"Peso de B:\nPB = mB × g = {masa_b:.2f} × {G:.2f} = {peso_b:.2f} N\n\n"
            f"Aceleración:\na = |mB - mA| × g / (mA + mB)\n"
            f"a = |{masa_b:.2f} - {masa_a:.2f}| × {G:.2f} / {masa_total:.2f} = {aceleracion:.4f} m/s²\n\n"
            f"{desarrollo_t}"
        )
        mostrar_desarrollo(desarrollo)
        st.info(f"Interpretación: {direccion}. Se supone una cuerda ideal y una polea sin masa ni fricción.")

else:
    st.subheader("Bloques conectados")
    c1, c2, c3 = st.columns(3)
    with c1:
        fuerza = st.number_input("Fuerza aplicada (N)", min_value=0.0, value=60.0, step=1.0)
        masa_a = st.number_input("Masa A (kg)", min_value=0.01, value=10.0, step=1.0)
    with c2:
        masa_b = st.number_input("Masa B (kg)", min_value=0.01, value=20.0, step=1.0)
        masa_c = st.number_input("Masa C (kg; 0 si no se usa)", min_value=0.0, value=30.0, step=1.0)
    with c3:
        mu = st.number_input("Coeficiente de fricción μ", min_value=0.0, value=0.0, step=0.05)
        st.caption("A y B deben ser positivos. C puede ser cero.")

    if st.button("Calcular", type="primary"):
        masas = [masa_a, masa_b] + ([masa_c] if masa_c > 0 else [])
        masa_total = sum(masas)
        fricciones = [mu * m * G for m in masas]
        friccion_total = sum(fricciones)
        fuerza_neta = fuerza - friccion_total
        aceleracion = fuerza_neta / masa_total
        tension_ab = sum(masas[1:]) * aceleracion + sum(fricciones[1:])
        tension_bc = masa_c * aceleracion + fricciones[2] if masa_c > 0 else None
        if masa_c > 0:
            mostrar_resultados([
                ("Fuerza aplicada", f"{fuerza:.2f} N"),
                ("Masa A", f"{masa_a:.2f} kg"),
                ("Masa B", f"{masa_b:.2f} kg"),
                ("Masa C", f"{masa_c:.2f} kg"),
                ("Aceleración", f"{aceleracion:.2f} m/s²"),
                ("Tensión A-B", f"{tension_ab:.2f} N"),
                ("Tensión B-C", f"{tension_bc:.2f} N"),
                ("Fuerza neta", f"{fuerza_neta:.2f} N")
            ])
            desarrollo_t = (
                f"T_AB = (mB + mC) × a + fB + fC\n"
                f"T_AB = ({masa_b:.2f} + {masa_c:.2f}) × {aceleracion:.4f} + {fricciones[1]:.2f} + {fricciones[2]:.2f} = {tension_ab:.2f} N\n\n"
                f"T_BC = mC × a + fC\n"
                f"T_BC = {masa_c:.2f} × {aceleracion:.4f} + {fricciones[2]:.2f} = {tension_bc:.2f} N"
            )
        else:
            mostrar_resultados([
                ("Fuerza aplicada", f"{fuerza:.2f} N"),
                ("Masa A", f"{masa_a:.2f} kg"),
                ("Masa B", f"{masa_b:.2f} kg"),
                ("Aceleración", f"{aceleracion:.2f} m/s²"),
                ("Tensión A-B", f"{tension_ab:.2f} N"),
                ("Fricción total", f"{friccion_total:.2f} N"),
                ("Fuerza neta", f"{fuerza_neta:.2f} N"),
                ("μ", f"{mu:.2f}")
            ])
            desarrollo_t = (
                f"T = mB × a + fB\n"
                f"T = {masa_b:.2f} × {aceleracion:.4f} + {fricciones[1]:.2f} = {tension_ab:.2f} N"
            )
        desarrollo = (
            f"Sistema de {len(masas)} bloques\n\n"
            f"Fricción total:\nfT = μ × g × mT = {mu:.2f} × {G:.2f} × {masa_total:.2f} = {friccion_total:.2f} N\n\n"
            f"Fuerza neta:\nΣF = F - fT = {fuerza:.2f} - {friccion_total:.2f} = {fuerza_neta:.2f} N\n\n"
            f"Segunda Ley:\na = ΣF / mT = {fuerza_neta:.2f} / {masa_total:.2f} = {aceleracion:.4f} m/s²\n\n"
            f"{desarrollo_t}"
        )
        mostrar_desarrollo(desarrollo)
        st.info(f"Los {len(masas)} bloques se modelan con la misma aceleración. La fricción total reduce la fuerza neta.")

st.divider()
st.caption(
    "Equipo: Gálvez Santamaría, Hilary; Mejía Balvin, Liz Sharon; Nolasco Rojas, Raúl Adrián; "
    "Papini Briceño, Luis Ernesto; Sánchez Bustamante, Sajami."
)
