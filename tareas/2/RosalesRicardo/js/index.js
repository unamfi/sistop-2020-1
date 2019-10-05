var num = Math.floor((Math.random() * (11-5))+5);
var promedio;

//Funcion encargada de generar Procesos aleatorios guardarlos en un json 
function generarProcesos(){
    let procesos = [];
    let procesos2 = [];
    let nombres = ['A','B','C','D','E']
    let t_llegada = [];
    let t_requerido = [];
    //Creando numeros aleatorios 
    for(var n = 0; n < 5 ; n++){
        t_llegada.push(Math.floor((Math.random() * (12-1))+1));
        t_requerido.push(Math.floor((Math.random() * (6-2))+2));
    }
    //Declarando el primer tiempo de llegada en 0
    t_llegada.splice(0,1,0);
    //Ordenando los tiempo de llegada
    t_llegada.sort(function(a, b){return a-b});

    //Agregando los valores de tiempo de llegada y tiempo requerido a un objeto JSON 
    if(sinRepetidos(t_llegada)){
        for(var n = 0;  n < t_llegada.length ; n++){
            procesos.push({nombre : nombres[n] ,t_llegada : t_llegada[n] , t_requerido : t_requerido[n], nivel : 0})
            procesos2.push({nombre : nombres[n] ,t_llegada : t_llegada[n] , t_requerido : t_requerido[n], nivel : 0})
        }
        let suma = 0;
        procesos.forEach((e)=>{
            suma += e.t_requerido;
        });
        procesos2.forEach((e)=>{
            suma += e.t_requerido;
        });
        promedio = Math.floor(suma / t_requerido.length);
        generaTablaBase(procesos , promedio);
        FCFS(procesos);
        retroMulti(procesos, procesos2);
    }else{
        generarProcesos();
    }
    
}

//Nos asegura que los tiempos de llegada no se repitan
function sinRepetidos(array){
    for(var n = 0 ; n < array.length - 1 ; n++){
        if(array[n] == array[n+1]){
            return false;
        }
    }
    return true;
}

//Se realia el algoritmo de Primeras llegadas , Primeras salidas , regresa la tabla de resultados 

function FCFS(procesos){

    let fcfs = [];
    let inicio = 0;
    let fin = 0;

    for(var n = 0 ; n < procesos.length ; n ++ ){
        if(inicio < procesos[n].t_llegada){
            inicio = procesos[n].t_llegada;
            fin = procesos[n].t_llegada;
        }
        fin+=procesos[n].t_requerido; 

        fcfs.push({
            proceso : procesos[n].nombre 
            ,inicio : inicio
            ,fin : fin
            ,tiempo : fin-procesos[n].t_llegada 
            ,espera : (fin-procesos[n].t_llegada ) - procesos[n].t_requerido
            ,penalizacion : (fin-procesos[n].t_llegada) / procesos[n].t_requerido 
        });
            
        inicio = fin;
 
    }
    generaTabla(fcfs, "tabla_resultadosFCFS");

}

//Generando la tabla orignal que contiene únicamente , los tiempos de llegada y tiempo de realización

function generaTablaBase(procesos, promedio){

    var div_tabla = document.getElementById("tabla_base");
    var tabla = document.createElement("table");
    let celdas = [];
    let prom;
    let hileras = [];

    tabla.style.border= "1px solid #000";

    div_tabla.appendChild(tabla);
    div_tabla.appendChild(document.createElement("br"));
    div_tabla.appendChild(document.createElement("br"));
    div_tabla.appendChild(document.createElement("br"));

    var hilera = document.createElement("tr");
    
    for(var n = 0 ; n < 3 ; n++){
        celdas.push(document.createElement("td"));  
    }

    celdas[0].innerHTML = "Proceso";
    celdas[1].innerHTML = "Tiempo de llegada";
    celdas[2].innerHTML = "Tiempo requerido";

    celdas.forEach((e)=> {
        e.style.backgroundColor = "#D3D3D3";
        e.style.width = "25%";
        e.style.textAlign = "left";
        e.style.verticalAlign = "top";
        e.style.border = "1px solid #000";
        e.style.borderSpacing = "0";
    })

    celdas.forEach((e)=> {
        hilera.appendChild(e);
    })

    tabla.appendChild(hilera);


    for(var n = 0 ; n < procesos.length ; n ++){
        let contenido = []
        hileras.push(document.createElement("tr"));
        contenido.push(document.createElement("td"));
        contenido.push(document.createElement("td"));
        contenido.push(document.createElement("td"));
        contenido[0].innerHTML = procesos[n].nombre;
        contenido[1].innerHTML = procesos[n].t_llegada;
        contenido[2].innerHTML = procesos[n].t_requerido;

        contenido.forEach((e)=> {
            e.style.width = "25%";
            e.style.textAlign = "left";
            e.style.verticalAlign = "top";
            e.style.border = "1px solid #000";
            e.style.bordercollapse = "collapse";
            e.style.padding = "0.3em";
            e.style.captionSide = "bottom";
        });

        contenido.forEach((e) => {
            hileras[n].appendChild(e);
        });
    }  
    hileras.forEach((e)=>{
        tabla.appendChild(e);
    });

    prom = document.createElement("tr");
    celdas.push(document.createElement("td"));
    celdas.push(document.createElement("td"));
    celdas.push(document.createElement("td"));
    celdas[3].innerHTML = "Promedio";
    celdas[5].innerHTML = promedio;

    for(var n = 3 ; n  < 6 ; n++ ){
        prom.appendChild(celdas[n]);
    }

    tabla.appendChild(prom);
}


