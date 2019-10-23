
# `skidpad_planner`

Paczka `skidpad_planner` odpowiada za wygenerowanie ścieżki odpowiadającej układem trasie typu Skid Pad z [FSAE](https://www.fsaeonline.com/). Kształt trasy odpowiada poniższemu rysunkowi, lecz wymiary mogą być konfigurowane. Szerokość trasy pomija się.

![](https://eforce.cvut.cz/wp-content/uploads/2018/09/skid-1.jpg)

Przy uruchomieniu węzeł `skidpad_planner` generuje za każdym razem trasę w takim położeniu, aby pojazd znajdował się na jej początku - niezależnie od jego położenia w przestrzeni.

## `skidpad_planer`

## Published topics
`path`([std_msgs/Float64](http://docs.ros.org/api/std_msgs/html/msg/Float64.html)) Najbliższy aktualny odcinek ścieżki, publikowany w układzie współrzędnych `skidpad`. Do stosowania bezpośrednio na wejście systemu sterowania. **Nie wymagane jest dodatkowe stosowanie paczki `path_extractor`.**

`skidpad`([visualization_msgs/Marker](http://docs.ros.org/api/std_msgs/html/msg/Float64.html)) Wizualizacja wygenerowanej trasy.

`s` ([std_msgs/Float64](http://docs.ros.org/api/std_msgs/html/msg/Float64.html)) Postęp na trasie (w metrach).

# Parameters

## Track dimensions

`~/skidpad/R` (`double`, default: 5.0) Promień obydwu zakrętów.

`~/skidpad/a` (`double`, default: 5.0) Długość rozbiegu (Entry).

`~/skidpad/b` (`double`, default: 5.0) Długość wyjazdu (Exit).

## Path configuration

`~/path/start` (`double`, default: -1.0) W jakiej odległości od samochodu powinna zaczynać się publikowana ścieżka.

`~/path/stop` (`double`, default: 2.5) W jakiej odległości powinna się ona kończyć.

`~/path/step` (`double`, default: 0.25) Jaki powinien być odstęp między kolejnymi punktami ścieżki.

## Required transforms:

`map` → `base_link`

## Published transforms:

`map` → `skidpad`
