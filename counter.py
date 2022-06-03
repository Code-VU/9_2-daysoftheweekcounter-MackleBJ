
def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")    # end assignment
    file_handle = open(file_name, 'r')

    day_counter = {}

    for line in file_handle:
        if line.startswith('From'):
            if line.startswith('From:'):
                continue
            else:
                sections_of_line = line.split(' ')
                day = sections_of_line[2]
                if day in day_counter:
                    day_counter[day] += 1
                else:
                    day_counter[day] = 1
    
    print(day_counter)
## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#countDayOfTheWeek()