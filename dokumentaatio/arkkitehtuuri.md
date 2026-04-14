```mermaid
 classDiagram
      exercises "*" --> "1" days
      days "*" --> "1" users
      class users{
          username
          password
      }
      class days{
          id
          username
          day_name
      }
      class exercises{
          id
          day_id
          name
          sets
          reps
          weight
      }
```
