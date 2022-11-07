using System;

public class Ribosoma : Organulos  {
	private int cantidadARN;
	private int cantidadProteina;

	public int GetCantidadARN() {
		return this.cantidadARN;
	}
	public void SetCantidadARN(ref int cantidadARN) {
		this.cantidadARN = cantidadARN;
	}
	public int GetCantidadProteina() {
		return this.cantidadProteina;
	}
	public void SetCantidadProteina(ref int cantidadProteina) {
		this.cantidadProteina = cantidadProteina;
	}

}
