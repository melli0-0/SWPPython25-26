```table-of-contents
title: Inhaltsverzeichnis 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
include: 
exclude: 
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in console
```

## Compiler- vs. Interpretersprachen

Compilersprache: 
- wandelt Code in Maschinensprache für ein Ziel um
- Compilersprachen sind schneller -> direkt Maschinencode
- muss Speicher richtig überwachen und verwalten
- C, C++, C#, ... 

Interpretersprache: 
- braucht extra Software (Interpreter): "Echt Zeit" Interpretation
- Interpretersprachen können unabhängig überall laufen 
- Speicher muss nicht selber gemanaged werden  
- Python, Perl, ...


## Prozesse und Threads

Ein Prozess ist eine Instanz eines Programms, die ausgeführt wird. 
Der Prozess besteht dann aus 1 oder mehreren Threads (einer für Sound, einer Bild, ...). 
Prozesse kommunizieren nicht miteinander, Threads schon
Wenn mehrere Kernel vorhanden sind, können die Threads parallel laufen -> verbessert Laufzeit. Sonst wird die Parallelität nur "vorgegaukelt"

## Rekursion und Iteration

Rekursive Methoden sind Methoden, die sich selbst aufrufen und ihre Parameter ändern. Diese Wiederholung geht bis Bedingung erfüllt ist, dann wird sie in eine Iteration umgewandelt.
Iteration ist eine Schleife.
- Rekusion
	- übersichtlicher
	- oftmals weniger Code bei komplexen iterativem Code
	- z.B. Fibonacci
- Iteration
	- schneller (braucht keinen extra Speicherplatz für zwischengespeicherte Variablen)
	- z.B. while - Schleife


## Programmierparadigmen

- Imperative Programmierung
	- Schritt für Schritt 
	- Fokus auf Zustände & Anweisungen
	- Schleifen sind typisch
	- z.B. C, C++
	```
	int s = 0;
	for (int i = 0; i < 10; i++){
		s += i;
	}
	```

- Deklarative Programmierung
	- Ziel wird beschrieben, nicht der Ablauf
	- z.B. SQL, HTML
	```
	SELECT title FROM articles WHERE id = 1;
	```

- Objektorientierte Programmierung
	- Klassen, Objekte, Vererbung
	- z.B. C++, C#, Java
	```
	class Articles{
		private int id;
		private String name;
		
		public Articles(int id, String n){
			this.id = id;
			this.name = n;
		}
	}
	```

- Funktionale Programmierung
	- Fokus auf Ausdrücke statt Anweisungen
	- alles ist ein Returnwert von anderer Methode
	- z.B. Haskell, Lisp, Teile von JS / Python
	```
	auto square = [](int x) {return x * x;};
	int result = square(2); 
	```


## Compilierter Code

- Compiler übersetzt Quellcode in Maschinencode
- Optimiert (unnötige Befehle entfernen)
- Verknüpft

Ein Prozessor hat verschiedene Speicherbereiche, in denen Daten verwaltet werden:

- Register
	- sehr schnell, direkt auf CPU
	- `int a = 5;` 
	
- RAM 
	- Laufzeitdaten
	- z.B. Arrays

- ROM
	- permanente, unveränderbare Daten
	- teils Firmware
	
- Stack
	- im RAM 
	- Variablen und Funktionsaufrufe
	- z.B. Parameter, Rücksprungadressen
	
- Heap
	- dynamischer Speicher
	- z.B. `new` in C++


Auf Maschinencode - Ebene bestehen Anweisungen aus Assembly - Befehlen
 - MOV, JMP, ADD, AND, IN, ...

## ARGS und KWARGS

Schlüsselwörter um beliebig viele Parameter an eine Funktion zu übergeben
ARGS - (un)bestimmte Länge
Tuple
KWARGS - bestimmter Länge
Dictionary
 // Keyword Arguments


## Python Interpreter

Assembly - C - Python

Python hat mehrere Interpreter 
- Cpython - zeilenweise interpretieren
- PyPy - JIT Interpreter (just in time): nicht so gut mit C Extentions kombinierbar 
- Jython - benutzt Java Virtual Machine JVM
- IronPython - bei Verwendung mit .net


