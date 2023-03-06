def convert_units(value, from_unit, to_unit):
    # Dicionário de unidades de tempo
    time_units = {
        "segundos": 1,
        "minutos": 60,
        "horas": 3600
    }

    # Dicionário de unidades de volume
    volume_units = {
        "litros": 1,
        "mililitros": 1000
    }

    # Dicionário de unidades de massa
    mass_units = {
        "kg": 1,
        "g": 1000
    }

    # Verifica se a unidade de origem e destino estão no dicionário de unidades de tempo
    if from_unit in time_units and to_unit in time_units:
        return value * time_units[from_unit] / time_units[to_unit]

    # Verifica se a unidade de origem e destino estão no dicionário de unidades de volume
    elif from_unit in volume_units and to_unit in volume_units:
        return value * volume_units[from_unit] / volume_units[to_unit]

    # Verifica se a unidade de origem e destino estão no dicionário de unidades de massa
    elif from_unit in mass_units and to_unit in mass_units:
        return value * mass_units[from_unit] / mass_units[to_unit]

    # Caso contrário, retorna mensagem de erro
    else:
        return "Unidade de medida não suportada"

value = float(input("Informe o valor a ser convertido: "))
from_unit = input("Informe a unidade de origem (ex.: segundos, minutos, horas, litros, mililitros, kg, g): ")
to_unit = input("Informe a unidade de destino (ex.: segundos, minutos, horas, litros, mililitros, kg, g): ")

result = convert_units(value, from_unit, to_unit)
print("Resultado:", result, to_unit)
