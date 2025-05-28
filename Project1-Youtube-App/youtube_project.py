import json

def load_data():
    try:
     with open('youtube.txt','r') as file:
         return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videoes):
    with open('youtube.txt', 'w') as file:
        return json.dump(videoes,file)
    
def list_youtube_videoes(videoes):
    for index,video in enumerate(videoes,start=1):
        print(f"{index}.{video['name']},duration:{video['time']}")

def add_youtube_videoes(videoes):
    name=input("Enter video name")
    time=input("Enter video time")
    videoes.append({'name':name,'time':time})
    save_data_helper(videoes)

def update_youtube_videoes(videoes):
    list_youtube_videoes(videoes)
    index=int(input("Enter number to update"))
    if 1<=index<=len(videoes):
        name=input("Enter new video name.")
        time=input("Enter new video time")
        videoes[index-1]={'name':name,'time':time}
        save_data_helper(videoes)
    else:
        print("Invalid option selected")

def delete_youtube_videoes(videoes):
    list_youtube_videoes(videoes)
    index=int(input("Enter video number"))
    if 1<=index<=len(videoes):
        del videoes[index-1]
        save_data_helper(videoes)
    else:
        print("Invalid option selected")


def main():
    videoes=load_data()
    while True:
        print("\n Youtube videoes application")
        print("1. List all youtube videoes")
        print("2. Add youtube videoes")
        print("3. Update youtube videoes")
        print("4. Delete youtube videoes")
        print("5. Exit the app")
        choice=input("Enter your choice:")
        print(videoes)

        if choice == '1':
            list_youtube_videoes(videoes)
        elif choice == '2':
            add_youtube_videoes(videoes)
        elif choice == '3':
            update_youtube_videoes(videoes)
        elif choice == '4':
            delete_youtube_videoes(videoes)
        elif choice == '5':
            break
        else:
            print("Invalid choice")
        
        
if __name__=="__main__":
    main()           



