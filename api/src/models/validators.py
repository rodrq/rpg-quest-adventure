from src.models.enums import CharacterClassesEnum, CharacterVirtuesEnum, CharacterFlawsEnum

def validate_not_empty(key, value):
    if not value or value.isspace():
        raise ValueError(f"{key} cannot be empty")
    return value

def validate_enum(key, value):
    if not value:
        raise ValueError(f"{key} cannot be empty")
    
    enum_mapping = {
        'class_': CharacterClassesEnum,
        'virtue': CharacterVirtuesEnum,
        'flaw': CharacterFlawsEnum,
    }
    enum_type = enum_mapping.get(key)
    if enum_type is None:
        raise ValueError(f"Invalid key: {key}")

    if value not in enum_type:
        raise ValueError(f"Invalid value for {key}: {value}")

    print(value)
    return value
 