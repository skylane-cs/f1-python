import random, time

tracks = {
    "Bahrain": {"CIRC": "Bahrain International Circuit", "LAPS": 57, 'POLE': 90.558, "RAIN": 0},
    "Jeddah": {"CIRC": "Jeddah Street Circuit", "LAPS": 50, 'POLE': 88.2, "RAIN": 0},
    "Melbourne": {"CIRC": "Albert Park Circuit", "LAPS": 58, 'POLE': 77.868, "RAIN": 20},
    "Imola": {"CIRC": "Autodromo Enzo e Dino Ferrari", "LAPS": 63, 'POLE': 87.999, "RAIN": 30},
    "Miami": {"CIRC": "Miami International Autodrome", "LAPS": 57, 'POLE': 88.796, "RAIN": 15},
    "Barcelona": {"CIRC": "Circuit de Barcelona-Catalunya", "LAPS": 66, 'POLE': 79.750, "RAIN": 15},
    "Monaco": {"CIRC": "Circuit de Monaco", "LAPS": 78, 'POLE': 71.376, "RAIN": 60},
    "Baku": {"CIRC": "Baku City Circuit", "LAPS": 51, 'POLE': 101.359, "RAIN": 20},
    "Montreal": {"CIRC": "Circuit Gilles Villeneuve", "LAPS": 70, 'POLE': 81.299, "RAIN": 50},
    "Silverstone": {"CIRC": "Silverstone Circuit", "LAPS": 52, 'POLE': 100.983, "RAIN": 40},
    "Austria": {"CIRC": "Red Bull Ring", "LAPS": 71, 'POLE': 64.984, "RAIN": 30},
    "Paul Ricard": {"CIRC": "Circuit Paul Ricard", "LAPS": 53, 'POLE': 90.872, "RAIN": 20},
    "Budapest": {"CIRC": "Hungaroring", "LAPS": 70, 'POLE': 77.377, "RAIN": 55},
    "Belgium": {"CIRC": "Circuit de Spa-Francorchamps", "LAPS": 44, 'POLE': 103.665, "RAIN": 50},
    "Zandvoort": {"CIRC": "Circuit Zandvoort", "LAPS": 72, 'POLE': 70.342, "RAIN": 20},
    "Monza": {"CIRC": "Autodromo Nazionale di Monza", "LAPS": 53, 'POLE': 80.161, "RAIN": 20},
    "Singapore": {"CIRC": "Marina Bay Street Circuit", "LAPS": 61, 'POLE': 109.412, "RAIN": 75},
    "Suzuka": {"CIRC": "Suzuka Intl. Racing Course", "LAPS": 53, 'POLE': 89.304, "RAIN": 40},
    "Austin": {"CIRC": "CIRC of The Americas", "LAPS": 56, 'POLE': 94.356, "RAIN": 15},
    "Mexico": {"CIRC": "Autodromo Hermanos Rodriguez", "LAPS": 71, 'POLE': 77.775, "RAIN": 20},
    "Brazil": {"CIRC": "Autodromo Jose Carlos Pace", "LAPS": 71, 'POLE': 71.674, "RAIN": 85},
    "Abu Dhabi": {"CIRC": "Yas Marina Circuit", "LAPS": 55, 'POLE': 83.8241, "RAIN": 0},
}

