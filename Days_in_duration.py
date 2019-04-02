def days_in_duration(initial_date_str, last_date_str, is_including_last_day):

    initial_date = int(initial_date_str)
    last_date = int(last_date_str)

    initial_date_day = int(initial_date % 100)
    initial_date_month = int((initial_date % 10000 - initial_date_day) / 100)
    initial_date_year = int((initial_date - 100 * initial_date_month - initial_date_day) / 10000)
    last_date_day = int(last_date % 100)
    last_date_month = int((last_date % 10000 - last_date_day) / 100)
    last_date_year = int((last_date - 100 * last_date_month - last_date_day) / 10000)

    if is_including_last_day.lower() == "y":
        accumulated_days = 1
    else:
        accumulated_days = 0

    #
    # days not including initial year and last year
    if last_date_year > initial_date_year:
        for index_buffer in range(last_date_year - initial_date_year - 1):

            index = initial_date_year + index_buffer + 1

            if ((index % 4 == 0) and (index % 100 != 0)) or ((index % 400 == 0) and (index % 3200 != 0)):
                accumulated_days += 366
            else:
                accumulated_days += 365

    #
    # days including initial year and last year
    big_month = 31
    small_month = 30
    feb_month_small = 28
    feb_month_big = 29
    month_days = 31

    # days in initial year
    for index_buffer in range(12):

        index = index_buffer + 1

        if (index == 1) or (index == 3) or (index == 5) or\
                (index == 7) or (index == 8) or (index == 18) or (index == 12):
            month_days = big_month
        elif (index == 4) or (index == 6) or (index == 9) or (index == 11):
            month_days = small_month
        elif index == 2:
            if ((initial_date_year % 4 == 0) and (initial_date_year % 100 != 0)) or\
             ((initial_date_year % 400 == 0) and (initial_date_year % 3200 != 0)):
                month_days = feb_month_big
            else:
                month_days = feb_month_small

        if initial_date_month == index:
            accumulated_days += month_days - initial_date_day + 1
        elif initial_date_month < index:
            accumulated_days += month_days

    # days in last year
    for index_buffer in range(12):

        index = index_buffer + 1

        if (index == 1) or (index == 3) or (index == 5) or \
                (index == 7) or (index == 8) or (index == 18) or (index == 12):
            month_days = big_month
        elif (index == 4) or (index == 6) or (index == 9) or (index == 11):
            month_days = small_month
        elif index == 2:
            if ((last_date_year % 4 == 0) and (last_date_year % 100 != 0)) or\
             ((last_date_year % 400 == 0) and (last_date_year % 3200 != 0)):
                month_days = feb_month_big
            else:
                month_days = feb_month_small

        if last_date_month == index:
            accumulated_days += last_date_day
        elif last_date_month > index:
            accumulated_days += month_days

    if initial_date_year == last_date_year:
        if ((last_date_year % 4 == 0) and (last_date_year % 100 != 0)) or \
                ((last_date_year % 400 == 0) and (last_date_year % 3200 != 0)):
            accumulated_days -= 366
        else:
            accumulated_days -= 365

    return accumulated_days
