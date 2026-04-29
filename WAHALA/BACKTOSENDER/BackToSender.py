def daily_wage(number_of_successful_delivery):
    amount_per_parcel = 0
   
    if number_of_successful_delivery < 50:
        amount_per_parcel = 160
    elif 50 <= number_of_successful_delivery < 60:
        amount_per_parcel = 200
    elif 60 <= number_of_successful_delivery < 70:
        amount_per_parcel = 250
    else:
        amount_per_parcel = 500
       
    return (number_of_successful_delivery * amount_per_parcel) + 5000

