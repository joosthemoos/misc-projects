 import java.util.Arrays;

public class MergeSort {

  /**
   * Method that merges two sorted halves of a subarray (from Weiss,
   * Data Structures and Algorithm Analysis in Java)
   * 
   * @param a
   *          an array of Comparable items.
   * @param tmpArray
   *          an array to place the merged result.
   * @param leftPos
   *          the left-most index of the subarray.
   * @param rightPos
   *          the index of the start of the second half.
   * @param rightEnd
   *          the right-most index of the subarray.
   */
  private static void merge(Integer[] a, Integer[] tmp, int leftPos, int rightPos, int rightEnd) {

        int aCtr = leftPos;
        int bCtr = rightPos; 
        int cCtr = leftPos; 

        while (aCtr < rightPos && bCtr <= rightEnd) {
            
            if (a[aCtr] <= a[bCtr]) 
                tmp[cCtr++] = a[aCtr++];
            else 
                tmp[cCtr++] = a[bCtr++];
        }
        
        if (aCtr >= rightPos )  // copy remaining elements in right partion 
            while (bCtr <= rightEnd) 
                tmp[cCtr++] = a[bCtr++];

        if (bCtr > rightEnd ) // copy remaining elements in left partion
            while (aCtr < rightPos) 
                tmp[cCtr++] = a[aCtr++]; 
            
        for (int i=leftPos; i<=rightEnd; i++) {
            a[i] = tmp[i];
        }

  }

 
  /* 
   * @param inputArray
   *          an array of Integer items.
   * @param tmpArray
   *          an array to place the merged result.
   * @param left
   *          the left-most index of the subarray.
   * @param rightPos
   *          the start of the right partition.
   * @param right
   *          the right-most index of the subarray.
   */
  private static void mergeSort(Integer[] inputArray) {
      int size = inputArray.length;
      int currentSize;
      Integer[] tmpArray = new Integer[size];
      for (currentSize=1; currentSize < size ; currentSize=currentSize*2) {
          for (int i=0; i < size-1; i = i + currentSize*2) {
              int left = i;
              int rightPos = left + currentSize;
              int right;
              if (i+2*currentSize-1 <= size-1)
                  right=i+2*currentSize-1;
              else
                  right = size-1;
              //System.out.println(Arrays.toString(tmpArray));
              
              if (rightPos <= right)
                  merge(inputArray, tmpArray, left, rightPos, right);
              //System.out.println(Arrays.toString(tmpArray));
              //System.out.println("Init array: "+Arrays.toString(tmpArray));
          }
      }
        // TODO: Write an iterative version of merge sort. There should be no recursive calls!
        return; 
  }

  public static void main(String[] args) {
    Integer[] a = {1,9,2,4,7,8,3,5,0};
    System.out.println(Arrays.toString(a)); 
    MergeSort.mergeSort(a);
    System.out.println(Arrays.toString(a)); 
      
//      Integer[] b = {1,2,3,4,5,6,4};
//      System.out.println(Arrays.toString(b)); 
//      MergeSort.mergeSort(b);
//      System.out.println(Arrays.toString(b)); 
    
     Integer[] c = {11,1,2,3,0,6,8,7,4, 20};
     System.out.println(Arrays.toString(c)); 
     MergeSort.mergeSort(c);
     System.out.println(Arrays.toString(c)); 
  }
}
