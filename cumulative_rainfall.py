def cumulative_rainfall(rainfallToday):

    # Reading Cumulative Rainfall from cum_rainfall.txt
    f = open("./cumulative_rainfall.txt", "r")
    str_rainfallCumulative = f.read()
    f.close()

    # Converting String to Integer
    rainfallCumulative = int(str_rainfallCumulative)

    # Adding Today's Rainfall to Cumulative Rainfall
    rainfallCumulative = rainfallCumulative + int(rainfallToday)

    # Converting Integer to String
    str_rainfallCumulative = str(rainfallCumulative)

    # Updating Cumulative Rainfall in cum_rainfall.txt
    f = open("./cumulative_rainfall.txt", "w")
    f.write(str_rainfallCumulative)
    f.close()

    return str_rainfallCumulative

# output = cumulative_rainfall('100')
# print(output)