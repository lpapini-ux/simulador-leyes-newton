
import tkinter as tk
from tkinter import messagebox
import math

from leyes_newton import SegundaLey

GRAVEDAD = 9.81


def mostrar_desarrollo(desarrollo_label, texto):
    desarrollo_label.config(state="normal")
    desarrollo_label.delete("1.0", tk.END)
    desarrollo_label.insert(tk.END, texto)
    desarrollo_label.see("1.0")
    desarrollo_label.config(state="disabled")


def actualizar_tarjetas(tarjetas, nombres, valores):
    """Actualiza las 8 tarjetas de resultados."""
    for i in range(8):
        tarjetas[i].config(
            text=f"{nombres[i]}\n{valores[i]}"
        )


def limpiar_resultados(tarjetas, resultado_label, interpretacion_label, desarrollo_label):
    actualizar_tarjetas(
        tarjetas,
        ["RESULTADO"] * 8,
        ["--"] * 8
    )
    resultado_label.config(text="")
    interpretacion_label.config(text="Interpretación")
    mostrar_desarrollo(desarrollo_label, "Desarrollo matemático")


def calcular_superficie_plana(entrada1, entrada2, entrada3,
                              tarjetas, resultado_label,
                              interpretacion_label, desarrollo_label):
    try:
        fuerza = float(entrada1.get())
        masa = float(entrada2.get())
        texto_mu = entrada3.get().strip()
        mu = 0.0 if texto_mu == "" else float(texto_mu)
    except ValueError:
        messagebox.showerror("Error", "Ingresa valores numéricos válidos.")
        return

    if fuerza < 0 or masa <= 0 or mu < 0:
        messagebox.showerror("Error", "La fuerza no puede ser negativa, la masa debe ser mayor que cero y μ no puede ser negativo.")
        return

    peso = masa * GRAVEDAD
    normal = peso
    friccion = mu * normal
    fuerza_neta = fuerza - friccion

    ley = SegundaLey()
    aceleracion = ley.calcular(fuerza=fuerza_neta, masa=masa)
    if isinstance(aceleracion, str):
        messagebox.showerror("Error", aceleracion)
        return

    actualizar_tarjetas(
        tarjetas,
        ["FUERZA APLICADA", "FRICCIÓN", "FUERZA NETA", "ACELERACIÓN",
         "MASA", "PESO", "NORMAL", "μ CINÉTICO"],
        [f"{fuerza:.2f} N", f"{friccion:.2f} N", f"{fuerza_neta:.2f} N",
         f"{aceleracion:.2f} m/s²", f"{masa:.2f} kg", f"{peso:.2f} N",
         f"{normal:.2f} N", f"{mu:.2f}"]
    )

    desarrollo = (
        "Peso:\n"
        "P = m × g\n"
        f"P = {masa:.2f} × {GRAVEDAD:.2f}\n"
        f"P = {peso:.2f} N\n\n"
        "Normal:\n"
        "N = P = m × g\n"
        f"N = {normal:.2f} N\n\n"
        "Fricción:\n"
        "f = μ × N\n"
        f"f = {mu:.2f} × {normal:.2f}\n"
        f"f = {friccion:.2f} N\n\n"
        "Fuerza neta:\n"
        "ΣF = F - f\n"
        f"ΣF = {fuerza:.2f} - {friccion:.2f}\n"
        f"ΣF = {fuerza_neta:.2f} N\n\n"
        "Segunda Ley de Newton:\n"
        "a = ΣF / m\n"
        f"a = {fuerza_neta:.2f} / {masa:.2f}\n"
        f"a = {aceleracion:.2f} m/s²"
    )
    mostrar_desarrollo(desarrollo_label, desarrollo)

    if mu == 0:
        texto = "No se considera fricción porque μ = 0 o el campo quedó vacío."
    else:
        texto = "La fricción se opone al movimiento y reduce la fuerza neta disponible para acelerar el bloque."
    interpretacion_label.config(text=texto)
    resultado_label.config(text="Cálculo realizado correctamente.")


