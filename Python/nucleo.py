#!/usr/bin/python
# -*- coding: UTF-8 -*-
import celula
from typing import List

class nucleo(object):
	def getCromosoma(self) -> str:
		return self.___cromosoma

	def setCromosoma(self, aCromosoma : str) -> None:
		self.___cromosoma = aCromosoma

	def __init__(self):
		self.___cromosoma : str = None
		self._unnamed_celula_ : celula = None
		"""# @AssociationKind Composition"""

