# encoding=UTF-8
"""Módulo de Test para la clase src.Controladores.SesionController
"""

from unittest import TestCase
from src.Controladores.SesionController import *

__author__ = 'Gregorio y Ángel'


class TestSesionController(TestCase):
    """Esta clase corresponde al caso de prueba de src.Controladores.SesionController
    """

    def setUp(self):
        """Este método prepara el contexto necesario para las pruebas de TestSesionController.
        """
        print("Preparando contexto para " + self.__class__.__name__)
        self.controlador = SesionController(None)
        self.usuario_tec = "u10025580R"
        self.passwrd_tec = "tecnico"
        self.usuario_doc = "u49251223B"
        self.passwrd_doc = "docente1"

    def tearDown(self):
        """Este método elimina el contexto utilizado para las pruebas de TestSesionController.
        """
        print("Destruyendo contexto para " + self.__class__.__name__)
        del self.controlador
        del self.usuario_tec
        del self.passwrd_tec
        del self.usuario_doc
        del self.passwrd_doc

    def test_get_almacen(self):
        """Comprueba que el controlador puede obtener una instancia de almacen.
        """
        self.assertNotEqual(self.controlador.get_almacen(), None)

    def test_obtener_sesion(self):
        """Comprueba que no devulve ninguna sesión cuando se introducen credenciales erróneas,
        y que se devuelva una sesión cuando las credenciales son correctas.
        """
        self.assertEquals(self.controlador.obtener_sesion("upepito", "pepito"), None)

        self.assertNotEqual(self.controlador.obtener_sesion(self.usuario_tec, self.passwrd_tec), None)
        self.assertNotEqual(self.controlador.obtener_sesion(self.usuario_doc, self.passwrd_doc), None)