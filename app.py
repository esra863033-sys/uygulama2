from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# *** YAPAY ZEKA API'SI İLE TARİF OLUŞTURMA İŞLEVİ ***
# Gerçek bir projede API anahtarınızı güvenli bir şekilde saklayın!
def generate_ai_recipe(ingredients):
    # Örn: Basitleştirilmiş bir OpenAI/Dil Modeli API çağrısı
    prompt = f"Şu malzemelerle yaratıcı, 5 adımlı ve benzersiz bir tarif oluştur: {', '.join(ingredients)}. Tarifin adı, kısa bir hikayesi ve besin değeri özeti olsun."
    
    # Gerçek API çağrısı yerine basitleştirilmiş bir simülasyon çıktısı:
    # Gerçek projede burada requests.post ile API'ye bağlanılacak.
    mock_response = {
        "title": "Samuray'ın Sırrı: Brokolili Tavuk Wok",
        "story": "Efsaneye göre, bu tarif hızlı enerjiye ihtiyacı olan bir samuray için...",
        "steps": [
            "Tavuğu soya sosu ve zencefille marine edin.",
            "Wok'ta yüksek ateşte tavukları kızartın.",
            "Brokoli ve pirinci ekleyip karıştırın.",
            "Özel sosu (bal, sarımsak) ekleyip 2 dakika pişirin.",
            "Sıcak servis edin."
        ],
        "nutritional_summary": "Yüksek protein, düşük karbonhidrat."
    }
    return mock_response

@app.route('/', methods=['GET', 'POST'])
def index():
    recipe_data = None
    if request.method == 'POST':
        # Formdan malzemeleri al
        ingredients_input = request.form.get('ingredients')
        ingredients_list = [i.strip() for i in ingredients_input.split(',')]
        
        # AI destekli tarifi oluştur
        recipe_data = generate_ai_recipe(ingredients_list)
        
    return render_template('index.html', recipe=recipe_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
