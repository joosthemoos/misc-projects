/**
 * Represent a timestamp consisting of a date (day/month/year) and time 
 * in hours and minutes (24h format.
 */
public class DateTime implements Comparable<DateTime> { //For part 4
    
    public int year;
    public int month;
    public int day; 
    public int hours;
    public int minutes;    
    public int seconds;
    public boolean pm; 

    
    public DateTime(int year, int day, int month, int h, int m) {        
        this.year = year; 
        this.month = month; 
        this.day = day;     
        this.hours = h; 
        this.minutes = m;                
    }
    
    public DateTime(String datetime) {
        String[] fields = datetime.split(" ");
        String[] dateFields = fields[0].split("/");
        month = Integer.parseInt(dateFields[0]);
        day = Integer.parseInt(dateFields[1]);
        year = Integer.parseInt(dateFields[2]);
        
        String[] timeFields = fields[1].split(":"); 
        hours = Integer.parseInt(timeFields[0]);
        minutes = Integer.parseInt(timeFields[1]);;
    }
    
    public int compareTo(DateTime other) { //should return true if this one is newer than the one compared to. this is wrong and needs to be fixed.
            if (year == other.year) {
                if (month == other.month) {
                    if (day == other.day) {
                        if (hours == other.hours) {
                            if (minutes == other.minutes) {
                                return 0;
                            }
                            else if (minutes < other.minutes) {
                                return -1;
                            }
                            else
                                return 1;
                        }
                        else if(hours < other.hours) {
                            return -1;
                        }
                        else
                            return 1;
                    }
                    else if (day < other.day) {
                        return -1;
                    }
                    else
                        return 1;
                }
                else if (month < other.month) {
                    return -1;
                }
                else
                    return 1;
            }
        else if (year < other.year) {
            return -1;
        }
        else 
            return 1;
           

               
    }
    
    public String toString() {
        return Integer.toString(month)+"/"+Integer.toString(day)+"/"+Integer.toString(year)+"  "+
            String.format("%02d" , hours)+":"+String.format("%02d", minutes);
    }   
    
    @Override
    public boolean equals(Object o) {
        DateTime other = (DateTime) o;
        if (this.compareTo(other)==0) {
            return true;
        }
        else
            return false;
    }
    
    
    @Override
    public int hashCode() {
        return (525600*year+43800*month+1440*day+60*hours+minutes);
    }
    
}