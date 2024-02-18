from src.models.enums import CharacterClassesEnum

def validate_not_empty(key, value):
    if not value or value.isspace():
        raise ValueError(f"{key} cannot be empty")
    return value

def validate_class(key, value):
        if value not in CharacterClassesEnum:
            raise ValueError(f"Invalid value for {key}: {value}")
        return value
    
    
    