//Genera la tabla en HTML del algoritmo ya con , tiempos , Espera, etc.
function generaTabla(procesos, tabla){
    var div_tabla = document.getElementById(tabla);
    var tabla = document.createElement("table");
    let celdas = [];
    let prom;
   

    tabla.style.border= "1px solid #000";

    div_tabla.appendChild(tabla);
    div_tabla.appendChild(document.createElement("br"));
    div_tabla.appendChild(document.createElement("br"));
    div_tabla.appendChild(document.createElement("br"));
    div_tabla.appendChild(document.createElement("br"));

    var hilera = document.createElement("tr");
    
    for(var n = 0 ; n < 6 ; n++){
        celdas.push(document.createElement("td"));
        
    }

    celdas[0].innerHTML = "Proceso";
    celdas[1].innerHTML = "Inicio";
    celdas[2].innerHTML = "Fin";
    celdas[3].innerHTML = "T";
    celdas[4].innerHTML = "E";
    celdas[5].innerHTML = "P";

    celdas.forEach((e)=> {
        e.style.backgroundColor = "#D3D3D3";
        e.style.width = "25%";
        e.style.textAlign = "left";
        e.style.verticalAlign = "top";
        e.style.border = "1px solid #000";
        e.style.borderSpacing = "0";
    })

    celdas.forEach((e)=> {
        hilera.appendChild(e);
    })

    tabla.appendChild(hilera);

    let hileras = [];
    let prom_tiempo = 0;
    let prom_espera = 0;
    let prom_penalizacion = 0;

    for(var n = 0 ; n < procesos.length ; n ++){
        let contenido = []
        hileras.push(document.createElement("tr"));
        contenido.push(document.createElement("td"));
        contenido.push(document.createElement("td"));
        contenido.push(document.createElement("td"));
        contenido.push(document.createElement("td"));
        contenido.push(document.createElement("td"));
        contenido.push(document.createElement("td"));
        contenido[0].innerHTML = procesos[n].proceso;
        contenido[1].innerHTML = procesos[n].inicio;
        contenido[2].innerHTML = procesos[n].fin;
        contenido[3].innerHTML = procesos[n].tiempo;
        contenido[4].innerHTML = procesos[n].espera;
        contenido[5].innerHTML = Math.round((procesos[n].penalizacion) * 100) / 100; ;

        prom_tiempo += procesos[n].tiempo;
        prom_espera += procesos[n].espera;
        prom_penalizacion += procesos[n].penalizacion;

        contenido.forEach((e)=> {
            e.style.width = "25%";
            e.style.textAlign = "left";
            e.style.verticalAlign = "top";
            e.style.border = "1px solid #000";
            e.style.bordercollapse = "collapse";
            e.style.padding = "0.3em";
            e.style.captionSide = "bottom";
        });

        contenido.forEach((e) => {
            hileras[n].appendChild(e);
        });
    }  

    hileras.forEach((e)=>{
        tabla.appendChild(e);
    });


    prom = document.createElement("tr");
    celdas.push(document.createElement("td"));
    celdas.push(document.createElement("td"));
    celdas.push(document.createElement("td"));
    celdas.push(document.createElement("td"));
    celdas.push(document.createElement("td"));
    celdas.push(document.createElement("td"));
    celdas[6].innerHTML = "Promedio";
    celdas[9].innerHTML = Math.round((prom_tiempo / 5 ) * 100) / 100;
    celdas[10].innerHTML = Math.round((prom_espera / 5) * 100) / 100;
    celdas[11].innerHTML = Math.round((prom_penalizacion / 5) * 100) / 100;

    celdas.forEach((e)=> {
        e.style.backgroundColor = "#D3D3D3";
        e.style.width = "25%";
        e.style.textAlign = "left";
        e.style.verticalAlign = "top";
        e.style.border = "1px solid #000";
        e.style.borderSpacing = "0";
    })

    for(var n = 6 ; n  < 12 ; n++ ){
        prom.appendChild(celdas[n]);
    }

    tabla.appendChild(prom);
}

