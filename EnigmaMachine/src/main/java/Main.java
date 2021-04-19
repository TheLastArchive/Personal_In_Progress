import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Locale;
import java.util.Scanner;

public class Main {

    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        String userRotors;
        do {
            System.out.println("Rotor combination (eg: IV V II): ");
            userRotors = scanner.nextLine();
        } while (!rotorValidation(userRotors));

        Rotors rotors = new Rotors(userRotors);
        rotors.setRotorConfig();

        System.out.println("Starting positions (eg: 15 20 9): ");
        String userStartPositions = scanner.nextLine();

    }

    /**
     * Ensures that the rotors entered by the user are all unique and within range
     * @param userRotors the input from the user
     * @return boolean whether the solution is valid or not
     */
    private static boolean rotorValidation(String userRotors) {
        ArrayList<String> possibleValues = new ArrayList<>(Arrays.asList("I", "II", "III", "IV", "V"));

        for (String rotor : userRotors.split(" ")) {
            if (possibleValues.contains(rotor.toUpperCase(Locale.ROOT))) {
                possibleValues.remove(rotor);
            }
            else {
                System.out.println("Incompatible rotor configuration");
                return false;
            }
        }
        return true;
    }
}
