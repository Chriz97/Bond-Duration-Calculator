# Function to Calculate the Bond Duration as well as the Modified Duration
def bond_duration(face_value, coupon_rate, time_to_maturity, yield_rate, frequency):
    if frequency == 2:
        n = time_to_maturity * 2
        c = coupon_rate / 2
        y = yield_rate / 2
    elif frequency == 1:
        n = time_to_maturity
        c = coupon_rate
        y = yield_rate

    pv_sum = 0
    price = face_value * (1/(1+ y) ** n)
    cf_sum = 0
    year = 1
    for i in range(1, n+1):
        cf = face_value * c
        discount_factor = 1 / (1 + y) ** year
        cf_sum += cf * discount_factor
        pv_sum += cf * discount_factor * year
        year += 1
    cf_sum = price + cf_sum
    pv_sum = price * n + pv_sum
    if frequency == 2:
        mac_duration = (pv_sum / cf_sum) / 2
        mod_duration = mac_duration / (1 + y)
    elif frequency == 1:
        mac_duration = pv_sum / cf_sum
        mod_duration = mac_duration / (1 + y)
    return mac_duration, mod_duration


# Input for the Function
face_value = 1000  # Value in USD
coupon_rate = 0.05  # Coupon Rate as a Decimal  == 5 %
time_to_maturity = 10  # Years to Maturity
yield_rate = 0.06  # Yield to Maturity in Per Cent as a Decimal == 6 %
frequency = 2  # 2 for semi-annual coupon payments, 1 for annual coupon payments

mac_duration, mod_duration = (bond_duration(face_value, coupon_rate, time_to_maturity, yield_rate, frequency))

print("Macaulay Duration: {:.3f} years".format(mac_duration))
print("Modified Duration: {:.3f}".format(mod_duration))




