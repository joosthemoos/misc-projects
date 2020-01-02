import java.io.BufferedReader;
import java.io.IOException;

/**
 * A simple reader for CSV files. 
 */
public class CsvReader {
    
    BufferedReader reader; 
    int bestSize = 10; // Default number of columns
    
    
    /**
     * Create a new CsvReader object. 
     * @param  br  A java.util.BufferedReader instance. 
     */
    public CsvReader(BufferedReader br) {
        reader = br;
    }
    
    private String[] adjustArray(String[] old, int size) {
                    String[] result = new String[size];
                    for (int j=0;j<Math.min(size, old.length);j++)
                        result[j] = old[j];
                    return result;
    }
   
    /**
     * Return the data fields in the next line. 
     * 
     * @return A String[] containing the data fields in the next line. 
     */
    public String[] nextLine() throws IOException {
        
        String[] result = new String[bestSize];
                
        String line = reader.readLine();
        
        if (line==null) 
            return null;
        
        Character c;
       
      
        int currentField = 0;
        int currentStart = 0;
        String field = "";
       
        boolean inQuote = false;
        for (int i = 0;i < line.length(); i++){
            c = line.charAt(i);
            
            if (!inQuote && c == ',') {
                
                if (currentField == bestSize) { // resize array if necessary
                    bestSize = bestSize*2;
                    result = adjustArray(result, bestSize);
                }
                field = line.substring(currentStart,i);
                if (field.charAt(0)=='"' && field.charAt(field.length()-1)=='"')
                    field = field.substring(1,field.length()-1);
                result[currentField++] = field;
                currentStart = i+1;
            } else if (!inQuote && c == '"') {
                inQuote = true;
            } else if (inQuote && c=='"' && (i==0 || line.charAt(i-1)!='\\')) {
                inQuote = false;
            }
            
        }
        if (currentField == bestSize) { // resize array if necessary
             bestSize = bestSize+1;
             result = adjustArray(result, bestSize);
        }
        field = line.substring(currentStart,line.length());
        if (field.charAt(0)=='"' && field.charAt(field.length()-1)=='"')
            field = field.substring(1,field.length()-1);
        result[currentField++] = field;
                                             
        if (currentField < bestSize)  {
            bestSize = currentField;
            result = adjustArray(result, currentField);
        }
        return result;                                            
        
    }
    
    
}