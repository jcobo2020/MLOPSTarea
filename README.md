# MLOPSTarea
Proyecto para implementar un CICD de unas tareas en python.

## Explicación de la estructura del proyecto
**Labs:** Estan los cuadernos Jupyter que traen la logica inicial de la preparación de los datos y el entrenamiento del modelo.<br>
**src:** Se encarga del ambiente para ejecutar  feafure_engineering.py, training_model.py , asi como la clase storage, esta con su Dockerfile.<br>
**Api:** Se encarga del ambiente para los api (Flask ) de caracteristicas y el de predicción. Maneja una clase singleton(singleton.py) para tener la instancia de los datos en memoria. Tiene carga_datos.py que se encarga de bajar los datos del blob storage, Dockerfile y start.sh para la ejecuciom inical de carga y levantar el api de Flask.<br>
**cicd:** Plantilla azure-pipelines.yml usado en el proceso de CICD desde el proveedor Azure .<br>
**data:** Archivos CSV utilizados en el proyecto.<br>


## Canalización usada para el proyecto
<img width="760" alt="image" src="https://user-images.githubusercontent.com/63362120/157254638-57bdde1c-ab74-4426-a10c-6c8a853a9a89.png">


## Estructura del manejo de la data en el storage
<img width="901" alt="image" src="https://user-images.githubusercontent.com/63362120/157252832-3fe681be-02dd-4c29-ab46-a486395f05c7.png">

## Api habilitadas para caracteristica y prediccion

https://sa-prediccion-riesgo-lab.azurewebsites.net/api/user/5008806/caracteristicasriesgo

{
   "nb_previous_loans":29.0,
   "avg_amount_loans_previous":136.4468640135,
   "age":59.0,
   "years_on_the_job":3.0,
   "flag_own_car":1.0
}

https://sa-prediccion-riesgo-lab.azurewebsites.net/api/user/5008806/prediccion

{"resultado": [0]}

## Componentes en Azure
**Azure DevOps:** Servicio para administrar el ciclo de vida del desarrollo de un extremo a otro.
**Blob Storage :** Almacenar la información de los csv y el modelo entrenado.
**Registro de contenedor:** Almacenar las imagenes de los contenedores.
**App Service (Web App for Containers):** Es un servicio PaaS para hospedar aplicaciones web, API REST basado en un contenedor.


## Mejoras 
- La información que se genera del train_model.csv se pudo almacenar en una base NOSQL.
- Usar una base como auditoria para almacenar la información de las ejecuciones.
- Aplicar mas validaciones en caso de que el User Id no exista.
