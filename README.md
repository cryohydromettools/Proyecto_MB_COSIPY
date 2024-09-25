# Proyecto: Uso de un modelo físico para modelar el balance de masa

**Autores:** <br />
Christian Torres <br />
Claudio Bravo

## Descripción del proyecto

El proyecto está compuesto por cuatro cuadernos Jupyter en Python, en los que se detalla la aplicación del modelo glaciológico [COSIPY](https://cryo-tools.org/tools/cosipy/) para simular el balance de masa superficial de los glaciares. Para la ejecución del modelo, se emplearán datos topográficos extraídos de inventarios nacionales de glaciares, y datos meteorológicos obtenidos del conjunto de  reanálisis [ERA5](https://cds-beta.climate.copernicus.eu/). El proyecto se enfoca en cuatro glaciares ubicados en los Andes peruanos, la Patagonia chilena y el norte de la Península Antártica. Puedes observar la ubicación y algunas características de estos glaciares en la siguiente figura.

<img src="img/mapa_taller.png" width="650"> <br>

En este proyecto se tratan los siguientes temas:

1. [Preprocesamiento de datos](https://github.com/cryohydromettools/Proyecto_MB_COSIPY/blob/main/1_Preprocesamiento.ipynb) :earth_africa:: Aquí aprenderemos a preparar los datos estáticos (topografía, pendiente, aspecto, macará) y meteorológicos (temperatura, precipitación, radiación solar, etc).

2. [Exploración de datos](https://github.com/cryohydromettools/Proyecto_MB_COSIPY/blob/main/2_Exploracion_datos.ipynb) :mag:: Aquí aprenderemos a ver los datos de entrada a través de figuras espaciales y temporales. En caso de disponer de datos meteorológicos registrados por una estación cercana al glaciar, estos pueden emplearse para verificar la precisión de los datos de ERA5 e incluso ajustarlos si es necesario.

3. [Ejecución del modelo ](https://github.com/cryohydromettools/Proyecto_MB_COSIPY/blob/main/3_Ejecutar_COSIPY.ipynb) :rocket:: Aquí aprenderemos a ejecutar el modelo COSIPY. Además, exploraremos los diferentes parámetros libres que tiene el modelo.

4. [Análisis de resultados](https://github.com/cryohydromettools/Proyecto_MB_COSIPY/blob/main/4_Analizar_salida.ipynb) :dart:: Una vez que hayamos generado resultados con el modelo COSIPY, aquí aprenderemos a analizar estas salidas mediante figuras espaciales y temporales.



