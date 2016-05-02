---
layout: default
title: Personas de Tierra del Fuego
permalink: /personas/
date: 2016-05-01
show_source: false
show_history: false
---

<h1>Personas de Tierra del Fuego</h1>

Noble listado. Pronto se expandirá y se podrá buscar o filtrar.

<ul class="listado-entidades listado-personas">
{% for person in site.personas %}
	<li class="card-entidad">
		<div class="logo">
		
			{% if person.imagen %}
				{% assign tmp = person.imagen | downcase %}
				{% if tmp == "si" %}
					{% assign page_filename = person.path | split:"/" | last | split: "." | first %}
				<img src="{{ site.baseurl }}/assets/personas/{{ page_filename }}.jpg" alt="logo" class="u-logo u-photo" width="300" itemprop="image">
				{% else %}
				<img src="{{ person.imagen }}" alt="logo" class="u-logo u-photo" width="140" itemprop="image">
				{% endif %}
			{% endif %}
		</div>

		<div class="info">
			<p class="p-name"><a href="{{ person.url }}">{{ person.nombre }}</a></p>
			<dl>
				<dt class="precio visuallyhidden">Ocupación</dt>
					<dd>{{ person.ocupacion }}</dd>
			{% if person.residencia %}
				<dt class="visuallyhidden">Origen</dt>
					<dd class="p-street-address">
					{% assign tmp = site.data.prettify[person.residencia] %}
						{% if tmp != ""%}{{ tmp }}{% else %}{{ person.residencia }}{% endif %}
					</dd>
			{% endif %}
			</dl>
		</div>
	</li>
{% else %}<li>No se ingresaron personas ni bandas. Si querés agregarte o agregar a otro, no dudes en <a href="{{ site.data.wiki.colaboracion }}" rel="external">colaborar</a>.</li>
{% endfor %}
</ul>