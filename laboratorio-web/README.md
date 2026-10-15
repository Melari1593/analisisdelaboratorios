# Clara · Lectura de laboratorios y ecografías

Aplicación web en español para subir informes (PDF, JPG, PNG, WEBP, TXT, CSV) y recibir una lectura orientativa. Requiere Node.js 20 o superior, una clave de OpenAI API y una clave de acceso propia. No ofrece diagnósticos definitivos.

## Inicio

```bash
cd laboratorio-web
export OPENAI_API_KEY="su-clave-de-api"
export ACCESS_TOKEN="una-clave-larga-y-privada"
npm start
```

Abra `http://localhost:3000` e introduzca `ACCESS_TOKEN` en el campo de acceso. Configure `PORT` y `OPENAI_MODEL` si lo necesita (predeterminado: `3000` y `gpt-5.5`). Ejecute `npm test` para las comprobaciones del servidor. El repositorio de GitHub solo contiene el código: para abrir la web a otras personas se necesita alojar este servidor Node con HTTPS y configurar las variables de entorno en el proveedor de hosting. No publique las claves en GitHub ni en el navegador.

## Alcance y datos

- Hasta tres archivos, 8 MB cada uno; máximo de 18 MB por solicitud. Los archivos se procesan en memoria, se envían a OpenAI para el análisis y no se guardan en disco ni en una base de datos de esta aplicación. La solicitud a OpenAI utiliza `store: false`. Revise los términos, la privacidad y los controles de datos del proveedor antes de usar datos de pacientes.
- La clave de acceso se conserva únicamente en la pestaña, sin almacenamiento local. Use una clave distinta de la API. Para uso público o con múltiples usuarios, sustituya este control compartido por autenticación individual, límites de uso, protección frente a abuso y revisión legal de protección de datos.
- Compare valores solo con el intervalo impreso en el informe. Una imagen de ecografía sin informe firmado puede ser insuficiente; la aplicación lo debe indicar. Revise los valores extraídos contra el documento original, pues los modelos pueden equivocarse al leer tablas o imágenes.
- No se ha validado clínicamente. Un profesional debe revisar la salida antes de usarla para decisiones de atención. Si aparecen síntomas graves, busque atención médica inmediata.

Fuentes de diseño clínico: [MedlinePlus: lectura de resultados](https://medlineplus.gov/lab-tests/how-to-understand-your-lab-results/) y [ACR: informe oficial ecográfico](https://gravitas.acr.org/PPTS/GetDocumentView?docId=24). Documentación técnica: [archivos en Responses](https://developers.openai.com/api/docs/guides/file-inputs), [imágenes](https://developers.openai.com/api/docs/guides/images-vision) y [salidas estructuradas](https://developers.openai.com/api/docs/guides/structured-outputs).
