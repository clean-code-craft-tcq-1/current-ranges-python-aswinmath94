def check_if_valid_input(ranges):
    if len(ranges) > 0:
        return True
    else:
        return False

def get_continous_range_count(list_of_nos):
    if check_if_valid_input(list_of_nos):
        sorted_list = sorted(list_of_nos)
        range_list = []
        continous_list = []

        i = 0
        while (i+1 < len(sorted_list)):
            if ((sorted_list[i+1] - sorted_list[i]) <= 1):
                continous_list.append(sorted_list[i])
            else:
                continous_list.append(sorted_list[i])
                range_list.append(continous_list)
                continous_list = []

            i += 1
        print_range_count(range_list)
        return 'Success'
    else:
        return 'Invalid Input'

def print_range_count(bin_list):
    print('Ranges', 'Readings')
    for bin in bin_list:
        print(str(bin[0]) + "-" + str(bin[-1]) + ", " + str(len(bin)))
