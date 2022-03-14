Lst_Temp1=['Lunes','Martes','Miercoles','Jueves','Perro'];

print("-----------------");

print(Lst_Temp1);

print("-----------------");

Lst_Temp1.remove('Jueves');
print(Lst_Temp1);

("-----------------");

Lst_Temp1.append('Viernes');
Lst_Temp1.append('Viernes');
Lst_Temp1.append('Viernes');
Lst_Temp1.append('Viernes');
print(Lst_Temp1);

("-----------------");
Lst_Temp1.remove('Viernes');
print(Lst_Temp1);

("-----------------");
Lst_Temp2=['Marcos','Adrian','Andres','Erick','Hector'];
Lst_Temp2.sort();
Lst_Temp2.pop();
print(Lst_Temp2);

print("*************************************************************");
if 'Luan' in Lst_Temp2:
    print("Si existe Erick");
elif 'Juan' in Lst_Temp2:
    print("Si existe Andres");
else:
    print("No existen los nombres buscados");

print("*************************************************************");
if 'Juan' and 'Luan'in Lst_Temp2:
    print("Adrian esta dentro de la lista")
else:
    print("Adrian esta dentro de la lista")

if 'Juan' or 'Luan'in Lst_Temp2:
    print("Uno de los dos esta dentro de la lista");
else:
    print("No existen");