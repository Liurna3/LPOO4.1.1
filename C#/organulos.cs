using System;

public class Organulos {
	private int cantidadLisosomas;
	private int cantidadPeroxiomas;

	public int GetCantidadPeroxiomas() {
		return this.cantidadPeroxiomas;
	}
	public void SetCantidadPeroxiomas(ref int cantidadPeroxiomas) {
		this.cantidadPeroxiomas = cantidadPeroxiomas;
	}
	public int GetCantidadLisosomas() {
		return this.cantidadLisosomas;
	}
	public void SetCantidadLisosomas(ref int cantidadLisosomas) {
		this.cantidadLisosomas = cantidadLisosomas;
	}

	private Celula celula;

}
