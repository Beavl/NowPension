from .context import q1


def test_generate_sentences():
    assert q1.generate_sentences(["Vlad", "John"], ["drives"], ["car", "motorcycle", "bus"]) == "John drives bus. John drives car. John drives motorcycle. Vlad drives bus. Vlad drives car. Vlad drives motorcycle."


def test_generate_sentences_empty():
    assert q1.generate_sentences([], [], []) == ""


def test_generate_sentences_itertools():
    assert q1.generate_sentences_itertools(["Vlad", "John"], ["drives"], ["car", "motorcycle", "bus"]) == "John drives bus. John drives car. John drives motorcycle. Vlad drives bus. Vlad drives car. Vlad drives motorcycle."


def test_generate_sentences_empty_itertools():
    assert q1.generate_sentences_itertools([], [], []) == ""
