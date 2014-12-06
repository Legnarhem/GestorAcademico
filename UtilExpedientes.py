# encoding=UTF-8
__author__ = 'Gregorio y Ángel'
from Entidades.Resumen import *
from Entidades.Rango import *
from Entidades.MatriculasYMenciones import *

class UtilExpedientes:

    NOTA_MATRICULAS = 10
    NOTA_MENCION = 9.5

    NOTA_APROBADOS = 5
    NOTA_NOTABLES = 7
    NOTA_SOBRESALIENTES = 9
    NOTA_LIMITE = 10

    def getMatriculasYMenciones(self, expedientes):
        mat = 0
        men = 0
        for e in expedientes:
            m = self.getMediaExpediente(e)
            if self.NOTA_MENCION <= m <= self.NOTA_MATRICULAS:
                men += 1
            elif m == self.NOTA_MATRICULAS:
                mat += 1
        return MatriculasYMenciones(mat, men)

    def getMediaExpediente(self, expediente):
        notaAcumulada = 0
        nNotas = 0
        for n in expediente.getNotas():
            notaAcumulada += float(n)
            nNotas += 1
        return float(notaAcumulada/nNotas)

    def getMediaExpedientes(self, expedientes):
        mediaAcumulada = 0
        nExpedientes = 0
        for e in expedientes:
            mediaAcumulada+=self.getMediaExpediente(e)
            nExpedientes += 1
        return float(mediaAcumulada/nExpedientes)

    def getRangosExpedientes(self, expedientes):
        suspensos = 0
        aprobados = 0
        notables = 0
        sobresalientes = 0
        for e in expedientes:
            media = self.getMediaExpediente(e)
            if media <= self.NOTA_APROBADOS:
                suspensos += 1
            elif self.NOTA_APROBADOS <= media < self.NOTA_NOTABLES:
                aprobados += 1
            elif self.NOTA_NOTABLES <= media < self.NOTA_SOBRESALIENTES:
                notables += 1
            elif self.NOTA_SOBRESALIENTES <= media <= self.NOTA_LIMITE:
                sobresalientes += 1
        return Rango(suspensos,aprobados,notables,sobresalientes)

    def getResumen(self, expedientes):
        asignaturas = dict()
        notaAlumnoAcumulada = 0
        notaAsignaturaAcumulada = 0
        nExpedientes = 0
        for e in expedientes:
            asig = e.getAsignatura().getCodigo()
            if asig not in asignaturas:
                asignaturas[asig]=[]
            asignaturas[asig].append(e)
        for asig in asignaturas.keys():
            l = list(asignaturas.get(asig))
            for exp in l:
                notaAlumnoAcumulada += self.getMediaExpediente(exp)
            notaAsignaturaAcumulada += self.getMediaExpedientes(l)
            nExpedientes += len(l)
        return Resumen(float(notaAlumnoAcumulada/nExpedientes),float(notaAsignaturaAcumulada/len(asignaturas.keys())))