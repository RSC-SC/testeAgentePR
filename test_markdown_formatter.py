from markdown_formatter import format_heading, format_bullet_list, format_blockquote


def test_format_heading():
    assert format_heading("Título Principal", 1) == "# Título Principal"
    assert format_heading("Subtítulo", 2) == "## Subtítulo"
    assert format_heading("Nível Máximo", 10) == "###### Nível Máximo"


def test_format_bullet_list():
    itens = ["Item 1", "Item 2", "Item 3"]
    esperado = "- Item 1\n- Item 2\n- Item 3"
    assert format_bullet_list(itens) == esperado
    assert format_bullet_list([]) == ""


def test_format_blockquote():
    texto = "Linha 1\nLinha 2"
    esperado = "> Linha 1\n> Linha 2"
    assert format_blockquote(texto) == esperado
    assert format_blockquote("") == ""
