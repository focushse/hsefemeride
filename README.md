# Archivo HSE

Proyecto web estatico de una sola pagina para publicar efemerides HSE en GitHub Pages.

## Publicacion diaria

`index.html` muestra automaticamente la efemeride correspondiente al dia actual usando el horario de Bogota/Quito/Lima (`America/Bogota`).

- El 26 de junio muestra solo la efemeride del 26 de junio.
- El 27 de junio muestra la del 27 y permite volver a la del 26.
- Las efemerides futuras quedan bloqueadas hasta su fecha.
- Se puede revisar una historia pasada usando `?id=003`, por ejemplo.
- La lista maestra se abre con:

```text
index.html?lista=1
```

## Como guardar imagen y audio por efemeride

Usa una carpeta por historia dentro de:

```text
assets/efemerides/
```

Formato recomendado para cada carpeta:

```text
assets/efemerides/AAAA-MM-DD-nombre-corto/
  portada.png
  historia.m4a
  contenido-completo.md
```

Ejemplo para la historia del 26 de junio de 1964:

```text
assets/efemerides/1964-06-26-marshalls-creek/
  portada.png
  historia.m4a
  contenido-completo.md
```

Luego en `index.html`, dentro de `historiaDelDia`, usa esta forma:

```js
carpetaAssets: "assets/efemerides/1964-06-26-marshalls-creek/",
imagen: "portada.png",
audio: "historia.m4a",
```

## Recomendaciones

- Imagen: usa `.png` si ChatGPT te las entrega asi. Idealmente comprimelas si pesan mucho para que carguen rapido en celular.
- Audio: usa `.m4a` si ese es el formato que estas generando. Idealmente comprimelo si pesa mucho para compartir y abrir rapido.
- Texto completo: guarda la informacion original en `contenido-completo.md` para no perder la version larga aunque la pagina use una capsula resumida.
- Nombres: evita espacios, acentos y mayusculas en archivos y carpetas.
- GitHub Pages distingue mayusculas y minusculas: `Portada.png` no es igual que `portada.png`.
