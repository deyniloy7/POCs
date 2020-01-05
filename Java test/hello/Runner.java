import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Runner {

    public static void main(String[] args) {
        List<Laptop> laps = new ArrayList<Laptop>();

        laps.add(new Laptop("Dell", 16, 800));
        laps.add(new Laptop("Apple", 8, 1200));
        laps.add(new Laptop("Acer", 12, 700));

        Comparator<Laptop> com = new Comparator<Laptop>() {
            public int compare(Laptop lap1, Laptop lap2){
                if(lap1.getPrice() > lap2.getPrice()){
                    return 1;
                } else {
                    return -1;
                }
            }
        };

        for(Laptop l : laps) {
            System.out.println(l);
        }

        Collections.sort(laps, com);


        for(Laptop l : laps) {
            System.out.println(l);
        }
    }
}