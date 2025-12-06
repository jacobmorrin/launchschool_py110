

temperatures = {
'Seattle': [22, 25, 28, 26, 23, 24, 27],
'Phoenix': [35, 38, 40, 37, 33, 36, 39],
'Denver': [20, 24, 29, 31, 25, 22, 26],
'Austin': [32, 30, 29, 34, 31, 33, 30],
}

hot_cities = {city: max(temperatures[city]) for city in temperatures if max(temperatures[city]) >= 30}

print(hot_cities)