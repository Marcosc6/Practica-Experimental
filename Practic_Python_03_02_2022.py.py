print("-------------------------");
print("Hola Mundo!");

print("Hola Mundo!");
print("-------------------------");

print(2+2);
print(5-2);
print(3*3);
print(2/2);
print(2+2*5/8);
print(((2+2)*5)/8);
print("-------------------------");

print("----------Cadena de caracteres---------------");
Lv_Temp="Hola Python"

print(Lv_Temp[5]);
print(Lv_Temp[5:11]);
print(Lv_Temp + "T");
print((Lv_Temp + " ") * 3);
print("-------------------------");

print("-----------Listas------------");
Lst_Temp=["Marcos","Alvarez",2022,15,7.50];

print("------*Listas - Impresión*--------");
print(Lst_Temp);

print("------*Listas de Posición*--------");
print(Lst_Temp[4]);

print("------*Listas de Rango de Valores*--------");
print(Lst_Temp[2:5]);
print(Lst_Temp[2]);
print((Lst_Temp[0]+ " " + Lst_Temp[1] + " ") * 3);

print("-------------*Tuplas*------------");
Tpl_Temp=('Agromatica','Programación','Seguridad','Construcción' , 2022,7.50);

print("------*Tuplas - Impresión*--------");
print(Tpl_Temp);

print("------*Tuplas - Posición*--------");
print(Tpl_Temp[3]);


print("------*Tuplas - Rango de Valores*--------");
print(Tpl_Temp[3]);
print(Tpl_Temp[1:4]);
print(Tpl_Temp[1]+ " " + Tpl_Temp[2] + " ")
print((Tpl_Temp[1]+ " " + Tpl_Temp[2] + " ") * 3);

print("-----------Diccionario--------------");
Dct_Materia= {'Nombre_Materia':'Agromatica','Estado':'Activo'};
print(Dct_Materia['Nombre_Materia']);
print(Dct_Materia['Estado']);
print(Dct_Materia.keys());
print(Dct_Materia.values());

print("-------------Variables------------");

Lv_Nombre='';
print("Hola, ingrese su nombre:")
Lv_Nombre= input();
print("Gusto en conocerte, "+ Lv_Nombre);

print("Hola, ingrese su apellido:")
Lv_Apellido= input();
print(f"Gusto en conocerte,{ Lv_Apellido}");

Lv_Usuario= input("Ingrese su Usuario:")
print(f"Ingreso exitoso,{Lv_Usuario}");

