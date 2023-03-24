# Usuario
* Nombre (string)
* Correo (string) (Clave Primaria)
* Contraseña (string)
* Dobletitulacion (booleano)
* carrera 1 (clave foranea)
* carrera 2 (clave foranea) (nullable)

# Asignatura
* Codigo asignatura (int) (clave primaria)
* Temas (string)
* Parciales (documentos)
* Matrial (documentos)

# Carrera
* codigo plan de estudios (int) (clave primaria)
* Sede (string)
* Facultad (string)
* Departamento (string)
* Director (string)
* Secretaria (string)

# Sesion de estudio
* codigo de sesion (int) (auto_escalable) (clave primaria)
* Hora (fecha)
* Ubicacion (clave foranea)
* Tematica (string)
* Material (documentos)

# Grupo de estudio
* codigo grupo de estudio (int) (auto_escalable) (clave primaria)
* Asignatura (clave foranea)
* Objetivos (string)
* material (documentos)

# Estudiante X Grupo de estudio
* cod grupo de estudio (clave foranea)
* estudienate (clave foranea)

# Sesion de estudio X Grupo de estudio
* cod grupo de estudio
* cod grupo de sesion

# Asignatura X Sesion de estudio
* cod asignatura (clave foranea)
* cod sesion de estudio (clave foranea)

# Ubicacion
* Nombre (string) (clave primaria)
* Geolocalizacion (coordenada)

# Asignatura X Carrera
* cod asignatura (clave foranea)
* cod carrera (clave foranea)

# Sesion de estudio X Estudiante
* cod sesion (clave foranea)
* estudiante (clave foranea)

# Amista (Estudiante X Estudiante)
* Estudiante 1 (clave foranea)
* Estudiante 2 (clave foranea)
