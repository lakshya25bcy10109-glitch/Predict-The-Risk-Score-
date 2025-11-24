def predict_risk_score(value, distance, history):
    
    is_high_value = value > 1000.00
    is_international = distance > 5000
    is_new_customer = history < 2

   
    if is_high_value and is_international and is_new_customer:
        return 'extreme'

    elif (is_high_value or is_international) and is_new_customer:
        return 'elevated'
    elif history >= 5 or (not is_international and value < 500):
        return 'low'


    else:
       
        return 'medium'

def determine_transaction_status(risk_score, payment_method):
    """Simulates the Logic Programming Expert System.
    Determines the final transaction action to take which is based on ML Risk Score and Payment Method."""
    risk = risk_score.lower()
    method = payment_method.lower()
    
    if risk == 'extreme':
        action = "Decline Transaction"
        rationale = "Risk exceeds all thresholds. Immediate hard decline to prevent loss."
        
    elif risk == 'elevated' and method in ['paypal', 'apple pay']:
        action = "Hold for Manual Review"
        rationale = "Suspicious, but the payment method provides a layer of security. Hold for human analyst verification (call/email customer)."

 
    elif risk == 'elevated' and method == 'credit card':
        action = "Soft Decline & Challenge"
        rationale = "High risk combined with direct payment. Transaction declined, but initiate a 3D Secure or verification challenge for the user."

    elif risk == 'low':
        action = "Approve"
        rationale = "Risk is negligible. Proceed with standard transaction approval."
        
    else:
        action = "System Default"
        rationale = "Unknown or Medium risk combination. Defaulting to Hold for review."
        
    return action, rationale

def run_system():
    """Runs the full analysis loop."""
    print("AI E-COMMERCE FRAUD DETECTOR--")
    print("Hybrid system using ML risk scoring and rule-based actioning.")
    print("-" * 55)

    try:
        value = float(input("1. Enter Order Value ($USD, e.g., 550.00): ").strip())
        distance = int(input("2. Enter Geo Distance (KM between IP/Billing, e.g., 6000): ").strip())
        history = int(input("3. Enter Historical Purchase Count (e.g., 0): ").strip())
        
        method_input = input("4. Enter Payment Method (Credit Card / PayPal / Apple Pay): ").strip()

        if value < 0 or distance < 0 or history < 0:
            print("\n[ERROR] Inputs must be non-negative numbers.")
            return

        method = method_input 
        risk_score = predict_risk_score(value, distance, history)
  
        action, rationale = determine_transaction_status(risk_score, method)

        print("\n" + "=" * 60)
        print(f"ML FRAUD RISK SCORE:\t{risk_score.upper()}")
        print(f"PAYMENT METHOD:\t\t{method.upper()}")
        print("-" * 60)
        print(f"LP TRANSACTION STATUS:\t{action.upper()}")
        print(f"RATIONALE:\t{rationale}")
        print("=" * 60)

    except ValueError:
        print("\n[ERROR] Please enter valid numbers for the transaction inputs.")
    except Exception as e:
        print(f"\n[SYSTEM ERROR] An unexpected error occurred: {e}")

if __name__ == '__main__':
    run_system()
