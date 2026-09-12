# SmartCollaudo PRO v1.0.1

Applicazione PyQt6 per analizzare schede di collaudo Word `.docx` e generare report Excel comparativi.

## Novita' v1.0.1

- Versione letta dal file root `version.txt`, come richiesto dal flusso release.
- Aggiunto controllo aggiornamenti automatico all'avvio e manuale da **Aiuto > Controlla Aggiornamenti**.
- Aggiunto launcher compatibile `src/main.py`.
- Aggiunti test minimi e workflow GitHub Actions per build Windows con PyInstaller.

## Novita' v1.0.0

- Versione stabile candidata all'uso operativo.
- Aggiunto il pulsante **Esci** anche nella scheda **Riepilogo**, cosi' non serve tornare alla scheda **Operazioni**.
- GUI semplificata: restano solo le schede **Operazioni** e **Riepilogo**.
- La finestra finale del report mostra solo le azioni rapide essenziali.
- Il controllo preliminare resta automatico durante **Genera Report Excel**.
- Logica report congelata dalla v0.4.16: numerazione logica allineata alla v0.4.10 e correzione delle descrizioni numeriche.

## Gia' presente dalla v0.4.8

- La tabella documenti usa sempre la vista compatta: le colonne **Percorso** e **Dimensione** sono nascoste per dare piu' spazio a Stato, File, Controlli e Avvisi.
- L'opzione viene salvata nelle impostazioni utente e resta attiva tra una sessione e l'altra.
- Aggiunta conferma esplicita prima di sovrascrivere un report Excel gia' esistente.
- Migliorato il messaggio di errore quando Excel e' aperto o il file di destinazione non e' scrivibile.
- Aggiunta cartella `tools/` con prima bozza di script per creare un EXE Windows con PyInstaller.
- La logica del report Excel resta invariata rispetto alla v0.4.6.

## Gia' presente dalla v0.4.6

- GUI ottimizzata per aumentare lo spazio utile della tabella documenti.
- Intestazione superiore piu' compatta e professionale.
- Comandi documento integrati nella stessa riga del filtro:
  - **Aggiungi**;
  - **Rimuovi**;
  - **Svuota**.
- Ridotto lo spazio verticale occupato da titolo, sottotitolo, filtri e pulsanti.
- Tabella documenti con altezza utile maggiore.
- Dimensione finestra e splitter predefiniti aggiornati per dare priorita' alla tabella file.
- Pannello laterale a schede reso piu' compatto.

## Nota sulle funzioni rimosse dalla GUI

Le schede **Anteprima**, **Avvisi** e **Registro** erano presenti nelle versioni precedenti, ma restano rimosse nella v1.0.0 per ridurre complessita' e duplicazioni.
I dettagli tecnici restano comunque disponibili nel report Excel, nei fogli **Diagnostica** e **Ambigui**.

## Gia' presente dalla v0.4.0

- GUI riorganizzata in due colonne con pannello laterale semplificato.
- Filtro rapido nella tabella dei documenti.
- Menu contestuale sulla tabella file.
- Doppio clic su una riga per aprire il documento Word.
- Memorizzazione di dimensione finestra e posizione dello splitter.
- Mantiene la logica report della v0.3.5:
  - nessuna colonna `Sezione` e `Strumento` nel foglio principale;
  - esclusione righe con descrizione solo numerica;
  - annotazione `{Nr}` solo nelle celle valore con numerazione disallineata;
  - fogli `Analisi`, `Diagnostica`, `Ambigui`.

## Avvio

```bash
pip install -r requirements.txt
python src/main.py
```

## Requisiti

- Python 3.11+
- PyQt6
- pandas
- python-docx
- openpyxl
- pytest
- ruff
- Windows + Microsoft Word + pywin32 per la conversione dei controlli ActiveX.

Su sistemi senza Word/pywin32 il programma prova comunque a leggere i DOCX, ma i controlli ActiveX potrebbero non essere convertiti.

## Aggiornamenti

Il controllo aggiornamenti usa `SMARTCOLLAUDO_UPDATE_URL` oppure `SMARTCOLLAUDO_GITHUB_REPOSITORY`.
Per GitHub Releases imposta, ad esempio:

```bash
set SMARTCOLLAUDO_GITHUB_REPOSITORY=utente/repository
python src/main.py
```


## Note v0.4.8

- La finestra finale del report e' stata semplificata: Apri Excel, Apri Cartella, Copia Percorso, Chiudi.
- La tabella documenti ora usa la colonna Percorso e mostra sempre il percorso completo del file selezionato sotto la tabella.
- Il riepilogo essenziale resta nel pannello laterale; i dettagli completi restano nei fogli Excel del report.


## Versione 1.0.0

- Aggiunto pulsante Esci anche nella scheda Riepilogo.
- Numerazione logica allineata alla 0.4.10: i primi controlli tecnici partono da 3.1.
- Corretto bug descrizione numerica, ad esempio 5.1 al posto della descrizione reale.
