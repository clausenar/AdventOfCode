import re

data = open("./data/01_test.txt")

translation = ["zero",
              "one",
              "two",
              "three",
              "four",
              "five",
              "six",
              "seven",
              "eight",
              "nine",
              "zero"]

translation_reverse = [i[::-1] for i in translation]

#print (translation,translation_reverse)

translation_join = "|".join(translation)
translation_reverse_join = "|".join(translation)
#print (translation_join)

nums = data.readlines()
sum=0

for i in nums:
    first_digits = re.search("[0-9]",i)
    last_digits = re.search("[0-9]",i[::-1])
    first_number = re.search(translation_join,i)
    last_number = re.search(translation_reverse_join,i[::-1])
    if first_digits is None:
        first_digits =""
    if last_digits is None:
        last_digits =""
    #if first_number is None:
    #    first_number =""
    #if last_number is None:
    #    last_number =""
    else:
        first_digit_position = first_digits.start()
        first_digit = first_digits.group()
        last_digit = last_digits.group()
        print (i,first_digit,last_digit)
        number = first_digit+last_digit
        sum += int(number)
        #print (i,first_number,last_digits)

    #last = re.finditer("[0-9]",i[::-1])
    #print (i,digits)
    numbers = re.search(translation_join,i)
    #print (numbers)
    #print (i,digits,numbers)
    
    #last_digit = re.search("[0-9]",i[::-1]).group()
    #first_digt_pos = re.search("[0-9]",i).span()
    #last_digit_pos = re.search("[0-9]",i[::-1]).span()

    #translation_join = "|".join(translation)
    #sprint (translation_join)

    #first_number = re.findall("|".join(translation),i)
    #print (first_number)
    #last_number = re.search(",i[::-1]).group()
    #first_number_pos = re.search("[0-9]",i).span()
    #last_number_pos = re.search("[0-9]",i[::-1]).span()

    #rint (i,digits)

print (sum)
    


    

    #number = int(first+last)
    #sum+= number

#print (sum)

tranlation = {"one":1,
              "two":2,
              "three":3,
              "four":4,
              "five":5,
              "six":6,
              "seven":7,
              "eight":8,
              "nine":9,
              "zero":0,}





