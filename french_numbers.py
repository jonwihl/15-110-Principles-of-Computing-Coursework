# Part 3: print french for the numbers between lo and hi (inclusive)
def print_french(lo, hi):
    for i in range(lo, hi + 1):
        print (i, num_in_french(i))
    
def digit(num, pos):
    return (num // 10**(pos-1)) % 10

def num_in_french(num): # assumes 0 <= num <= 100

    ones_list = ["zero", "un", "deux", "trois", "quatre", "cinq", "six", "sept",
                 "huit", "neuf", "dix","onze", "douze", "treize", "quatorze",
                 "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"]

    tens_list = ["", "dix", "vingt", "trente", "quarante", "cinquante", 
                "soixante", "soixante", "quatre-vingt", "quatre-vingt"]


    # Part 1: get the ones and tens digits of num
    if num != 100:
        ones_digit = digit(num,1)
        tens_digit = digit(num,2)
        if num < 20:
            return ones_list[num]
        elif num >= 70 and num < 80:
            if ones_digit != 1:
                number = tens_list[digit(num,2)] + "-" + ones_list[ones_digit + 10]
                return number
            else:
                number = tens_list[digit(num,2)] + " et " + ones_list[ones_digit + 10]
                return number
        elif num >= 90 and num < 100:
                number = tens_list[digit(num,2)] + "-" + ones_list[ones_digit + 10]
                return number
        elif num < 70 and num > 19:
            if ones_digit == 0:
                return tens_list[tens_digit]
            elif ones_digit == 1 and tens_digit != 8:
                number = tens_list[digit(num,2)] + " et " + ones_list[ones_digit]
                return number
            elif tens_digit < 7 and tens_digit > 1 and ones_digit >= 2 and ones_digit <= 9:
                number = tens_list[tens_digit] + "-" + ones_list[ones_digit]
                return number
        elif num >= 80 and num < 90:
            if ones_digit != 0:
                number = tens_list[tens_digit] + "-" + ones_list[ones_digit]
                return number
            elif ones_digit == 0:
                number = tens_list[tens_digit] + "s"
                return number
    else:
        number = "cent"
        return number