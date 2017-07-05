# C Y B E R C A E S A R

Ave!

Heard of Caesar cipher?

It's a simple shift cipher. Just choose the rotation key, and every letter will be cyclically sifted of it's value.

This is an online caesar cipher encryption tool. It's already on the web. [Here.](http://cybercaesar.herokuapp.com/)

### Usage

Left box is for regular text, right one is for encrypted. Choose the rotation key and press encrypt button (right arrow) to see it in action!

Another use case is cipher breaking. You can try to decrypt text without knowing the key. Put it to the encrypted text box (right) and press he "guess key" link. Cyber Ceaser will do frequency analysis and try to define the key.

### Installation

1. Install dependencies using
```
pip install -r requirements.txt
```
2. Deploy static files
```
python manage.py collectstatic
```

3. Run the server using django built-in server or using heroku (already configured with gunicorn)
