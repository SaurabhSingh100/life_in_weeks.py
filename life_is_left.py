is_true = True
while is_true:
    age = (input("enter your age"))
    if age.lower() == "off":
        print("thankyou")
        break
    age_as_int = int(age)
    year = (70 - age_as_int)
    days_left = (year * 365)
    week_left = (year * 52)
    months_left = (year * 12)
    print(f"you have {days_left} days, {week_left} weeks and ,{months_left} months left.")
