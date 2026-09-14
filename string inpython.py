# name="shYaM"
#
# print(name.lower())
# print(name.upper())
# print(name.capitalize())   # make first letter to capital
from secrets import token_urlsafe

# mobile="9003200696"

# masked=mobile[:2]    #show first two index value
# print(masked)

# masked=mobile[-4:]    #show only last four index value
# print(masked)

# masked=mobile[:2]+mobile[-2:]
# print(masked)

# masked=mobile[:3]+"*****"+mobile[-2:]
# print(masked)

# song="shape of you"       #(title is a function make the first letter of every word into capital)
# artist="ed sheeran"
# formated=(f"name of the song {song.title()}-artist name is {artist.title()}")
# print(formated)

#split=funtion used to split the sentance using the index or delimiters

# message="your uber booking id is : UB12345. please keep it safe"
# booking_id=message.split(":")[1]
# booking_id=message.split(":")[1].split(".")[0]
# booking_id=message.split(":")[1].split(".")[0].strip()   #strip remove the space
# print(booking_id)

#replace== replace the new word by new
location="chennai central"
current_location=location.replace("chennai central","thambaram")
print(current_location)


#len()=lenght is used to count how many charcter in the row or string
# word="the trip was amazing"
# word_count=len(word)
# print(word_count)

#join==combin multiple string into one string
# name="shayam jayaraj"
# first_letter=name[0].upper().split()
# first_letter=[word[0].upper() for word in name.split()]
# first_letter="".join(word[0].upper()for word in name.split())
# print(first_letter)