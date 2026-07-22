# 2026-07 -22

import math


def time_to_minutes(time_str):
    hh, mm = map(int, time_str.split(":"))
    return hh * 60 + mm


def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees

    parking = {}
    total_times = {}

    for record in records:
        time_str, car_num, status = record.split()
        time_min = time_to_minutes(time_str)

        if status == "IN":
            parking[car_num] = time_min
        else:
            in_time = parking.pop(car_num)
            parked_duration = time_min - in_time
            total_times[car_num] = total_times.get(car_num, 0) + parked_duration

    max_time = time_to_minutes("23:59")
    for car_num, in_time in parking.items():
        parked_duration = max_time - in_time
        total_times[car_num] = total_times.get(car_num, 0) + parked_duration

    answer = []
    for car_num in sorted(total_times.keys()):
        duration = total_times[car_num]

        if duration <= base_time:
            fee = base_fee
        else:
            extra_time = duration - base_time
            fee = base_fee + math.ceil(extra_time / unit_time) * unit_fee

        answer.append(fee)

    return answer
