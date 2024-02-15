

def individual_serial(asegurado) -> dict:
    return {
        "id": asegurado["id"]["$oid"],
        "seccion": asegurado["seccion"]["$numberInt"],
        "poliza": asegurado["poliza"]["$numberInt"],
        "endoso": asegurado["endoso"]["$numberInt"],
        "certificado": asegurado["certificado"]["$numberInt"],
        "emision": asegurado["emision"]["$date"],
        "asegurado": asegurado["asegurado"],
        "nacimiento": asegurado["nacimiento"]["$date"],
        "documento": asegurado["documento"]["$numberInt"],
        "capital": asegurado["capital"]["$numberInt"],
        "tipo": asegurado.get("tipo", None),
        "plazo": asegurado.get("plazo", None),
        "desde": asegurado["desde"]["$date"],
        "cancelacion": asegurado["cancelacion"]["$date"],
        "premio": asegurado["premio"]["$numberInt"],
        "solicitud": asegurado.get("solicitud", None),
    }

def list_serial(asegurados) -> list:
    return [individual_serial(asegurado) for asegurado in asegurados]