def calcular_plano_inclinado(entrada1, entrada2, entrada3, entrada4,
                              tarjetas, resultado_label,
                              interpretacion_label, desarrollo_label):
    try:
        fuerza = float(entrada1.get())
        masa = float(entrada2.get())
        texto_mu = entrada3.get().strip()
        mu = 0.0 if texto_mu == "" else float(texto_mu)
        angulo = float(entrada4.get())
    except ValueError:
        messagebox.showerror("Error", "Ingresa valores numéricos válidos.")
        return

    if fuerza < 0 or masa <= 0 or mu < 0 or angulo < 0 or angulo >= 90:
        messagebox.showerror("Error", "Revisa fuerza, masa, μ y ángulo. El ángulo debe estar entre 0° y 89°.")
        return

    rad = math.radians(angulo)
    peso = masa * GRAVEDAD
    peso_x = peso * math.sin(rad)
    peso_y = peso * math.cos(rad)
    normal = peso_y
    friccion = mu * normal

    # La fuerza aplicada se toma hacia arriba del plano.
    fuerza_neta = fuerza + friccion - peso_x
    aceleracion = fuerza_neta / masa

    actualizar_tarjetas(
        tarjetas,
        ["FUERZA APLICADA", "FRICCIÓN", "FUERZA NETA", "ACELERACIÓN",
         "MASA", "PESO", "NORMAL", "μ CINÉTICO"],
        [f"{fuerza:.2f} N", f"{friccion:.2f} N", f"{fuerza_neta:.2f} N",
         f"{aceleracion:.2f} m/s²", f"{masa:.2f} kg", f"{peso:.2f} N",
         f"{normal:.2f} N", f"{mu:.2f}"]
    )

    desarrollo = (
        "Peso:\n"
        "P = m × g\n"
        f"P = {masa:.2f} × {GRAVEDAD:.2f}\n"
        f"P = {peso:.2f} N\n\n"
        "Componente paralela:\n"
        "Px = P × sen(θ)\n"
        f"Px = {peso:.2f} × sen({angulo:.2f}°)\n"
        f"Px = {peso_x:.2f} N\n\n"
        "Componente perpendicular:\n"
        "Py = P × cos(θ)\n"
        f"Py = {peso:.2f} × cos({angulo:.2f}°)\n"
        f"Py = {peso_y:.2f} N\n\n"
        "Normal:\n"
        "N = Py\n"
        f"N = {normal:.2f} N\n\n"
        "Fricción:\n"
        "f = μ × N\n"
        f"f = {mu:.2f} × {normal:.2f}\n"
        f"f = {friccion:.2f} N\n\n"
        "Fuerza neta:\n"
        "ΣF = F - Px - f\n"
        f"ΣF = {fuerza:.2f} - {peso_x:.2f} - {friccion:.2f}\n"
        f"ΣF = {fuerza_neta:.2f} N\n\n"
        "Segunda Ley de Newton:\n"
        "a = ΣF / m\n"
        f"a = {fuerza_neta:.2f} / {masa:.2f}\n"
        f"a = {aceleracion:.2f} m/s²"
    )
    mostrar_desarrollo(desarrollo_label, desarrollo)

    if mu == 0:
        texto = "El plano se analiza sin fricción porque μ = 0 o el campo quedó vacío."
    elif aceleracion >= 0:
        texto = "La fuerza aplicada supera la componente del peso y la fricción, por lo que la aceleración es hacia arriba del plano."
    else:
        texto = "La componente del peso y la fricción superan la fuerza aplicada, por lo que la aceleración resulta dirigida hacia abajo del plano."
    interpretacion_label.config(text=texto)
    resultado_label.config(text="Cálculo realizado correctamente.")


