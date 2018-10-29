# Matrix_class
Questa classe permette di fare calcoli tra **matrici** e trovare il _determinente_, la _matrice inversa_ ecc. di una matrice e di eseguire calcoli con essa e altre.
<br>
### Funzionamento
Per creare una matrice chiamare Matrix(arg) dove come argomento puoi scegliere tra:
<ul>
<li>Una stringa con colonne separate da ";" e righe da spazi<br>es: "1 2 3; 2 3 4; 3 4 5"</li>
<li>Una lista o tuple contenente le righe della matrice, e ogni riga composta da tuple o lista contenente i valori<br>es: ((1, 2, 3), (2, 3, 4), (3, 4, 5))</li>
</ul>
 Se quindi si scrive <code>A = Matrix("1 2 3; 2 3 4; 3 4 5")</code> verrà creato un oggetto matrice A.
 Se si scriverà <code>print(A)</code> si otterrà<br><pre>
┎                 ┒
┃ 1     2       3 ┃
┃ 2     3       4 ┃
┃ 3     4       5 ┃
┖                 ┚</pre>
ossia il formato user-friendly.

#### Le operazioni permesse sono:
<table>
<tr>
<th>Comando</th><th>Risultato</th>
</tr>
<tr><td>str(A)</td><td>Stringa con la matrice A in formato <b>user-friendly</b></td></tr>
<tr><td>A + B + ...</td><td><b>Somma</b> (e differenza) tra matrici A e B ecc...</td></tr>
<tr><td>A * B * ...<br>A * 2<br>A / B</td><td><b>Prodotto</b> (e divisione) tra matrici o tra una matrice e un numero</td><tr>
<tr><td>A.addcolumn(colonna)</td><td>Aggiungere una <b>colonna</b> ad A</td></tr>
<tr><td>A.addrow(riga)</td><td>Aggiungere una <b>riga</b> ad A</td></tr>
<tr><td>A.delcolum(indice)</td><td>Eliminare la colonna {indice}</td></tr>
<tr><td>A.delrow(indice)</td><td>Eliminare la riga {indice}</td></tr>
<tr><td>A.replacerow(indice, riga)</td><td>Sostituire una riga con una data</td></tr>
<tr><td>A.replacecolumn(indice, colonna)</td><td>Sostituire una colonna con una data</td></tr>
<tr><td>A.arrotonda([cifre])</td><td>Creare una matrice con ogni numero <b>arrotondato</b> a (di default) due cifre decimali</td></tr>
<tr><td>A.fraziona()</td><td>Crea una matrice con i valori sotto forma di oggetto Fraction e non float o int</td></tr>
<tr><td>A.compl_alg(r, c)</td><td>Ottenere il <b>Complemento algebrico</b> della matrice A in (r, c): A<sub>(r, c)</sub></td></tr>
<tr><td>A.min_compl(r, c)</td><td>Ottenere il <b>Minore complementare</b> della matrice A in (r, c): M<sub>(r, c)</sub></td></tr>
<tr><td>A.det()</td><td>Ottenere il <b>determinante</b> della matrice A</td></tr>
<tr><td>A.inversa()</td><td>Ottenere la <b>matrice inversa</b> della matrice A</td></tr>
<tr><td>A.opposite()</td><td>Ottenere la matrice A con ogni numero sostituito dal suo <b>opposto</b></td></tr>
<tr><td>A.trasposta()</td><td>Ottenere la matrice <b>trasposta</b> della matrice dei complementi algebrici</td></tr>
<tr><td>Matrix.zero(lato)</td><td>Creare una matrice <b>nulla</b> di lato dato (static method)</td></tr>
<tr><td>Matrix.uno(lato)</td><td>Creare una matrice <b>unità</b> di lato dato (static method)</td></tr>
</table>

### License
GNU GPLv3.0<br>
Read the file LICENSE for more information
