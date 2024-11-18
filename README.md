<!-- ia_tp1 (pwd) -->
# Introduction au Machine Learning et Deep Learning
En ligne sur [courdier.github.io/ia/](https://courdier.github.io/ia/)

## Slides
1. [Inroduction à l'IA](https://courdier.github.io/ia/pdfs/intro_ia.pdf)
2. [Introduction au Deep Learning pour la Télédétection](https://courdier.github.io/ia/slides/intro.html#p1)
3. [Aspects theoriques du Machine learning et Deep Laerning](https://courdier.github.io/ia/slides/nn.html)
4. [Réseaux de Neurones Convolutionnels](https://courdier.github.io/ia/slides/cnn.html)

## TP 
Pour faire ces TP, vous pouvez utiliser *Google Colab* comme plateforme de travail.  

1. TP1 : 
* Sujet : [Classification d’images satellitaires](https://colab.research.google.com/github/courdier/ia/blob/master/TP/TP_1_GIS.ipynb)
<button onclick="showCustomPrompt()">Correction</button>
<div id="customPrompt" style="display:none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); padding: 20px; background-color: #f0f0f0; border: 1px solid #ccc;">
  <label for="passwordInput">Entrez le mot de passe :</label>
  <input type="password" id="passwordInput">
  <button onclick="checkPassword()">Valider</button>
  <button onclick="closePrompt()">Annuler</button>
</div>
<script>
  function showCustomPrompt() {
    document.getElementById('customPrompt').style.display = 'block';
  }
  function closePrompt() {
    document.getElementById('customPrompt').style.display = 'none';
  }
  function checkPassword() {
    const inputPassword = document.getElementById('passwordInput').value;
    const encodedPassword = '69615f747031'; 
    const encodedUrl = '68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6769746875622f636f7572646965722f69612f626c6f622f6d61737465722f54502f54505f315f4749535f436f727265637465642e6970796e62'

    function toHex(str) {
      return str.split('').map(char => char.charCodeAt(0).toString(16)).join('');
    }
    function toStrFromHex(hex) {
        let str = '';
        for (let i = 0; i < hex.length; i += 2) {
            str += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
        }
        return str;
    }
    if (toHex(inputPassword) === encodedPassword) {
        closePrompt();
        window.location.href = toStrFromHex(encodedUrl);
    } else {
        alert('Mot de passe incorrect.');
    }
  }
</script>

2. TP2 : 
* Sujet : Object detection / counting (Disponible ulterieurement)

## Tests de connaissances

-  [Cours & TP Classification] A venir
<!-- (https://colab.research.google.com/github/courdier/ia/blob/master/Exam1/2023_exam1.ipynb) -->

## Liens web 

- [Techniques for deep learning on satellite and aerial imagery](https://github.com/satellite-image-deep-learning/techniques)
- [Crop type classification with satellite imagery -- Learn about our approach to crop type classification ](https://medium.com/geekculture/crop-type-classification-with-satellite-imagery-dfc200f82927)

### Machines personnelles

Vous pourrez par la suite aussi les faire marcher sur vos machines personnelles.

Il faudra cloner le repertoire github et installer les packages pythons nécessaires:

```sh
git clone https://github.com/courdier/ia && cd ia
pip install -r requirements.txt
```
Vous pouvez ensuite lancer un notebook avec la commande:
```sh
jupyter notebook
```

