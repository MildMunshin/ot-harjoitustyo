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


<img width="518" height="347" alt="Screenshot from 2026-05-10 19-59-20" src="https://github.com/user-attachments/assets/6261a465-05c5-4c41-ad91-819adc665248" />

Luo vähintään viisi merkkiä pitkä käyttäjänimi ja vähintään viisi merkkiä pitkä salasana ja paina "Create". Tämän jälkeen voit kirjautua tällä nimimerkillä.


<img width="518" height="347" alt="Screenshot from 2026-05-10 20-00-05" src="https://github.com/user-attachments/assets/f540f9cf-12ec-436e-8d7f-53b7155230d2" />

Kirjautumisen jälkeen voit luoda uusia päiviä syöttämällä vasemmalla sivulla näkyvään kenttään haluamasi nimen päivälle ja painamalla "Add New Day". Uusi päivä ilmestyy näkymään.


<img width="701" height="347" alt="Screenshot from 2026-05-10 20-02-39" src="https://github.com/user-attachments/assets/54ca94f5-8822-4272-9523-6a60484668f8" />

Klikkaamalla päivää näet sen sisältämät harjoitteet. Uusia harjoitteita voit luoda klikkaamalla näkymän "Add Exercise" -painiketta.


<img width="1343" height="347" alt="Screenshot from 2026-05-10 20-02-10" src="https://github.com/user-attachments/assets/c95e4af7-8478-420d-ba94-49cd156ded8e" />

Tämän jälkeen voit syöttää uuden harjoitteen nimen, sarjojen ja toistojen määrän sekä käytetyn painon. Tallenna harjoite painamalla "Save"-painiketta.


<img width="1343" height="347" alt="Screenshot from 2026-05-10 20-01-43" src="https://github.com/user-attachments/assets/9dae359a-8aca-4a07-baa8-2cbfcbbae0c4" />

Tämän jälkeen voit luoda lisää harjoitteita, tai päivittää olemassa olevia harjoitteta syöttämällä uusia arvoja syötekenttiin ja painamalla "Update". Harjoitteen voi poistaa painamalla "Delete exercise" -painiketta.
