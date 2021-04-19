import java.util.ArrayList;
import java.util.Locale;

public class Rotors {

    //I'm using Rotors IV-VIII introduced in 1938/1939
    private String rotorI = "ESOVPZJAYQUIRHXLNFTGKDCMWB";
    private String rotorII = "VZBRGITYUPSDNHLXAWMJQOFECK";
    private String rotorIII = "JPGVOUMFYQBENHZRDKASXLICTW";
    private String rotorIV = "NZJHGRCXMYSWBOUFAIVLPEKQDT";
    private String rotorV = "FKQHTLXOCBJSPDZRAMEWNIUYGV";
    private ArrayList<String[]> rotorConfig = new ArrayList<>();
    String userRotors;

    public Rotors(String userRotors) {
        this.userRotors = userRotors;
    }

    public void setRotorConfig() {

        for (String rotor : this.userRotors.split(" ")) {
            switch (rotor.toUpperCase(Locale.ROOT)) {
                case "I":
                    rotorConfig.add(rotorI.split(""));
                    break;
                case "II":
                    rotorConfig.add(rotorII.split(""));
                    break;
                case "III":
                    rotorConfig.add(rotorIII.split(""));
                    break;
                case "IV":
                    rotorConfig.add(rotorIV.split(""));
                    break;
                case "V":
                    rotorConfig.add(rotorV.split(""));
                    break;
            }
        }
    }

    public ArrayList getRotorConfig() { return this.rotorConfig; }
}
