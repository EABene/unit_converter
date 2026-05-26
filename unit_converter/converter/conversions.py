def convert(value, from_unit, to_unit):
    # Alles zuerst in Meter umrechnen
    to_meters = {
        'km': 1000,
        'miles': 1609.344,
    }
    
    in_meters = value * to_meters[from_unit]
    result = in_meters / to_meters[to_unit]
    return result
