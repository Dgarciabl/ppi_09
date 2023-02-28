from pysentimiento import create_analyzer
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from sentence_transformers import SentenceTransformer


model_str = "mrm8488/bert2bert_shared-spanish-finetuned-summarization"
tokenizer = AutoTokenizer.from_pretrained(model_str)
model = AutoModelForSeq2SeqLM.from_pretrained(model_str)

model_sim = SentenceTransformer('hiiamsid/sentence_similarity_spanish_es')


def found_similuted(text_1, text_2):
    encode = model_sim.encode([text_1, text_2])
    return encode

def generate_summary(text):
   inputs = tokenizer([text], padding="max_length", truncation=True, max_length=512, return_tensors="pt")
   input_ids = inputs.input_ids
   attention_mask = inputs.attention_mask
   output = model.generate(input_ids, attention_mask=attention_mask)
   return tokenizer.decode(output[0], skip_special_tokens=True)


def predict_sentiment(text):
    """Predict sentiment of text"""
    analyzer = create_analyzer(task = "sentiment", lang="es")
    output = analyzer.predict(text)
    return output

def test():
    text_summ = "Gracias presidente por la transparencia y la honestidad con la que se comunica con nosotros, SU PUEBLO, éste que lo ha elegido y al que respetuosamente da explicaciones frente a los dañinos mensajes de los que SIEMPRE nos han engañado. TOTAL APOYO Y CONFIANZA!"
    text = text_summ
    output = predict_sentiment(text)
    summary = generate_summary(text_summ)
    similarity = found_similuted("No me gusta ir mucho a clase", "La clase no es buena")
    print(output)
    print(summary)
    print(similarity)
    


if __name__ == "__main__":
    test()