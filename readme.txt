Antud programm tõmbab youtubeist laule nimede listi põhjal.
Nimede sisestamiseks on 2 võimalust:
* tekstifail "inpfile.txt" formaadist artist@laulu nimi
* google spreadsheets, sel juhul tuleb luua spreadsheet,
  esimesele reale käivad pealkirjad nimi, artist ja kõik ülejäänud read
  žanritele, järgmistel ridadel on igal real üks laul
 * spreadsheetsi loomisel tuleb seda ka jagada kasutajaga, kelle email on
   client_secret.json failis client_email

config faili tuleb panna failitee, kuhu faile salvestatakse ja spreadsheetsi
kasutuse soovil spreadsheetsi nimi

laulud salvestatakse music kausta, iga bandi laulud oma kausta (laulude
nimed ja artistid on need mis sisse anti, mitte youtube nimed)

kui kasutatakse spreadsheetsi salvestatakse ka laulude žanrid kausta genres,
kus iga žanri jaoks on tekstifail, milles on laulude nimed koos artistidega

allalaadimise käivitamiseks käivitada musicdownloader.py, see on kirjutatud
python2.7 peale aga arvatavasti töötab ka python3.5 peal

allalaadimine võtab üsna kaua aega, tundub et paariminutise laulu jaoks u 1
minut, ma ei tea täpselt millest see sõltub, nii et on soovitatav algul
paari lauluga katsetada ja siis ülejäänud laulud käima panna pikemaks ajaks

kui laul on juba olemas ei teki duplikatsioone