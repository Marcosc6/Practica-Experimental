### Funciones

def Fnc_Calculo(In_Valor1,In_Valor2,Iv_Proceso):
    if(Iv_Proceso=="1"):
       print(In_Valor1+In_Valor2);
    elif(Iv_Proceso=="2"):
       print(In_Valor1-In_Valor2);
    elif(Iv_Proceso=="3"):
       print(In_Valor1*In_Valor2);
    else:
       print(In_Valor1/In_Valor2);

Ln_Valor1=int(input("Ingrese valor #1:"));
Ln_Valor2=int(input("Ingrese valor #2:"));


print("¿Que cálculo desea realizar?");
print("1.-Suma");
print("2.-Resta");
print("3.-Multiplicación");
print("4.-División");

Lv_Proceso=(input("Digite su opción:"))
Fnc_Calculo(Ln_Valor1,Ln_Valor2,Lv_Proceso);