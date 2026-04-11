import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import time
import datetime
import pygame

script_dir = os.path.dirname(os.path.abspath(__file__))  
sound_file = os.path.join(script_dir, "music.mp3")

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    
    if not os.path.exists(sound_file):
        print(f"❌ Error: {sound_file} file nahi mila!")
        return
    
    is_running = True 
    alarm_triggered = False  
    
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, end="\r") 

        if current_time == alarm_time and not alarm_triggered:
            print("\n🔔 WAKE UP! WAKE UP! WAKE UP!")    
            alarm_triggered = True
            
            try:
                pygame.mixer.init()
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play(-1)  
                
                time.sleep(10)
                
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                
                is_running = False
                
            except Exception as e:
                print(f"❌ Sound error: {e}")
                is_running = False
        
        time.sleep(0.5) 


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS) [24-hour format]: ")
    set_alarm(alarm_time)