import time
from app import autenticar_usuario

# Casos de prueba (Testing) CP-01 a CP-07

def test_cp01_login_exitoso():
    r = autenticar_usuario("admin", "1234")
    assert r["success"] is True
    assert r["message"] == "Acceso concedido"

def test_cp02_usuario_vacio():
    r = autenticar_usuario("", "1234")
    assert r["success"] is False
    assert r["message"] == "Usuario y contraseña son requeridos"

def test_cp03_contrasena_vacia():
    r = autenticar_usuario("admin", "")
    assert r["success"] is False
    assert r["message"] == "Usuario y contraseña son requeridos"

def test_cp04_usuario_inexistente():
    r = autenticar_usuario("pedro", "1234")
    assert r["success"] is False
    assert r["message"] == "Usuario no existe"

def test_cp05_contrasena_incorrecta():
    r = autenticar_usuario("admin", "9999")
    assert r["success"] is False
    assert r["message"] == "Contraseña incorrecta"

def test_cp06_tiempo_respuesta_valido():
    r = autenticar_usuario("admin", "1234")
    assert r["response_time_ms"] > 0
    assert r["response_time_ms"] < 500

def test_cp07_estructura_salida():
    r = autenticar_usuario("admin", "1234")
    assert "success" in r
    assert "message" in r
    assert "response_time_ms" in r

# Pruebas exploratorias
def test_exploratoria_espacios():
    r = autenticar_usuario("   ", "1234")
    assert r["success"] is False

def test_exploratoria_mayusculas():
    r = autenticar_usuario("ADMIN", "1234")
    assert r["success"] is False

def test_exploratoria_caracteres_especiales():
    r = autenticar_usuario("@dm!n", "1234")
    assert r["success"] is False

def test_exploratoria_ambos_vacios():
    r = autenticar_usuario("", "")
    assert r["success"] is False

def test_exploratoria_password_larga():
    r = autenticar_usuario("admin", "x"*100)
    assert r["success"] is False

# Prueba de tiempo real
def test_tiempo_real():
    inicio = time.perf_counter()
    r = autenticar_usuario("admin", "1234")
    fin = time.perf_counter()
    tiempo_ms = (fin - inicio) * 1000
    assert tiempo_ms < 500

# Prueba de regresión
def test_regresion_mensaje_correcto():
    r = autenticar_usuario("admin", "1234")
    assert r["message"] == "Acceso concedido"

# 5 Pruebas adicionales

def test_exploratoria_espacios_en_username():
    r = autenticar_usuario("   ", "1234")
    assert r["success"] is False

def test_exploratoria_mayusculas_username():
    r = autenticar_usuario("ADMIN", "1234")
    assert r["success"] is False

def test_exploratoria_caracteres_especiales():
    r = autenticar_usuario("@dm!n", "1234")
    assert r["success"] is False

def test_exploratoria_ambos_campos_vacios():
    r = autenticar_usuario("", "")
    assert r["success"] is False

def test_exploratoria_password_muy_larga():
    r = autenticar_usuario("admin", "x"*200)
    assert r["success"] is False
