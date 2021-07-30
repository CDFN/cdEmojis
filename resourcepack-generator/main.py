import os
from os import path
import json
import shutil

emojisPath = "twemoji/assets/72x72/"
resourcepackPath = "resourcepack/assets/cdemojis/"
fontDirPath = resourcepackPath + "font/"
fontTexturesDirPath = resourcepackPath + "textures/font/"

shutil.rmtree(fontDirPath, ignore_errors=True)
shutil.rmtree(fontTexturesDirPath, ignore_errors=True)

os.makedirs(fontDirPath)
os.makedirs(fontTexturesDirPath)

with open('allmoji.json') as emojiFile:
    emojis = json.load(emojiFile)
    lang_file = {
        'providers': []
    }

    for emoji in emojis:
        rawName = f"{emojis[emoji]['img']}.png"
        filePath = emojisPath + rawName
        if not path.exists(filePath):
            continue
        lang_file['providers'].append(
                {
                    "type": "bitmap",
                    "file": "minecraft:font/" + rawName,
                    "ascent": 7,
                    "chars": [chr(int('0x' + string, 0)) for string in
                              emojis[emoji]['codepoints']]
                }
        )
        shutil.copyfile(filePath, fontTexturesDirPath + rawName)

    with open(fontDirPath + 'default.json', 'w') as outfile:
        json.dump(lang_file, outfile, indent=2, ensure_ascii=False)
