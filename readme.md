# Opdracht: Letterfrequenties
Niels Bijl 1754339 <br>
Floris Videler 1758374

## How to run
Voor het trainen op een Engelse text:<br>
`python train_mapper.py < data\entext.txt | sort | python train_reducer.py | python train_reduce_to_matrix.py en` 

Voor het trainen op een Nederlandse text:<br>
`python train_mapper.py < data\nltext.txt | sort | python train_reducer.py | python train_reduce_to_matrix.py nl`

Voor het valideren:<br>
`mapper.py < data\validation.txt | sort | python reducer.py | python reduce_to_matrix.py | python reduce_to_validation.py exported_models\en_fit.npy exported_models\nl_fit.npy`

## Resultaten
In het validatie bestand staan 191 regels waarvan 73 in het Nederlands en 118 in het engels. Met de train tests die ook op deze GitHub staan zaten wij er 4 of 5 naast. Best een goede score!
<br><br>
![resultaat](https://i.ibb.co/KXkDwzk/letterfrequenties-result.png)