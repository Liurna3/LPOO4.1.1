#!/usr/bin/python
# -*- coding: UTF-8 -*-
import celula
from typing import List

class organulos(object):
	def getCantidadPeroxiomas(self) -> int:
		return self.___cantidadPeroxiomas

	def setCantidadPeroxiomas(self, aCantidadPeroxiomas : int) -> None:
		self.___cantidadPeroxiomas = aCantidadPeroxiomas

	def getCantidadLisosomas(self) -> int:
		return self.___cantidadLisosomas

	def setCantidadLisosomas(self, aCantidadLisosomas : int) -> None:
		self.___cantidadLisosomas = aCantidadLisosomas

	def __init__(self):
		self.___cantidadLisosomas : int = None
		self.___cantidadPeroxiomas : int = None
		self._unnamed_celula_ : celula = None
		"""# @AssociationKind Composition"""

