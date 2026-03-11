import timeit
import sys


def main():
        
    if(len(sys.argv) !=3):
        return 

    email_list =  ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    func_name = sys.argv[1]
    count = int(sys.argv[2])


    dict_def = {
        "loop": find_app,
        "list_comprehension": find_comp,
        "map": find_map,
        "filter": find_filter
    }
   

    if(sys.argv[1] not in dict_def):
        return

    if(func_name in dict_def):
        target_name = dict_def[func_name]

    time1 = timeit.timeit(lambda: target_name(email_list), number= count) 

    print(time1)


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

def find_filter(email_list):
    return list(filter(lambda email: email.endswith('@gmail.com'), email_list))

if __name__ == "__main__":
    main()

    
