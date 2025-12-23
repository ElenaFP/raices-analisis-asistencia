#!/usr/bin/env python3
import csv
import sys
import os
from collections import defaultdict

# Verificar que se proporcionó el archivo CSV como argumento
if len(sys.argv) < 2:
    print("Error: Debes proporcionar el nombre del archivo CSV como argumento.")
    print()
    print("Uso:")
    print(f"  python3 {sys.argv[0]} <archivo.csv>")
    print()
    print("Ejemplo:")
    print(f"  python3 {sys.argv[0]} DescargaExpGesExpDat_20251223_130245_105367.CSV")
    sys.exit(1)

csv_file = sys.argv[1]

# Verificar que el archivo existe
if not os.path.exists(csv_file):
    print(f"Error: El archivo '{csv_file}' no existe.")
    sys.exit(1)

print(f"Procesando archivo: {csv_file}")
print()

# Diccionarios para almacenar las faltas y retrasos por curso para cada evaluación
faltas_1ev = defaultdict(int)
retrasos_1ev = defaultdict(int)
faltas_2ev = defaultdict(int)
retrasos_2ev = defaultdict(int)
faltas_3ev = defaultdict(int)
retrasos_3ev = defaultdict(int)
# Diccionario para almacenar NIAs únicos por curso (usando set para evitar duplicados)
nias_por_curso = defaultdict(set)
# Variable para guardar el año del curso
anno_curso = None

# Leer y procesar el CSV
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=',')

    for row in reader:
        # Capturar el año del curso (solo la primera vez)
        if anno_curso is None:
            anno_curso = row['C_ANNO']

        curso = row['CURSO']
        nia = row['NIA']

        # Leer datos de las tres evaluaciones
        faltas_1_str = row['FALTAS_ASISTENCIA_1EV']
        retrasos_1_str = row['RETRASOS_ASISTENCIA_1EV']
        faltas_2_str = row['FALTAS_ASISTENCIA_2EV']
        retrasos_2_str = row['RETRASOS_ASISTENCIA_2EV']
        faltas_3_str = row['FALTAS_ASISTENCIA_3EV']
        retrasos_3_str = row['RETRASOS_ASISTENCIA_3EV']

        # Agrupar cursos de Bachillerato
        if curso.startswith('1º de Bachillerato'):
            curso = '1º de Bachillerato'
        elif curso.startswith('2º de Bachillerato'):
            curso = '2º de Bachillerato'
        # Agrupar Programas de Diversificación con sus cursos de ESO
        elif curso == '1º Programa de Diversificación Curricular (LOMLOE)':
            curso = '3º de E.S.O. (LOMLOE)'
        elif curso == '2º Programa de Diversificación Curricular (LOMLOE)':
            curso = '4º de E.S.O. (LOMLOE)'

        # Convertir a entero, si está vacío o no es número usar 0
        def to_int(val):
            try:
                return int(val) if val else 0
            except ValueError:
                return 0

        faltas_1ev[curso] += to_int(faltas_1_str)
        retrasos_1ev[curso] += to_int(retrasos_1_str)
        faltas_2ev[curso] += to_int(faltas_2_str)
        retrasos_2ev[curso] += to_int(retrasos_2_str)
        faltas_3ev[curso] += to_int(faltas_3_str)
        retrasos_3ev[curso] += to_int(retrasos_3_str)

        nias_por_curso[curso].add(nia)

# Función para ordenar cursos por nivel educativo
def orden_curso(curso):
    orden = {
        '1º de E.S.O. (LOMLOE)': 1,
        '2º de E.S.O. (LOMLOE)': 2,
        '3º de E.S.O. (LOMLOE)': 3,
        '4º de E.S.O. (LOMLOE)': 4,
        '1º de Bachillerato': 5,
        '2º de Bachillerato': 6
    }
    return orden.get(curso, 99)

