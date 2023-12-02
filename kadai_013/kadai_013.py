def getPriceWithTax(price, tax_rate):
  tax_rate = tax_rate / 100
  return price * (1 + tax_rate)

print(getPriceWithTax(100, 10))
print(getPriceWithTax(100, 20))
print(getPriceWithTax(500, 4))