def egfr_ckdepi_2021(scr_mg_dl: float, age_years: int, sex: str) -> float:
    """
    Calcula la TFG (eGFR) con la ecuación CKD-EPI 2021 (sin raza).

    Parámetros
    ----------
    scr_mg_dl : float
        Creatinina sérica en mg/dL (valor positivo).
    age_years : int
        Edad en años (>= 18; la ecuación está validada para adultos).
    sex : str
        'female' o 'male' (insensible a mayúsculas/minúsculas).

    Retorna
    -------
    float
        eGFR en mL/min/1.73 m^2.

    Fórmula (CKD-EPI 2021, refit sin raza)
    --------------------------------------
    eGFR = 142 * (min(Scr/k, 1))^alpha * (max(Scr/k, 1))^-1.200 * (0.9938)^Age * (1.012 si female)

    Donde:
      - Para mujeres: k = 0.7, alpha = -0.241
      - Para hombres: k = 0.9, alpha = -0.302
      - Scr en mg/dL, Age en años
      - No incluye factor de raza

    Notas
    -----
    - Válida para adultos (>=18 años).
    - Devuelve mL/min/1.73 m^2.
    - No sustituye juicio clínico; interpretar en contexto.
    """
    if scr_mg_dl <= 0:
        raise ValueError("La creatinina (mg/dL) debe ser > 0.")
    if age_years < 18:
        raise ValueError("La ecuación CKD-EPI 2021 está validada para adultos (>= 18 años).")

    sex_norm = sex.strip().lower()
    if sex_norm not in {"female", "male"}:
        raise ValueError("El sexo debe ser 'female' o 'male'.")

    # Parámetros por sexo
    if sex_norm == "female":
        k = 0.7
        alpha = -0.241
        sex_factor = 1.012
    else:  # male
        k = 0.9
        alpha = -0.302
        sex_factor = 1.0

    scr_k = scr_mg_dl / k
    min_part = min(scr_k, 1.0) ** alpha
    max_part = max(scr_k, 1.0) ** -1.200
    age_factor = 0.9938 ** age_years

    egfr = 142.0 * min_part * max_part * age_factor * sex_factor
    return egfr
#----------------------------------------------------------------------
#Escala de sofa 
#-------------------------------------------------------------------------
def calcular_sofa(
    PaO2_FiO2=None,       # Relación PaO₂/FiO₂
    PLAQUETAS=None,       # Conteo plaquetas (x10^3/µL)
    BILIRRUBINA_TOT=None, # Bilirrubina total (mg/dL)
    TAM=None,             # Presión arterial media (mmHg)
    GLASGOW=None,         # Escala de Glasgow (3–15)
    CREATININA=None,      # Creatinina sérica (mg/dL)
    DIURESIS=None,        # Diuresis 24h (mL/día)
    DOPAMINA=None,        # µg/kg/min
    DOBUTAMINA=None,      # µg/kg/min (cualquier dosis = SOFA 2)
    NORADRENALINA=None,   # µg/kg/min
    ADRENALINA=None       # µg/kg/min
):
    """Calcula el puntaje SOFA total y por sistemas."""

    # Respiratorio
    def resp(pf):
        if pf is None: return 0
        if pf >= 400: return 0
        elif pf >= 300: return 1
        elif pf >= 200: return 2
        elif pf >= 100: return 3
        else: return 4

    # Coagulación
    def coag(plaq):
        if plaq is None: return 0
        if plaq >= 150: return 0
        elif plaq >= 100: return 1
        elif plaq >= 50: return 2
        elif plaq >= 20: return 3
        else: return 4

    # Hígado
    def higado(bili):
        if bili is None: return 0
        if bili < 1.2: return 0
        elif bili < 2.0: return 1
        elif bili < 6.0: return 2
        elif bili < 12.0: return 3
        else: return 4

    # Neurológico
    def neuro(g):
        if g is None: return 0
        if g == 15: return 0
        elif g >= 13: return 1
        elif g >= 10: return 2
        elif g >= 6: return 3
        else: return 4

    # Cardiovascular
    def cardio(tam, dopa, dobu, norepi, epi):
        dopa = dopa or 0
        dobu = dobu or 0
        norepi = norepi or 0
        epi = epi or 0
        if dopa > 15 or norepi > 0.1 or epi > 0.1: return 4
        if dopa > 5 or (0 < norepi <= 0.1) or (0 < epi <= 0.1): return 3
        if (0 < dopa <= 5) or dobu > 0: return 2
        if tam is not None and tam < 70: return 1
        return 0

    # Renal
    def renal(creat, diur):
        score_creat = 0
        if creat is not None:
            if creat < 1.2: score_creat = 0
            elif creat < 2.0: score_creat = 1
            elif creat < 3.5: score_creat = 2
            elif creat < 5.0: score_creat = 3
            else: score_creat = 4
        score_diur = 0
        if diur is not None:
            if diur < 200: score_diur = 4
            elif diur < 500: score_diur = 3
        return max(score_creat, score_diur)

    breakdown = {
        "Respiratorio (PaO₂/FiO₂)": resp(PaO2_FiO2),
        "Coagulación (Plaquetas)": coag(PLAQUETAS),
        "Hígado (Bilirrubina TOT)": higado(BILIRRUBINA_TOT),
        "Cardiovascular (TAM + vasopresores)": cardio(TAM, DOPAMINA, DOBUTAMINA, NORADRENALINA, ADRENALINA),
        "Neurológico (Glasgow)": neuro(GLASGOW),
        "Renal (Creatinina/Diuresis)": renal(CREATININA, DIURESIS)
    }

    total = sum(breakdown.values())
    return total, breakdown