//Define como se van a ir ingresando los valores a un array el cual esta simuladno ser la cola de procesos
function retroMulti(procesos, procesos2){
    var auxProcesos = [];
    var retroMultiNiv = []
    var tiempo  = 0;
    let proceso ;

    procesos.forEach((elem)=>{
        auxProcesos.push(elem);
    });

    proceso = encuentraProceso(tiempo, auxProcesos);
    retroMultiNiv.push(proceso.nombre);
    
    while(proceso != false){
         tiempo += 1;
         proceso = encuentraProceso(tiempo , auxProcesos);
         retroMultiNiv.push(proceso.nombre);
    }

    defineTiempos(retroMultiNiv, procesos2);

}

//Para mandarlos a la tabla que los despliega en HTML tienen que cumplir con un estandar de objeto json que yo diseñe
function defineTiempos(retroM , procesos){
    let tiempoRetro  = [];
    let t_fin = [];

    retroM.pop();

    for(var n = 0; n < procesos.length ; n++){
        
        let  x = retroM.reverse().indexOf(procesos[n].nombre);
        retroM.reverse();
        t_fin.push(retroM.length - (x+1));

        tiempoRetro.push({'proceso': procesos[n].nombre,
            'inicio' : procesos[n].t_llegada ,
            'fin': retroM.length - (x+1) ,
            'tiempo' :(retroM.length - (x+1) + 1)- procesos[n].t_llegada ,
            'espera': ((retroM.length - (x+1)+1 )- procesos[n].t_llegada ) - procesos[n].t_requerido,
            'penalizacion': ((retroM.length - (x+1)+ 1)- procesos[n].t_llegada)/procesos[n].t_requerido
            });

    }

    generaTabla(tiempoRetro, 'tabla_resultadosRM');
}

//Busca cuales porceso cumplen con la condición de estarse ejecutando en un momento especifico
function encuentraProceso(tiempo, auxProcesos){
    let auxArr = [];

    depuraProcesos(auxProcesos);

    if(auxProcesos.length == 0 ){
        return false;
    }

    for(var n = 0 ; n < auxProcesos.length ; n++){
        if(auxProcesos[n].t_llegada <= tiempo && auxProcesos[n].t_requerido != 0){
            auxArr.push(auxProcesos[n]);
        }
    }

    if(auxArr.length == 0 ){
        return false;
    }else{
        return encuentraMenor(auxArr);
    }
   
}

//En caso de que el poryecto halla acabado se elimina del stack 
function depuraProcesos(array){
    for(var n = 0 ; n < array.length ; n++){
        if(array[n].t_requerido == 0 ){
            array.slice(n, 1);
        }
    }
}

//Busca el elemento que tenga menor nivel y además se encuentra en un timpo de incio menor
function encuentraMenor(array){

    let  menorElem = array[0];

    if(array.length == 1){
        menorElem.nivel += 1;
        menorElem.t_requerido -= 1;
        return menorElem;
    }
    for(var n = 1  ; n < array.length ; n++){
        if(menorElem.nivel > array[n].nivel ){
            menorElem = array[n];
        }
        if(menorElem.nivel == array[n].nivel){
            if(menorElem.t_llegada > array[n].t_llegada){
                menorElem = array[n];
            }else{
                
            }
        }
    }
    menorElem.nivel += 1;
    menorElem.t_requerido -= 1;
    return menorElem;
}


//Se va a llamar tres veces a la función para que visualicen como funciona
generarProcesos();
generarProcesos();
generarProcesos();