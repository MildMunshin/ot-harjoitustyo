# Ohjelmistotekniikka, harjoitustyö

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
  poetry run invoke coverage-raport
  ```

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/MildMunshin/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/MildMunshin/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [AI:n käyttö ja koodin kopioiminen](https://github.com/MildMunshin/ot-harjoitustyo/blob/master/dokumentaatio/AI:n_kaytto_ja_koodin_kopioiminen.md)
- [Changelog](https://github.com/MildMunshin/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
