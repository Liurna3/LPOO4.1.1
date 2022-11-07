using System;

public class MembranaCelular {
	private int toxinasExpulsadas;
	private String nutrientesTransportados;

	public int GetToxinasExpulsadas() {
		return this.toxinasExpulsadas;
	}
	public void SetToxinasExpulsadas(ref int toxinasExpulsadas) {
		this.toxinasExpulsadas = toxinasExpulsadas;
	}
	public void GetNutrientesTransportados() {
		return this.nutrientesTransportados;
	}
	public void SetNutrientesTransportados(ref object nutrientesTransportados) {
		this.nutrientesTransportados = nutrientesTransportados;
	}

	private Celula celula;

}
