print("---------Variables numerica----------");

Ln_Valor=int(input("Ingrese valor #1:"));
print(Ln_Valor * 3);
print("Cuantos días quieres libres:"+ str(Ln_Valor))
print("-------------------------");

print("Todos los días es Lunes.")
print("Todos los días es Miercoles.\n")
print("Todos los días es Viernes.")
print("-------------------------");

print("Ingrese 'S' para continuar.");
print('Ingrese "S" para continuar.');
print("-------------------------");

Lv_Nombre=input("Ingrese su nombre:");
Lv_Apellido=input("Ingrese su apellido:");

print("Su nombre escrito en mayuscula es:", Lv_Nombre.upper());
print("Su nombre escrito en minuscula es:", Lv_Apellido.lower());
print("Su nombre tiene un total de:", len(Lv_Apellido));
print("-------------------------");

Lv_Frase1=input("Ingrese frase:");

print("Dentro de su frase existe 'a'",Lv_Frase1.count('a'));
