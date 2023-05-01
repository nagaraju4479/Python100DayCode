your_name = input("inter your name : ").lower()
your_partner_name = input("Your partner name : ").lower()

true_letters={'t':0 , 'r':0, 'u':0, 'e':0}
love_letters={'l':0, 'o':0, 'v':0, 'e':0}

#Logic
for name in [your_name,your_partner_name]:
   for letter in true_letters:
      true_letters[letter] += name.count(letter)
sum_truecount = sum(true_letters.values())

for name1 in [your_name,your_partner_name]:
   for letter1 in love_letters:
      love_letters[letter1] += name.count(letter1)
sum_loveCount = sum(love_letters.values())

true_value = str(sum_truecount)
love_value = str(sum_loveCount)

print(f"Love Score : {true_value}{love_value}")