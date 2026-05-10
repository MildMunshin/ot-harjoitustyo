# Ohjelmistotekniikka, harjoitustyö

## Sovelluksen kuvaus

Sovelluksessa käyttäjä voi pitää kirjaa kuntosaliohjelmastaan ja kehityksestään. Sovelluksessa käyttäjä voi määritellä itselleen useasta eri päivästä koostuvan saliohjelman. Jokaiselle päivälle voi määritellä tietyt liikkeet, niiden toistokerrat ja käytetyt painot. Sovelluksen avulla käyttäjä pystyy seuraamaan päiväohjelmiaan, millä painoilla ja toistoilla liikkeitä on tehty sekä päivittämään niiden arvoja.

## Asennus

- Asenna riippuvuudet:
  ```bash
  poetry install
  ```
- Alusta tietokanta:
  ```bash
  poetry run python -m src.initialize_database
  ```
- Käynnistä sovellus:
  ```bash
  poetry run invoke start
  ```
  
## Lisätoiminnot

- Testaus:
  ```bash
  poetry run invoke test
  ```
- Toteuta coverage:
  ```bash
  poetry run invoke coverage
  ```
- Luo coverage-raportti:
  ```bash
  poetry run invoke coverage-report
  ```
- Suorita pylint:
  ```bash
  poetry run invoke lint
  ```

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/MildMunshin/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/MildMunshin/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [AI:n käyttö ja koodin kopioiminen](https://github.com/MildMunshin/ot-harjoitustyo/blob/master/dokumentaatio/AI:n_kaytto_ja_koodin_kopioiminen.md)
- [Changelog](https://github.com/MildMunshin/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/MildMunshin/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](https://github.com/MildMunshin/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [Testausdokumentti](https://github.com/MildMunshin/ot-harjoitustyo/blob/master/dokumentaatio/testausdocumentti.md)
