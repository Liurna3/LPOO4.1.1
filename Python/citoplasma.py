#!/usr/bin/python
# -*- coding: UTF-8 -*-
import celula
from typing import List

class citoplasma(object):
	def getCantidadSal(self) -> int:
		return self.___cantidadSal

	def setCantidadSal(self, aCantidadSal : int) -> None:
		self.___cantidadSal = aCantidadSal

	def getCantidadAgua(self) -> int:
		return self.___cantidadAgua

	def setCantidadAgua(self, aCantidadAgua : int) -> None:
		self.___cantidadAgua = aCantidadAgua

	def __init__(self):
		self.___cantidadSal : int = None
		self.___cantidadAgua : int = None
		self._unnamed_celula_ : celula = None
		"""# @AssociationKind Composition"""

