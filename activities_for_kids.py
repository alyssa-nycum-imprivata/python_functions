def run(*kids_names):
    for kid in kids_names:
        print(f"{kid} ran around the playground")

def swing(*kids_names):
    for kid in kids_names:
        print(f"{kid} swang on the swings")

def slide(*kids_names):
    for kid in kids_names:
        print(f"{kid} slide down the slide")

def hide_and_seek(*kids_names):
    for kid in kids_names:
        print(f"{kid} played hide and seek")

run("Pam", "Sam", "Andrea", "Will")
swing("Marybeth", "Ariel", "Kevin", "Courtney")
slide("Mike", "Jack", "Jennifer", "Earl")
hide_and_seek("Henry", "Heather", "Hayley", "Hugh")