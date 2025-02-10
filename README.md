
# Worklog on 30 Days of streamlit

Basierend auf [30days Streamlit](https://30days.streamlit.app/)

## Day 1
Mit `conda create -n stenv python=3.11` habe ich eine Conda-Umgebung mit dem Namen `stenv` und der Python-Version `3.11` erstellt.
- [ ] Ich frage mich, wo diese wohl erstellt wird.

> 💡 Beim Initialisieren musste ich zunächst in VS Code das Terminal von `psh` zu `cmd` wechseln, da PowerShell aus irgendeinem Grund `conda` nicht aktivieren wollte. Daraufhin habe ich dann `conda init` und `conda activate stenv` gemacht.

## Day 2
Meine leere `streamlit_app.py` Datei habe ich lieber mit `type nul > streamlit_app.py` in der Kommandozeile erstellt. Mit `streamlit run streamlit_app.py` läuft die App dann auch lokal.

## Day 3
Ich habe einen Button erstellt mit `st.button`. Yay, ist doch wunderschön, oder?

![Day 3 App](media/day3-app.png "Screenshot of the app created on Day 3 showing a button created with st.button")

## Day 4
joa... hier habe ich mir ein Video angeschaut.
Cool zu sehen wie er Lamda functions nutzt und wie man einfache Dashboard bauen kann.

## Day 5
ich habe noch ein Bild hinzugefügt.

## Day 6
app nach github gepusht

## Day 7
geskipped, weil ich es nicht in der streamlit community publishen will. Ansonsten wäre es der Plan die App an dieser Stelle dort zu hosten

## Day 8
okay, man kann nice sliders erstellen und deren Werte auslesen.
```python
values = st.slider(
     'Select a range of values and set a step',
     0.0, 100.0, (25.0, 75.0))
st.write('Lower bound value:', values[0], 'Upper bound value:', values[1])
```
### Code Erklärung
- `st.slider`: Erstellt ein Slider-Widget.
- `'Select a range of values and set a step'`: Beschriftung für den Slider.
- `0.0, 100.0, 1.0`: Mindest- und Höchstwerte für den Slider und Schritt.
- `(25.0, 75.0)`: Standardmäßig ausgewählter Bereich.
- `st.write`: Zeigt die ausgewählten unteren und oberen Grenzwerte des Sliders an.

## Day 9
Die Erstellung eines einfach Charts geht mit dem `st.line_chart` Befehl der auf dem `st.altair_chart` Befehlt basiert. Hier habe ich ein bisschen mehr herumexperimentiert. Siehe dazu auch `streamlit_app_day10.py`.

## Day 10
Auswahlboxen kann man easy mit `st.selectbox` erstellen. Die Auswahl kann man dann weiter im Code nutzen indem die Auswahl einer Variable zugewiesen wird und diese weiter genutzt wird.

## Day 11
Es gibt mit `st.multiselect` auch die Möglichkeit eine Mehrfachauswahl zu ermöglichen.

## Day 12
`st.checkbox` kann genutzt werden um ja wow checkboxes zu erstllen. Das Ausblenden ist irgendiwe merkwürdig, da lediglich das Label und nicht die Checkbox ausgeblendet wird. Naa, der Usecase muss dann angeschaut werden, wenn man ihn brauch. Man kann ja auch die checkbox hinter einem if statement legen. 

## Day 13
GitHub Codespace test. Joa ehrlich gesagt war das nicht so erfolgreich. Habe zwar ein Codespace erstellt aber dann die App nicht dort zum Laufen bekommen. Hatte dann auch keine Lust mehr weiter herumzuprobieren.

## Day 14
Ja super, mit der Komponente läuft man direkt in einen Error rein. Auch keine Lust das zu debuggen.

## Day 15
Okay cool. man kann mit `st.latex` Formeln in Latex darstellen.

## Day 16
Wenn man ein `config.toml` File anlegt um den Style zu ändern, dann muss die App neu gelateden werden mit dem `streamlit run streamlit_app.py` befehl, da ansonsten das ConfigFile nicht berücksichtigt wird.

## Day 17
Anscheinend speichert man secrets in `.streamlit.secrets.toml`. Ich frage mich was das für einen Unterschied macht zu Secrets die man in einer `.env` speichern würde

## Day 18
Der Upload ist erstmal gefailed weil ich natürlich nicht gelesen hatte, dass man CSVs hochladen soll. Dann mit einem deutsch CSV (also Semicolon getrennt) waren die Daten bescheuert ausgelesen. Habe ich dann als Grund genutzt eine Helper-Function in `helper.py` zu definieren, die ersteinmal schaut welchen delimeter wir nutzen um entsprechend das CSV auszulesen. Dann gings.

## Day 19
Es geht ans Gestalten der Webseite. Dafür wurde der Screen wide gestellt, eine Sidebar erstellt und Eingabefelder berücksichtigt. Das schöne ist, es gibt [hier](https://docs.streamlit.io/develop/api-reference/layout) viele tolle Module. Schau sie dir mal an.

## Day 20
Sicherlich ein spannendes Video über `tech Twitter Space` aber ganz ehrlich, was war nochmal Twitter?

## Day 21
Man kann Progressbars mit `st.progress` bauen. Da muss man dann iterativ Zahlen hinzufügen. In dem Test läuft das durch einen Loop, kann man evtl sich überlegen ob es sinnvoll wäre eine Progressbar so zu bauen, dass durch if bedingungen oder ähnliches der Progress getrackt wird.

## Day 22
Wenn man mit `st.form` Eingaben bündelt, muss man diese mit einem Button der App zurückgeben. Das führt dazu, dass die App nicht jedes Mal geladen wird sondern erst beim Ausführen des Buttons.

## Day 23
Sofern man über die URL direkt Daten mitgeben und auslesen will, sollte man sich `st.experimental_get_query_params` mal anschauen. Habe ich an dieser Stelle nicht implementiert.