import timeit


def main():

    email_list =  ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5

    time1 = timeit.timeit(lambda: find_app(email_list), number=9000000)
    time2 = timeit.timeit(lambda: find_comp(email_list), number=9000000)  
    time3 = timeit.timeit(lambda: find_map(email_list), number=9000000)  


    if(time1 <= time2 and time1 <= time3):
        print("it is better to use a loop")
    elif time2 < time1 and time2 < time3:
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a map")

    times = [time1, time2, time3]
    times.sort()

    print(f"{times[0]} vs {times[1]} vs {times[2]}")


def find_app(email_list):
    gmail_list = []

    for email in email_list:
        if email.endswith('@gmail.com'):
            gmail_list.append(email)
    return gmail_list


def find_comp(email_list):
    return [email for email in email_list if email.endswith('@gmail.com')]


def find_map(email_list):
    return list(map(lambda email: email if email.endswith('@gmail.com') else None, email_list))

if __name__ == "__main__":
    main()

    
