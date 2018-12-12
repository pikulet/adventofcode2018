with open('d04-input.txt', 'r') as f:
    data = f.readlines()


def parse_record(record):
    record = record.split("]")
    timestamp = parse_timestamp(record[0][1:])
    message = parse_message(record[1][1:])
    return timestamp + message


def parse_timestamp(timestamp):
    timestamp = timestamp.split()
    date = [int(x) for x in timestamp[0].split("-")]
    hour = [int(x) for x in timestamp[1].split(":")]
    return date, hour


def parse_message(msg):
    event = msg[0]
    if event == "G":
        guard_no = msg.split()[1][1:]
        return "guard", guard_no
    elif event == "f":
        return "sleep",
    elif event == "w":
        return "wake",


############################# Parsing data #############################

# sort the data
data = [parse_record(r) for r in data]
data.sort(key=lambda r: (r[0], r[1]))

sleep_record = dict()
current_date = []
current_guard_id = -1
sleep_start_time = 60  # assumes guard did not sleep
sleep_wake_times = set()

for record in data:
    record_type = record[2]
    record_minute = record[1][1]
    if record_type == "guard":
        # add previous date's records
        sleep_record.setdefault(current_guard_id, list())
        guard_records = sleep_record.get(current_guard_id)
        guard_records.append((current_date, sleep_wake_times))
        sleep_record.update({current_guard_id: guard_records})

        # reset counters
        current_date = record[0]
        current_guard_id = record[3]
        sleep_start_time = 60
        sleep_wake_times = set()
    elif record_type == "sleep":
        sleep_start_time = record_minute
    elif record_type == "wake":
        sleep_wake_times.add((sleep_start_time, record_minute - 1))
        sleep_start_time = -1
#####################################################################


# Part 1a: Find guard with the most sleep
def calculate_sleep_minutes(sleep_periods):
    return sum([r[1] - r[0] + 1 for r in sleep_periods])


guard_sleep_record = dict()
for guard_id, data in sleep_record.items():
    sleep_time = sum(calculate_sleep_minutes(x[1]) for x in data)
    new_total_sleep = guard_sleep_record.get(guard_id, 0) + sleep_time
    guard_sleep_record.setdefault(guard_id, new_total_sleep)
    guard_sleep_record.update({guard_id: new_total_sleep})


sleepy_guard = max(guard_sleep_record.items(), key=lambda r: r[1])[0]
sleepy_guard_records = [x[1] for x in sleep_record.get(sleepy_guard)]

minutes_asleep = [0]*60
for r in sleepy_guard_records:
    for period in r:
        for minute in range(period[0], period[1] + 1):
            minutes_asleep[minute] += 1

best_minute = minutes_asleep.index(max(minutes_asleep))
result = int(sleepy_guard) * best_minute
print(result)
