#include <iostream>
#define limite 3
using namespace std;


void insertar(char datos[],int tiempo[],int l)

    {
    for(int i = 0; i < (l); i++)
        {
        cout << "inserte el tiempo en el proceso [" << datos[i] << "]: ";
        cin >> tiempo[i];
        }
    }

void FCFS(char datos[],int tiempo[], int l)

    {
    int tiempoTotal = 0;
    int tiempoEspera = 0;
    float tiempoReturn = 0.0f;
    insertar(datos,tiempo, l);

    for(int j = 0;j < l; j++)
        {
        tiempoTotal += tiempo[j];
        tiempoReturn += tiempoTotal;
        tiempoEspera += (tiempoTotal-tiempo[j]);
        cout <<"\n\t""Proceso \t"<<datos[j]<<"\t";
        cout <<"\n""tiempo total     T de ["<<datos[j]<<"]: "<<tiempoTotal<<"\t";
        cout <<"\n""tiempo de espera E de ["<<datos[j]<<"]: "<<tiempoEspera<<"\t";
        cout <<"\n\t";
        }

    tiempoReturn = tiempoReturn / l;
    cout<<"\nEl tiempo promedio de las entradas para FCFS son: "<<tiempoReturn<<endl;;
    cout<<"\t\t_______________________________________\n"<<endl;
    }


int quantum(int tiempo[],int numero)
    {
    int resultado = 0;
    for(int i = 0; i < numero;++i)
        {
        resultado += tiempo[i];
        }

    resultado /= numero;
    return resultado;
    }

void RoundRobin(char datos[], int tiempo[], int numero)

    {
    //insertar(datos,tiempo, numero);
     /*cout<<"\t\t\n"<<endl;
    cout<<"El quantum es: "<< Quantum <<endl;*/
    int Quantum = quantum(tiempo,numero);
    int tiempoFinal = 0;
    float suma = 0.0f;
    int m = 0;
    int i = 0;

    do
        {
        tiempo[i] != 0 ? tiempo[i] -= Quantum : ++i;

        if(tiempo[i] > 0)
            {
            tiempoFinal += Quantum;
            }
        else
            {
            tiempoFinal += Quantum+tiempo[i];
            suma += tiempoFinal;
            cout <<"tiempo total T de proceso de["<<datos[i]<<"]: "<<tiempoFinal << endl;
            m++;
            }

        i < (numero - 1) ? i++ : i = 0;
        }
    while(m < numero);
        suma /= numero;
        cout << "Tiempo promedio de los procesos para RoundRobin es: "<< suma << endl;
}



int main()
    {
    cout<<"\t\t\tSimulacion de FCFS y Round Robin"<<endl;
    cout<<"\n"<<endl;
    char datos[limite] = {'1','2','3'};
    int tiempo[limite];
    FCFS(datos,tiempo,limite);
    RoundRobin(datos,tiempo,limite);
    //cin.get();
    //cin.get();
    return 0;
}
