import pytest
from src.translator import Translator
from src.dependency_containers.translator_container import TranslatorContainer


def test_translator():
  container = TranslatorContainer()
  translator_service = container.translator_service()
  response = translator_service.execute("hola")
  print(response)
  assert response == "hola"