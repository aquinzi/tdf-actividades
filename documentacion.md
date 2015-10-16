Documentación
=================

 - FEED: hay feeds por ciudad
 - BREADCRUMBS: Los breadcrumbs se crean automáticamente por la url, hay una opción en config (``breadcrumb_limit``) para limitar la cantidad a poner (limita la profundidad)
 - TOC: jekyll usa kramdown por default, que genera TOC automaticamente. A su vez, jekyll tiene por defecto la opcion auto_ids para generar automaticamente los ID de los headers. Para usar el TOC: en la pagina.md poner ``* TOC(linebreak){:toc}`` [tip](http://www.seanbuscay.com/blog/jekyll-toc-markdown/)
 - "wiki links" (basicamente para facil linkeo de entidades, el resto es estatico simple). Se usa un wiki.yml que contiene los links; manualmente se tiene que poner el site.baseurl en el archivo yml. Para linkear: ``[titulo](site.data.wiki.[key])``. Se pueden usar los [repeated nodes](https://en.wikipedia.org/wiki/YAML#Repeated_nodes). (Ideas: [Jekyll Talk: Better way to manage links to articles](https://talk.jekyllrb.com/t/better-way-to-manage-links-to-articles/1199/6) y [Jekyll Issues: Add a tag to link to a post/page with it's title shown](https://github.com/jekyll/jekyll/issues/3182#issuecomment-70561683))
 - Se creó el ``slugify-word.html`` por que el filtro "raw" de liquid no funciona en gh-pages (y supongo que hace lio con los acentos)
 - Código del sitemap de: [davidensinger](http://davidensinger.com/2013/11/building-a-better-sitemap-xml-with-jekyll/)


Traducción de Jekyll
------------------------

Se usan algunos archivos yaml en ``_data`` para traducir meses y días.



Changelog
--------------

Se puede usar tranquilamente un html pero necesitamos (al 20/09/2015) una forma de traer los ultimos cambios y yaml nos ayuda para hacer esto.

Se elige yaml a json (que seria mejor para python, ya que lo trae incluido) por ser de facil lectura, y sin tantos simbolos "raros". Ademas, al ser sintaxis simple, podemos hacer algo sucio: leer/escribir en python como texto plano.

Acordarse de NO usar espacios despues de las keys, sino se parsean como hashed ("diccionario"). Si no tiene key = solo info normal.



Listado de actividades
-----------------------------------------

Están en yaml, asi se puede agrupar mas facilmente y no tener que andar haciendo varios loops para conseguir los tipos (deporte, arte...).


Antes se usaba CSV. La explicación: 

Las actividades por ciudad están en ``_data/[ciudad]/actividades.csv``. Esto es porque requieren un par de datos extra, además de que se puede listar sin tener entidades.

Se podrian haber hecho tambien en json/yaml, con la particularidad que ya estan agrupados. Se eligió csv porque:

- es mas legible asi (una linea-un dato; sin tantas keys, con especificarlo arriba ya alcanza).
- se puede editar facilmente: ya sea en un txt editor, editor simple de csv o un programa de hojas de calculos, porque son pocos datos.
- no pude hacer un sorting de las keys (grupos) en json (jekyll).

Por si se cambia de parecer, el json que se estaba usando era:

```json
{
  "arte": [{ "nombre": "", "nombre_alt": "" }], 
  "deporte": [{ "nombre": "", "nombre_alt": "" }], 
  "afición": [{ "nombre": "", "nombre_alt": "" }]
}
```
	
y se traian los datos con:

```liquid
{% for group in site.data.riogrande.actividades | sort:"group[0]" %}
    <p><strong>{{group[0]}}</strong><br>
    {% for item in group[1] | sort:"nombre" %}
        {{item.nombre}}<br>
    {% endfor %}
    </p>
{% endfor %}
```



Listado de lugares
---------------------

Los lugares estan en un yaml en ``_data/[ciudad]/lugares.yml``. Jekyll no lee geojson.

Para linkear los lugares en los posts y entidades, poner en ``location`` el ID_lugar.


Entidades
----------------

Las entidades estan en ``_entidades-[ciudad]``. Se usan subcarpetas para hacer cierta separacion; como Jekyll lo toma como parte del path, hay que poner permalink por archivo. Usar script.

Se listan los posts de entidades cuando éstos se linkean en el metadata de ``people`` usando la ID (nombre de archivo)



Tags 
-----------

Los índices de los tags se crean manualmente. Usar script.

Como a veces hay delay entre posts y creación manual de tags (ej: actualizado por web), al mostrar  los tags en eventos, se busca su existencia y se linkea, sino solo muestra nombre.


URLs
------------

Los eventos/posts estan ``/[ciudad]/agenda/[año]/[mes]/[evento-slug]/index.html``.

Los slug de posts es el texto despues de la fecha en el archivo. Se podria usar la propiedad "slug" pero parece que es un bug en jekyll (ver: [Jekyll Talk: Clarification on slug in YAML](https://talk.jekyllrb.com/t/clarification-on-slug-in-yaml-front-matter-doesnt-seem-to-affect-my-permalinks/1103))


Posts y páginas
---------------------

Los posts se encuentran en ``[ciudad]/_posts/[año]/[mes?]`` esto es para tener cierto orden, ademas de que nos olvidamos de tener que poner una categoria (ya sea en el archivo o por _config). [Fuente del dato](https://github.com/jekyll/jekyll/pull/2633#issuecomment-98330970).

Varias paginas se encuentran en ``_pages``, donde en cada una se settea el permalink correspondiente. Esto es para tener un orden y no queden en el root ([idea](http://pixelcog.com/blog/2013/jekyll-from-scratch-core-architecture/#adding-pages))


Backend
-------------

Se tiene GUI para añadir eventos (hecho en python y wxwidgets) y en html-js (para cosas rapidas, no muy actualizado ni bien implementado).

el form de entrada de datos en html/js fue tomado de [vrypan.net](http://blog.vrypan.net/2015/05/29/post-to-github-jekyll-using-a-bookmarklet/) ([github: jekyll-post-via-web](https://github.com/vrypan/jekyll-post-via-web)) 

Hay scripts para automatizar ciertas cosas, hasta que se cree un CMS para el proyecto.


Imágenes de cover para redes sociales
---------------------------------------

- ACTUAL: tdf satelital dada vuelta y de costado, sin nubes (2014) [NASA](http://visibleearth.nasa.gov/view.php?id=83713)
- tdf satelital: (2001) [NASA](http://visibleearth.nasa.gov/view.php?id=56170) popular porque esta en [wikimedia](https://commons.wikimedia.org/wiki/File:TierraDelFuego_Satellite1.jpg)
- tdf satelital (todo el cono sur de arg-chile) (2003) [NASA][http://visibleearth.nasa.gov/view.php?id=65873]
- tdf satelital (sin muchas nubes y poca nieve) (2006) [spacearchive](http://www.spacearchive.info/2006-11-22-tierra-del-fuego-large.jpg)