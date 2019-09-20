**Alumno**: Martínez Ostoa Néstor Iván 
**Materia**: Sistemas Operativos 
**Semestre**: 2020-1

---

**Problema**: Santa Claus 
**Lenguaje**: Python3
**Estrategia**: 

- *Mutex* para proteger variables compartidas. 
- *Señalización* para el funcionamiento de Santa Claus. Si el hilo de Santa llega antes de que la cantidad de elfos con problemas o la cantidad de los renos sea la requerida, se va a dormir. Santa se despierta hasta que los renos o los elfos lo despierten. 
- *Barreras* para los elfos y los renos. En mi implementación solo estoy permitiendo que un elfo o un reno estén despiertos y los posteriores los mando a dormir. La manera en despertarlos es si la longitud ya sea de los elfos o los renos (elfos con problemas == 3 o renos == 9)  aún NO es igual a la requerida. 

**Refinamientos**: el problema no sugiere refinamientos. 

---

**Comentarios adicionales**: es posible que a la hora de imprimir el estado actual de los hilos, se vean entre mezclados, sin embargo, Santa solo hará caso a la cantidad de elfos o renos actuales. Aunado a esto, hay una priorización de los eventos. Es decir, si la longitud de los renos es igual a 9 y la cantidad de los elfos es igual a 3, Santa atenderá primero a los renos pues así lo indica el problema. 