def current_ranges(ranges):
    if check_if_valid_input(ranges):
        no_of_bins = 4
        bin_parameter = bin_parameter_calculator(ranges,no_of_bins)
        bin_range_list = bin_ranges_calculator(bin_parameter)
        bin_list = range_binner(ranges,bin_parameter,bin_range_list)
        get_output(bin_list)
        return 'Valid Input list'
    else:
        return 'Invalid Input list'



def check_if_valid_input(ranges):
    if len(ranges) > 0:
        return 1
    else:
        return 0

def bin_parameter_calculator(ranges,no_of_bins):
    maximum_value = sorted(ranges)[-1]
    minimum_value = sorted(ranges)[0]

    #Assume equal width binning
    bin_width = (maximum_value-minimum_value)/no_of_bins
    value_dict ={'bin_wdith':bin_width,'maximum':maximum_value,'minimum':minimum_value,'no_of_bins':no_of_bins}
    return value_dict

def bin_ranges_calculator(bin_paramters):
    range_list =[]
    for i in range(0, bin_paramters['no_of_bins'] + 1):
        range_list = range_list + [bin_paramters['minimum'] + bin_paramters['bin_wdith'] * i]
    return range_list

def range_binner(ranges,bin_parameters,range_list):
    bin = []

    for i in range(0, bin_parameters['no_of_bins']):
        temp = []
        for j in ranges:
            if lower_limit_check(j,range_list[i]) and j < upper_limit_check(j,range_list[i]):
                temp += [j]
        bin += [temp]
    return bin

def lower_limit_check(number,lower_limit):
    if number >= lower_limit:
        return True
    else:
        return False

def upper_limit_check(number,upper_limit):
    if number <= upper_limit:
        return False

def get_output(bin_list):
    print(bin_list)
    print('Ranges','Readings')
    for bin in bin_list:
        if len(bin) > 0:
            reading = len(bin)
            ranges = str(bin[0]) + '-' + str(bin[len(bin) - 1])
            output = str(ranges) + ',' + str(reading)
            print(output)
    return output
