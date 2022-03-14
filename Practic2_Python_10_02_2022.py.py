#File
f=open("PrimerFile.text",'w');
try:
    f.write("Esta es mi primera linea en el file \n");
    f.write("Esta es mi segunda linea en el file \n");
    f.write("Esta es mi tercera linea en el file \n");
    f.write("Esta es mi cuarta linea en el file \n");
    f.write("Total de linea escritas 4 \n");
finally:
    f.close();

### Para Leee
f=open("PrimerFile.text",'r');
Lv_Mensaje=f.read();
print(Lv_Mensaje);
f.close();

###  Para Agregar

f=open("PrimerFile.text",'a');
f.write("Esta es una linea nueva, osea en la 5");
f.close();

### Para Leer
f=open("PrimerFile.text",'r');
Lv_Mensaje=f.read();
print(Lv_Mensaje);
f.close();