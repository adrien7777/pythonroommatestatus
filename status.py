# ===== DORM STATUS ======

import sqlite3


from datetime import datetime

#def set_status(status):
#    with open("status.txt", "w", encoding="utf-8") as f:
#        print()
#        print(f"Input {status} selected")
#        f.write(status)

#def check_status():
#    with open("status.txt", "r", encoding="utf-8") as f:
#        print()
#        print("Input STATUS CHECK selected")
#        print("")
#        returned_status = (f.read())
#        return returned_status

def set_status(status, location, reason):
    conn = sqlite3.connect("status.db")
    cur = conn.cursor()
    time = datetime.now().isoformat(timespec="seconds")
    cur.execute("INSERT INTO status (status, location, time, reason) VALUES (?, ?, ?, ?)", (status,location, time, reason))
    conn.commit()
    conn.close()
    return time

def check_status():
    conn = sqlite3.connect("status.db")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM status
                ORDER BY time DESC
                LIMIT 1""")
    return cur.fetchone()


def main():

    print("1. I'm in")
    print("2. I'm out")
    print("3. Check status")
    print("4. Quit")
    print("")

    status_check = input("Choose an option:")

    while status_check != "4":

        if status_check == "1":
            set_status("IN")

        elif status_check == "2":
            set_status("OUT")

        elif status_check == "3":
            current_status = check_status()
            print(current_status)


        elif status_check not in ["1", "2", "3", "4"]:
            print()
            print("Try again bro!")
            print()

        print()
        status_check = input("Choose an option:")

    print()
    print("You are now not viewing Adrien's beautiful status")
    print()
    print("Bye bye")

if __name__ == "__main__":
    main()


