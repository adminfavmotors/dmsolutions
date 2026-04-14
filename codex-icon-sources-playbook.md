# Codex: gdzie szukać gotowych ikon i jak je podłączać

Praktyczny cheat sheet do użycia przez Codex / agentów kodowych.

Cel: **nie rysować ikon samodzielnie**, tylko znajdować gotowe, licencyjnie czytelne zasoby i podpinać je do projektu w sposób technicznie sensowny.

---

## 1. Główne ścieżki pozyskiwania ikon

### 1.1. Biblioteki ikon jako pakiety NPM
To najprostsza droga, jeśli projekt jest na React / Next / Vite / Vue / Svelte.

Możliwości:
- instalacja gotowej biblioteki ikon jako pakietu
- import tylko używanych ikon
- użycie komponentów SVG bez ręcznego pobierania plików
- łatwiejsze utrzymanie spójnego stylu w całym projekcie

Przykłady:
- `lucide-react`
- `@tabler/icons-react`
- `@heroicons/react`
- `@phosphor-icons/react`
- `react-icons`
- pakiety Material Symbols / Material Design Icons

Kiedy ta droga ma sens:
- klasyczny UI strony lub aplikacji
- formularze, CTA, sekcje usług, dashboardy
- gdy potrzebna jest spójność stylu i szybkie wdrożenie

---

### 1.2. Agregatory wielu zestawów ikon
To wyszukiwarki / warstwy pośrednie nad wieloma bibliotekami.

Możliwości:
- wyszukiwanie jednej ikony w setkach kolekcji
- użycie rzadkich lub branżowych ikon bez zmiany głównej biblioteki
- import lokalny albo komponentowy
- dostęp do kolekcji brandowych, medycznych, akademickich, pogodowych, flag, map, gamingowych itd.

Najważniejsze opcje:
- **Iconify**
- **Icones**
- **unplugin-icons**

Typowe zastosowania:
- kiedy główna biblioteka nie ma potrzebnego symbolu
- kiedy potrzeba ikon niszowych lub branżowych
- kiedy agent ma przeszukać wiele źródeł jednym mechanizmem

---

### 1.3. Surowe pliki SVG pobierane do projektu
Zamiast używać pakietu, można pobrać konkretne pliki SVG i trzymać je lokalnie.

Możliwości:
- pełna kontrola nad plikami
- brak zależności od biblioteki runtime
- możliwość czyszczenia i optymalizacji SVG
- łatwe włączenie do sprite lub komponentów

Źródła:
- SVG Repo
- bezpośrednie repozytoria bibliotek na GitHubie
- oficjalne katalogi ikon, które pozwalają pobierać SVG

Dobre do:
- landing page’y i strony marketingowe
- ikony bardzo rzadko używane
- logo partnerów / payment icons / pojedyncze symbole specjalne

---

### 1.4. Icon font / variable font / webfont
Część zestawów oferuje ikony jako font lub variable font.

Możliwości:
- łatwe użycie w klasycznym HTML/CSS
- szybkie prototypowanie
- jedna paczka dla dużej liczby ikon

Przykłady:
- Material Symbols
- starsze warianty Font Awesome
- niektóre zestawy eksportowane jako webfont

Wady praktyczne:
- gorsza kontrola niż przy SVG
- zwykle słabsza dostępność i semantyka
- trudniej dopracować pojedynczą ikonę niż przy inline SVG

---

### 1.5. CDN / zewnętrzne hostowanie ikon
Można ładować ikony z zewnętrznego CDN lub serwisu po URL.

Możliwości:
- brak lokalnych plików
- szybki prototyp
- użycie publicznego zasobu bez instalacji

Ryzyka:
- zależność od zewnętrznego hosta
- potencjalne problemy z dostępnością, cache i licencją
- słabsza kontrola nad wersją zasobu

Ta ścieżka jest możliwa, ale wymaga ostrożności przy projektach produkcyjnych.

---

## 2. Biblioteki ogólnego przeznaczenia

### Lucide
Możliwości:
- zestaw clean outline icons
- komponenty do frameworków
- dobre do UI, sekcji usług, formularzy, CTA, feature list
- łatwe kolorowanie i skalowanie przez CSS / propsy

