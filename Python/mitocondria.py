#!/usr/bin/python
# -*- coding: UTF-8 -*-
import organulos
from typing import List

class mitocondria(organulos):
	def getCantidadATP(self) -> int:
		return self.___cantidadATP

	def setCantidadATP(self, aCantidadATP : int) -> None:
		self.___cantidadATP = aCantidadATP

	def __init__(self):
		self.___cantidadATP : int = None