def calcular_atwood(entrada1, entrada2, tarjetas, resultado_label,
                    interpretacion_label, desarrollo_label):
    try:
        masa_a = float(entrada1.get())
        masa_b = float(entrada2.get())
    except ValueError:
        messagebox.showerror("Error", "Ingresa valores numéricos válidos.")
        return

    if masa_a <= 0 or masa_b <= 0:
        messagebox.showerror("Error", "Las dos masas deben ser mayores que cero.")
        return

    masa_total = masa_a + masa_b
    aceleracion = abs(masa_b - masa_a) * GRAVEDAD / masa_total

    if masa_b > masa_a:
        tension = masa_a * (GRAVEDAD + aceleracion)
        direccion = "B ↓"
    elif masa_a > masa_b:
        tension = masa_b * (GRAVEDAD + aceleracion)
        direccion = "A ↓"
    else:
        tension = masa_a * GRAVEDAD
        direccion = "Equilibrio"

    peso_a = masa_a * GRAVEDAD
    peso_b = masa_b * GRAVEDAD

    actualizar_tarjetas(
        tarjetas,
        ["MASA A", "MASA B", "MASA TOTAL", "ACELERACIÓN",
         "TENSIÓN", "PESO A", "PESO B", "DIRECCIÓN"],
        [f"{masa_a:.2f} kg", f"{masa_b:.2f} kg", f"{masa_total:.2f} kg",
         f"{aceleracion:.2f} m/s²", f"{tension:.2f} N", f"{peso_a:.2f} N",
         f"{peso_b:.2f} N", direccion]
    )

    if masa_b > masa_a:
        desarrollo_tension = (
            "Tensión:\n"
            "La masa B desciende y la masa A asciende.\n"
            "T = mA × (g + a)\n"
            f"T = {masa_a:.2f} × ({GRAVEDAD:.2f} + {aceleracion:.4f})\n"
            f"T = {tension:.2f} N"
        )
    elif masa_a > masa_b:
        desarrollo_tension = (
            "Tensión:\n"
            "La masa A desciende y la masa B asciende.\n"
            "T = mB × (g + a)\n"
            f"T = {masa_b:.2f} × ({GRAVEDAD:.2f} + {aceleracion:.4f})\n"
            f"T = {tension:.2f} N"
        )
    else:
        desarrollo_tension = (
            "Tensión:\n"
            "El sistema está en equilibrio.\n"
            "T = mA × g\n"
            f"T = {masa_a:.2f} × {GRAVEDAD:.2f}\n"
            f"T = {tension:.2f} N"
        )

    desarrollo = (
        "Peso de A:\n"
        "PA = mA × g\n"
        f"PA = {masa_a:.2f} × {GRAVEDAD:.2f}\n"
        f"PA = {peso_a:.2f} N\n\n"
        "Peso de B:\n"
        "PB = mB × g\n"
        f"PB = {masa_b:.2f} × {GRAVEDAD:.2f}\n"
        f"PB = {peso_b:.2f} N\n\n"
        "Aceleración del sistema:\n"
        "a = |mB - mA| × g / (mA + mB)\n"
        f"a = |{masa_b:.2f} - {masa_a:.2f}| × {GRAVEDAD:.2f} / {masa_total:.2f}\n"
        f"a = {aceleracion:.2f} m/s²\n\n"
        + desarrollo_tension
    )
    mostrar_desarrollo(desarrollo_label, desarrollo)
    interpretacion_label.config(text=f"La masa que desciende es {direccion.split()[0] if direccion != 'Equilibrio' else 'ninguna'}. La tensión es la misma en ambos lados de la cuerda ideal.")
    resultado_label.config(text="Cálculo realizado correctamente.")


