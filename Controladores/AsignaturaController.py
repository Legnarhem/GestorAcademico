# encoding=UTF-8
"""Módulo AsignaturaController del paquete Controladores
"""
__author__ = 'Gregorio y Ángel'
from Almacen import *
from UtilExpedientes import *


class AsignaturaController:
    """Esta clase es un controlador de la entidad Asignatura.
    Args:
        terminales (list<Terminal): Lista de terminales/vistas asociadas al controlador
    """
    def __init__(self, terminales):
        self.__terminales = terminales

    @staticmethod
    def get_almacen():
        """Obtiene una instancia de Almacen.
        :return:Instancia de Almacen (Almacen)
        """
        return Almacen.getInstance()

    def obtener_asigs_grado(self, codigo, sesion):
        """Obtiene una lista de las asignaturas asociadas al grado/curso indicado, si el usuario
        conectado al gestor académico tiene acceso.
        :param codigo:Codigo de grado/curso (int)
        :param sesion:Sesion del usuario conectado al gestor académico (Sesion)
        :return:Lista de asignaturas asociadas (list) si existen o None en caso contrario o de carencia de privilegios
        """
        if sesion.getTipo() == "TecnicoCalidad":
            return self.get_almacen().listarAsignaturasGrado(Grado(codigo, None, None))
        return None

    def obtener_media(self, codigo, sesion):
        """Obtiene la media global de una asignatura indicada, si el usuario conectado al gestor académico tiene acceso.
        :param codigo:Codigo de asignatura (int)
        :param sesion:Sesion del usuario conectado al gestor académico (Sesion)
        :return:Media global de asignatura (float) si existe o None en caso contrario o de carencia de privilegios
        """
        apto = False
        asignatura = Asignatura(codigo, None)
        if sesion.getTipo() == "TecnicoCalidad":
            apto = True
        elif sesion.getTipo() == "Docente":
            if asignatura in self.get_almacen().listarAsignaturasDocente(
                    Docente(None, None, sesion.getDNI(), None, None)):
                apto = True
        return UtilExpedientes().getMediaExpedientes(
            self.get_almacen().listarExpedientesAsignatura(asignatura)) if apto else None

    def obtener_rango(self, codigo, sesion):
        """Obtiene el rango de notas de los distintos expedientes asociados a la asignatura indicada
        que es accesible por el usuario conectado al gestor academico.
        :param codigo:Codigo de asignatura (int)
        :param sesion:Sesion del usuario conectado al gestor académico (Sesion)
        :return:Rango de notas (Rango) si existe o None en caso contrario o de carencia de privilegios
        """
        apto = False
        asignatura = Asignatura(codigo, None)
        if sesion.getTipo() == "TecnicoCalidad":
            apto = True
        elif sesion.getTipo() == "Docente":
            if asignatura in self.get_almacen().listarAsignaturasDocente(
                    Docente(None, None, sesion.getDNI(), None, None)):
                apto = True
        return UtilExpedientes().getRangosExpedientes(
            self.get_almacen().listarExpedientesAsignatura(asignatura)) if apto else None

    def listar(self, sesion):
        """Obtiene una lista de todos las asignaturas a las que el usuario conectado al gestor académico tiene acceso.
        :param sesion:Sesion del usuario conectado al gestor académico (Sesion)
        :return:Lista de asignaturas (list) si existen o None en caso contrario o de carencia de privilegios
        """
        if sesion.getTipo() == "TecnicoCalidad":
            return self.get_almacen().listarAsignaturasCentro()
        elif sesion.getTipo() == "Docente":
            return self.get_almacen().listarAsignaturasDocente(Docente(None, None, sesion.getDNI(), None, None))
        return None


