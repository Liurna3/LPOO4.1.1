#!/usr/bin/python
# -*- coding: UTF-8 -*-
import celula
from typing import List

class membranaCelular(object):
	def getToxinasExpulsadas(self) -> int:
		return self.___toxinasExpulsadas

	def setToxinasExpulsadas(self, aToxinasExpulsadas : int) -> None:
		self.___toxinasExpulsadas = aToxinasExpulsadas

	def getNutrientesTransportados(self):
		return self.___nutrientesTransportados

	def setNutrientesTransportados(self, aNutrientesTransportados) -> None:
		self.___nutrientesTransportados = aNutrientesTransportados

	def __init__(self):
		self.___toxinasExpulsadas : int = None
		self.___nutrientesTransportados = None
		self._unnamed_celula_ : celula = None
		"""# @AssociationKind Composition"""

