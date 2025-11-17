import java.util.Arrays;

class Linea {
    private String color;
    private Persona[] filaPersonas;
    private Cabina[] cabinas;
    private int cantidadCabinas;
    private int indiceFila;
    private int indiceCabinas;

    public Linea(String color) {
        this.color = color;
        this.cantidadCabinas = 10;
        this.filaPersonas = new Persona[100];
        this.cabinas = new Cabina[cantidadCabinas];
        this.indiceFila = 0;
        this.indiceCabinas = 0;
    }

    public void agregarPersona(Persona p) {
        if (indiceFila < filaPersonas.length) {
            filaPersonas[indiceFila] = p;
            indiceFila++;
        }
    }

    public void agregarCabina(int nroca) {
        if (indiceCabinas < cabinas.length) {
            cabinas[indiceCabinas] = new Cabina(nroca);
            indiceCabinas++;
        }
    }

    public String getColor() {
        return color;
    }

    public Persona[] getFilaPersonas() {
        return filaPersonas;
    }

    public Cabina[] getCabinas() {
        return cabinas;
    }

    public int getCantidadCabinas() {
        return cantidadCabinas;
    }

    public float calcularIngresoTotal() {
        float ingreso = 0;
        for (Cabina c : cabinas) {
            if (c != null) {
                for (Persona p : c.getPersonasabordo()) {
                    if (p != null) {
                        if (p.getEdad() < 25 || p.getEdad() > 60) {
                            ingreso += 1.5f;
                        } else {
                            ingreso += 3.0f;
                        }
                    }
                }
            }
        }
        return ingreso;
    }

    public float calcularIngresoRegular() {
        float ingreso = 0;
        for (Cabina c : cabinas) {
            if (c != null) {
                for (Persona p : c.getPersonasabordo()) {
                    if (p != null) {
                        ingreso += 3.0f;
                    }
                }
            }
        }
        return ingreso;
    }

    public boolean todasCabinasCumplen() {
        for (Cabina c : cabinas) {
            if (c != null && !c.cumpleReglas()) {
                return false;
            }
        }
        return true;
    }

    @Override
    public String toString() {
        return "Linea{color='" + color + "', filaPersonas=" + indiceFila + ", cabinas=" + indiceCabinas + ", cantidadCabinas=" + cantidadCabinas + "}";
    }
}