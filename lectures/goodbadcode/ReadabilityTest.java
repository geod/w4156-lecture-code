

public class BadCode {

    public int calculateFoo(int x, int y, boolean increment){
        if(increment)
            x++;
            x *= 2;

        x += y;
        return x;
    }

    @Test
    public void test(){
        assertEquals(calculateFoo(3, 5, True), 13);
        assertEquals(calculateFoo(3, 5, False), 8);
    }

}