### Tabler Icons
Możliwości:
- bardzo szerokie pokrycie klasycznych potrzeb biznesowych i UI
- dużo ikon usługowych, systemowych, technicznych, commerce
- pakiety React i SVG

### Heroicons
Możliwości:
- zestaw prostych ikon pod klasyczny nowoczesny UI
- outline + solid
- częste użycie w ekosystemie Tailwind

### Phosphor
Możliwości:
- wiele wag i stylów
- dobre do interfejsów, które potrzebują większej elastyczności wizualnej
- duże pokrycie tematów ogólnych

### Material Symbols / Material Design Icons
Możliwości:
- bardzo szerokie pokrycie codziennych znaczeń
- łatwe do znalezienia symbole systemowe, biznesowe, mapowe, komunikacyjne
- użycie jako SVG, komponenty lub font

### React Icons
Możliwości:
- jedna paczka agregująca wiele bibliotek
- szybki dostęp do bardzo wielu zestawów przez wspólny interfejs
- wygodne przy projektach prototypowych lub szybkich integracjach

Uwaga praktyczna:
- daje szeroki wybór, ale nie rozwiązuje automatycznie problemu spójności stylu

---

## 3. Zestawy branżowe i specjalistyczne

### 3.1. Brand / social / payment / platform logos
#### Simple Icons
Możliwości:
- logotypy marek, social media, dostawców płatności, narzędzi i platform
- dobre do sekcji „integracje”, „płatności”, „social proof”, „narzędzia”

### 3.2. Tech stack / programowanie / dev tools
#### Devicon
Możliwości:
- języki programowania
- frameworki
- bazy danych
- narzędzia developerskie
- idealne do sekcji „technologie”, portfolio software house, case studies tech

### 3.3. Edukacja / nauka / akademia
Przykładowe możliwości przez Iconify / powiązane zestawy:
- Academicons
- ikony publikacji, badań, uczelni, cytowań, DOI, ORCID, bibliotek naukowych

### 3.4. Medycyna / zdrowie / opieka
Przykładowe możliwości przez Iconify / zbiory tematyczne:
- Health Icons
- Medical Icons
- symbole zdrowia, szpitali, leków, laboratoriów, opieki, rehabilitacji

### 3.5. Pogoda / klimat / outdoor
Przykłady:
- Weather Icons
- Meteocons
- symbole temperatury, opadów, wiatru, chmur, alertów pogodowych

### 3.6. Flagi / kraje / geografia / mapy
Przykłady:
- Flag Icons
- Circle Flags
- Map Icons
- GeoGlyphs

### 3.7. Gry / achievement / fantasy / gamification
Przykłady:
- Game Icons
- sety achievement, badge, inventory, skills, quest, battle, loot

---

## 4. Gdzie szukać ikon „dla różnych firm”

Dla większości realnych branż lokalnych nie trzeba osobnego branżowego pakietu. Najczęściej wystarczy szukać po słowach kluczowych w dużych bibliotekach i agregatorach.

### Typowe branże i słowa kluczowe do wyszukiwania

#### Motoryzacja / warsztat / auto detailing
Słowa kluczowe:
- `car`
- `garage`
- `wrench`
- `tool`
- `battery`
- `engine`
- `oil`
- `tire`
- `steering`
- `diagnostics`

#### Elektryk
Słowa kluczowe:
- `plug`
- `bolt`
- `flash`
- `power`
- `cable`
- `electric`
- `socket`
- `lightbulb`

#### Hydraulik / instalacje
Słowa kluczowe:
- `pipe`
- `wrench`
- `droplet`
- `water`
- `tap`
- `shower`
- `sink`
- `plumbing`

#### Szkoła językowa / edukacja
Słowa kluczowe:
- `book`
- `graduation`
- `school`
- `globe`
- `language`
- `dictionary`
- `pencil`
- `lesson`

#### Groomer / pet care
Słowa kluczowe:
- `paw`
- `pet`
- `dog`
- `cat`
- `scissors`
- `brush`
- `sparkles`
- `bath`

#### Beauty / salon / barber / kosmetyka
Słowa kluczowe:
- `scissors`
- `comb`
- `spray`
- `mirror`
- `sparkles`
- `brush`
- `makeup`