drivers = {
    "VER": {"Team": "Red Bull", "QUA": 95, "RAC": 95, "AWA": 91, "EXP": 78, "REL": 90, "STR": 95},
    "LEC": {"Team": "Ferrari", "QUA": 94, "RAC": 91, "AWA": 92, "EXP": 72, "REL": 89, "STR": 79},
    "PER": {"Team": "Red Bull", "QUA": 89, "RAC": 90, "AWA": 91, "EXP": 84, "REL": 90, "STR": 95},
    "RUS": {"Team": "Mercedes", "QUA": 88, "RAC": 88, "AWA": 83, "EXP": 70, "REL": 95, "STR": 71},
    "SAI": {"Team": "Ferrari", "QUA": 91, "RAC": 89, "AWA": 89, "EXP": 78, "REL": 89, "STR": 79},
    "HAM": {"Team": "Mercedes", "QUA": 87, "RAC": 87, "AWA": 95, "EXP": 91, "REL": 95, "STR": 71},
    "NOR": {"Team": "McLaren", "QUA": 86, "RAC": 80, "AWA": 86, "EXP": 70, "REL": 92, "STR": 89},
    "OCO": {"Team": "Alpine", "QUA": 80, "RAC": 79, "AWA": 82, "EXP": 73, "REL": 75, "STR": 77},
    "ALO": {"Team": "Alpine", "QUA": 84, "RAC": 79, "AWA": 79, "EXP": 95, "REL": 75, "STR": 77},
    "BOT": {"Team": "Alfa Romeo", "QUA": 79, "RAC": 76, "AWA": 93, "EXP": 81, "REL": 77, "STR": 66},
    "RIC": {"Team": "McLaren", "QUA": 76, "RAC": 71, "AWA": 71, "EXP": 84, "REL": 92, "STR": 89},
    "VET": {"Team": "Aston Martin", "QUA": 75, "RAC": 75, "AWA": 87, "EXP": 90, "REL": 92, "STR": 76},
    "MAG": {"Team": "Haas", "QUA": 78, "RAC": 70, "AWA": 82, "EXP": 76, "REL": 92, "STR": 65},
    "GAS": {"Team": "AlphaTauri", "QUA": 77, "RAC": 72, "AWA": 65, "EXP": 73, "REL": 89, "STR": 79},
    "STR": {"Team": "Aston Martin", "QUA": 71, "RAC": 72, "AWA": 71, "EXP": 74, "REL": 92, "STR": 76},
    "MSC": {"Team": "Haas", "QUA": 73, "RAC": 69, "AWA": 86, "EXP": 67, "REL": 92, "STR": 65},
    "TSU": {"Team": "AlphaTauri", "QUA": 75, "RAC": 70, "AWA": 75, "EXP": 67, "REL": 89, "STR": 79},
    "ZHO": {"Team": "Alpha Romeo", "QUA": 73, "RAC": 70, "AWA": 79, "EXP": 65, "REL": 77, "STR": 66},
    "ALB": {"Team": "Williams", "QUA": 73, "RAC": 71, "AWA": 66, "EXP": 68, "REL": 92, "STR": 74},
    "LAT": {"Team": "Williams", "QUA": 65, "RAC": 65, "AWA": 74, "EXP": 69, "REL": 92, "STR": 74},
}

weather = {
    "Sunny": {"TEMP": 26, "DELT": 1},
    "Light Cloud": {"TEMP": 22, "DELT": 1.005},
    "Cloudy": {"TEMP": 16, "DELT": 1.01},
    "Light Rain": {"TEMP": 15, "DELT": 1.1},
    "Heavy Rain": {"TEMP": 14, "DELT": 1.15}
}

for driver, data in drivers.items():
    drivers[driver]["GRI"] = 0
    drivers[driver]["TIM"] = 0
    drivers[driver]["TOT"] = 0
    drivers[driver]["DNF"] = False

print("\n------------------------------------\n\nWelcome to skyv1111's F1 Simulator!\n")

