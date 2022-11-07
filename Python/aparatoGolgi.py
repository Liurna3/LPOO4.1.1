#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class aparatoGolgi(object):
	def getProteinaGenerada(self) -> int:
		return self.___proteinaGenerada

	def setProteinaGenerada(self, aProteinaGenerada : int):
		self.___proteinaGenerada = aProteinaGenerada

	def getLipidosGenerados(self):
		return self.___lipidosGenerados

	def setLipidosGenerados(self, aLipidosGenerados):
		self.___lipidosGenerados = aLipidosGenerados

	def __init__(self):
		self.___proteinaGenerada : int = None
		self.___lipidosGenerados = None
		"""# @AssociationKind Composition"""