## Stackspeicher

Stack ist ein Sonderbereich im RAM 

Prozess bekommt Speicher von OS -> Stackspeicher (inkl. Variablen, Referenzen, …) ist ein begrenzter Speicher

Reverenz: a=5  Referenz a zeigt auf die (int) 5 im Speicher (ähnlich wie eine Adresse) / "Pointer"


## Garbage Collection

Wird eine Variable nicht mehr verwendet, wird sie freigegeben um etwas Neues speichern zu können.
Referenzzähler: a = 5, Die Referenz a wird 5 Mal verwendet wenn man dann `b=a` setzt wird der Referenzzähler um 1 erhöht.
Wenn man b nicht mehr braucht, bzw. der Counter auf 0 wäre (Variable nicht benötigt). Dann kommt der Garbage Collector (periodisch) und 
Garbage Collector kommt periodisch und gibt alle nicht benötigten Variablen etc. frei.
Der Garbage Collector teilt Speicher in zwei Hälften und kopiert alle Referenzen (wo Counter nicht 0) in die neue Hälfte.
Garbage Collector kann ausgeschaltet werden und mit 
del() können Referenzen manuel gelöscht werden (~ 10% mehr productivity, da GC nur periodisch freigibt)
del(a): (command) - löscht referenz weist garbage collector zu a freizugeben (GC kommt normal periodisch vorbei, nicht früher)

```
import gc
gc.get_threshold()
(700, 10, 10)
```

MAN KANN NICHTS LÖSCHEN NUR FREIGEBEN!


## Bedingte Ausdrücke

var = (20 if x == 1 else 30)
A if BEDINGUNG else B


## Match Case

Match Case ist wie Switch Case in Python
Automatisches Break, muss nicht gecoded werden
case _ ist der Default

```
>>> a = 2
>>> match(a):    
...     case 0: print(f'0:{a}')  
...     case 1: print(f'1:{a}')  
...     case _: # default    
...         print(f'default: {a}')  
...            
default: 2
```



## Kontrollstrukturen

Anweisungen, die die Reihenfolge von Befehlen in einem Programm bestimmen

#### Sequenz (Reihenfolge)

Befehle nacheinander
```
a = 1
b = 2
print(f'a+b=')
```
#### Verzweigung (Bedingungen)

If, Else, Switch/Match
```
if a == 1:
	print(f'True')
else:
	print(f'{a=}')	
```
#### Schleifen

For, While, Do ... While
```
>>> for i in range(4):  
...     print(i)       
0  
1  
2  
3
```
#### Sprungstrukturen (Überspringen)

break, continue, return, pass
```
>>> for i in range(2):  
...     if i > 1: break  
...     print(i)    
0  
1
```
#### Fehlerbehandlung

try, except, else, finally
```
>>> try:    
...     val = int('defnoInt')  
... except ValueError:  
...     print('No Integer :(')  
... finally:    
...     print('finally')        
No Integer :(  
finally
```
#### Funktionen / Rekursionen

#### Parallelität

Interrupts ist Code, der unabhängig vom Hauptprogramm ausgeführt wird

#### Async Abläufe

millis, async/await



## Datenstrukturen

Es gibt nur **zwei** Datenstrukturen (alle anderen, z.b. dictionaries arbeiten mit denen zwei)

- **Array**
- **Listen** (Linked Lists)

**Array** 
- zusammenhängende Datenstruktur mit fixer Länge 
- Daten liegen hintereinander
- schneller Zugriff, direktes Indexing
- langsames Einfügen / Löschen, da Array fixe Größe hat
- nur ein Datentyp (außer bei Objects)
- CPU liest 40 Byte in Registerbank 

**List**
- Element enthält Daten und Zeiger auf nächstes Element ("Inseln")
- langsamer Zugriff, da man schauen muss wo das nächste Element ist (Zeiger)
- schnelles Einfügen / Löschen
- letztes Element zeigt auf NULL oder None
- verschiedene Datentypen möglich
- Liste ist nicht beschränkt (außer der Speicher ist voll x_x )

