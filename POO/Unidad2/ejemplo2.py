from datetime import timedelta

class Pelicula:
    def __init__(self, id, titulo, clasificacion, director,
                 subtitulos, duracion_horas,
                 duracion_minutos):
        self.id = id
        self.titulo = titulo
        self.clasificacion = clasificacion
        self.director = director
        self.duracion = timedelta(hours=duracion_horas, minutes=duracion_minutos)
        self.subtitulos = subtitulos
    
    def Convertir_A_Minutos(self):
        return int(self.duracion.total_seconds() // 60)
    
    def Tiene_Subtitulos(self):
        return self.subtitulos
    
mi_Pelicula = Pelicula(
    1, "Avengers", "+13", "Quien sabe", False, 2, 30)

print(f"""
      Titulo: {mi_Pelicula.titulo}
      Clasificación: {mi_Pelicula.clasificacion}
      Director: {mi_Pelicula.director}
      Duración minutos: {mi_Pelicula.duracion}
      Subtitulo: {'Si' if mi_Pelicula.Tiene_Subtitulos() else 'No'}
      """)