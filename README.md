# Group-Generator

## Introduzione
L'obbiettivo di tale programma è la generazione automatica di un elevato numero di gruppi Telegram.<br/>
Il nome di tali gruppi è prelevato da un file di testo chiamato `group_names.txt`, il quale riporta per ogni riga:
```
<nome corso>,<codice corso>
```

## Librerie
Lo script è stato sviluppato in Python 3 e le uniche librerie utilizzate finora sono:
- **Time**: in questa libreria è presente la funzione *sleep(seconds)* che permette di congelare l'esecuzione dello script per il numero di secondi specificati. È utile in questo caso, in quanto a volte è necessario attendere l'esecuzione di alcune operazioni all'interno di una pagina web (la scomparsa di un pop-up, il caricamento di un pulsante, ecc...).
- **Selenium Webdriver**: la libreria citata in precedenza, attraverso la quale è impostato tutto lo script.
