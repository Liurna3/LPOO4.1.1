using System;

public class Citoplasma {
	private int cantidadSal;
	private int cantidadAgua;

	public int GetCantidadSal() {
		return this.cantidadSal;
	}
	public void SetCantidadSal(ref int cantidadSal) {
		this.cantidadSal = cantidadSal;
	}
	public int GetCantidadAgua() {
		return this.cantidadAgua;
	}
	public void SetCantidadAgua(ref int cantidadAgua) {
		this.cantidadAgua = cantidadAgua;
	}

	private Celula celula;

}
