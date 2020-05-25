pip install --upgrade "ibm-watson>=4.2.1"
import requests
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('xx')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
print(type(language_translator))

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/ad0baccc-1587-4c3c-aeba-9bdd06e96161')

translation = language_translator.translate(
    text='Hello',
    model_id='en-es').get_result()
print(translation['translations'][0]['translation'])

import requests
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
while True:
    try:
        _inputtext_ = input('Please input the language you want to translate:')
        language = language_translator.identify(_inputtext_).get_result()
        if language['languages'][0]['language'] == 'en':
            break
        else:
            raise ValueError
    except ValueError:
        print('We can only translate from English')
        continue
        
def Translator(x):
    
    authenticator = IAMAuthenticator('Xxx')
    language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
    language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/ad0baccc-1587-4c3c-aeba-9bdd06e96161')
    translation = language_translator.translate(text=x,model_id='en-es').get_result()
    _answer_ = json.dumps(translation, indent=2)["translations"][0]["translation"]
    return print('The translation:', _answer_))
print(Translator(_inputtext_))

import requests
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
_inputtext_ = input('Please input the language you want to translate:')
language = language_translator.identify(_inputtext_).get_result()
print(language)

import requests
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
while True:
    try:
        _inputtext_ = input('Please input the textyou want to translate:')
        _language_ = int(input('Please type in 0:French, 1:Spanish'))
        language = language_translator.identify(_inputtext_).get_result()
        if language['languages'][0]['language'] == 'en':
            if _language_ == 0 or _language_ == 1:
                break
            else:
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        print('We can only translate from English and to French and Spanish')
        continue
        
def Translator(x,y):
    
    authenticator = IAMAuthenticator('XxO7r8R6IIpppV1xL1-9BsrkJwYi60MU9MLQcAKvwo1y')
    language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
    language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/ad0baccc-1587-4c3c-aeba-9bdd06e96161')
    if y == 0:
        translation = language_translator.translate(text=x,model_id='en-fr').get_result()
    elif y == 1:
        translation = language_translator.translate(text=x,model_id='en-es').get_result()
    return print(translation['translations'][0]['translation'])

Translator(_inputtext_, _language_)