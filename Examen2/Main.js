public class Main {
	public static void main(String[] args) {
	    MiTeleferico teleferico = new MiTeleferico();


	    teleferico.agregarLinea("Roja");
	    teleferico.agregarLinea("verde");
	    teleferico.agregarLinea("Amarilla")

	 
	    teleferico.agregarCabina("Roja");
	    teleferico.agregarCabina("Roja");

	  
	    Persona p1 = new Persona("pao", 20);
	    Persona p2 = new Persona("juan", 30);
	    teleferico.agregarPersonaFila(p1, "Roja");
	    teleferico.agregarPersonaFila(p2, "verde");

	  
	    System.out.println(teleferico);
	}
