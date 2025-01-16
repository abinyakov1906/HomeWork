calls = 0
def count_calls():
    global calls
    calls += 1
def string_info():
    a = 'Capybara'
    count_calls()
    print(len(a), a.upper(), a.lower())
string_info()
def string_info():
    b = 'Armageddon'
    count_calls()
    print(len(b), b.upper(), b.lower())
string_info()
def is_contains():
    string1 = "urban"
    count_calls()
    list_to_search1 = ['ban', 'BaNaN', 'urBAN']
    if string1.lower() in (word.lower() for word in  list_to_search1):
        print(True)
    else:
        print(False)
is_contains()
def is_contains():
    string2 = "cycle"
    count_calls()
    list_to_search2 = ['recycling', 'cyclic']
    if string2.lower() in (word.lower() for word in  list_to_search2):
        print(True)
    else:
        print(False)
is_contains()
print(calls)