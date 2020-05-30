# Group-Generator

## Introduzione
L'obbiettivo di tale programma è la generazione automatica di un elevato numero di gruppi Telegram, ognuno dei quali rappresenterà un differente corso di Ingegneria Elettronica al Politecnico di Torino.<br/>
Si è scelto di utilizzare la libreria **selenium webdriver** in quanto permette l'utilizzo del browser (in questo caso Chrome) in modo automatizzato.
La scelta di utilizzare questa libreria è risultata la migliore, per semplicità di sviluppo e di esecuzione.<br/>
Il nome di tali gruppi è prelevato da un file di testo chiamato `group_names.txt`, il quale riporta per ogni riga il nome del corso e il codice corrispondente nel seguente formato:
```
<nome_corso>,<codice_corso>
```
## Librerie
Lo script è stato sviluppato in Python 3 e le uniche librerie utilizzate finora sono:
- **Time**: in questa libreria è presente la funzione *sleep(seconds)* che permette di congelare l'esecuzione dello script per il numero di secondi specificati. È utile in questo caso, in quanto a volte è necessario attendere l'esecuzione di alcune operazioni all'interno di una pagina web (la scomparsa di un pop-up, il caricamento di un pulsante, ecc...).
- **Selenium Webdriver**: la libreria citata in precedenza, attraverso la quale è impostato tutto lo script.

## Algoritmo
Alcuni dettagli sull'algoritmo eseguito dal codice:
- **Setup dell'ambiente di sviluppo**:
  - In seguito ad un problema con *Telegram Web* che non permette di eseguire il login dopo un certo numero di test dello script si è scelto di aprire *Chrome* mediante il profilo di default in modo da conservare lo stesso login anche dopo l'arresto del browser:
      ```
      options = webdriver.ChromeOptions()
      options.add_argument('path-to-default-profile')
      ```
      È possibile trovare il percorso per il proprio profilo default cercando sul browser: chrome://version/.
  
  - Dopo aver caricato il profilo default si può caricare il driver di *Chrome* utilizzando il seguente comando:
      ```
      driver = webdriver.Chrome('path-to-chrome-driver',options)
      ```
      D'ora in avanti basterà utilizzare l'oggetto `driver` per eseguire tutte le operazioni sul browser.
    
  - Lo step successivo è quello di caricare la pagina web di *Telegram Web*:
      ```
      driver.get('https://web.telegram.org/')
      ```
      La pagina web verrà aperta direttamente nella schermata principale, evitando il login.
    
  - Il comando:
      ```
      wait = WebDriverWait(driver, timeout)
      ```
      permette di creare un oggetto di tipo `WebDriverWait` che serve ad impostare un tempo di attesa ad hoc, mediante la funzione `until(condition)` passando come parametro una condizione su un determinato elemento html. Il parametro `timeout` indica il numero di secondi di attesa prima che la funzione dia errore.

- **Apertura del file di testo**: il file dovrebbe contenere, per ogni riga, il nome del corso e, separato dalla virgola, il codice corrispondente, per esempio:
    ```
    Nome del Primo Corso,FD89076
    Nome del Secondo Corso,EL67834
    ```
- **Iterazione sui gruppi**: questa parte dello script è racchiusa in un ciclo che itera su tutti i corsi presenti nel file di testo. Ogni operazione eseguita in questa fase dello script consiste nell'identificazione di un pulsante da cliccare mediante il suo xpath (cliccare sul pulsante che si vuole identificare all'interno della pagina web con il tasto destro, poi cliccare su *Ispeziona* e dunque cliccare con il tasto destro sul corrispettivo elemento in html e selezonare *Copy XPath*) e successivamente il pulsante viene cliccato (metodo `click()`), oppure viene scritto qualcosa (metodo `send_keys('ciò-che-vuoi-scrivere')`) nel caso in cui si tratti di una casella di testo (variabili in cui è presente `_tab_` nel nome).
Un esempio di comando per cliccare un pulsante è il seguente:
  ```
  hamburger_button_xpath = 'xpath-of-the-hamburger-button'
  wait.until(ec.element_to_be_clickable((By.XPATH, hamburger_button_xpath)).click()
  ```
- **Creazione del gruppo**: per la creazione di ogni gruppo vengono eseguite le seguenti operazioni:
  - Cliccare sul pulsante a forma di hamburger in alto a sinistra;
  - Cliccare su *Nuovo gruppo*;
  - Cercare `$PrimoUtente` nella tab di ricerca e selezionarlo;
  - Cliccare su *Avanti*;
  - Inserire il nome del gruppo e cliccare su *Crea Gruppo*;
  - Aspettare che il pop-up scompaia (utilizzo un `try-except` per i pop-up);
  - Cliccare sull'header del gruppo;
  - Selezionare *Aggiorna a super magruppo* (per avere descrizione e link di accesso);
  - Cliccare su *OK*;
  - Aspettare la scomparsa del pop-up e cliccare sull'header del gruppo di nuovo;
  - Selezionare *Modifica* e inserire la descrizione;
  - Cliccare su *Salva*;
  
## Problemi e risoluzioni
Il problema che bisogna affrontare al momento è quello di un errore che viene mandato dal server di *Telegram* nel caso in cui viene identificata una velocità di esecuzione delle operazioni troppo elevata.
Questo problema causa l'impossibilità di fare qualsiasi cosa per un periodo di tempo successivo.
Nonostante si sia fatto il possibile per aumentare la velocità di esecuzione dell'algoritmo, adesso bisogna fare un passo indietro e stabilire una velocità minore, aggiungendo varie chiamate al metodo `sleep()`.
In questo modo si può provare a stabilire un tempo di esecuzione maggiore, ma comunque minore di quello che verrebbe impiegato da un utente nello svolgere le stesse operazioni, soprattutto considerando l'elevato numero di iterazioni.
