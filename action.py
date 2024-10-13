import datetime
import speak
import webbrowser
import weather
import os
import random




def Action(send) :   
  
    data_btn  = send.lower()

    if "what is your name" in   data_btn :
      speak.speak("my name is virtual Assistant")  
      return "my name is virtual Assistant"

    elif "hello" in data_btn  or "hye" in data_btn  or "hay" in data_btn: 
        speak.speak("Hey , How i can  help you !")  
        return "Hey , How i can  help you !" 

    elif "how are you" in  data_btn :
            speak.speak("I am doing great these days ") 
            return "I am doing great these days "   

    elif "thanku" in data_btn or "thank" in data_btn:
           speak.speak("its my pleasure  to stay with you")
           return "its my pleasure  to stay with you"      

    elif "good morning" in data_btn:
           speak.speak("Good morning , i think you might need some help")
           return "Good morning , i think you might need some help"   

    elif "time now" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time) 

    elif "shutdown" in data_btn or "quit" in data_btn:
            speak.speak("Okay, shutting down.")
            return "ok "  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")   
        speak.speak("gaana.com is now ready for you, enjoy your music")                   
        return "gaana.com is now ready for you, enjoy your music"


    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("google open")  
        return "google open"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open") 
        return "YouTube open"    
    
    elif 'weather' in data_btn :
       ans   = weather.Weather()
       speak.speak(ans) 
       return ans

    elif 'tell me a joke' in data_btn:
        jokes = [
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't skeletons fight each other? They don't have the guts.",
            "What do you call fake spaghetti? An impasta!"
        ]
        joke = random.choice(jokes)
        speak.speak(joke)
        return joke

    else :
        speak.speak( "i'm able to understand!")
        return "i'm able to understand!"       
