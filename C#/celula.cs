using System;

public class Celula {
	private Citoesqueleto[] citoesqueletos;
	public Citoesqueleto[] Citoesqueletos {
		get {
			return citoesqueletos;
		}
		set {
			citoesqueletos = value;
		}
	}
	private Citoplasma citoplasma;
	private Nucleo nucleo;
	private Mitocondria mitocondria;
	private Ribosoma ribosoma;
	private MembranaCelular membranaCelular;
	private ReticuloEndoplasmatico reticuloEndoplasmatico;
	private AparatoGolgi aparatoGolgi;

	public Citoesqueleto GetCitoesqueletos() {
		return this.citoesqueletos;
	}
	public void SetCitoesqueletos(ref Citoesqueleto citoesqueletos) {
		this.citoesqueletos = citoesqueletos;
	}
	public Citoplasma GetCitoplasma() {
		return this.citoplasma;
	}
	public void SetCitoplasma(ref Citoplasma citoplasma) {
		this.citoplasma = citoplasma;
	}
	public Nucleo GetNucleo() {
		return this.nucleo;
	}
	public void SetNucleo(ref Nucleo nucleo) {
		this.nucleo = nucleo;
	}
	public Mitocondria GetMitocondria() {
		return this.mitocondria;
	}
	public void SetMitocondria(ref Mitocondria mitocondria) {
		this.mitocondria = mitocondria;
	}
	public Ribosoma GetRibosoma() {
		return this.ribosoma;
	}
	public void SetRibosoma(ref Ribosoma ribosoma) {
		this.ribosoma = ribosoma;
	}
	public MembranaCelular GetMembranaCelular() {
		return this.membranaCelular;
	}
	public void SetMembranaCelular(ref MembranaCelular membranaCelular) {
		this.membranaCelular = membranaCelular;
	}
	public ReticuloEndoplasmatico GetReticuloEndoplasmatico() {
		return this.reticuloEndoplasmatico;
	}
	public void SetReticuloEndoplasmatico(ref ReticuloEndoplasmatico reticuloEndoplasmatico) {
		this.reticuloEndoplasmatico = reticuloEndoplasmatico;
	}
	public AparatoGolgi GetAparatoGolgi() {
		return this.aparatoGolgi;
	}
	public void SetAparatoGolgi(ref AparatoGolgi aparatoGolgi) {
		this.aparatoGolgi = aparatoGolgi;
	}

	private Citoesqueleto citoesqueleto;
	private Organulos organulos;

}
