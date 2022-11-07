using System;

public class AparatoGolgi {
	private int proteinaGenerada;
	private String lipidosGenerados;

	public int GetProteinaGenerada() {
		return this.proteinaGenerada;
	}
	public void SetProteinaGenerada(ref int proteinaGenerada) {
		this.proteinaGenerada = proteinaGenerada;
	}
	public void GetLipidosGenerados() {
		return this.lipidosGenerados;
	}
	public void SetLipidosGenerados(ref object lipidosGenerados) {
		this.lipidosGenerados = lipidosGenerados;
	}

	private Celula celula;

}
