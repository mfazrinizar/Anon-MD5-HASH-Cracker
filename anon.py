# !/usr/bin/python
# Creator : Anon6372098
# Team : D4RK SYST3M F41LUR3 S33K3R

# Persiapan Alat Tempur :V
import md5, sys

# Intro Dulu ea :V 
anon = """
   ###    ##    ##  #######  ##    ##    ##     ## ########  ########    ##     ##    ###     ######  ##     ## 
  ## ##   ###   ## ##     ## ###   ##    ###   ### ##     ## ##          ##     ##   ## ##   ##    ## ##     ## 
 ##   ##  ####  ## ##     ## ####  ##    #### #### ##     ## ##          ##     ##  ##   ##  ##       ##     ## 
##     ## ## ## ## ##     ## ## ## ##    ## ### ## ##     ## #######     ######### ##     ##  ######  ######### 
######### ##  #### ##     ## ##  ####    ##     ## ##     ##       ##    ##     ## #########       ## ##     ## 
##     ## ##   ### ##     ## ##   ###    ##     ## ##     ## ##    ##    ##     ## ##     ## ##    ## ##     ## 
##     ## ##    ##  #######  ##    ##    ##     ## ########   ######     ##     ## ##     ##  ######  ##     ## 

 ######  ########     ###     ######  ##    ## ######## ########                                                
##    ## ##     ##   ## ##   ##    ## ##   ##  ##       ##     ##                                               
##       ##     ##  ##   ##  ##       ##  ##   ##       ##     ##                                               
##       ########  ##     ## ##       #####    ######   ########                                                
##       ##   ##   ######### ##       ##  ##   ##       ##   ##                                                 
##    ## ##    ##  ##     ## ##    ## ##   ##  ##       ##    ##                                                
 ######  ##     ## ##     ##  ######  ##    ## ######## ##     ## 

 
\t\t+=================================================+
\t\t+      Creator  : Anon6372098                     +
\t\t+      Contact  : anon6372098.id@gmail.com        +                             
\t\t+      Team     : D4RK SYST3M F41LUR3 S33K3R      +
\t\t+      Homepage : https://www.dsfs-indo.zone.id/  +                                       
\t\t+      Thanks to: All Member of DSFS Official     +
\t\t+      GitHub   : https://github.com/Anon6372098/ +       
\t\t+=================================================+
"""
print anon

# Waktunya Beraksi :)
if len(sys.argv) != 3:
    print "\n Penggunaan : python anon.py <hash> <tempat wordlist>"
    sys.exit(1)
   
anon1 = sys.argv[1]
anon2 = sys.argv[2]
try:
  anon3 = open(anon2, "r")
except(IOError):
  print "[-] Cek input tempat wordlist mu\n"
  sys.exit(1)
anon3 = anon3.readlines()
print "\n",len(anon3),"[+] Wordlist dimuat..."
anon7=open('hash.txt','a')
for anon4 in anon3 :
    anon5 = md5.new(anon4[:-1])
    anon6 = anon5.hexdigest()
    if anon1 == anon6:
        print "[+] Passwordnya adalah :",anon4,"\n"
        anon7.write("\n [+] Hashes berhasil dicrack ! :)\n\n")
        anon7.write(anon1+"\t\t")
        anon7.write(anon4+"\n")