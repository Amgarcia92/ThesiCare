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
