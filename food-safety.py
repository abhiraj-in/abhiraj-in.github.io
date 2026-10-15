<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>आहार सत्य | पैकेटबंद भोजन का निष्पक्ष सच</title>
    <style>
        :root {
            --primary: #15803d;
            --primary-dark: #14532d;
            --primary-light: #dcfce7;
            --accent: #eab308;
            --danger: #ef4444;
            --bg: #f8fafc;
            --card-bg: #ffffff;
            --text-dark: #0f172a;
            --text-muted: #64748b;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
        body { background: linear-gradient(180deg, #ecfdf5 0%, #f8fafc 300px); color: var(--text-dark); min-height: 100vh; padding: 18px 12px; display: flex; flex-direction: column; align-items: center; }
        
        .main-container { width: 100%; max-width: 500px; }

        /* Header Style */
        .brand-header { text-align: center; margin-bottom: 22px; }
        .tag-pill { display: inline-flex; align-items: center; gap: 6px; background: #dcfce7; color: var(--primary-dark); padding: 6px 14px; border-radius: 99px; font-size: 12px; font-weight: 800; border: 1px solid #bbf7d0; margin-bottom: 10px; }
        .brand-header h1 { font-size: 32px; font-weight: 900; color: var(--primary-dark); letter-spacing: -0.5px; }
        .brand-header p { font-size: 14px; color: var(--text-muted); margin-top: 6px; line-height: 1.4; }

        /* Cards */
        .card { background: var(--card-bg); border-radius: 18px; padding: 20px; margin-bottom: 16px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.04), 0 8px 10px -6px rgba(0,0,0,0.02); border: 1.5px solid #e2e8f0; }
        .card-label { font-size: 14px; font-weight: 800; color: #1e293b; margin-bottom: 12px; display: flex; align-items: center; gap: 8px; }

        /* Upload Area */
        .upload-zone { border: 2px dashed #86efac; border-radius: 14px; padding: 22px 14px; text-align: center; background: #f0fdf4; cursor: pointer; transition: 0.2s all ease; position: relative; }
        .upload-zone:active { transform: scale(0.99); background: #dcfce7; }
        .upload-zone input { position: absolute; inset: 0; opacity: 0; width: 100%; height: 100%; cursor: pointer; }
        .upload-icon { font-size: 36px; display: block; margin-bottom: 6px; }
        .upload-text { font-size: 14px; font-weight: 700; color: var(--primary-dark); }
        .upload-subtext { font-size: 11px; color: var(--text-muted); margin-top: 3px; }

        #imagePreview { width: 100%; max-height: 220px; object-fit: cover; border-radius: 12px; margin-top: 14px; display: none; border: 2px solid #bbf7d0; }

        /* Input Box */
        .text-input { width: 100%; padding: 14px 16px; border-radius: 12px; border: 1.5px solid #cbd5e1; font-size: 15px; outline: none; transition: 0.2s border; background: #fff; }
        .text-input:focus { border-color: var(--primary); box-shadow: 0 0 0 3px rgba(21,128,61,0.15); }

        /* Quick Test Chips */
        .quick-chips-title { font-size: 12px; font-weight: 700; color: var(--text-muted); margin-top: 10px; margin-bottom: 8px; }
        .chips-list { display: flex; flex-wrap: wrap; gap: 8px; }
        .chip { background: #f1f5f9; border: 1px solid #cbd5e1; padding: 6px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; cursor: pointer; color: #334155; transition: 0.2s; }
        .chip:hover, .chip:active { background: #dcfce7; border-color: #86efac; color: var(--primary-dark); }

        /* Action Button */
        .btn-analyze { width: 100%; background: linear-gradient(135deg, #16a34a 0%, #15803d 100%); color: white; border: none; padding: 16px; border-radius: 14px; font-size: 17px; font-weight: 800; cursor: pointer; box-shadow: 0 10px 20px -3px rgba(22,163,74,0.35); transition: 0.2s transform; display: flex; justify-content: center; align-items: center; gap: 8px; }
        .btn-analyze:active { transform: scale(0.98); }

        /* Animated Loader */
        .loader-box { display: none; background: #ffffff; border-radius: 18px; padding: 26px; text-align: center; border: 1.5px solid #e2e8f0; margin-top: 18px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        .spinner { width: 42px; height: 42px; border: 4px solid #f1f5f9; border-top-color: var(--primary); border-radius: 50%; animation: spin 0.8s linear infinite; margin: 0 auto 12px; }
        @keyframes spin { to { transform: rotate(360deg); } }
        .loader-title { font-size: 15px; font-weight: 800; color: #1e293b; }
        .loader-desc { font-size: 12px; color: var(--text-muted); margin-top: 5px; }

        /* Report Box */
        .report-box { display: none; margin-top: 18px; background: #ffffff; border-radius: 18px; border: 2px solid #86efac; padding: 22px; box-shadow: 0 12px 30px -8px rgba(0,0,0,0.08); }
        .report-header { display: flex; align-items: center; justify-content: space-between; border-bottom: 2px solid #f0fdf4; padding-bottom: 12px; margin-bottom: 16px; }
        .report-header-title { font-size: 19px; font-weight: 900; color: var(--primary-dark); display: flex; align-items: center; gap: 8px; }
        .report-badge { background: #dcfce7; color: var(--primary-dark); font-size: 12px; font-weight: 800; padding: 4px 10px; border-radius: 8px; }
        
        .report-content { font-size: 14.5px; line-height: 1.8; color: #334155; }
        .report-content b { color: #0f172a; font-weight: 800; }
        .report-content ul { padding-left: 20px; margin-top: 8px; }
        .report-content li { margin-bottom: 6px; }

        /* Safety Warning Banner */
        .footer-note { text-align: center; margin-top: 25px; font-size: 12px; color: var(--text-muted); }
    </style>
</head>
<body>

<div class="main-container">
    
    <!-- Header -->
    <div class="brand-header">
        <div class="tag-pill">🌱 जनहित में स्वदेशी स्वास्थ्य पहल</div>
        <h1>आहार सत्य</h1>
        <p>पैकेट के चमकदार दावों के पीछे छुपे केमिकल्स, पामोलीन, और बैन घटकों का निष्पक्ष विश्लेषण</p>
    </div>

    <!-- Image Upload Card -->
    <div class="card">
        <div class="card-label">📸 पैकेट के घटकों (Ingredients) की फोटो खींचें:</div>
        <div class="upload-zone">
            <input type="file" id="foodImage" accept="image/*" capture="environment" onchange="previewSelectedImage(event)">
            <span class="upload-icon">📷</span>
            <div class="upload-text">कैमरा खोलें या गैलरी से फोटो चुनें</div>
            <div class="upload-subtext">पैकेट के पीछे लिखी बारीक सामग्री की साफ फोटो लें</div>
        </div>
        <img id="imagePreview" alt="Food Package Preview">
    </div>

    <!-- Text / Barcode Input Card -->
    <div class="card">
        <div class="card-label">✍️ या किसी भी उत्पाद का नाम / बारकोड लिखें:</div>
        <input type="text" id="productInput" class="text-input" placeholder="उदा. Maggi Masala, Kurkure, Lays, Oreo...">
        
        <div class="quick-chips-title">या तुरंत टेस्ट करने के लिए इनमें से कोई एक चुनें:</div>
        <div class="chips-list">
            <span class="chip" onclick="selectQuickProduct('Maggi 2-Minute Noodles')">🍜 Maggi Noodles</span>
            <span class="chip" onclick="selectQuickProduct('Kurkure Masala Munch')">🌶️ Kurkure</span>
            <span class="chip" onclick="selectQuickProduct('Lays Classic Salted')">🥔 Lays Chips</span>
            <span class="chip" onclick="selectQuickProduct('Cadbury Dairy Milk')">🍫 Dairy Milk</span>
            <span class="chip" onclick="selectQuickProduct('Frooti Mango Drink')">🥭 Frooti</span>
        </div>
    </div>

    <!-- Analyze Button -->
    <button class="btn-analyze" onclick="executeFoodAudit()">
        <span>जांच शुरू करें (सत्य देखें)</span> ➔
    </button>

    <!-- Animated Loading Status -->
    <div class="loader-box" id="loader">
        <div class="spinner"></div>
        <div class="loader-title">रसायनों और घटकों की पड़ताल जारी है...</div>
        <div class="loader-desc">फैक्ट्री प्रोसेस, पामोलीन तेल और विदेशी प्रतिबंध नियमों का मिलान किया जा रहा है</div>
    </div>

    <!-- Dynamic AI Report Card -->
    <div class="report-box" id="reportBox">
        <div class="report-header">
            <div class="report-header-title">
                <span>📋</span> आहार सत्य रिपोर्ट
            </div>
            <div class="report-badge">AI विश्लेषित</div>
        </div>
        <div class="report-content" id="reportContent"></div>
    </div>

    <div class="footer-note">
        आहार सत्य • उपभोक्ता जागरूकता एवं स्वास्थ्य सुरक्षा मंच
    </div>

</div>

<script>
    const API_KEY = "AQ.Ab8RN6I6-SqAi-gBEGpHOfPJNH-Y19nb1iVP_LaFk2ANLJo5Eg";
    let encodedImageBase64 = "";

    function previewSelectedImage(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                const img = document.getElementById('imagePreview');
                img.src = e.target.result;
                img.style.display = 'block';
                encodedImageBase64 = e.target.result.split(',')[1];
            };
            reader.readAsDataURL(file);
        }
    }

    function selectQuickProduct(name) {
        document.getElementById('productInput').value = name;
        executeFoodAudit();
    }

    async function executeFoodAudit() {
        const productText = document.getElementById('productInput').value.trim();
        const loader = document.getElementById('loader');
        const reportBox = document.getElementById('reportBox');
        const reportContent = document.getElementById('reportContent');

        if (!encodedImageBase64 && !productText) {
            alert('कृपया पैकेट की फोटो खींचें, नाम लिखें या नीचे दिए गए किसी उत्पाद पर टच करें!');
            return;
        }

        loader.style.display = 'block';
        reportBox.style.display = 'none';

        try {
            let prompt = "आप एक निष्पक्ष, स्वतंत्र खाद्य विश्लेषक और वैज्ञानिक हैं। उपभोक्ता को इस पैकेज्ड फूड का सच बिना किसी लाग-लपेट के सरल, स्पष्ट हिंदी में समझाएं।\n\n" +
                "रिपोर्ट को इन 5 शीर्षकों में सजाकर दें:\n" +
                "1. 🧪 मुख्य सामग्री और रासायनिक कोड (INS/E Codes): इसमें क्या-क्या मिलाया गया है और उनका असली रासायनिक नाम क्या है?\n" +
                "2. 🛢️ तेल और फैट का सच: इसमें कौन सा तेल (पामोलीन, हाइड्रोजनेटेड फैट आदि) इस्तेमाल हुआ है और वह शरीर की धमनियों पर क्या असर डालता है?\n" +
                "3. 🚫 अंतर्राष्ट्रीय नियम व प्रतिबंध: क्या इसमें कोई ऐसा रसायन या रंग है जो यूरोपीय संघ (EU), अमेरिका या अन्य देशों में प्रतिबंधित या चेतावनी-युक्त है?\n" +
                "4. 💨 पैकेजिंग गैस व प्रिजर्वेटिव्स: पैकेट को महीनों सुरक्षित रखने के लिए क्या डाला गया है?\n" +
                "5. ⚖️ अंतिम निर्णय (स्वास्थ्य रेटिंग): क्या यह बच्चों और परिवार के लिए रोजाना खाने लायक है, या कभी-कभार, या पूरी तरह से परहेज करना चाहिए?";

            let payload = { contents: [{ parts: [] }] };

            if (encodedImageBase64) {
                payload.contents[0].parts.push({
                    inlineData: { mimeType: "image/jpeg", data: encodedImageBase64 }
                });
            }

            if (productText) {
                prompt += `\n\nजांचे जाने वाले उत्पाद का नाम/बारकोड: ${productText}`;
            }

            payload.contents[0].parts.push({ text: prompt });

            const res = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${API_KEY}`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });

            const data = await res.json();
            loader.style.display = 'none';
            reportBox.style.display = 'block';

            if (data.candidates && data.candidates[0].content && data.candidates[0].content.parts[0].text) {
                let markdown = data.candidates[0].content.parts[0].text;
                reportContent.innerHTML = formatMarkdown(markdown);
            } else {
                reportContent.innerHTML = "<p style='color:#ef4444; font-weight: bold;'>⚠️ रिपोर्ट तैयार करने में रुकावट आई। कृपया दोबारा प्रयास करें।</p>";
            }
        } catch (error) {
            loader.style.display = 'none';
            reportBox.style.display = 'block';
            reportContent.innerHTML = `<p style='color:#ef4444; font-weight: bold;'>⚠️ त्रुटि: ${error.message}</p>`;
        }
    }

    function formatMarkdown(text) {
        return text
            .replace(/\*\*(.*?)\*\*/g, '<b>$1</b>')
            .replace(/\*(.*?)\*/g, '<i>$1</i>')
            .replace(/\n\n/g, '<br><br>')
            .replace(/\n/g, '<br>');
    }
</script>

</body>
</html>
