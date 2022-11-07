#!/usr/bin/python
# -*- coding: UTF-8 -*-
import celula
from typing import List

class citoesqueleto(object):
	def getDensidadFIbras(self) -> int:
		return self.___densidadFIbras

	def setDensidadFIbras(self, aDensidadFIbras : int) -> None:
		self.___densidadFIbras = aDensidadFIbras

	def __init__(self):
		self.___densidadFIbras : int = None
		self._unnamed_celula_ : celula = None
		"""# @AssociationKind Composition"""

