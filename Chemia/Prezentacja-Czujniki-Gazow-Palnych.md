### Czujniki gazów palnych
3 III 2022
Zbiór informacji odnośnie typów czujników gazów palnych, wraz z ich mocnymi, oraz słabymi stronami.

**Wykorzystanie**<br/>
Niniejszy tekst jest skryptem do prezentacji na tytułowy temat. Niemniej jednak zawiera on wiele interesujących informacji. Projekt z pewnością można zaliczyć jako działanie ku szerszemu zrozumieniu powszechnie obecnego, choć bliżej nieznanego zagadnienia.

**PPM oraz PPB**<br/>
Standardem określania zawartości jednego elementu w innym, jak chociażby metanu w atmosferze, jest stosunek ilości cząsteczek elementu w stosunku do liczby wszystkich cząsteczek. Do dalszego przeprowadzenia wywodu konieczne jest wyjaśnienie czym jest PPM lub PPB. PPM (czyli Parts Per Milion) to liczba cząsteczek danej substancji w stosunku do miliona cząsteczek próbki. 
Obliczenia L: Przypuśćmy że w 1000 gramach powietrza znajdują się 2 mikrogramy metanu. Stężenie metanu w mieszaninie wyniesie...	
Obliczenia P: Wyrażając całość w procentach dostrzegamy jedynie nieczytelny zapis, stąd używa się kolejnych mniejszych wielkości... Przykład zastosowania PPM – Skład atmosfery... <br/>

**Katalityczny czujnik gazów palnych – pellistor**<br/>
Wykrywanie metanu i wielu gazów palnych może odbywać się poprzez ich faktyczne spalanie. Czujniki katalityczne wymagają tlenu. Dla metanu zachodzi reakcja spalania całkowitego: (Równanie I)
(Diagram I) Ciepło generowane w procesie spalania wywołuje zmianę rezystancji na termistorze sensorycznym [Rs]. Ze względu na zasadę działania czujniki tego typu  mogą wykrywać wiele różnych palnych gazów w tym samym czasie.<br/>

**Przykładowy układ czujnika**<br/>
Przedstawiony układ jest dzielnikiem napięcia. Rezystor R_H jest podgrzewany napięciem V_H inicjując reakcje spalania wewnątrz czujnika. Palny gaz który dostaje się do czujnika zwiększa intensywność reakcji i cieplnie wpływa na termistor R_S, 
który w zależności od charakterystyki prądowo-napięciowej zmienia swoją rezystancje. Dokonywany zostaje pomiar napięcia V_RL, który prowadzi do wyznaczenia zależności rezystancji od stężenia gazu palnego. (Wyprowadznie I)
Przykładowa zależność jest widoczna na charakterystyce (Charakterystyka I).<br/>
 
**FID – Flame Iionization Detector**<br/>
W tym typie czujnika wykrywanie gazu palnego odbywa się na zasadzie przewodzenia. Podgrzewana próbka wraz z płonącym wodorem generuje strumień, przez który przy wysokim napięciu może popłynąć prąd. Urządzenie jest tak skalibrowanie, że sam wodór nie generuje przeskoku. Ustalona ilość metanu, bądź innego gazu palnego powoduje przeskok prądu, który jest następnie odbierany, wzmacniany i przesyłany jako sygnał wykrycia gazu palnego. Czujnik jest trudny w obsłudze i rzadko używany...<br/>

**IR – Wykrywanie za pomocą światła**<br/>
Wykrywanie gazu palnego odbywa się na podstawie analizy optycznej. Do komory testowej wprowadza się próbkę powietrza, a następnie mierzy się tłumienie wiązki na częstotliwościach charakterystycznych dla konkretnego gazu. Tłumienie jest wprost proporcjonalne do stężenia gazu w powietrzu. Przy okrojonym układzie jest to jeden z rodzajów czujników dymu (Przykładowa charakterysytka, praca naukowa)
Doświadczenie – Odpowiedź sensora na zapalniczkę
Zapalnicza w momencie zapłonu wystrzeliwuje niewielkie ilości gazu do atmosfery. W początkowym etapie wyrzucania gazu jest go na tyle mało, że nie ulega on zapłonowi i może być wykryty przez czujnik katalityczny. Doświadczenie ma na celu pokazać czułość i szybkość reakcji czujnika na nagłe zmiany stężenia palnych gazów w atmosferze. Potrzebny sprzęt (Lista I).<br/>

**Podsumowanie**<br/>
Przedstawione czujniki mają swoje plusy oraz minusy, przedstawione zostały w następującej tabeli:

| Czujniki Katalityczne  | Czujniki FID | Czujniki IR |
|---|---|---|
| Tani | Bardzo Drogi | Drogi |
| Małych rozmiarów | Dużych rozmiarów | Średnich rozmiarów |
| Wykrywa gazy palne | Wykrywa związki organiczne | Wykrywa gazy |
| Niedokładny | Niedokładny | Dokładny |
| Wymaga kalibracji | Wymaga kalibracji | Próbka wewnętrzna |
| Wymaga tlenu | Wymaga tlenu i wodoru | Nie wymaga tlenu |
