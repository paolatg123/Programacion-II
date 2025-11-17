import java.util.Arrays;

class MiTeleferico {
    private Linea[] lineas;
    private float cantidadIngreso;
    private MiTeleferico[] miteleferico;
    private int indiceLineas;

    public MiTeleferico() {
        this.lineas = new Linea[10];
        this.cantidadIngreso = 0.0f;
        this.miteleferico = new MiTeleferico[10];
        this.indiceLineas = 0;
    }

    public void agregarPersonaFila(Persona p, String linea) {
        for (int i = 0; i < indiceLineas; i++) {
            if (lineas[i] != null && lineas[i].getColor().equals(linea)) {
                lineas[i].agregarPersona(p);
                return;
            }
        }
    }

    public void agregarCabina(String linea) {
        for (int i = 0; i < indiceLineas; i++) {
            if (lineas[i] != null && lineas[i].getColor().equals(linea)) {
                int nroca = lineas[i].getCabinas().length + 1;
                lineas[i].agregarCabina(nroca);
                return;
            }
        }
    }

    public boolean agregarPrimeraPersonaACabina(Persona p, String linea, int nroCabina) {
        for (int i = 0; i < indiceLineas; i++) {
            if (lineas[i] != null && lineas[i].getColor().equals(linea)) {
                Cabina[] cabinas = lineas[i].getCabinas();
                for (Cabina c : cabinas) {
                    if (c != null && c.getNroncabina() == nroCabina) {
                        if (c.getCantidadPersonas() == 0 && c.agregarPersona(p)) {
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }

    public boolean todasCabinasCumplen() {
        for (Linea l : lineas) {
            if (l != null && !l.todasCabinasCumplen()) {
                return false;
            }
        }
        return true;
    }

    public float calcularIngresoTotal() {
        float total = 0;
        for (Linea l : lineas) {
            if (l != null) {
                total += l.calcularIngresoTotal();
            }
        }
        return total;
    }

    public String lineaConMasIngresoRegular() {
        String lineaMax = null;
        float maxIngreso = 0;
        for (Linea l : lineas) {
            if (l != null) {
                float ingreso = l.calcularIngresoRegular();
                if (ingreso > maxIngreso) {
                    maxIngreso = ingreso;
                    lineaMax = l.getColor();
                }
            }
        }
        return lineaMax;
    }

    public Linea[] getLineas() {
        return lineas;
    }

    public float getCantidadIngreso() {
        return cantidadIngreso;
    }

    public void setCantidadIngreso(float cantidadIngreso) {
        this.cantidadIngreso = cantidadIngreso;
    }

    public MiTeleferico[] getMiteleferico() {
        return miteleferico;
    }

    @Override
    public String toString() {
        return "MiTeleferico{lineas=" + Arrays.toString(lineas) + ", cantidadIngreso=" + cantidadIngreso + ", miteleferico=" + Arrays.toString(miteleferico) + "}";
    }

}
