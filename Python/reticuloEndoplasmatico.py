#!/usr/bin/python
# -*- coding: UTF-8 -*-
import celula
from typing import List

class reticuloEndoplasmatico(object):
	def getDensidad(self) -> float:
		return self.___densidad

	def setDensidad(self, aDensidad : float) -> None:
		self.___densidad = aDensidad

	def __init__(self):
		self.___densidad : float = None
		self._unnamed_celula_ : celula = None
		"""# @AssociationKind Composition"""