#### Gastronomia / kawiarnia / restauracja
Słowa kluczowe:
- `coffee`
- `cup`
- `fork`
- `knife`
- `burger`
- `chef`
- `menu`
- `delivery`

#### Budowlanka / remonty / wykończenia
Słowa kluczowe:
- `hammer`
- `drill`
- `ruler`
- `helmet`
- `house`
- `paint`
- `brick`

#### Transport / logistyka
Słowa kluczowe:
- `truck`
- `package`
- `route`
- `warehouse`
- `delivery`
- `map-pin`
- `navigation`

---

## 5. Katalogi i serwisy do przeszukiwania ikon

### Iconify
Możliwości:
- przeszukiwanie ogromnej liczby otwartych zestawów ikon
- użycie przez API
- eksport danych ikon
- komponenty do różnych frameworków
- praca z kolekcjami branżowymi i niszowymi

### Icones
Możliwości:
- szybkie wyszukiwanie ikon po nazwie
- wygodne do ręcznej selekcji lub wskazania konkretnych nazw dla Codexa
- dobre jako katalog referencyjny

### SVG Repo
Możliwości:
- ogromny katalog gotowych SVG
- przydatne przy rzadkich symbolach
- możliwość pobrania pojedynczych plików do projektu

### The Noun Project
Możliwości:
- bardzo szerokie pokrycie znaczeń i pojęć
- dobre do ikon mniej oczywistych, metaforycznych lub bardzo specyficznych
- dostęp przez API

### Flaticon
Możliwości:
- ogromna liczba ikon i stickerów
- łatwe wyszukiwanie kategorii biznesowych i lifestyle’owych
- przydatne do inspiracji i pojedynczych pobrań

### Bezpośrednie katalogi bibliotek
Możliwości:
- pobranie ikony bez pośredników
- lepsza kontrola nad źródłem i licencją
- łatwiejsze przypisanie ikony do konkretnego pakietu

---

## 6. Sposoby technicznego podłączenia ikon

### 6.1. Komponenty React / Next / Vue / Svelte
Schemat:
- instalacja pakietu
- import konkretnej ikony
- użycie jak zwykłego komponentu

Możliwości:
- łatwe sterowanie rozmiarem
- kolor przez CSS / propsy
- ikonę można używać warunkowo
- łatwe tree-shaking przy sensownych importach

### 6.2. Local SVG files
Schemat:
- pobranie SVG
- zapis do `assets/icons`
- użycie jako `<img>`, inline SVG albo komponent przez SVGR

Możliwości:
- pełna kontrola nad plikiem
- łatwe wersjonowanie w repo
- dobre do logo, partnerów, specjalnych ikon lub ikon z różnych źródeł

### 6.3. SVGR / konwersja SVG do komponentów
Możliwości:
- zamiana pliku SVG na komponent React
- łatwe stylowanie ikon jak komponentów
- wygodne przy niestandardowych lub pojedynczych ikonach

### 6.4. Sprite SVG
Możliwości:
- wiele ikon w jednym pliku sprite
- użycie `<use href="#icon-name">`
- sensowne przy większej liczbie powtarzalnych ikon

### 6.5. Webfont / variable font
Możliwości:
- użycie przez klasę CSS
- szybki prototyp i klasyczne wdrożenia
- bywa wygodne w prostych projektach bez frameworka

### 6.6. Runtime API / dynamic loading
Możliwości:
- ładowanie ikon tylko wtedy, gdy są potrzebne
- dobre przy bardzo szerokich katalogach i wyszukiwarkach ikon
- przydatne w generatorach i builderach

Uwaga praktyczna:
- dynamiczne ładowanie wymaga kontroli nad SSR/CSR, cache i przesunięciami layoutu

---

## 7. Framework-specific możliwości

### React / Vite
Możliwości:
- biblioteki React jako komponenty
- SVGR
- Iconify component
- unplugin-icons
- lokalne SVG importowane jako komponenty lub URL

### Next.js
Możliwości:
- biblioteki React
- lokalne SVG
- sprite
- icon components po stronie klienta
- użycie build-time pluginów zamiast runtime, jeśli projekt tego wymaga

