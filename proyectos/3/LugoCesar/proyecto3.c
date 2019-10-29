#include <dirent.h>
#include <stdio.h>
/* La verdad no estoy seguro de lo que estaba haciendo, creo que el codigo
no se acerca a la solucion pero no se me ocurrio nada más :'(*/

//int int main(void) {

  int select;
  printf("Seleccione alguna opcion:\n");
  printf("1.-Lista de contenidos\n");
  printf("2.-Copiar uno de los archivos FiUnamFS -> Sistema\n");
  printf("3.-Copiar uno de los archivos Sistema -> FiUnamFS\n");
  printf("4.-Eliminar un archivo del FiUnamFS\n");
  printf("5.-Desfragmentante\n");

  scanf("%d", &select);
  switch (select) {
    case 1:listDir();
    case 2:copFile();
    case 3:copFile();
    case 4:rmFile(1,[1]);
    case 5: defragment();
    default:
      printf("Opcion no valida\n", );
  }


  return 0;
}

int listDir(void) {
  DIR *d;
  struct dirent *dir;//apuntador a la entrada del directorio
  d = opendir("."); //opendir nos regresa un apuntador del tipo DIR

  if (d == NULL){
    printf("Could not open current directory");
    return 0;

  }

  if (d) {
    while ((dir = readdir(d)) != NULL) {
      printf("%s\n", dir->d_name);
    }
    closedir(d);
  }
  return(0);
}

int copFile(){

      FILE *fptr1, *fptr2;
      char filename[100], c;

      printf("Enter the filename to open for reading \n");
      scanf("%s", filename);

      // Esta parte es para abrir el archivo
      fptr1 = fopen(filename, "r");
      if (fptr1 == NULL)
      {
          printf("Cannot open file %s \n", filename);
          exit(0);
      }

      printf("Enter the filename to open for writing \n");
      scanf("%s", filename);


      fptr2 = fopen(filename, "w");
      if (fptr2 == NULL)
      {
          printf("Cannot open file %s \n", filename);
          exit(0);
      }

      // leemos el contenido del archivo
      c = fgetc(fptr1);
      while (c != EOF)
      {
          fputc(c, fptr2);
          c = fgetc(fptr1);
      }

      printf("\nContents copied to %s", filename);

      fclose(fptr1);
      fclose(fptr2);
      return 0;
}
void rmFile(int argc, char* argv[]){
if(argc!=2 || argv[1]=="--help")
  {
    printf("\nusage: rm FileTodelete\n");
  }
int status;
status=remove(argv[1]);
if(status==0)
  {
    printf("successfull\n");
  }
else
   {
    printf("Unsuccessfull\n");
   }
}

void defragment(Pool* pool)
{
    if(pool && pool->root)
    {
        Block* current = pool->root;

        while(current)
        {
            if(!current->free)
            {
                Block* current_prev = current->prev;

                if(current_prev && current_prev->free)
                {
                    Block* prev_prev = current_prev->prev;
                    int new_block_size = current_prev->size;

                    Block* moved_current = memmove(current_prev, current, sizeof(Block) + current->size);

                    if(!moved_current)
                    {
                        printf("couldn't move memory\n");
                    }
                    else
                    {
                        Block* new_block = initBlock((((char*)moved_current) + sizeof(Block) + moved_current->size), new_block_size);
                        new_block->prev = moved_current;
                        new_block->next = moved_current->next;

                        moved_current->prev = prev_prev;
                        moved_current->next = new_block;

                        if(prev_prev)
                        {
                            prev_prev->next = moved_current;
                        }

                        current = moved_current;
                        continue;
                    }
                }
            }

            current = current->next;
        }
    }
}
