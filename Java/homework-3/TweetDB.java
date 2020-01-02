import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap; 
import java.util.TreeMap; 
import java.util.ArrayList;
import java.util.Map;
import java.util.List;
import java.util.SortedMap;
import java.util.HashSet;

public class TweetDB {
   
    
    HashMap<String, List<Tweet>> tweetsPerUser;
    HashMap<String, List<Tweet>> tweetsPerKeyword;  
    TreeMap<DateTime, List<Tweet>> tweetsByTime;
    String[] currLine;
    Tweet thisTweet;
    List<Tweet> tweets;
    
    public TweetDB(String pathToFile) throws FileNotFoundException, IOException {
        BufferedReader tweetReader = new BufferedReader(new FileReader(pathToFile));
        CsvReader betterTweetReader = new CsvReader(tweetReader); 
        tweetsPerUser = new HashMap<>();               
        tweetsPerKeyword = new HashMap<>();   
        tweetsByTime = new TreeMap<>();   
        
        while ((currLine = betterTweetReader.nextLine())!=null) {
            tweets = new ArrayList<Tweet>();
            DateTime date = new DateTime(currLine[2]);
            //System.out.println("it got to here!");
            Tweet thisTweet = new Tweet(currLine[0], date, currLine[1]);
            
            //tweets.add(thisTweet);
            //System.out.print("it got to here!");
            if (!tweetsPerUser.containsKey(thisTweet.user)) {
               tweetsPerUser.put(thisTweet.user,tweets); //I need to figure out if i can just call user like that????
            }
            tweetsPerUser.get(thisTweet.user).add(thisTweet);
            
            
            String[] keywords = keywordList(thisTweet.content);
            tweets = new ArrayList<Tweet>();
            for (String n : keywords) {
                if (!tweetsPerKeyword.containsKey(n)) {
                    tweetsPerKeyword.put(n, tweets);
                }
                tweetsPerKeyword.get(n).add(thisTweet);
            }
            tweets = new ArrayList<Tweet>();
            if (!tweetsByTime.containsKey(thisTweet.datetime)) {
                tweetsByTime.put(thisTweet.datetime, tweets);
           }
            tweetsByTime.get(thisTweet.datetime).add(thisTweet);
        }

        //while ((thisTweet = tweets.get(i)) != null) {
            
        //}
        
        
    } 
    
    public String[] keywordList(String contents) {
        String content = contents;
        //System.out.println("before replacement");
        //content.replaceAll(",","");
        //content.replaceAll(".","");
        //content.replaceAll("!","");
        //content.replaceAll("@","");
        //content.replaceAll("#","");
        //System.out.println("it got to here?");
        //content.replaceAll("\\?","");
        //System.out.println("it replaced!");
        content.replaceAll("\\p{Punct}^[@]^[_]","");
        String[] keywords = content.split(" ");
        return keywords;
    }
    
    
    
    public List<Tweet> getTweetsByUser(String user) {
        List<Tweet> userTweets = new ArrayList<Tweet>();
        List<Tweet> betterTweets = new ArrayList<Tweet>();
        if (tweetsPerUser.containsKey(user)) {
            userTweets = tweetsPerUser.get(user);  
        }
        else 
            return null;
        HashSet<Tweet> tempSet = new HashSet<Tweet>();
        for (Tweet t : userTweets) {
            //if (! tempSet.contains(t))
                tempSet.add(t);
        }
        betterTweets = new ArrayList<Tweet>(tempSet);
        
        return betterTweets;
    }
    
    
    
    public List<Tweet> getTweetsByKeyword(String kw) {
        List<Tweet> keywordTweets = new ArrayList<Tweet>();
        List<Tweet> betterTweets = new ArrayList<Tweet>();
        if (tweetsPerKeyword.containsKey(kw)) {
            keywordTweets = tweetsPerKeyword.get(kw);
        }
        
        HashSet<Tweet> tempSet = new HashSet<Tweet>();
        for (Tweet t : keywordTweets) {
            //if (! tempSet.contains(t))
                tempSet.add(t);
        }
        betterTweets = new ArrayList<Tweet>(tempSet);
        
        return betterTweets;
        //return keywordTweets; 
    }
    
    
     public List<Tweet> getTweetsInRange(DateTime start, DateTime end) {
         //System.out.print(start.day);
         List<Tweet> theRangeOfTweets = new ArrayList<Tweet>();
         List<Tweet> betterTweets = new ArrayList<Tweet>();
         //System.out.print(tweetsByTime);
         //System.out.print(tweetsByTime.subMap(start, end));
         for (DateTime datim : tweetsByTime.subMap(start, end).keySet()) {
             for (Tweet n : tweetsByTime.get(datim)) {
                 theRangeOfTweets.add(n);
             }
             
         }
        HashSet<Tweet> tempSet = new HashSet<Tweet>();
        for (Tweet t : theRangeOfTweets) {
            //if (! tempSet.contains(t))
                tempSet.add(t);
        }
        betterTweets = new ArrayList<Tweet>(tempSet);
         return betterTweets; // replace this 
    }  
    
    public static void main(String[] args) {
          
        try {
            TweetDB tdb = new TweetDB("coachella_tweets.csv");

//            Part 1: Search by username 
//             for(Tweet t : tdb.getTweetsByUser("hannah_frog"))
//                 System.out.println(t);
            
              
// //             Part 2: Search by keyword
             for(Tweet t : tdb.getTweetsByKeyword("coachella"))
                 System.out.println(t);
            
            
//            //Part 3: Search by date/time interval          
//             for(Tweet t : tdb.getTweetsInRange(new DateTime("1/7/15 00:00"), new DateTime("1/7/15 5:00")))
//                 System.out.println(t);
             //   while(true)
             //
             //System.out.println("congrats! it works!");   
            
        } catch (FileNotFoundException e) {
            System.out.println(".csv File not found.");
        } catch (IOException e) {
            System.out.println("Error reading from .csv file.");
        }
        
        
        
        
    }
    
}