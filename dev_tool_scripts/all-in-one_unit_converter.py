import math

# Conversion Functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def liters_to_gallons(liters):
    return liters * 0.264172

def gallons_to_liters(gallons):
    return gallons / 0.264172

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def grams_to_ounces(grams):
    return grams * 0.035274

def ounces_to_grams(ounces):
    return ounces / 0.035274

def sq_meters_to_sq_feet(sq_meters):
    return sq_meters * 10.7639

def sq_feet_to_sq_meters(sq_feet):
    return sq_feet / 10.7639

def mm_to_inches(mm):
    return mm / 25.4

def inches_to_mm(inches):
    return inches * 25.4

def hours_to_minutes(hours):
    return hours * 60

def minutes_to_hours(minutes):
    return minutes / 60

def days_to_hours(days):
    return days * 24

def hours_to_days(hours):
    return hours / 24

def kmh_to_ms(kmh):
    return kmh / 3.6

def ms_to_kmh(ms):
    return ms * 3.6

def psi_to_pa(psi):
    return psi * 6894.76

def pa_to_psi(pa):
    return pa / 6894.76

def feet_to_yards(feet):
    return feet / 3

def yards_to_feet(yards):
    return yards * 3

def watts_to_kw(watts):
    return watts / 1000

def kw_to_watts(kw):
    return kw * 1000

def joules_to_kj(joules):
    return joules / 1000

def kj_to_joules(kj):
    return kj * 1000

def db_to_amplitude(db):
    return 10 ** (db / 20)

def amplitude_to_db(amplitude):
    return 20 * math.log10(amplitude)

# Ask for conversion type
def ask_conversion():
    print("Welcome to the Conversion Tool!")
    print("Choose a conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")
    print("5. Liters to Gallons")
    print("6. Gallons to Liters")
    print("7. Kilograms to Pounds")
    print("8. Pounds to Kilograms")
    print("9. Grams to Ounces")
    print("10. Ounces to Grams")
    print("11. Square Meters to Square Feet")
    print("12. Square Feet to Square Meters")
    print("13. Millimeters to Inches")
    print("14. Inches to Millimeters")
    print("15. Hours to Minutes")
    print("16. Minutes to Hours")
    print("17. Days to Hours")
    print("18. Hours to Days")
    print("19. Speed (km/h to m/s)")
    print("20. Speed (m/s to km/h)")
    print("21. PSI to Pascals")
    print("22. Pascals to PSI")
    print("23. Feet to Yards")
    print("24. Yards to Feet")
    print("25. Watts to Kilowatts")
    print("26. Kilowatts to Watts")
    print("27. Joules to Kilojoules")
    print("28. Kilojoules to Joules")
    print("29. Decibels to Amplitude")
    print("30. Amplitude to Decibels")
    
    # Get the user's choice
    choice = int(input("Enter the number of the conversion you want to perform: "))
    
    # Based on the choice, ask for input and perform conversion
    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C = {celsius_to_fahrenheit(celsius)}°F")
    
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit)}°C")
    
    elif choice == 3:
        km = float(input("Enter distance in kilometers: "))
        print(f"{km} km = {km_to_miles(km)} miles")
    
    elif choice == 4:
        miles = float(input("Enter distance in miles: "))
        print(f"{miles} miles = {miles_to_km(miles)} kilometers")
    
    elif choice == 5:
        liters = float(input("Enter volume in liters: "))
        print(f"{liters} liters = {liters_to_gallons(liters)} gallons")
    
    elif choice == 6:
        gallons = float(input("Enter volume in gallons: "))
        print(f"{gallons} gallons = {gallons_to_liters(gallons)} liters")
    
    elif choice == 7:
        kg = float(input("Enter weight in kilograms: "))
        print(f"{kg} kg = {kg_to_pounds(kg)} pounds")
    
    elif choice == 8:
        pounds = float(input("Enter weight in pounds: "))
        print(f"{pounds} pounds = {pounds_to_kg(pounds)} kilograms")
    
    elif choice == 9:
        grams = float(input("Enter weight in grams: "))
        print(f"{grams} grams = {grams_to_ounces(grams)} ounces")
    
    elif choice == 10:
        ounces = float(input("Enter weight in ounces: "))
        print(f"{ounces} ounces = {ounces_to_grams(ounces)} grams")
    
    elif choice == 11:
        sq_meters = float(input("Enter area in square meters: "))
        print(f"{sq_meters} m² = {sq_meters_to_sq_feet(sq_meters)} ft²")
    
    elif choice == 12:
        sq_feet = float(input("Enter area in square feet: "))
        print(f"{sq_feet} ft² = {sq_feet_to_sq_meters(sq_feet)} m²")
    
    elif choice == 13:
        mm = float(input("Enter length in millimeters: "))
        print(f"{mm} mm = {mm_to_inches(mm)} inches")
    
    elif choice == 14:
        inches = float(input("Enter length in inches: "))
        print(f"{inches} inches = {inches_to_mm(inches)} mm")
    
    elif choice == 15:
        hours = float(input("Enter time in hours: "))
        print(f"{hours} hours = {hours_to_minutes(hours)} minutes")
    
    elif choice == 16:
        minutes = float(input("Enter time in minutes: "))
        print(f"{minutes} minutes = {minutes_to_hours(minutes)} hours")
    
    elif choice == 17:
        days = float(input("Enter time in days: "))
        print(f"{days} days = {days_to_hours(days)} hours")
    
    elif choice == 18:
        hours = float(input("Enter time in hours: "))
        print(f"{hours} hours = {hours_to_days(hours)} days")
    
    elif choice == 19:
        kmh = float(input("Enter speed in km/h: "))
        print(f"{kmh} km/h = {kmh_to_ms(kmh)} m/s")
    
    elif choice == 20:
        ms = float(input("Enter speed in m/s: "))
        print(f"{ms} m/s = {ms_to_kmh(ms)} km/h")
    
    elif choice == 21:
        psi = float(input("Enter pressure in PSI: "))
        print(f"{psi} PSI = {psi_to_pa(psi)} Pascals")
    
    elif choice == 22:
        pa = float(input("Enter pressure in Pascals: "))
        print(f"{pa} Pascals = {pa_to_psi(pa)} PSI")
    
    elif choice == 23:
        feet = float(input("Enter length in feet: "))
        print(f"{feet} feet = {feet_to_yards(feet)} yards")
    
    elif choice == 24:
        yards = float(input("Enter length in yards: "))
        print(f"{yards} yards = {yards_to_feet(yards)} feet")
    
    elif choice == 25:
        watts = float(input("Enter power in watts: "))
        print(f"{watts} watts = {watts_to_kw(watts)} kilowatts")
    
    elif choice == 26:
        kw = float(input("Enter power in kilowatts: "))
        print(f"{kw} kilowatts = {kw_to_watts(kw)} watts")
    
    elif choice == 27:
        joules = float(input("Enter energy in joules: "))
        print(f"{joules} joules = {joules_to_kj(joules)} kilojoules")
    
