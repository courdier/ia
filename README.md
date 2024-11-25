<!-- ia_tp1 (pwd) -->
<!-- t2024 -->
# Deep Learning for geomatics
En ligne sur [courdier.github.io/ia/](https://courdier.github.io/ia/)

## Slides
1. [Inroduction à l'IA](https://courdier.github.io/ia/pdfs/intro_ia.pdf)
2. [Introduction au Deep Learning pour la Télédétection](https://courdier.github.io/ia/slides/intro.html#p1)
3. [Aspects theoriques du Machine learning et Deep Laerning](https://courdier.github.io/ia/slides/nn.html)
4. [Réseaux de Neurones Convolutionnels](https://courdier.github.io/ia/slides/cnn.html)

## TP
La plateforme de travail utilisée dans ce cours est *Google Colab* .

* Sujet : [Classification d’images satellitaires](https://colab.research.google.com/github/courdier/ia/blob/master/TP/TP_1_GIS.ipynb)
<button onclick="showCustomPrompt('promptTP')">Correction</button>
<div id="promptTP" style="display:none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); padding: 20px; background-color: #f0f0f0; border: 1px solid #ccc;">
  <label for="passwordInputTP">Entrez le mot de passe :</label>
  <input type="password" id="passwordInputTP">
  <button onclick="checkPassword('69615f747031', '68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6769746875622f636f7572646965722f69612f626c6f622f6d61737465722f54502f54505f315f4749535f436f727265637465642e6970796e62', 'passwordInputTP')">Valider</button>
  <button onclick="closePrompt('promptTP')">Annuler</button>
</div>

## Tests de connaissances

-  [tests 2024](https://colab.research.google.com/github/courdier/ia/blob/master/Exam1/2024_exam1.ipynb)
<button onclick="showCustomPrompt('promptTest')">Correction</button>
<div id="promptTest" style="display:none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); padding: 20px; background-color: #f0f0f0; border: 1px solid #ccc;">
  <label for="passwordInputTest">Entrez le mot de passe :</label>
  <input type="password" id="passwordInputTest">
  <button onclick="checkPassword('7432303234', '68747470733A2F2F636F6C61622E72657365617263682E676F6F676C652E636F6D2F6769746875622F636F7572646965722F69612F626C6F622F6D61737465722F4578616D312F323032345F6578616D315F636F7272656374696F6E2E6970796E62', 'passwordInputTest')">Valider</button>
  <button onclick="closePrompt('promptTest')">Annuler</button>
</div>

<script>
  function showCustomPrompt(id) {
    document.getElementById(id).style.display = 'block';
  }

  function closePrompt(id) {
    document.getElementById(id).style.display = 'none';
  }

  function checkPassword(encodedPassword, encodedUrl, inputId) {
    const inputPassword = document.getElementById(inputId).value;

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
      closePrompt(inputId.replace('passwordInput', 'prompt'));
      window.location.href = toStrFromHex(encodedUrl);
    } else {
      alert('Mot de passe incorrect.');
    }
  }
</script>

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