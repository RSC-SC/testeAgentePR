import pytest
from url_validator import is_valid_url, extract_domain


def test_is_valid_url():
    assert is_valid_url("https://github.com/RSC-SC/testeAgentePR") is True
    assert is_valid_url("http://localhost:8000/api") is True
    assert is_valid_url("ftp://servidor.com") is False
    assert is_valid_url("") is False
    assert is_valid_url(None) is False


def test_extract_domain():
    assert extract_domain("https://github.com/owner/repo") == "github.com"
    assert extract_domain("http://api.sistema.com.br:8080/v1") == "api.sistema.com.br"
    assert extract_domain("invalida") is None
