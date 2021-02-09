# ubacivanje koda u simon says pomocu stlinka, u terminalu kaze da li je ok ili je tries excededd, i ja iz terminala povucem taj string i ispisujem da li je uspjesno ili neuspjesno isprogramirano
import os
import board
import neopixel
import subprocess
pixels = neopixel.NeoPixel(board.D18, 25)
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN, pull_up_down = gpio.PUD_UP)
print('Script for programming multiple STM8 MCUs has started\nFor exit press CTRL+Z')


#----------------------------------------------------START OF DEF programming----------------------------------------------------
def programming(channel):
	# U listy polijepiš odgovor iz terminala, prvo u terminalu pokreneš Ispisivanje_serijskih_brojeva, dobiješ odgovor ( serijske brojeve i ovdje polijepiš)
	listy = ['640047001200005153484c4e', '64005200050000315037504e', '54000800040000315037504e', '63004800050000315037504e', '470032001100005153484c4e', '312f0d002c135737334d4e00', '59001800050000315037504e', '59001200050000315037504e', '58003200050000315037504e', '46002600020000315037504e']
	STLinkCount = len(listy)  # broj ST Linkova
	
	#Lista u koju se stavljaju odgovori od terminala od svih STLinkova
	outputStr = []
	while len(outputStr) <= STLinkCount: 
		outputStr.append([])  #U listu outputStr stavlja elemente koji su lista (lista u listi)

	pixels.fill((0, 0, 0))  
	#pixels.show()   
	t = 0
	k = 0
	n = 0
	x = 0

	#timeutil.get_epochtime_ms()
	succ = [0 for i in range(STLinkCount)]

	#list3 = []
	while x < STLinkCount:     # sve dok je index u polju pocevsi od 0 manji od zadnjeg index-a u polju ucini sljedece
		#from subprocess import Popen, PIPE	
		outputStr[x] = subprocess.Popen(['sudo' , 'stm8flash','-c' , 'stlinkv2', '-p' , 'stm8s001j3' ,'-w', 'led_blink.hex', '-S' , listy[x].upper()], shell = False, stdout = subprocess.PIPE, stderr=subprocess.STDOUT)    # pozivanje popena, dakle pozivanje st linkova
		#listy=su470032001100005153484c4ebprocess.Popen("pgrep -u root", stdout= subprocess.PIPE, shell = True)
		x+=1
		time.sleep(0.05) # Kratki delay između slanja zbog hub-a 
	print('Programiranje je u tijeku...')

	if x == 0:
		print('Greška na hub-u, restartiraj hub')	
		exit()
			
	#print('\n\nOut{x}:\n')
	#print(outputStr[0].stdout.readlines())     #odgovor od st linka

	t = round(time.time())    # uzimanje minutne vrijednosti i zaokruživanje
	n = 0
	k = 0

	while ((k < STLinkCount) and ((round(time.time()) - t) < 10)):  # dok je index k manji od zadnjeg indexa u listy i dok je vrijeme manje od imeouta(vrijeme u sek), u ovoj petlji gledam da li ima odgovora od st linka, tj provjeravam ih i parsiram
		if ((outputStr[n].poll() != None) and (succ[n] == 0)): # ako je odgovor od st linka različit od None(dakle ako postoji odgovor) i ako je succ[n] == 0 ( ako je succesfull jednako false
			line = str(outputStr[n].stdout.readlines())  # spremi u polje line, odgovor od st linka u obliku stringa i citaj ga
			if 'OK' in line:  # ako si nasao ok u stringu tj ako je True	
				print('Uspjesno')	
				pixels[n] = (0, 255, 0) #postavljanje zelene boje
				#pixels.show()  #paljenje ledice
			
			elif 'Tries' in line: # ako si nasao Tries onda ucini sljedece
				print('Neuspjesno')
				pixels[n] = (255, 0, 0)  #postavljanje crvene boje
				#pixels.show()
			#time.sleep(5)
			#pixels.fill((0,0,0))
			else:
				print('Greska')
				pixels[n] = (255, 32, 0)   #postavljanje narancaste boje
				#pixels.show()
			succ[n] = 1  # succesfull od n tog st linka je true
			k+=1  # povecaj k za jedan, dakle idi na sljedeci st link
		n+=1  # idi dalje sa indexom u polju succ
		if(n > (STLinkCount - 1)): n = 0   # ako je n koji je u polju succesfull odnosno ako je uspješnan odgovor veci od duljine listey, n stavi na 0 dakle stavi na false  i idi ispocetka
		
		
		
		
		#while (outputStr[x].poll() == False):
		#	pass
		
		#time.sleep(5)
		#print('\n\nOut{x}:\n')
		#print(outputStr[x].stdout.readlines())
#----------------------------------------------------END OF DEF programming----------------------------------------------------

gpio.add_event_detect(17, gpio.FALLING, callback = programming, bouncetime = 700)
while 1:
	time.sleep(360)
