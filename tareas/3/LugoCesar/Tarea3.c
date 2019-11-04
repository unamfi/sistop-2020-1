#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <time.h>

char memory[31];

char nameNewProcess(){
  int i = 0, j = 0;
  for(i = 0; i < 30; i++){

    if (memory[i] > j){

      j = memory[i];

    }
  }
  return j+1;
}


void initMem() {

  int index = 0;
  int i = 0;

  while (i < 30){

    if (rand()%3 == 0){
      int sizeSp = rand()%4 + 2; 

      for (j = 0; j < sizeSp; j++){
          memory[i] = '-';
          i++;

          if (i >= 30){
            break;
          }
      }
    }

    else {
      int sizeSp = rand() %14 + 2;
      int j = 0;

      for(j = 0; j < sizeSp; j++){
        memory[i] = 'A' + index;
        i++;
        if (i >= 30){
          break;
        }
      }
      index++;
    }
  }
  memory[30] = '\0';
}


int searchFirstAdjust(int size){

  int i = 0;
  int j = 0;

  for(i = 0; i < 30; i++){

    if (memory[i] == '-'){
      j++;

      if (j == size){
        return i - size+1;
      }
    }

    else {
      j = 0;
    }
  }
  return -1;
}


void compactMem(){

  int i = 0;

  for (i = 0; i < 30; i++){

    if (memory[i] == '-'){

      int j = i;

      while(j < 30 && memory[j] == '-'){
        j++;
      }

      if (j < 30){

        memory[i] = memory[j];
        memory[j] = '-';
      }
    }
  }
}

int main(void) {

  int reply = 0;
  srand(time(NULL));
  initMem();

  for(;;){

    printf("Asignacion actual:\n\n%s\n Asignar (0) o Liberar (1): ",memory);
    scanf("%i", &reply);

    if (reply == 1){

      printf("Proceso a liberar (ABCDEFGHI): ");
      char process[2];
      scanf("%s", process);
      int i = 0;
      for(i = 0; i < 30; i++){

        if(memory[i] == toupper(process[0])){
          memory[i] = '-';
        }
      }
    }
    else{


      char name = nameNewProcess();
      printf("Nuevo proceso (%C): ",name);
      scanf("%i",&reply);

      while(reply < 2 || reply > 15){

        printf("Valor incorrecto.\nEl tamanio de memoria del proceso de estar entre los valores 2-15:");
        scanf("%i", &reply);
      }

      int memoryPlace = searchFirstAdjust(reply);

      if(memoryPlace != -1){

        int i = 0;

        for (i = 0; i < reply; i++){

            memory[memoryPlace + i] = name;
        }
      }

      else {

        compactMem();
        printf("***Compactacion requerida***\n Nueva situacion: \n%s\nAsignando a %C...\n",memory, name);
        memoryPlace = searchFirstAdjust(reply);

        if (memoryPlace != -1){

          int i = 0;
          for (i = 0; i < reply; i++){

            memory[memoryPlace + i] = name;
          }
        }
        else{
          printf("Memoria insuficiente para el proceso\n Libera uno o mas procesos. \n");
        }
      }
    }
  }
  return 0;
}
