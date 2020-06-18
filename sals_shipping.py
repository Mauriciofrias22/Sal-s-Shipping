#function to calculate ground shipping cost
def cost_of_ground_shipping(weight):

  if weight <= 2:
     price_per_pound = 1.50
  elif weight <= 6:
     price_per_pound = 3.00
  elif weight <=10:
     price_per_pound = 4.00
  else:
     price_per_pound = 4.75

  return (price_per_pound * weight) + 20

print(cost_of_ground_shipping(8.4))

#premium ground cost
cost_of_premium_ground_shipping = 125.00

#function to calculate drone shipping cost
def cost_of_drone_shipping(weight):

  if weight <= 2:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.0
  elif weight <=10:
     price_per_pound = 12.0
  else:
     price_per_pound = 14.25
  return (price_per_pound * weight)

print(cost_of_drone_shipping(1.5))

#function to calculate cheapest shipping method
def print_cheapest_shipping_method(weight):
  ground = cost_of_ground_shipping(weight)
  premium = cost_of_premium_ground_shipping
  drone = cost_of_drone_shipping(weight)

  if ground < premium and ground < drone:
    method = "ground shipping"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium ground shipping"
    cost = premium
  else:
    method = "drone shipping"
    cost = drone

  print(
    "The cheapest option available is $%.2f with  %s shipping."
  %   (cost, method)
)

print_cheapest_shipping_method(4.8)
print_cheapest_shipping_method(41.5)
