# Sistems de archivos Extended (ext, ext2, ext3, ext4)

## Extended File System (ext)
El Sistema de Archivos Extendido (Extended File System) fue implementado en abril de 1992. Fue el primero de una serie de sistemas de archivos creados exclusivamente para Linux. Fue diseñado por Rémy Card para superar ciertas limitaciones del sistema de archivos de MINIX (el primer sistema de archivos de Linux). Dos de ellas fueron el tamaño máximo de partición y de nombre de archivos. Este sistema permitía 2GB de datos y nombres de archivos de 255 caracteres.

Este sistema fue el primero en utilizar el API del Sistema Virtual de Archivos (VFS).


<figure>
  <img src="./img/MINIX.jpg" alt="Estructura del sistema de archivos MiniX">
  <figcaption>Fig.1 - Estructura del sistema de archivos MiniX.</figcaption>
</figure>

## Second Extended File System (ext2)

Este sistema fue desarrolló en enero de 1993 para el Kernel de Linux 0.99. Surgió como una solución a tres problemas que tenía ext, modificación de inodo, modificación de datos y no soportaba marcas de tiempo (timestamps) para acceso de archivo.

## Referencias

[1] RUSLING, D. A. (S.F.). THE SECOND EXTENDED FILE SYSTEM (EXT2). RECUPERADO 11 OCTUBRE, 2019, DE HTTP://WWW.SCIENCE.UNITN.IT/%7EFIORELLA/GUIDELINUX/TLK/NODE95.HTML

[2] POIRIER, D. (2002). SECOND EXTENDED FILE SYSTEM.

[3] WIKIPEDIA CONTRIBUTORS. (2019B, 20 SEPTIEMBRE). FILE SYSTEM FOR THE LINUX KERNEL. RECUPERADO 11 OCTUBRE, 2019, DE HTTPS://EN.WIKIPEDIA.ORG/WIKI/EXT2