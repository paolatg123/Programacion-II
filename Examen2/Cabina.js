import java.util.Arrays;

class Cabina {
    private int nroncabina;
    private Persona[] personasabordo;
    private int capacidad;

    public Cabina(int nroncabina) {
        this.nroncabina = nroncabina;
        this.capacidad = 10;
        this.personasabordo = new Persona[capacidad];
    }

    public boolean agregarPersona(Persona p) {
        for (int i = 0; i < personasabordo.length; i++) {
            if (personasabordo[i] == null) {
                personasabordo[i] = p;
                return true;
            }
        }
        return false;
    }

    public int getNroncabina() {
        return nroncabina;
    }

    public Persona[] getPersonasabordo() {
        return personasabordo;
    }

    public float getPesoTotal() {
        float pesoTotal = 0;
        for (Persona p : personasabordo) {
            if (p != null) {
                pesoTotal += p.getPesoPersona();
            }
        }
        return pesoTotal;
    }

    public int getCantidadPersonas() {
        int count = 0;
        for (Persona p : personasabordo) {
            if (p != null) {
                count++;
            }
        }
        return count;
    }

    public boolean cumpleReglas() {
        return getCantidadPersonas() <= 10 && getPesoTotal() <= 850;
    }

    @Override
    public String toString() {
        return "Cabina{nroncabina=" + nroncabina + ", personasabordo=" + Arrays.toString(personasabordo) + "}";
    }
}
