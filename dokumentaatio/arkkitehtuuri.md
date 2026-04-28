## Rakenne

Sovelluksen rakenne on kolmikerroksinen. ui-kansion sisältö vastaa sovelluksen käyttöliittymästä, Services sovelluslogiikasta, ja Repositories toimintojen tallentamisesta tietokantaan. Repositories- ja Services-kansioiden sisältö hyödyntää Entities-kansion sisältöä.

## Käyttöliittymä

Käyttöliittymä sisältää neljä erilaista näkymää:
- Kirjautuminen
- Uuden käyttäjän luominen
- Luodut päivät
- Valitun päivän sisältämät harjoitteet

Jokaisella näkymällä on oma luokka, joka vastaa sen esillepanosta. Kirjautumisen jälkeen avautuva päivänäkymä näyttää käyttäjän luomat päivät. Haluttua päivää klikkaamalla avautuu näkymä, joka näytää päivän sisältämät harjoitteet. Tämä näkymä hyödyntää ExerciseElement-luokkaa, joka vastaa luodun harjoitteen esittämisestä mielekäällä tavalla, ja joka sisältää tiedot harjoitteen nimestä, sarjoista, toistoista ja käytettävästä painosta.

Käyttäjä voi luoda uusia päiviä päivänäkymässä. Valitun päivän näkymässä, joka näyttää päivän sisältämät harjoitteet, käyttäjä voi luoda uusia harjoitteita, poistaa ja päivittää niiden arvoja.

Käyttöliittymä on eriytetty sovelluslogiikasta ja toteuttaa toiminnallisuuksia kutsumalla eri Services-kansion sisältämiä metodeja.

## Sovelluslogiikka
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

Sovelluksen tietokantarakenne on kolmikerroksinen. users-taulu sisältää tiedot käyttäjän nimimerkistä ja salasanasta. Kun uusi päivä luodaan, days-tauluun tallennetaan tieto siitä, mille käyttäjätunnukselle päivä kuuluu (username). Uusia harjoitteita luodessa tallennetaan tieto siitä, mille päivälle harjoite kuuluu (day_id). Jos käyttäjä poistaa tietyn päivän, päivän lisäksi myös sen sisältämät harjoitteet poistetaan automaattisesti tietokannasta.

## Pakkauskaavio
```mermaid
classDiagram
    namespace Services {
        class DayService
        class UserService
        class ExerciseService
    }
    namespace Repositories {
        class DayRepository
        class UserRepository
        class ExerciseRepository
    }
    namespace Entities {
        class Day
        class User
        class Exercise
    }

    class UI
    UI "1" -- "0..1" User
UI ..> DayService
UI ..> UserService
UI ..> ExerciseService
DayRepository "1" --> "1" DayService
UserRepository "1" --> "1" UserService
ExerciseRepository "1" --> "1" ExerciseService
DayService ..> Day
UserService ..> User
ExerciseService ..> Exercise
DayRepository ..> Day
UserRepository ..> User
ExerciseRepository ..> Exercise

```

## Käyttäjän sisäänkirjautuminen
```mermaid
sequenceDiagram
    actor User
    participant LoginView
    participant UI
    participant UserService
    participant UserRepository
    participant Database
    participant DayView

    User->>LoginView: Insert username + password
    User->>LoginView: Click "Login"
    LoginView->>UI: _handle_login(username, password)
    UI->>UserService: login(username, password)
    UserService->>UserRepository: find_by_username(username)
    UserRepository->>Database: SELECT * FROM users WHERE username = ?
    Database-->>UserRepository: user row
    UserRepository-->>UserService: User
    UserService-->>UI: user
    UI->>DayView: _show_day_view()
```
