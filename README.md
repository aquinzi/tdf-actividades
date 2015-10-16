# test-jekyll

Repositorio para probar jekyll y la creación del theme correspondiente, para no instalar :gem: ruby :grin:

Sitio de prueba: http://eikiu.github.io/test-jekyll/


Porque siempre me olvido, links al liquid syntax:

- [a github/oficial](https://github.com/Shopify/liquid/wiki/Liquid-for-Designers)
- [de shopify](https://docs.shopify.com/themes/liquid-documentation/)


Notas miscelaneas:

 - dotfiles are excluded by default
 - excluir carpetas con guion bajo. Ej. _esconder-carpeta
 - ``JEKYLL_ENV=production`` para ponerlos en los templates si se necesita cambiar el enviroment.
 - para el "edit on github":
     - Páginas: ``{{site.github.repository_url}}/blob/gh-pages/{{page.path}}``
     - collections/posts: ``{{ site.github.repository_url }}/tree/{{site.github.branch}}/{{ service.relative_path }}``