### Vue / Nuxt
Możliwości:
- `unplugin-icons`
- Iconify
- komponenty frameworkowe
- local SVG

### Astro / SSG
Możliwości:
- lokalne SVG
- komponenty wybranej biblioteki
- build-time generowanie ikon

---

## 8. Licencje i prawa użycia — co agent ma sprawdzać

To nie jest porada „co wybrać”, tylko lista rzeczy, które **mogą się różnić między źródłami** i które trzeba sprawdzić.

### 8.1. Najczęstsze licencje spotykane przy ikonach
- MIT
- Apache 2.0
- CC BY
- Public Domain
- licencje komercyjne / premium
- licencje własne platformy

### 8.2. Co trzeba sprawdzić przed użyciem
- czy zestaw pozwala na użycie komercyjne
- czy wymaga atrybucji
- czy logo marek można użyć w danym kontekście
- czy można modyfikować SVG
- czy można osadzić ikonę w projekcie produkcyjnym
- czy wolno hostować lokalnie
- czy wolno używać przez API lub eksportować

### 8.3. Szczególny przypadek: logotypy marek
Brand icons to osobna kategoria. Nawet jeśli zestaw udostępnia logo, trzeba sprawdzić disclaimer dotyczący znaków towarowych.

---

## 9. Co Codex może robić zamiast rysowania ikon

### Możliwość 1: dobrać ikonę z głównej biblioteki projektu
- wyszukać po nazwie
- dodać import
- użyć w komponencie

### Możliwość 2: dobrać ikonę przez agregator
- znaleźć odpowiedni set
- zanotować nazwę ikony i źródło
- podłączyć przez komponent lub lokalny import

### Możliwość 3: pobrać pojedynczy SVG
- pobrać plik
- zapisać lokalnie
- oczyścić atrybuty
- włączyć jako asset lub komponent

### Możliwość 4: dobrać brand/logo z dedykowanego źródła
- pobrać logo z katalogu brand icons
- zachować oryginalny kształt
- nie „przerysowywać” logotypu samodzielnie

### Możliwość 5: użyć ikon jako sprite lub zestawu lokalnego
- kiedy projekt ma dużo powtarzalnych ikon
- kiedy trzeba ograniczyć zależności runtime

---

## 10. Wzorzec działania dla Codexa

### Szybka procedura
1. Sprawdź, czy projekt już używa jakiejś biblioteki ikon.
2. Jeśli tak, najpierw szukaj w tej bibliotece.
3. Jeśli ikony nie ma, sprawdź agregator ikon.
4. Jeśli nadal nie ma, szukaj w katalogach SVG / tematycznych setach.
5. Zweryfikuj licencję lub warunki użycia.
6. Wybierz sposób podłączenia:
   - komponent pakietu
   - lokalny SVG
   - sprite
   - webfont
7. Zadbaj o spójne nazewnictwo i miejsce przechowywania.
8. Nie twórz „własnej interpretacji” logotypu, jeśli istnieje gotowy brand icon.

---

## 11. Gotowe typy źródeł, które agent może przeszukiwać

### Open-source packages
- Lucide
- Tabler Icons
- Heroicons
- Phosphor
- Material Symbols
- Material Design Icons
- React Icons

### Unified search / aggregator
- Iconify
- Icones
- unplugin-icons

### Brand / logo sets
- Simple Icons

### Tech stack sets
- Devicon

### Theme / niche sets przez agregatory
- health / medical
- academicons
- weather
- flags
- maps
- gaming

### SVG catalogs / single-file sources
- SVG Repo
- oficjalne repo bibliotek
- oficjalne katalogi producentów zestawów ikon

### API-driven icon catalogs
- The Noun Project API
- platformy agregacyjne z API

---

## 12. Różne scenariusze użycia

### Strona firmowa / agencja / lokalne usługi
Możliwości:
- ogólne biblioteki UI
- ikony sekcji usług
- ikony kontaktu, lokalizacji, telefonu, formularza
- pojedyncze lokalne SVG dla partnerów / marek

### SaaS / dashboard / panel admina
Możliwości:
- biblioteki komponentowe
- spójny pack ikon UI
- sprite lub import komponentowy
- agregatory do rzadkich ikon systemowych

