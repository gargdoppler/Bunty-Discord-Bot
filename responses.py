import random

sys_random = random.SystemRandom()

bet_placed = ["Lagadi Bhau, All The Best", "Bhau aapich jeetoge likh ke dera mai", "Ok bhai, abhi lagara", "Bhau, mereko lag nahi rha aap jeetoge, change karlo", "Bhau aap rakam bolo, abhich fix karke aata hu mai ye match"]

bet_not_placed = ["Bhau, aaj ye team ka match thode hi hai", "Bhau aap mere bina daaru pine lag gye ho kya", "Bhau ye Majumdar se charas kyon lete ho aap, apun dega na badhia wala maal", "Bhau check karlo aaj iska match hai bhi ya nahi", "bhau team ka naam toh sahi daalo"]

cheater = ["Bhau kya cheating kar rhe ho aise 🙃", "Kya bhau aap toh late hogye", "Bhau bakchodi nahi karne ka, rules are rules", "Bhau boleto 100 rupay table ke niche se sarka doge toh laga dunga mai, par aise toh nahi laga sakta", "Bhau mereko galat kaam karne ko bol rhe ho aap, sahi nahi hai ye", "Bunty toh chutiya hai, tu banayega aur mai banjaunga"]

jhand_text = ["Qagaar ke chode mujhe order dene ke liye lund khada karna padta hai 🖕", "Chal chutiye teri kaun sun rha", "Bsdk lund 1 inch ka hai nahi, mereko aankhein dikha rha", "Bunty naam hai mera, yahan se lund fek ke maarunga, pura palwal chudh jayega", "Abhi time hai nikal le hijde, warna gaand mai goli maarunga orgasm aajayega"]

movie_absent = ["Bhau maine kalich dekhi hai ye movie, ek number choice bhau, ek number 😎", "Daaldi bhau list mai", "Bhau ye movie kab aayi thi?", "Bhau apun ko toh angrezi filmein bohot pasand hai, samjh kuchh nahi aata par maja bada aata hai", "Bhau apun ko bhi bula lena jab ye movie dekhoge"]

movie_present = ["Bhau ye movie toh pehle se hi list mai hai", "Bhau ye movie pehle koi daal chuka hai list mai", "List mai already hai ye movie bhau", "Bhau ye toh dekh chuke ho aap"]

allot_bet = ["Chalo ramji ki kripa se sabne bets lagayi hai aaj. Sabko bunty ki taraf se all the best", "Sabne bets lagayi hai aaj toh maja aayega", "Aaj kisi ki random nahi lagani padi mujhe"]

no_user_mentioned = ["Bhau kisika naam toh lo", "bhau kiske points batane hai?", "Bhau thoda clearly bologe kya, apun ko samjha nahi kiske points maangrele tum"]

def betPlaced():
	return sys_random.choice(bet_placed)

def betNotPlaced():
	return sys_random.choice(bet_not_placed)

def cheating():
	return sys_random.choice(cheater)

def jhand():
	return sys_random.choice(jhand_text)

def addMoviePresent():
	return sys_random.choice(movie_present)

def addMovieAbsent():
	return sys_random.choice(movie_absent)

def allotBet():
	return sys_random.choice(allot_bet)

def noUserMentioned():
    return sys_random.choice(no_user_mentioned)
