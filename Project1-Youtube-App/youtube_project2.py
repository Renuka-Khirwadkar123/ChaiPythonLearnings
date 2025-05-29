import json

def load_data():
      try:
        with open("youtube1.txt",'r') as file:
            return json.load(file)
      except FileNotFoundError:
            return []
            
def savedata(videoes):
      with open("youtube1.txt",'w') as file:
            return json.dump(videoes,file)

def list_youtube_video(videoes):
      for index,video in enumerate(videoes,start=1):
            print(f"{index}.{video['name'],video['time']}")
def add_youtube_video(videoes):
     name=input('Enter name of the video')
     time=input('Enter time of the video')
     videoes.append({'name':name,'time':time})
     savedata(videoes)
def update_youtube_video(videoes):
    list_youtube_video(videoes)
    index=input(f"Enter video number: ")
    if 1<=index<=len(videoes):
          name=input("Enter name")
          time=input("Enter time")
          videoes[index-1]={'name':name,'time':time}
          savedata(videoes)
          
def delete_youtube_video(videoes):
        list_youtube_video(videoes)
        index=input(f"Enter video number: ")
        if 1<=index<=len(videoes):
              del videoes[index-1]
def main():
    videoes=load_data()
    while True:
        print("Welcome to youtube manager application")
        print("1. List videos")
        print("2. Add new video")
        print("3.Update video")
        print("4. Delete video")
        print("5.Exit application")
        choice=input("Enter your choice")
    

        match choice:
            
            case '1':
                    list_youtube_video(videoes)
            case '2':
                    add_youtube_video(videoes)
            case '3':
                    update_youtube_video(videoes)
            case '4':
                    delete_youtube_video(videoes)
            case '5':
                break
            case _:
                    print("Invalid choice")

        
if __name__=="__main__":
      main()      
            



