from .translate_core import TransalteCore
from transformers import MBartForConditionalGeneration, MBartTokenizer
model_repo = "DinhTheBao1997/mbart-for-medical"
lang_code = {
    "tgt": "vi_VN",
}
model = MBartForConditionalGeneration.from_pretrained(model_repo)
tokenizer = MBartTokenizer.from_pretrained(model_repo, tgt_lang=lang_code["tgt"])

split="."
predictions=[]
def clean(v: str):
    return v.strip()

def translate(v: str):
    if v is None or len(v) == 0:
        return ""
    inputs = tokenizer(v, return_tensors="pt")
    translated_tokens = model.generate(**inputs, decoder_start_token_id=tokenizer.lang_code_to_id[lang_code["tgt"]], early_stopping=True, max_length=1024)
    pred = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
    return pred

def seperate(para: str):
    temp=para.split(split)
    return map(clean, temp)

def decode(lst: list[str]):
    return ". ".join(lst).strip()
class CustomModel(TransalteCore):
    def translate_en2vi(raw: str) -> str:
        sentences = seperate(raw)
        t_preds = []
        for sentence in sentences:
            t_preds.append(translate(sentence))
        return decode(t_preds)
