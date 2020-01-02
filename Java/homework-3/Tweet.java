/**
 * Represent a tweet, including the content, author's username
 * and time when it was posted. 
 */
public class Tweet {
    
    public String user;
    public DateTime datetime; 
    public String content;
    
    public Tweet(String user, DateTime datetime, String content) {
            this.user = user; 
            this.datetime = datetime;
            this.content = content;       
    }
    
    public String toString(){
        return "@"+this.user+" ["+datetime.toString()+"]: "+content;
    }
    
    @Override
    public boolean equals(Object o) {
        Tweet other = (Tweet) o;
        if(this.user.equals(other.user) && this.datetime.equals(other.datetime) && this.content.equals(other.content))
            return true;
        else
            return false;
    }
    
    @Override
    public int hashCode() {
        return this.datetime.hashCode() + 10000000*(int)this.user.charAt(0);
    }
}