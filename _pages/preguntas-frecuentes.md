---
title: Preguntas frecuentes
permalink: /preguntas-frecuentes/
date: 2015-07-24
---


{% comment %}use markdown=1 to parse markdown syntax inside html block {% endcomment %}

<div id="tabla-contenido" markdown="1">

Contenido en esta página:

1. TOC (to make it use ordered list)
{:toc}

</div>



¿Por qué?  {#por-que}
-----------------------

Me decidí a hacer este proyecto de "directorio" por la falta de algún sitio web que lo haga, asi como también el déficit de personas que hagan un perfil en una red social (u algún otro sitio gratuito) para promover lo que hacen (vamos, ¡estamos en 2015!).



¿Vas a expandir esto al resto de la provincia?  {#resto-provincia}
------------------------------------------------

Si me ayudas con tu [colaboración]({{ site.data.wiki.colaboracion }}), si. Esa es la idea.



¿Qué tipo de actividades se pueden incluir?  {#tipo-actividades}
------------------------------------------------

Cualquier actividad (artística, deportiva, turistica), pago o gratuita, que cumpla con los siguientes "requisitos":

1. Que se realicen todos los años (nada de "clínicas"/"talleres" de un día para el otro)
2. Que se realicen por lo menos 6 meses (por poner un número) de los 12 meses del año, con la excepción de las actividades invernales.
3. Abierto a quién quiera. Nada de "tenés que hablar con el rey de turno para que te haga una evaluación y, en base a eso, ver si podes entrar o no" (exagerado el ejemplo, pero se entiende la idea)



¿Qué es eso de "última actualización"?  {#que-es-ultima-actualizacion}
------------------------------------------------

Eso. La última vez que cambié datos (importantes) en el item/actividad/lugar.
	
Es para tener una referencia sobre los datos y que, si "es muy viejo", que los uses bajo tu "propio riesgo". Esto es mas que nada para los datos de email (que pueden llegar a rebotar por caída de dominio o cierre de cuenta; o a no ser leídos), teléfonos (especialmente celulares) y sitios web (caída de dominio, falta de actualización, etc); y, en menor medida, horarios y dirección/lugar donde se realiza.



Ingresé y/o edité datos de actividades pero no se actualizaron. ¿Cuándo se van a ver en el sitio?  {#actualizaciones-en-el-sitio}
-------------------------------------------------------------------------------------------------

En cuanto pueda. Básicamete el traspaso de datos es manual. El orden de más laborioso a menos es:

1. Issue en GitHub
2. Mediante el formulario
3. Fork y pull request del repositorio



Quiero darte ideas o tengo mas dudas, ¿dónde puedo contactarte?  {#como-contactarme}
-----------------------------------------------------------------

Abrí un [issue]({{ site.github.issues_url }}){:rel="external"}.

Si no tenes cuenta en GitHub podes buscarle la vuelta al [formulario de entrada de actividades]({{ site.social.form_colaboracion }}){:rel="external"}.


¿Por qué le pones un ^ (acento circunflejo) a ciertas letras?  {#por-que-acento-circunflejo}
------------------------------------------------------------------

Para marcar las vocales largas en las palabras japonesas.

No le puedo poner macrón (rayita sobre caracter), y lo aceptable sería poner el acento circunflejo (según "La Gran Fuente de Información" (Wikipedia))



¿Por qué el abuso a los `dl`?  {#por-que-dl}
------------------------------------------

Para aumentar el ranking de uso de los pobres.

Se me hacía la etiqueta mas "semántica" para lo que quería hacer.



¿Por qué archivos varios y no una base de datos?  {#por-que-no-base-de-datos}
-----------------------------------------------

No quería tomarme el tiempo de usar una base de datos, diseñarla, escribir los <i lang="en">update, edit, add</i>, etc. Sería lo mas apropiado para este caso, pero quería algo rápido y elegí texto plano. <i lang="en"><abbr title="comma-separated values">CSV</abbr></i> (archivo separado por comas) lo dejé porque no sabía qué sintaxis usar para listados, además de que es ilegible en un editor de texto plano.

Además, el programa que uso para generar el sitio lee este tipo de formato (<i lang="en">YAML</i>). Algún día lo haré como se debe, con una linda base de datos.