### Landing page / marketing page
Możliwości:
- biblioteki ogólne
- lokalne SVG dla rzadkich symboli
- brand icons dla integracji i partnerów
- lekkie inline SVG dla performance

### Projekt z wieloma branżami
Możliwości:
- jedna biblioteka bazowa
- niszowe ikony z agregatora
- lokalny katalog własny `assets/icons`
- mapowanie branża → lista słów kluczowych → źródła

### Builder / generator stron
Możliwości:
- runtime search w agregatorze
- duży katalog ikon z API
- local cache wybranych ikon
- system tagów i kategorii

---

## 13. Typowe problemy, które mogą się pojawić

- brak spójności stylu, jeśli używa się wielu różnych setów bez kontroli
- niejasna licencja w katalogach agregujących
- runtime lag przy dynamicznym ładowaniu ikon
- przesunięcia layoutu przy client-side icon components
- zbyt ciężkie bundlowanie, jeśli importowane są całe paczki zamiast konkretnych ikon
- hotlinkowanie do zewnętrznych SVG bez kontroli wersji
- użycie logo marki bez sprawdzenia zasad trademark usage

---

## 14. Minimalny „lifehack” do wpisania w instrukcję dla Codexa

```txt
Do not draw icons manually unless the user explicitly asks for custom icon design.
Always search existing icon libraries first.
Search order:
1) project's current icon library,
2) general open-source icon packages,
3) Iconify/Icones and thematic sets,
4) brand/dev-specific icon sets,
5) local SVG import from a catalog with visible license.
When using a brand/logo icon, prefer official or dedicated brand icon sets.
When using a rare icon, save the SVG locally instead of hotlinking a remote URL.
Always keep note of the icon source and license.
```

---

## 15. Linki źródłowe / katalogi / dokumentacja

### Biblioteki i dokumentacja
- Lucide: https://lucide.dev/icons/
- Tabler Icons: https://tabler.io/icons
- Heroicons: https://heroicons.com/
- Phosphor: https://phosphoricons.com/
- Material Symbols: https://developers.google.com/fonts/docs/material_symbols
- React Icons: https://react-icons.github.io/react-icons/
- shadcn/ui icons note: https://ui.shadcn.com/docs/changelog/2024-11-icons

### Agregatory i wyszukiwarki
- Iconify docs: https://iconify.design/docs/
- Iconify collections: https://icon-sets.iconify.design/
- Icones: https://icones.js.org/
- unplugin-icons: https://github.com/unplugin/unplugin-icons

### Zestawy specjalistyczne
- Simple Icons: https://github.com/simple-icons/simple-icons
- Devicon: https://devicon.dev/

### Katalogi SVG / API / komercyjne bazy
- SVG Repo: https://www.svgrepo.com/
- SVG Repo licensing: https://www.svgrepo.com/page/licensing/
- The Noun Project API: https://thenounproject.com/api/
- Flaticon: https://www.flaticon.com/

### Fora i dyskusje praktyczne
- Reddit / webdev — what icon libraries do you use: https://www.reddit.com/r/webdev/comments/1p72igp/what_icon_libraries_do_you_actually_use/
- Reddit / Next.js — best icon libraries: https://www.reddit.com/r/nextjs/comments/1hch2y1/best_icon_libraries_for_nextjs/
- Hacker News discussion: https://news.ycombinator.com/item?id=43808443
- Iconify issue on vendor icon sets / licensing nuances: https://github.com/iconify/icon-sets/issues/152

---

## 16. Krótkie podsumowanie

Jeśli agent ma **nie rysować ikon sam**, tylko korzystać z gotowych zasobów, to ma do dyspozycji:
- biblioteki ikon jako pakiety,
- agregatory wielu zestawów,
- katalogi SVG,
- brand icon sets,
- tech icon sets,
- niszowe kolekcje tematyczne,
- API katalogów ikon,
- lokalne przechowywanie SVG,
- sprite, komponenty i webfonty jako różne sposoby integracji.

To nie jest jedna „najlepsza” droga, tylko pełna mapa opcji, które Codex może wykorzystać zależnie od projektu.
