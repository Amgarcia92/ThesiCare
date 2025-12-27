# ThesiCare - Sistema de Información Médica 🏥

**Plataforma web para cálculo de escalas médicas y evaluación clínica**

ThesiCare es una aplicación web desarrollada con Django especializada en el cálculo de escalas médicas, específicamente la estimación de la Tasa de Filtración Glomerular (eGFR) usando la ecuación CKD-EPI 2021.

## Características principales

- 🏥 **Cálculo eGFR CKD-EPI 2021**: Estimación en tiempo real de función renal
- 🎨 **Interface médica moderna**: Diseño profesional y responsive
- ✅ **Validación clínica**: Restricción a población adulta (≥18 años)
- 🎯 **Sistema de colores**: Interpretación visual según rangos clínicos
- 🔒 **Seguridad de datos**: Bloqueo automático para edades no válidas
- ⚡ **Tiempo real**: Cálculos instantáneos al ingresar datos

## Tecnologías utilizadas

- **Backend**: Django 5.2.9
- **Frontend**: HTML5, CSS3, JavaScript
- **Base de datos**: SQLite
- **Python**: 3.11+

# Instalación y Configuración

### Prerrequisitos
- Python 3.11+
- pip (gestor de paquetes de Python)

### Instalación Local

1. **Clona el repositorio:**
```bash
git clone https://github.com/tu-usuario/ThesiCare.git
cd ThesiCare
```

2. **Crea un entorno virtual:**
```bash
python -m venv env
env\Scripts\activate  # Windows
source env/bin/activate  # Linux/Mac
```

3. **Instala dependencias:**
```bash
pip install -r requirements.txt
```

4. **Ejecuta migraciones:**
```bash
python manage.py migrate
```

5. **Inicia el servidor:**
```bash
python manage.py runserver
```

## Deployment en la Web

