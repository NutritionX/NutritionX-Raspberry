package nutritionx.main;

public class Main {

    public Main() {
    }

    public static void main(String[] args) {
        Main main = new Main();
        System.out.println(main.recognize());
    }

    public int recognize() {
        Process process = null;
        try {
            process = Runtime.getRuntime().exec("raspistill -o /home/pi/cam.jpg");
            process.waitFor();
        } catch (Exception e) {
            e.printStackTrace();
        }

        return 0;
    }
}
