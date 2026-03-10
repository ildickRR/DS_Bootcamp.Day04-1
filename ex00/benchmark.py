import timeit

def find_app(email_list):
    gmail_list = []

    for email in email_list:
        if email.endswith('@gmail.com'):
            gmail_list.append(email)
    return gmail_list


def find_comp(email_list):
    return [email for email in email_list if email.endswith('@gmail.com')]


def main():

    email_list =  ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5

    vizov_app = find_app(email_list)
    vizov_comp = find_comp(email_list)

    time1 = timeit.timeit(lambda: vizov_app, number=90000000)
    time2 = timeit.timeit(lambda: vizov_comp, number=90000000)

    if(time1 <= time2):
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a loop")

    times = [time1, time2]
    times.sort()

    print(f"{times[0]} vs {times[1]}")

if __name__ == "__main__":
    main()

    
