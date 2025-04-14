works = [
    ("programming", "saturday", "10h", "completed"),
    ("driving", "afterClass", "2h", "notcompleted"),
    ("eating", "monday", "1h", "notstarted"),
    ("checking", "tuesday", "8h", "completed"),
    ("chatting", "wednesday", "9h", "notcompleted")
]
print("All works:", works)

def filterDone():
    for item in works:
        if item[3] == "completed":
            print(item)

def findFirstNotStarted():
    print("")
    for item in works:
        if item[3] == "notstarted":
            print(item)
            break
    else:
        print("No work is marked as 'not-started'.")

filterDone()
findFirstNotStarted()
