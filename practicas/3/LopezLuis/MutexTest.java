import java.util.concurrent.Semaphore;
import java.util.concurrent.ThreadLocalRandom;

public class MutexTest {
   static Semaphore semaphore = new Semaphore(1);

   static class MyThread extends Thread {
      boolean lock;
      char c = ' ';

      MyThread(boolean lock, char c) {
         this.lock = lock;
         this.c = c;
      }

      public void run() {
         try {
            // Generate a random number between 0 & 50
            // The random nbr is used to simulate the "unplanned"
            // execution of the concurrent code
            int randomNbr = ThreadLocalRandom.current().nextInt(0, 50 + 1);

            for (int j=0; j<10; ++j) {
               if(lock) semaphore.acquire();
               try {
                  for (int i=0; i<5; ++i) {
                     System.out.print(c);
                     Thread.sleep(randomNbr);
                  }
               } finally {
                  if(lock) semaphore.release();
               }
               System.out.print('|');
            }
         } catch (InterruptedException e) {
            e.printStackTrace();
         }
      }
   }

   public static void main(String[] args) throws Exception {
      System.out.println("Without Locking:");
      MyThread th1 = new MyThread(false, '$');
      th1.start();
      MyThread th2 = new MyThread(false, '#');
      th2.start();
      
      th1.join();
      th2.join();

      System.out.println('\n');

      System.out.println("With Locking:");
      MyThread th3 = new MyThread(true, '$');
      th3.start();
      MyThread th4 = new MyThread(true, '#');
      th4.start();
      
      th3.join();
      th4.join();

      System.out.println('\n');
   }
}