# Amazon Reviews Data Pipeline, Analytics and Machine Learning 

## Acerca del proyecto

La compañía de comercio electrónico Amazon, contrató a la empresa de Ciencia de Datos Skaivu Insights, para contar con sus servicios de procesamiento y análisis de datos con el fin de encontrar nuevas perspectivas para mejorar sus ventas. La empresa se encargará de almacenar, transformar, estructurar, analizar y modelar la información proporcionada para crear un sistema automático de recomendación de productos relevantes, basado en la información de opiniones provenientes de otros usuarios.

## Objetivo General

Realizar un análisis de reseñas y ventas de productos a partir de la información proporcionada por el cliente Amazon, así, extraer información objetiva y concisa de indicadores claves de desempeño e idear un sistema de recomendaciones de productos. 

## Acerca de los datos

Se cuenta con 24 tablas (una por cada categoría de producto) con información de artículos comprados en Amazon. El rango de fecha data desde 1996 hasta 2014. Se poseen alrededor de 20gb con un total de 142.8 millones de reviews y 3.1gb de metadata.

**Nombre de las categorías**: Books, Electronics, Movies and TV, CD and Vinyl, Clothing, shoes and Jewelry, Home and Kitchen, Kindle Store, Sports and Outdoors, Cell Phones and Accessories, Health and Personal Care, Toys and Games, Video Games, Tools and Home Improvment, Beauty, Apps for Android, Office Products, Office Products, Pet Supplies, Automotive, Grocery and Gourmet Food, Patio, Lawn and Garden, Baby, Digital Music, Musical Instruments, Amazon Instant Video.

## **Diccionario de datos:**

### **Reseñas**
reviewerID - ID del usuario, ejemplo: A2SUAM1J3GNN3B.

asin - ID del producto, ejemplo: 0000013714.

reviewerName - nombre del usuario.

helpful - Puntaje de utilidad de la reseña (votos externos), e.g. 2/3.

reviewText - Texto de la reseña.

overall - Puntaje dado al producto.

summary - Resumen de la reseña.

unixReviewTime - Fecha de la reseña (unix time).

reviewTime - Fecha de la reseña .


### **Metadata de productos**

**asin** - ID del producto, ejemplo: 0000031852.

**title** - Nombre del producto.

**price** - Precio en dólares.

**imUrl** - URL de la imagen del producto.

**related** - Productos relacionados (comprados juntos, también revisados, comprados por el mismo usuario, comprados luego de verlos).

**salesRank** - Información sobre cómo rankea en ventas.

**brand** - Nombre de la marca del producto.

**categories** - Lista de la categoría a la que pertenece el producto.

La gran cantidad de volumen y variedad de dato son indicativos para emplear herramientas de Big Data. 

Afortunadamente, las columnas de cada tabla presentan la misma información, la tabla de reviews hace referencia a: Quién la realizó, qué producto está calificando, cuán útil es la reseña, texto de la reseña, puntaje del producto y cuándo se hizo la reseña. 

Las tablas de metadata representan el nombre del producto, precio, URL de la imagen, productos relacionados, rank en ventas, nombre de la marca y a qué categoría pertenece. 

## Equipo de Trabajo

Skaivu Insights consta de profesionales en diferentes áreas que estarán encargados de realizar en conjunto las tareas designadas durante el proyecto. El equipo de trabajo estará conformado por: 

* [Tomás Astrada](https://www.linkedin.com/in/tom%C3%A1s-astrada-370b73171/) - Data Engineer
* [Jean Fabra](https://www.linkedin.com/in/jeanfabra/) - Data Engineer 
* [Jorge Fonseca](https://www.linkedin.com/in/jorge-fonseca-alba-83433b117/) - Data Scientist 
* [Daniela Hugueth](https://www.linkedin.com/in/dhugueth/) - Data Analytic
* [Ingmar Orta](https://www.linkedin.com/in/ingmarorta/) - Data Scientist