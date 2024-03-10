import serial
import pynmea2
import datetime
import calendar
import time
import sys
import os
from datetime import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('/home/pi/sailtrack/sailing-track-pkey.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {'databaseURL': "https://sailing-track-default-rtdb.firebaseio.com"})

id=sys.argv[1]
voyage=sys.argv[2]
secondes_sleep=int(sys.argv[3])


i=0
nbError=0

lastDataOk = "1"


#print(str(i)+"  Attente secondes:"+str(secondes_sleep))
#time.sleep(secondes_sleep)

print("Demarrage programme.... ")
time.sleep(5)
print(".... ")
time.sleep(5)

myref = id+"/"+voyage
print("ref="+myref)
ref = db.reference(myref)

ref_racine = db.reference("/")
#print("ref firebase racine="+str(ref_racine.order_by_key().limit_to_first(1).get()))

now = datetime.now()
dname=str(now.year)+"_"+str(now.month)+"_"+str(now.day)+"_"+str(now.hour)+"_"+str(now.minute)+"_"+str(now.second)

#nom fichier pour vrai tracker
fcurent_name="/media/pi/DATA/data_"+voyage+"_"+dname+".csv"

#nom fichier pour env dev (penser a commenter)
#fcurent_name="/home/pi/sailtrack/DATA/data_"+voyage+"_"+dname+".csv"
f = open(fcurent_name, "a")
f.write("latitude,longitude,date,dtl"+"\n")

#nom fichier pour vrai tracker
frecap_name="/media/pi/DATA/data_"+voyage+".csv"

#nom fichier pour env dev  (penser a commenter)
#frecap_name="/home/pi/sailtrack/DATA/data_"+voyage+".csv"

if os.path.isfile(frecap_name):
    frecap = open(frecap_name,"a+")
else:
    frecap = open(frecap_name,"a+")
    frecap.write("latitude,longitude,date,dtl"+"\n")

while True:
    try:	 
        port="/dev/ttyAMA0"
        # baud rate 4800 9600 19200 38400 57600 1152000
        ser=serial.Serial(port, baudrate=9600, timeout=0.5)
        dataout = pynmea2.NMEAStreamReader()
        newdata=ser.readline()
        n_data = newdata.decode('latin-1')
        # attention dans le BN220 on doit etre en nmea 4.0 sinon pynmea2 est perdu....
        if n_data[0:6] == '$GNRMC':
            newmsg=pynmea2.parse(n_data)
            ok=newmsg.is_valid

            if (ok):
                lat=newmsg.latitude
                lng=newmsg.longitude
                dt=newmsg.datetime
                dtl = calendar.timegm(dt.timetuple())*1000
                lat_f8 = "{:.{prec}f}".format(lat,prec=8)
                lng_f8 = "{:.{prec}f}".format(lng,prec=8)
                
                # on ecrit dabord dans fichiers
                gps = str(lat_f8) + "," + str(lng_f8)+ "," + str(dt)+ "," +str(dtl)
                gps_log = str(lat_f8) + "," + str(lng_f8)+ "," + str(dt)
                
                f.write(gps+"\n")
                f.flush()

                frecap.write(gps+"\n")
                frecap.flush()
                
                if (nbError>0):
                      print("Input file:"+gps_log)
                      
                # on teste si cnx internet firebase OK
                # si erreur c'est souvent ici! (pas de cnx reseeau wifi ou pb reseau) on part là vers le catch error 
                # position quand meme ecrite avant dans fichier pour reprise 
                test_cnx = ref_racine.order_by_key().limit_to_first(1).get()
                #la si erreur reseau premiere attente de cnx peut durer longtemps... bloqué ici attendre jusqu'a l'exception
                # qui sera renouvelée ensuite regulierement suivant le sleep defini dans le bloc exception     

                # si cnx retouvée on arrive ici avec nbError>0 et positions ecrites dans fichier a inserer dans firebase
                if (nbError>0):
                     print("***Cnx internet OK: List Input internet" )
                     with open(fcurent_name, 'r') as fp:
                        # read all lines using readline()
                        lines = fp.readlines()
                        nb_lines=len(lines)
                        trouve=False
                        for row in lines:
                             # si trouve==True : toutes les lignes suivantes jusqu'a la fin sont a inserer   
                             if trouve==True:
                                    lst = row.split(',')
                                    lat_r = lst[0]
                                    lng_r = lst[1]
                                    dt_r  = lst[2]
                                    dtl_r = int(lst[3])
                                    
                                    # ne pas prendre la derniere ligne
                                    if  nb_lines > (lines.index(row)+1) :
                                           #print( str(lines.index(row)+1)+" / "+str(nb_lines) )   
                                           data_r = {"LAT": lat_r, "LNG": lng_r , "DT": dtl_r, "COMMENT":"", "IMAGEURL":"", "LIENVIDEO":"","ANCRE":0,"VRV":0,"VRA":0,"VAV":0,"VAA":0}
                                           ref.push().set(data_r)
                                           print("*** "+str(lines.index(row)+1)+"/"+str(nb_lines)+" "+str(lat_r)+","+str(lng_r)+","+str(dt_r)) 
                                    
                             # find() method returns -1 if the value is not found,
                             # if found it returns index of the first occurrence of the substring
                             if row.find(lastDataOk) != -1:
                                      #print("***Reprise données à partir de la position:"+str(row))
                                      trouve=True
                             else:
                                      if lastDataOk=="1":
                                              #print("***Reprise données à partir de la premiere position:"+str(row))
                                              trouve=True
                                              
                        
                        # sortie de boucle : si recup dans fichier ok et maj firebase OK
                        nbError=0
                        
                # Là tout va bien : ecriture fichiers OK   et cnx OK   
                data = {"LAT": lat_f8, "LNG": lng_f8 , "DT": dtl, "COMMENT":"", "IMAGEURL":"", "LIENVIDEO":"","ANCRE":0,"VRV":0,"VRA":0,"VAV":0,"VAA":0}
                ref.push().set(data) 
         
                                
                print("Input file+internet:"+gps_log)
                # si tout s'est bien passé lastDataOk = gps
                lastDataOk = gps
 
                i=i+1
                if (i>9999):
                     i=0 

                print(str(i)+"  Attente secondes:"+str(secondes_sleep))
                time.sleep(secondes_sleep)
            else:
                i=i+1
                # print(newmsg)
                print(str(i)+"  En attente Position GPS...")
            
    except Exception as error:
            i=i+1
            nbError=nbError+1
            #print("  Erreur numero "+str(nbError), error)
            print(str(i)+"  ERREUR attente secondes:"+str(secondes_sleep))
            time.sleep(secondes_sleep)

f.close()
frecap.close()
 
  
	 
     
                   