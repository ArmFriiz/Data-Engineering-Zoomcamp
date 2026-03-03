### **Muhammad Faris Akbar**

---

#### Question 1. What is the start date and end date of the dataset? (1 point)

- Answer : 2009-06-01 to 2009-07-01
- Solution :
  <img width="428" height="233" alt="image" src="https://github.com/user-attachments/assets/323adde2-840a-4d97-ba1a-818201ff640a" />

<br></br>

#### Question 2. Materialization Strategies You're building a pipeline that processes NYC taxi data organized by month based on pickup_datetime. Which incremental strategy is best for processing a specific interval period by deleting and inserting data for that time period? (1 point)

- Answer : time_interval - incremental based on a time column
- Solution :
  <img width="986" height="628" alt="image" src="https://github.com/user-attachments/assets/3488e868-711e-4a4c-a60a-dc7d6d22f360" />

- References : https://getbruin.com/docs/bruin/assets/materialization.html#time-interval

<br>

Question 3. Pipeline VariablesYou have a variable defined in pipeline.yml:variables: taxi_types: type: array items: type: string default: ["yellow", "green"]How do you override this when running the pipeline to only process yellow taxis? (1 point)

- Answer : bruin run --var 'taxi_types=["yellow"]'
- Solution :
  <img width="947" height="379" alt="image" src="https://github.com/user-attachments/assets/6fc912e9-6e67-4a0f-b49c-9e5a532c0af4" />

- References : https://getbruin.com/docs/bruin/getting-started/pipeline-variables.html#overriding-variables
  <br></br>

#### Question 4. Running with DependenciesYou've modified the ingestion/trips.py asset and want to run it plus all downstream assets. Which command should you use? (1 point)

- Answer : bruin run ingestion/trips.py --downstream
- Solution :
  <img width="1133" height="484" alt="image" src="https://github.com/user-attachments/assets/c75a436f-9eaa-40ff-a2ac-9dfeb5a9bcfb" />

<br></br>

#### Question 5. Quality Checks. You want to ensure the pickup_datetime column in your trips table never has NULL values. Which quality check should you add to your asset definition? (1 point)

- Answer : name: not_null
- References : https://getbruin.com/product/quality/
  <br></br>

#### Question 6. Lineage and DependenciesAfter building your pipeline, you want to visualize the dependency graph between assets. Which Bruin command should you use? (1 point)

- Answer : bruin lineage
- Solution :
  <img width="1380" height="301" alt="image" src="https://github.com/user-attachments/assets/1f0478ab-cd7c-468d-9a85-7f58c1906593" />

<br></br>

#### Question 7. First-Time RunYou're running a Bruin pipeline for the first time on a new DuckDB database. What flag should you use to ensure tables are created from scratch? (1 point)

- Answer : --full-refresh
- Solution :
  <img width="1133" height="484" alt="image" src="https://github.com/user-attachments/assets/c75a436f-9eaa-40ff-a2ac-9dfeb5a9bcfb" />

#### Learning in Public

- https://www.linkedin.com/posts/m-faris-akbar-_modul-5-data-platforms-menggunakan-bruin-share-7433661704724713473-_5R5?utm_source=share&utm_medium=member_desktop&rcm=ACoAAC2WdgQBFNQvyaHEVM4pwzRNofINDz0G8dY