# Función para mostrar una tabla y guardar CSV
def mostrar_tabla(titulo, faltas_dict, retrasos_dict, nias_dict, csv_filename=None):
    # Ordenar por nivel educativo
    faltas_ordenadas = sorted(faltas_dict.items(), key=lambda x: orden_curso(x[0]))

    print("\n" + "=" * 115)
    print(titulo)
    print("=" * 115)
    print(f"{'CURSO':<35} {'ALUMNOS':>8} {'FALTAS':>10} {'RETRASOS':>10} {'MEDIA FALTAS':>15} {'MEDIA RETRASOS':>15}")
    print("-" * 115)

    # Preparar datos para CSV
    datos_csv = []

    for curso, total_faltas in faltas_ordenadas:
        total_retrasos = retrasos_dict[curso]
        num_alumnos = len(nias_dict[curso])
        media_faltas = total_faltas / num_alumnos if num_alumnos > 0 else 0
        media_retrasos = total_retrasos / num_alumnos if num_alumnos > 0 else 0
        print(f"{curso:<35} {num_alumnos:>8} {total_faltas:>10} {total_retrasos:>10} {media_faltas:>15.2f} {media_retrasos:>15.2f}")

        # Guardar datos para CSV
        datos_csv.append({
            'CURSO': curso,
            'ALUMNOS': num_alumnos,
            'FALTAS': total_faltas,
            'RETRASOS': total_retrasos,
            'MEDIA_FALTAS': round(media_faltas, 2),
            'MEDIA_RETRASOS': round(media_retrasos, 2)
        })

    print("=" * 115)

    # Totales generales
    total_nias_unicos = len(set().union(*nias_dict.values()))
    total_faltas = sum(faltas_dict.values())
    total_retrasos = sum(retrasos_dict.values())
    media_general_faltas = total_faltas / total_nias_unicos if total_nias_unicos > 0 else 0
    media_general_retrasos = total_retrasos / total_nias_unicos if total_nias_unicos > 0 else 0

    print(f"{'TOTAL GENERAL:':<35} {total_nias_unicos:>8} {total_faltas:>10} {total_retrasos:>10} {media_general_faltas:>15.2f} {media_general_retrasos:>15.2f}")
    print("=" * 115)

    # Agregar totales al CSV
    datos_csv.append({
        'CURSO': 'TOTAL GENERAL',
        'ALUMNOS': total_nias_unicos,
        'FALTAS': total_faltas,
        'RETRASOS': total_retrasos,
        'MEDIA_FALTAS': round(media_general_faltas, 2),
        'MEDIA_RETRASOS': round(media_general_retrasos, 2)
    })

    # Escribir CSV si se especifica nombre de archivo
    if csv_filename:
        with open(csv_filename, 'w', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['CURSO', 'ALUMNOS', 'FALTAS', 'RETRASOS', 'MEDIA_FALTAS', 'MEDIA_RETRASOS']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(datos_csv)
        print(f"CSV generado: {csv_filename}")

# Mostrar tabla para 1ª Evaluación
mostrar_tabla(f"FALTAS Y RETRASOS DE ASISTENCIA - 1ª EVALUACIÓN (Curso {anno_curso})",
              faltas_1ev, retrasos_1ev, nias_por_curso,
              f"{anno_curso}_1EV.csv")

# Mostrar tabla para 2ª Evaluación
mostrar_tabla(f"FALTAS Y RETRASOS DE ASISTENCIA - 2ª EVALUACIÓN (Curso {anno_curso})",
              faltas_2ev, retrasos_2ev, nias_por_curso,
              f"{anno_curso}_2EV.csv")

# Mostrar tabla para 3ª Evaluación
mostrar_tabla(f"FALTAS Y RETRASOS DE ASISTENCIA - 3ª EVALUACIÓN (Curso {anno_curso})",
              faltas_3ev, retrasos_3ev, nias_por_curso,
              f"{anno_curso}_3EV.csv")

# Calcular totales del curso (suma de las 3 evaluaciones)
faltas_total = defaultdict(int)
retrasos_total = defaultdict(int)

for curso in nias_por_curso.keys():
    faltas_total[curso] = faltas_1ev[curso] + faltas_2ev[curso] + faltas_3ev[curso]
    retrasos_total[curso] = retrasos_1ev[curso] + retrasos_2ev[curso] + retrasos_3ev[curso]

# Mostrar tabla para el Total del Curso
mostrar_tabla(f"FALTAS Y RETRASOS DE ASISTENCIA - TOTAL DEL CURSO (Curso {anno_curso})",
              faltas_total, retrasos_total, nias_por_curso,
              f"{anno_curso}_TOTAL.csv")
