#!/usr/bin/python
# -*- coding: UTF-8 -*-
import organulos
from typing import List

class ribosoma(organulos):
	def getCantidadARN(self) -> int:
		return self.___cantidadARN

	def setCantidadARN(self, aCantidadARN : int) -> None:
		self.___cantidadARN = aCantidadARN

	def getCantidadProteina(self) -> int:
		return self.___cantidadProteina

	def setCantidadProteina(self, aCantidadProteina : int) -> None:
		self.___cantidadProteina = aCantidadProteina

	def __init__(self):
		self.___cantidadARN : int = None
		self.___cantidadProteina : int = None

