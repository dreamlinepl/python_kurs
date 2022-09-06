# =============================================================================
# Wykorzystując moduł wbudowany re pozwalający pracować z wyrażeniami regularnymi 
# w Pythonie wydobądź wszystkie cyfry w formie listy z poniższego tekstu:
#     text = 'Python 3.8'
# i wydrukuj do konsoli.
# =============================================================================

    
import re
#%%
text = 'Python 3.8'

print (re.findall("\d", text))

# =============================================================================
# Wykorzystując moduł wbudowany re pozwalający pracować z wyrażeniami regularnymi w Pythonie wydobądź wszystkie znaki nie będące cyfrą w formie listy z poniższego tekstu:
# 
# text = 'Python 3.8'
# i wydrukuj do konsoli.
# 
# =============================================================================

print (re.findall(r'\D', text))
#%%

# =============================================================================
# Wykorzystując moduł wbudowany re pozwalający pracować z wyrażeniami regularnymi w Pythonie wydobądź wszystkie znaki nie będące zerem oraz myślnikiem w formie listy z poniższego kodu:
# 
# code = '0010-000-423'
# i wydrukuj do konsoli.
# =============================================================================

code = '0010-000-423'
print (re.findall(r'[^0-]', code))
#%%
# =============================================================================
# Wykorzystując moduł wbudowany re oraz odpowiednie wyrażenie regularne wydobądź z poniższego kodu:
# 
# code = '0010-000-423-22'
# listę następujących wartości:
# 
# ['0010', '000', '423', '22']
# Wynik wydrukuj do konsoli.
# =============================================================================

code = '0010-000-423-22'
print (re.findall(r'\d+', code))
#%%
# =============================================================================
# Wykorzystując moduł wbudowany re oraz odpowiednie wyrażenie regularne wydobądź z poniższego kodu:
# 
# code = 'PL code: XG-GH-110'
# listę następujących wartości:
# 
# ['PL', '110']
# Wynik wydrukuj do konsoli.
# =============================================================================

code = 'PL code: XG-GH-110'
pattern = r"^\w+|\d+"
print (re.findall(pattern, code))
#%%
# =============================================================================
# Podany jest poniższy tekst:
# Wykorzystując moduł wbudowany re wyciągnij z tekstu html wszystkie tagi w formie listy. Wydrukuj każdy tag w osobnej linii do konsoli.
# =============================================================================
html = """<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>The HTML5 Title</title>
  <meta name="description">

  <link rel="stylesheet" href="css/styles.css?v=1.0">

</head>

<body>
  <script src="js/scripts.js"></script>
</body>
</html>"""
pattern = r"<\w.*"
print (re.findall(pattern, html))

pattern = r"<html lang.*"
print (re.findall(pattern, html))

#%%

text1 = """Python plays a key role in our production pipeline.
Without it a project the size of Star Wars: Episode II would have been very difficult to pull off."""


pattern = r"\w*\s+"
pattern = r"\w+"
print (re.findall(pattern, text))

text = "Please send an email to infdo@template.com or sales-info@template.it"

pattern = r"\w*\@\w*.\w*"
pattern1 = r"[\w\.-]+@[\w\.-]+"
pattern2 = r"[A-Z]\w+"

print (re.findall(pattern, text))
print (re.findall(pattern1, text))
print (re.findall(pattern2, text1))


#%%

message = 'For more information, please call: 123-456-789'
pattern = r"\d{3}-\d{3}-\d{3}"
print (re.findall(pattern, message))

pattern =r"\d{3}"
print(re.sub(pattern, "***", message))














