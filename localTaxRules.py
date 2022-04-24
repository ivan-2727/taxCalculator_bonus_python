from helpers import parse

def localTaxRules():

    time_zones = [
        "06:00–06:29 8",
        "06:30–06:59 13",
        "07:00–07:59 18",
        "08:00–08:29 13",
        "08:30–14:59 8",
        "15:00–15:29 13",
        "15:30–16:59 18",
        "17:00–17:59 13",
        "18:00–18:29 8",
        "18:30–05:59 0"
    ]

    free_vehicles = [
        "MOTORCYCLE",
        "TRACTOR",
        "EMERGENCY",
        "DIPLOMAT",
        "FOREIGN",
        "MILITARY" 
    ]

    free_dates = {
    "2013": [
            [1],
            [],
            [28,29],
            [1,30],
            [1,8,9],
            [5,6,21],
            [-1],
            [],
            [],
            [],
            [1],
            [24,25,26,31]
        ]
    }

    return {"time_zones": [parse(zone) for zone in time_zones], "free_vehicles": free_vehicles, "free_dates": free_dates}

