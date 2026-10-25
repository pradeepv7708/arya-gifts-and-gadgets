# Arya Gifts & Gadgets — Flask demo storefront

## Requirements
- Python 3.10 or newer
- Internet connection for Google Fonts and the sample product images

## Run in VS Code (Ubuntu/Linux)
1. Extract this ZIP and open the `lilly_shop_website` folder in VS Code.
2. Open a terminal in that folder.
3. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install Flask:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the website:

   ```bash
   python app.py
   ```

6. Open http://127.0.0.1:5000 in your browser.

## What's included
- Responsive Arya Gifts & Gadgets-inspired homepage
- Product cards and search
- Added “Why shop with us?” benefits section for a more polished client preview
- Demo session-based cart
- Demo checkout form and confirmation page
- HTML templates, CSS and JavaScript

## Important notes
- This is a visual/demo recreation based on the supplied screen recording, not the original website source.
- Product photos are loaded from Unsplash URLs and need an internet connection.
- Cart contents use Flask sessions; they are not stored in MySQL.
- Checkout is for demonstration only. It does not collect payments, verify UPI transfers, or save orders in a database.
- Before deploying publicly, set a strong `app.secret_key`, disable debug mode, add validation/CSRF protection, use HTTPS, and connect a proper database and verified payment/order workflow.