def calcular_bloques_conectados(entrada1, entrada2, entrada3, entrada4, entrada5,
                                 tarjetas, resultado_label,
                                 interpretacion_label, desarrollo_label):
    try:
        fuerza = float(entrada1.get())
        masa_a = float(entrada2.get())
        masa_b = float(entrada3.get())
        texto_c = entrada4.get().strip()
        masa_c = 0.0 if texto_c == "" else float(texto_c)
        texto_mu = entrada5.get().strip()
        mu = 0.0 if texto_mu == "" else float(texto_mu)
    except ValueError:
        messagebox.showerror("Error", "Ingresa valores numéricos válidos.")
        return

    if fuerza < 0 or masa_a <= 0 or masa_b <= 0 or masa_c < 0 or mu < 0:
        messagebox.showerror("Error", "Revisa los valores. A y B deben ser mayores que cero; C y μ pueden ser 0, pero no negativos.")
        return

    masas = [masa_a, masa_b] + ([masa_c] if masa_c > 0 else [])
    masa_total = sum(masas)
    fricciones = [mu * m * GRAVEDAD for m in masas]
    friccion_total = sum(fricciones)
    fuerza_neta = fuerza - friccion_total
    aceleracion = fuerza_neta / masa_total

    # Fuerza de contacto entre A-B. Si existe C, es la fuerza que acelera B+C.
    tension_ab = sum(masas[1:]) * aceleracion + sum(fricciones[1:])
    tension_bc = None
    if masa_c > 0:
        tension_bc = masa_c * aceleracion + fricciones[2]

    if masa_c > 0:
        # En tres bloques mostramos las dos fuerzas de contacto
        # y también la masa del tercer bloque.
        actualizar_tarjetas(
            tarjetas,
            ["FUERZA APLICADA", "MASA A", "MASA B", "MASA C",
             "ACELERACIÓN", "TENSIÓN A-B", "TENSIÓN B-C", "FUERZA NETA"],
            [f"{fuerza:.2f} N", f"{masa_a:.2f} kg", f"{masa_b:.2f} kg",
             f"{masa_c:.2f} kg", f"{aceleracion:.2f} m/s²",
             f"{tension_ab:.2f} N", f"{tension_bc:.2f} N",
             f"{fuerza_neta:.2f} N"]
        )
    else:
        actualizar_tarjetas(
            tarjetas,
            ["FUERZA APLICADA", "MASA A", "MASA B", "ACELERACIÓN",
             "TENSIÓN", "FRICCIÓN", "FUERZA NETA", "μ"],
            [f"{fuerza:.2f} N", f"{masa_a:.2f} kg", f"{masa_b:.2f} kg",
             f"{aceleracion:.2f} m/s²", f"{tension_ab:.2f} N",
             f"{friccion_total:.2f} N", f"{fuerza_neta:.2f} N", f"{mu:.2f}"]
        )

    if masa_c > 0:
        desarrollo_tension = (
            "Fuerzas de contacto:\n"
            "T_AB = (mB + mC) × a + fB + fC\n"
            f"T_AB = ({masa_b:.2f} + {masa_c:.2f}) × {aceleracion:.2f} + "
            f"{fricciones[1]:.2f} + {fricciones[2]:.2f}\n"
            f"T_AB = {tension_ab:.2f} N\n\n"
            "T_BC = mC × a + fC\n"
            f"T_BC = {masa_c:.2f} × {aceleracion:.2f} + {fricciones[2]:.2f}\n"
            f"T_BC = {tension_bc:.2f} N"
        )
        tipo_sistema = "tres bloques"
    else:
        desarrollo_tension = (
            "Tensión entre A y B:\n"
            "T = mB × a + fB\n"
            f"T = {masa_b:.2f} × {aceleracion:.2f} + {fricciones[1]:.2f}\n"
            f"T = {tension_ab:.2f} N"
        )
        tipo_sistema = "dos bloques"

    desarrollo = (
        f"Sistema de {tipo_sistema}:\n\n"
        "Fricción total:\n"
        "fT = μ × g × (mA + mB + mC)\n"
        f"fT = {friccion_total:.2f} N\n\n"
        "Fuerza neta:\n"
        "ΣF = F - fT\n"
        f"ΣF = {fuerza:.2f} - {friccion_total:.2f}\n"
        f"ΣF = {fuerza_neta:.2f} N\n\n"
        "Segunda Ley de Newton:\n"
        "a = ΣF / mT\n"
        f"a = {fuerza_neta:.2f} / {masa_total:.2f}\n"
        f"a = {aceleracion:.2f} m/s²\n\n"
        + desarrollo_tension
    )
    mostrar_desarrollo(desarrollo_label, desarrollo)

    if mu == 0:
        texto = f"Los {tipo_sistema} se consideran sin fricción porque μ = 0 o el campo quedó vacío."
    else:
        texto = f"Los {tipo_sistema} se desplazan con la misma aceleración; la fricción total reduce la fuerza neta disponible."
    interpretacion_label.config(text=texto)
    resultado_label.config(text="Cálculo realizado correctamente.")


def mostrar_primera_ley(contenido, boton_primera, boton_segunda, boton_tercera):
    for widget in contenido.winfo_children():
        widget.destroy()
    boton_primera.config(relief="sunken")
    boton_segunda.config(relief="raised")
    boton_tercera.config(relief="raised")
    tk.Label(contenido, text="PRIMERA LEY DE NEWTON", font=("Arial", 20, "bold")).pack(pady=10)
    tk.Label(contenido, text="Ley de la inercia", font=("Arial", 14, "bold")).pack(pady=5)
    tk.Label(contenido, text="ΣF = 0", font=("Arial", 24, "bold")).pack(pady=10)
    tk.Label(contenido, text="Cuando la fuerza neta es cero, un cuerpo mantiene su estado de movimiento.", font=("Arial", 12), wraplength=850).pack(pady=10)


