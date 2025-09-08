package pack1;

public class Circulo2D {
    private double x;
    private double y;
    private double radio;

    public Circulo2D() {
        this(0, 0, 1);
    }

    public Circulo2D(double x, double y, double radio) {
        this.x = x;
        this.y = y;
        this.radio = radio;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double getRadio() {
        return radio;
    }

    public double getArea() {
        return Math.PI * radio * radio;
    }

    public double getPerimetro() {
        return 2 * Math.PI * radio;
    }

    public boolean contiene(double x, double y) {
        double distancia = Math.sqrt(Math.pow(this.x - x, 2) + Math.pow(this.y - y, 2));
        return distancia <= radio ;
    }

    public boolean contieneCirculo(Circulo2D circulo) {
        double distancia = Math.sqrt(Math.pow(this.x - circulo.x, 2) + Math.pow(this.y - circulo.y, 2));
        return distancia + circulo.radio <= this.radio;
    }

    public boolean sobrepone(Circulo2D circulo) {
        double distancia = Math.sqrt(Math.pow(this.x - circulo.x, 2) + Math.pow(this.y - circulo.y, 2));
        return distancia < this.radio + circulo.radio;
    }

    public static void main(String[] args) {
        Circulo2D c1 = new Circulo2D(2, 0, 1);
        System.out.printf("Area: %.2f%n", c1.getArea());
        System.out.printf("Perimetro: %.2f%n", c1.getPerimetro());
        System.out.println(c1.contiene(2.5, 0));
        System.out.println(c1.contieneCirculo(new Circulo2D(2, 0, 0.5)));
        System.out.println(c1.sobrepone(new Circulo2D(0, 0, 2)));
    }
}


