# sentence = "what is the airspeed velocity of an unladen swallow?"
# split_sentence = sentence.split()
#
# result = {word: len(word) for word in split_sentence}
# print(result)

weather_c = {
    "monday": 12,
    "tuesday": 14,
    "wednesday": 15,
    "thursday": 14,
    "friday": 21,
    "saturday": 23,
    "sunday": 18,
}

# temp_f = (temp * 9/5) + 32
weather_f = {days: (temp * 9/5) + 32 for (days, temp) in weather_c.items()}
print(weather_f)