for i, (l, r) in enumerate(zip(list(tracks.items())[:len(list(tracks.items())) // 2], list(tracks.items())[len(list(tracks.items())) // 2:])):
    print(f"{i + 1:2}. {l[0]:15s} {i + len(list(tracks.items())) // 2 + 1:2}. {r[0]:30s}")

sel_track = input("\nSelect a track:  ").lower()

while sel_track.lower() not in [t.lower() for t in tracks.keys()] and not any(str(i + 1) == sel_track for i in range(len(tracks))):
    sel_track = input("\nInvalid track. Select a track:  ").lower()

if sel_track.isdigit():
    sel_track = list(tracks.keys())[int(sel_track) - 1]
else:
    sel_track = [t for t in tracks.keys() if t.lower() == sel_track][0]

def simulate_qualifying(drivers):

    print("\n------------------------------------\n\nQualifying Information:")

    track = tracks[sel_track]["CIRC"]
    pole = tracks[sel_track]["POLE"]
    rain = tracks[sel_track]["RAIN"]

    grid_penalties = []

    if rain == 0:
        cond = random.choice(["Sunny", "Light Cloud"])
    elif rain > 50:
        cond = random.choice(["Sunny", "Light Cloud", "Cloudy", "Light Rain", ])
    else:
        cond = random.choice(["Sunny", "Light Cloud", "Cloudy", "Light Rain", "Heavy Rain"])

    temp = weather[cond]["TEMP"]
    temp_delta = weather[cond]["DELT"]

    print(f"\nCircuit: {track}\nWeather: {cond}\nTemperature: {temp + random.randint(-3, 3)}°C")

    for driver, data in drivers.items():
        if cond == "Light Rain" or cond == "Heavy Rain":
            qualifying_time = pole + temp_delta + random.uniform(-0.1, 1.9) + 9.5 - (data["QUA"] / 10)
        elif cond in ["Sunny", "Light Cloud", "Cloudy"]:
            qualifying_time = pole + temp_delta + random.uniform(-0.1, 0.9) + 9.5 - (data["QUA"] / 10)
        data["TIM"] = qualifying_time

    sorted_grid = sorted(drivers.items(), key=lambda x: x[1]["TIM"])

    for i, (driver, data) in enumerate(sorted_grid):
        if random.random() < 0.01:
            grid_penalty = random.choice([5, 10, 15, 20])
            drivers[driver]["GRI"] = i + 1 + grid_penalty
            grid_penalties.append((driver, grid_penalty))
        else:
            drivers[driver]["GRI"] = i + 1
        drivers[driver]["TIM"] = data["TIM"]

    if grid_penalties:
        print("Grid Penalties: ", end="")
        for i, (driver, penalty) in enumerate(grid_penalties):
            if i == 0:
                print(f"{driver} ({penalty})")
            else:
                print(f"\t\t\t    {driver} ({penalty})")

    sorted_grid = sorted(drivers.items(), key=lambda x: x[1]["GRI"])

    print("\n------------------------------------\n\nStarting Grid:\n")


    for i in range(0, len(sorted_grid), 2):
        left_driver = sorted_grid[i]
        right_driver = sorted_grid[i + 1] if i + 1 < len(sorted_grid) else None
        left_time = f"{left_driver[1]['TIM'] // 60:1.0f}:{left_driver[1]['TIM'] % 60:06.3f}"
        right_time = f"{'':>5}{right_driver[1]['TIM'] // 60:1.0f}:{right_driver[1]['TIM'] % 60:06.3f}"

        print(f"{i + 1:2}. {left_driver[0]:<15s}{i + 2:2}. {right_driver[0]:<2s}")
        print(f"{'':>4}{left_time:14}{right_time}")



def simulate_race(drivers):
    print("\n------------------------------------\n\nRace Information:")

    rain_chance = tracks[sel_track]["RAIN"]
    if rain_chance == 0:
        cond = random.choice(["Sunny", "Light Cloud"])
    elif rain_chance > 50:
        cond = random.choice(["Sunny", "Light Cloud", "Cloudy", "Light Rain", ])
    else:
        cond = random.choice(["Sunny", "Light Cloud", "Cloudy", "Light Rain", "Heavy Rain"])

    track = tracks[sel_track]["CIRC"]
    temp = weather[cond]["TEMP"] + random.randint(-3, 3)
    temp_delta = weather[cond]["DELT"]
    pole = tracks[sel_track]["POLE"]

    print(f"\nCircuit: {track}\nWeather: {cond}\nTemperature: {temp}°C\n")

    print("------------------------------------\n")

    race_results = {}

    for lap in range(1, tracks[sel_track]["LAPS"] + 1):

        for driver in drivers:

            if lap <= 10:
                grid = 1.0 + (drivers[driver]["GRI"] - 1) * 0.01
                lap_time = (pole * grid + random.uniform(-0.1, 2) + 9.5 - (data["RAC"] / 10)) * temp_delta
                grid - 0.001
            else:
                lap_time = (pole * grid + random.uniform(-0.1, 0.5) + 9.5 - (data["RAC"] / 10)) * temp_delta

            leader = min(drivers.items(), key=lambda x: x[1]["TOT"])

            if leader[0] != driver:
                delta_time = drivers[leader[0]]["TOT"] - drivers[driver]["TOT"]
                if delta_time <= 1:
                    lap_time -= 0.25

            drivers[driver]["TOT"] += lap_time

            sorted_race = sorted(drivers.items(), key=lambda x: x[1]["TOT"])


        lap_leader = min(drivers.items(), key=lambda x: x[1]["TOT"])[0]

        print(f"[Lap {lap} / {tracks[sel_track]['LAPS']}] \n {lap_leader} leads")

        prev_leader = lap_leader

    sorted_race = sorted(drivers.items(), key=lambda x: x[1]["TOT"])
    leader_lap_time = sorted_race[0][1]["TOT"]

    leader_avg_lap = leader_lap_time / lap
    leader_lap_time = sorted_race[0][1]["TOT"]

    print()

    # Print race results (TEMP)

    for i in range(0, len(sorted_race), 2):
        left_driver = sorted_race[i]
        right_driver = sorted_race[i + 1] if i + 1 < len(sorted_race) else None

        left_time = f"{left_driver[1]['TOT'] // 60:1.0f}:{left_driver[1]['TOT'] % 60:06.3f}"
        right_time = f"{'':>5}{right_driver[1]['TOT'] // 60:1.0f}:{right_driver[1]['TOT'] % 60:06.3f}"

        print(f"{i + 1:2}. {left_driver[0]:<15s}{i + 2:2}. {right_driver[0]:<2s}")
        print(f"{'':>4}{left_time:14}{right_time}")

simulate_qualifying(drivers)
simulate_race(drivers)
