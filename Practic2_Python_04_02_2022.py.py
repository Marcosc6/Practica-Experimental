Lv_Frase1=input("Ingrese frase:");

print("Dentro de su frase existe 'a'",Lv_Frase1.count('a'));
print("Dentro de su frase existe 'A'",Lv_Frase1.count('A'));
print("Esta es su frase si reemplazamos la 'a' por la 'e':", Lv_Frase1.replace('a','e'))


print(f"La frase ingresada es:{Lv_Frase1}");
print("-------------------------");

print("La subfrase 'ta' ¿Existe dentro de la frase?:",'ta' in Lv_Frase1);
print("-------------------------");

print("La subfrase 'ta' ¿No existe dentro de la frase?:",'ta' not in Lv_Frase1);