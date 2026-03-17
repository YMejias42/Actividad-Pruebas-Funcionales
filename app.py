def autenticar_usuario(username, password):
    usuarios = {
        "admin": "1234",
        "javier": "python123",
        "estudiante": "abc123"
    }

    if username == "" or password == "":
        return {
            "success": False,
            "message": "Usuario y contraseña son requeridos",
            "response_time_ms": 50
        }

    if username not in usuarios:
        return {
            "success": False,
            "message": "Usuario no existe",
            "response_time_ms": 70
        }

    if usuarios[username] != password:
        return {
            "success": False,
            "message": "Contraseña incorrecta",
            "response_time_ms": 80
        }

    return {
        "success": True,
        "message": "Acceso concedido",
        "response_time_ms": 60
    }
