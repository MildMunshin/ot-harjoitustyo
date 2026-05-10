# Käyttöohje

Lataa projektin viimeisin release tästä(linkki)

## Ohjelman käynnistäminen

- Asenna riippuvuudet:
  ```bash
  poetry install
  ```
- Luo data-kansio sovelluksen juuressa:
  ```bash
  mkdir data
  ```
- Alusta tietokanta:
  ```bash
  poetry run python -m src.initialize_database
  ```
- Käynnistä sovellus:
  ```bash
  poetry run invoke start
  ```

## Ohjelman käyttö

Sovellus avautuu kirjautumisnäkymään. Luodaksesi uuden tunnuksen klikkaa "Create User" -painiketta.

Luo vähintään viisi merkkiä pitkä käyttäjänimi ja vähintään viisi merkkiä pitkä salasana ja paina "Create". Tämän jälkeen voit kirjautua tällä nimimerkillä.

Kirjautumisen jälkeen voit luoda uusia päiviä syöttämällä vasemmalla sivulla näkyvään kenttään haluamasi nimen päivälle ja painamalla "Add New Day". Uusi päivä ilmestyy näkymään.

Klikkaamalla päivää näet sen sisältämät harjoitteet. Uusia harjoitteita voit luoda klikkaamalla näkymän "Add Exercise" -painiketta.

Tämän jälkeen voit syöttää uuden harjoitteen nimen, sarjojen ja toistojen määrän sekä käytetyn painon. Tallenna harjoite painamalla "Save"-painiketta.

Tämän jälkeen voit luoda lisää harjoitteita, tai päivittää olemassa olevia harjoitteta syöttämällä uusia arvoja syötekenttiin ja painamalla "Update". Harjoitteen voi poistaa painamalla "Delete exercise" -painiketta.