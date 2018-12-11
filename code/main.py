from helium import get_helium_ratio


D = 36 #in
m = 250 #g


h_to_air = get_helium_ratio(D, m)
print(h_to_air)
