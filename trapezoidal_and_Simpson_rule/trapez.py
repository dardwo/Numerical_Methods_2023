"""TEST 3

NEWTON(stycznych)
-warunek zbieżności f(a)*f(b)<0 i f’(x) i f’’(x) nie zmieniają znaku w [a,b], to przyjmując x0 t.z. f’(x0)*f’’(x0)>0 jest zbieżne
-najszybciej zbieżny ze wszystkich 
-wykładnik=2



-wybór punktu startowego:
(f(a)·f(b) < 0); k = 0, 
gdy f ’(x)·f ”(x) > 0 dla x 𝜖[a, b] to przyjmij x0= b; 
 gdy f ’(x)·f ”(x) < 0 dla x 𝜖[a, b] to przyjmij x0= a;

M.BISEKCJI
-warunek zbieżności: jedynie ciągłość funkcji
-wykładnik=1 (zbieżne liniowo)

-wystarczy wykonać k=k(eps)=sufit(log2(b-e)/eps)   -1



M.SIECZNYCH
-warunek zbieżności f(a)*f(b)<0 i f’(x) i f’’(x) nie zmieniają znaku w [a,b], to przyjmując x0 i x1 t.z. f’(x0)*f’’(x0)>0  i f’(x1)*f’’(x1)>0 jest zbieżne
-dla 0 jednokrotnych i dostatecznie gładkich funkcji ok.1,618
-jako wariant metody newtona to m.siecznych jest zbieżna lokalnie



KWADRATURy
-Korzystamy gdy: 
	-nie potrafimy wyznaczyć
	-bardzo skomplikowane do wyznaczenia
	-funkcja podcałkowa jest dana tabelarycznie
	-błąd kwadratury oblicza się w oparciu o odpowiednią pochodną funkcji podcałkowej
-Kwadratury interpolacyjne oparte na węzłach o łącznej krotności n+1 są rzędu co najmniej n+1.
-otrzymywanie; całkowanie funkcji interpolującej funkcję podcałkową 

Kryteria zakończenia procesu iteracyjnego: 
1. znalezienie przybliżenia spełniającego warunek |f(xk+1)| ≤ epsilon, 
2.zbieżność iteracji, czyli |xk+1 – xk | ≤ epsilon, 
3. zbieżność iteracji |xk+1 – xk | ≤ epsilon* |xk+1 |, 
4. awaryjne kryteria zakończenia obliczeń w przypadku zbyt długo trwającej iteracji: 
	• ograniczenie na maksymalną ilość iteracji, 
	• xk poza przedziałem (a, b), 
	• |f(xk+1)| > |f(xk)|
 """