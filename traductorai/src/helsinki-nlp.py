lang = "es"
target_lang = "enmodel_name = f'Helsinki-NLP/opus-mt-{lang}-{target_lang}'
# Descargando el modelo y Tokenizar
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)
                
# Tokenizar texto
batch = tokenizer([text], return_tensors="pt", padding=True)
batch["input_ids"] = batch["input_ids"][:, :512]
batch["attention_mask"] = batch["attention_mask"][:, :512]
translation = model.generate(**batch)
tokenizer.batch_decode(translation, skip_special_tokens=True)