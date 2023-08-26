# Variable Info

* device_id: l’identificatore univoco

* iaq (Indoor Air Quality): misura o un indice che valuta la qualità dell’aria interna. Calcolato considerando diversi
  parametri come la concentrazione di particelle in sospensione, la presenza di composti chimici nocivi o altre metriche
  legate alla qualità dell’aria.
  trovare il valore appropriato e chiedere se è inversamente proporzionale o meno

* electrosmog_lf: riferimento alla misura o alla quantità di elettrosmog a bassa frequenza nell’ambiente. L’elettrosmog
si riferisce alle radiazioni elettromagnetiche prodotte da dispositivi elettronici o reti wireless. La misura potrebbe
indicare la quantità di radiazioni elettromagnetiche presenti nell’ambiente.

* wifi_level: il livello di segnale o la potenza del segnale WiFi nell’ambiente. In dBm (decibel-milliwatt) o in
un’altra scala di misura. Questa informazione può essere utile per valutare la copertura o la qualità del segnale WiFi
nelle diverse aree dell’ufficio o dell’edificio.

* wifi_n: numero di reti WiFi rilevate o disponibili nell’ambiente. Indica la quantità di reti wireless presenti nelle
vicinanze del dispositivo di rilevamento.

* temperature: temperatura ambientale nell’area monitorata.

* humidity: l’umidità relativa dell’aria nell’ambiente. L’umidità relativa si riferisce alla quantità di vapore acqueo
presente nell’aria rispetto alla massima quantità che l’aria potrebbe contenere a una determinata temperatura.

* air_pressure: pressione atmosferica nell’ambiente. La pressione atmosferica è la forza esercitata dall’atmosfera sulla
superficie terrestre e viene misurata solitamente in unità come Pascal (Pa) o millibar (mbar).

* ambient_light: livello di luce ambientale nell’ambiente. Potrebbe essere espresso in unità di illuminazione come lux o
in una scala relativa.

* tvoc (Total Volatile Organic Compounds): indicazione della qualità dell’aria in relazione alla presenza di composti
organici volatili. I composti organici volatili sono sostanze chimiche che possono essere rilasciate nell’aria da
materiali o attività presenti nell’ambiente. Alcuni esempi di composti organici volatili includono formaldeide,
benzene, toluene e altri idrocarburi. Un livello elevato di TVOC potrebbe indicare una possibile presenza di
inquinanti nell’aria, che potrebbero influire sulla qualità dell’ambiente interno.


* Qualità dell’ aria 
  * VOC ppb 
  * CO2 ppm 
  * CO2 e ppm 
  * PM 10 µg/m3 
  * PM 2.5 µg/m3 
  * IAQ N.A.
  
* Comfort Ambientale 
  * Temp °C 
  * Pressione mbar 
  * Lux lux 
  * Umidità RH% 
  * Suono dB
  
* Elettrosmog 
  * Elett. HF V/m 
  * Elett. LF nT 
    
* Wifi Liv. dBm
* Wifi N. N.A.

Normalizzazione delle variabili:

Normalizza la temperatura (T) nell’intervallo da 0 a 1: T_norm = (T - T_min) / (T_max - T_min) Normalizza l’umidità (
H) nell’intervallo da 0 a 1: H_norm = (H - H_min) / (H_max - H_min) Calcolo del punteggio dell’IAQ:
Assegna un peso alla temperatura (w_T) e all’umidità (w_H). Calcola il punteggio dell’IAQ (IAQ_score) come la media
ponderata dei valori normalizzati: IAQ_score = w_T * T_norm + w_H * H_norm

# TODO

capire se c’è correlazione dei dati interni e dati esterni con stessi periodi etc…correlazione diretta o indiretta
predittiva–> cosa succede nei prossimi mesi… what if analysis se temp sale 1 grado cosa accade aglei altri parametri,
correlazione tra i vari parametri anomaly detection, dati 2 3 anni di dati capire se ci sono eventi che vanno fuori il
comportamento attes—>costruire modello comportamentale “standard” e trovari i picchi…