def mostrar_tercera_ley(contenido, boton_primera, boton_segunda, boton_tercera):
    for widget in contenido.winfo_children():
        widget.destroy()
    boton_primera.config(relief="raised")
    boton_segunda.config(relief="raised")
    boton_tercera.config(relief="sunken")
    tk.Label(contenido, text="TERCERA LEY DE NEWTON", font=("Arial", 20, "bold")).pack(pady=10)
    tk.Label(contenido, text="Ley de acción y reacción", font=("Arial", 14, "bold")).pack(pady=5)
    tk.Label(contenido, text="F_AB = -F_BA", font=("Arial", 24, "bold")).pack(pady=10)
    tk.Label(contenido, text="A toda acción corresponde una reacción de igual magnitud y sentido contrario.", font=("Arial", 12), wraplength=850).pack(pady=10)


def crear_tarjetas(contenido):
    marco = tk.Frame(contenido)
    marco.pack(fill="x", padx=25, pady=5)
    tarjetas = []
    for i in range(8):
        tarjeta = tk.Label(
            marco,
            text="RESULTADO\n--",
            width=16,
            height=3,
            relief="groove",
            font=("Arial", 9, "bold"),
            justify="center"
        )
        tarjeta.grid(row=i // 4, column=i % 4, padx=4, pady=4, sticky="nsew")
        tarjetas.append(tarjeta)
    for columna in range(4):
        marco.grid_columnconfigure(columna, weight=1)
    return tarjetas


def crear_simulador_segunda_ley(contenido):
    for widget in contenido.winfo_children():
        widget.destroy()

    tk.Label(contenido, text="ΣF = m × a", font=("Arial", 27, "bold")).pack(pady=(0, 10))
    tk.Label(contenido, text="TIPO DE PROBLEMA", font=("Arial", 12, "bold")).pack(pady=5)

    tipo_problema = tk.StringVar(value="Superficie plana")
    problemas = tk.Frame(contenido)
    problemas.pack(pady=5)

    datos = tk.LabelFrame(contenido, text="DATOS DE ENTRADA", font=("Arial", 11, "bold"), padx=15, pady=10)
    datos.pack(fill="x", padx=30, pady=10)

    etiquetas = [tk.Label(datos, text="") for _ in range(5)]
    entradas = [tk.Entry(datos, width=15) for _ in range(5)]

    for i in range(5):
        fila = i // 2
        columna = (i % 2) * 2
        etiquetas[i].grid(row=fila, column=columna, padx=8, pady=5, sticky="e")
        entradas[i].grid(row=fila, column=columna + 1, padx=8, pady=5)

    tarjetas = crear_tarjetas(contenido)

    resultado_label = tk.Label(contenido, text="", font=("Arial", 10), justify="left")
    resultado_label.pack(pady=3)

    boton_calcular = tk.Button(contenido, text="CALCULAR", font=("Arial", 12, "bold"), width=16)
    boton_calcular.pack(pady=8)

    marco_desarrollo = tk.LabelFrame(contenido, text="DESARROLLO MATEMÁTICO", font=("Arial", 11, "bold"), padx=5, pady=5)
    marco_desarrollo.pack(fill="x", padx=30, pady=5)
    barra = tk.Scrollbar(marco_desarrollo, orient="vertical")
    barra.pack(side="right", fill="y")
    desarrollo_label = tk.Text(marco_desarrollo, height=20, width=80, font=("Arial", 11), wrap="word", yscrollcommand=barra.set)
    desarrollo_label.pack(side="left", fill="both", expand=True)
    barra.config(command=desarrollo_label.yview)
    desarrollo_label.config(state="disabled")

    interpretacion_label = tk.Label(contenido, text="Interpretación", font=("Arial", 11), wraplength=850, justify="left")
    interpretacion_label.pack(pady=5)

    def mostrar_campos():
        for etiqueta, entrada in zip(etiquetas, entradas):
            etiqueta.grid_remove()
            entrada.grid_remove()
            entrada.delete(0, tk.END)

        problema = tipo_problema.get()
        if problema == "Superficie plana":
            configuracion = ["Fuerza aplicada (N):", "Masa (kg):", "Fricción μ:"]
        elif problema == "Plano inclinado":
            configuracion = ["Fuerza aplicada (N):", "Masa (kg):", "Fricción μ:", "Ángulo (°):"]
        elif problema == "Polea Atwood":
            configuracion = ["Masa A (kg):", "Masa B (kg):"]
        else:
            configuracion = ["Fuerza aplicada (N):", "Masa A (kg):", "Masa B (kg):", "Masa C (kg):", "Fricción μ:"]

        for i, texto in enumerate(configuracion):
            fila = i // 2
            columna = (i % 2) * 2
            etiquetas[i].config(text=texto)
            etiquetas[i].grid(row=fila, column=columna, padx=8, pady=5, sticky="e")
            entradas[i].grid(row=fila, column=columna + 1, padx=8, pady=5)

        limpiar_resultados(tarjetas, resultado_label, interpretacion_label, desarrollo_label)

    def ejecutar():
        problema = tipo_problema.get()
        if problema == "Superficie plana":
            calcular_superficie_plana(entradas[0], entradas[1], entradas[2], tarjetas, resultado_label, interpretacion_label, desarrollo_label)
        elif problema == "Plano inclinado":
            calcular_plano_inclinado(entradas[0], entradas[1], entradas[2], entradas[3], tarjetas, resultado_label, interpretacion_label, desarrollo_label)
        elif problema == "Polea Atwood":
            calcular_atwood(entradas[0], entradas[1], tarjetas, resultado_label, interpretacion_label, desarrollo_label)
        else:
            calcular_bloques_conectados(entradas[0], entradas[1], entradas[2], entradas[3], entradas[4], tarjetas, resultado_label, interpretacion_label, desarrollo_label)

    boton_calcular.config(command=ejecutar)

    for opcion in ["Superficie plana", "Plano inclinado", "Polea Atwood", "Bloques conectados"]:
        tk.Radiobutton(problemas, text=opcion, variable=tipo_problema, value=opcion, command=mostrar_campos).pack(side="left", padx=8)

    mostrar_campos()


def mostrar_segunda_ley(contenido, boton_primera, boton_segunda, boton_tercera):
    boton_primera.config(relief="raised")
    boton_segunda.config(relief="sunken")
    boton_tercera.config(relief="raised")
    crear_simulador_segunda_ley(contenido)


def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Simulador de Leyes de Newton")
    ventana.geometry("1100x750")
    ventana.minsize(900, 700)

    canvas = tk.Canvas(ventana, highlightthickness=0)
    barra_scroll = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=barra_scroll.set)
    canvas.pack(side="left", fill="both", expand=True)
    barra_scroll.pack(side="right", fill="y")

    contenido_scroll = tk.Frame(canvas)
    ventana_scroll = canvas.create_window((0, 0), window=contenido_scroll, anchor="nw")

    contenido_scroll.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind("<Configure>", lambda event: canvas.itemconfig(ventana_scroll, width=event.width))
    ventana.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

    tk.Label(contenido_scroll, text="SIMULADOR DE LEYES DE NEWTON", font=("Arial", 24, "bold")).pack(pady=(15, 3))
    tk.Label(contenido_scroll, text="Principios Físicos para Ingeniería", font=("Arial", 13)).pack(pady=(0, 12))

    selector = tk.Frame(contenido_scroll)
    selector.pack(fill="x", padx=25, pady=5)
    contenido = tk.Frame(contenido_scroll)
    contenido.pack(fill="both", expand=True, padx=20, pady=5)

    boton_primera = tk.Button(selector, text="Primera Ley", font=("Arial", 11, "bold"))
    boton_segunda = tk.Button(selector, text="Segunda Ley", font=("Arial", 11, "bold"))
    boton_tercera = tk.Button(selector, text="Tercera Ley", font=("Arial", 11, "bold"))
    for boton in (boton_primera, boton_segunda, boton_tercera):
        boton.pack(side="left", fill="x", expand=True, padx=3)

    boton_primera.config(command=lambda: mostrar_primera_ley(contenido, boton_primera, boton_segunda, boton_tercera))
    boton_segunda.config(command=lambda: mostrar_segunda_ley(contenido, boton_primera, boton_segunda, boton_tercera))
    boton_tercera.config(command=lambda: mostrar_tercera_ley(contenido, boton_primera, boton_segunda, boton_tercera))

    def cerrar_programa():
        mensaje = (
            "Este programa fue desarrollado por:\n\n"
            "Gálvez Santamaría, Hilary\n"
            "Mejía Balvin, Liz Sharon\n"
            "Nolasco Rojas, Raúl Adrián\n"
            "Papini Briceño, Luis Ernesto\n"
            "Sánchez Bustamante, Sajami\n\n"
            "Para el curso de Principios Físicos para Ingeniería."
        )
        messagebox.showinfo("Créditos del programa", mensaje)
        ventana.destroy()

    ventana.protocol("WM_DELETE_WINDOW", cerrar_programa)

    mostrar_segunda_ley(contenido, boton_primera, boton_segunda, boton_tercera)
    return ventana
