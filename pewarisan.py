class unggas(object) :
	def sifatUnggas(self) :
		print ("\tBertelur\t")
		print ("\tBersayap\t")
		
class bebek(unggas) :
	def sifatBebek(self) : 
		print ("\tBerenang\t")

class ayam(unggas) :
	def sifatAyam(self) :
		print ("\tBerkokok\t")


#inisialisasi		
unggas = unggas()
ayam = ayam()
bebek = bebek()

print ("Unggas itu\t : ")
unggas.sifatUnggas()


print ("Ayam itu\t : ")
ayam.sifatUnggas()
ayam.sifatAyam()


print ("Bebek itu\t : ")
bebek.sifatUnggas()
bebek.sifatBebek()
        
