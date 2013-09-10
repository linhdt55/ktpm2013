package project1;

import static org.junit.Assert.*;

import org.junit.Test;

public class GiaiPTB1Test {

	@Test
	public void PTB1Test1() {
		GiaiPTB1 test1 = new GiaiPTB1();
		
		assertEquals("Nghiem phuong trinh la: ", -1f ,test1.Resulf(1f , 1f), 0f);
	}
	
	@Test
	public void PTB1Test2() {
		GiaiPTB1 test2 = new GiaiPTB1();
		
		assertEquals("Nghiem phuong trinh la: ", 9f , test2.Resulf(10f, -90f) , 0f);
	}
}
