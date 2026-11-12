import time
from json_cache import SimpleJsonCache


def test_cache_set_and_get():
    cache = SimpleJsonCache(default_ttl_seconds=10)
    cache.set("usuario", {"id": 1, "nome": "Rafael"})

    assert cache.has("usuario") is True
    assert cache.get("usuario")["nome"] == "Rafael"
    assert cache.get("chave_inexistente", "padrao") == "padrao"


def test_cache_expiracao():
    cache = SimpleJsonCache(default_ttl_seconds=1)
    cache.set("token", "xyz_123", ttl=1)

    assert cache.get("token") == "xyz_123"
    time.sleep(1.1)
    assert cache.get("token") is None
