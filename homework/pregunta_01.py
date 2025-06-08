# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os
import zipfile
import pandas as pd

import os
import zipfile
import pandas as pd

def pregunta_01():
    # Ruta del archivo ZIP
    zip_path = os.path.join("files", "input.zip")
    destino = os.path.join("files")

    os.makedirs(destino, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(destino)

    print(f"Extracción completada en: {os.path.abspath(destino)}")

    base_input_path = os.path.join("files", "input")
    carpetas = ["train", "test"]
    sentimientos = ["negative", "positive", "neutral"]

    output_path = os.path.join("files", "output")
    os.makedirs(output_path, exist_ok=True)

    for carpeta in carpetas:
        frases = []
        labels = []

        ruta_carpeta = os.path.join(base_input_path, carpeta)

        for sentimiento in sentimientos:
            ruta_sentimiento = os.path.join(ruta_carpeta, sentimiento)
            if not os.path.isdir(ruta_sentimiento):
                continue

            for archivo in os.listdir(ruta_sentimiento):
                if archivo.endswith(".txt"):
                    archivo_path = os.path.join(ruta_sentimiento, archivo)
                    with open(archivo_path, "r", encoding="utf-8") as f:
                        texto = f.read().strip()
                        frases.append(texto)
                        labels.append(sentimiento)

        df = pd.DataFrame({"phrase": frases, "target": labels})  # Aquí renombramos 'sentiment' a 'target'

        archivo_salida = os.path.join(output_path, f"{carpeta}_dataset.csv")
        df.to_csv(archivo_salida, index=False)

    print("Archivos CSV creados en la carpeta 'files/output/'")

pregunta_01()
"""
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


"""
