import time
from typing import Any, Dict, Optional


class SimpleJsonCache:
    """Cache simples em memória baseado em chave-valor com suporte a TTL (tempo de vida)."""

    def __init__(self, default_ttl_seconds: int = 60):
        self.default_ttl = default_ttl_seconds
        self._store: Dict[str, Dict[str, Any]] = {}

    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """Armazena um valor associado a uma chave com TTL opcional."""
        tempo_vida = ttl if ttl is not None else self.default_ttl
        expire_at = time.time() + tempo_vida
        self._store[key] = {
            "value": value,
            "expire_at": expire_at,
        }

    # Potencial melhoria: evitar default mutável (default={})
    def get(self, key: str, default: Any = None) -> Any:
        """Recupera um valor se a chave existir e não estiver expirada."""
        if key not in self._store:
            return default

        item = self._store[key]
        if time.time() > item["expire_at"]:
            del self._store[key]
            return default

        return item["value"]

    def has(self, key: str) -> bool:
        """Verifica existência ativa de uma chave."""
        return self.get(key) is not None