**ArrayList**
- in Java
- wenn Array voll ist, wird das Array verdoppelt und Elemente werden EINZELN ins neue kopiert
- Beide Arrays sind solang vorhanden bis GC das alte freigibt
	- Achtung: wenn GC nicht schnell genug ist, kann es zu einer Memory Overflow Exception kommen (Speicher voll)

**Dynamischer Array / Python-Lists**
- in Python gibt es eigentlich keine Arrays, außer Import Array (wird selten verwendet)
- ist wie eine ArrayList 
- append() - fügt Element hinzu
- remove() - löscht Element
- in Python wird je nach Version das Array nicht jedes Mal verdoppelt, sondern irgendwann nur mehr 40 % oder 5 % , ... (Speichermanagement)
- Bei "echten Arrays" wir der Datentyp angegeben
	- i ... integer (unsigned - positiv) 
	- I ... integer (signed - 1 Bit mehr)

**Zuordnungs Datenstruktur (Dictionary / HashMap)** 
- Key-Value-Pairs
- dynamische Arrays mit Liste verbunden
	- Key: linkedList / Array
	- Valus: dynamisches Array
	- Verknüpfung: Hash-Mechanismus / List
	
- Achtung: in früheren Python-Versionen ist die Reihenfolge nicht garantiert
	- sorted Dictionaries
	


## Zufallszahlen

Echte Zufallszahlen sind schwer mit Computer möglich, deswegen werden sogenannte Pseudo-Zufallszahlen erzeugt. Diese werden mithilfe der Zeit, Macadressen, Seriennummern, etc. erzeugt.

## Type Hinting / Type Checking / Data Validation

**Type Hinting**
Hinweis auf Datentypen geben um die Lesbarkeit zu verbessern. 
Wird nicht zur Laufzeit geprüft.

**Type Checking**
externe Tools prüfen vor der Laufzeit, ob die richtigen Datentypen verwendet worden sind. 
z.B. MyPy 
- Problem: oftmals nur static analasys möglich, der Code kann  normal ausgeführt werden und funktioniert dennoch.
- Nicht gut bei APIs, da die Datatypes vor der Laufzeit nicht bekannt sind

**Data Validation**
Prüfung während der Laufzeit
z.B. pydantic
(@Annotation) - sind gut für API, DB, … 
Man kann auch manuel Fehler werfen (raise Error)
Prüft nicht nur Typen sondern auch Constraints und Regeln
Kann automatisch konvertieren ("38" -> 38)


## self

Verweis auf das aktuelle Object einer Klasse
- wie this
self muss als erstes Argument in jeder Instanzmethode stehen!
self ist bei statischen Methoden nicht notwendig

## Coding Richtlinien

Varieren je Firma, Ort, ...

- Methoden atomar (ohne Prints)
- mit MAIN Methode
- Name convention: name_name
- english
- kurze knappe Kommentare
- lokale variablen
- Parameter (nur 1mal ändern)
- nicht mit TABS programmieren
- and und or ausschreiben
- Keywords nicht vergessen (int, yield, …)


## Comprehensions

Eine Comprehension ist eine kompakte Möglichkeit, Datenstrukturen zu erstellen. Comprehensions werden verwendet um Code besser lesbar zu machen, die Funktionen unterscheiden sich dabei nicht.
z.B. chr(65) ... Ascii Number --> A

#### List Comprehensions

```
# [ <Ausdruck> for <Element> in <Iterable> if <Bedingung> ]
[print(i) for i in range(4) if i%2==0]
```

#### Set Comprehensions

Datenstruktur mit unique Elemente

`{print(i) for i in range(10)}`


#### Dict Comprehensions

Key-Value-Pairs

`{i: i*i for i in range(10)}`

## Walrus Operator

:= 
Weist einer Variable innerhalb einer Expression einen Wert zu
`print(value := True)`

## Copy & DeepCopy

```
a = [1, "Hello", [3.14, "world"]]
b = a.copy()
a[2][0] = 99 
import copy
c = copy.deepcopy(a)
a[2][0] = 45
a  
[1, 'Hello', [45, 'world']]  
b  
[1, 'Hello', [45, 'world']]  
c  
[1, 'Hello', [99, 'world']]
```

copy: kopiert immer den aktuellen stand 
deepcopy: kopiert nur den jetzigen stand