### Opción 1: Railway (Recomendado)
1. Crea cuenta en [Railway.app](https://railway.app)
2. Conecta tu repositorio GitHub
3. Railway detectará automáticamente Django
4. Se desplegará automáticamente

### Opción 2: Heroku
1. Instala Heroku CLI
2. Crea aplicación: `heroku create thesicare-app`
3. Push a Heroku: `git push heroku main`
4. Ejecuta migraciones: `heroku run python manage.py migrate`

### Opción 3: Render
1. Conecta repositorio en [Render.com](https://render.com)
2. Configuración automática con `requirements.txt`
3. Deploy automático desde GitHub

## Uso del Sistema

### Cálculo de eGFR

1. **Edad**: Ingresa edad del paciente (≥18 años)
   - Si edad < 18: Se muestra mensaje "En el momento solo para población adulta"
   - Los campos SEXO y CREATININA se bloquean automáticamente

2. **Sexo**: Selecciona M (Masculino) o F (Femenino)

3. **Creatinina**: Ingresa valor en mg/dl
   - Valores > 1.3 mg/dl se destacan en color

4. **Resultado**: eGFR se calcula automáticamente
   - 🔘 **Gris**: Datos insuficientes
   - 🟢 **Verde**: eGFR ≥ 90 (función normal)
   - 🔴 **Rojo**: eGFR < 90 (función reducida)

## Escalas Médicas

### eGFR CKD-EPI 2021
- **Ecuación**: CKD-EPI 2021 (sin factor de raza)
- **Población**: Adultos ≥18 años
- **Unidades**: mL/min/1.73 m²
- **Fórmula**: 142 × (min(Scr/k, 1))^α × (max(Scr/k, 1))^-1.200 × (0.9938)^Edad × (1.012 si mujer)

#### Parámetros por sexo:
- **Mujeres**: k = 0.7, α = -0.241
- **Hombres**: k = 0.9, α = -0.302

## Estructura del Proyecto

```
ThesiCare/
├── main/                    # App principal
│   ├── templates/main/      # Templates HTML
│   │   └── home.html       # Interface principal
│   └── views.py            # Lógica de vistas
├── escalas.py              # Funciones médicas
├── ThesiCare/              # Configuración Django
│   └── settings.py         # Configuración del proyecto
├── requirements.txt        # Dependencias
├── Procfile               # Configuración Heroku
└── README.md              # Documentación
```

## Tecnologías Utilizadas

### Backend
- **Django 5.2.9**: Framework web principal
- **Python 3.11**: Lenguaje de programación
- **SQLite/PostgreSQL**: Base de datos

### Frontend  
- **HTML5**: Estructura semántica
- **CSS3**: Estilos modernos con gradientes y animaciones
- **JavaScript**: Cálculos en tiempo real y validaciones

### Deployment
- **Gunicorn**: Servidor WSGI para producción
- **WhiteNoise**: Servicio de archivos estáticos
- **dj-database-url**: Configuración de base de datos

## Características Técnicas

### Validaciones
- ✅ Edad mínima 18 años
- ✅ Creatinina valores positivos
- ✅ Sexo obligatorio para cálculo
- ✅ Bloqueo automático de campos

### Interface
- 🎨 Design médico profesional
- 📱 Responsive para móviles
- ⚡ Cálculos instantáneos
- 🎯 Colores según interpretación clínica

### Seguridad
- 🔒 Configuración segura para producción
- 🌐 Variables de entorno
- 📊 Logs de errores
- 🛡️ Middleware de seguridad Django

## Autor

**Proyecto desarrollado para tesis de grado**
- Universidad: Pontificia Universidad Javeriana
- Área: Sistema de Información Médica
- Enfoque: Escalas de evaluación clínica

## Licencia

MIT License - Ver archivo LICENSE para más detalles

## Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Haz fork del proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## Soporte

Para soporte técnico o preguntas sobre el sistema:
- Abre un issue en GitHub
- Consulta la documentación médica incluida
- Revisa los logs de error en caso de problemas

---

**⚠️ Importante**: Este sistema es para fines educativos y de investigación. No sustituye el juicio clínico profesional.

### Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   # El proyecto ya está en: C:\Users\andre\OneDrive - Pontificia Universidad Javeriana\Tesis\ThesiCare
   ```

2. **Navegar al directorio del proyecto**
   ```bash
   cd "C:\Users\andre\OneDrive - Pontificia Universidad Javeriana\Tesis\ThesiCare"
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Realizar migraciones**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

7. **Acceder a la aplicación**
   - Abrir navegador en: http://127.0.0.1:8000/
   - Panel de administración: http://127.0.0.1:8000/admin/

## Estructura del Proyecto

```
ThesiCare/
├── manage.py                # Script de gestión de Django
├── requirements.txt         # Dependencias del proyecto
├── .env.example            # Ejemplo de variables de entorno
├── ThesiCare/              # Configuración principal del proyecto
│   ├── __init__.py
│   ├── settings.py         # Configuraciones de Django
│   ├── urls.py             # URLs principales
│   └── wsgi.py             # Configuración WSGI para despliegue
├── main/                   # Aplicación principal
│   ├── templates/          # Plantillas HTML
│   ├── views.py            # Vistas de la aplicación
│   ├── urls.py             # URLs de la aplicación
│   ├── models.py           # Modelos de datos
│   └── admin.py            # Configuración del admin
├── static/                 # Archivos estáticos (CSS, JS)
│   ├── css/
│   └── js/
└── media/                  # Archivos multimedia subidos
```

## Tecnologías Utilizadas

- **Backend**: Django 5.2.9
- **Base de datos**: SQLite (desarrollo) / PostgreSQL (producción recomendada)
- **Frontend**: HTML5, CSS3, JavaScript
- **Librerías**: Pillow (manejo de imágenes), python-dotenv (variables de entorno)

## Despliegue en Producción

### Preparación para producción

1. **Configurar variables de entorno**
   ```bash
   # Copiar archivo de ejemplo
   cp .env.example .env
   # Editar .env con configuraciones de producción
   ```

2. **Configurar base de datos**
   - Recomendado: PostgreSQL
   - Actualizar DATABASE_URL en .env

3. **Configurar archivos estáticos**
   ```bash
   python manage.py collectstatic
   ```

### Opciones de despliegue

- **Heroku**: Plataforma cloud fácil de usar
- **DigitalOcean**: Droplets con mayor control
- **AWS**: EC2, Elastic Beanstalk, o Lambda
- **Vercel/Netlify**: Para despliegues rápidos

## Desarrollo

### Comandos útiles

```bash
# Crear nueva aplicación
python manage.py startapp nueva_app

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Ejecutar servidor de desarrollo
python manage.py runserver

# Ejecutar shell de Django
python manage.py shell

# Ejecutar tests
python manage.py test
```

## Contribución

1. Fork del repositorio
2. Crear rama para nueva característica (`git checkout -b feature/nueva-caracteristica`)
3. Commit de cambios (`git commit -am 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crear Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto

- **Desarrollador**: [Tu nombre]
- **Email**: [tu-email@ejemplo.com]
- **Universidad**: Pontificia Universidad Javeriana

---

**¡Gracias por usar ThesiCare!** 🎓📚