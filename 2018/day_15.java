import javafx.util.Pair; 
import java.util.ArrayList; 

public class day_15 {
    static ArrayList<Unit> units;
    
    public static void main(String args[]) {
       
    }
}

class Unit {

    static char type;
    static int hitPoints;
    static Pair coordinate;

    public Unit(char type, Pair coordinate) {
        this.type = type;
        this.coordinate = coordinate;
        this.hitPoints = 200;
    }

    public void attack(Unit other) {
        other.hitPoints -= 3;
    }
}