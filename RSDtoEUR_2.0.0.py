#	//////Start//////
RSDtoEUR = True
bool('RSDtoEUR')
ConState = False
ReCon = False

if RSDtoEUR == True:
	print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
	print('	  Welcome to RSD to EUR Converter [2023] by')
	print('		    Lazar Stankovic <5964>')
	print('		   Metropolitan  University')
	print(' ')
	print(' 		  	 Version, 2.0.1')
	print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
	print(' ')
	var1 = input('Begin Conversion? [Y/N]) ')
	print(' ')
elif RSDtoEUR == False:
	print(' ')

if var1 == ("Y"):
	ConState = True
elif var1 == ("N"):
	ConState == False
	RSDtoEUR = False
	
while ConState == True:
	print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
#	//////Iznos u dinarima//////
	RSD_Iznos = float(input('Enter RSD amount: '))
	print(' ')
	
#	//////Konverzija Kursa//////
	Kurs = 117

#	//////Iznos u Evrima//////
	EUR_Iznos = RSD_Iznos / Kurs
	print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
	print(RSD_Iznos, ' RSD = ', EUR_Iznos, '€')
	print(' ')
	ReCon = input('Would you like to covert again? [Y/N] ')
	
	if ReCon == ("Y"):
		print(' ')
	elif ReCon == ("N"):
		ConState = False
		
if ConState == False:
	RSDtoEUR = False