## Tiefen- und Breitensuche

**Tiefensuche**
(Depth - First Search DFS)
geht so tief wie möglich in einen Pfad bevor man zurückgeht
Stake

**Breitensuche**
(Breadth - First Search BFS)
geht alle Knoten einer Ebene durch, erst dann in die nächste Ebene
Queue

## range()

range() erzeugt eine Sequenz von Zahlen
Werte werden bei Bedarf generiert (Speichereffizient)
```
for i in range(5):
	print(i)
```

Syntax: `range(start, stop, step)`


## Shebang

Kann am Anfang eines Skripts stehen, um den Interpreter anzugeben, der das Skript ausführen soll

`#!/usr/bin/env python3`

Dateiendungen sind dabei nicht wichtig (nur fürs Programm)


## Mutable vs. Immutable

**mutable**
- Inhalt eines Objects kann geändert werden
- Lists, Dictionaries, Sets, bytearrays
- in Java werden Seiteneffekte durch private, get, set verhindert

**immutable**
- Object muss neu angelegt werden, wenn man es ändert möchte
- primitive Datentypen
	- Integer, Float, String, Tuple(Liste), Frozenset
- Rust ist immutable, deswegen auch schneller als C

```
>>> a
[1, 2, 3]
>>> b=2
>>> id(b)
140728045433672
>>> id(2)
140728045433672
>>> id(a[1])
140728045433672

-> Liste ist mutable (veränderbar)
>>> id(a)
1937334178560
>>> a[2] = 99
>>> id(a)
1937334178560 
```


## Dunder

Meistens werden Variablen als Dunder Variablen und Methoden als Magic Methods bezeichnet.  Sie sind ein Teil der Grund-Standard-Funktionen.
Dunder: Double Underscore
`__name__` 
Dunder für alle Methoden / Variablen verwendet, die von Python (Interpreter) selber befüllt / ausgeführt werden

Können überschrieben werden.

z.B. um von anderen Skripts main aufzurufen


## Operator overloading 

Einem Operator (z.B. +) eine andere Bedeutung geben.
Operator Overloading soll nur in so fern verwendet werden, dass die standard Bedeutung nicht total abweicht (Übersicht)


## f String & raw String

```
>>> a = 'alias'  
>>> print(f'this {a} is a fstring')  
this alias is a fstring
```

Mit f Strings kann man Variablen direkt über {} mitgeben

```
>>> print(f'this {a=}')  
this a='alias'
```

 Mit {var = } wird ein Wert direkt ausgegeben oder auch berechnet z.B. {1+1=}

```
>>> print(fr'this {b}')  
this /bthis/t
```

Raw String werden verwendet um einen String nur als String zu sehen, z.B. keine Zeilenumbrüche etc. (Achtung: aus div. Gründen darf das letzte Zeichen kein / sein) 

f Strings können auch nested werden (geht aber so nur in bestimmten Python Versionen)


## isinstance()

Eine Funktion, die True returned, wenn ein bestimmtes Objekt einen speziellen Datentyp(en) hat.
`isinstance(object, type)`
Als Type können auch mehrere Typen angeben werden, dann wird True returned wenn das Objekt einen dieser Datentypen hat.
`isinstance(var, (int, str, float, list))`


## eingebaute Funktionen

[[https://openbook.rheinwerk-verlag.de/python/19_008.html#u19.8]]


## Exception Handling

Wenn ein Fehler gefunden wird, wie geht man mit diesem Fehler um?
Wie kann man das Programm stabil halten? -> Richtige Fehler behandeln. 
Fehlercode: sys.exit() -> 0 ... fehlerfrei

#### Lokal behandeln

Fehler wird direkt in der Methode geworfen und behandelt.

#### Lokal weiterreichen

Fehler wird in der Methode geworfen, aber weitergerreicht - throw
Wenn man den Fehler in der Methode eventuell nicht abhandeln kann.

#### Weiterreichen

Fehler wird abgefangen, kann nicht behandelt werden und wird weitergegeben

#### Behandeln

Fehler wird abgefangen und behandelt.

#### Main

try - except:
	sys.exit(1)




[^1]

[^1]: Author: Melli Lindebner

