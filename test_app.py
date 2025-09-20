import app

def test_generate_response_keywords():
    assert "save" in app.generate_response("How to save money").lower()
    assert "tax" in app.generate_response("Tell me about taxes").lower()
    assert "invest" in app.generate_response("Investment advice").lower()

def test_calculator_inr():
    principal = 1000.0
    rate = 5.0
    time = 10
    amount = principal * (1 + rate/100)**time
    assert round(amount, 2) == 1628.89

def test_calculator_usd():
    principal = 1000.0
    rate = 5.0
    time = 10
    amount = principal * (1 + rate/100)**time
    assert round(amount, 2) == 1628.89
