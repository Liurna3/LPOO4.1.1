#!/usr/bin/python
# -*- coding: UTF-8 -*-
from citoesqueleto import citoesqueleto
from citoplasma import citoplasma
from nucleo import nucleo
from membranaCelular import membranaCelular
from reticuloEndoplasmatico import reticuloEndoplasmatico
from aparatoGolgi import aparatoGolgi
from organulos import organulos
from typing import List

class celula(object):
	def getCitoesqueletos(self) -> citoesqueleto:
		pass

	def setCitoesqueletos(self, aCitoesqueletos : citoesqueleto) -> None:
		pass

	def getCitoplasma(self) -> citoplasma:
		return self.___citoplasma

	def setCitoplasma(self, aCitoplasma : citoplasma) -> None:
		self.___citoplasma = aCitoplasma

	def getNucleo(self) -> nucleo:
		return self.___nucleo

	def setNucleo(self, aNucleo : nucleo) -> None:
		self.___nucleo = aNucleo

	def getMitocondria(self) -> mitocondria:
		return self.___mitocondria

	def setMitocondria(self, aMitocondria : mitocondria) -> None:
		self.___mitocondria = aMitocondria

	def getRibosoma(self) -> ribosoma:
		return self.___ribosoma

	def setRibosoma(self, aRibosoma : ribosoma) -> None:
		self.___ribosoma = aRibosoma

	def getMembranaCelular(self) -> membranaCelular:
		return self.___membranaCelular

	def setMembranaCelular(self, aMembranaCelular : membranaCelular) -> None:
		self.___membranaCelular = aMembranaCelular

	def getReticuloEndoplasmatico(self) -> reticuloEndoplasmatico:
		return self.___reticuloEndoplasmatico

	def setReticuloEndoplasmatico(self, aReticuloEndoplasmatico : reticuloEndoplasmatico) -> None:
		self.___reticuloEndoplasmatico = aReticuloEndoplasmatico

	def getAparatoGolgi(self) -> aparatoGolgi:
		return self.___aparatoGolgi

	def setAparatoGolgi(self, aAparatoGolgi : aparatoGolgi) -> None:
		self.___aparatoGolgi = aAparatoGolgi

	def __init__(self):
		self.___citoesqueletos : citoesqueleto = None
		self.___citoplasma : citoplasma = None
		self.___nucleo : nucleo = None
		self.___mitocondria : mitocondria = None
		self.___ribosoma : ribosoma = None
		self.___membranaCelular : membranaCelular = None
		self.___reticuloEndoplasmatico : reticuloEndoplasmatico = None
		self.___aparatoGolgi : aparatoGolgi = None
		self._unnamed_nucleo_ : nucleo = None
		self._unnamed_membranaCelular_ : membranaCelular = None
		self._unnamed_reticuloEndoplasmatico_ : reticuloEndoplasmatico = None
		self._unnamed_aparatoGolgi_ : aparatoGolgi = None
		self._unnamed_citoplasma_ : citoplasma = None
		self._unnamed_citoesqueleto_ : citoesqueleto = None
		self._unnamed_organulos_ : organulos = None

