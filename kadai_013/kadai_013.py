def getPriceWithTax(price, tax_rate = 0.1):
  if(tax_rate > 1):
    return 'tax_rateは1以下の数字を入力してください'
  return price * (1 + tax_rate)

print(getPriceWithTax(100))
print(getPriceWithTax(100, 0.2))
print(getPriceWithTax(100, 4))